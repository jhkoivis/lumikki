
R_IRFOCUS = "/cmd/irfocus.cgi";
R_IRCONNECT = "/cmd/irconnect.cgi";
R_IRDISCONNECT = "/cmd/irdisconnect.cgi";
R_IRIMAGESERIES = "/cmd/irimageseries.cgi";
R_IRSTOP = "/cmd/irstop.cgi";
R_IRSIMULATETRIGGER = "/cmd/irsimulatetrigger.cgi";

ir = {

	irConnectRequest: function () {
		general.request(R_IRCONNECT)
	},
	
	irDisconnectRequest: function() {
		general.request(R_IRDISCONNECT);
	},
	
	irFocusRequest: function() {
		general.request(R_IRFOCUS);
	},
	
	irStopRequest: function() {
		general.request(R_IRSTOP);
	},
	
	irImageSeriesRequest: function() {
		general.request(R_IRIMAGESERIES);
	},
	
	irSimulateTriggerRequest: function(){
		general.request(R_IRSIMULATETRIGGER);
	},
	
	irTransferAction: function() {
	    general.transferStateOfForm("ir");
	}
}
