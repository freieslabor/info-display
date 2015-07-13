function showError(msg) {
	$("#public-transport-schedule").append($("<li>").addClass("error")
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
		if (data.length == 0) {
			showError("Keine Verbindungen gefunden.");
			return;
		}

		$("#title").html("Verbindungen von \"" + data[0].station_name + "\"");

		$('#public-transport-schedule').empty();

		$.each(data, function (index, connection) {
			// generate date string
			var connection_date = new Date(connection.date);
			var tomorrow = new Date.today().add(1).day();
			var date_str = connection_date.toString("HH:mm");

			if (connection_date.getDayName() == tomorrow.getDayName()) {
				date_str = "morgen, " + date_str;
			}

			// append new schedule line
			var newLi = $("<li>");
			newLi.append(date_str);
			newLi.append($("<span>").append(" " + connection.line + " ")
				.addClass("numberCircle"));
			newLi.append(connection.direction + " ("
				+ connection.transport_type + ")");

 			$("#public-transport-schedule").append(newLi);
		});
	}).fail(function() {
		showError("Fehler beim Laden des Plans");
	});
}
