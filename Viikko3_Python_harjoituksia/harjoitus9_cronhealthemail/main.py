import smtplib
import socket
import requests
socket.getaddrinfo('localhost', 8080)
server = smtplib.SMTP('smtp.gmail.com', 587)

def health_check():
    r = requests.get("http://34.125.89.188/health.html")
    if r.ok is not True:
        email_alert()

def email_alert():
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("sposti", "salis")

    msg = "\nHealth check epäonnistui!"
    server.sendmail("sposti", "sposti", msg)


health_check()