;(function ($) {
    var path = window.location['pathname'].split('/')[2];
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

    if($('#blog_upload_button').hasClass('alert')) {
        $('#blog_upload_button').click(remove_image);
    }
    else {
        $('#blog_upload_button').click(upload_image);
    }
    function upload_image() {
        // on choose photo
        var form = [];
        form.push('<form id="blog_upload_photo" ');
        form.push('action="/admin/blog/upload" ');
        form.push('method="POST" ');
        form.push('enctype="multipart/form-data">');
        form.push('<input id="file_input" type="file" name="upload" />');
        form.push('</form>');
        form = $(form.join(''));
        $('#blog_upload_placeholder').append(form);

        form.ajaxForm(function (data) {
            var img  = '<img id="preview_image" src="'+data+'" />';
            var path = '<input id="path" type="hidden" name="path" value="'+data+'" />';

            $('#blog_add_new').append(path);
            $('#blog_upload_placeholder').empty().append(img);
            $('#blog_upload_button').html('Usuń')
                                    .removeClass('confirm')
                                    .addClass('alert')
                                    .unbind('click')
                                    .click(remove_image);
        });

        $(this).html('Dodaj zdjęcie')
               .removeClass('success')
               .addClass('confirm')
               .unbind('click')
               .click(function () {
            // on upload photo
            form.submit();
        });
    }

    function remove_image() {
        // on remove photo
        $('#preview_image').remove();
        $('#path').remove();
        $(this).html('Wybierz zdjęcie')
               .removeClass('alert')
               .addClass('success')
               .unbind('click')
               .click(upload_image);
    }


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
