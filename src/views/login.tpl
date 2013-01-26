<br />

<div class="row">
    <div class="panel twelve columns">

        <form action="/admin/check_login" method="POST">

        <div class="row">
            <div class="eight columns">
                <h5>Wybierz użytkownika</h5>
            </div>
        </div>
        
        <div class="row">
            <div class="eight columns">
                <select name="user">
                %for user in users:
                    <option value="{{user}}">{{user}}</option>
                %end
                </select>
            </div>
        </div>

        <div class="row">
            <div class="eight columns">
                %if error:
                    <h5>Chyba złe hasło. Spróbuj jeszcze raz...</h5>
                %else:
                    <h5>Podaj hasło</h5>
                %end
            </div>
        </div>
        
        <div class="row">
            <div class="eight columns">
                <input type="password" name="pass" placeholder="Hasło" value="" /> 
            </div>
        </div>
        <br />
        <div class="row">
            <div class="eight columns">
                <input type="submit" class="middle radius confirm button" value="Zaloguj!" />
            </div>
        </div>

        </form>
    </div>
</div>

%rebase base
