import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Defining variables in order to make the code neater and prevent typo mistakes
myEmail = 'cuprojecttes277@gmail.com'
reciverEmail = 'cuprojecttes277@gmail.com'
subject = 'Lap times from todays session! '

#This part deals with filling all required when writing an email and giving it extra complexity
message = MIMEMultipart()
message['From '] = myEmail
message['To '] = reciverEmail
message['Subject '] = subject

#Addin a short message in the body
body = 'Good day to you! We are sending this e-mail with all of your lap times from your last session.'
message.attach(MIMEText (body, 'plain'))

#Opening the template with the letter and the information and making it attachment
filename = 'template.txt'
attachment = open(filename, 'rb')

#First part of the Attachment and setting it up
#Allowing the uppload of the attachment
#Encoding in base 64 as that is one of the standard bases for emails
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= "+filename)

message.attach(part)
text = message.as_string()

#Setting up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myEmail, 'Resit123')

#Execution followed by Quitting the server
server.sendmail(myEmail, reciverEmail, text)
server.quit()