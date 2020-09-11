import csv, smtplib, time

#server credentials
port = #### 
smtp_server = "" #fake server name
login = "" 
password = "" 

message = """Subject: ####
To: {recipient}
From: {sender}

####"""
sender = "new@example.com"

with smtplib.SMTP("########", ###) as server:
    server.login(login, password)
    with open("csv") as file:
        reader = csv.reader(file)
        next(reader)  # it skips the header row
        while True:
        for name, email in reader:
            server.sendmail(
               sender,
                email,
                message.format(name=name, recipient=email, sender=sender)
        time.sleep(0.5)
            )
            