$(function () {
    /* Product
    * */

    $.ajax({url: '/lookup/size',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('#product_size').append(new Option(v, k));
            });
        }
    });

    $.ajax({url: '/lookup/medium',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('#product_medium').append(new Option(v, k));
            });
        }
    });

    $.ajax({url: '/lookup/supplier',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('#product_supplier').append(new Option(v, k));
            });
        }
    });

    $.ajax({url: '/lookup/royalty_img',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('#product_royalty_img').append(new Option(v, k));
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

    $(".product_control_action_cancel").click(function() {
        $("#product_content").dialog("close");
    });


    // Save/Update Customer Details
    $('.product_control_action_save').live('click', function () {
        var c_form = $(this).parents('#frm_product').eq(0);
        var obj_id = $.trim($('.product_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;


        var model_fields = c_form.getDataFields();

        if (model_fields['product'].sp_cost[0] == "$")
            model_fields['product'].sp_cost = model_fields['product'].sp_cost.slice(1);

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.product',
            'fields': model_fields['product']
        }];
        $.ajax({
            url: '/product/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                console.log('prod save success!');
                console.debug(json);

                if (!obj_id){
                    c_form.resetForm();
                    $("#product_add").dialog("close");
                    $("#product_content").dialog("open");
                    $.get('/product/' + json['product_id'] + '/');

                }

                alert(json['msg']);
            },
            error: function (xhr, status) {
                console.log('Error requesting /save/product! status:');
                console.log(status);
            },
            complete: function (xhr, status) {
                console.log('Complete request for /save/product');
            }
        });
        return false;
    });


});