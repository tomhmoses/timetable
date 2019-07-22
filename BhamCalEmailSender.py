from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os

from apiclient import errors


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.compose'

def sendMail(email, linkToCal):
    print("in email sender...")
    myEmail = "bham.timetable@gmail.com"
    subject = "Link to your timetable calendar"
    message_text = getCustomEmail(linkToCal)

    store = file.Storage('/home/tomhmoses/mysite_ttc/mailToken.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('/home/tomhmoses/mysite_ttc/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    message = CreateMessage("Bham Timetable Converter", email, subject, message_text)
    sentMessage = SendMessage(service, myEmail, message)

def getCustomEmail(linkToCal):
    print("making custom email")
    orig = getMessageHTML()
    #print(linkToCal)
    message_text = orig.replace("LINK_GOES_HERE", linkToCal)
    #print(message_text)
    return message_text

def getMessageHTML():
    messageHTML = "could not grab html... LINK GOES HERE <-- click here"
    try:
        file = open("/templates/email_inline.html","r")
        messageHTML = file.read()
        file.close()
    except:
        try:
            file = open("/home/tomhmoses/mysite_ttc/templates/email_inline.html","r")
            messageHTML = file.read()
            file.close()
        except:
            print("Couldn't find email HTML")
    return messageHTML

def SendMessage(service, user_id, message):
    """Send an email message.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

    Returns:
    Sent Message.
    """

    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id: %s' % message['id'])
    return message


def CreateMessage(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  #message = MIMEText(message_text)
  message = MIMEText(message_text,'html')
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

