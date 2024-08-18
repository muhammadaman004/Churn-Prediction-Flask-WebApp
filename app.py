from flask import Flask, render_template, request, flash
from form import InputDataForm
import torch
import pickle
import pandas as pd

model = torch.load('model.pt')

with open('onehotencoder_geo.pkl','rb') as file:
    label_encoder_geo=pickle.load(file)

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputDataForm()

    if form.validate_on_submit():
        data = {
            'CreditScore': form.credit_score.data,
            'Geography': form.geography.data,
            'Gender': form.gender.data,
            'Age': form.age.data,
            'Tenure': form.tenure.data,
            'Balance': form.balance.data,
            'NumOfProducts': form.num_of_products.data,
            'HasCrCard': form.has_cr_card.data,
            'IsActiveMember': form.is_active_member.data,
            'EstimatedSalary': form.estimated_salary.data
        }
        input_df=pd.DataFrame([data])
        input_df['Gender']=label_encoder_gender.transform(input_df['Gender'])
        geo_encoded = label_encoder_geo.transform([[data['Geography']]]).toarray()
        geo_encoded_df = pd.DataFrame(geo_encoded, columns=label_encoder_geo.get_feature_names_out(['Geography']))
        input_df=pd.concat([input_df.drop("Geography",axis=1),geo_encoded_df],axis=1)
        input_scaled=scaler.transform(input_df)
        input_tensor = torch.tensor(input_scaled, dtype=torch.float32)
        with torch.no_grad():
            prediction = model(input_tensor)
        if prediction.item() > 0.5:
            flash('The customer is likely to churn.')
        else:
            flash('The customer is not likely to churn.')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
