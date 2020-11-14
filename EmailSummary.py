import smtplib
import config


def sendEmailSummary(smallFiles, bigFiles):
    """ Sends an email summary of all small files and all big files. """
    if not smallFiles:
        raise Exception("You must send a list of small files")
    if not bigFiles:
        raise Exception("You must send a list of big files")

    message = """ \
Files sent to Movies:
{1}

Files sent to Series:
{2}
"""
    messageWithHeader = 'Subject:File sort summary\n\n{0}'.format(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(config.username, config.password)
        server.sendmail(config.sender, config.receiver, messageWithHeader.format(config.sender, '\n'.join(bigFiles), '\n'.join(smallFiles)))

#smallFiles = ["first.mkv", "second.mkv"]
#bigFiles = ["big1.mkv", "big2.avi"]
#sendEmailSummary(smallFiles, bigFiles)