from flask import Flask, request
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "TODO OK"

@app.route('/predict', methods=['GET'])
def pred():
    age = request.args.get('age')
    sex = request.args.get('sex')
    clase = request.args.get('clase')

    if age is None or sex is None or clase is None:
        return "Introduce todas las variables"
    
    if not(age.isnumeric() and sex.isnumeric() and clase.isnumeric()):
        return "Introduce numeros"
    
    age = int(age)
    sex = int(sex)
    clase = int(clase)
    
    
    with open ("modelo_random_clasificacion.pkl", "rb") as f:
        rf = pickle.load(f)

    df = pd.DataFrame({'Age': [age], 'Sex': [sex], 'Pclass': [clase]})
    prediction = rf.predict(df)

    return str(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

