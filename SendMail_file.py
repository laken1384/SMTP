from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from email.mime.application import MIMEApplication
def sendmail_file(Itid):
    html = """
        <html>
        <body>
            <font size="3">
                <b>
                    <p>您好：</p>
                    <p>重要事件通知，請參照附件</p>
                </b>
            </font>
        </body>
        </html>
        """
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = Itid.Subject #"測試寄信"  #郵件標題
    content["from"] = Itid.From #"寄件者的信箱"  #寄件者
    content["to"] = ",".join(Itid.To) #"收件者的信箱" #收件者
    content.attach(MIMEText(html,"html"))  #郵件內容
    content.attach(MIMEImage(Path("image.jpg").read_bytes()))  # 郵件圖片內容

    #寄送PDF檔案
    fileName = 'test.pdf'
    pdfload = MIMEApplication(open(fileName,'rb').read())
    pdfload.add_header('Content-Disposition',
                    'attachment',
                    filename=fileName)
    content.attach(pdfload)

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(Itid.From,Itid.password)#"寄件者的信箱", "寄件者的寄件密碼")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("成功傳送")
            return True
        except Exception as e:
            print("Error message: ", e)
            return e
