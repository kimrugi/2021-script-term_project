
import smtplib
from email.mime.text import MIMEText
import email_password

def send_mail(recipientAddr, text):
    smtpHost = "smtp.gmail.com"   #smtp 서버 주소
    port = "587"

    msg = MIMEText(text)  #텍스트가 기본인 메일을 하나 생성합니다. text는 반듯이 ASCII코드여야만 합니다. 만약 unicode가 들어 있다면 받는 쪽에서 문자가 깨져있는 메일을 받게 될 것 입니다.


    msg['Subject'] = "test email"
    msg['From'] = email_password.id()
    msg['To'] = recipientAddr



    #SMTP 서버를 이용해 메일 보냅니다.
    s = smtplib.SMTP(smtpHost, port)
    s.starttls()
    s.login(email_password.id(), email_password.password())
    s.sendmail(email_password.id(), [recipientAddr], msg.as_string())
    s.close()

