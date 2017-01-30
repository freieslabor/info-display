function detail_table(part) {
  $('#name').text(part.name);
  $('#description').text(part.description);
  $('#category').text(part.categoryPath);
  $('#location').text(part.storageLocation.name);

  if (part.partCondition != null && part.partCondition != '')
    part.status = part.status + '/' + part.partCondition;

  $('#status').text(part.status);

  if (part.attachments.length > 0 && part.attachments[0].isImage) {
    $('#photo').attr('src', '/partkeepr_search/img/' + part.attachments[0]['@id'].split('/').pop());
  } else {
    $('#photo').attr('src', '/static/partkeepr_search/img/no_picture.png');
  }

  $('#location-map1').inventory_overview(part.storageLocation.name);
  $('#location-map2').inventory_detail(part.storageLocation.name);
}

$(document).ready(function() {
  $('#search-input').searchbox({
    url: '/partkeepr_search/search.json',
    param: 'q',
    dom_id: '#results',
  });
});

$(document).keyup(function(e) {
  // ignore cursor keys
  if (e.which >= 37 && e.which <= 40) return;
  if ($('#search-input').val() == '') {
    if (e.which == 8 || e.which == 27) {
      if ($('#search-input').is(":focus")) $('#partkeepr-detail').hide();
    } else {
      $('#partkeepr-detail').show();
      $('#search-input').focus();
    }
  }
});
