$(function () {
    $(".dt_from").datepicker({
        defaultDate: "-1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: 'dd/mm/yy',
        onClose: function(selectedDate) {
            $(this).parents('form').find(".dt_to").datepicker( "option", "minDate", selectedDate );
        }
    });
    $( ".dt_to" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: 'dd/mm/yy',
        onClose: function( selectedDate ) {
            $(this).parents('form').find(".dt_from").datepicker( "option", "maxDate", selectedDate );
        }
    });
    $('.report_to_pdf').live("click", function(){
        var form = $('#' + $(this).parents('div[action_id]').attr('action_id'));
        if (form.length == 0){
            document.location = $(this).parent().parent().attr('report_get_url') + '?format=pdf';
        } else{
            document.location = form.attr('action') + '?' + form.serialize() + '&format=pdf';
        }
    });
    $('.report_to_csv').live("click", function(){
        var form = $('#' + $(this).parents('div[action_id]').attr('action_id'));
        if (form.length == 0){
            document.location = $(this).parent().parent().attr('report_get_url') + '?format=csv';
        } else {
            document.location = form.attr('action') + '?' + form.serialize() + '&format=csv';
        }
    });





    /* Report 1
    * */
     $("#model_report_1").dialog({
        title: "Sales Order Listing",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {
            $("#model_report_1_table").dialog('close');
        }
    });
    $("#model_report_1_table").dialog({
        title: "Sales Order Listing",
        autoOpen: false,
        resizable: false,
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
        var $loader = loader_on('#model_report_1');
        $('#frm_report_1').ajaxSubmit({
            success: function(){
                $("#report1_accordion").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                }).accordion( "refresh" );
                $("#model_report_1_table").dialog("open");
                $loader.remove();
            },
            error: function(){
                $loader.remove();
                alert('Error! Please try again.');
            }
        });

    });






    /* Report 2
    * */
     $("#model_report_2").dialog({
        title: "Top Sellers",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {
            $("#model_report_2_table").dialog('close');
        }
    });
    $("#model_report_2_table").dialog({
        title: "Top Sellers (first 100)",
        autoOpen: false,
        resizable: false,
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
        var $loader = loader_on('#model_report_2');
        $('#frm_report_2').ajaxSubmit({
            success: function(){
                $loader.remove();
            },
            error: function(){
                $loader.remove();
                alert('Error! Please try again.');
            }
        });

    });





    /* Report 3
    * */
    $("#model_report_3").dialog({
        title: "Sent items",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {
            $("#model_report_3_table").dialog('close');
        }
    });
    $("#model_report_3_table").dialog({
        title: "Sent items",
        autoOpen: false,
        resizable: false,
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
        var $loader = loader_on('#model_report_3');
        $('#frm_report_3').ajaxSubmit({
            success: function(){
                $("#report3_accordion").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                }).accordion( "refresh" );
                $loader.remove();
            },
            error: function(){
                $loader.remove();
                alert('Error! Please try again.');
            }
        });

    });





    /* Report 4
    * */
    $("#model_report_4_table").dialog({
        title: "Minimum Stock Report",
        autoOpen: false,
        resizable: false,
        width: 800,
        height: 500,
        open: function( event, ui ) {
            $.get($('#model_report_4_table').attr('report_get_url'));
        }
    });
    $("#menu_report_4").click(function(){
        $("#model_report_4_table").dialog("open");
    });





    /* Report 5
    * */
    $("#model_report_5").dialog({
        title: "Volume by Product",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {
            $("#model_report_5_table").dialog('close');
        }
    });
    $("#model_report_5_table").dialog({
        title: "Volume by Product",
        autoOpen: false,
        resizable: false,
        width: 800,
        height: 500,
        close: function( event, ui ) {
        }
    });
    $("#menu_report_5").click(function(){
        $("#model_report_5").dialog("open");
    });

    $('.add_product_to_report5').live('click', function(){
        $('.report_5_products tbody .empty_row').hide();

        var pform = $('#frm_product');
        var pid = $('.product_id', pform).val(),
            pcode = $('.product_code', pform).val(),
            pname = $('.product_name', pform).val();

        if ($('.report_5_products tbody tr[pid=' + pid + ']').length == 0){
            $('.report_5_products tbody').append("<tr pid='"+ pid +
                        "' class='form_list_row'><td>" + pcode + "</td><td>" + pname +
                        "</td><td><div class='btn_cancel'></div></td></tr>");
        }

        if (!$("#model_report_5").dialog( "isOpen" )){
            $("#model_report_5").dialog("open");
        }
        $("#model_report_5").dialog( "moveToTop" );
    });

    $('.add_product_from_list_to_report5').live('click', function(){
        $('.report_5_products tbody .empty_row').hide();
        var prnt = $(this).parents('tr');
        var pid = $(prnt).attr('cid'),
            pcode = $('.pr_code', prnt).text(),
            pname = $('.pr_name', prnt).text();

        if ($('.report_5_products tbody tr[pid=' + pid + ']').length == 0){
            $('.report_5_products tbody').append("<tr pid='"+ pid +
                        "' class='form_list_row'><td>" + pcode + "</td><td>" + pname +
                        "</td><td><div class='btn_cancel'></div></td></tr>");
        }

        if (!$("#model_report_5").dialog( "isOpen" )){
            $("#model_report_5").dialog("open");
        }
        $("#model_report_5").dialog( "moveToTop" );

        return false;
    });

    $('.report_5_products tbody .btn_cancel').live('click', function(){
        $(this).parents('tr').remove();
        if ($('.report_5_products tbody tr:visible').length == 0){
            $('.report_5_products tbody .empty_row').show();
        }
    });

    $("#report_5_get").live("click", function(){
        if ($('.report_5_products tbody tr:not(.empty_row)').length == 0){
            alert('You have to add some product');
            return
        }
        var $table = $('#frm_report_5');

        var prod_ids = $('.report_5_products tbody tr:not(.empty_row)').map(function() {
            return $(this).attr('pid');
        }).get().join();

        $('.product_ids', $table).val(prod_ids);
        $("#model_report_5_table").dialog("close");
        var $loader = loader_on('#model_report_5');
        $table.ajaxSubmit({
            success: function(){
                $("#report5_accordion").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                }).accordion( "refresh" );
                $("#model_report_5_table").dialog("open");
                $loader.remove();
            },
            error: function(){
                $loader.remove();
                alert('Error! Please try again.');
            }
        });


    });





    /* Report 6
    * */
     $("#model_report_6").dialog({
        title: "Product Stock Costings (stocktake)",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {
            $("#model_report_6_table").dialog('close');
        }
    });
    $("#model_report_6_table").dialog({
        title: "Product Stock Costings (stocktake)",
        autoOpen: false,
        resizable: false,
        width: 800,
        height: 500,
        close: function( event, ui ) {
        }
    });
    $("#menu_report_6").click(function(){
        $("#model_report_6").dialog("open");
    });

    $("#report_6_get").live("click", function(){
        $("#model_report_6_table").dialog("close");
        var $loader = loader_on('#model_report_6');
        $('#frm_report_6').ajaxSubmit({
            success: function(){
                $("#report6_accordion").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                }).accordion( "refresh" );

                $(".report6_sub_accordion").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                });

                $("#model_report_6_table").dialog("open");
                $loader.remove();
            },
            error: function(){
                $loader.remove();
                alert('Error! Please try again.');
            }
        });

    });






    /* Report 7
    * */
     $("#model_report_7").dialog({
        title: "Royalty Summary by Type",
        autoOpen: false,
        resizable: false,
        width: 'auto',
        close: function( event, ui ) {
            $("#model_report_7_table").dialog('close');
        }
    });
    $("#model_report_7_table").dialog({
        title: "Royalty Summary by Type",
        autoOpen: false,
        resizable: false,
        width: 800,
        height: 500,
        close: function( event, ui ) {
        }
    });
    $("#menu_report_7").click(function(){
        $("#model_report_7").dialog("open");
    });

    $("#report_7_get").live("click", function(){
        $("#model_report_7_table").dialog("close");
        var $loader = loader_on('#model_report_7');
        $('#frm_report_7').ajaxSubmit({
            success: function(){
                $("#report7_accordion").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                }).accordion( "refresh" );
                $("#model_report_7_table").dialog("open");
                $loader.remove();
            },
            error: function(){
                $loader.remove();
                alert('Error! Please try again.');
            }
        });

    });

});