import smtplib

#잊어버려서 다시 했다

EMAIL = ""
TO = ""
PASSWORD = ""

def send():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(EMAIL,PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=TO,
        msg="subject:Python testing\n\ndone?",
    )

send()