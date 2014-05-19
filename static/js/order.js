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
        var cid = $(this).parents('tr').attr('cid');
        $("#product_content").dialog("open");
        $.get('/product/' + cid + '/');
    });

    // Search/Find Order
    $("#find_order_search").live('click', function(){
        var queryString = $('#frm_find_order').formSerialize();
        $.get(__url_order_list + '?' + queryString);
    });

    // Open order detail
    $('#order_search_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $("#order_content").dialog("open");
        $.get('/order/get/' + cid + '/');
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
    $(".order_shipping_cost").spinner({
        min: 0,
        max: 2500,
        step: .15,
        start: 1000,
        numberFormat: "C",
        culture: "en-AU"
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


    // Create/Save/Update Order
    $('.save_order').live('click', function () {
        var c_form = $(this).parents('form').eq(0);
        var obj_id = $.trim($('.order_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;


        var model_fields = c_form.getDataFields();

        if (model_fields['order'].shipping_cost && model_fields['order'].shipping_cost[0] == "$")
            model_fields['order'].shipping_cost = model_fields['order'].shipping_cost.slice(1);

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.order',
            'fields': model_fields['order'],
            'invoice': model_fields['invoice']
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
                        $.get('/order/get/' + json['obj_id'] + '/');
                    } else { // Updated
                        $("#order_content").dialog("close");
                    }
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
});