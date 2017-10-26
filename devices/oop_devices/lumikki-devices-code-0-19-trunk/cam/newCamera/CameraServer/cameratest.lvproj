<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="8608001">
	<Property Name="varPersistentID:{90004DD0-081B-4F5C-90FD-914061AB66EC}" Type="Ref">/My Computer/camVariables.lvlib/SaunaInfo</Property>
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
		<Item Name="Camera" Type="Folder">
			<Item Name="cameratest.vi" Type="VI" URL="../cameratest.vi"/>
			<Item Name="Parse2.vi" Type="VI" URL="../lib/Parse2.vi"/>
			<Item Name="CameraSettings2.vi" Type="VI" URL="../lib/CameraSettings2.vi"/>
			<Item Name="ErrorToSatus2.vi" Type="VI" URL="../lib/ErrorToSatus2.vi"/>
			<Item Name="SavePictures2.vi" Type="VI" URL="../lib/SavePictures2.vi"/>
			<Item Name="CameraShoot32.vi" Type="VI" URL="../lib/CameraShoot32.vi"/>
		</Item>
		<Item Name="Humidity controller" Type="Folder">
			<Item Name="humiditytest.vi" Type="VI" URL="../humiditytest.vi"/>
		</Item>
		<Item Name="camVariables.lvlib" Type="Library" URL="../camVariables.lvlib"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="NI_Vision_Acquisition_Software.lvlib" Type="Library" URL="/&lt;vilib&gt;/vision/driver/NI_Vision_Acquisition_Software.lvlib"/>
				<Item Name="IMAQdx.ctl" Type="VI" URL="/&lt;vilib&gt;/userDefined/High Color/IMAQdx.ctl"/>
				<Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/Vision/Basics.llb/IMAQ Create"/>
				<Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
				<Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
				<Item Name="IMAQ Image Datatype to Image Cluster.vi" Type="VI" URL="/&lt;vilib&gt;/vision/DatatypeConversion.llb/IMAQ Image Datatype to Image Cluster.vi"/>
				<Item Name="IMAQ Image Cluster to Image Datatype.vi" Type="VI" URL="/&lt;vilib&gt;/vision/DatatypeConversion.llb/IMAQ Image Cluster to Image Datatype.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="IMAQ Write TIFF File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write TIFF File 2"/>
				<Item Name="IMAQ Write File 2" Type="VI" URL="/&lt;vilib&gt;/Vision/Files.llb/IMAQ Write File 2"/>
				<Item Name="IMAQ Write BMP File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write BMP File 2"/>
				<Item Name="IMAQ Write Image And Vision Info File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write Image And Vision Info File 2"/>
				<Item Name="IMAQ Write JPEG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG File 2"/>
				<Item Name="IMAQ Write JPEG2000 File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG2000 File 2"/>
				<Item Name="IMAQ Write PNG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write PNG File 2"/>
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
			<Item Name="TCPIP.Server2.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/TCPIP.Server2.vi"/>
			<Item Name="CheckTheMode.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/CheckTheMode.vi"/>
			<Item Name="ParseHelp.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/ParseHelp.vi"/>
			<Item Name="niimaqdx.dll" Type="Document" URL="niimaqdx.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nivissvc.dll" Type="Document" URL="nivissvc.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="ErrorToSatus.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/ErrorToSatus.vi"/>
			<Item Name="MakeTheTestFolder.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/MakeTheTestFolder.vi"/>
			<Item Name="ParseLegasyFIXME.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/ParseLegasyFIXME.vi"/>
			<Item Name="ChangeSettings.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/ChangeSettings.vi"/>
			<Item Name="CalculateFPS.vi" Type="VI" URL="/D/Program Files/National Instruments/LabVIEW 8.6/examples/IMAQ/IMAQdx Examples.llb/CalculateFPS.vi"/>
			<Item Name="SavePictures.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/SavePictures.vi"/>
			<Item Name="makeName.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Utils for camera/makeName.vi"/>
			<Item Name="nivision.dll" Type="Document" URL="nivision.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="WaitMessage2.vi" Type="VI" URL="../lib/WaitMessage2.vi"/>
			<Item Name="lvanlys.dll" Type="Document" URL="/D/Program Files/National Instruments/LabVIEW 8.6/resource/lvanlys.dll"/>
			<Item Name="AddDataPoint.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/AddDataPoint.vi"/>
			<Item Name="Integral.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/Integral.vi"/>
			<Item Name="OutputToRange.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/OutputToRange.vi"/>
			<Item Name="LineForecast.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/LineForecast.vi"/>
			<Item Name="Proportianal%toV.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/Proportianal%toV.vi"/>
			<Item Name="ProportionaAndDerivative.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/ProportionaAndDerivative.vi"/>
			<Item Name="PID.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/PID.vi"/>
			<Item Name="PreIntegral.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/Taylor/PreIntegral.vi"/>
			<Item Name="SaunaInfo.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/UtilitiesForSteamController/SaunaInfo.vi"/>
			<Item Name="AppendCollectedDataToFile.vi" Type="VI" URL="../../Documents and Settings/sauna.CAM/Desktop/controller_100504/UtilitiesForSteamController/AppendCollectedDataToFile.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
