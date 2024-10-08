from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, SelectField, StringField, TextAreaField, DateTimeField, BooleanField, FloatField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class MarketForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

class InterventionForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    provider = StringField('Provider', validators=[DataRequired()])
    is_valid = BooleanField('Is Valid')
    market_id = StringField('Market ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

class InvoiceForm(FlaskForm):
    amount = StringField('Amount', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    intervention_id = StringField('Intervention ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

