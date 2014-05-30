$(function () {
    $("#login_form_dialog").dialog({
        title: "Login",
        autoOpen: true,
        width: 'auto',
        closeOnEscape: false,
        draggable: false,
        position: {
            my: "center",
            at: "center",
            of: $('#container')
        },
        buttons: [{
            text: "Submit",
            click: function() {
                $("#frm_login", $(this)).submit();
            }
        }],
        close: function(){
            $(this).dialog('open');
        }
    }).dialogExtend({
        "closable" : false
    });

});