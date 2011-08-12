<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="8608001">
	<Property Name="varPersistentID:{07364808-64E2-4394-AFE3-E1DDAF1EC41F}" Type="Ref">/My Computer/lib/camVariables.lvlib/parentFolder</Property>
	<Property Name="varPersistentID:{076DD2BD-9953-45D6-8991-FA41D3BE204A}" Type="Ref">/My Computer/lib/camVariables.lvlib/offsety</Property>
	<Property Name="varPersistentID:{1AD224DF-938D-496C-AE5B-DABA6F2EED19}" Type="Ref">/My Computer/lib/camVariables.lvlib/height</Property>
	<Property Name="varPersistentID:{318E48DA-6E37-4B3D-814F-48C473F31B5F}" Type="Ref">/My Computer/lib/camVariables.lvlib/exposure</Property>
	<Property Name="varPersistentID:{327B8348-A1DE-44F6-9C4F-536AAD9553A6}" Type="Ref">/My Computer/lib/camVariables.lvlib/index</Property>
	<Property Name="varPersistentID:{3C7B5A0C-DC86-44EC-972F-E6BAEF8E9447}" Type="Ref">/My Computer/lib/camVariables.lvlib/startCamera</Property>
	<Property Name="varPersistentID:{473E5AA5-2B15-4656-B2BD-612530CB9F06}" Type="Ref">/My Computer/lib/camVariables.lvlib/packSize</Property>
	<Property Name="varPersistentID:{4CEFE251-2707-4DC5-8AEB-8D4C133B9D9D}" Type="Ref">/My Computer/lib/camVariables.lvlib/stopCam</Property>
	<Property Name="varPersistentID:{656BBD78-20FA-4993-A095-833FA344F330}" Type="Ref">/My Computer/lib/camVariables.lvlib/fps</Property>
	<Property Name="varPersistentID:{834DA614-59E8-4011-9698-0C1012860ED0}" Type="Ref">/My Computer/lib/camVariables.lvlib/settingsChanged</Property>
	<Property Name="varPersistentID:{93D5A689-2C03-4A19-97FD-F5219B9F8C14}" Type="Ref">/My Computer/lib/camVariables.lvlib/width</Property>
	<Property Name="varPersistentID:{9939AD1D-AAA9-4812-A64C-6818C07BD961}" Type="Ref">/My Computer/lib/camVariables.lvlib/offsetx</Property>
	<Property Name="varPersistentID:{B5D66EC9-ADE9-4616-A97E-E57DDDD665BA}" Type="Ref">/My Computer/lib/camVariables.lvlib/camSettings</Property>
	<Property Name="varPersistentID:{DFC54FF6-B004-477D-9130-8C8FD52829EC}" Type="Ref">/My Computer/lib/camVariables.lvlib/SaunaInfo</Property>
	<Property Name="varPersistentID:{FE038D34-B03F-4C6D-A961-FA009F34F2A7}" Type="Ref">/My Computer/lib/camVariables.lvlib/testName</Property>
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
		<Item Name="lib" Type="Folder">
			<Item Name="cameraServer.vi" Type="VI" URL="../cameraServer.vi"/>
			<Item Name="CameraSettingsManual.vi" Type="VI" URL="../CameraSettingsManual.vi"/>
			<Item Name="CameraShootManual.vi" Type="VI" URL="../CameraShootManual.vi"/>
			<Item Name="camVariables.lvlib" Type="Library" URL="../camVariables.lvlib"/>
			<Item Name="humidityController.vi" Type="VI" URL="../humidityController.vi"/>
		</Item>
		<Item Name="serverCommands" Type="Folder">
			<Item Name="camera_stop.vi" Type="VI" URL="../camera_stop.vi"/>
			<Item Name="camera_run.vi" Type="VI" URL="../camera_run.vi"/>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="NI_Vision_Acquisition_Software.lvlib" Type="Library" URL="/&lt;vilib&gt;/vision/driver/NI_Vision_Acquisition_Software.lvlib"/>
				<Item Name="IMAQdx.ctl" Type="VI" URL="/&lt;vilib&gt;/userDefined/High Color/IMAQdx.ctl"/>
				<Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/Vision/Basics.llb/IMAQ Create"/>
				<Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
				<Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="IMAQ Write TIFF File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write TIFF File 2"/>
				<Item Name="IMAQ Write File 2" Type="VI" URL="/&lt;vilib&gt;/Vision/Files.llb/IMAQ Write File 2"/>
				<Item Name="IMAQ Write BMP File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write BMP File 2"/>
				<Item Name="IMAQ Write Image And Vision Info File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write Image And Vision Info File 2"/>
				<Item Name="IMAQ Write JPEG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG File 2"/>
				<Item Name="IMAQ Write JPEG2000 File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG2000 File 2"/>
				<Item Name="IMAQ Write PNG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write PNG File 2"/>
				<Item Name="IMAQ Image Datatype to Image Cluster.vi" Type="VI" URL="/&lt;vilib&gt;/vision/DatatypeConversion.llb/IMAQ Image Datatype to Image Cluster.vi"/>
				<Item Name="IMAQ Image Cluster to Image Datatype.vi" Type="VI" URL="/&lt;vilib&gt;/vision/DatatypeConversion.llb/IMAQ Image Cluster to Image Datatype.vi"/>
				<Item Name="Merge Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Merge Errors.vi"/>
				<Item Name="ErrorConvert.vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/SubVIs/ErrorConvert.vi"/>
				<Item Name="FP Read (Boolean).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Boolean).vi"/>
				<Item Name="FP Read (Boolean Array).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Boolean Array).vi"/>
				<Item Name="FP Read (Float).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Float).vi"/>
				<Item Name="FP Read (Float Array).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Float Array).vi"/>
				<Item Name="FP Read (Float Array -IO).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Float Array -IO).vi"/>
				<Item Name="FP Read (Float -IO).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Float -IO).vi"/>
				<Item Name="FP Read (Boolean -IO).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Boolean -IO).vi"/>
				<Item Name="FP Read (Boolean Array -IO).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Boolean Array -IO).vi"/>
				<Item Name="FP Read (Polymorphic).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Read.llb/FP Read (Polymorphic).vi"/>
				<Item Name="FP Write (Boolean).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Boolean).vi"/>
				<Item Name="FP Write (Boolean Array).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Boolean Array).vi"/>
				<Item Name="FP Write (Float).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Float).vi"/>
				<Item Name="FP Write (Float Array).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Float Array).vi"/>
				<Item Name="FP Write (Float Array -IO).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Float Array -IO).vi"/>
				<Item Name="FP Write (Boolean -IO).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Boolean -IO).vi"/>
				<Item Name="FP Write (Boolean Array -IO).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Boolean Array -IO).vi"/>
				<Item Name="FP Write (Float -IO).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Float -IO).vi"/>
				<Item Name="FP Write (Polymorphic).vi" Type="VI" URL="/&lt;vilib&gt;/FieldPoint/Polymorphic Write.llb/FP Write (Polymorphic).vi"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="General Error Handler CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
				<Item Name="Write To Spreadsheet File (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (string).vi"/>
				<Item Name="Write To Spreadsheet File (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (I64).vi"/>
				<Item Name="Write To Spreadsheet File (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (DBL).vi"/>
				<Item Name="Write To Spreadsheet File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File.vi"/>
				<Item Name="FPLVMgr.dll" Type="Document" URL="/&lt;vilib&gt;/FieldPoint/SubVIs/FPLVMgr.dll"/>
			</Item>
			<Item Name="niimaqdx.dll" Type="Document" URL="niimaqdx.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nivissvc.dll" Type="Document" URL="nivissvc.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="makeName.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/makeName.vi"/>
			<Item Name="nivision.dll" Type="Document" URL="nivision.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="SavePicturesManual.vi" Type="VI" URL="../lib/SavePicturesManual.vi"/>
			<Item Name="MakeTheTestFolderManual.vi" Type="VI" URL="../lib/MakeTheTestFolderManual.vi"/>
			<Item Name="lvanlys.dll" Type="Document" URL="/D/Program Files/National Instruments/LabVIEW 8.6/resource/lvanlys.dll"/>
			<Item Name="AddDataPoint.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/AddDataPoint.vi"/>
			<Item Name="Integral.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/Integral.vi"/>
			<Item Name="OutputToRange.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/OutputToRange.vi"/>
			<Item Name="LineForecast.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/LineForecast.vi"/>
			<Item Name="Proportianal%toV.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/Proportianal%toV.vi"/>
			<Item Name="ProportionaAndDerivative.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/ProportionaAndDerivative.vi"/>
			<Item Name="PID.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/PID.vi"/>
			<Item Name="PreIntegral.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/PreIntegral.vi"/>
			<Item Name="SaunaInfo.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/UtilitiesForSteamController/SaunaInfo.vi"/>
			<Item Name="AppendCollectedDataToFile.vi" Type="VI" URL="../../../Documents and Settings/sauna.CAM/Desktop/controller_100504/UtilitiesForSteamController/AppendCollectedDataToFile.vi"/>
			<Item Name="imaqdx.rc" Type="Document" URL="/D/Program Files/National Instruments/LabVIEW 8.6/resource/objmgr/imaqdx.rc"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="camera" Type="RESTful WS">
				<Property Name="Bld_buildSpecName" Type="Str">camera</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Destination[0].destName" Type="Str">camera.lvws</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/camera/internal.llb</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/camera/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[0].template" Type="Str">/manualCamera/:offsetY/:offsetX/:fps/:width/:height/:testName/:packsize/:username/:index/:exposure</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[0].VIName" Type="Str">manualCamera.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[1].template" Type="Str">/camera_run</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[1].VIName" Type="Str">camera_run.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[2].template" Type="Str">/camera_stop</Property>
				<Property Name="RESTfulWebSrvc_routingTemplate[2].VIName" Type="Str">camera_stop.vi</Property>
				<Property Name="RESTfulWebSrvc_routingTemplateCount" Type="Int">3</Property>
				<Property Name="Source[0].itemID" Type="Str">{B622FB29-FFA1-499C-A088-75135D92CACF}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/lib/cameraServer.vi</Property>
				<Property Name="Source[1].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">HTML</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/serverCommands/camera_run.vi</Property>
				<Property Name="Source[2].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">HTML</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[2].type" Type="Str">RESTfulVI</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/serverCommands/camera_stop.vi</Property>
				<Property Name="Source[3].RESTfulVI.VIConfigInfoOutputFormat" Type="Str">HTML</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[3].type" Type="Str">RESTfulVI</Property>
				<Property Name="SourceCount" Type="Int">4</Property>
				<Property Name="WebSrvc_serviceGUID" Type="Str">{A456502A-750E-4265-8B89-6C8297337D7A}</Property>
				<Property Name="WebSrvc_serviceName" Type="Str">camera</Property>
			</Item>
		</Item>
	</Item>
</Project>
