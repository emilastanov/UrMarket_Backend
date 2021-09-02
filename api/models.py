from api import db


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
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
                "max": self.amountMax
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

    def to_dict(self):
        return {
            "id": self.id,
            "language": self.language,
            "question": self.question,
            "answer": self.answer
        }