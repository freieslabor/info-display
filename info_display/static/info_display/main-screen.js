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


// popup timeout
var popup_timeout = 0;

function setup_popup_timeout() {
    clearTimeout(popup_timeout);

    popup_timeout = setTimeout(function() {
        ractive.set('mode', 'normal');
    }, 5000);
}


// keyboard
$(document).keydown(function(event) {
    var mode = ractive.get('mode');
    var key = event.which;

    var movement_keys = [
        32,  // Space
        37,  // left
        38,  // up
        39,  // right
        40,  // down
        73,  // inventar
    ];

    // idle timeout
    if(mode != 'normal') {
        setup_popup_timeout();
    }

    // open help
    if(mode == 'normal' && movement_keys.indexOf(key) == -1) {
        ractive.set('mode', 'help');

        return;
    }

    // hanle keys
    switch(key) {
        case 27: // ESC
            ractive.set('mode', 'normal');
            break;

        case 73: // i (Inventar)
            if(ractive.get('mode') != 'inventar') {
                event.preventDefault();

                ractive.set('mode', 'inventar');
                ractive.set('inventar.query', '');
                ractive.set('inventar.selected_item', 0);

                $('#inventar-query').focus();
            }

            break;

        case 37: // left
            if(mode == 'normal') {
                clearTimeout(screen_cycle_timeout);
                show_previous_screen();
                update_screen_state();
                setup_screen_cycle();

            } else if(mode == 'inventar') {
                event.preventDefault();

            }

            break;

        case 38: // up
            // inventar result scrolling
            if(ractive.get('mode') == 'inventar') {
                var result_length = ractive.get('inventar_results').length;
                var selected_item = ractive.get('inventar.selected_item');

                selected_item--;

                if(selected_item < 0) {
                    selected_item = result_length - 1;
                }

                ractive.set('inventar.selected_item', selected_item);

                event.preventDefault();
            }

            break;

        case 40: // down
            // inventar result scrolling
            if(ractive.get('mode') == 'inventar') {
                var result_length = ractive.get('inventar_results').length;
                var selected_item = ractive.get('inventar.selected_item');

                selected_item++;

                if(selected_item >= result_length) {
                    selected_item = 0;
                }

                ractive.set('inventar.selected_item', selected_item);

                event.preventDefault();
            }

            break;

        case 39: // right
            if(mode == 'normal') {
                clearTimeout(screen_cycle_timeout);
                show_next_screen();
                update_screen_state();
                setup_screen_cycle();

            } else if(mode == 'inventar') {
                ractive.set('inventar.query',
                            ractive.get('inventar_results')[ractive.get('inventar.selected_item')]);

            }

            break;

        case 32: // space
            if(mode == 'normal') {
                if(screen_cycle_timeout == 0) {
                    setup_screen_cycle();

                } else {
                    clearTimeout(screen_cycle_timeout);
                    screen_cycle_timeout = 0;
                }
            }
    }
});

Ractive.debug = true;

var ractive = new Ractive({
    el: '#ractive',
    template: '#popup',
    data: {
        mode: 'normal',
        inventar: {
            query: '',
            selected_item: 0
        }
    },
    computed: {
        inventar_results: function() {
            var results = [];
            var q = ractive.get('inventar.query');

            for(var i=0; i<q.length; i++) {
                results.push(q.repeat(i + 1));
            }

            ractive.set('inventar.selected_item', 0);

            return results;
        }
    }
});
