  <br />

<div class="row">
  <div class="panel radius twelve columns">

  <div class="row">
    <div class="twelve columns">
        <h3>Obywatel senior</h3>
    </div>
  </div>

  <div class="row">
    <hr />
  </div>

  <div class="row">
    <div class="six columns">

        <h4>Grupa pierwsza</h4>

        <div class="row">
            <div class="eleven columns">
              %for post in grp_one:
                <div class="row">
                    <div class="three columns">
                        <h5 class="left" style="color: #888">{{post['date']}}</h5>
                    </div>
                    <div class="nine columns">
                        <h5 class="left">{{!post['title']}}</h5>
                    </div>
                </div>
              %end
            </div>
        </div>

      %if grp_one:
        <a href='/1'>Czytaj całość</a>
      %end
    </div>

    <div class="six columns">

        <h4>Grupa druga</h4>

        <div class="row">
            <div class="eleven columns">
              %for post in grp_two:
                <div class="row">
                    <div class="three columns">
                        <h5 class="left" style="color: #888">{{post['date']}}</h5>
                    </div>
                    <div class="nine columns">
                        <h5 class="left">{{!post['title']}}</h5>
                    </div>
                </div>
              %end
            </div>
        </div>

      %if grp_two:
        <a href='/2'>Czytaj całość</a>
      %end
    </div>

  </div>

  </div>
</div>
  
%rebase base
