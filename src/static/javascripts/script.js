;(function ($) {
    var path = window.location['pathname'].slice(1);
    $('li.active').removeClass('active');
    $('#nav-'+path).addClass('active');
})(jQuery);
