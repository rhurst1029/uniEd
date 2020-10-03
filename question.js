$(function(){
	$('button').click(function(){
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/addQuestion',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});