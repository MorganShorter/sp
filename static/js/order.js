$(function () {
    /* Order
    * */
    $("#order_content").dialog({
        title: "Show order",
        autoOpen: false,
        width: 800
    });
    $("#order_find").dialog({
        title: "Find order",
        autoOpen: false,
        width: 'auto'
    });

    $(".button_order_show_dialog").click(function () {
        $("#order_content").dialog("open");
    });
    $(".button_order_find_dialog").click(function () {
        $("#order_find").dialog("open");
    });

    // Search/Find Order
    $("#find_order_search").live('click', function(){
        var queryString = $('#frm_find_order').formSerialize();
        $.get(__url_order_list + '?' + queryString);
    });


    $("#order_order_date").datepicker({ dateFormat: 'dd/mm/yy' });
    $("#order_wanted_by").datepicker({ dateFormat: 'dd/mm/yy' });

    $('#frm_find_order .form_input').on('input', function(){
        $('#frm_find_order .form_input').not(this).val('');
    });
});