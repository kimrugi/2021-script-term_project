
import smtplib
from email.mime.text import MIMEText
from tkinter import *
import email_password


class Mail:
    def __init__(self, library):
        window = Tk()
        self.library = library
        self.email_address = Entry(window)
        self.email_address.bind('<Return>', self.make_text)
        # self.to_search.pack()
        self.email_address.pack()
        Button(window, text="Send", command=self.make_text).pack()
        window.mainloop()
        pass

    def make_text(self):
        library = self.library
        msg = library["LIBRRY_NM"] + "\n주소: " + library["ADDRESS"] + "\n전화번호: " + library["LIBRRY_TELNO"] + "\n휴관일: " + \
              library["CLOSE_DE_INFO"] + "\n평일 운영시간: " + library["BEGIN_TM"] + "~" + library["END_TM"] + "\n토요일 운영시간" + \
              library["SAT_BEGIN_TM"] + "~" + library["SAT_END_TM"] + "\n공휴일 운영시간" + library["HOLI_BEGIN_TM"] + "~" + \
              library["HOLI_END_TM"]
        self.send_mail(msg)

    def send_mail(self, text):
        smtpHost = "smtp.gmail.com"   #smtp 서버 주소
        port = "587"
        recipientAddr = Entry.get(self.email_address)
        msg = MIMEText(text, "plain", "utf-8")

        msg['Subject'] = "library"
        msg['From'] = email_password.id()
        msg['To'] = recipientAddr

        s = smtplib.SMTP(smtpHost, port)
        s.starttls()
        s.login(email_password.id(), email_password.password())
        s.sendmail(email_password.id(), [recipientAddr], msg.as_string())
        s.close()


