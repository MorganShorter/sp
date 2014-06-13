$(function(){
    var size_item_default_btn = [
        {
            text: "Save",
            click: function() {
                save_size()
            }
        }, {
            text: "Delete",
            click: function() {
                var c_form = $('#frm_size');
                var obj_id = $.trim($('.obj_id', c_form).val());
                if (obj_id == "" || obj_id == undefined || obj_id == null){
                    alert('Error! ID not found');
                    return false;
                }

                var cnf = confirm('Sure you want to delete this size?');
                if (cnf != true){
                    return false;
                }
                $.get('/size/delete/' + obj_id + '/', function(data){
                    if (data['status'] == 'error'){
                        alert('Error! ' + data['msg']);
                    } else {
                        alert(data['msg']);
                        c_form.resetForm();
                        $("#size_item_dialog").dialog('close');
                        $.get(__url_size_list);
                        $("#size_list_dialog").dialog('open');
                        refresh_size();
                    }
                });
                return false;
            }
        }
    ];

    var size_item_create_btn = [
        {
            text: "Create",
            click: function() {
                save_size()
            }
        }
    ];

    $("#size_list_dialog").dialog({
        title: "Size list",
        autoOpen: false,
        resizable: false,
        width: 414,
        buttons: [{
            text: "Create",
            click: function() {
                $("#size_item_dialog")
                    .dialog("close")
                    .dialog("option", "title", "Create Size")
                    .dialog("option", "buttons", size_item_create_btn)
                    .dialog("open");
            }
        }, {
            text: "Close",
            click: function() {
                $("#size_list_dialog").dialog('close');
            }
        }]
    });

    $('.button_products_size').click(function(){
        $("#size_list_dialog").dialog('open');
        $.get(__url_size_list);
    });

    $('#size_list_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $.get('/size/open/' + cid + '/');
        $("#size_item_dialog")
            .dialog("close")
            .dialog("option", "title", "Edit Size")
            .dialog("option", "buttons", size_item_default_btn)
            .dialog("open");
        return false;
    });


    $("#size_item_dialog").dialog({
        title: "Edit Size",
        autoOpen: false,
        resizable: false,
        width: 414,
        close: function(){
            $('form', this).resetForm();
            $('form .obj_id', this).val('');
        },
        buttons: size_item_default_btn
    });

    function save_size() {
        var c_form = $('#frm_size');
        var obj_id = $.trim($('.obj_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var model_fields = c_form.getDataFields();

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.size',
            'fields': model_fields['size']
        }];
        $.ajax({
            url: '/size/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                if (json['saved']){
                    c_form.resetForm();
                    $("#size_item_dialog").dialog('close');
                    $.get(__url_size_list);
                    $("#size_list_dialog").dialog('open');
                    refresh_size();
                }
                alert(json['msg']);
            }
        });
        return false;
    }
});