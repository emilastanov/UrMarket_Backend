import json

from api import db
from sqlalchemy.orm import relationship,backref


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    market = db.Column(db.String)
    title = db.Column(db.String)
    logotype = db.Column(db.String)
    description = db.Column(db.Text)
    link = db.Column(db.String)
    isShow = db.Column(db.Boolean, default=False)
    rate = db.Column(db.Float)
    termMin = db.Column(db.Integer)
    termMax = db.Column(db.Integer)
    amountMin = db.Column(db.Integer)
    amountMax = db.Column(db.Integer)
    amountSymbol = db.Column(db.String)
    rating = db.Column(db.Integer)
    processingTimeMin = db.Column(db.Integer)
    processingTimeMax = db.Column(db.Integer)
    processingMethods = db.Column(db.Text)
    requirementsAgeMin = db.Column(db.Integer)
    requirementsAgeMax = db.Column(db.Integer)
    requirementsIncome = db.Column(db.Integer)
    requirementsIncomeProof = db.Column(db.Boolean)
    requirementsDocuments = db.Column(db.Text)
    requirementsUkrainNationality = db.Column(db.Boolean)
    requirementsSpecial = db.Column(db.Text)
    child = relationship("Review", backref="parent", passive_deletes=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "market": self.market,
            "logotype": self.logotype,
            "description": self.description,
            "is_show": self.isShow,
            "link": self.link,
            "rate": self.rate,
            "term": {
                "min": self.termMin,
                "max": self.termMax
            },
            "amount": {
                "min": self.amountMin,
                "max": self.amountMax,
                "symbol": self.amountSymbol
            },
            "rating": self.rating,
            "processing_time": {
                "min": self.processingTimeMin,
                "max": self.processingTimeMax
            },
            "processing_methods": self.processingMethods.split(","),
            "requirements": {
                "age": {
                    "min": self.requirementsAgeMin,
                    "max": self.requirementsAgeMax
                },
                "income": self.requirementsIncome,
                "income_proof": self.requirementsIncomeProof,
                "documents": self.requirementsDocuments.split(","),
                "ukrain_nationality": self.requirementsUkrainNationality,
                "special": self.requirementsSpecial
            }
        }


class AuthKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String)
    name = db.Column(db.String)
    permission = db.Column(db.String) #admin | editor

    def to_dict(self):
        return {
            "id": self.id,
            "key": self.key,
            "name": self.name,
            "permission": self.permission
        }


class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    market = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "language": self.language,
            "market": self.market,
            "question": self.question,
            "answer": self.answer
        }


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logotype = db.Column(db.String)
    language = db.Column(db.String)
    market = db.Column(db.String)
    title = db.Column(db.String)
    metaTitle = db.Column(db.String)
    metaDescription = db.Column(db.String)
    metaKeywords = db.Column(db.String)
    header = db.Column(db.String)
    description = db.Column(db.String)
    calcAmountLabel = db.Column(db.String)
    calcAmountPlaceholder = db.Column(db.String)
    calcTermLabel = db.Column(db.String)
    calcTermPlaceholder = db.Column(db.String)
    calcButton = db.Column(db.String)
    adsParagraph = db.Column(db.String)
    adsImage = db.Column(db.String)
    filterHeader = db.Column(db.String)
    filterAmount = db.Column(db.String)
    filterTerm = db.Column(db.String)
    filterRate = db.Column(db.String)
    filterPopular = db.Column(db.String)
    footerParagraph = db.Column(db.String)
    footerPartnersHeader = db.Column(db.String)
    topTitle = db.Column(db.String)
    footerLegalAddress = db.Column(db.String)
    topTableColumnCompany = db.Column(db.String)
    topTableColumnAmount = db.Column(db.String)
    topTableColumnTerm = db.Column(db.String)
    offerAmount = db.Column(db.String)
    offerTime = db.Column(db.String)
    offerTimeUnits = db.Column(db.String)
    offerTermUnits = db.Column(db.String)
    offerRateUnits = db.Column(db.String)
    offerTerm = db.Column(db.String)
    offerRate = db.Column(db.String)
    offerButton = db.Column(db.String)
    topTableColumnRate = db.Column(db.String)
    reviewHeader = db.Column(db.String)
    reviewFormName = db.Column(db.String)
    reviewFormSelectOrganization = db.Column(db.String)
    reviewFormInputPlaceholder = db.Column(db.String)
    reviewFormRating = db.Column(db.String)
    reviewFormButton = db.Column(db.String)
    reviewSuccessMessage = db.Column(db.String)
    reviewListHeader = db.Column(db.String)
    reviewListLoader = db.Column(db.String)
    faqHeader = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "language": self.language,
            "market": self.market,
            "logotype": self.logotype,
            "title": self.title,
            "header": self.header,
            "description": self.description,
            "meta": {
                "title": self.metaTitle,
                "description": self.metaDescription,
                "keywords": self.metaKeywords
            },
            "calc": {
                "amount": {
                    "label": self.calcAmountLabel,
                    "placeholder": self.calcAmountPlaceholder,
                },
                "term": {
                    "label": self.calcTermLabel,
                    "placeholder": self.calcTermPlaceholder
                },
                "button": self.calcButton
            },
            "ads": {
                "paragraph": self.adsParagraph,
                "image": self.adsImage
            },
            "filter": {
                "header": self.filterHeader,
                "amount": self.filterAmount,
                "term": self.filterTerm,
                "rate": self.filterRate,
                "popular": self.filterPopular
            },
            "footer": {
                "paragraph": self.footerParagraph,
                "partners_header": self.footerPartnersHeader,
                "legal_address": self.footerLegalAddress
            },
            "top": {
                "title": self.topTitle,
                "table_columns": {
                    "amount": self.topTableColumnAmount,
                    "term": self.topTableColumnTerm,
                    "rate": self.topTableColumnRate,
                    "company": self.topTableColumnCompany
                }
            },
            "offer": {
                "amount": self.offerAmount,
                "button": self.offerButton,
                "time": {
                    "title": self.offerTime,
                    "units": self.offerTimeUnits
                },
                "term": {
                    "title": self.offerTerm,
                    "units": self.offerTermUnits
                },
                "rate": {
                    "title": self.offerRate,
                    "units": self.offerRateUnits
                }
            },
            "review": {
                "header": self.reviewHeader,
                "form": {
                    "name": self.reviewFormName,
                    "select_organization": self.reviewFormSelectOrganization,
                    "input_placeholder": self.reviewFormInputPlaceholder,
                    "rating": self.reviewFormRating,
                    "button": self.reviewFormButton
                },
                "success_message": self.reviewSuccessMessage,
                "list": {
                    "header": self.reviewListHeader,
                    "loader": self.reviewListLoader
                }
            },
            "faq_header": self.faqHeader
        }


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    text = db.Column(db.Text, unique=True)
    rating = db.Column(db.Integer)
    company = db.Column(db.Integer, db.ForeignKey(Offer.id, ondelete='CASCADE'))
    market = db.Column(db.String)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "market": self.market,
            "text": self.text,
            "rating": self.rating,
            "company": Offer.query.get(self.company).to_dict()
        }


class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    description = db.Column(db.String)
    active = db.Column(db.Boolean)

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "description": self.description,
            "active": self.active
        }


class CreditCardOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    logotype = db.Column(db.String)
    isShow = db.Column(db.Boolean)
    rating = db.Column(db.Integer)
    market = db.Column(db.String)
    amountSymbol = db.Column(db.String)
    link = db.Column(db.String)
    description = db.Column(db.String)
    gracePeriod = db.Column(db.Integer)
    rate = db.Column(db.String)
    servicePayment = db.Column(db.Integer)
    creditLimit = db.Column(db.Integer)
    creditDocs = db.Column(db.String)
    ageMin = db.Column(db.Integer)
    ageMax = db.Column(db.Integer)
    onlyIndividual = db.Column(db.Boolean)
    minimumWorkExperience = db.Column(db.Integer)
    minimumCurrentWorkExperience = db.Column(db.Integer)
    salaryMinimumSalary = db.Column(db.Integer)
    salaryMinimumSalaryMainRegions = db.Column(db.Integer)
    salaryMainRegions = db.Column(db.String)
    cardType = db.Column(db.String)
    cashWithdrawal = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "card_type": self.cardType,
            "cash_withdrawal": self.cashWithdrawal,
            "title": self.title,
            "logotype": self.logotype,
            "amount_symbol": self.amountSymbol,
            "link": self.link,
            "rating": self.rating,
            "is_show": self.isShow,
            "market": self.market,
            "description": self.description,
            "grace_period": self.gracePeriod,
            "rate": self.rate,
            "service_payment": self.servicePayment,
            "credit_limit": self.creditLimit,
            "credit_docs": self.creditDocs,
            "age": {
                "min": self.ageMin,
                "max": self.ageMax
            },
            "only_individual": self.onlyIndividual,
            "minimum_work_experience": self.minimumWorkExperience,
            "minimum_current_work_experience": self.minimumCurrentWorkExperience,
            "salary": {
                "minimum_salary": self.salaryMinimumSalary,
                "minimum_salary_main_regions": self.salaryMinimumSalaryMainRegions,
                "main_regions": self.salaryMainRegions
            }
        }


class CreditCardReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    text = db.Column(db.Text, unique=True)
    rating = db.Column(db.Integer)
    card = db.Column(db.Integer, db.ForeignKey(CreditCardOffer.id, ondelete='CASCADE'))
    market = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "market": self.market,
            "text": self.text,
            "rating": self.rating,
            "card": CreditCardOffer.query.get(self.card).to_dict()
        }
