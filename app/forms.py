
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, SubmitField, StringField, IntegerField, TextAreaField, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Products(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    discount = IntegerField('Discount')
    price = IntegerField('Price', validators=[DataRequired()])
    availableStock = IntegerField(
        'Available Stock', validators=[DataRequired()])
    submit = SubmitField('Submit')


    image = FileField('Image 1', validators=[
        FileRequired(), FileAllowed(['png', 'gif', 'jpg', 'jpeg'])])
    image_1 = FileField('Image 2', validators=[
                        FileRequired(), FileAllowed(['png', 'gif', 'jpg', 'jpeg'])])
    image_2 = FileField('Image 3', validators=[
                        FileRequired(), FileAllowed(['png', 'gif', 'jpg', 'jpeg'])])


class MerchantSignup(FlaskForm):
    fullname = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    reenter = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField('Submit')

class MerchantLogin(FlaskForm):
    fullname = StringField('Name', validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField('Submit')