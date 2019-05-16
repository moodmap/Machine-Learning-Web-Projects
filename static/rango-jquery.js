$(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });

    $("#about-btn").click( function(event) {
        msgstr = $("#msg").html()
        msgstr = msgstr + "ooooooooooo"
        $("#msg").html(msgstr)
    });

    $( "#about-btn" ).on( "click", function() {
    $("body").css("background-color","#000000");
    });

});
