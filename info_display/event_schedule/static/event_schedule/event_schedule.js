function showError(msg) {
    $("#event-schedule").append($("<li>").addClass("error")
        .text(msg));
}

$(document).ready(function() {
    refresh();
});

function refresh() {
    $.ajax({
        type: "GET",
        url: "schedule.json",
    }).done(function(data) {
        $('#event-schedule').empty();
        if (data.length == 0) {
            showError("Keine Veranstaltungen gefunden.");
            return;
        }

        $.each(data, function (index, event) {
            // generate date string
            var event_date = new Date(event.date);
            var date_str = event_date.toString("dd.MM. HH:mm");

			if (event_date.compareTo(new Date.today()) == 0) {
                date_str = "heute, " + event_date.toString("HH:mm");
            }

            // append new event item
            var newLi = $("<li>");
            newLi.append(date_str);
            newLi.append(" &ndash; " + event.title);

             $("#event-schedule").append(newLi);
        });
    }).fail(function() {
        showError("Fehler beim Laden des Kalenders.");
    });
}
