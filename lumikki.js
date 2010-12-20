$(document).ready(function() {
	$('#logstatus').submit(function() {
		getStatus();
		return false;
	    });
    });


$(function() {
	$(".css-tabs:first").tabs(".css-panes:first > div");
});

function getStatus() {
    $.get("http://localhost:8080/status", function(data) {
		alert(data.status);
    }, "json");
}
