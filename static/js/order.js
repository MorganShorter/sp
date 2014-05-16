$(function () {
    /* Order
    * */
    $("#order_content").dialog({
        title: "Show order",
        autoOpen: false,
        width: 800
    });
    $("#order_find").dialog({
        title: "Find order",
        autoOpen: false,
        width: 'auto'
    });

    $(".button_order_show_dialog").click(function () {
        $("#order_content").dialog("open");
    });
    $(".button_order_find_dialog").click(function () {
        $("#order_find").dialog("open");
    });
    $(".order_customer_id_search").click(function(){
        var cid = $("#frm_order .customer_id").val();
        $("#customer_content").dialog("open");
        $.get('/customer/' + cid + '/');
    });
    $(".order_product_item_show").live('click', function(){
        var cid = $(this).parents('tr').attr('cid');
        $("#product_content").dialog("open");
        $.get('/product/' + cid + '/');
    });

    // Search/Find Order
    $("#find_order_search").live('click', function(){
        var queryString = $('#frm_find_order').formSerialize();
        $.get(__url_order_list + '?' + queryString);
    });

    // Open product detail
    $('#order_search_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $("#order_content").dialog("open");
        $.get('/order/get/' + cid + '/');
    });


    $("#order_order_date").datepicker({ dateFormat: 'dd/mm/yy' });
    $("#order_wanted_by").datepicker({ dateFormat: 'dd/mm/yy' });

    $('#frm_find_order .form_input').on('input', function(){
        $('#frm_find_order .form_input').not(this).val('');
    });

    $.ajax({url: '/lookup/company',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.invoice_company').append(new Option(v, k));
            });
        }
    });
});