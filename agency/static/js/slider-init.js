
$(document).ready(function() {
   $('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav'
  });
  $('.slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.slider-for',
    dots: false,
    centerMode: true,
    focusOnSelect: true,
    variableWidth: true
  });

  $('#fullscreenSlider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    fade: true,
    infinite: false,
  });


  $('.item-for').on('click', function() {

    var index = $(this).parent().index();
    $('#fullscreenSlider').slick('slickGoTo', index);

    $('#fullscreenModal').modal('show');
  });
});



