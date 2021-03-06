<div class="row">
    <div class="twelve columns">
        <h5>Wypełnij poniższe pola by dodać wpis na bloga</h5>
    </div>
</div>

<div class="row">
    <div class="panel twelve columns">

        %if post:
        <form action="/blog/{{post['id']}}" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Tytuł wpisu</h5>
                <input type="text" name="title" placeholder="Tytuł" value="{{post['title']}}" /> 

                <h5>Autor wpisu</h5>
                <input type="text" name="author" placeholder="Autor" value="{{post['author']}}" /> 
            </div>
        </div>
        <div class="row">
            <div class="twelve columns">
                <h5>Treść wpisu</h5>
                <textarea id="editor1" rows="20" name="text" placeholder="Treść wpisu">{{post['text']}}</textarea>
        %else:
        <form action="/blog/new" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Tytuł wpisu</h5>
                <input type="text" name="title" placeholder="Tytuł" value="" /> 

                <h5>Autor wpisu</h5>
                <input type="text" name="author" placeholder="Autor" value="" /> 
            </div>
        </div>
        <div class="row">
            <div class="twelve columns">
                <h5>Treść wpisu</h5>
                <textarea id="editor1" rows="20" name="text" placeholder="Treść wpisu"></textarea>
        %end
                <br />

                <div class="row">
                    <div class="eight columns">
                        <input type="submit" class="large radius success button" value="Zapisz" />
                    </div>
                    <div class="four columns">
                        <a href="#" data-reveal-id="myModal" data-target="/blog" class="right small alert radius button cancel">Rezygnuj</a>
                    </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</div>

%rebase return target='/blog'
