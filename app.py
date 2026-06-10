from flask import Flask, render_template, request, jsonify, redirect, url_for
from helper import preprocessing, vectorizer, get_prediction

app = Flask(__name__)

data = dict()
reviews = []

positive = 0
negative = 0

@app.route('/')

def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html', data=data)

@app.route('/', methods=['POST'])

def add_review():
    review = request.form['text']
    preprocessed_review = preprocessing(review)
    vectorized_review = vectorizer(preprocessed_review)
    prediction = get_prediction(vectorized_review)

    if prediction == 'positive':
        global positive
        positive += 1
    else:
        global negative
        negative += 1

    reviews.insert(0, review)

    return redirect(request.url)

if __name__ == '__main__':
    app.run()