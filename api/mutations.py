from api.models import *
from hashlib import sha256
from random import randrange
from api.resolvers import isAuthenticated


@isAuthenticated('admin', 'editor')
def add_offer_resolver(obj, info, title, description, logotype, link, rate, amountMin, amountMax, termMin, termMax,
                       rating, processingTimeMin, processingTimeMax, processingMethods, requirementsAgeMin,
                       requirementsAgeMax, requirementsIncomeProof, requirementsDocuments,
                       requirementsUkrainNationality, requirementsSpecial=None, requirementsIncome=None):
    offer = Offer(
        title=title, description=description, logotype=logotype, link=link, rate=rate, amountMin=amountMin,
        amountMax=amountMax, termMin=termMin, termMax=termMax, rating=rating, processingTimeMin=processingTimeMin,
        processingTimeMax=processingTimeMax, processingMethods=processingMethods, requirementsAgeMin=requirementsAgeMin,
        requirementsAgeMax=requirementsAgeMax, requirementsIncome=requirementsIncome,
        requirementsIncomeProof=requirementsIncomeProof, requirementsDocuments=requirementsDocuments,
        requirementsUkrainNationality=requirementsUkrainNationality, requirementsSpecial=requirementsSpecial
    )
    db.session.add(offer)
    db.session.commit()
    payload = {
        "success": True,
        "offer": offer.to_dict()
    }

    return payload


@isAuthenticated('admin', 'editor')
def update_offer_resolver(obj, info, id, title=None, description=None, logotype=None, link=None, rate=None, amountMin=None, amountMax=None, termMin=None, termMax=None,
                       rating=None, processingTimeMin=None, processingTimeMax=None, processingMethods=None, requirementsAgeMin=None,
                       requirementsAgeMax=None, requirementsIncomeProof=None, requirementsDocuments=None,
                       requirementsUkrainNationality=None, requirementsSpecial=None, requirementsIncome=None):

    offer = Offer.query.get(id)
    if title:
        offer.title = title
    if description:
        offer.description = description
    if logotype:
        offer.logotype = logotype
    if link:
        offer.link = link
    if rate:
        offer.rate = rate
    if amountMin:
        offer.amountMin = amountMin
    if amountMax:
        offer.amountMax = amountMax
    if termMin:
        offer.termMin = termMin
    if termMax:
        offer.termMax = termMax
    if rating:
        offer.rating = rating
    if processingTimeMin:
        offer.processingTimeMin = processingTimeMin
    if processingTimeMax:
        offer.processingTimeMax = processingTimeMax
    if processingMethods:
        offer.processingMethods = processingMethods
    if requirementsAgeMin:
        offer.requirementsAgeMin = requirementsAgeMin
    if requirementsAgeMax:
        offer.requirementsAgeMax = requirementsAgeMax
    if requirementsIncome:
        offer.requirementsIncome = requirementsIncome
    if requirementsIncomeProof:
        offer.requirementsIncomeProof = requirementsIncomeProof
    if requirementsDocuments:
        offer.requirementsDocuments = requirementsDocuments
    if requirementsUkrainNationality:
        offer.requirementsUkrainNationality = requirementsUkrainNationality
    if requirementsSpecial:
        offer.requirementsSpecial = requirementsSpecial

    db.session.commit()
    payload = {
        "success": True,
        "offer": offer.to_dict()
    }

    return payload


def genKey():
    k = ""
    u = 1
    while u != 0:
        k = sha256(str(randrange(1, 10 ** 10)).encode('utf-8')).hexdigest()
        u = AuthKey.query.filter(AuthKey.key == k).count()
    return k


@isAuthenticated('admin')
def add_user_resolver(obj,info,permission, name=None):
    user = AuthKey(
        name=name,
        permission=permission,
        key=genKey()
    )
    db.session.add(user)
    db.session.commit()

    payload = {
        "success": True,
        "user": user.to_dict()
    }

    return payload


@isAuthenticated('admin')
def remove_user_resolver(obj,info,id):
    AuthKey.query.filter(AuthKey.id == id).delete()
    db.session.commit()

    payload = {
        "success": True
    }

    return payload


@isAuthenticated('admin')
def update_user_resolver(obj, info, id,name):
    user = AuthKey.query.get(id)
    user.name = name
    db.session.commit()

    payload = {
        "success": True,
        "user": user.to_dict()
    }

    return payload

