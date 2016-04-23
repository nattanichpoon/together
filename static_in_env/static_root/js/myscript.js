

jQuery(document).ready(function() {
  if ($('.cd-stretchy-nav').length > 0) {
    var stretchyNavs = $('.cd-stretchy-nav');

    stretchyNavs.each(function() {
      var stretchyNav = $(this),
        stretchyNavTrigger = stretchyNav.find('.cd-nav-trigger');

      stretchyNavTrigger.on('click', function(event) {
        event.preventDefault();
        stretchyNav.toggleClass('nav-is-visible');
      });
    });

    $(document).on('click', function(event) {
      (!$(event.target).is('.cd-nav-trigger') && !$(event.target).is('.cd-nav-trigger span')) && stretchyNavs.removeClass('nav-is-visible');
     
    });

  }
  $('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');
});


  $('#project_filters > ul.nav-pills li').click(function(e) {
    $('.nav li.active').removeClass('active');
    var $this = $(this);
    $this.addClass('active');
    e.preventDefault();
});

