$(function () {
    $.ajaxSetup({
        cache: false
    });

    // console fix
    if (typeof console == undefined) {
        window.console = {
            log: function (s) {
                return false;
            }
        };
        console.warn = console.debug = console.log;
    }

    $.taconite.debug = true;

    $("#window").draggable({
        revert: "invalid"
    });
    $("#order_window").draggable({
        revert: "invalid"
    });

    $("#container").droppable({
        drop: function (event, ui) {
            $(this)
                    .find("#debug_msg")
                    .html("window in position");
        }
    });

    $(document).tooltip({
        position: {
            my: "right bottom+6",
            at: "center bottom",
            of: "#avator",
            using: function (position, feedback) {
                $(this).css(position);
                $("<div>")
                        .addClass("arrow")
                        .addClass(feedback.vertical)
                        .addClass(feedback.horizontal)
                        .appendTo(this);
            }
        }
    });

    refresh_size();
    refresh_medium();
    refresh_supplier();
    refresh_royalty_img();
    refresh_level();

});