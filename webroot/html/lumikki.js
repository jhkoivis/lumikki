$(document).ready(function() {
    $('#logstatus').submit(function() {
	doStatus();
	return false;
    });
    logC("UI created");
    doEcho();
    doStatus();
});


$(function() {
	$(".css-tabs:first").tabs(".css-panes:first > div");
});


R_ECHO = "/cmd/echo.cgi"
R_STATUS = "/cmd/status.cgi";

TTM=0;
AE=1;
CAM=2;
IR=3;
NMAP = ["Tensile", "AE", "Camera", "IR Camera"];

errmap = { "000":"Cannot connect to anything"
	   , "010":"Server sent unknown status"
	   , "020":"Server response did not contain status"
	   , "100":"Target machine did not respond"
	   , "200":"Target available, values not set"
	   , "210":"Ready to measure"
	   , "220":"Measuring"
	   , "230":"State not available, please try again" 
	 };


function echo(json) {
    echo.json = json;
    logC("echo model says: " + echo.json.echo);
}

function doEcho() {
    var s = JSON.stringify({ echo:"success"});
    logC("Request: " + R_ECHO + " with " + s);
    $.post(R_ECHO, s, function(data) { logR("Echo response: " + JSON.stringify(data)); echo(data); }, 'json');
}

function showStatus() {
    var rowCount = $('#stable tr').length;
    for (i = 0; i < rowCount -1; i++) {
	$('#stable tr:last').remove()
    }	
    for(i=0; i < NMAP.length; i++) {
	$('#stable tr:last').after("<tr><td>" 
				   + NMAP[i]
				   + "</td><td>" 
				   + status.st[i]	
				   + "</td><td>" 
				   + errmap[status.st[i]]
				   + "</td></tr>");
    }
}

function status(target, value) {
    if (value == null) {
	status.st[target] = "000";
    } else if (typeof value.status == 'undefined') {
	status.st[target] =  "010";
    } else if (typeof errmap[value.status] == 'undefined') {
	status.st[target] = "020";
    } else {
	status.st[target] = value.status;
    }
    if (status.st.length == NMAP.length) {
	showStatus();
    }
}

function doStatus() {
    status.st = [];
    var i = 0;
    for(i=0; i < NMAP.length; i++) {
	status(i, request(R_STATUS, i)); 
    }
}

function request(request, target) {
    var rdata = null; 
    var id = reqId();
    var params =   "i=" + id + "&t=" + target;
    logC(request + "?" + params);
    $.get(request, params, function(data) { 
	logR(req + " " +  data); 
	status(target, data); }, "json");
}


function reqId() {
    if ( typeof reqId.c == 'undefined' || reqId.c > 9998) {
        reqId.c = 999;
    }
    return ++reqId.c;
}

function getTime() {
    var d = new Date();
    var f = function(t) { return t<10 ? "0" + t : "" + t; }; 
    return  f(d.getHours()) 
	+ ":" 
	+ f(d.getMinutes()) 
	+ ":" 
	+ f(d.getSeconds())
	+ "." 
	+ f(parseInt((d.getMilliseconds()/1000*100))
	   );
}


function logC(logstring) { log("C", logstring); }
function logR(logstring) { log("R", logstring); }
function log(id, logstring) {
    $('#css-log p:first').before("<p> "+ id + getTime() + " " + logstring +  "</p>");
}
