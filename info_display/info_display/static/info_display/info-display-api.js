var screens = $('iframe.screen');

function get_info() {
    return new Array(screens.length, screens.index($('iframe.screen.active')));
}

function show_next_screen() {
    var next_screen_index = screens.index($('iframe.screen.active')) + 1;

    if(next_screen_index >= screens.length) {
        next_screen_index = 0;
    }

    try {
        $(screens)[next_screen_index].contentWindow.refresh();
    } catch(error) {
        /* nah... nevermind! */
    }

    $(screens).removeClass('active');
    $(screens[next_screen_index]).addClass('active');
}

function show_previous_screen() {
    var previous_screen_index = screens.index($('iframe.screen.active')) - 1;

    if(previous_screen_index < 0) {
        previous_screen_index = screens.length - 1;
    }

    try {
        $(screens)[previous_screen_index].contentWindow.refresh();
    } catch(error) {
        /* nah... nevermind! */
    }

    $(screens).removeClass('active');
    $(screens[previous_screen_index]).addClass('active');
}

function show_screen(index) {
    if(index < 0 || index > screens.length - 1) {
        return false;
    }

    try {
        $(screens)[index].contentWindow.refresh();
    } catch(error) {
        /* nah... nevermind! */
    }

    $(screens).removeClass('active');
    $(screens[index]).addClass('active');

    return index;
}
