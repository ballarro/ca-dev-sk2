from wtforms import Form, StringField, FloatField, SelectField, validators

class SearchForm(Form):
    coin_id = StringField("Coin ID", validators=[validators.input_required()])
    currency = SelectField(
        "Currency",
        choices=[
            ("uad", "Aus Dollars"),
            ("eur", "Euro Dollars"),
            ("gbp", "Britih Lbs"),
            ("usd", "United States Dollars")
        ]
    )
    quantity = FloatField("Quantity", validators=[validators.number_range(min=0.0)])