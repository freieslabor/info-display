function show_next_screen() {
    var screens = $('iframe.screen');
    var active_screen = $(screens).index($('iframe.screen.active'));

    $(screens).removeClass('active');

    if(active_screen + 1 >= $(screens).length) {
        $(screens[0]).addClass('active');
    } else {
        $(screens[active_screen + 1]).addClass('active');
    }
}

function show_previous_screen() {
    var screens = $('iframe.screen');
    var active_screen = $(screens).index($('iframe.screen.active'));

    $(screens).removeClass('active');

    if(active_screen - 1 >= 0) {
        $(screens[active_screen - 1]).addClass('active');
    } else {
        $(screens[$(screens).length - 1]).addClass('active');
    }
}

function show_screen(index) {
    var screens = $('iframe.screen');

    if(index < 0 || index > $(screens).length - 1) {
        return false;
    }

    $(screens).removeClass('active');
    $(screens[index]).addClass('active');

    return index;
}
