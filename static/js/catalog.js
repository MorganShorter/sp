$(function(){
    var catalog_item_default_btn = [{
            text: "Save",
            click: function() {
                save_catalog()
            }
        }, {
            text: "Delete",
            click: function() {
                var c_form = $('#frm_catalog');
                var obj_id = $.trim($('.obj_id', c_form).val());
                if (obj_id == "" || obj_id == undefined || obj_id == null){
                    alert('Error! ID not found');
                    return false;
                }

                var cnf = confirm('Sure you want to delete this Catalog?');
                if (cnf != true){
                    return false;
                }
                $.get('/catalog/delete/' + obj_id + '/', function(data){
                    if (data['status'] == 'error'){
                        alert('Error! ' + data['msg']);
                    } else {
                        alert(data['msg']);
                        c_form.resetForm();
                        $("#catalog_item_dialog").dialog('close');
                        $.get(__url_catalog_list);
                        $("#catalog_list_dialog").dialog('open');
                        refresh_catalog();
                    }
                });
                return false;
            }
        }
    ];

    var catalog_item_create_btn = [
        {
            text: "Create",
            click: function() {
                save_catalog()
            }
        }
    ]


    $("#catalog_list_dialog").dialog({
        title: "catalog list",
        autoOpen: false,
        width: 414,
        buttons: [{
            text: "Create",
            click: function() {
                $("#catalog_item_dialog")
                    .dialog("close")
                    .dialog("option", "title", "Create catalog")
                    .dialog("option", "buttons", catalog_item_create_btn)
                    .dialog("open");
            }
        }, {
            text: "Close",
            click: function() {
                $("#catalog_list_dialog").dialog('close');
            }
        }]
    });

    $('.button_catalog_dialog').click(function(){
        $("#catalog_list_dialog").dialog('open');
        $.get(__url_catalog_list);
    });

    $('#catalog_list_result tbody tr').live('click', function(){
        var cid = $(this).attr('cid');
        $.get('/catalog/open/' + cid + '/');
        $("#catalog_item_dialog")
            .dialog("close")
            .dialog("option", "title", "Edit Catalog")
            .dialog("option", "buttons", catalog_item_default_btn)
            .dialog("open");
        return false;
    });

    $("#catalog_item_dialog").dialog({
        title: "Edit catalog",
        autoOpen: false,
        width: 414,
        buttons: catalog_item_default_btn
    });

    function save_catalog() {
        var c_form = $('#frm_catalog');
        var obj_id = $.trim($('.obj_id', c_form).val());
        if (obj_id == "" || obj_id == undefined || obj_id == null)
            obj_id = null;

        var model_fields = c_form.getDataFields();

        var obj_json = [{
            'pk': obj_id,
            'model': 'frontend.catalog',
            'fields': model_fields['catalog']
        }];
        $.ajax({
            url: '/catalog/save/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            contentType: 'application/json; charset=UTF-8',
            headers: { 'X-CSRFToken': $.cookie('csrftoken') },
            data: JSON.stringify(obj_json),
            success: function (json) {
                if (json['saved']){
                    c_form.resetForm();
                    $("#catalog_item_dialog").dialog('close');
                    $.get(__url_catalog_list);
                    $("#catalog_list_dialog").dialog('open');
                }
                alert(json['msg']);
            }
        });
        return false;
    }
});

