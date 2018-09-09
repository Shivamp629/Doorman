// $(function() {
   	//make connection
	// var socket = io.connect('http://localhost:5000')

	// //buttons and inputs
	// var message = $("#message")
	// var username = $("#username")
	// var send_message = $("#send_message")
	// var send_username = $("#send_username")
	// var chatroom = $("#chatroom")
	// var feedback = $("#feedback")

	//Emit message
	// send_message.click(function(){
	// 	socket.emit('message', {message : message.val()})
	// })

	//Listen on new_message
	// socket.on("emotion", (data) => {
	// 	console.log(data)
	// })

	//Emit a username
	// send_username.click(function(){
	// 	socket.emit('change_username', {username : username.val()})
	// })
	//
	// //Emit typing
	// message.bind("keypress", () => {
	// 	socket.emit('typing')
	// })
	//
	// //Listen on typing
	// socket.on('typing', (data) => {
	// 	feedback.html("<p><i>" + data.username + " is typing a message..." + "</i></p>")
	// })
// });

$(document).ready(function(){
	namespace = '/test'; // change to an empty string to use the global namespace

	// the socket.io documentation recommends sending an explicit package upon connection
	// this is specially important when using the global namespace
	var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

	socket.on('connect', function(msg) {
		socket.emit('my event', {data: 'I\'m connected!'});
	});


	socket.on('message', function(msg){
		console.log(msg)
	});

});
