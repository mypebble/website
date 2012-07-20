$ = jQuery;

// Temp jQuery -- devs to review and remove this comment when done

$(function(){

    /*
    // Login box in .titlerow
    $('.loginbtn').click(function(){
        $(this).siblings('.loginbox').slideDown();
        return false;
    });
    $('.loginbox .close').click(function(){
        $(this).parents('.loginbox').slideUp();
        return false;
    });*/
    
    // Slideshow on product homepages
    $('#productCarousel').carousel({
        interval: 5000
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
