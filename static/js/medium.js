$(function(){
    $("#medium_list_dialog").dialog({
        title: "Medium list",
        autoOpen: false,
        width: 414
    });

    $('.button_products_medium').click(function(){
        $("#medium_list_dialog").dialog('open');
        $.get(__url_medium_list);
    });
});