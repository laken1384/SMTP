import email.message
import smtplib
def sendmail_txt(Itid):
    try:
        msg=email.message.EmailMessage()
        msg["From"]=Itid.From
        msg["To"]=",".join(Itid.To)
        msg["Subject"]=Itid.Subject
        msg.set_content(Itid.content)
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(Itid.From,Itid.password)#帳號 密碼
        server.send_message(msg)
        server.close()
        return True
    except:
        return False