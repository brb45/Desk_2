from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#send_Email(server, sender, recipients, subject, text_PKG_QA)
def send_Email( server, sender, recipients, subject, message ):
	session = smtplib.SMTP(server)
	msg = MIMEMultipart('alternative')
	msg['From'] = sender
	msg['To'] = "xu"
	msg['To'] = "y"
	for receiver in recipients:
		msg['To'] =  receiver
	print(msg['To'])

	print("msg['To'] type is {0}".format(type(msg['To'])))
	#print("msg['To'] is {0}".format(msg['To']))
	print(msg['To'])

	msg['Subject'] = subject
	text_PKG = message
	# Record the MIME types of both parts - text/plain and text/html.
	msg_PKG = MIMEText(text_PKG, 'plain')
	# Attach parts into message container.
	msg.attach(msg_PKG)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	print ("\n Sending email from:" , sender, "to: " , recipients)
	print(msg.as_string())
	session.sendmail(sender, recipients, msg.as_string())
	session.quit()

if __name__ == "__main__":
	sender = 'jian.sun@litepoint.com'#'Silicon_Solution_QA@litepoint.com'
	server = '192.168.2.199'
	Project_Name = "Auto_test sample run\nCorrelation report follow up"
	subject = "QA update for station: {0}".format(Project_Name)
	#text_PKG_QA = "\nAuto test passed {0} QA for the package : {1}".format("test_mode", "IQfact_package")
	text_PKG_QA = """
1. Test status: pass
	2. No errors found
	    3. build version 1.0
					"""
	recipients = ["sunusd@yahoo.com","jian.sun@litepoint.com"]
	#recipients.append()
	send_Email(server, sender, recipients, subject, text_PKG_QA)
