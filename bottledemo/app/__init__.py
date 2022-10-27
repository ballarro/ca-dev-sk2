from locale import currency
from bottle import Bottle, static_file, template, view, jinja2_template, request, redirect
from forms import SearchForm

from pygecko.crypto_prices import simple_single_price
from portfolio import PORTFOLIO

app = Bottle()
#bottle.TEMPLATE_PATH.insert(0, '/path/to/xxx/views')

most_recent_user = {}

@app.route("/")
@app.route("/get_bitcoin_value")
def get_bitcoin_value():
    return "<h2>current price of " + \
        "btc is $10000</h2>"

@app.route("/get_eth_value")
def get_eth_value():
    return "<h2>current price of " + \
        "eth is $100</h2>"

@app.route("/say_hello")
def say_hello():
    message = "Hello Bottle.v1.4"
    return f"<h2>{message}</h2>"

@app.route("/say_hello2")
def say_hello2():
    return "<h2>Hello Bottle.v2.x</h2>"

@app.route("/does_not_exist")
def does_not_exist():
    raise NotImplementedError("This path does not exist.")

@app.route("/get_price")
@app.route("/get_price/<coin_id>")
@app.route("/get_price/<coin_id>/<currency>")
@app.route("/get_price/<coin_id>/<currency>/<quantity:float>")
def get_price(coin_id="bitcoin", currency="usd", quantity=1.0):
    coin_price = simple_single_price(coin_id, currency)
    return f"<h2>Current price of {quantity} {coin_id} is {coin_price * quantity} {currency}</h2>"

@app.route("/get_price_tpl/<coin_id>")
@app.route("/get_price_tpl/<coin_id>/<currency>")
@app.route("/get_price_tpl/<coin_id>/<currency>/<quantity:float>")
def get_price_tpl(coin_id="bitcoin", currency="usd", quantity=1.0):
    if quantity < 0.0:
            raise ValueError("Quantity needs fixing into non-negative")
    coin_price = simple_single_price(coin_id, currency)
    return template("get_price", coin_id=coin_id, coin_price=coin_price, currency=currency, quantity=quantity)

@app.route("/get_price_dec/<coin_id>")
@view("get_price")
def get_price_dec(coin_id="bitcoin", currency="usd", quantity=1.0):
    coin_price = simple_single_price(coin_id, currency)
    return dict(coin_id=coin_id, coin_price=coin_price, currency=currency, quantity=quantity)

@app.route("/static/<filename>")
@app.route("/static/<filename:path>")
def get_static_file(filename):
    return static_file(filename, root="/projects/bottle/bottledemo/assets")

@app.route("/portfolio")
def portfolio():
    return template("portfolio", portfolio=PORTFOLIO)

@app.route("/portfolio/<coin_id>")
def portfolio_by_coin(coin_id):
    coin_price = simple_single_price(coin_id, "usd")
    #return template("mockup", coin_id=coin_id, coin_price=coin_price)
    return template("coins", coin_id=coin_id, coin_price=coin_price)

@app.route("/jinja/portfolio")
def use_jinja():
    return jinja2_template("jinja/portfolio.html", portfolio=PORTFOLIO)

@app.route("/search_coins")
def search_coins():
    if "coin_name" in request.GET:
        coin_name = request.GET["coin_name"]
        currency = request.GET["currency"]
        coin_price = simple_single_price(coin_name, currency)
        return template("search_coins", coin_id=coin_name, coin_price=coin_price, currency=currency)
    return template("search_coins", coin_id=None)

@app.route("/register", method=["GET", "POST"])
def register():
    if "username" in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            confirm = request.POST["confirm"]
            description = request.POST["description"]
            avatar = request.POST["avatar"]
            avatar.save("./bottledemo/assets/images")
            avatar_path = f"/static/images/{avatar.filename}"
            global most_recent_user
            most_recent_user = {
                "username": username,
                "password": password,
                "description": description,
                "avatar_path": avatar_path
            }
            redirect("/welcome")
    return template("register", user=None)

@app.route("/welcome")
def welcome():
    return template("register", user=most_recent_user)

@app.get("/search_coins2")
def search_coins2():
    if "coin_name" in request.GET:
        coin_name = request.query["coin_name"]
        currency = request.params["currency"]
        coin_price = simple_single_price(coin_name, currency)
        return template("search_coins", coin_id=coin_name, coin_price=coin_price, currency=currency)
    return template("search_coins", coin_id=None)

@app.get("/register2")
@app.post("/register2")
def register2():
    if "username" in request.POST:
            username = request.forms["username"]
            password = request.params["password"]
            confirm = request.POST["confirm"]
            description = request.POST["description"]
            avatar = request.files["avatar"]
            avatar.save("./bottledemo/assets/images")
            avatar_path = f"/static/images/{avatar.filename}"
            global most_recent_user
            most_recent_user = {
                "username": username,
                "password": password,
                "description": description,
                "avatar_path": avatar_path
            }
            redirect("/welcome")
    return template("register", user=None)

@app.route("/search_coins_wtf", method=["GET", "POST"])
def search_coins_wtf():
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.validate():
            coin_id = form.coin_id.data
            currency = form.currency.data
            quantity = form.quantity.data
            coin_price = simple_single_price(coin_id, currency)
            global db
            db = {
                "coin_id": coin_id,
                "currency": currency,
                "quantity": quantity,
                "coin_price": coin_price
            }
            redirect("/search_wtf")
        return template("search_coins_wtf", form=form)
    form = SearchForm()
    return template("search_coins_wtf", form=form)

@app.route("/search_wtf")
def search_wtf():
    if "coin_id" in request.GET:
        coin_name = request.query["coin_id"]
        currency = request.params["currency"]
        coin_price = request.params["coin_price"]
        return template("search_wtf", coin_id=coin_name, coin_price=coin_price, currency=currency)
    return template("search_wtf", coin_id=None, coin_price=None, currency=None)