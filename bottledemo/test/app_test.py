import unittest

from webtest import TestApp

from app import app

class AppTest(unittest.TestCase):
    def test_say_hello(self):
        sut = TestApp(app)
        response = sut.get("/say_hello")
        self.assertEqual(response.status_int,200)

    def test_say_hello_says_hello(self):
        sut = TestApp(app)
        response = sut.get("/say_hello")
        self.assertIn("v1.4", response)

    def test_btc(self):
        sut = TestApp(app)
        response = sut.get("/get_bitcoin_value")
        self.assertEqual(response.status_int,200)

    def test_btc_says_btc(self):
        sut = TestApp(app)
        response = sut.get("/get_bitcoin_value")
        self.assertIn("btc", response)

    def test_eth(self):
        sut = TestApp(app)
        response = sut.get("/get_eth_value")
        self.assertEqual(response.status_int,200)

    def test_eth_says_eth(self):
        sut = TestApp(app)
        response = sut.get("/get_eth_value")
        self.assertIn("eth", response)

    # def test_does_not_exist_does_not_exist(self):
    #     sut = TestApp(app)
    #     response = sut.get("/does_not_exist")
    #     self.assertEqual(response.status_int,500)

    def test_get_price(self):
        sut = TestApp(app)
        response = sut.get("/get_price")
        self.assertEqual(response.status_int,200)

    # def test_get_price_tpl(self):
    #     sut = TestApp(app)
    #     response = sut.get("/get_price_tpl")
    #     self.assertEqual(response.status_int,200)

    # def test_get_price_dec(self):
    #     sut = TestApp(app)
    #     response = sut.get("/get_price_dec")
    #     self.assertEqual(response.status_int,200)

    def test_portfolio(self):
        sut = TestApp(app)
        response = sut.get("/portfolio")
        self.assertEqual(response.status_int,200)

    def test_get_jinja_portfolio(self):
        sut = TestApp(app)
        response = sut.get("/jinja/portfolio")
        self.assertEqual(response.status_int,200)

    def test_search_coins(self):
        sut = TestApp(app)
        response = sut.get("/search_coins")
        self.assertEqual(response.status_int,200)

    def test_register(self):
        sut = TestApp(app)
        response = sut.get("/register")
        self.assertEqual(response.status_int,200)

    def test_register2(self):
        sut = TestApp(app)
        response = sut.get("/register2")
        self.assertEqual(response.status_int,200)

    def test_welcome(self):
        sut = TestApp(app)
        response = sut.get("/welcome")
        self.assertEqual(response.status_int,200)

    def test_search_coins_wtf(self):
        sut = TestApp(app)
        response = sut.get("/search_coins_wtf")
        self.assertEqual(response.status_int,200)

    # def test_search_wtf(self):
    #     sut = TestApp(app)
    #     response = sut.get("/search_wtf")
    #     self.assertEqual(response.status_int,200)

    # def test_api_echo(self):
    #     sut = TestApp(app)
    #     response = sut.get("/api/echo")
    #     self.assertIn("Hello", response)

    # def test_api_echo(self):
    #     sut = TestApp(app)
    #     response = sut.get("/api/echo")
    #     self.assertIn("Hello", response)

    # def test_get_api_portfolio(self):
    #     sut = TestApp(app)
    #     response = sut.get("/api/portfolio")
    #     self.assertEqual(response.status_int,200)

    # def test_api_portfolio_pdf(self):
    #     sut = TestApp(app)
    #     response = sut.get("/api/portfolio/pdf")
    #     self.assertEqual(response.status_int,404)