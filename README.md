# microsoft-teams-message-bot
- GitHub Action to send a message to Microsoft Teams using a webhook


## Usage
1. In order to use this, First you need is to create a Webhook in your Microsoft Teams Channel, follow [this link](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-an-incoming-webhook-1) for info about creating a webhook.

2. Add the created webhook uri in Ms_Teams_Webhook_URI on your repository's configs on Settings > Secrets. It is the Webhook URI of the dedicated Microsoft Teams channel for notification. Learn more about setting up [GitHub Secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)

3. Add a new `step` on your github actions workflow code below:

```yaml

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Microsoft Teams Webhook Message Bot
        uses: myusufcse/microsoft-teams-message-bot@v1.1
        with:
          webhook: ${{ secrets.Ms_Teams_Webhook_URI }}
          message: Your custom notification message 
          notification_color: success or danger or warning or info (optional)
          button_link_text: The button text for navigation to link from Microsoft Teams channel (optional)
          button_link: The button link for navigation from Microsoft Teams channel (optional)
```

4. Simplified version of the code: **Advice not to pass the webhook uri directly**
```yaml
- name: Microsoft Teams Webhook Message Bot
        uses: myusufcse/microsoft-teams-message-bot@v1.1
        with:
          webhook: Your webhook uri
          message: Your custom notification message 
```
## Sample
![Sample Notification](https://github.com/myusufcse/microsoft-teams-message-bot/blob/main/Microsoft%20Teams%20Webhook%20Message%20Bot.png?raw=true)
