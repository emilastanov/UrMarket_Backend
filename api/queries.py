from .models import *
from ariadne import convert_kwargs_to_snake_case
from .resolvers import isAuthenticated

def listOffers_resolver(obj, info):
    try:
        offers = [offer.to_dict() for offer in Offer.query.all()]
        payload = {
            "success": True,
            "offers": offers
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getOffer_resolver(obj, info, id):
    try:
        offer = Offer.query.get(id)
        print(offer.to_dict())
        payload = {
            "success": True,
            "offer": offer.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload


@isAuthenticated('admin')
def listUsers_resolver(obj,info):
    try:
        users = [user.to_dict() for user in AuthKey.query.all()]
        payload = {
            "success": True,
            "users": users
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@isAuthenticated('editor', 'admin')
def getUser_resolver(obj, info, id):
    try:
        user = AuthKey.query.get(id)
        payload = {
            "success": True,
            "user": user.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload
