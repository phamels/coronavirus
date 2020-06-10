# Coronavirus data scraping
This is a simple script that scrapes the coronavirus numbers from worldofmeters with BeautifulSoup4 and dumps it to a json file.

## Installation
```console
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python coronascrape.py
```

## Further information
- Run the `coronscrapy.py` script every 10 minutes or so in a cronjob.
- Setup a webserver with webroot `html` if you desire.

## Example
- https://covid19.hamels.be
- link to the json file: https://covid19.hamels.be/covid19.json