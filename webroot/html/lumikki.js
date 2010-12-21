$(document).ready(function() {
    $('#logstatus').submit(function() {
	getStatus();
	showStatus();
	return false;
    });
    logC("UI created");
});


$(function() {
	$(".css-tabs:first").tabs(".css-panes:first > div");
});



R_STATUS = "/status";

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


function showStatus() {
    var rowCount = $('#stable tr').length;
    for (i = 0; i < rowCount -1; i++) {
	$('#stable tr:last').remove()
    }	
    for(i=0; i<IR+1; i++) {
	$('#stable tr:last').after("<tr><td>" 
				   + NMAP[i]
				   + "</td><td>" 
				   + state.st[i]	
				   + "</td><td>" 
				   + errmap[state.st[i]]
				   + "</td></tr>");
    }
}

function state(id, value) {
    if (value == null) {
	state.st[id] = "000";
    } else if (typeof value.status == 'undefined') {
	state.st[id] =  "010";
    } else if (typeof errmap[value.status] == 'undefined') {
	state.st[id] = "020";
    } else {
	state.st[id] = value.status;
    }
}

function getStatus() {
    state.st = [];
    var i = 0;
    for(i=0; i<IR+1; i++) {
	state(i, request($.get, R_STATUS, i)); 
    }
}

function request(reqfun, request, target) {
    var rdata = null; 
    var id = reqId();
    var req = "i=" + id + "&t=" + target;
    logC(req);
    reqfun(request, req, function(data) { logR(req + " " +  data); rdata = data; }, "json");
    return rdata;
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
