from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, URL
from wtforms import StringField, SubmitField, IntegerField
import smtplib

USERNAME = "jeffreyjeremiahpython@gmail.com"
PASSWORD = "jeffrey766"

app = Flask(__name__)
app.config['SECRET_KEY'] = '5be08a69dd9b22f121c77e43ac49127769'
Bootstrap(app)


class ContactForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email")
    phone = IntegerField("Phone")
    message = StringField("Message")
    submit = SubmitField("Submit")


@app.route('/', methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return redirect(url_for('home'))
    return render_template("index.html", form=form)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(USERNAME, "jeffreyjeremiah1@gmail.com", email_message)


if __name__ == '__main__':
    app.run(debug=True)


