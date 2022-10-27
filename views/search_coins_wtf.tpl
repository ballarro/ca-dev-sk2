% rebase("base.tpl")


<aside></aside>
<div class="container">
    <form action="" method="post">
        <div class="form-class">
            {{! form.coin_id.label }}
            {{! form.coin_id() }}
        </div>
        % if form.coin_id.errors:
        <ul>
            % for error in form.coin_id.errors:
            {{ error }}
            % end
        </ul>
        % end
        <div class="form-class">
            {{! form.currency.label }}
            {{! form.currency() }}
        </div>
        <div class="form-class">
            {{! form.quantity.label }}
            {{! form.quantity() }}
        </div>
        % if form.quantity.errors:
        <ul>
            % for error in form.quantity.errors:
            {{ error }}
            % end
        </ul>
        % end
        <div class="form-row">
            <input type="submit" value="Submit" />
        </div>
    </form>
</div>