$ = jQuery;
$(function(){

    var test = 18000;
    if ($(window).width() <= 600){
        test = 20000;
    }

    // Slideshow on product homepages     
    $('#productCarousel').carousel({
        interval: test
    });
        
    $('#productCarousel .tabs a').click(function(){
        $('#productCarousel').carousel($(this).closest('li').index());
        $('#productCarousel .tabs li').removeClass('active-tab');
        $(this).closest('li').addClass('active-tab');
        return false;
    });
    $('#productCarousel').bind('slid', function (e) {
        $('#productCarousel .tabs li').removeClass('active-tab');
        var i = $(this).find('.item.active').index();
        $('#productCarousel .tabs li').eq(i).addClass('active-tab');
    });
    
    // Slideshow on the Support team focus
    $('#supportCarousel').carousel({
        interval: 10000
    });
    
    // Accordion on the Support team focus
    $('.collapse').collapse('accordion-group');

    // Tooltips and popovers (Bootstrap)
    $('[rel=tooltip]').tooltip('hide');
    $('[rel=popover]').popover('hide');

});
