<div class="row">
    <div class="twelve columns">
        <h5>Wypełnij poniższe pola by dodać nowe zadanie</h5>
    </div>
</div>

<div class="row">
    <div class="panel twelve columns">

        <form action="/admin/terminarz/nowe" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Nazwa zadania</h5>
                <input type="text" name="title" placeholder="Nazwa" value="" /> 

                <h5>Osoba odpowiedzialna</h5>
                <select name="person">
                %for user in users:
                    <option value="{{user}}">{{user}}</option>
                %end
                </select>

                <h5>Termin wykonania</h5>
                <input type="text" name="date" placeholder="Termin" value="" id="datepicker" /> 
            </div>
        </div>
        <div class="row">
            <div class="twelve columns">
                <h5>Opis zadania (nie jest konieczny)</h5>
                <textarea id="editor1" rows="20" name="text" placeholder="Opis"></textarea>

                <br />

                <div class="row">
                    <div class="eight columns">
                        <input type="submit" class="large radius success button" value="Zapisz" />
                    </div>
                    <div class="four columns">
                        <a href="#" data-target="/admin/terminarz" class="right small alert radius button cancel">Rezygnuj</a>
                    </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</div>

%rebase return target='/terminarz'
