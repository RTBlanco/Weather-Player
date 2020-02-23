from flask_wtf import FlaskForm
from Weather.Weather_api import check_zip
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import InputRequired, Length

def valid_zipcode(self, zipcode):
    if check_zip(zipcode.data) == '404':
        raise ValidationError('Zipcode can not be found')

class Myform(FlaskForm):
    zipcode = StringField('zipcode', validators=[InputRequired(), Length(min=5,max=5,message='Zipcode must be 5 characters long'), valid_zipcode])
    submit = SubmitField('ENTER')
