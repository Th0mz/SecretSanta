import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import date

def sendEmail(info):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Connect to the server that will send the mail
    server.starttls()

    # Get the mail and password from external file
    with open("emailInfo.txt", "r") as emailInfo:
        (sender_email, password) = emailInfo.readline().split(" ")
    
    # Login to gmail
    server.login(sender_email, password)


    for email in info:
        # Create custom message for each person
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = "Amigo Secreto " + str(date.today().year)
        
        content = MIMEText("O teu amigo secreto é " + info[email], "plain") 
        message.attach(content)

        message = message.as_string()

        # Send the mail from our email[sender_email] to the
        # other person's mail [email] with the custom message
        server.sendmail(sender_email, email, message)

        print("Successfully sent mail to " + email)

    # Close the server
    server.quit()