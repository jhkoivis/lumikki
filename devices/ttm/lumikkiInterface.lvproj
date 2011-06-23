<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="9008000">
	<Property Name="varPersistentID:{27A437C3-08E6-4272-BF4C-BCA3A427A737}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/stop</Property>
	<Property Name="varPersistentID:{2B2FC599-F619-4235-B2BA-4148E630442A}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/creepRunning</Property>
	<Property Name="varPersistentID:{328BF208-91FB-42DF-90F1-1D0F893C8AAB}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/expId</Property>
	<Property Name="varPersistentID:{336383FD-A068-47D7-BCDB-43B3AE27493D}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/channelInt</Property>
	<Property Name="varPersistentID:{34B2EAD7-88AF-4171-88AF-0015D3E71CEF}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/setpointTime</Property>
	<Property Name="varPersistentID:{502809B8-22B0-44C2-89E0-65ACE7145AE6}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/startStatusQuery</Property>
	<Property Name="varPersistentID:{80BFE2B5-B71D-403E-939A-EE2C41E4D3CC}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/loggingIsOn</Property>
	<Property Name="varPersistentID:{8B411B40-7358-46B4-8486-EBC064765ADE}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/busy</Property>
	<Property Name="varPersistentID:{8D94BF3C-E8AD-4BC6-B6AC-5588B36BB534}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/startCreep</Property>
	<Property Name="varPersistentID:{8DF4073D-E5FF-49EF-92EB-9C1E14A7C45E}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/newSetpointCommand</Property>
	<Property Name="varPersistentID:{945017DA-938E-4FB6-9D3E-F8A2B85F5443}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/startRamp</Property>
	<Property Name="varPersistentID:{9BFCA6F4-477D-4AE1-BA4E-0DEA32C88F3C}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/creepLoad</Property>
	<Property Name="varPersistentID:{A08E68F5-7EA0-4B22-A0D7-7D0C2C951E29}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/startLogging</Property>
	<Property Name="varPersistentID:{A3B70838-E574-40C5-9727-A5407E46F553}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/statusText</Property>
	<Property Name="varPersistentID:{AE3850BA-CACD-44E6-A2DA-285D8087E66B}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/statusCode</Property>
	<Property Name="varPersistentID:{CBF25575-E584-488F-87C1-99997E90A92E}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/startSetRamp</Property>
	<Property Name="varPersistentID:{D35C91FC-7202-4C7F-B1FB-9AD09AB88073}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/rampAmplitude</Property>
	<Property Name="varPersistentID:{DC07E9E3-96F8-4700-8BDF-E46784C10E56}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/setpoint</Property>
	<Property Name="varPersistentID:{F4E9CABE-A97B-4289-AD67-613727397037}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/stopLogging</Property>
	<Property Name="varPersistentID:{FF1066FC-C3B1-4F72-A129-42DE239D4CB1}" Type="Ref">/My Computer/lumikkiVariableList.lvlib/rampRate</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="csm_lumikki_instron_moveToSetpoint_poller.vi" Type="VI" URL="../csm_lumikki_instron_moveToSetpoint_poller.vi"/>
		<Item Name="csm_lumikki_instron_startLogging_poller.vi" Type="VI" URL="../csm_lumikki_instron_startLogging_poller.vi"/>
		<Item Name="csm_lumikki_instron_stopLogging_poller.vi" Type="VI" URL="../csm_lumikki_instron_stopLogging_poller.vi"/>
		<Item Name="csm_lumikki_instron_initRamp_poller.vi" Type="VI" URL="../csm_lumikki_instron_initRamp_poller.vi"/>
		<Item Name="csm_lumikki_instron_startRamp_poller.vi" Type="VI" URL="../csm_lumikki_instron_startRamp_poller.vi"/>
		<Item Name="csm_lumikki_instron_creep_poller.vi" Type="VI" URL="../csm_lumikki_instron_creep_poller.vi"/>
		<Item Name="csm_lumikki_instron_status_poller.vi" Type="VI" URL="../csm_lumikki_instron_status_poller.vi"/>
		<Item Name="csm_lumikki_instron_stop_poller.vi" Type="VI" URL="../csm_lumikki_instron_stop_poller.vi"/>
		<Item Name="csm_lumikki_instron_moveToSetpoint.vi" Type="VI" URL="../csm_lumikki_instron_moveToSetpoint.vi"/>
		<Item Name="csm_lumikki_instron_startLogging.vi" Type="VI" URL="../csm_lumikki_instron_startLogging.vi"/>
		<Item Name="csm_lumikki_instron_stopLogging.vi" Type="VI" URL="../csm_lumikki_instron_stopLogging.vi"/>
		<Item Name="csm_lumikki_instron_initRamp.vi" Type="VI" URL="../csm_lumikki_instron_initRamp.vi"/>
		<Item Name="csm_lumikki_instron_startRamp.vi" Type="VI" URL="../csm_lumikki_instron_startRamp.vi"/>
		<Item Name="csm_lumikki_instron_stop.vi" Type="VI" URL="../csm_lumikki_instron_stop.vi"/>
		<Item Name="csm_lumikki_instron_init.vi" Type="VI" URL="../csm_lumikki_instron_init.vi"/>
		<Item Name="csm_lumikki_instron_creep.vi" Type="VI" URL="../csm_lumikki_instron_creep.vi"/>
		<Item Name="lumikkiVariableList.lvlib" Type="Library" URL="../lumikkiVariableList.lvlib"/>
		<Item Name="MX Data Logging Read.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Data Acquisition/MX Data Logging Read.vi"/>
		<Item Name="csm_lumikki_instron_status.vi" Type="VI" URL="../csm_lumikki_instron_status.vi"/>
		<Item Name="MX System Status with Dialog.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/System Status/MX System Status with Dialog.vi"/>
		<Item Name="csm_lumikki_instron_statusQue.vi" Type="VI" URL="../csm_lumikki_instron_statusQue.vi"/>
		<Item Name="statusQuery.vi" Type="VI" URL="../lib/statusQuery.vi"/>
		<Item Name="moreSamplesToPlayback.vi" Type="VI" URL="../lib/moreSamplesToPlayback.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="Write File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write File+ (string).vi"/>
				<Item Name="compatWriteText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatWriteText.vi"/>
				<Item Name="Open Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Open Registry Key.vi"/>
				<Item Name="Registry SAM.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry SAM.ctl"/>
				<Item Name="Registry RtKey.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry RtKey.ctl"/>
				<Item Name="Registry refnum.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry refnum.ctl"/>
				<Item Name="Registry View.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry View.ctl"/>
				<Item Name="Registry WinErr-LVErr.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry WinErr-LVErr.vi"/>
				<Item Name="STR_ASCII-Unicode.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/STR_ASCII-Unicode.vi"/>
				<Item Name="Registry Handle Master.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Handle Master.vi"/>
				<Item Name="Read Registry Value Simple.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple.vi"/>
				<Item Name="Read Registry Value Simple STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple STR.vi"/>
				<Item Name="Registry Simplify Data Type.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Simplify Data Type.vi"/>
				<Item Name="Read Registry Value.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value.vi"/>
				<Item Name="Read Registry Value STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value STR.vi"/>
				<Item Name="Read Registry Value DWORD.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value DWORD.vi"/>
				<Item Name="Read Registry Value Simple U32.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple U32.vi"/>
				<Item Name="Close Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Close Registry Key.vi"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Write To Spreadsheet File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File.vi"/>
				<Item Name="Write To Spreadsheet File (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (DBL).vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="General Error Handler CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler CORE.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
				<Item Name="Write To Spreadsheet File (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (I64).vi"/>
				<Item Name="Write To Spreadsheet File (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (string).vi"/>
				<Item Name="NI_Matrix.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/Matrix/NI_Matrix.lvlib"/>
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="Wait types.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/Wait types.ctl"/>
				<Item Name="List Event Descriptions.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/List Event Descriptions.vi"/>
				<Item Name="List Events Available.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/List Events Available.vi"/>
				<Item Name="Create Error Clust.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/Create Error Clust.vi"/>
				<Item Name="Event Param Info.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/Event Param Info.vi"/>
				<Item Name="Create ActiveX Event Queue.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/Create ActiveX Event Queue.vi"/>
				<Item Name="Open_Create_Replace File.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/Open_Create_Replace File.vi"/>
				<Item Name="compatFileDialog.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatFileDialog.vi"/>
				<Item Name="compatOpenFileOperation.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatOpenFileOperation.vi"/>
				<Item Name="compatCalcOffset.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatCalcOffset.vi"/>
			</Item>
			<Item Name="Get Conversion Factors.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Data Acquisition/Get Conversion Factors.vi"/>
			<Item Name="MX Data Logging Start-Stop.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Data Acquisition/MX Data Logging Start-Stop.vi"/>
			<Item Name="MX Command.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/MX Command.vi"/>
			<Item Name="Setup Axis Selector.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Setup Axis Selector.vi"/>
			<Item Name="SX Command.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/SX Command.vi"/>
			<Item Name="8X00 Communication Central.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/8X00 Communication Central.vi"/>
			<Item Name="8X00 GPIB Query Error State.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/8X00 GPIB Query Error State.vi"/>
			<Item Name="Arby Spoll.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Arby Spoll.vi"/>
			<Item Name="Arby.dll" Type="Document" URL="Arby.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Write Commands to File.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Write Commands to File.vi"/>
			<Item Name="Global Variables.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Globals/Global Variables.vi"/>
			<Item Name="Write String to debug file.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Write String to debug file.vi"/>
			<Item Name="Get Local Time.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Get Local Time.vi"/>
			<Item Name="Kernel32.dll" Type="Document" URL="Kernel32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Path Details.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Path Details.vi"/>
			<Item Name="Path Maker.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Path Maker.vi"/>
			<Item Name="Update Error Cluster.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Error Handling/Update Error Cluster.vi"/>
			<Item Name="Get Application Special Folder Path.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Get Application Special Folder Path.vi"/>
			<Item Name="Application Special Folder.ctl" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Application Special Folder.ctl"/>
			<Item Name="Get Special Folder Path.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Get Special Folder Path.vi"/>
			<Item Name="shfolder.dll" Type="Document" URL="shfolder.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Generate String Buffer.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Generate String Buffer.vi"/>
			<Item Name="File Errors.ctl" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Error Handling/File Errors.ctl"/>
			<Item Name="Special Folder Required.ctl" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Special Folder Required.ctl"/>
			<Item Name="Append Path If String Not Empty.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Append Path If String Not Empty.vi"/>
			<Item Name="Write Characters To File - no error dialogue.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Write Characters To File - no error dialogue.vi"/>
			<Item Name="Arby Send.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Arby Send.vi"/>
			<Item Name="Manage 8X00 Device Status.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Manage 8X00 Device Status.vi"/>
			<Item Name="GetStatusMessageForDeviceID.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/GetStatusMessageForDeviceID.vi"/>
			<Item Name="GetStatusMessageForGroup.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/GetStatusMessageForGroup.vi"/>
			<Item Name="Arby Get Status.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Arby Get Status.vi"/>
			<Item Name="Write Status to File.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Write Status to File.vi"/>
			<Item Name="Status String.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Status String.vi"/>
			<Item Name="ReverseBuildStatRepString.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/ReverseBuildStatRepString.vi"/>
			<Item Name="Arby Query.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Arby Query.vi"/>
			<Item Name="Join command and selectors.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Join command and selectors.vi"/>
			<Item Name="MX Data Logging Setup.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Data Acquisition/MX Data Logging Setup.vi"/>
			<Item Name="Format &amp; Append with comma replace.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Format &amp; Append with comma replace.vi"/>
			<Item Name="8X00 Initialise.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/8X00 Initialise.vi"/>
			<Item Name="MX Get Device ID and GPIB Group.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/MX Get Device ID and GPIB Group.vi"/>
			<Item Name="RegFunc_RegGetGroupString.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/RegFunc_RegGetGroupString.vi"/>
			<Item Name="Regfunc.dll" Type="Document" URL="Regfunc.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Get Group ID.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Get Group ID.vi"/>
			<Item Name="MX Write GPIB Array Dev Info.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/MX Write GPIB Array Dev Info.vi"/>
			<Item Name="RegFunc_RegGetDeviceString.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/RegFunc_RegGetDeviceString.vi"/>
			<Item Name="Reg Get Device.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Reg Get Device.vi"/>
			<Item Name="Advapi32.dll" Type="Document" URL="Advapi32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Get Group Device Info.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Get Group Device Info.vi"/>
			<Item Name="Get Channel Info for each group.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Get Channel Info for each group.vi"/>
			<Item Name="RegFunc_GetSensorString.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/RegFunc_GetSensorString.vi"/>
			<Item Name="RegFunc_GetSensorValue.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/RegFunc_GetSensorValue.vi"/>
			<Item Name="Set Debug Flags.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Set Debug Flags.vi"/>
			<Item Name="Arby Register.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Arby Register.vi"/>
			<Item Name="This VI Name.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Setup/Utility/This VI Name.vi"/>
			<Item Name="Ramp Generator.vi" Type="VI" URL="../../csm_setpoint_and_ramp/Ramp Generator.vi"/>
			<Item Name="MX Ramp Rate.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Ramp Waveform/MX Ramp Rate.vi"/>
			<Item Name="Extract Array of Full Scales.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Extract Array of Full Scales.vi"/>
			<Item Name="Select Channels to match axes.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Select Channels to match axes.vi"/>
			<Item Name="MX Ramp Waveform Type.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Ramp Waveform/MX Ramp Waveform Type.vi"/>
			<Item Name="MX Ramp Amplitude.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Ramp Waveform/MX Ramp Amplitude.vi"/>
			<Item Name="MX Control Mode.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Control Mode/MX Control Mode.vi"/>
			<Item Name="MX Read Control Mode.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Control Mode/MX Read Control Mode.vi"/>
			<Item Name="MX Query.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/MX Query.vi"/>
			<Item Name="SX Query.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/SX Query.vi"/>
			<Item Name="MX Ramp Control.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Ramp Waveform/MX Ramp Control.vi"/>
			<Item Name="fileNameCreator.vi" Type="VI" URL="../../csm_setpoint_and_ramp/fileNameCreator.vi"/>
			<Item Name="MX Data Query.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Data Acquisition/MX Data Query.vi"/>
			<Item Name="MX Query Data Buffers.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Data Acquisition/MX Query Data Buffers.vi"/>
			<Item Name="GoSlowlyToSetpoint.vi" Type="VI" URL="../../csm_setpoint_and_ramp/GoSlowlyToSetpoint.vi"/>
			<Item Name="MX Set Point Advanced.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Control Mode/MX Set Point Advanced.vi"/>
			<Item Name="Build Command Array C123 s cv1 cv2 cv3.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Build Command Array C123 s cv1 cv2 cv3.vi"/>
			<Item Name="Create Command C123 s cv1 cv2 cv3.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Create Command C123 s cv1 cv2 cv3.vi"/>
			<Item Name="MX Sample Data Buffer Load.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Sample Data Playback/MX Sample Data Buffer Load.vi"/>
			<Item Name="MX Convert Sample Data to Command String.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Sample Data Playback/MX Convert Sample Data to Command String.vi"/>
			<Item Name="MX Sample Data Parameters.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Sample Data Playback/MX Sample Data Parameters.vi"/>
			<Item Name="MX System Status Dialog.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/System Status/MX System Status Dialog.vi"/>
			<Item Name="Display Status Dialogue Box.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/System Status/Display Status Dialogue Box.vi"/>
			<Item Name="Fetch INI Entry.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Fetch INI Entry.vi"/>
			<Item Name="MX System Status.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/System Status/MX System Status.vi"/>
			<Item Name="MX Combined Status.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/System Status/MX Combined Status.vi"/>
			<Item Name="MX Cyclic Control.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Cyclic Waveform/MX Cyclic Control.vi"/>
			<Item Name="manipulate3Columns.vi" Type="VI" URL="../../csm_setpoint_and_ramp/manipulate3Columns.vi"/>
			<Item Name="lvanlys.dll" Type="Document" URL="../../../Program Files/National Instruments/LabVIEW 2009/resource/lvanlys.dll"/>
			<Item Name="MX Arbitrator Globals.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/MX Arbitrator Globals.vi"/>
			<Item Name="CreateCreepSamples.vi" Type="VI" URL="../lib/CreateCreepSamples.vi"/>
			<Item Name="samplePlaybackGenerator.dll" Type="Document" URL="../lib/samplePlaybackGenerator.dll"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="lumikki" Type="RESTful WS">
				<Property Name="Bld_buildSpecName" Type="Str">lumikki</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Destination[0].destName" Type="Str">lumikki.lvws</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/lumikki/lumikki/internal.llb</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/lumikki/lumikki/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[0].template" Type="Str">/csm_lumikki_instron_moveToSetpoint/:setPointTime/:setPoint</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[0].VIName" Type="Str">csm_lumikki_instron_moveToSetpoint.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[1].template" Type="Str">/csm_lumikki_instron_startLogging/:expId</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[1].VIName" Type="Str">csm_lumikki_instron_startLogging.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[2].template" Type="Str">/csm_lumikki_instron_stopLogging</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[2].VIName" Type="Str">csm_lumikki_instron_stopLogging.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[3].template" Type="Str">/csm_lumikki_instron_initRamp/:rampRate/:rampAmplitude</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[3].VIName" Type="Str">csm_lumikki_instron_initRamp.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[4].template" Type="Str">/csm_lumikki_instron_startRamp</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[4].VIName" Type="Str">csm_lumikki_instron_startRamp.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[5].template" Type="Str">/csm_lumikki_instron_stop</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[5].VIName" Type="Str">csm_lumikki_instron_stop.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[6].template" Type="Str">/csm_lumikki_instron_creep</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[6].VIName" Type="Str">csm_lumikki_instron_creep.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[7].template" Type="Str">/csm_lumikki_instron_creep/:creepLoad/:channelInt</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[7].VIName" Type="Str">csm_lumikki_instron_creep.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[8].template" Type="Str">/csm_lumikki_instron_status</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[8].VIName" Type="Str">csm_lumikki_instron_status.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplateCount" Type="Int">9</Property>
				<Property Name="Source[0].itemID" Type="Str">{56681B55-B83C-4840-BFF6-D2F62BD250AF}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/csm_lumikki_instron_stopLogging_poller.vi</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[10].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[10].itemID" Type="Ref">/My Computer/csm_lumikki_instron_startRamp.vi</Property>
				<Property Name="Source[10].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">JSON</Property>
				<Property Name="Source[10].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[10].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[11].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[11].itemID" Type="Ref">/My Computer/csm_lumikki_instron_stop.vi</Property>
				<Property Name="Source[11].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">JSON</Property>
				<Property Name="Source[11].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[11].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[12].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[12].itemID" Type="Ref">/My Computer/csm_lumikki_instron_creep.vi</Property>
				<Property Name="Source[12].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">JSON</Property>
				<Property Name="Source[12].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[12].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[13].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[13].itemID" Type="Ref">/My Computer/csm_lumikki_instron_status.vi</Property>
				<Property Name="Source[13].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">JSON</Property>
				<Property Name="Source[13].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[13].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/csm_lumikki_instron_init.vi</Property>
				<Property Name="Source[2].type" Type="Str">VI</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/csm_lumikki_instron_initRamp_poller.vi</Property>
				<Property Name="Source[3].type" Type="Str">VI</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/csm_lumikki_instron_moveToSetpoint.vi</Property>
				<Property Name="Source[4].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">JSON</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[4].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/csm_lumikki_instron_startLogging_poller.vi</Property>
				<Property Name="Source[5].type" Type="Str">VI</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/My Computer/csm_lumikki_instron_startRamp_poller.vi</Property>
				<Property Name="Source[6].type" Type="Str">VI</Property>
				<Property Name="Source[7].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[7].itemID" Type="Ref">/My Computer/csm_lumikki_instron_startLogging.vi</Property>
				<Property Name="Source[7].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">JSON</Property>
				<Property Name="Source[7].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[7].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[8].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[8].itemID" Type="Ref">/My Computer/csm_lumikki_instron_stopLogging.vi</Property>
				<Property Name="Source[8].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">JSON</Property>
				<Property Name="Source[8].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[8].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[9].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[9].itemID" Type="Ref">/My Computer/csm_lumikki_instron_initRamp.vi</Property>
				<Property Name="Source[9].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">JSON</Property>
				<Property Name="Source[9].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[9].type" Type="Str">RESTfulVI</Property>
				<Property Name="SourceCount" Type="Int">14</Property>
				<Property Name="WebSrvc_enableDebugging" Type="Bool">true</Property>
				<Property Name="WebSrvc_serviceGUID" Type="Str">{C3134F95-9BBA-4846-98B5-326E0C907D4C}</Property>
				<Property Name="WebSrvc_serviceName" Type="Str">lumikki</Property>
			</Item>
		</Item>
	</Item>
</Project>
