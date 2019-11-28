
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from wtforms.validators import DataRequired


# class PitchForm(FlaskForm):
#     '''
#     Class to create a wtf form for creating a pitch
#     '''
#     content = TextAreaField('YOUR PITCH')
#     submit = SubmitField('SUBMIT')


class PitchForm(FlaskForm):
     title = StringField('Title', validators=[DataRequired()])
     content = TextAreaField('Content',validators=[DataRequired()])
     submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    opinion = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')

class CategoryForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')
