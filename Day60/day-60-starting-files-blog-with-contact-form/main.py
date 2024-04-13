from flask import Flask, render_template, request
import requests

import os
import base64
from email.message import EmailMessage

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def gmail_send_message(message_subject, message_content):
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

    credentials_json = "C:/Users/jimli/OneDrive - NVIDIA Corporation/NVIDIA/Python/python 100 days/Day47/yes72002.json"
    credentials_json = "C:/Users/jimli/OneDrive - NVIDIA Corporation/NVIDIA/Python/python 100 days/Day47/imperialtheory.json"
    
    creds = None
    
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_json, SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(message_content)

        message["To"] = "imperialtheory@gmail.com"
        message["From"] = "imperialtheory@gmail.com"
        message["Subject"] = message_subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
    return send_message


# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/contact")
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name)
        print(email)
        print(phone)
        print(message)

        # send email
        message_subject = f"Subject: Day 60: New Message"
        message_content = f"name: {name}\nemail: {email}\nphone: {phone}\nmessage: {message}\n"
        gmail_send_message(message_subject, message_content)
        print("Send Email Succeed!")

        # return "<h1>Successfully sent your message</h1>"
        return render_template("contact.html", meg_sent=True)
    else:
        return render_template("contact.html", meg_sent=False)

# @app.route('/from-entry', methods=['POST', 'GET'])
# def receive_data():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         message = request.form['message']
#         print(name)
#         print(email)
#         print(phone)
#         print(message)
#         return "<h1>Successfully sent your message</h1>"
#     else:
#         return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
