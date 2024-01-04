# WTForms is a flexible forms validation and rendering library for Python web development
# FlaskForm is a class provided by flask_wtf for web forms in Flask Application

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class Todo_Form(FlaskForm):
    name= StringField("Name", [DataRequired()])
    description= TextAreaField("Description", [DataRequired()])
    # Here one False and True are labels
    completed= SelectField("Completetd", choices=[("False", "False"), ("True", "True")], validators=[DataRequired()])
    submit= SubmitField("Add Todo", [DataRequired()])