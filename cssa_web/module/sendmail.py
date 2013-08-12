import smtplib
from email.mime.multipart import MIMEMultipart
from cssa_web.models import UserConfirm
import random

def generateRandom():
    maxint = 99999999
    ret = random.randint(0, maxint)
    return ret

def sendConfirmEmail(user):
    username = 'fatestudio'
    password = 'wokaolei!'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)

    me = 'fatestudio@gmail.com'
    msgFrom = "From: From IT Director: QIN <" + me + ">\n"
    msgTo = "To: To YOU <" + user.ucsb_email + ">\n"
    msgMI = "MIME-Version: 1.0\nContent-type: text\n"
    msgSub = "Subject: Welcome to CSSA! Please confirm this email\n"
    msgWelcome = "Welcome to CSSA!\n\n"
    msgUsername = "Your username is:\t" + user.username + "\n"
    msgUCSBEmail = "Your UCSB Email is:\t" + user.ucsb_email + "\n\n"
    ran = generateRandom()
    userConfirm = UserConfirm(checknum=ran)
    userConfirm.user = user
    userConfirm.save()
    
    msgConfirmLink = "Here is the confirmation link:\nhttp://127.0.0.1:8000/cssa/confirm/" + user.username + "&" + str(ran) + "\n"
    
    msg = msgFrom + msgTo + msgMI + msgSub + msgWelcome + msgUsername + msgUCSBEmail + msgConfirmLink
    toaddrs = list()
    toaddrs.append(user.ucsb_email)
    #toaddrs.append(me)
    print(msg)
    server.sendmail(me, toaddrs, msg)
    server.quit()
