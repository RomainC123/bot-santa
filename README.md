# bot-santa

This bot will allow you to setup secret santa draws through Telegram's API.

# Setup

1. You will need to create a bot using @BotFather on Telegram. Just start a chat with him, and follow the instructions to create your bot. This will allow you to name it, and to get its token.

2. Create a folder name data at the root of your repo, and create two files, admins.txt and token.txt inside of it. Then paste your bot token in the token.txt file. You will also need to choose at least one admin, to do so add its Telegram username (without the @, hence if your @ telegram is '@username', then you will need to write 'username' (without the quotes) in your admins.txt file). If you want to add more than one admin, just each new username on a new line.

3. Open a terminal, and make sure you have docker installed (check this https://docs.docker.com/get-docker/ for instructions on how to achieve that). Then run the following commands, making sure you still are in your app folder:

```
docker build -f Dockerfile -t santa-app .
docker run -i -t --rm santa-app
```

4. You should see the log output of your bot. To shut it down, press Ctrl (or cmd) + c. To restart it, just run the second line from the above commands.

# Bot commands

The followings commands are available:

* Admin commands : these commands are only available to admins, if you username isn't in admins.txt, then these commands won't do anything.

  1. /reset: Clears the data folder, removes all participants and all pairings.

  2. /add: Allows an admin to add a list of @ to the list of participants. To use it, write /add @username1 @username2, adding a space between each username.

  3. /assign: Uses the current list of participants to assign pairings to all participants. This commands will restrict the usage of /add and /join, which will become unavailable until the /reset is used.

  4. /get_all: Displays the list of all pairings. Only works after /assign has been called. This command is designed for testing purposes, and should not be used by an admin if he/she wishes to participate in the secret santa, for obvious reasons.

* User commands: these are the commands available to anyone.

  1. /start: Called when you first interact with the bot, displays the list of user commands and guidelines on how to participate in the secret santa.

  2. /join: Adds the username of the user that uses the command to the list of participants.

  3. /list: Displays a list of all participants.

  4. /get_name: Displays the pairing of the user that uses the command.
