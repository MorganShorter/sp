$(function(){
    $("#bo_list_dialog").dialog({
        title: "Back orders",
        autoOpen: false,
        resizable: false,
        width: 414
    });

    $('.button_bo_find_dialog').click(function(){
        $("#bo_list_dialog").dialog('open');
        $.get(__url_bo_list);
    });

    // Search/Find Order
    $("#frm_find_bo_btn").live('click', function(){
        var queryString = $('#frm_find_bo').formSerialize();
        $.get(__url_bo_list + '?' + queryString);
    });

    $('.change_bo_status').live('click', function(){
        var cid = $(this).attr('cid');

        var cnf = confirm('Sure you want to change BO status?');
        if (cnf == true){
            $(this).parents('tr').remove();
            $.get('/bo/update/?bo_id=' + cid, function(data){
                if (data['updated'] == true){
                    alert('BO status has been changed');
                }
            });

        }
        return false;
    });


});