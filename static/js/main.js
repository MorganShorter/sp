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

    $.ajax({url: '/lookup/states',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('#customer_state').append(new Option(v, k));
                $('#customer_delivery_state').append(new Option(v, k));
            });
        },
        error: function (xhr, status) {
        },
        complete: function (xhr, status) {
        }
    });

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
    $("#product_supplier").autocomplete({
        source: [
            "Australian Institute Optom (AIO)",
            "AIOLT",
            "AMI",
            "BackTalk (BT)",
            "Chiro Assc. Aus (CAA)",
            "Disney (JH)",
            "Koren 1",
            "Koren 2",
            "LT",
            "MedART",
            "SP"
        ]
    });
    $("#order_order_date").datepicker({ dateFormat: 'dd/mm/yy' });
    $("#order_wanted_by").datepicker({ dateFormat: 'dd/mm/yy' });
    $("#product").mask("99/99/9999", {
        completed: function () {
            alert("You typed the following: " + this.val());
        }
    });
    $("#order_shipping_cost").spinner({
        min: 0,
        max: 2500,
        step: .15,
        start: 1000,
        numberFormat: "C",
        culture: "en-AU"
    });
    $("#product_cost_price").spinner({
        min: 0,
        max: 2500,
        step: .25,
        start: 1000,
        numberFormat: "C",
        culture: "en-AU"
    });
    $("#product_current_stock").spinner({
        min: 0,
        max: 250000,
        step: 1,
        start: 1000,
        culture: "en-AU"
    });
    $("#product_minimum_stock").spinner({
        min: 0,
        max: 250000,
        step: 25,
        start: 1000,
        culture: "en-AU"
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