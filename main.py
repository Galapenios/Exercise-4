from twilio.rest import Client
import subprocess

account_sid = 'AC98da704927a45a0d2db8fb520ccf4506'   #inloggegevens voor de twilio api#
auth_token = 'b83ff370f24ac5d08b3c614d744b03a2'      #inloggegevens voor de twilio api#

client = Client(account_sid, auth_token)             # geeft de tokens mee aan de client die een message kan schrijven

from_number = 'whatsapp:+14155238886'  # het number van de api#
to_number = 'whatsapp:+31649802900'  # mijn number#
message_warning = "your laptop has been connected to an external disk!"
y = subprocess.getstatusoutput("diskutil list")
diskutil_list = y[1]
if (diskutil_list.find("external") != -1):
    message_body = message_warning
    print(message_warning)
    message = client.messages.create(       #
        from_=from_number,
        body=message_body,
        to=to_number
    )
else:

    print("niks is aangesloten!")




