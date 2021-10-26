import smtplib
import socket
socket.getaddrinfo('localhost', 8080)
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login("sposti", "salansana")

msg = "\nviesti"
server.sendmail("sähköposti", "sposti", msg)
