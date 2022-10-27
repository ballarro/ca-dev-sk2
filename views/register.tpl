% rebase("base.tpl")

<aside></aside>
<div class="container">
    <form action="/register2" method="post" enctype="multipart/form-data">
        <div class="form-row">
            <label for="username">UserName: </label>
            <input type="text" name="username" />
        </div>
        <div class="form-row">
            <label for="password">Password: </label>
            <input type="password" name="password" />
        </div>
        <div class="form-row">
            <label for="confirm">Confirm: </label>
            <input type="password" name="confirm" />
        </div>
        <div class="form-row">
            <label for="avatar">Avatar: </label>
            <input type="file" name="avatar" />
        </div>
        <div class="form-row">
            <label for="description">Description: </label>
            <textarea rows="10" cols="40" name="description"></textarea>
        </div>
        <div class="form-row">
            <input type="submit" value="Submit" />
        </div>
    </form>
    % if user:
    <div>Registered "{{user['username']}}" with password "{{user['password']}}" and description
        "{{user['description']}}"
    </div>
    <div>
        <img src="{{user['avatar_path']}}" />
    </div>
    % end
</div>