// global chart config
var config = {
    scaleShowVerticalLines: false,
    animation: false, 
    scaleFontSize: 20, 
    scaleFontColor: "#f2f2f2",
    showTooltips: false
}

var preset_data = {
    labels: [],
    datasets: [
        {
            fillColor: "rgba(151,187,205,0.6)",
            strokeColor: "rgba(151,187,205,0.8)",
            highlightFill: "rgba(220,220,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: []
        }
    ]
};


$(document).ready(function() {
    refresh();
});

function refresh() {
    dow_stats();
    hour_stats();
}

function show_error(elem) {
    $(elem).empty();
    $(elem).append($("<div>").addClass("error").text("Fehler beim Laden der Statistiken."));
}

function dow_stats() {
    // reset chart specifics
    preset_data["datasets"]["data"] = [];
    preset_data["labels"] = [];

    // create chart
    var ctx = $("#diagram-dow")[0].getContext("2d");
    var chart = new Chart(ctx).Bar(preset_data, config);

    // retrieve aggregated data
    $.ajax({
        type: "GET",
        url: "dow.json",
    }).done(function(data) {
        $.each(data, function (index, dow) {
            var weekday = Date.today().moveToDayOfWeek(dow.day_of_week+1).toString("dddd");
            chart.addData([dow.percentage], [weekday]);
        });
        chart.update();
    }).fail(function() {
        show_error("#dow");
    });
}

function hour_stats() {
    // reset chart specifics
    preset_data["datasets"]["data"] = [];
    preset_data["labels"] = [];

    // create chart
    var ctx = $("#diagram-hour")[0].getContext("2d");
    var chart = new Chart(ctx).Bar(preset_data, config);

    // retrieve aggregated data
    $.ajax({
        type: "GET",
        url: "hour.json",
    }).done(function(data) {
        $.each(data, function (index, hour) {
            chart.addData([hour.percentage], [hour.hour]);
        });
        chart.update();
    }).fail(function() {
        show_error("#hour");
    });
}
