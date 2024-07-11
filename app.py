from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Load and preprocess data
data = pd.read_csv('dataset.csv')
data['age'] = 2024 - data["year_built"]

categorical_features = ['location']
encoder = OneHotEncoder(handle_unknown='ignore')
encoded_features = pd.DataFrame(encoder.fit_transform(data[categorical_features]).toarray())
encoded_feature_names = encoder.get_feature_names_out(categorical_features)
encoded_features.columns = encoded_feature_names

data = data.drop(categorical_features, axis=1)
data = pd.concat([data, encoded_features], axis=1)
data.columns = data.columns.astype(str)

X_train, X_test, y_train, y_test = train_test_split(data.drop('sale_price', axis=1), data['sale_price'], test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = int(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    location = request.form['location']
    year_built = int(request.form['year_built'])

    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'location': [location],
        'year_built': [year_built]
    })

    input_data['age'] = 2024 - input_data['year_built']

    encoded_input = pd.DataFrame(encoder.transform(input_data[categorical_features]).toarray())
    encoded_input.columns = encoded_feature_names

    input_data = input_data.drop(categorical_features, axis=1)
    input_data = pd.concat([input_data, encoded_input], axis=1)
    input_data.columns = input_data.columns.astype(str)

    prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction_text=f'Predicted sale price for the house:Rs{prediction:.2f}')

if __name__ == "__main__":
    app.run(debug=True)
