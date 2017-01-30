(function($){
  $.fn.inventory = function(storage_key, background, location_json) {
    var container = this;

    this.empty();
    this.addClass('grundriss-container');

    // load hidden background image
    $('<img>')
      .attr('src', background)
      .hide()
      .addClass('grundriss')
      .appendTo(this).load(function() {
        // original svg dimensions
        var original_width = $(this).width();
        var original_height = $(this).height();

        // container dimensions
        var display_width = parseInt(container.css('width'));
        var display_height = parseInt(container.css('height'));

        // resize for display (use container dimensions) and show
        $(this)
          .css('width', display_width + 'px')
          .css('height', display_height + 'px')
          .show();

        // marker
        $.getJSON(location_json, function(mapping) {
          // load hidden marker image
          $('<img>')
            .attr('src', '/static/partkeepr_search/img/marker.gif')
            .hide()
            .addClass('grundriss-marker').appendTo(container).load(function() {
              if (typeof mapping[storage_key] == 'undefined') {
                alert('No position found for key "' + storage_key + '".');
                return container;
              }
              // horizontal position proportional to image size
              var left = mapping[storage_key][0] / (original_width/display_width);
              // subtract half of the marker image width
              left -= $(this).width() / 2;
              // vertical position proportional to image size
              var bottom = mapping[storage_key][1] / (original_height/display_height);
              // subtract half of the marker image height
              bottom -= $(this).height() / 2;

              // set correct marker position and show
              $(this)
                .css('left', left + 'px')
                .css('bottom', bottom + 'px')
                .show();
            });;
          });
      });

    return this;
  };

  // wrapper function for overview data
  $.fn.inventory_overview = function(storage_location) {
    // storage location consists of a letter identifying the cabinet followed
    // by a number identifying the specific location in the cabinet
    var cabinet = storage_location.charAt(0).toUpperCase();
    var background = '/static/partkeepr_search/img/labor/grundriss_blank.svg';
    var location_json = '/static/partkeepr_search/cabinet-locations.json';
    return $(this).inventory(cabinet, background, location_json);
  };

  // wrapper function for detail data
  $.fn.inventory_detail = function(storage_location) {
    // storage location consists of a letter identifying the cabinet followed
    // by a number identifying the specific location in the cabinet
    var cabinet = storage_location.charAt(0).toUpperCase();
    var number = parseInt(storage_location.substring(1));

    if (isNaN(number)) {
      alert(storage_location + ' is not a valid storage location. Please correct it.');
      return this;
    }
    var background = '/static/partkeepr_search/img/labor/' + cabinet + '.svg';
    var location_json = '/static/partkeepr_search/cabinet-locations-' + cabinet + '.json';
    return $(this).inventory(number, background, location_json);
  };
})(jQuery);
