$(function () {
    /* Order
    * */
    $("#order_content").dialog({
        title: "Orders",
        autoOpen: false,
        width: 800
    });
    $(".button_order_add_dialog").click(function () {
        $("#order_content").dialog("open");
    });

    // Search/Find Order by ID
    $('#order_order_id_search').live('click', function () {
        var order_id = $.trim($('#order_order_id').val());
        if (!order_id) {
            alert('You must enter a Order ID!');
        } else {
            $.get('/order/' + order_id);
        }

    });

    $("#order_order_date").datepicker({ dateFormat: 'dd/mm/yy' });
    $("#order_wanted_by").datepicker({ dateFormat: 'dd/mm/yy' });
});