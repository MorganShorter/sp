$(function(){
    $("#size_list_dialog").dialog({
        title: "Size list",
        autoOpen: false,
        width: 414
    });

    $('.button_products_size').click(function(){
        $("#size_list_dialog").dialog('open');
        $.get(__url_size_list);
    });
});