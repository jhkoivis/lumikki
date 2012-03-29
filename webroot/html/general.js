
general = {
		request: function (cgiFileName){
			var id = reqId();
			var params = JSON.stringify({"id":id}); 
			logC(cgiFileName + "::" + params);
			$.post(	cgiFileName, params, function(response) { 
					logR(cgiFileName + "::" + JSON.stringify(response)); 
					showError(response);
					}, "json");
		},
		
		transferStateOfForm: function(formName){
			/* 
				Check all variables starting with formName and
				add them to memcache via stateMap -> stateAction -> config.py
			*/
			logC("test");
		    var id = reqId(), stateMap = {"id":id}, i=0;
		    var formChildren = $("#" + formName + " > *");
		    for (i=0; i < formChildren.length; i++) {
		    o = formChildren[i];
		    if (o.id.match("^" + formName + "_") == (formName + "_")) {
		    	/* different types of input require different handling */
		    	if (o.type == "checkbox"){
		    		stateMap[o.id] = $("#" + o.id).is(":checked");
		    	}
		    	else if (o.type == "select-one"){
		    		stateMap[o.id] = $("#" + o.id).val();
		    	}
		    	else {
		    		stateMap[o.id] = $("#" + o.id).val();
		    		
		    	}
		    	logR(o.type + ' : ' + o.id + '=' + stateMap[o.id])  
		    }
		    }
		    stateAction(stateMap); 
		} 
}