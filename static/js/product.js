$(function () {
    /* Product
    * */
    $("#product_content").dialog({
        title: "Products",
        autoOpen: false,
        width: 414
    });
    $("#button_products_open_dialog").click(function () {
        $("#product_content").dialog("open");
    });
});