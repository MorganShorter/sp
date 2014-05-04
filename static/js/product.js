$(function () {
    /* Product
    * */

    $.ajax({url: '/lookup/size',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.customer_delivery_state').append(new Option(v, k));
            });
        }
    });

    $.ajax({url: '/lookup/states',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.customer_delivery_state').append(new Option(v, k));
            });
        }
    });

    $("#product_content").dialog({
        title: "Products",
        autoOpen: false,
        width: 414
    });
    $("#product_find").dialog({
        title: "Find Product",
        autoOpen: false,
        width: 'auto',
        close: function( event, ui ) {
            $("#product_content").dialog('close');
            $("#product_add").dialog('close');
        }
    });

    $(".button_products_open_dialog").click(function () {
        $("#product_content").dialog("open");
    });
    $(".button_products_find_dialog").click(function(){
        $("#product_find").dialog("open");
    });

    $("#find_product_search").live('click', function(){
        var queryString = $('#frm_find_product').formSerialize();
        $.get(__url_product_list + '?' + queryString);
    });

    // Open product detail
    $('#product_search_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $("#product_content").dialog("open");
        $.get('/product/' + cid + '/');
    });

});