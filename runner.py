import pymsteams
import sys

color_scheme={'success':'00c551','danger':'ff4444','warning':'ffbb33','info':'33b5e5'}

# print(len(sys.argv))
# for i in range(1, len(sys.argv)):
#     print(sys.argv[i])

if len(sys.argv) < 2:
  raise Exception("Please pass the webhooks and message for the notification")

webhook = sys.argv[1]
message = sys.argv[2]

myTeamsMessage = pymsteams.connectorcard(webhook)

myTeamsMessage.text(message)

if len(sys.argv) > 3:
    notification_color = color_scheme.get(sys.argv[3], '33b5e5')
    myTeamsMessage.color(notification_color)
else:
    notification_color = color_scheme.get('info', '33b5e5')
    myTeamsMessage.color(notification_color)

if len(sys.argv) > 4:
    button_link_text = sys.argv[4]
    button_link = sys.argv[5]
    myTeamsMessage.addLinkButton(button_link_text, button_link)

myTeamsMessage.send()