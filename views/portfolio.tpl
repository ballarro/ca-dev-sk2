% rebase("base.tpl")

<ul>
% for coin in portfolio:
    <li style="color: {{ 'red' if coin.current < coin.buy else 'black' }}">
    {{ coin.coin_id }} - ${{ coin.current }}
    </li>
% end
</ul>

<%
current_value = [coin.current * coin.quantity for coin in portfolio]
portfolio_value = sum(current_value)
total_tax = portfolio_value * 0.2 if portfolio_value > 25000 else portfolio_value * 0.12
%>
<h2>Total tax: ${{total_tax}}</h2>