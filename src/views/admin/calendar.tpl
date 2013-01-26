  <div class="row">
    <div class="twelve columns">
        <a href="/admin/terminarz/nowe" class="large radius success button">Dodaj nowe zadanie</a>
    </div>
  </div>

  <div class="row">
    <hr />
  </div>

  <div class="row">
    <div class="twelve columns">
        <h5>
        % if todo:
        Poniżej znajduje się lista aktualnych zadań
        % else:
        Nie ma jeszcze żadnych żadnych zadań. Nuda!
        % end
        </h5>
    </div>
  </div>

  %for note in todo:
    <div class="row">
        %if note['overdue']:
        <div class="twelve columns radius panel overdue">
        %else:
        <div class="twelve columns radius panel">
        %end

            <div class="nine columns r-border">
                <div class="row">
                    <div class="twelve columns">
                        <h5>{{!note['date']}}, {{!note['person']}}</h5>
                        <h3>{{note['title']}}</h3>
                        <p>{{!note['text']}}</p>
                    </div>
                </div>
            </div>

            <div class="three columns">
                <div class="row">
                    <div class="twelve columns">
                        <a href="/admin/terminarz/{{note['id']}}" class="large radius button left">Zrobione?</a>
                    </div>
                </div>
            </div>
        
        </div>
    </div>
  %end

    <div class="row">
        <hr />
    </div>

    <!-- W Y K O N A N E -->
    <div class="row">
        <div class="twelve columns">
            <h5>Poniżej znajduje się lista wykonanych zadań</h5>
        </div>
    </div>

  %for note in done:
    <div class="row">
        <div class="twelve columns radius panel">

            <div class="nine columns r-border">
                <div class="row">
                    <div class="twelve columns">
                        <h5>{{!note['date']}}, {{!note['person']}}</h5>
                        <h3>{{note['title']}}</h3>
                        <p>{{!note['text']}}</p>
                    </div>
                </div>
            </div>

            <div class="three columns">
                <div class="row">
                    <div class="twelve columns">
                        <div class="panel yellow radius">
                            <p class="center"><strong>Zrobione!</strong></p>
                        </div>
                    </div>
                </div>
            </div>
        
        </div>
    </div>
  %end
  
%rebase layout
