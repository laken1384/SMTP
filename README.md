# SMTP
以python為基礎，基於SMTP結合Flask，可由外部帶入Body來實現寄信功能
# Running
#### 寄送純文字信件
POST : http://localhost:5010/api

Body:
```json
"From":"寄件人",
"To":"收件人",
"Subject":"主旨",
"content":"內容",
"password":"密碼"
```
#### 寄送含附件檔案
POST : http://localhost:5010/file

Body:
```json
"From":"寄件人",
"To":"收件人",
"Subject":"主旨",
"content":"內容",
"password":"密碼"
```
