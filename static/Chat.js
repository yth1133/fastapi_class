var socket = io();

var form = $("#message-form");
var input_box = $("#message");
var message_list = $("#messages");

form.submit(function(e) {
    e.preventDefault();
    socket.emit("message", input_box.val());
    input_box.val("");
});

socket.on("connect", function() {
    console.log("connected");
});

socket.on("message", function(data) {
    console.log(data);
    message_list.prepend("<p><span class='name'>" + data.name + "</span>: " + data.message + "</p>")
});

socket.on("join", function(data) {
    console.log(data);
    message_list.prepend("<div><span class='notice'>" + data + "</span></div>")
});

socket.on("leave", function(data) {
    console.log(data);
    message_list.prepend("<div><span class='notice'>" + data + "</span></div>")
});
