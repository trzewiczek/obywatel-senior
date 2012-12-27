<div class="row">
    <div class="twelve columns">
        <h5>Wypełnij poniższe pola by dodać nową notatkę</h5>
    </div>
</div>

<div class="row">
    <div class="panel twelve columns">

        %if note:
        <form action="/notatki/{{note['id']}}" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Tytuł notatki</h5>
                <input type="text" name="title" placeholder="Tytuł" value="{{note['title']}}" /> 

                <h5>Autor notatki</h5>
                <input type="text" name="author" placeholder="Autor" value="{{note['author']}}" /> 
            </div>
        </div>
        <div class="row">
            <div class="twelve columns">
                <h5>Treść notatki</h5>
                <textarea id="editor1" rows="20" name="text" placeholder="Treść notatki">{{note['text']}}</textarea>
        %else:
        <form action="/notatki/nowa" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Tytuł notatki</h5>
                <input type="text" name="title" placeholder="Tytuł" value="" /> 

                <h5>Autor notatki</h5>
                <input type="text" name="author" placeholder="Autor" value="" /> 
            </div>
        </div>
        <div class="row">
            <div class="twelve columns">
                <h5>Treść notatki</h5>
                <textarea id="editor1" rows="20" name="text" placeholder="Treść notatki"></textarea>
        %end
                <br />

                <div class="row">
                    <div class="eight columns">
                        <input type="submit" class="large radius success button" value="Zapisz" />
                    </div>
                    <div class="four columns">
                        <a href="#" data-target="/notatki" class="right small alert radius button cancel">Rezygnuj</a>
                    </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</div>

%rebase return target='/notatki'
