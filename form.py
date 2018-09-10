from flask_wtf import FlaskForm
from wtforms import DecimalField


class CoefficientsForm(FlaskForm):
    a = DecimalField('a')
    b = DecimalField('b')
    c = DecimalField('c')
