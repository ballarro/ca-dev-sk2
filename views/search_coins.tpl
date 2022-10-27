% rebase("base.tpl")

<aside></aside>
<div class="container">
    <form action="">
        <div class="form-row">
            <label for="coin_name">Coin Name: </label>
            <input type="text" name="coin_name" />
        </div>
        <div class="form-row">
            <label for="currency">Currency: </label>
            <select name="currency">
                <option value="aud">Australian Dollars</option>
                <option value="eur">Euro Dollars</option>
                <option value="gpb">British Lbs</option>
                <option value="usd">USD Dollars</option>
            </select>
        </div>
        <div class="form-row">
            <input type="submit" value="Search" />
        </div>
    </form>
    % if coin_id:
    <div class="form-row">
        <h2>The price of {{ coin_id }} is {{ coin_price }} {{ currency }}.</h2>
    </div>
    % end
</div>