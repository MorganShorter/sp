$(function(){
    $("#supplier_list_dialog").dialog({
        title: "Suppliers list",
        autoOpen: false,
        width: 414
    });

    $('.button_products_supplier').click(function(){
        $("#supplier_list_dialog").dialog('open');
        $.get(__url_supplier_list);
    });
});