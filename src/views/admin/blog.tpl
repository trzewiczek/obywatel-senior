  <div class="row">
    <div class="twelve columns">
        <a href="/admin/blog/new" class="large radius success button">Dodaj nowy wpis</a>
    </div>
  </div>

  <div class="row">
    <hr />
  </div>

  <div class="row">
    <div class="twelve columns">
        <h5>
        % if posts:
        Poniżej znajduje się lista wpisów na blogu
        % else:
        Nie ma jeszcze żadnych wpisów. Do roboty!
        % end
        </h5>
    </div>
  </div>

  %for post in posts:
    <div class="row">
        <div class="twelve columns radius panel">

            <div class="nine columns r-border">
                <div class="row">
                    <div class="twelve columns">
                        <h5>{{!post['date']}}, {{post['author']}}</h5>
                        <h3>{{!post['title']}}</h3>
                        %if post['path']:
                        <img src="{{post['path']}}" />
                        %end
                        <p>{{!post['text']}}</p>
                    </div>
                </div>
            </div>

            <div class="three columns">
                <div class="row">
                    <div class="eight columns">
                        <a href="/admin/blog/{{post['id']}}" class="large  radius button right">Edytuj</a>
                    </div>
                    <div class="four columns">
                        <a href="#" data-target="/admin/blog/{{post['id']}}/delete" class="right small alert radius button delete">Usuń</a>
                    </div>
                </div>
            </div>
        
        </div>
    </div>
  %end
  
%rebase layout
