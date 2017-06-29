# twitter-unfollowers

Forked from ChunaraLab/Fetching-Twitter-Followers

This is a simple python script used to list down people who you follow but are not following you back. It can be used to detect people who have unfollowed you. I know it's a childish concept, but let's admit that we all care about this piece of information to some degree.

## Getting Started

* Clone: `git clone https://github.com/penafieljlm/twitter-unfollowers.git`
* Install python-twitter `pip install python-twitter`
* Create config file (*see below*): `vi config.json`
* Launch script in the shell: `python twitter-unfollowers.py`

## Config file

You will need a `config.json` file in order to run the script.
> Here is a sample configuration:

```json
{
  "twitter": {
    "consumer_key": "...",
    "consumer_secret": "...",
    "access_token_key": "...",
    "access_token_secret": "..."
  },
  "accounts": ["someaccount", "anotherusername", "anotheryetagain", "etc"]
}

```

## Links

* Create a new Twitter app: https://apps.twitter.com/app/new
* Generate the needed access tokens by using one of the methods described [here](https://github.com/bear/python-twitter#api) (either use the `get_access_token.py` or generate it via Twitter).
* `/followers/ids` API: https://dev.twitter.com/rest/reference/get/followers/ids