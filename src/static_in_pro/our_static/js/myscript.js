$('#project_filters > ul.nav-pills li').click(function(e) {
    $('.nav li.active').removeClass('active');
    var $this = $(this);
    $this.addClass('active');
    e.preventDefault();
});

