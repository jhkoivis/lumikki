<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="9008000">
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
		<Item Name="csm_lumikki_instron_init.vi" Type="VI" URL="../csm_lumikki_instron_init.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
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
			</Item>
			<Item Name="8X00 Initialise.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/8X00 Initialise.vi"/>
			<Item Name="MX Get Device ID and GPIB Group.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/MX Get Device ID and GPIB Group.vi"/>
			<Item Name="RegFunc_RegGetGroupString.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/RegFunc_RegGetGroupString.vi"/>
			<Item Name="Regfunc.dll" Type="Document" URL="Regfunc.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Get Group ID.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Get Group ID.vi"/>
			<Item Name="MX Write GPIB Array Dev Info.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/MX Write GPIB Array Dev Info.vi"/>
			<Item Name="MX Arbitrator Globals.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/MX Arbitrator Globals.vi"/>
			<Item Name="RegFunc_RegGetDeviceString.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/RegFunc_RegGetDeviceString.vi"/>
			<Item Name="Reg Get Device.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Reg Get Device.vi"/>
			<Item Name="Advapi32.dll" Type="Document" URL="Advapi32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="kernel32.dll" Type="Document" URL="kernel32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Get Group Device Info.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Get Group Device Info.vi"/>
			<Item Name="Get Channel Info for each group.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Get Channel Info for each group.vi"/>
			<Item Name="RegFunc_GetSensorString.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/RegFunc_GetSensorString.vi"/>
			<Item Name="RegFunc_GetSensorValue.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/RegFunc_GetSensorValue.vi"/>
			<Item Name="Set Debug Flags.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Central/Set Debug Flags.vi"/>
			<Item Name="Global Variables.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Globals/Global Variables.vi"/>
			<Item Name="Get Application Special Folder Path.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Get Application Special Folder Path.vi"/>
			<Item Name="Application Special Folder.ctl" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Application Special Folder.ctl"/>
			<Item Name="Get Special Folder Path.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Get Special Folder Path.vi"/>
			<Item Name="shfolder.dll" Type="Document" URL="shfolder.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Generate String Buffer.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Utility/Generate String Buffer.vi"/>
			<Item Name="File Errors.ctl" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Error Handling/File Errors.ctl"/>
			<Item Name="Special Folder Required.ctl" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Special Folder Required.ctl"/>
			<Item Name="Path Maker.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Path Maker.vi"/>
			<Item Name="Path Details.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Path Details.vi"/>
			<Item Name="Update Error Cluster.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Error Handling/Update Error Cluster.vi"/>
			<Item Name="Append Path If String Not Empty.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Filing/Utility/Append Path If String Not Empty.vi"/>
			<Item Name="Arby Register.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/MultiAxis/Arbitrator Interface/Arby Register.vi"/>
			<Item Name="Arby.dll" Type="Document" URL="Arby.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="This VI Name.vi" Type="VI" URL="../../../Documents and Settings/All Users/Documents/Instron/FastTrack3/Common/Application/Setup/Utility/This VI Name.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
