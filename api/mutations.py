from api.models import *
from hashlib import sha256
from random import randrange
from api.resolvers import isAuthenticated


@isAuthenticated('admin')
def add_market_resolver(obj, info, value, description):
    market = Market(
        value=value,
        description=description,
        active=False
    )

    db.session.add(market)
    db.session.commit()

    payload = {
        "success": True,
        "market": market.to_dict()
    }

    return payload


@isAuthenticated('admin')
def remove_market_resolver(obj, info, id):
    Market.query.filter(Market.id == id).delete()
    db.session.commit()

    payload = {
        "success": True
    }

    return payload


@isAuthenticated('admin', 'editor')
def add_offer_resolver(obj, info, title, description, logotype, link, rate, amountSymbol,amountMin, amountMax, termMin, termMax,
                       rating, processingTimeMin, processingTimeMax, processingMethods, requirementsAgeMin,
                       requirementsAgeMax, requirementsIncomeProof, requirementsDocuments,
                       requirementsUkrainNationality, isShow, market, requirementsSpecial=None, requirementsIncome=None):
    offer = Offer(
        title=title, description=description, logotype=logotype, link=link, rate=rate, amountSymbol=amountSymbol,amountMin=amountMin,
        amountMax=amountMax, termMin=termMin, termMax=termMax, rating=rating, processingTimeMin=processingTimeMin,
        processingTimeMax=processingTimeMax, processingMethods=processingMethods, requirementsAgeMin=requirementsAgeMin,
        requirementsAgeMax=requirementsAgeMax, requirementsIncome=requirementsIncome,
        requirementsIncomeProof=requirementsIncomeProof, requirementsDocuments=requirementsDocuments,
        requirementsUkrainNationality=requirementsUkrainNationality, requirementsSpecial=requirementsSpecial, isShow=isShow,
        market=market
    )
    db.session.add(offer)
    db.session.commit()
    payload = {
        "success": True,
        "offer": offer.to_dict()
    }

    return payload


@isAuthenticated('admin', 'editor')
def update_offer_resolver(obj, info, id, title=None, description=None, logotype=None, link=None, rate=None, amountSymbol=None, amountMin=None, amountMax=None, termMin=None, termMax=None,
                       rating=None, processingTimeMin=None, processingTimeMax=None, processingMethods=None, requirementsAgeMin=None,
                       requirementsAgeMax=None, requirementsIncomeProof=None, requirementsDocuments=None,
                       requirementsUkrainNationality=None,market=None, requirementsSpecial=None, requirementsIncome=None, isShow=None):

    offer = Offer.query.get(id)
    if isShow is True or isShow is False:
        offer.isShow = isShow
    if title:
        offer.title = title
    if description:
        offer.description = description
    if logotype:
        offer.logotype = logotype
    if market:
        offer.market = market
    if link:
        offer.link = link
    if rate:
        offer.rate = rate
    if amountSymbol:
        offer.amountSymbol = amountSymbol
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


@isAuthenticated('admin', 'editor')
def remove_offer_resolver(obj, info, id):
    Offer.query.filter(Offer.id == id).delete()
    db.session.commit()

    payload = {
        "success": True
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


@isAuthenticated('admin', 'editor')
def add_faq_resolver(obj, info, language, question, answer, market):
    faq = FAQ(
        language=language,
        question=question,
        answer=answer,
        market=market
    )

    db.session.add(faq)
    db.session.commit()

    payload = {
        "success": True,
        "faq": faq.to_dict()
    }

    return payload


@isAuthenticated('admin', 'editor')
def update_faq_resolver(obj, info, id, language=None, question=None, answer=None):
    faq = FAQ.query.get(id)
    if language:
        faq.language = language
    if question:
        faq.question = question
    if answer:
        faq.answer = answer

    db.session.add(faq)
    db.session.commit()

    payload = {
        "success": True,
        "faq": faq.to_dict()
    }

    return payload


@isAuthenticated('admin', 'editor')
def remove_faq_resolver(obj, info, id):
    FAQ.query.filter(FAQ.id == id).delete()
    db.session.commit()

    payload = {
        "success": True
    }

    return payload


def add_review_resolver(obj, info, name, market, text, rating, company):
    if Review.query.filter(Review.text == text).count():
        payload = {
            "success": False,
            "errors": ["Dublicated"]
        }
    else:
        review = Review(name=name, market=market, text=text, rating=rating, company=company)
        db.session.add(review)
        db.session.commit()
        payload = {
            "success": True,
            "review": {
                "id": review.id,
                "text": review.text,
                "rating": review.rating,
                "market": review.market,
                "name": review.name,
                "company": Offer.query.get(review.company)
            }
        }

    return payload


@isAuthenticated('admin', 'editor')
def remove_review_resolver(obj, info, id):
    Review.query.filter(Review.id == id).delete()
    db.session.commit()

    payload = {
        "success": True
    }

    return payload


@isAuthenticated('admin', 'editor')
def add_content_resolver(obj, info, logotype, language, market, title, metaTitle, metaDescription, metaKeywords, header,
               description, calcAmountLabel, calcAmountPlaceholder,calcButton, calcTermLabel, calcTermPlaceholder, adsParagraph,
               adsImage, filterHeader, filterAmount, filterTerm, filterRate, filterPopular, footerParagraph,
               footerPartnersHeader, topTitle, footerLegalAddress, topTableColumnAmount,topTableColumnCompany, topTableColumnTerm,
               topTableColumnRate, reviewHeader, reviewFormName, reviewFormSelectOrganization,
               reviewFormInputPlaceholder, reviewFormRating, reviewFormButton, reviewSuccessMessage, reviewListHeader,
               reviewListLoader,offerAmount, offerTime , offerTimeUnits, offerTermUnits, offerRateUnits, offerTerm, offerRate, offerButton,faqHeader):
    content = Content(logotype=logotype, language=language, market=market, title=title, metaTitle=metaTitle,
                      metaDescription=metaDescription, metaKeywords=metaKeywords, header=header,
                      description=description, calcAmountLabel=calcAmountLabel,
                      calcAmountPlaceholder=calcAmountPlaceholder,calcButton=calcButton, calcTermLabel=calcTermLabel,
                      calcTermPlaceholder=calcTermPlaceholder, adsParagraph=adsParagraph, adsImage=adsImage,
                      filterHeader=filterHeader, filterAmount=filterAmount, filterTerm=filterTerm,
                      filterRate=filterRate, filterPopular=filterPopular, footerParagraph=footerParagraph,
                      footerPartnersHeader=footerPartnersHeader, topTitle=topTitle,
                      footerLegalAddress=footerLegalAddress,topTableColumnCompany=topTableColumnCompany, topTableColumnAmount=topTableColumnAmount,
                      topTableColumnTerm=topTableColumnTerm, topTableColumnRate=topTableColumnRate,
                      reviewHeader=reviewHeader, reviewFormName=reviewFormName,
                      reviewFormSelectOrganization=reviewFormSelectOrganization,
                      reviewFormInputPlaceholder=reviewFormInputPlaceholder,
                      reviewFormRating=reviewFormRating, reviewFormButton=reviewFormButton,
                      reviewSuccessMessage=reviewSuccessMessage, reviewListHeader=reviewListHeader,
                      reviewListLoader=reviewListLoader,offerAmount=offerAmount, offerTime=offerTime ,
                      offerTimeUnits=offerTimeUnits, offerTermUnits=offerTermUnits, offerRateUnits=offerRateUnits,
                      offerTerm=offerTerm, offerRate=offerRate, offerButton=offerButton, faqHeader=faqHeader)

    db.session.add(content)
    db.session.commit()

    payload = {
        "success": True,
        "content": content
    }

    return payload


@isAuthenticated('admin', 'editor')
def update_content_resolver(obj, info, id, logotype=None, language=None, market=None, title=None, metaTitle=None,
                            metaDescription=None, metaKeywords=None, header=None, description=None,
                            calcAmountLabel=None, calcAmountPlaceholder=None,calcButton=None, calcTermLabel=None,
                            calcTermPlaceholder=None, adsParagraph=None, adsImage=None, filterHeader=None,
                            filterAmount=None, filterTerm=None, filterRate=None, filterPopular=None,
                            footerParagraph=None, footerPartnersHeader=None, topTitle=None, footerLegalAddress=None,
                            topTableColumnAmount=None, topTableColumnTerm=None,topTableColumnCompany=None, topTableColumnRate=None,
                            reviewHeader=None, reviewFormName=None, reviewFormSelectOrganization=None,
                            reviewFormInputPlaceholder=None, reviewFormRating=None, reviewFormButton=None,
                            reviewSuccessMessage=None, reviewListHeader=None, reviewListLoader=None,offerAmount=None,
                            offerTime=None , offerTimeUnits=None, offerTermUnits=None, offerRateUnits=None, offerTerm=None,
                            offerRate=None, offerButton=None, faqHeader=None):

    content = Content.query.get(id)
    if faqHeader:
        content.faqHeader = faqHeader
    if logotype:
        content.logotype = logotype
    if offerAmount:
        content.offerAmount = offerAmount
    if offerTime:
        content.offerTime = offerTime
    if offerTimeUnits:
        content.offerTimeUnits = offerTimeUnits
    if offerTermUnits:
        content.offerTermUnits = offerTermUnits
    if  offerRateUnits:
        content.offerRateUnits = offerRateUnits
    if offerTerm:
        content.offerTerm = offerTerm
    if offerRate:
        content.offerRate = offerRate
    if offerButton:
        content.offerButton = offerButton
    if language:
        content.language = language
    if market:
        content.market = market
    if title:
        content.title = title
    if metaTitle:
        content.metaTitle = metaTitle
    if metaDescription:
        content.metaDescription = metaDescription
    if metaKeywords:
        content.metaKeywords = metaKeywords
    if header:
        content.header = header
    if description:
        content.description = description
    if calcButton:
        content.calcButton = calcButton
    if calcAmountLabel:
        content.calcAmountLabel = calcAmountLabel
    if calcAmountPlaceholder:
        content.calcAmountPlaceholder = calcAmountPlaceholder
    if calcTermLabel:
        content.calcTermLabel = calcTermLabel
    if calcTermPlaceholder:
        content.calcTermPlaceholder = calcTermPlaceholder
    if adsParagraph:
        content.adsParagraph = adsParagraph
    if adsImage:
        content.adsImage = adsImage
    if filterHeader:
        content.filterHeader = filterHeader
    if filterAmount:
        content.filterAmount = filterAmount
    if filterTerm:
        content.filterTerm = filterTerm
    if filterRate:
        content.filterRate = filterRate
    if filterPopular:
        content.filterPopular = filterPopular
    if footerParagraph:
        content.footerParagraph = footerParagraph
    if footerPartnersHeader:
        content.footerPartnersHeader = footerPartnersHeader
    if topTitle:
        content.topTitle = topTitle
    if footerLegalAddress:
        content.footerLegalAddress = footerLegalAddress
    if topTableColumnAmount:
        content.topTableColumnAmount = topTableColumnAmount
    if topTableColumnCompany:
        content.topTableColumnCompany = topTableColumnCompany
    if topTableColumnTerm:
        content.topTableColumnTerm = topTableColumnTerm
    if topTableColumnRate:
        content.topTableColumnRate = topTableColumnRate
    if reviewHeader:
        content.reviewHeader = reviewHeader
    if reviewFormName:
        content.reviewFormName = reviewFormName
    if reviewFormSelectOrganization:
        content.reviewFormSelectOrganization = reviewFormSelectOrganization
    if reviewFormInputPlaceholder:
        content.reviewFormInputPlaceholder = reviewFormInputPlaceholder
    if reviewFormRating:
        content.reviewFormRating = reviewFormRating
    if reviewFormButton:
        content.reviewFormButton = reviewFormButton
    if reviewSuccessMessage:
        content.reviewSuccessMessage = reviewSuccessMessage
    if reviewListHeader:
        content.reviewListHeader = reviewListHeader
    if reviewListLoader:
        content.reviewListLoader = reviewListLoader

    db.session.commit()

    payload = {
        "success": True,
        "content": content
    }

    return payload


@isAuthenticated('admin', 'editor')
def remove_content_resolver(obj, info, id):
    Content.query.filter(Content.id == id).delete()
    db.session.commit()

    payload = {
        "success": True
    }

    return payload


@isAuthenticated('admin','editor')
def add_credit_card_offer_resolver(
        obj,
        info,
        title,
        logotype,
        isShow,
        market,
        rating,
        link,
        description,
        gracePeriod,
        rate,
        servicePayment,
        creditLimit,
        creditDocs,
        ageMin,
        ageMax,
        onlyIndividual,
        minimumWorkExperience,
        minimumCurrentWorkExperience,
        salaryMinimumSalary,
        salaryMinimumSalaryMainRegions,
        salaryMainRegions,
        cashFee,
        cardType
):
    offer = CreditCardOffer(
        title=title,
        logotype=logotype,
        isShow=isShow,
        rating=rating,
        market=market,
        link=link,
        description=description,
        gracePeriod=gracePeriod,
        rate=rate,
        servicePayment=servicePayment,
        creditLimit=creditLimit,
        creditDocs=creditDocs,
        ageMin=ageMin,
        ageMax=ageMax,
        onlyIndividual=onlyIndividual,
        minimumWorkExperience=minimumWorkExperience,
        minimumCurrentWorkExperience=minimumCurrentWorkExperience,
        salaryMinimumSalary=salaryMinimumSalary,
        salaryMinimumSalaryMainRegions=salaryMinimumSalaryMainRegions,
        salaryMainRegions=salaryMainRegions,
        cashFee=cashFee,
        cardType=cardType

    )
    db.session.add(offer)
    db.session.commit()
    payload = {
        "success": True,
        "credit_card": offer.to_dict()
    }

    return payload


@isAuthenticated('admin','editor')
def update_credit_card_offer_resolver(
        obj,
        info,
        id,
        title=None,
        logotype=None,
        isShow=None,
        rating=None,
        market=None,
        link=None,
        description=None,
        gracePeriod=None,
        rate=None,
        servicePayment=None,
        creditLimit=None,
        creditDocs=None,
        ageMin=None,
        ageMax=None,
        onlyIndividual=None,
        minimumWorkExperience=None,
        minimumCurrentWorkExperience=None,
        salaryMinimumSalary=None,
        salaryMinimumSalaryMainRegions=None,
        salaryMainRegions=None,
        cashFee=None,
        cardType=None
):
    offer = CreditCardOffer.query.get(id)
    if cashFee:
        offer.cashFee = cashFee
    if cardType:
        offer.cardType = cardType
    if title:
        offer.title = title
    if rating:
        offer.rating = rating
    if logotype:
        offer.logotype = logotype
    if isShow:
        offer.isShow = isShow
    if market:
        offer.market = market
    if link:
        offer.link = link
    if description:
        offer.description = description
    if gracePeriod:
        offer.gracePeriod = gracePeriod
    if rate:
        offer.rate = rate
    if servicePayment:
        offer.servicePayment = servicePayment
    if creditLimit:
        offer.creditLimit = creditLimit
    if creditDocs:
        offer.creditDocs = creditDocs
    if ageMin:
        offer.ageMin = ageMin
    if ageMax:
        offer.ageMax = ageMax
    if onlyIndividual:
        offer.onlyIndividual = onlyIndividual
    if minimumWorkExperience:
        offer.minimumWorkExperience = minimumWorkExperience
    if minimumCurrentWorkExperience:
        offer.minimumCurrentWorkExperience = minimumCurrentWorkExperience
    if salaryMinimumSalary:
        offer.salaryMinimumSalary = salaryMinimumSalary
    if salaryMinimumSalaryMainRegions:
        offer.salaryMinimumSalaryMainRegions = salaryMinimumSalaryMainRegions
    if salaryMainRegions:
        offer.salaryMainRegions = salaryMainRegions

    db.session.commit()

    payload = {
        "success": True,
        "credit_card": offer
    }

    return payload


@isAuthenticated('admin', 'editor')
def remove_credit_card_offer_resolver(obj, info, id):
    CreditCardOffer.query.filter(CreditCardOffer.id == id).delete()
    db.session.commit()

    payload = {
        "success": True
    }

    return payload


def add_credit_card_review_resolver(obj, info, name, market, text, rating, card):
    if CreditCardReview.query.filter(CreditCardReview.text == text).count():
        payload = {
            "success": False,
            "errors": ["Dublicated"]
        }
    else:
        review = CreditCardReview(name=name, market=market, text=text, rating=rating, card=card)
        db.session.add(review)
        db.session.commit()
        payload = {
            "success": True,
            "review": {
                "id": review.id,
                "text": review.text,
                "rating": review.rating,
                "market": review.market,
                "name": review.name,
                "card": CreditCardOffer.query.get(review.card)
            }
        }

    return payload


@isAuthenticated('admin', 'editor')
def remove_credit_card_review_resolver(obj, info, id):
    CreditCardReview.query.filter(CreditCardReview.id == id).delete()
    db.session.commit()

    payload = {
        "success": True
    }

    return payload