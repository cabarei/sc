console.log("ok");

$(document).ready(function(){

	console.log("load");
  
  	$(window).bind("click", function() {

		console.log("posting")
		
		$.ajax({
			url: 'http://localhost:5050/process',
			method: "POST",
			dataType: "json",
			data: JSON.stringify({'img': "hola"}),
			success: function (data){
				console.log("answer:", data)
				$("body").append("<br><br>sucess posting");
				$("body").append("<br>answer from server: " + data.answer);
			},
			error: function( error ){
				console.log("error:", error);
			}
		})
 	})
})
			 