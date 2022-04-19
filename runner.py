import pymsteams
import sys

color_scheme={'success':'00c551','danger':'ff4444','warning':'ffbb33','info':'33b5e5'}

if len(sys.argv) < 2:
  raise Exception("Please pass the webhooks and message for the notification")

webhook = sys.argv[0]
message = sys.argv[1]

myTeamsMessage = pymsteams.connectorcard(webhook)

myTeamsMessage.text(message)

if len(sys.argv) > 2:
    notification_color = color_scheme.get(sys.argv[2], '33b5e5')
    myTeamsMessage.color(notification_color)

if len(sys.argv) > 3:
    button_link_text = sys.argv[3]
    button_link = sys.argv[4]
    myTeamsMessage.addLinkButton(button_link_text, button_link)

myTeamsMessage.send()