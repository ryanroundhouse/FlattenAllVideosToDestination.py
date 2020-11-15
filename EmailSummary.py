import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmailSummary(smallFiles, bigFiles):
    """ Sends an email summary of all small files and all big files. """
    if not smallFiles:
        raise Exception("You must send a list of small files")
    if not bigFiles:
        raise Exception("You must send a list of big files")

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "File sort summary"
    msg['From'] = config.sender
    msg['To'] = config.receiver

    textMessage = """ \
Files sent to Movies:
{0}

Files sent to Series:
{1}
""".format('\n'.join(bigFiles), '\n'.join(smallFiles))

    htmlMessage = """ \
<html>
    <head></head>
    <body>
        <h2>Files sent to Movies:</h2>
        {0}

        <h2>Files sent to Series:</h2>
        {1}
    </body>
</html>
""".format('\n'.join(bigFiles), '\n'.join(smallFiles))

    part1 = MIMEText(textMessage, 'plain')
    part2 = MIMEText(htmlMessage, 'html')

    msg.attach(part1)
    msg.attach(part2)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(config.username, config.password)
        server.sendmail(config.sender, config.receiver, msg.as_string())

#smallFiles = ["first.mkv", "second.mkv"]
#bigFiles = ["big1.mkv", "big2.avi"]
#sendEmailSummary(smallFiles, bigFiles)