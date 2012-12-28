  <div class="row">
    <div class="twelve columns">
        <a href="/adresy/nowy" class="large radius success button">Dodaj nowy adres</a>
    </div>
  </div>

  <div class="row">
    <hr />
  </div>

  <div class="row">
    <div class="twelve columns">
        <h5>
        % if addresses:
        Poniżej znajduje się lista notatek
        % else:
        Nie ma jeszcze żadnych notatek. Do roboty!
        % end
        </h5>
    </div>
  </div>

  %for adrs in addresses:
    <div class="row">
        <div class="twelve columns radius panel">

            <div class="nine columns r-border">
                <div class="row">
                    <div class="twelve columns">
                        <h3>{{adrs['name']}}</h3>
                        <h5>{{adrs['person']}}</h5>
                        <div class="row">
                            <div class="six columns address">
                                <div>{{adrs['address']}}</div>
                                <div>{{adrs['zip']}} {{adrs['city']}}</div>
                            </div>
                            <div class="six columns address">
                                <div><span class="light">t:</span> {{adrs['phone']}}</div>
                                <div><span class="light">e:</span> {{adrs['email']}}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="three columns">
                <div class="row">
                    <div class="eight columns">
                        <a href="/adresy/{{adrs['id']}}" class="large  radius button right">Edytuj</a>
                    </div>
                    <div class="four columns">
                        <a href="#" data-target="/adresy/{{adrs['id']}}/delete" class="right small alert radius button delete">Usuń</a>
                    </div>
                </div>
                <br />
                <div class="row">
                    <div class="twelve columns">
                        <p>
                            %if adrs['newsletter']:
                            <input type="checkbox" data-id="{{adrs['id']}}" name="newsletter" checked class="finger" /> 
                            %else:
                            <input type="checkbox" data-id="{{adrs['id']}}" name="newsletter" class="finger" /> 
                            %end
                            <strong class="newsletter-checkbox finger">Newsletter</strong>
                        </p>
                    </div>
                </div>
            </div>
        
        </div>
    </div>
  %end
  
%rebase layout
