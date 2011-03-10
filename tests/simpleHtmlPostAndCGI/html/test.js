

$(document).ready(function() {
	$("#run").submit(function(){
			var params = JSON.stringify({"hello":"from test.js"});
	  	$.ajaxSetup({async:false});
			$.post(	"cmd/test.cgi", 
							params, 
							function(text){								
								alert(JSON.stringify(text));
							},
							"json");
	
	});
});

