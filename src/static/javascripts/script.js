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

})(jQuery);
