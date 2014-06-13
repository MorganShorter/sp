$(function(){
    var royalty_item_default_btn = [{
            text: "Save",
            click: function() {
                save_royalty()
            }
        }, {
            text: "Delete",
            click: function() {
                var c_form = $('#frm_royalty');
                var obj_id = $.trim($('.obj_id', c_form).val());
                if (obj_id == "" || obj_id == undefined || obj_id == null){
                    alert('Error! ID not found');
                    return false;
                }

                var cnf = confirm('Sure you want to delete this Royalty Group?');
                if (cnf != true){
                    return false;
                }
                $.get('/royalty/delete/' + obj_id + '/', function(data){
                    if (data['status'] == 'error'){
                        alert('Error! ' + data['msg']);
                    } else {
                        alert(data['msg']);
                        c_form.resetForm();
                        $("#royalty_item_dialog").dialog('close');
                        $.get(__url_royalty_list);
                        $("#royalty_list_dialog").dialog('open');
                        refresh_royalty();
                    }
                });
                return false;
            }
        }
    ];

    var royalty_item_create_btn = [
        {
            text: "Create",
            click: function() {
                save_royalty()
            }
        }
    ];


    $("#royalty_list_dialog").dialog({
        title: "Royalty Groups",
        autoOpen: false,
        resizable: false,
        width: 414,
        buttons: [{
            text: "Create",
            click: function() {
                $("#royalty_item_dialog")
                    .dialog("close")
                    .dialog("option", "title", "Create Royalty Group")
                    .dialog("option", "buttons", royalty_item_create_btn)
                    .dialog("open");
            }
        }, {
            text: "Close",
            click: function() {
                $("#royalty_list_dialog").dialog('close');
            }
        }]
    });

    $('.button_products_royalty').click(function(){
        $("#royalty_list_dialog").dialog('open');
        $.get(__url_royalty_list);
    });

    $('#royalty_list_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $.get('/royalty/open/' + cid + '/');
        $("#royalty_item_dialog")
            .dialog("close")
            .dialog("option", "title", "Edit Royalty Group")
            .dialog("option", "buttons", royalty_item_default_btn)
            .dialog("open");
        return false;
    });

    $("#royalty_item_dialog").dialog({
        title: "Edit Royalty Group",
        autoOpen: false,
        resizable: false,
        width: 414,
        buttons: royalty_item_default_btn
    });

    function save_royalty() {
        var c_form = $('#frm_royalty');
        var obj_id = $.trim($('.obj_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var model_fields = c_form.getDataFields();

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.royaltygroup',
            'fields': model_fields['royalty']
        }];
        $.ajax({
            url: '/royalty/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                if (json['saved']){
                    c_form.resetForm();
                    $("#royalty_item_dialog").dialog('close');
                    $.get(__url_royalty_list);
                    $("#royalty_list_dialog").dialog('open');
                    refresh_royalty();
                }
                alert(json['msg']);
            }
        });
        return false;
    }
});