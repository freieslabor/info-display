// resizing
function resize_main() {
    $('main').css('height', ($(window).height() - $('footer').height()))
}

$(document).ready(function() {
    resize_main();
});

$(window).resize(function() {
    resize_main();
});


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
            $('span#room-state').removeClass('open closed');

            if(data.open) {
                $('span#room-state').addClass('open').html('OPEN');
            } else {
                $('span#room-state').addClass('closed').html('CLOSED');
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
var screen_cycle_timeout = 0;

function setup_screen_cycle() {
    screen_cycle_timeout = setTimeout(function() {
        show_next_screen();
        update_screen_state();
        setup_screen_cycle();
    }, 5000);
}

setup_screen_cycle();


$(document).keydown(function(event) {
    switch(event.which) {
        case 37: // left
            clearTimeout(screen_cycle_timeout);
            show_previous_screen();
            update_screen_state();
            setup_screen_cycle();
            break;

        case 39: // right
            clearTimeout(screen_cycle_timeout);
            show_next_screen();
            update_screen_state();
            setup_screen_cycle();
            break;

        case 32: // space
            if(screen_cycle_timeout == 0) {
                setup_screen_cycle();
            } else {
                clearTimeout(screen_cycle_timeout);
                screen_cycle_timeout = 0;
            }

            break;

        default:
            return;
    }

    event.preventDefault();
});
