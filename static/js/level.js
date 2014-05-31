$(function(){
    $("#level_list_dialog").dialog({
        title: "Price Level Groups",
        autoOpen: false,
        width: 414,
        buttons: [{
            text: "Create",
            click: function() {

            }
        }, {
            text: "Close",
            click: function() {
                $("#level_list_dialog").dialog('close');
            }
        }]
    });

    $('.button_products_level').click(function(){
        $("#level_list_dialog").dialog('open');
        $.get(__url_level_list);
    });

    $('#level_list_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $.get('/price_level/open/' + cid + '/');
        $("#level_item_dialog").dialog("open");
        return false;
    });

    $("#level_item_dialog").dialog({
        title: "Edit Price Level Group",
        autoOpen: false,
        width: 414,
        buttons: [{
            text: "Save",
            click: function() {
                save_level()
            }
        }, {
            text: "Delete",
            click: function() {
                var c_form = $('#frm_level');
                var obj_id = $.trim($('.obj_id', c_form).val());
                if (obj_id == "" || obj_id == undefined || obj_id == null){
                    alert('Error! ID not found');
                    return false;
                }

                var cnf = confirm('Sure you want to delete this Price Level Group?');
                if (cnf != true){
                    return false;
                }
                $.get('/price_level/delete/' + obj_id + '/', function(data){
                    if (data['status'] == 'error'){
                        alert('Error! ' + data['msg']);
                    } else {
                        alert(data['msg']);
                        c_form.resetForm();
                        $("#level_item_dialog").dialog('close');
                        $.get(__url_level_list);
                        $("#level_list_dialog").dialog('open');
                        refresh_level();
                    }
                });
                return false;
            }
        }]
    });

    function save_level() {
        var c_form = $('#frm_level');
        var obj_id = $.trim($('.obj_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var model_fields = c_form.getDataFields();

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.pricelevelgroup',
            'fields': model_fields['level']
        }];
        $.ajax({
            url: '/price_level/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                if (json['saved']){
                    c_form.resetForm();
                    $("#level_item_dialog").dialog('close');
                    $.get(__url_level_list);
                    $("#level_list_dialog").dialog('open');
                    refresh_level();
                }
                alert(json['msg']);
            }
        });
        return false;
    }
});