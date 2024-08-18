from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, RadioField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class InputDataForm(FlaskForm):
    credit_score = IntegerField('Credit Score', validators=[DataRequired(), NumberRange(min=300, max=850)],
                                render_kw={"type": "number", "min": "300", "max": "850"})
    
    geography = SelectField('Geography', 
                            choices=[('Spain', 'Spain'), ('France', 'France'), ('Germany', 'Germany')],
                            validators=[DataRequired()])
    
    gender = SelectField('Gender', 
                         choices=[('Male', 'Male'), ('Female', 'Female')], 
                         validators=[DataRequired()])
    
    age = IntegerField('Age', 
                       validators=[DataRequired(), NumberRange(min=18, max=100)],
                       render_kw={"type": "number", "min": "18", "max": "100"})
    
    tenure = IntegerField('Tenure', validators=[DataRequired(), NumberRange(min=0, max=10)],
                          render_kw={"type": "number", "min": "0", "max": "10"})
    
    balance = FloatField('Balance', validators=[DataRequired()],
                         render_kw={"type": "number", "step": "0.01"})
    
    num_of_products = IntegerField('Number of Products', validators=[DataRequired(), NumberRange(min=1, max=4)],
                                   render_kw={"type": "number", "min": "1", "max": "5"})
    
    has_cr_card = RadioField('Has Credit Card', 
                             choices=[('1', 'Yes'), ('0', 'No')], 
                             validators=[DataRequired()])
    
    is_active_member = RadioField('Is Active Member', 
                                  choices=[('1', 'Yes'), ('0', 'No')], 
                                  validators=[DataRequired()])
    
    estimated_salary = FloatField('Estimated Salary', validators=[DataRequired()],
                                  render_kw={"type": "number", "step": "0.01"})
    
    predict = SubmitField('Predict')
