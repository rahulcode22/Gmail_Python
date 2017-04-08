import smtplib
#Create SMTP session
s=smtplib.SMTP('smtp.gmail.com',587)

#Start TLS for security
s.starttls()

#Authentication
s.login("sender_mail_id","sender_email_password")

#Message you need to sent
messsage="Message_info"

#Sending the mail
s.sendmail("sender_mail_id","receiver_email_id",message)

#terminating the session
s.quit()
