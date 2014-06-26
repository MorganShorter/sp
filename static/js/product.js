$(function () {
    /* Product
    * */

    $("#product_content").dialog({
        title: "Edit product",
        autoOpen: false,
        width: 414,
        close: function(event, ui){
            $('#frm_product').resetForm();
            $("#product_pricelevel").dialog("close");
            $("#product_catalog_issue").dialog("close");
        }
    }).dialogExtend({
        "closable" : true,
        "maximizable" : true,
        "minimizable" : true,
        "collapsable" : true,
        "dblclick" : "collapse",
        "minimizeLocation" : "right"
    });
    $("#product_create").dialog({
        title: "Create product",
        autoOpen: false,
        resizable: false,
        width: 414
    });
    $("#product_find").dialog({
        title: "Find Product",
        autoOpen: false,
        width: 420,
        close: function(event, ui) {
            $("#product_content").dialog('close');
            $("#product_add").dialog('close');
            $("#product_pricelevel").dialog("close");
        },
        create: function(event, ui) {
            $.get(__url_product_list + '?last=1');
        }
    }).dialogExtend({
        "closable" : true,
        "maximizable" : true,
        "minimizable" : true,
        "collapsable" : true,
        "dblclick" : "collapse",
        "minimizeLocation" : "right"
    });
    $("#product_pricelevel").dialog({
        title: "Product level template",
        autoOpen: false,
        resizable: false,
        width: 274,
        close: function(event, ui) {
            var f = $('#frm_add_pricelevel');
            f.resetForm();
            $('.price_product_id', f).val('');
            $('.price_id', f).val('');
        }
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
        $.get(__url_product_list + '?' + queryString, function(data){
            if ($("#order_content").dialog('isOpen')){
                $('.add_product_to_order').css('display', 'block');
            }
        });
    });

    // Open product detail
    $('.open_product_detail').live('click', function(){
        var cid = $(this).attr('cid');
        if (cid == undefined)
            return false;

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

        if (model_fields['product'].royalty_group == ''){
            model_fields['product'].royalty_group = NaN;
        }

        if (model_fields['product'].manual_royalty == ''){
            model_fields['product'].manual_royalty = NaN;
        }

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.product',
            'fields': model_fields['product'],
            'price_template': $('.product_price_level_template', c_form).val()
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
                if (json['saved']){
                    if (!obj_id){ // Created
                        c_form.resetForm();
                        $("#product_create").dialog("close");
                        $("#product_content").dialog("open");
                        $.get('/product/' + json['obj_id'] + '/');
                    } else { // Updated
                        $("#product_content").dialog("close");
                    }
                }

                alert(json['msg']);
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
    $(".product_royalty").spinner({
        min: 0,
        max: 100,
        step: 5,
        start: 0,
        culture: "en-AU"
    });

    //
    // Price Levels
    $('.price_table tbody tr').live("click", function(){
        var price_id = $(this).attr('pr_level_id');
        var prod_id = $('#product_content .product_id').val();
        $("#product_pricelevel")
            .dialog("close")
            .dialog("open");
        $.get('/product/pricelevel/' + prod_id + '/' + price_id + '/');
        return false;
    });
    $('.price_table tbody tr .delete_item').live("click", function(){
        var price_id = $(this).parent('tr').attr('pr_level_id');
        var prod_id = $('#product_content .product_id').val();

        var cnf = confirm('Sure you want to delete this price level?');
        if (cnf != true){
            return false;
        }
        $.get('/product/pricelevel/' + prod_id + '/' + price_id + '/delete/', function(data){
            if (data['status'] == 'error'){
                alert('Error! ' + data['msg']);
            } else {
                $.get('/product/' + prod_id + '/?only_lisr=1');
                alert(data['msg']);
            }
        });
        return false;
    });

    // Create/Save/Update price level
    $('#pricelevel_control_action_save').live('click', function () {
        var c_form = $(this).parents('form').eq(0);
        var obj_id = $.trim($('.price_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var product_id = $.trim($('.price_product_id', c_form).val());
        var model_fields = c_form.getDataFields();

        if (!obj_id){
            delete model_fields.pricelevel.id;
        }

        /*
        if (!$('.pricelevel_block_only', c_form).prop('checked')){
            model_fields.pricelevel.block_only = 0;
        } else {
            model_fields.pricelevel.block_only = 1;
        }
        */

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
                    $.get('/product/' + product_id + '/?only_lisr=1');
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
        $("#product_pricelevel").dialog("close").dialog("open");
        $('#frm_add_pricelevel .price_product_id').val($("#frm_product .product_id").val());
    });


    //
    // Product - catalog links
    var issue_link_default_btn = [
        {
            text: "Save",
            click: function() {
                save_issue_link();
            }
        }, {
            text: "Delete",
            click: function() {
                var c_form = $('#frm_product_catalog_issue');
                var obj_id = $.trim($('.obj_id', c_form).val());
                var product_id = $.trim($('.product_id', c_form).val());
                if (obj_id == "" || obj_id == undefined || obj_id == null){
                    alert('Error! ID not found');
                    return false;
                }

                var cnf = confirm('Sure you want to delete this Link?');
                if (cnf != true){
                    return false;
                }
                $.get('/product/issue/' + product_id + '/' + obj_id + '/delete/', function(data){
                    if (data['status'] == 'error'){
                        alert('Error! ' + data['msg']);
                    } else {
                        alert(data['msg']);
                        c_form.resetForm();
                        $("#product_catalog_issue").dialog('close');
                        $.get('/product/' + product_id + '/?only_list=1');
                    }
                });
                return false;
            }
        }
    ];

    var issue_link_create_btn = [
        {
            text: "Create",
            click: function() {
                save_issue_link()
            }
        }
    ];

    $("#product_catalog_issue").dialog({
        title: "Edit Catalog link",
        autoOpen: false,
        resizable: false,
        width: 414,
        buttons: issue_link_default_btn,
        close: function(event, ui){
            $("#product_catalog_issue")
                .dialog("option", "title", "Edit Catalog link")
                .dialog("option", "buttons", issue_link_default_btn);
        }
    });

    $('.catalog_list_table tbody tr').live("click", function(){
        var issue_id = $(this).attr('cid');
        var prod_id = $('#product_content .product_id').val();
        $("#product_catalog_issue")
            .dialog("close")
            .dialog("open");

        $.get('/product/issue/' + prod_id + '/' + issue_id + '/');
        return false;
    });

    $('.product_catalog_add_btn').live('click', function(){
       $("#product_catalog_issue")
               .dialog("close")
               .dialog("option", "title", "Create Catalog link")
               .dialog("option", "buttons", issue_link_create_btn)
               .dialog("open");

        var f = $('#frm_product_catalog_issue');

        $('.product_id', f).val($('#product_content .product_id').val());
        $('.obj_id', f).val('');
        $('.product_name', f).val($('#product_content .product_name').val());
    });

    function save_issue_link(){
        var c_form = $('#frm_product_catalog_issue');
        var obj_id = $.trim($('.obj_id', c_form).val());
        var product_id = $.trim($('.product_id', c_form).val());

        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var model_fields = c_form.getDataFields();

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.catalogissueproduct',
            'fields': model_fields['catalogissueproduct']
        }];
        $.ajax({
            url: '/product/issue/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                if (json['saved']){
                    c_form.resetForm();
                    $.get('/product/' + product_id + '/?only_list=1');
                    $("#product_catalog_issue").dialog("close");
                }
                alert(json['msg']);
            }
        });
        return false;
    }

});