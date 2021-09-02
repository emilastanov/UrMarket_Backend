from .models import Offer
from ariadne import convert_kwargs_to_snake_case
def listOffers_resolver(obj, info):
    try:
        offers = [offer.to_dict() for offer in Offer.query.all()]
        print(offers)
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