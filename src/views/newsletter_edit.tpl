<div class="row">
    <div class="twelve columns">
        <h5>Wypełnij poniższe pola by wysłać nowy newsletter</h5>
    </div>
</div>

<div class="row">
    <div class="panel twelve columns">

        <form action="/newsletter/send" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Tytuł newslettera</h5>
                <input type="text" name="title" placeholder="Tytuł" value="" /> 

            </div>
        </div>
        <div class="row">
            <div class="twelve columns">
                <h5>Treść newslettera</h5>
                <textarea id="editor1" rows="20" name="text" placeholder="Treść newslettera"></textarea>
                <br />

                <div class="row">
                    <div class="eight columns">
                        <input type="submit" class="large radius success button" value="Wyślij" />
                    </div>
                    <div class="four columns">
                        <a href="#" data-target="/newsletter" class="right small alert radius button cancel">Rezygnuj</a>
                    </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</div>

%rebase return target='/newsletter'
