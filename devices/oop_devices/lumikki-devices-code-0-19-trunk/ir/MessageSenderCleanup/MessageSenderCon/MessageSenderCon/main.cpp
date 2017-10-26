#include <stdio.h>
#include <windows.h>
#include <atlstr.h>
#include <iostream>
#include <time.h>
#include "JSON.h"
#include "C:\\Users\\sauna\\Desktop\\FSViewerCleanup\\FSViewer\\message.h"
#include "functions.h"
#include "receive.h"

#define TIMEOUT 5.0

int main(void){
	HWND pView;
	pView = FindWindow(NULL, CStringW("Untitled - FSViewer"));
	
	char readline[MAX_LENGTH];
	char filename[MAX_LENGTH];
	char expId[MAX_LENGTH];

	double framerate;
	double recordTime;
	
	HANDLE npipe;
	int status;
			
	int i=0;
	while((readline[i] = fgetc(stdin)) != EOF){
		i++;
		if (i >= (MAX_LENGTH - 1)) break;       
	}
	readline[i] = '\0';
	
	wchar_t readline_t[MAX_LENGTH];
	char_to_wchar(readline_t, readline);
	std::wcout << readline_t << std::endl;
	
	// Parse JSON
	JSONValue *value = JSON::Parse(readline_t);
	JSONObject root_out;

	//Default status = 240
	status = 240;
	
	if(value != NULL){

		JSONObject root;
		root = value->AsObject();

		if (root.find(L"expId") != root.end() && root[L"expId"]->IsString()){
			const wchar_t* found_text = root[L"expId"]->AsString().c_str();
			size_t origsize = wcslen(found_text) + 1;
			size_t convertedChars = 0;
			wcstombs_s(&convertedChars, expId, origsize, root[L"expId"]->AsString().c_str(), _TRUNCATE);
		}
		if(root.find(L"connect") != root.end() && root[L"connect"]->IsNumber()){
			npipe = CreatePipe();
			SendConnect(pView);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"disconnect") != root.end() && root[L"disconnect"]->IsNumber()){
			npipe = CreatePipe();
			SendDisconnect(pView);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if (root.find(L"getImage") != root.end() && root[L"getImage"]->IsNumber()){
			npipe = CreatePipe();
			SendGetImage(pView, filename);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if (root.find(L"getImageSeries") != root.end() && root[L"getImageSeries"]->IsNumber()){
			npipe = CreatePipe();
			SendGetImageSeries(pView);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"focus") != root.end() && root[L"focus"]->IsNumber()){
			npipe = CreatePipe();
			SendAutofocus(pView);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"framerate") != root.end() && root[L"framerate"]->IsNumber()){
			framerate = root[L"framerate"]->AsNumber();
			npipe = CreatePipe();
			SendFramerate(pView,framerate);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
			root_out[L"framerate"] = new JSONValue((double) status);
		}
		if(root.find(L"filename") != root.end() && root[L"filename"]->IsString()){
			const wchar_t* found_text = root[L"filename"]->AsString().c_str();
			size_t origsize = wcslen(found_text) + 1;
			size_t convertedChars = 0;
			wcstombs_s(&convertedChars, filename, origsize, root[L"filename"]->AsString().c_str(), _TRUNCATE);
			npipe = CreatePipe();
			SendFilename(pView, filename);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"stopRecording") != root.end() && root[L"stopRecording"]->IsNumber()){
			npipe = CreatePipe();
			SendStopRecording(pView);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"path") != root.end() && root[L"path"]->IsString()){
			const wchar_t* found_text = root[L"path"]->AsString().c_str();
			size_t origsize = wcslen(found_text) + 1;
			size_t convertedChars = 0;
			char path[1000];
			wcstombs_s(&convertedChars, path, origsize, root[L"path"]->AsString().c_str(), _TRUNCATE);
			npipe = CreatePipe();
			SendPath(pView, path);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"storeCondition") != root.end() && root[L"storeCondition"]->IsNumber()){
			short storeCondition = (short)root[L"storeCondition"]->AsNumber();
			npipe = CreatePipe();
			SendStoreCondition(pView, storeCondition);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"stopCondition") != root.end() && root[L"stopCondition"]->IsNumber()){
			short stopCondition = (short)root[L"stopCondition"]->AsNumber();
			npipe = CreatePipe();
			SendStopCondition(pView, stopCondition);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"startCondition") != root.end() && root[L"startCondition"]->IsNumber()){
			short startCondition = (short)root[L"startCondition"]->AsNumber();
			npipe = CreatePipe();
			SendStartCondition(pView, startCondition);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"startValue") != root.end() && root[L"startValue"]->IsNumber()){
			double startValue= root[L"startValue"]->AsNumber();
			npipe = CreatePipe();
			SendStartValue(pView, startValue);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"stopValue") != root.end() && root[L"stopValue"]->IsNumber()){
			recordTime = root[L"stopValue"]->AsNumber();
			npipe = CreatePipe();
			SendStopValue(pView,recordTime);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
			root_out[L"stopValue"] = new JSONValue((double) status);
		}
		if(root.find(L"storeValue") != root.end() && root[L"storeValue"]->IsNumber()){
			double storeValue = root[L"storeValue"]->AsNumber();
			npipe = CreatePipe();
			SendStoreValue(pView, storeValue);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"recordFormat") != root.end() && root[L"recordFormat"]->IsNumber()){
			short recordFormat = (short)root[L"recordFormat"]->AsNumber();
			npipe = CreatePipe();
			SendRecordFormat(pView, recordFormat);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"recordConditions") != root.end() && root[L"recordConditions"]->IsNumber()){
			npipe = CreatePipe();
			SendRecordConditions(pView);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"status") != root.end() && root[L"status"]->IsNumber()){
			short propertyId = (short)root[L"status"]->AsNumber();
			npipe = CreatePipe();
			SendStatusQuery(pView, propertyId);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"simulateTrigger") != root.end() && root[L"simulateTrigger"]->IsNumber()){
			std::wcout << "Simulate Trigger\n" << std::endl;
			npipe = CreatePipe();
			SendSimulateTrigger(pView);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"triggerSource") != root.end() && root[L"triggerSource"]->IsNumber()){
			short triggerSource = (short)root[L"triggerSource"]->AsNumber();
			npipe = CreatePipe();
			SendTriggerSource(pView, triggerSource);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"autoShutter") != root.end() && root[L"autoShutter"]->IsNumber()){
			short autoShutter = (short)root[L"autoShutter"]->AsNumber();
			npipe = CreatePipe();
			SendAutoShutter(pView, autoShutter);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"imageCorrection") != root.end() && root[L"imageCorrection"]->IsNumber()){
			short imageCorrection = (short)root[L"imageCorrection"]->AsNumber();
			std::wcout << "Image Correction: " << imageCorrection << std::endl;
			npipe = CreatePipe();
			SendImageCorrection(pView, imageCorrection);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"enableRecording") != root.end() && root[L"enableRecording"]->IsNumber()){
			npipe = CreatePipe();
			SendEnableRecording(pView);
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
		if(root.find(L"startRecording") != root.end() && root[L"startRecording"]->IsNumber()){
			short recordMode = (short)root[L"startRecording"]->AsNumber();
			npipe = CreatePipe();
			if(recordMode == 0){
				SendGetImageSeries(pView);
			}
			else if(recordMode == 1){
				SendEnableRecording(pView);
			}
			status = ReadPipe(npipe);
			DisconnectNamedPipe(npipe);
		}
	
	}
	JSONValue *value_out = new JSONValue(root_out);
	std::wcout << value_out->Stringify().c_str() << std::endl;
	fprintf(stdout, "Content Type: application/javascript\n\n");
	printStatus(status);
	DisconnectNamedPipe(npipe);
	

	return 0;
}
