from flask import Flask, render_template, redirect, url_for, request
import predict as pre

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
async def predict():
    if(request.method == "POST"):

        review = request.form.get('review')
        
        sentiment = await pre.get_sentiment(review)
        sentiment = sentiment[0]
        
        return redirect(url_for('get_results', sentiment=sentiment))

@app.route("/results/<sentiment>", methods=["GET"])
def get_results(sentiment):
    return render_template("results.html", sentiment=sentiment)

