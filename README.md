<h2> Telegram Scraper and Message Sender </h2>
<p align="center">
  <a href="https://github.com/adrianeth">
    <img src="https://img.shields.io/github/followers/adrianeth?label=Follow&style=social">
  </a>
  <a href="https://github.com/adrianeth/telegram-scraper-message-sender">
    <img src="https://img.shields.io/github/stars/adrianeth/telegram-scraper-message-sender?style=social">
  </a>
</p>
<p align="center">
  Telegram Scraper and Mass DM sender
</p>
<p align="center">
</p>

---
## • API Setup
* Go to http://my.telegram.org  and log in.
* Click on API development tools and fill the required fields.
* Put app name you want & select "other" for platform.
* Copy "api_id" & "api_hash" after clicking create app (will be used in setup.py)

## • How to install and use

`$ pkg install -y git python`

`$ git clone https://github.com/adrianeth/telegram-scraper-message-sender.git`

`$ cd telegram-scraper-message-sender`

* Install Requierments

`$ python setup.py -i`

* Setup configuration file (API ID and Hash ID)

`$ python setup.py -c`

* Collect user data <i>(members.csv will be generated upon scraping completion)</i>

`$ python scraper.py`

* Send mass DMs to collected targets

`$ python dmsbot.py members.csv`
