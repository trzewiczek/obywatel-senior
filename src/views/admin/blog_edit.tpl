<div class="row">
    <div class="twelve columns">
        <h5>Wypełnij poniższe pola by dodać wpis na bloga</h5>
    </div>
</div>

<div class="row">
    <div class="panel twelve columns">

        %if post:
        <form id="blog_add_new" action="/admin/blog/{{post['id']}}" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Tytuł wpisu</h5>
                <input type="text" name="title" placeholder="Tytuł" value="{{post['title']}}" /> 

            </div>
        </div>
        <div class="row">
            <div class="eight columns">

                <h5>Zdjęcie tytułowe</h5>
                %if post['path']:
                    <div id="blog_upload_placeholder" class="left" style="margin-right: 15px;">
                        <img id="preview_image" src="{{post['path']}}" />
                    </div>
                    <div id="blog_upload_button" class="small radius alert button">Usuń</div>
                %else:
                    <div id="blog_upload_placeholder" class="left" style="margin-right: 15px;"></div>
                    <div id="blog_upload_button" class="small radius success button">Wybierz zdjęcie</div>
                %end

            </div>
        </div>
        <div class="row">
            <div class="twelve columns">
                <h5>Treść wpisu</h5>
                <textarea id="editor1" rows="20" name="text" placeholder="Treść wpisu">{{post['text']}}</textarea>
        %else:
        <form id="blog_add_new" action="/admin/blog/new" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Tytuł wpisu</h5>
                <input type="text" name="title" placeholder="Tytuł" value="" /> 

            </div>
        </div>
        <div class="row">
            <div class="eight columns">

                <h5>Zdjęcie tytułowe</h5>
                <div id="blog_upload_placeholder" class="left" style="margin-right: 15px;"></div>
                <div id="blog_upload_button" class="small radius success button">Wybierz zdjęcie</div>

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
                        <a href="#" data-reveal-id="myModal" data-target="/admin/blog" class="right small alert radius button cancel">Rezygnuj</a>
                    </div>
                </div>
            </div>
        </div>
        </form>
    </div>
</div>

%rebase return target='/blog'
