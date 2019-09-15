$(document).ready(function(){
	namespace = '/test'; // change to an empty string to use the global namespace

	// the socket.io documentation recommends sending an explicit package upon connection
	// this is specially important when using the global namespace
	var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

	socket.on('connect', function(msg) {
		socket.emit('my event', {data: 'I\'m connected!'});
	});

	socket.on('message', function(d) {
		console.log(d)
		// var emoji = 'j';
		// if (emotion == 'happy') {
		// 	emoji = 😀
		// } else if (emotion == 'sad') {
		// 	emoji = 😭
		// } else if (emotion == 'angry') {
		// 	emoji = 😡
	    // } else if (emotion == 'disgust') {
		// 	emoji = 🤮
		// } else if (emotion == 'fear') {
		// 	emoji = 😱
	    // } else if (emotion == 'surprise') {
	    //     emoji = 😳
	    // } else if (emotion == 'neutral') {
	    //     emoji = 😛
	    // } else {
		// 	emoji = 😛
		// }

		$('#test').html('<h2>' + d.emotion + '</h2>');
		$('h2').css("margin-top", 0.2);
		$('h2').css("margin-bottom",0.2);
		$('h2').css("font",90);
		$('h2').css("font-weight",700);
		updateYoutubeVideo(d.song)
	});
});
