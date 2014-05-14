$(function () {
    /* Product
    * */

    $.ajax({url: '/lookup/size',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.product_size').append(new Option(v, k));
            });
        }
    });

    $.ajax({url: '/lookup/medium',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.product_medium').append(new Option(v, k));
            });
        }
    });

    $.ajax({url: '/lookup/supplier',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.product_supplier').append(new Option(v, k));
            });
        }
    });

    $.ajax({url: '/lookup/royalty_img',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.product_royalty_img').append(new Option(v, k));
            });
        }
    });

    $.ajax({url: '/lookup/price_level_group',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.product_price_level_template').append(new Option(v, k));
            });
        }
    });

    $("#product_content").dialog({
        title: "Edit product",
        autoOpen: false,
        width: 414,
        close: function(event, ui){
            $("#product_pricelevel").dialog("close");
        }
    });
    $("#product_create").dialog({
        title: "Create product",
        autoOpen: false,
        width: 414
    });
    $("#product_find").dialog({
        title: "Find Product",
        autoOpen: false,
        width: 'auto',
        close: function(event, ui) {
            $("#product_content").dialog('close');
            $("#product_add").dialog('close');
            $("#product_pricelevel").dialog("close");
        }
    });
    $("#product_pricelevel").dialog({
        title: "Product level template",
        autoOpen: false,
        width: 274
    });

    $(".button_products_open_dialog").click(function () {
        $("#product_content").dialog("open");
    });
    $(".button_products_add_dialog").click(function () {
        $("#product_create").dialog("open");
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

    $(".product_control_action_cancel", $("#product_content")).click(function() {
        $("#product_content").dialog("close");
    });

    $(".product_control_action_cancel", $("#product_create")).click(function() {
        $("#product_create").dialog("close");
    });
    $("#pricelevel_control_action_cancel").click(function(){
        $("#product_pricelevel").dialog("close");
    });

    // Create/Save/Update Product Details
    $('.product_control_action_save').live('click', function () {
        var c_form = $(this).parents('form').eq(0);
        var obj_id = $.trim($('.product_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;


        var model_fields = c_form.getDataFields();

        if (model_fields['product'].sp_cost && model_fields['product'].sp_cost[0] == "$")
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
                    $("#product_create").dialog("close");
                    $("#product_content").dialog("open");
                    $.get('/product/' + json['obj_id'] + '/');
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

    $(".product_cost_price").spinner({
        min: 0,
        max: 2500,
        step: .25,
        start: 1000,
        numberFormat: "C",
        culture: "en-AU"
    });
    $(".product_current_stock").spinner({
        min: 0,
        max: 250000,
        step: 1,
        start: 1000,
        culture: "en-AU"
    });
    $(".product_minimum_stock").spinner({
        min: 0,
        max: 250000,
        step: 25,
        start: 1000,
        culture: "en-AU"
    });


    // Price Levels
    $('.price_table tbody tr').live("click", function(){
        var price_id = $(this).attr('pr_level_id');
        var prod_id = $('#product_content .product_id').val();
        $("#product_pricelevel").dialog("open");
        $.get('/product/pricelevel/' + prod_id + '/' + price_id + '/');
        return false;
    });
    $('.price_table tbody tr .delete_item').live("click", function(){
        var cid = $(this).parent('tr').attr('pr_level_id');
        alert('delete ' + cid);
        //$("#product_pricelevel").dialog("open");
        //$.get('/customer/note/' + cid + '/' + nid + '/');

        return false;
    });

    // Create/Save/Update price level
    $('#pricelevel_control_action_save').live('click', function () {
        var c_form = $(this).parents('form').eq(0);
        var obj_id = $.trim($('.price_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var product_id = $.trim($('.price_products_id', c_form).val());
        var model_fields = c_form.getDataFields();

        if (!obj_id){
            delete model_fields.pricelevel.id;
        }

        if (!$('.pricelevel_block_only', c_form).prop('checked')){
            model_fields.pricelevel.block_only = 0;
        } else {
            model_fields.pricelevel.block_only = 1;
        }

        if (model_fields.pricelevel.max_amount == ''){
            model_fields.pricelevel.max_amount = NaN;
        }

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.pricelevel',
            'fields': model_fields['pricelevel']
        }];
        $.ajax({
            url: '/product/pricelevel/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                console.log('price save success!');
                console.debug(json);

                if (json['saved']){
                    c_form.resetForm();
                    $("#product_pricelevel").dialog("close");
                    $.get('/product/' + product_id + '/?only_price_levels=1');
                }


                alert(json['msg']);
            },
            error: function (xhr, status) {
                console.log('Error requesting /product/pricelevel/save/! status:');
                console.log(status);
            },
            complete: function (xhr, status) {
                console.log('Complete request for /product/pricelevel/save/');
            }
        });
        return false;
    });

    $('.price_level_add_btn').live('click', function(){
        $("#product_pricelevel").dialog("open");
        $('#frm_add_pricelevel .price_products_id').val($("#frm_product .product_id").val());
    });


    // ?????
    $("#product").mask("99/99/9999", {
        completed: function () {
            alert("You typed the following: " + this.val());
        }
    });

});