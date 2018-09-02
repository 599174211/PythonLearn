import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方smtp配置
mail_host = 'smtp.qq.com'
mail_user = '599174211'
mail_pass = 'fmwusuaeqcksbaih'

#发送的邮箱
senderEmail = '599174211@qq.com'
#接收的邮箱
toEmail = ['599174211@qq.com']
#host
HOST = 'localhost'
def sendMessage(eTitle, mSubject, eFrom, eTo) :
    message = MIMEText(mSubject, 'plain', 'utf-8')
    message['From'] = Header(eFrom, 'utf-8')
    message['To'] = Header(eTo, 'utf-8')
    message['Subject'] = Header(eTitle, 'utf-8')
    return message.as_string()

try :

    # smtpObj = smtplib.SMTP(HOST)
    # message = sendMessage('王振Test', '测试一下...', '王振', '王振QQ')
    # smtpObj.sendmail(senderEmail, toEmail, message)
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    message = sendMessage('wangzhenTitle','wangzehnaa','wangzhen',toEmail[0])
    smtpObj.sendmail(senderEmail, toEmail, message)
    print('发送成功')
except smtplib.SMTPException as e:
    print('Erro;无法发送邮件{}'.format(e))