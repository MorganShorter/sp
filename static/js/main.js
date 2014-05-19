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

    $("#order_order_company22").autocomplete({
        source: [
            "ActionScript",
            "AppleScript",
            "Asp",
            "BASIC",
            "C",
            "C++",
            "Clojure",
            "COBOL",
            "ColdFusion",
            "Erlang",
            "Fortran",
            "Groovy",
            "Haskell",
            "Java",
            "JavaScript",
            "Lisp",
            "Perl",
            "PHP",
            "Python",
            "Ruby",
            "Scala",
            "Scheme"
        ]
    });




    $("#order_product_item_percentage_ID").pcntspinner({
        min: 0,
        max: 100,
        step: 5,
        start: 0,
        culture: "en-AU"
    });
    $("#order_product_item_percentage_ID2").pcntspinner({
        min: 0,
        max: 100,
        step: 5,
        start: 0,
        culture: "en-AU"
    });
    $("#order_order_company").combobox();
    $("#order_accordion").accordion({
        collapsible: true
    });
    $("#customer_accordion").accordion({
        collapsible: true
    });
});