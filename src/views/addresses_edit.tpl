<div class="row">
    <div class="twelve columns">
        %if address:
        <h5>Wypełnij wybrane pola by zminić wpis w książce adresowej</h5>
        %else:
        <h5>Wypełnij poniższe pola by dodac nowy adres</h5>
        %end
    </div>
</div>

<div class="row">
    <div class="panel twelve columns">

        %if address:
        <form action="/adresy/{{address['id']}}" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Nazwa instytucji</h5>
                <input type="text" name="name" placeholder="Nazwa" value="{{address['name']}}" /> 

                <h5>Osoba kontaktowa (nie jest to konieczne)</h5>
                <input type="text" name="person" placeholder="Osoba" class="optional" value="{{address['person']}}" /> 

                <h5>Ulica</h5>
                <input type="text" name="address" placeholder="Adres" value="{{address['address']}}" /> 

                <h5>Kod pocztowy</h5>
                <input type="text" name="zip" placeholder="Kod" value="{{address['zip']}}" /> 

                <h5>Miasto</h5>
                <input type="text" name="city" placeholder="Miasto" value="{{address['city']}}" /> 

                <h5>Telefon (nie jest to konieczne)</h5>
                <input type="text" name="phone" placeholder="Telefon" class="optional" value="{{address['phone']}}" /> 

                <h5>Email (nie jest to konieczne)</h5>
                <input type="text" name="email" placeholder="Email" class="optional" value="{{address['email']}}" /> 

        %else:
        <form action="/adresy/nowa" method="POST">
        <div class="row">
            <div class="eight columns">

                <h5>Nazwa instytucji</h5>
                <input type="text" name="name" placeholder="Nazwa" value="" /> 

                <h5>Osoba kontaktowa (nie jest to konieczne)</h5>
                <input type="text" name="person" placeholder="Osoba" class="optional" value="" /> 

                <h5>Ulica</h5>
                <input type="text" name="address" placeholder="Adres" value="" /> 

                <h5>Kod pocztowy</h5>
                <input type="text" name="zip" placeholder="Kod" value="" /> 

                <h5>Miasto</h5>
                <input type="text" name="city" placeholder="Miasto" value="" /> 

                <h5>Telefon (nie jest to konieczne)</h5>
                <input type="text" name="phone" placeholder="Telefon" class="optional" value="" /> 

                <h5>Email (nie jest to konieczne)</h5>
                <input type="text" name="email" placeholder="Email" class="optional" value="" /> 

        %end
            </div>
        </div>

        <div class="row">
            <div class="eight columns">
                <input type="submit" class="large radius success button" value="Zapisz" />
            </div>
            <div class="four columns">
                <a href="#" data-target="/adresy" class="right small alert radius button cancel">Rezygnuj</a>
            </div>
        </div>
        </form>
    </div>
</div>

%rebase return target='/adresy'
