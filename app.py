from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form["email"]
    email_vector = vectorizer.transform([email])
    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        result = "Fraud Email"
    else:
        result = "Genuine Email"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)