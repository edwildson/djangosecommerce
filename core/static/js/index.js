$(function() {
    var locale = $('body').data('lang');

    $('.navbar-header, .search-responsive-collapse .search_mask')
      .click(function(e) {
        if ($(e.target).parent().is($('.mobile_search')) ||
            $(e.target).is($('#mobile_search_btn'))) {
          return;
        }

        if ($('.search-responsive-collapse').hasClass('in')) {
          $('input#mobile_search_btn').click();
          $('.search-responsive-collapse').collapse('hide');
        }
      });

      $('.navbar-header, .bread_mask').click(function(e) {
        if ($('.bread_mask').is(':visible')) {
          $('input#mobile_breadcrumb_btn').click();
        }
      });
      $('.menu_mask').click(function() {
        $('input#mobile_menu_btn').click();
      });
    
      // Dropdown menu collapse
      $('.dropdown-accordion')
          .on('click', 'a[data-toggle="collapse"]', function(event) {
            event.preventDefault();
            event.stopPropagation();
            $($(this).data('parent')).find('.panel-collapse.in').collapse('hide');
            $($(this).attr('href')).collapse('show');
          });
    });
    
var change_language =
    {
      post: function(url, language) {
        $.post(url, language, function(data) {
          window.location.href = window.location.href;
        });
      }
    }