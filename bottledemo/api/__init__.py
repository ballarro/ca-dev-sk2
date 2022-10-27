from bottle import Bottle, response, request
from faker import Faker

from pygecko.crypto_prices import simple_single_price

api_routes = Bottle()

portfolio = {
    "investments": {}
}

@api_routes.get("/api/echo")
def api_echo():
    response.set_header("Content-Type", "application/json")
    return{"Hello": "World"}

@api_routes.get("/api/coin/<coin_id>")
def api_coin(coin_id):
    price = simple_single_price(coin_id, "usd")
    response.set_header("Content-Type", "application/json") 
    return{"coin_id": coin_id, "price": price} 

@api_routes.post("/api/portfolio/<coin_id>")
def api_portfolio_new(coin_id):
    global portfolio
    response.set_header("Content-Type", "application/json")
    if coin_id in portfolio["investments"].keys():
        error = f"coin_id {coin_id} already in portfolio"
        return{"error": error}
    quantity = request.json["quantity"]
    portfolio["investments"][coin_id] = quantity
    response.status = 201
    return { coin_id: quantity}

@api_routes.get("/api/portfolio")
@api_routes.get("/api/portfolio/<coin_id>")
def api_portfolio(coin_id=None):
    response.set_header("Content-Type", "application/json")
    global portfolio
    if coin_id is None:
        return {
            "investments": [
                {
                    "coin_id": coin_id,
                    "value": simple_single_price(coin_id,"usd") * quantity
                }    for (coin_id, quantity) in portfolio["investments"].items()        
            ]
        }
    if not coin_id in portfolio["investments"].keys():
        return {"coin_id": coin_id, "value": simple_single_price(coin_id, "usd") * portfolio["investments"][coin_id]}
    error = f"No coin_id {coin_id} found"
    return {"error": error}

@api_routes.put("/api/portfolio/<coin_id>")
def api_portfolio_buy_sell(coin_id):
    global portfolio
    response.set_header("Content-Type", "application/json")
    if not coin_id in portfolio["investments"].keys():
        error = f"No coin_id {coin_id} found"
        return{"error": error}
    quantity = request.json["quantity"]
    portfolio["investments"][coin_id] += quantity
    return { "coin_id": coin_id,"quantity": portfolio["investments"][coin_id]}

@api_routes.get("/api/portfolio/pdf")
def api_pdf():
    global portfolio
    fake = Faker()
    pdfname = "-".join(fake.words()) + ".pdf"
    current_dt = datetime.datetime.now()
    datestring = current_dt.strftime("%Y/%m/%d %H:%M")
    y = 725
    c = canvas.Canvas(f"pdfs/{pdfname}")
    c.drawString(100, y, f"Your portfolio as of {datestring}")
    for investment, quantity in portfolio["investments"].items():
        y -= 20
        c.drawString(100, y, f"{investment} {quantity * simple_single_price(investment, 'usd')}")
    c.showPage()
    c.save()
    return static_file(pdfname, root="./pdfs", download="portfolio.pdf")