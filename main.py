from flask import Flask, render_template, request, redirect
from flask.helpers import url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        email = request.form["em"]
        return redirect(url_for("email", eml=email))
    else:
        return render_template('contact.html')


@app.route("/<eml>")
def email(eml):
    return f"<h1>The answer will be send to the following email:{eml}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
