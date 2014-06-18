$(function () {
    /* Customer
    * */

    $("#customer_accordion").accordion({
        collapsible: true
    });

    $.ajax({url: '/lookup/states',
        type: 'GET',
        dataType: 'json',
        headers: { 'X_HTTP_REQUESTED_WITH': 'XMLHttpRequest' },
        success: function (json) {
            $.each(json, function (k, v) {
                $('.state_list').append(new Option(v, k));
            });
        }
    });

    $("#customer_content").dialog({
        title: "Customer",
        autoOpen: false,
        width: 'auto',
        height: 'auto',
        close: function( event, ui ) {
            $("#add_contact").dialog('close');
            $("#show_note").dialog('close');
            $('#toggle_customer_main_options_delivery').hide();
            $('#customer_delivery_address_same').prop("checked", 1);
        }
    }).dialogExtend({
        "closable" : true,
        "maximizable" : true,
        "minimizable" : true,
        "collapsable" : true,
        "dblclick" : "collapse",
        "minimizeLocation" : "right"
    });

    $("#customer_find").dialog({
        title: "Find Customers",
        autoOpen: false,
        width: 420,
        open: function(event, ui){
            $('#find_customer_additional_filter').hide();
        },
        close: function(event, ui) {
            $("#customer_content").dialog('close');
            $("#add_contact").dialog('close');
            $("#show_note").dialog('close');
        },
        focus: function(event, ui){
            console.log('open');
            console.log($('#customer_find_filter_field').val())
            if ($('#customer_find_filter_field').val()){
                $('#customer_find_label_display').text($('#customer_find_filter_label').val());
                $('#customer_find_value_display').val($('#customer_find_filter_value').val());
                $('#find_customer_additional_filter').show();
            }
        }
    }).dialogExtend({
        "closable" : true,
        "maximizable" : true,
        "minimizable" : true,
        "collapsable" : true,
        "dblclick" : "collapse",
        "minimizeLocation" : "right"
    });

    $("#add_contact").dialog({
        title: "Add Contact",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {
            $('#frm_add_contact').trigger('reset');
        }
    });

    $("#show_note").dialog({
        title: "Note",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {
            $('#frm_add_note').trigger('reset');
        }
    });

    $(".button_customers_open_dialog").click(function() {
        $("#customer_find").dialog("open");
    });
    $("#customer_control_action_cancel").click(function() {
        $("#customer_content").dialog("close");
    });

    $(".frm_customer .form_label").live('click', function() {
        var label = $(this).text();
        var field = $('*[name="' + $(this).attr('for') + '"]');
        $('#customer_find_filter_field').val(field.attr('data-field'));
        $('#customer_find_filter_value').val(field.val());
        $('#customer_find_filter_label').val(label);
        $("#customer_find").dialog("moveToTop");
        $("#find_customer_search").trigger('click');
    });

    $(".find_customer_close").live('click', function(){
        $('#customer_find_filter_field').val('');
        $('#customer_find_filter_value').val('');
        $('#customer_find_filter_label').val('');
        $('#customer_find_label_display').text('');
        $('#customer_find_value_display').val('');
        $('#find_customer_additional_filter').hide();
    });


    $("#note_control_action_cancel").click(function() {
        $("#show_note").dialog("close");
    });
    $(".button_customers_find_dialog").click(function() {
        $("#customer_find").dialog("open");
    });
    $("#customer_content").on('click', '#customer_control_action_add_contact', function(){
        $("#add_contact").dialog("open");
        $("#contact_customer_id").val($('#customer_id').val());
        $("#contact_customer").val($('#customer_name').val());
        return false;
    });
    $("#contact_control_action_cancel").click(function() {
        $("#add_contact").dialog("close");
    });

    $("#find_customer_search").live('click', function(){
        var queryString = $('#frm_find_customer').formSerialize();
        $.get(__url_customer_list + '?' + queryString);
    });

    // Add customer
    $("#customer_add").dialog({
        title: "Add Customer",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {

        }
    });
    $(".button_customer_add").click(function(){
        $("#customer_add").dialog("open");
    });
    $("#customer_add_control_action_cancel").click(function() {
        $("#customer_add").dialog("close");
    });

    // Save/Update Customer Details
    $('.customer_control_action_save').live('click', function () {
        var c_form = $(this).parents('.frm_customer').eq(0);
        var customer_id = $.trim($('.customer_id', c_form).val());
        if (customer_id == "" || customer_id == undefined || customer_id == null)
            customer_id = null;

        if (!customer_id){
            if ($('#customer_add_delivery_address_same').prop('checked')){
                $('#customer_add_delivery_attn').val($('#customer_add_name').val());
                $('#customer_add_delivery_address1').val($('#customer_add_address1').val());
                $('#customer_add_delivery_address2').val($('#customer_add_address2').val());
                $('#customer_add_delivery_suburb').val($('#customer_add_suburb').val());
                $('#customer_add_delivery_state').val($('#customer_add_state').val());
                $('#customer_add_delivery_postcode').val($('#customer_add_postcode').val());
            }
        }

        var model_fields = c_form.getDataFields();
        var customer_json = [{
            'pk': customer_id,
            'model': 'frontend.customer',
            'fields': model_fields['customer']
        }];
        $.ajax({
            url: '/customer/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(customer_json),
            success: function (json) {
                console.log('/save/customer success!');
                console.debug(json);

                if (!customer_id){
                    c_form.resetForm();
                    $("#customer_add").dialog("close");
                    $("#customer_content").dialog("open");
                    $.get('/customer/' + json['customer_id'] + '/');

                }

                alert(json['msg']);
            },
            error: function (xhr, status) {
                console.log('Error requesting /save/customer! status:');
                console.log(status);
            },
            complete: function (xhr, status) {
                console.log('Complete request for /save/customer');
            }
        });
        return false;
    });

    $('#customer_address_copy').live('click', function(){
        $('#customer_delivery_attn').val($('#customer_name').val());
        $('#customer_delivery_address1').val($('#customer_address1').val());
        $('#customer_delivery_address2').val($('#customer_address2').val());
        $('#customer_delivery_suburb').val($('#customer_suburb').val());
        $('#customer_delivery_state').val($('#customer_state').val());
        $('#customer_delivery_postcode').val($('#customer_postcode').val());
    });

    // Add contact
    $('#contact_control_action_save').live('click', function () {
        var model_fields = $('#frm_add_contact').getDataFields();
        var send_json = [{
            'model': 'frontend.customercontact',
            'fields': model_fields['contact'],
            'pk': null
        }];
        $.ajax({
            url: '/contact/add/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(send_json),
            success: function (json) {
                console.log('/contact/add/ success!');
                console.debug(json);
                $.get('/customer/' + $('#customer_id').val() + '/');
                $("#add_contact").dialog("close");
                $('#frm_add_contact').trigger('reset');
            },
            error: function (xhr, status) {
                console.log('Error requesting /contact/add/! status:');
                console.log(status);
            },
            complete: function (xhr, status) {
                console.log('Complete request for /contact/add/');
            }
        });
    });

    // Delete contact
    $("#customer_content").on('click', '.contact_delete_btn', function(){
        var cnf = confirm('Sure you want to delete this contact?');
        if (cnf == true){
            $.get('/contact/delete/' + $(this).attr('cid'));
            $(this).parents('.form_list_row').remove();
        }

    });

    // Open customer detail
    $('#customer_contact_search tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $("#customer_content").dialog("open");
        $.get('/customer/' + cid + '/');
    });

    $('#customer_delivery_address_same').live("click", function () {
        if ($('#customer_delivery_address_same').prop("checked")) {
            $('#toggle_customer_main_options_delivery').hide('blind');
            $('#customer_address_copy').trigger('click');
        } else {
            $('#toggle_customer_main_options_delivery').show('slide');
        }
    });
    $('#customer_add_delivery_address_same').live("click", function () {
        if ($('#customer_add_delivery_address_same').prop("checked")) {
            $('#toggle_customer_add_main_options_delivery').hide('blind');
            $('#customer_add_address_copy').trigger('click');
        } else {
            $('#toggle_customer_add_main_options_delivery').show('slide');
        }
    });

    /*

    NOTE

     */
    // Open note
    $('#customer_note_items .note_item a').live("click", function(){
        var nid = $(this).attr('note_id');
        var cid = $(this).attr('c_id');
        $("#show_note").dialog("open");
        $.get('/customer/note/' + cid + '/' + nid + '/');
    });

    // Save note
    $('#customer_note_save').live("click", function(){
        var nid = $(this).attr('nid');
        var cid = $(this).attr('cid');
        $.ajax({
            type: "POST",
            url: '/customer/note/' + cid + '/' + nid + '/',
            data: {'text': $("#show_note textarea").val()},
            headers: {'X-CSRFToken': $.cookie('csrftoken')},
            success: function (json) {
                $("#show_note").dialog("close");
                $('#frm_add_note').trigger('reset');
                alert('Note has been saved');
            }
        });
    });

    // New note
    $('#customer_add_note').live("click", function(){
        $("#show_note").dialog("open");
        $('#customer_note_save')
                .attr('cid', $('#customer_id').val())
                .attr('nid', '');
        $("#show_note textarea").val('');
    });

    // Delete customer note
    $("#customer_content").on('click', '.note_delete_btn', function(){
        var nid = $(this).attr('nid');
        var cid = $(this).attr('cid');
        var cnf = confirm('Sure you want to delete this note?');
        if (cnf == true){
            $.get('/customer/note/' + cid + '/' + nid + '/delete/');
            $(this).parents('.form_list_row').remove();
        }
    });

    /*

    ORDER

     */

    $('#customer_order_items tr:gt(0)').live('click', function(){
        var cid = $(this).attr('cid');
        $("#order_content").dialog("open");
        $.get('/order/get/' + cid + '/');
    });

    $('#customer_control_action_add_order').live('click', function(){
        var c_form = $(this).parents('.frm_customer').eq(0);
        var customer_id = $.trim($('.customer_id', c_form).val());
        $("#order_content").dialog("open");
        $.get('/order/create/' + customer_id + '/');
        $.get('/customer/' + customer_id + '/?only_orders=1');

    });


    $(".droppable_customer_type").autocomplete({
        source: ["CAA", "Chiro", "Dental", "Medical", "Optom", "Ortho", "Podiatry", "Vet"]
    });
});
