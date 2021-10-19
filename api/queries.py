from .models import *
from ariadne import convert_kwargs_to_snake_case
from .resolvers import isAuthenticated


def listOffers_resolver(obj, info, market, main=False):
    try:
        if main:
            offers = [offer.to_dict() for offer in
                      Offer.query.filter(Offer.market == market).filter(Offer.isShow == True)]
        else:
            offers = [offer.to_dict() for offer in Offer.query.filter(Offer.market == market)]
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


def login_resolver(obj, info, key):
    try:
        user = AuthKey.query.filter(AuthKey.key == key)
        if user.count() == 0:
            payload = {
                "success": False,
                "errors": ["Bad auth key"]
            }
        else:
            payload = {
                "success": True,
                "user": user.first().to_dict()
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

        payload = {
            "success": True,
            "offer": offer.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Post item matching {id} not found"]
        }
    return payload


@isAuthenticated('admin')
def listUsers_resolver(obj, info):
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


def listFAQ_resolver(obj, info, language=None, market=None):
    try:
        if language and market:
            faqs = [faq.to_dict() for faq in FAQ.query.filter(FAQ.language == language).filter(FAQ.market == market)]
        else:
            faqs = [faq.to_dict() for faq in FAQ.query.all()]
        payload = {
            "success": True,
            "list_faq": faqs
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def listReviews_resolver(obj, info, market=None):
    try:
        if market:
            reviews = [review.to_dict() for review in
                       Review.query.filter(Review.market == market).order_by(Review.id.desc())]
        else:
            reviews = [review.to_dict() for review in Review.query.all().order_by(Review.id.desc())]
        payload = {
            "success": True,
            "reviews": reviews
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def getContent_resolver(obj, info, market, language):
    try:
        content = Content.query.filter(Content.market == market).filter(Content.language == language).first()
        payload = {
            "success": True,
            "content": content.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload


def listContent_resolver(obj, info, market):
    try:
        contents = [content.to_dict() for content in Content.query.filter(Content.market == market)]
        payload = {
            "success": True,
            "contents": contents
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload


def listMarkets_resolver(obj, info):
    try:
        markets = [market.to_dict() for market in Market.query.all()]
        payload = {
            "success": True,
            "markets": markets
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload


def listCreditCardOffers_resolver(obj, info, market, main=False):
    try:
        credit_cards = [
            creditCard.to_dict() for creditCard in CreditCardOffer.query.filter(
                CreditCardOffer.market == market
            ).filter(
                CreditCardOffer.isShow == True
            )
        ] if main else [
            creditCard.to_dict() for creditCard in CreditCardOffer.query.filter(
                CreditCardOffer.market == market
            )
        ]
        payload = {
            "success": True,
            "credit_cards": credit_cards
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload


def getCreditCardOffer_resolver(obj, info, id):
    try:
        credit_card = CreditCardOffer.query.get(id)

        payload = {
            "success": True,
            "credit_card": credit_card.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Post item matching {id} not found"]
        }
    return payload


def listCreditCardReviews_resolver(obj, info, market=None):
    try:
        if market:
            reviews = [review.to_dict() for review in
                       CreditCardReview.query.filter(CreditCardReview.market == market).order_by(CreditCardReview.id.desc())]
        else:
            reviews = [review.to_dict() for review in CreditCardReview.query.all().order_by(CreditCardReview.id.desc())]
        payload = {
            "success": True,
            "reviews": reviews
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def getCreditCardFilters_resolver(obj, info, market):
    try:
        creditCards = [creditCard.to_dict() for creditCard in CreditCardOffer.query.filter(CreditCardOffer.market == market)]
        cardTypes = []
        for creditCard in creditCards:
            if not creditCard['card_type'] in cardTypes:
                cardTypes.append(creditCard['card_type'])
        cardGracePeriods = [creditCard['grace_period'] for creditCard in creditCards]
        gracePeriod = {
            "min": min(cardGracePeriods),
            "max": max(cardGracePeriods)
        }
        cardAmounts = [creditCard['credit_limit'] for creditCard in creditCards]
        amount = {
            "min": min(cardAmounts),
            "max": max(cardAmounts)
        }
        payload = {
            "success": True,
            "filters": {
                "amount": amount,
                "grace_period": gracePeriod,
                "card_types": cardTypes
            }
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
