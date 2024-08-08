try:
#     connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject:hey\n\nThis is the body of the email")
#     connection.close()
# except TimeoutError as e:
#     print("Error: unable to send email")