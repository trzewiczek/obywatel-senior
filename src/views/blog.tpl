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
    <div class="twelve columns">

      %for post in posts:
        <div class="row">
            <div class="twelve columns">
                <h3>{{!post['title']}}</h3>
                <h5>{{!post['date']}}, {{post['author']}}</h5>
                <img src="{{post['path']}}" />
                <p>{{!post['text']}}</p>
            </div>
        </div>
      %end

    </div>
  </div>

  </div>
</div>
  
%rebase base
