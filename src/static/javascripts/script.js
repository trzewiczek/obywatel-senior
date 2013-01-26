;(function ($) {
    var path = window.location['pathname'].split('/')[1];
    $('li.active').removeClass('active');
    $('#nav-'+path).addClass('active');

    $('.cancel').click(function () {
        var choice = confirm("Czy na pewno chcesz zrezygnować z edycji?!");
        if(choice) {
            window.location.href = $(this).attr('data-target');
        }
    });
    $('.delete').click(function () {
        var choice = confirm("Czy na pewno chcesz usunąć?!");
        if(choice) {
            window.location.href = $(this).attr('data-target');
        }
    });


    $('.newsletter-checkbox').click(function () {
        var check = $(this).prev();
        check.click();
    });

    $('input:checkbox').change(function () {
        var address_id = $(this).attr('data-id');
        var newsletter = !!($(this).attr('checked')) ? 1 : 0;

        $.get('/admin/adresy/newsletter/'+address_id+'/'+newsletter);
    });
 
    $('.resend').click(function () {
        alert('Newsletter został wysłany!');
    });

    // ckeditor
    CKEDITOR.replace('editor1', {
        filebrowserImageUploadUrl: '/upload',
        language: 'pl',
        height: 400,
        toolbar :
        [
            { name: 'basicstyles', items : [ 'Bold','Italic' ] },
            { name: 'paragraph', items : [ 'NumberedList','BulletedList' ] },
            { name: 'links', items : [ 'Link','Unlink' ] },
            { name: 'insert', items : [ 'Image','Table','HorizontalRule'] },
            { name: 'tools', items : [ 'Maximize','-','About' ] }
        ]
    });


    // datepicker
    $("#datepicker").datepicker({
        firstDay: 1,
        dayNamesMin: [ "Nd", "Pn", "Wt", "Śr", "Cz", "Pt", "So" ],
        monthNames: [ "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień" ],
        dateFormat: "dd.mm.yy"
    });
    
})(jQuery);
