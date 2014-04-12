$(function () {
    /* Order
    * */
    $("#order_content").dialog({
        title: "Orders",
        autoOpen: false,
        width: 800
    });
    $("#button_orders_open_dialog").click(function () {
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
});