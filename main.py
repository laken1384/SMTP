from flask import Flask,request
from flask_cors import CORS
import uuid
import time
from SendMail_txt import sendmail_txt
from SendMail_file import sendmail_file
app = Flask(__name__)
CORS(app)

class Itid():
    From=""#寄件人
    To=""#收件人
    Subject=""#標題
    content=""#內容
    password=""

@app.route('/api', methods=["POST","GET"])
def sendtxt():
    return request_data('txt')
@app.route('/file', methods=["POST","GET"])
def sendfile():
    return request_data('file')


def request_data(Format):
    if(request.method == 'GET'):
        return {
            "From":Itid.From,
            "To":Itid.To,
            "Subject":Itid.Subject,
            "content":Itid.content,
            "password":Itid.password
        }
    #uich()
    if(request.method == 'POST'):
        Itid.From = request.json.get('From')
        Itid.To = request.json.get('To')
        Itid.Subject = request.json.get('Subject')#+" Time:"+str(time.ctime())
        Itid.content = request.json.get('content')#+" uuid:"+str(uuid.uuid4())
        Itid.password = request.json.get('password')
        if Format == 'txt':
            Status = sendmail_txt(Itid)
        elif Format == 'file':
            Status = sendmail_file(Itid)
        else:
            Status = False

        if Status == True:
            Status = "成功"
        else:
            Status = "失敗"
        return {
            "scusses":Status,
            "From":Itid.From,
            "To":Itid.To,
            "Subject":Itid.Subject,
            "content":Itid.content,
        }
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5010)
