  <div class="row">
    <div class="twelve columns">
        <a href="/newsletter/nowy" class="large radius success button">Wyślij  nowy newsletter</a>
    </div>
  </div>

  <div class="row">
    <hr />
  </div>

  <div class="row">
    <div class="twelve columns">
        <h5>
        % if letters:
        Poniżej znajduje się lista dotychczas wysłanych newsletterów
        % else:
        Nie wyslano jeszcze żadnych newsletterów. Bierzemy się do pracy!
        % end
        </h5>
    </div>
  </div>

  %for letter in letters:
    <div class="row">
        <div class="twelve columns radius panel">

            <div class="nine columns r-border">
                <div class="row">
                    <div class="twelve columns">
                        <h5>{{!letter['date']}}</h5>
                        <h3>{{letter['title']}}</h3>
                        <p>{{!letter['text']}}</p>
                    </div>
                </div>
            </div>

            <div class="three columns">
                <div class="row">
                    <div class="twelve columns">
                        <a href="/newsletter/{{letter['id']}}" class="resend large radius button left">Wyślij ponownie</a>
                    </div>
                </div>
            </div>
        
        </div>
    </div>
  %end
  
%rebase layout
