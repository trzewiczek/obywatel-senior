  <div class="row">
    <div class="twelve columns">
        <a href="/admin/notatki/nowa" class="large radius success button">Dodaj nową notatkę</a>
    </div>
  </div>

  <div class="row">
    <hr />
  </div>

  <div class="row">
    <div class="twelve columns">
        <h5>
        % if notes:
        Poniżej znajduje się lista notatek
        % else:
        Nie ma jeszcze żadnych notatek. Do roboty!
        % end
        </h5>
    </div>
  </div>

  %for note in notes:
    <div class="row">
        <div class="twelve columns radius panel">

            <div class="nine columns r-border">
                <div class="row">
                    <div class="twelve columns">
                        <h5>{{!note['date']}}, {{note['author']}}</h5>
                        <h3>{{!note['title']}}</h3>
                        <p>{{!note['text']}}</p>
                    </div>
                </div>
            </div>

            <div class="three columns">
                <div class="row">
                    <div class="eight columns">
                        <a href="/admin/notatki/{{note['id']}}" class="large  radius button right">Edytuj</a>
                    </div>
                    <div class="four columns">
                        <a href="#" data-target="/admin/notatki/{{note['id']}}/delete" class="right small alert radius button delete">Usuń</a>
                    </div>
                </div>
            </div>
        
        </div>
    </div>
  %end
  
%rebase layout
