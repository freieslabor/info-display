var displayDate;
var timer;

function refresh() {
  displayDate = new Date().add(-6).hours().set({minute: 0});
  update();
}

function update() {
  // FIXME: if screen loses focus, return
  displayDate.add(30).minutes();
  if (displayDate.compareTo(new Date()) == 1) {
    return;
  }
  $("#picture-container").append($("<img>").addClass("webcam-img").attr("src", function( i, val ) {
    return "http://webcamberry/" + displayDate.toString("yyyy-MM-dd") + "/" + displayDate.toString("yyyy-MM-dd_HHmm") + ".jpg";
  }).hide().bind("load", function () {
    $(this).fadeIn(180, function() {
      if ($("#picture-container").children().length > 1) {
        $("#picture-container").children().first().remove();
        timer = setTimeout(update, 190);
      }
      $("#date").remove();
      $("<div>").text(displayDate.toString("dd.MM.yyyy HH:mm")).appendTo($("#picture-container")).attr("id", "date");
    });
  }));
}
