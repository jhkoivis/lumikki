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
R_RUN = "/cmd/run.cgi";

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


function run(json) {
    run.json = json; 
}


function echo(json) {
    echo.json = json;
    logC("echo model says: " + echo.json.echo);
}

function doEcho() {
    var s = JSON.stringify({ echo:"success"});
    logC(R_ECHO + "::" + s);
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

function status(value) {
    status.st[value.target] = value.status;
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
    var params =   JSON.stringify({'id':id, 'target':target});
    logC(request + "::" + params);
    $.post(request, params, function(data) { 
	logR("status: " + JSON.stringify(data)); 
	status(data); }, "json");
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
    var f2 = function(t) { var s = f(t); return t<100 ? "0"+s : s};
    return  f(d.getHours()) 
	+ ":" 
	+ f(d.getMinutes()) 
	+ ":" 
	+ f(d.getSeconds())
	+ "." 
	+ f2(parseInt((d.getMilliseconds()/1000*1000))
	   );
}


function logC(logstring) { log("C", logstring); }
function logR(logstring) { log("R", logstring); }
function log(id, logstring) {
    $('#css-log p:first').before("<p> "+ id + getTime() + " " + logstring +  "</p>");
}
