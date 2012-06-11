
// load xmldoc to DOM object
function loadXml(filename)
{
	if (window.XMLHttpRequest)	{// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}	
	else {// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.open("GET",filename,false);
	xmlhttp.send();
	xmlDoc=xmlhttp.responseXML;
	return xmlDoc;
}

// parse tab names from variables stored as DOM
function getTabNames(xmlDoc){
	// store all var-elements to variables
	var variables = xmlDoc.getElementsByTagName("var");
	// init tab name array
    var varList = new Array();
	for (i = 0; i < variables.length; i++ ){
		// get the "name"-element value
		var varName = variables[i].getElementsByTagName("name")[0].childNodes[0].nodeValue;
		// split the name by '_'
		var tabNames = varName.split('_');
		// use the beginning as tab name
		var tabName = tabNames[0];

		// if tab name array already contains the tab, do not add it
		// $.inArray is a Jquery function
		if ($.inArray(tabName,varList) == -1){
			varList.push(tabName);
		}
	}
    return varList;
}

// create tabs
// uses css-stylesheet
function createTabs(tabList){
    document.write('<ul class="css-tabs">\n');
    for (i in tabList){
        document.write('<li><a href="#">'+ tabList[i] + '</a></li>\n');
    }
    document.write('</ul>');    
}

function writeTabHeader(tabName){
    document.write('<div style="height:600px">\n');
}

function writeTabFooter(){
	document.write('</div>\n');
}

//function getTtmProtocolName_DEPRECATED(){
//	var variables = xmlDoc.getElementsByTagName("var");
//	var i = 0;
//	var protocol = "";
//   for (i = 0; i < variables.length; i++ ){
//	    var varName = variables[i].getElementsByTagName("name")[0].childNodes[0].nodeValue;
//	    if (varName == "ttm_global_protocol"){
//	    	protocol = variables[i].getElementsByTagName("value")[0].childNodes[0].nodeValue;
//	    } 
//   }
//    return protocol;
//}

// stateRequest is defined in lumikki.js
//function getTtmProtocolName(){
//	var protocol = "";
//	stateRequest({}, function(response) {
//		logC(response["ttm_global_protocol"]);
//       global_protocol = response["ttm_global_protocol"];
//        return global_protocol;
//    });
//	
//	return global_protocol;
//}

// write a form with id=$tabName and put all variables that start with $tabName in it
// see getTabNames function for comments (similar to this)
function writeFormWithVariables(tabName){
	document.write('<div style="float:left;width:600px;min-height:400px;display:block;border-width: 1px 1px 1px">\n'); 
	document.write('<form  id="' + tabName + '" action="" style="text-align:right">\n');
	
	var nameList = new Array();
	var variables = xmlDoc.getElementsByTagName("var");
	var i = 0;
    for (i = 0; i < variables.length; i++ ){
	    var varName = variables[i].getElementsByTagName("name")[0].childNodes[0].nodeValue;
	    //var title = variables[i].getElementsByTagName("title")[0].childNodes[0].nodeValue;
	    var compTabNames = varName.split('_');
	    var compTabName = compTabNames[0];
	    
	    
	    if (compTabName == tabName){
	    	nameList.push(varName);
	    	
	    }
    }
    
    nameList.sort()
    
    for (var i in nameList){ 
    	varName = nameList[i];
    	// write variable box	
        document.write('<label style="float:left" for="' + varName + '">' + varName + '</label>\n'); 
        document.write('<input type="text" size="20" maxlength="20" id="' + varName + '"><br />\n');   
	}
    
    // write 
    document.write('<input style="float:bottom;" type="submit" value="Apply" />\n');
    document.write('</form>\n');
    document.write('</div>\n');
}

// sort of factory method. It would be a factory, if it would return an object that does things. 
function writeSpecialTabContent(tabName){
	if (tabName == 'g')   {writeSpecialTabContentForG()};
	if (tabName == 'ttm') {writeSpecialTabContentForTtm()};
	if (tabName == 'cam') {writeSpecialTabContentForCam()};
	if (tabName == 'ir')  {writeSpecialTabContentForIr()};
	//if (tabName == 'temperature')	{temperature.writeSpecialTabContent()};
}


// special content functions...
// these are a bit messy...
// TODO: replace with "document-write-external-html"?
function writeSpecialTabContentForG(){
    	document.write('<div style="float:left;width:300px;min-height:200px;display:block;border-width: 1px 1px 1px">');
        document.write('<form  id="run" action="">');
        document.write('<p>');
        document.write('<label for="g_measurementid">Measurement ID (Max. len. 9)</label>');
        document.write('<input type="text"  size="20" maxlength="9" id="g_measurementid">');
        document.write('</p>');
        document.write('<p>');
        document.write('<input style="float:bottom;" type="submit" value="Run" />');
        document.write('</p>');
        document.write('</form>');
        document.write('<p>');
        document.write('<form  id="stop" action="">');
        document.write('<input style="float:bottom;" type="submit" value="Stop" />');
        document.write('</form>');
        document.write('</p>');
        document.write('<hr />');
        document.write('<p>');
        document.write('<form  id="restore" action="">');
        document.write('<input id="rbutton" style="float:bottom;" type="submit" value="Dump state" />');
        document.write('<br /><label for="rbutton" class="buttonlabel">Returns server state as log events.</label>');
        document.write('</form>');
        document.write('</p>');
        document.write('</div>');      
        document.write('<div style="float:right;width:300px;min-height:200px;display:block;border-width: 1px 1px 1px">');
        document.write('<table id="stable">');
        document.write('<tr>');
        document.write('<th>Machine</th><th>Status</th><th>Description</th><th>Active</th></tr>');
        document.write('<tr><td>TTM</td><td id="stableStatus0" /><td id="stableDescr0" /><td><input id="stableIsActive0"  type="checkbox" /></td></tr>');
        document.write('<tr><td>AE</td><td id="stableStatus1" /><td id="stableDescr1" /><td><input id="stableIsActive1"  type="checkbox" /></td></tr>');
        document.write('<tr><td>Camera</td><td id="stableStatus2" /><td id="stableDescr2" /><td><input id="stableIsActive2"  type="checkbox" /></td></tr>');
        document.write('<tr><td>IR</td><td id="stableStatus3" /><td id="stableDescr3" /><td><input id="stableIsActive3"  type="checkbox" /></td></tr>');
        document.write('<tr><td>Temperature</td><td id="stableStatus4" /><td id="stableDescr4" /><td><input id="stableIsActive4"  type="checkbox" /></td></tr>');
        document.write('</tr>');
        document.write('</table>');
        document.write('<form  id="logstatus" action="">');
        document.write('<input style="float:bottom;" type="submit" value="Force status" />');
        document.write('</form>');
        document.write('</div>');
}

function writeSpecialTabContentForTtm(){
	document.write('<div style="float:right;width:250px;min-height:200px;display:block;border-width: 1px 1px 1px">');
	document.write('<form  id="ttmsetpointrun" action="" style="text-align:right">');
	document.write('<input style="float:bottom;" type="submit" value="Move to Set Point" />');
	document.write('</form>');
	//document.write('<h1>Current Protocol: '+  getTtmProtocolName() +'</h1>')
	document.write('</div>');
}

function writeSpecialTabContentForCam(){}

function writeSpecialTabContentForIr(){
	document.write('<div style="float:right;width:250px;min-height:200px;display:block;border-width: 1px 1px 1px">');

	document.write('<form  id="irfocus" action="" style="text-align:right">');
	document.write('<input style="float:bottom;" type="submit" value="Focus IR Camera" />');
	document.write('</form>');
	document.write('<br />');
	
	document.write('<form  id="irconnect" action="" style="text-align:right">');
	document.write('<input style="float:bottom;" type="submit" value="Connect IR Camera" />');
	document.write('</form>');
	document.write('<br />');
	
	document.write('<form  id="irdisconnect" action="" style="text-align:right">');
	document.write('<input style="float:bottom;" type="submit" value="Disconnect IR Camera" />');
	document.write('</form>');
	document.write('<br />');
	
    document.write('<hr />');

    document.write('<form  id="irimageseries" action="" style="text-align:right">');
    document.write('<input style="float:bottom;" type="submit" value="Take a serie of images" />');
    document.write('</form>');
    document.write('<br />');
    
    document.write('<form  id="irstop" action="" style="text-align:right">');
    document.write('<input style="float:bottom;" type="submit" value="Stop recording" />');
    document.write('</form>');
   
    document.write('</div>');
}







 
