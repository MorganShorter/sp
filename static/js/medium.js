$(function(){
    $("#medium_list_dialog").dialog({
        title: "Medium list",
        autoOpen: false,
        width: 414,
        buttons: [{
            text: "Create",
            click: function() {

            }
        }, {
            text: "Close",
            click: function() {
                $("#medium_list_dialog").dialog('close');
            }
        }]
    });

    $('.button_products_medium').click(function(){
        $("#medium_list_dialog").dialog('open');
        $.get(__url_medium_list);
    });

    $('#medium_list_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $.get('/medium/open/' + cid + '/');
        $("#medium_item_dialog").dialog("open");
        return false;
    });

    $("#medium_item_dialog").dialog({
        title: "Edit Medium",
        autoOpen: false,
        width: 414,
        buttons: [{
            text: "Save",
            click: function() {
                save_medium()
            }
        }, {
            text: "Delete",
            click: function() {
                var c_form = $('#frm_medium');
                var obj_id = $.trim($('.obj_id', c_form).val());
                if (obj_id == "" || obj_id == undefined || obj_id == null){
                    alert('Error! ID not found');
                    return false;
                }

                var cnf = confirm('Sure you want to delete this medium?');
                if (cnf != true){
                    return false;
                }
                $.get('/medium/delete/' + obj_id + '/', function(data){
                    if (data['status'] == 'error'){
                        alert('Error! ' + data['msg']);
                    } else {
                        alert(data['msg']);
                        c_form.resetForm();
                        $("#medium_item_dialog").dialog('close');
                        $.get(__url_medium_list);
                        $("#medium_list_dialog").dialog('open');
                        refresh_medium();
                    }
                });
                return false;
            }
        }]
    });

    function save_medium() {
        var c_form = $('#frm_medium');
        var obj_id = $.trim($('.obj_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var model_fields = c_form.getDataFields();

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.medium',
            'fields': model_fields['medium']
        }];
        $.ajax({
            url: '/medium/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                if (json['saved']){
                    c_form.resetForm();
                    $("#medium_item_dialog").dialog('close');
                    $.get(__url_medium_list);
                    $("#medium_list_dialog").dialog('open');
                    refresh_medium();
                }
                alert(json['msg']);
            }
        });
        return false;
    }
});

