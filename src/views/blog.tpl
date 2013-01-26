  <div class="row">
    <div class="twelve columns">
        Obywatel senior
    </div>
  </div>

  <div class="row">
    <hr />
  </div>

  <div class="row">
    <div class="twelve columns">

      %for post in posts:
        <div class="row">
            <div class="twelve columns">
                <h5>{{!post['date']}}, {{post['author']}}</h5>
                <h3>{{!post['title']}}</h3>
                <p>{{!post['text']}}</p>
            </div>
        </div>
      %end

    </div>
  </div>

  
%rebase base
