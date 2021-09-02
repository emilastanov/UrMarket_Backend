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
