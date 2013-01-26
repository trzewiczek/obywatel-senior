  <div class="row">
    <div class="twelve columns">
        Obywatel senior
    </div>
  </div>

  <div class="row">
    <hr />
  </div>

  <div class="row">
    <div class="six columns">

      %for post in grp_one:
        <div class="row">
            <div class="twelve columns">

                <h5>{{!post['title']}}</h5>

            </div>
        </div>
      %end

    <a href='/1'>Czytaj całość</a>
    </div>

    <div class="six columns">

      %for post in grp_two:
        <div class="row">
            <div class="twelve columns">

                <h5>{{!post['title']}}</h5>

            </div>
        </div>
      %end

    <a href='/2'>Czytaj całość</a>
    </div>
  </div>

  
%rebase base
