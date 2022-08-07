<h2> Telegram Scraper and Message Sender </h2>
---
## • API Setup
* Go to http://my.telegram.org  and log in.
* Click on API development tools and fill the required fields.
* Put app name you want & select "other" for platform.
* Copy "api_id" & "api_hash" after clicking create app (will be used in setup.py)

## • How to install and use

`$ pkg install -y git python`

`$ git clone https://github.com/th3unkn0n/TeleGram-Scraper.git`

`$ cd TeleGram-Scraper`

* Install Requierments

`$ python3 setup.py -i`

* Setup configuration file (API ID and Hash ID)

`$ python3 setup.py -c`

* Collect user data

`$ python3 scraper.py`

* (members.csv will be generated upon scraping completion)
* Send mass DMs to collected targets

`$ python3 dmsbot.py members.csv`
