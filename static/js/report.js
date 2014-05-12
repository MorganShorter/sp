$(function () {
    $(".dt_from").datepicker({
        defaultDate: "-1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: 'yy-mm-dd',
        onClose: function(selectedDate) {
            $(this).parents('form').find(".dt_to").datepicker( "option", "minDate", selectedDate );
        }
    });
    $( ".dt_to" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: 'yy-mm-dd',
        onClose: function( selectedDate ) {
            $(this).parents('form').find(".dt_from").datepicker( "option", "maxDate", selectedDate );
        }
    });
    $('.report_to_pdf').live("click", function(){
        var form = $('#' + $(this).parents('div[action_id]').attr('action_id'));
        document.location = form.attr('action') + '?' + form.serialize() + '&format=pdf';
    });
    $('.report_to_csv').live("click", function(){
        var form = $('#' + $(this).parents('div[action_id]').attr('action_id'));
        document.location = form.attr('action') + '?' + form.serialize() + '&format=csv';
    });


    /* Report 1
    * */
     $("#model_report_1").dialog({
        title: "Sales Order Listing",
        autoOpen: false,
        width: '280px',
        close: function( event, ui ) {
            $("#model_report_1_table").dialog('close');
        }
    });
    $("#model_report_1_table").dialog({
        title: "Sales Order Listing",
        autoOpen: false,
        width: 800,
        height: 500,
        close: function( event, ui ) {
        }
    });
    $("#menu_report_1").click(function(){
        $("#model_report_1").dialog("open");
    });

    $("#report_1_get").live("click", function(){
        $("#model_report_1_table").dialog("close");
        $('#frm_report_1').ajaxSubmit({
            success: function(){
                $("#report1_accordion").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                }).accordion( "refresh" );
            }
        });

    });



    /* Report 2
    * */
     $("#model_report_2").dialog({
        title: "Top Sellers",
        autoOpen: false,
        width: '280px',
        close: function( event, ui ) {
            $("#model_report_2_table").dialog('close');
        }
    });
    $("#model_report_2_table").dialog({
        title: "Top Sellers (first 100)",
        autoOpen: false,
        width: 800,
        height: 500,
        close: function( event, ui ) {
        }
    });
    $("#menu_report_2").click(function(){
        $("#model_report_2").dialog("open");
    });
    $("#report_2_get").live("click", function(){
        $("#model_report_2_table").dialog("close");
        $('#frm_report_2').ajaxSubmit({
            success: function(){

            }
        });

    });

    /* Report 3
    * */
     $("#model_report_3").dialog({
        title: "Sent items",
        autoOpen: false,
        width: '280px',
        close: function( event, ui ) {
            $("#model_report_3_table").dialog('close');
        }
    });
    $("#model_report_3_table").dialog({
        title: "Sent items",
        autoOpen: false,
        width: 800,
        height: 500,
        close: function( event, ui ) {
        }
    });
    $("#menu_report_3").click(function(){
        $("#model_report_3").dialog("open");
    });

    $("#report_3_get").live("click", function(){
        $("#model_report_3_table").dialog("close");
        $('#frm_report_3').ajaxSubmit({
            success: function(){
                $("#report3_accordion").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                }).accordion( "refresh" );
            }
        });

    });

});