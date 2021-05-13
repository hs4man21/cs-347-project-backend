import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to our CS 347 project API!</h1>"

@app.route('/send-test/', methods=['POST'])
def send_test():
    gmail_user = 'cs347spring2021@gmail.com'
    gmail_password = 'ec5dwU7pwViBTw5'

    sent_from = gmail_user
    to = ['cs347spring2021@gmail.com']
    subject = 'New feedback'
    body = request.json.get("feedback")

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
        return 200
    except:
        print('Something went wrong...')