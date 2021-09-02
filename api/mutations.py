from api.models import *


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
