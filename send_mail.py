
import smtplib
from email.mime.text import MIMEText
from tkinter import *
import email_password


class Mail:
    def __init__(self, library):
        window = Tk()
        window.title("메일 전송")
        self.library = library
        self.msg = self.make_text()
        frame = Frame(window)
        frame.pack()
        Label(frame, text=self.msg).pack()
        Label(window, text="메일주소: ").pack(side=LEFT)
        self.email_address = Entry(window)
        self.email_address.bind('<Return>', self.send_mail)
        self.email_address.pack(side=LEFT)
        self.send_button = Button(window, text="Send", command=self.send_mail)
        self.send_button.pack()

        window.mainloop()

    def make_text(self):
        library = self.library
        msg = library["LIBRRY_NM"] + "\n주소: " + library["ADDRESS"] + "\n전화번호: " + library["LIBRRY_TELNO"] + "\n휴관일: " + \
              library["CLOSE_DE_INFO"] + "\n평일 운영시간: " + library["BEGIN_TM"] + "~" + library["END_TM"] + "\n토요일 운영시간: " + \
              library["SAT_BEGIN_TM"] + "~" + library["SAT_END_TM"] + "\n공휴일 운영시간: " + library["HOLI_BEGIN_TM"] + "~" + \
              library["HOLI_END_TM"]
        return msg

    def send_mail(self, event=None, text=None):
        if text is None:
            text = self.msg
        self.send_button["state"] = "disabled"
        self.email_address.unbind('<Return>')
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
        try:
            s.sendmail(email_password.id(), [recipientAddr], msg.as_string())
            self.email_address.delete(0,"end")
            self.email_address.insert(0, "성공: 메일을 보냈습니다.")
        except:
            self.email_address.delete(0, "end")
            self.email_address.insert(0, "실패: 다시 입력해주세요.")
            self.send_button["state"] = "active"
            self.email_address.bind('<Return>', self.send_mail)

        s.close()


