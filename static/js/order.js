$(function () {
    /* Order
    * */

    $("#order_accordion").accordion({
        collapsible: true
    });

    $("#order_content").dialog({
        title: "Show order",
        autoOpen: false,
        width: 800,
        close: function(){
            $('.add_product_to_order').css('display', 'none');
        },
        open: function(){
            $('.add_product_to_order').css('display', 'block');
        }
    }).dialogExtend({
        "closable" : true,
        "maximizable" : true,
        "minimizable" : true,
        "collapsable" : true,
        "dblclick" : "collapse",
        "minimizeLocation" : "right"
    });

    $("#order_find").dialog({
        title: "Find order",
        autoOpen: false,
        width: 420,
        create: function (event, ui) {
            $.get(__url_order_list + '?last=1');
        }
    }).dialogExtend({
        "closable" : true,
        "maximizable" : true,
        "minimizable" : true,
        "collapsable" : true,
        "dblclick" : "collapse",
        "minimizeLocation" : "right"
    });

    $(".button_order_show_dialog").click(function () {
        $("#order_content").dialog("open");
    });
    $(".dialog_close_order").click(function(){
        $("#order_content").dialog("close");
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
        var cid = $(this).attr('cid');
        $("#product_content").dialog("open");
        $.get('/product/' + cid + '/');
    });
    $(".dialog_refresh_order").live('click', function(){
        var c_form = $(this).parents('form').eq(0);
        var cid = $.trim($('.order_id', c_form).val());
        $.get('/order/get/' + cid + '/');
    });
    $(".button_order_create_dialog").live('click', function(){
        alert("You can add the order via the customer dialog.");
        return false;
    });

    // Search/Find Order
    $("#find_order_search").live('click', function(){
        var queryString = $('#frm_find_order').formSerialize();
        $.get(__url_order_list + '?' + queryString);
    });

    // Open order detail
    $('.open_order_detail').live('click', function(){
        var cid = $(this).attr('cid');
        $("#order_content").dialog("open");
        $.get('/order/get/' + cid + '/');
        order_init();
    });

    // Delete order
    $('#order_control_action_delete').live('click', function(){
        var c_form = $(this).parents('form').eq(0);
        var cid = $.trim($('.order_id', c_form).val());

        var cnf = confirm('Sure you want to delete this order?');
        if (cnf != true){
            return false;
        }

        $.get('/order/delete/' + cid + '/', function(data){
            if (data['status'] == 'error'){
                alert('Error! ' + data['msg']);
            } else {
                $("#order_content").dialog("close");
                $("#order_search_result tr[cid=" + cid + "]").remove();
                $("#customer_order_items tr[cid=" + cid + "]").remove();
                alert(data['msg']);
            }
        });
        return false;
    });

    $(".order_order_date").datepicker({
        dateFormat: 'dd/mm/yy',
        altField: ".hidden_order_date",
        altFormat: "yy-mm-dd"
    });
    $(".order_wanted_by").datepicker({
        dateFormat: 'dd/mm/yy',
        altField: ".hidden_wanted_by",
        altFormat: "yy-mm-dd"
    });

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

    $.ajax({url: '/lookup/order/status/',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.order_status').append(new Option(v, k));
            });
        }
    });


    // Create/Save/Update Order
    $('.save_order').live('click', function () {
        var c_form = $(this).parents('form').eq(0);
        var obj_id = $.trim($('.order_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;


        var model_fields = c_form.getDataFields();

        if (model_fields['order'].shipping_cost && model_fields['order'].shipping_cost[0] == "$")
            model_fields['order'].shipping_cost = model_fields['order'].shipping_cost.slice(1);

        // products
        var products = {};
        $("#order_product_items tr:gt(0):not(:last)").each(function(){
            products[$(this).attr('cid')] = {
                quantity: $('.order_product_quantity', $(this)).val(),
                cost: $('.order_product_cost', $(this)).spinner('value'),
                discount: $('.order_product_percentage', $(this)).val(),
                tax: $('.order_product_tax', $(this)).prop('checked')
            }
        });

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.order',
            'fields': model_fields['order'],
            'invoice': model_fields['invoice'],
            'status': $(".order_status", c_form).val(),
            'products': products
        }];

        $.ajax({
            url: '/order/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                console.log('order save success!');
                console.debug(json);
                if (json['saved']){
                    if (!obj_id){ // Created
                        c_form.resetForm();
                        $("#order_create").dialog("close");
                        $("#order_content").dialog("open");
                    }
                    $.get('/order/get/' + json['obj_id'] + '/');
                    $.get('/customer/' + model_fields['order'].customer + '/?only_orders=1');
                }

                alert(json['msg']);
            },
            error: function (xhr, status) {
                console.log('Error requesting /save/order! status:');
                console.log(status);
            },
            complete: function (xhr, status) {
                console.log('Complete request for /save/order');
            }
        });
        return false;
    });

    // Add product to current order
    $('#order_control_action_add').live('click', function(){
        $("#product_find").dialog("open");
    });
    $('.add_product_to_order').live('click', function(){
        var prod_id = parseInt($(this).parents('tr').eq(0).attr('cid'));
        var order_id = $('#frm_order .order_id').val();
        console.log('Add product #' + prod_id + ' to order #' + order_id);

        $.get('/order/add_product/' + order_id + '/' + prod_id + '/', function(data){
            if (data['status'] == 'ok') {
                $.get('/order/get/' + order_id + '/?only_products=1');
                alert('Product has added to the order');
            } else {
                alert('Error! Product not added');
            }
        });

        return false;
    });

    // Product price level
    $('.order_product_pl').live('change', function(){
        var val = $(this).val();
        if (val){
            $('.order_product_cost', $(this).parents('tr')).spinner('value', val);
            call_product_recount($(this).parents('tr'));
        }
    });
    $('.order_product_tax').live('change', function(){
        call_product_recount($(this).parents('tr'));
    });

    // Delete product
    $('.order_product_item_delete').live('click', function(){
        var order_prod_id = parseInt($(this).parents('tr').eq(0).attr('cid'));
        var order_id = $('#frm_order .order_id').val();

        var cnf = confirm('Sure you want to delete this product?');
        if (cnf != true){
            return false;
        }

        $.get('/order/delete_product/' + order_prod_id + '/', function(data){
            if (data['status'] == 'ok') {
                $.get('/order/get/' + order_id + '/?only_products=1');
                alert('Product has removed from the order');
            } else {
                alert('Error! Product not removed');
            }
        });
    });


    $('.print_invoice').live('click', function(){
        var order_id = $('#frm_order .order_id').val();
        document.location = '/order/get_pdf/' + order_id + '/';
        return false;
    });

    $('.send_invoice').live('click', function(){
        var order_id = $('#frm_order .order_id').val();
        $.get('/order/send_pdf/' + order_id + '/', function(data){
            if (data['status'] == 'error'){
                alert(data['msg']);
            } else {
                alert('An invoice sent')
            }
        });
        return false;
    });

});


function order_init(){
    $(".order_shipping_cost").spinner({
        min: 0,
        step: 0.01,
        start: 0,
        numberFormat: "C",
        culture: "en-AU"
    });
    $(".order_product_cost").spinner({
        min: 0,
        step: 0.01,
        start: 0,
        numberFormat: "C",
        culture: "en-AU",
        spin: product_recount,
        stop: product_recount,
        create: product_recount
    });

    $(".order_product_quantity").spinner({
        min: 1,
        step: 1,
        start: 1,
        culture: "en-AU",
        create: product_recount
    });

    $(".order_product_percentage").spinner({
        min: 0,
        max: 100,
        step: 1,
        start: 0,
        culture: "en-AU",
        create: product_recount
    });

    $(".order_product_spinner").spinner({
        spin: product_recount,
        stop: product_recount
    });
}

function product_recount(){
    var parent = $(this).parents('tr');
    call_product_recount(parent);
}

function call_product_recount(parent){
    var count = parseInt($('.order_product_quantity', parent).val());
    var cost = parseFloat($('.order_product_cost', parent).spinner('value'));
    var discount = parseFloat($('.order_product_percentage', parent).val());
    var stock = parseInt($('.order_product_stock', parent).text());
    var tax = $('.order_product_tax', parent).prop('checked');
    var royalty = parseFloat($('.order_product_royalty', parent).text());

    $('.back_order_icon', parent).removeClass('back_order_yes').removeClass('back_order_no');
    if (count > stock){
        $('.back_order_icon', parent).addClass('back_order_yes');
    } else {
        $('.back_order_icon', parent).addClass('back_order_no');
    }

    cost *= count;
    var result = cost;
    var royalty_total = 0;
    if (royalty){
        royalty_total = cost * (royalty/100)
        result += royalty_total;
    }

    if (discount > 0){
        result -= cost * (discount/100);
    }

    if (tax){
        result += (cost + royalty_total)  * __tax_percent / 100;
    }

    $('.order_product_total', parent).text(result.toFixed(2));
}