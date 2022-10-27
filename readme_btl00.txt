0. mkdir btl01
(.venv) PS D:\projects\bottle\bottledemo> waitress-serve --listen=127.0.0.1:8080 app:app

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-venv

https://learn.microsoft.com/en-us/windows/python/web-frameworks#open-a-wsl---remote-window

1.create new venv
python3 -m venv .venv

source .venv/bin/activate
python3 -m pip install bottle

2.select command pallte_ select python inter
3. choose venv
4. pip install bottle
5. new main.py
6. from bottle import route, run
7. python main.py

http://127.0.0.1:8080/say_hello

pip install waitress
waitress-serve --listen=*:8000 myapp.wsgi:application
waitress-serve --listen=*:8000 app.wsgi:application
waitress-serve --listen=*:8000 app:app
waitress-serve --listen=127.0.0.1:8080 app:app
waitress.serve(app, listen='0.0.0.0:5003')
waitress.serve(app, listen='127.0.0.1:8080')
http://0.0.0.0:8000

8. gunicorn main:app
9. cd bottledemo
10. gunicorn app:app

11. waitress.served.

12. pip install webtest
13. pip install requests

http://127.0.0.1:8080/get_price/solana
http://127.0.0.1:8080/get_price/bitcoin/eur
http://127.0.0.1:8080/static/bottle.jfif

127.0.0.1:8080/portfolio/bitcoin

3 template engines
14. pip install jinja2

3 files - base, portfolio, footer

http://127.0.0.1:8080/jinja/portfolio

15. pip install wtforms
16. REST BOOK
GET http://127.0.0.1:8080/api/portfolio

POST 127.0.0.1:8080/api/portfolio/ethereum
Content-Type: application/json

{
    "quantity": 20.0
}

error handler
127.0.0.1:8080/get_price_tpl/bitcoin/usd/-1.0
17. docker pull mongo
18. docker run -d --name crypto_tracker -p 27017:27017 mongo:latest
19. pip install pymongo
20. pip install ipython
pip install ipython
ipython

from pymongo import MongoClient

In [2]: client = MongoClient()

In [3]: client
Out[3]: MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

In [4]: db = client_crypto_tracker
In [5]: db = client.crypto_tracker

In [6]: portfolios = db.portfolios

In [7]: portfolio = {"username": "pip_squeek", "investments": {"solana": 1.0, "ethereum": 0.1}}

In [8]: portfolios.insert_one(portfolio)

21.
from bson.json_util import dumps

dumps(portfolios.find())

22. jon_doe_portfolio = portfolios.find_one({"username": "jon_doe"})
jon_doe_portfolio

docker kill crypto_tracker
docker-compose ps
deactivate