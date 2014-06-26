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


});