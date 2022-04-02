# Fantasy F1 Leaderboard Discord bot

A simple Discord bot to display a league leaderboard from the official Formula 1 Fantasy game in a text channel using a command. This bot isn't hosted anywhere yet. It's still a work in progress, and also have some major limitations which prevents it from becoming a verified/hosted bot at the moment. The reasoning is explained below.


## Getting started

This bot isn't hosted anywhere. So it is up to you to run it on your own environment.

### Prerequisites

* Docker

### Step 1 - Extract the auth cookie

The official F1 API currently blocks any automated requests on the authentication API at the moment, so there is no way to automatically generate this cookie. So it's currently a dirty manual hack to get it to work.

After logging into the Fantasy F1 game, you can open up the developer console on your browser and make a request to the following API endpoint: `https://fantasy-api.formula1.com/f1/2022/`

In the developer console, go to the network tab and click on the `2022/` request. Then switch to the Headers tab within the request browser and then copy the value for the `Cookie` header in the `Request Headers` section. How long this cookie is valid for is yet to be tested.

### Step 2 - Setup the environment variables with your league details

You need to setup a few environment variables in order to run this bot. Those are as follows:

* `BOT_TOKEN` - This is the bot token you get from the Discord developer portal when you setup your bot there.
* `F1_SEASON` - This is the year of the F1 season you're playing on. (Eg. 2022)
* `LEAGUE_ID` - You can find this on the URL of your league web page. (Eg. In the case of https://fantasy.formula1.com/app/#/league/457649, your league id would be 457649)
* `COOKIE` - This is the cookie which you extracted in step 1.

You can either set these up as system environment variables, in the docker-compose file, or in a `.env` file.

Example .env below:

```
BOT_TOKEN='abcdefgh123456789'
LEAGUE_ID='457649'
COOKIE='cookie_consent=true; notice_preferences=2:; ... '
F1_SEASON='2022'
```

### Step 3 - Run the bot

You can run the bot with docker compose. It will spin up the bot and then you can join the bot into your server to use it.

```
docker-compose up
```

Or you can start the bot in the background using the following command.

```
docker-compose start bot
```


### Step 4 - Run the leaderboard command from Discord

From a text channel in your server where the bot is joined to, you can type the command `$leaderboard` and the bot will respond with the leaderboard table.

## Possible future improvements

* Investigate and implement a proper way to authenticate against the API.
* Ability to work with multiple leagues from a single bot.
* Ability to configure multiple leagues for a single Discord server.
* Host and get the bot verified.
