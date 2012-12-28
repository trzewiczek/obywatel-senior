<div class="row">
    <div class="twelve columns">
        <h5>Wypełnij poniższe pola by dodać nowe zadanie</h5>
    </div>
</div>

<div class="row">
    <div class="panel twelve columns">

        <form action="/terminarz/nowe" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Nazwa zadania</h5>
                <input type="text" name="title" placeholder="Nazwa" value="" /> 

                <h5>Osoba odpowiedzialna</h5>
                <input type="text" name="person" placeholder="Osoba" value="" /> 

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
                        <a href="#" data-target="/terminarz" class="right small alert radius button cancel">Rezygnuj</a>
                    </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</div>

%rebase return target='/terminarz'
