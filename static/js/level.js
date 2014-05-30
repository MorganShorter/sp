$(function(){
    $("#level_list_dialog").dialog({
        title: "Price Level Groups",
        autoOpen: false,
        width: 414
    });

    $('.button_products_level').click(function(){
        $("#level_list_dialog").dialog('open');
        $.get(__url_level_list);
    });
});