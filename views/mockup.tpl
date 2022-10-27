<!doctype html>
<html>
    <head>
        <link href="/static/styles/main.css" rel="stylesheet">
    </head>
    <body>
        <div class="wrapper">
            <header>
                <h3>Crypto Tracker</h3>
            </header>
            <main>
                <aside>
                    <ul>
                        <li><a href="/portfolio/bitcoin">Bitcoin</a></li>
                        <li><a href="/portfolio/ethereum">Ethereum</a></li>
                        <li><a href="/portfolio/solana">Solana</a></li>
                    </ul>
                </aside>
                <h2>The price of {{ coin_id }} is {{ coin_price }}.</h2>
            </main>
            <footer>
                <h4>Prices courtesy of <a href="https://coingecko.com">Coin Gecko</a>.</h4>
            </footer>
        </div>
    </body>
</html>