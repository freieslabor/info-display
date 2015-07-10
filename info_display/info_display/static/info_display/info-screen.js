// clock
function update_clock() {
    var date_obj = new Date();
    var timestring = ('0' + date_obj.getHours()).slice(-2) + ':' + ('0' + date_obj.getMinutes()).slice(-2) + ':' + ('0' + date_obj.getSeconds()).slice(-2);

    $('span#clock').html(timestring);
}

update_clock();
var clock_interval = setInterval(update_clock, 1000);


// room_state
function update_room_state() {
    $.getJSON('https://freieslabor.org/api/room/', function(data) {
        if(data.open != room_open) {
            $('span#room-state').removeClass('open close');

            if(data.open) {
                $('span#room-state').addClass('open').html('OPEN');
            } else {
                $('span#room-state').addClass('close').html('CLOSED');
            }

            room_open = data.open;
        }
    });
}

var room_open;
update_room_state();
var room_state_interval = setInterval(update_room_state, 10000);


// screen info
function update_screen_state() {
    var screens = get_info();

    $('span#screen-state').html('Screen ' + String(screens[1]+1) + '/' + String(screens[0]));
}

update_screen_state();


// screen cycling
var screen_cycle_interval = setInterval(function() {
    show_next_screen();
    update_screen_state();
}, 5000);
