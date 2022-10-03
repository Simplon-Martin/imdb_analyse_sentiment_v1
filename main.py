from flask import Flask
from flask import render_template
from flask import request
from lightgbm import LGBMClassifier
import pickle

from Forms import ReviewForm
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/',  methods=['GET', 'POST'])
def home():
    form = ReviewForm()

    return render_template('index.html', form=form)


@app.route('/shortenurl', methods=['GET', 'POST'])
def shortenurl():
    if request.method == 'POST':
        return render_template('shortenurl.html', shortcode=request.form['url'])
    elif request.method == 'GET':
        return 'A GET request was made'
    else:
        return 'Not a valid request method for this route'


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    model = load_model()
    data = request.form['sentence']
    print(data)
    print("passe dans predict")
    prediction = model.predict([data])
    predictionproba = model.predict_proba([data])
    print(predictionproba)

    return render_template('predict.html', label=data, prediction=prediction[0])


"""

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(f'Email :{form.email.data}')
        print(f'Password :{form.password.data}')
    return render_template('register.html', form=form, title='Register')

"""


def load_model():

    # Load the saved model
    with open('model/model_analyse_sentiment_v1.pkl', 'rb') as file:
        model = pickle.load(file)

    return model

