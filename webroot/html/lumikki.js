$(document).ready(function() {
    $('#logstatus').submit(function() {
	updateMachineStatus();
	statusAction();
	return false;
    });
    $('#run').submit(function() {
	runAction();
	return false;
    });
    $('#stop').submit(function() {
	stopAction();
	return false;
    });
    $('#restore').submit(function() {
	restoreAction();
	return false;
    });
    $('#cam').submit(function() {
	camTransferAction();
	return false;
    });
    $('#ttm').submit(function() {
	ttmTransferAction();
	return false;
    });
    logC("UI created");
    statusAction();
    stateAction({});
});


$(function() {
	$(".css-tabs:first").tabs(".css-panes:first > div");
});


R_ECHO = "/cmd/echo.cgi";
R_STATUS = "/cmd/status.cgi";
R_RUN = "/cmd/run.cgi";
R_STATE = "/cmd/state.cgi";
R_LOCK = "/cmd/lock.cgi";
R_STOP = "/cmd/stop.cgi";

TTM=0;
AE=1;
CAM=2;
IR=3;

NMAP = ["Tensile", "AE", "Camera", "IR Camera"];

errmap = { "000":"Cannot connect to anything"
	   , "010":"Server sent unknown status"
	   , "020":"Server response did not contain status"
	   , "100":"Disabled from server."
	   , "110":"Target machine did not respond"
	   , "120":"Server received malformed command."
	   , "122":"Connection refused."
	   , "200":"Target available, values not set"
	   , "210":"Ready to measure"
	   , "220":"Measuring"
	   , "230":"System is busy, please try again in a while." 
	 };


/* *Action refers to UI event, which was received by the UI, 
e.g. button press */
function statusAction() {
    status.st = [];
    var i = 0;
    for(i=0; i < NMAP.length; i++) {
	status(i, statusRequest(R_STATUS, i)); 
    }
}

function restoreAction() {
    dumpMemcached();
}

function camTransferAction() {
    transferStateOfForm("cam");
}

function ttmTransferAction() {
    transferStateOfForm("ttm");
}

function runAction() {
    updateMachineStatus();
    runRequest();
}

function stopAction() {
    logC("stop sent");
    stopRequest();
}

function stateAction(inputMap) {
    stateRequest(inputMap, updateFormValues); 
}

function stopRequest() {
    var params = JSON.stringify({"id":reqId()});
    $.post(R_STOP, params, function(response) {
	if (!showError(response)) {
	    logR("stopped");
	}
    }, "json");
}


function runRequest() {
    var id = reqId();
    var valueMap = {   "id"     : id
                   , "g_measurementid" : $('#g_measurementid').val() 
                   }; 
    var params = JSON.stringify(valueMap); 
    logC(R_RUN + "::" + params);
    $.post(R_RUN, params, function(response) { 
	logR(R_RUN + "::" + JSON.stringify(response)); 
	showError(response);
    }, "json");

}


function stateRequest(inputMap, actionFunction) {
    inputMap["id"] = reqId();
    $.post(R_STATE, JSON.stringify(inputMap), function(response) {
	if (showError(response)==true) { return; }
	actionFunction(response);
     }, "json");
}



function statusRequest(request, target) {
    var rdata = null; 
    var id = reqId();
    var params =   JSON.stringify({'id':id, 'target':target});
    logC(request + "::" + params);
    $.post(request, params, function(data) { 
	logR("status: " + JSON.stringify(data)); 
	showError(data);
	status(data); }, "json");
}


function transferStateOfForm(formName) {
    var id = reqId(), stateMap = {"id":id}, i=0;
    var formChildren = $("#" + formName + " > *");
    for (i=0; i < formChildren.length; i++) {
	o = formChildren[i];
	if (o.id.match("^" + formName + "_") == (formName + "_")) {
	    stateMap[o.id] = $("#" + o.id).val();
	}
    }
    stateAction(stateMap); 
} 


function showError(response) {
    if (typeof response.st != 'undefined' && response.st != 0) {
	alert(typeof response.msg == 'undefined' ? "No message!" : 
	     response.msg);
	return true;
    }
    return false;
}


function dumpMemcached() {
    var i=0; 
    stateRequest({}, function(response) {
	if (showError(response) == true) return;
	logC("--STATE--");
	for(var key in response) {
	    logC(key + "=" + response[key]);
	}
    });
}


function updateFormValues(response) {
    logR(R_STATE + "::values updated succesfully to/from memcached.");
    for (var key in response) {
	var jqueryId = "#" + key;
	$(jqueryId).val(response[key]);
    }

}

function updateMachineStatus() {
    var new_active = [false, false, false, false];
    for (i=0; i <= IR; i++) {
	new_active[i] = $("#stableIsActive" + i).is(":checked");
    }
    stateRequest({'g_active':new_active}, function(r) {});
}

function activeStateObject(i) {
    function robj(response) {
	$("#stableIsActive" + i).attr("checked", response.g_active[i]);
    };
    return robj;
}

function showStatus() {
    var i = 0;
    for (i=0; i<= IR; i++) {
	$("#stableStatus" + i).text(status.st[i]);
	$("#stableDescr" + i).text(errmap[status.st[i]]);
	var robj = new activeStateObject(i);
	stateRequest({}, robj);
    }
}

function status(value) {
    status.st[value.target] = value.status;
    if (status.st.length == NMAP.length) {
	showStatus();
    }
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
