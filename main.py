from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'

db = SQLAlchemy(app)


class Inquiries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return'<Message %r>' % self.id


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact', methods=["POST", "GET"])
def contact():

    if request.method == "POST":
        username = request.form['name']
        mail_adress = request.form['email']
        user_inquirie = request.form['message']

        new_inquirie = Inquiries(
            name=username, email=mail_adress, message=user_inquirie)

        try:
            db.session.add(new_inquirie)
            db.session.commit()
            return redirect('/')
        except Exception:
            return "There wass an error sending your inquirie"
    else:
        return render_template('contact.html')


@app.route("/<eml>")
def email(eml):
    return f"<h1>The answer will be send to the following email:{eml}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
