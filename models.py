from datetime import datetime
from app import db

class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Market('{self.name}', '{self.description}')"

class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    provider = db.Column(db.String(100), nullable=False)
    is_valid = db.Column(db.Boolean, default=False)
    market_id = db.Column(db.Integer, db.ForeignKey('market.id'), nullable=False)

    def __repr__(self):
        return f"Intervention('{self.date}', '{self.provider}', '{self.is_valid}')"

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    intervention_id = db.Column(db.Integer, db.ForeignKey('intervention.id'), nullable=False)

    def __repr__(self):
        return f"Invoice('{self.amount}', '{self.price}')"

