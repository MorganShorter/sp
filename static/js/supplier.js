$(function(){
    $("#supplier_list_dialog").dialog({
        title: "Suppliers list",
        autoOpen: false,
        width: 414,
        buttons: [{
            text: "Create",
            click: function() {

            }
        }, {
            text: "Close",
            click: function() {
                $("#supplier_list_dialog").dialog('close');
            }
        }]
    });

    $('.button_products_supplier').click(function(){
        $("#supplier_list_dialog").dialog('open');
        $.get(__url_supplier_list);
    });

    $('#supplier_list_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $.get('/supplier/open/' + cid + '/');
        $("#supplier_item_dialog").dialog("open");
        return false;
    });

    $("#supplier_item_dialog").dialog({
        title: "Edit Supplier",
        autoOpen: false,
        width: 414,
        buttons: [{
            text: "Save",
            click: function() {
                save_supplier()
            }
        }, {
            text: "Delete",
            click: function() {
                var c_form = $('#frm_supplier');
                var obj_id = $.trim($('.obj_id', c_form).val());
                if (obj_id == "" || obj_id == undefined || obj_id == null){
                    alert('Error! ID not found');
                    return false;
                }

                var cnf = confirm('Sure you want to delete this Supplier?');
                if (cnf != true){
                    return false;
                }
                $.get('/supplier/delete/' + obj_id + '/', function(data){
                    if (data['status'] == 'error'){
                        alert('Error! ' + data['msg']);
                    } else {
                        alert(data['msg']);
                        c_form.resetForm();
                        $("#supplier_item_dialog").dialog('close');
                        $.get(__url_supplier_list);
                        $("#supplier_list_dialog").dialog('open');
                        refresh_supplier();
                    }
                });
                return false;
            }
        }]
    });

    function save_supplier() {
        var c_form = $('#frm_supplier');
        var obj_id = $.trim($('.obj_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var model_fields = c_form.getDataFields();

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.supplier',
            'fields': model_fields['supplier']
        }];
        $.ajax({
            url: '/supplier/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                if (json['saved']){
                    c_form.resetForm();
                    $("#supplier_item_dialog").dialog('close');
                    $.get(__url_supplier_list);
                    $("#supplier_list_dialog").dialog('open');
                    refresh_supplier();
                }
                alert(json['msg']);
            }
        });
        return false;
    }
});