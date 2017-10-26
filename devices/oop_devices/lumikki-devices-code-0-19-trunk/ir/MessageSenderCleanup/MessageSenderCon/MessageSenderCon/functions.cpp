#include <stdio.h>
#include <windows.h>
#include <atlstr.h>
#include <iostream>
#include <string.h>
#include <time.h>
#include "JSON.h"
#include "C:\\Users\\sauna\\Desktop\\FSViewerCleanup\\FSViewer\\message.h"

#define TIMEOUT 5.0

void SendConnect(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = CONNECT;
	data.cbData = sizeof(filename);
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendDisconnect(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = DISCONNECT;
	data.cbData = sizeof(filename);
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendIsConnected(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = ISCONNECTED;
	data.cbData = sizeof(filename);
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendAutofocus(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = AUTOFOCUS;
	data.cbData = sizeof(filename);
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendGetImage(HWND pView, char *filename){
	COPYDATASTRUCT data;
	data.dwData = GETIMAGE;
	data.cbData = strlen(filename) + 1;
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendGetImageSeries(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = GETIMAGESERIES;
	data.cbData = strlen(filename) + 1;
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendFilename(HWND pView, char* filename){
	COPYDATASTRUCT data;
	data.dwData = SETFILENAME;
	data.cbData = strlen(filename) + 1;
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void char_to_wchar(wchar_t* wide, char* normal){
	size_t origsize = strlen(normal) + 1;
	size_t convertedChars = 0;
	mbstowcs_s(&convertedChars, wide, origsize, normal, _TRUNCATE);
}

void wchar_to_char(char* normal, wchar_t* wide){
	size_t origsize = wcslen(wide) + 1;
	size_t convertedChars = 0;
	wcstombs_s(&convertedChars, normal, origsize, wide, _TRUNCATE);
}

void printStatus(int status ){
	JSONObject root_out;
	root_out[L"status"] = new JSONValue((double) status);
	JSONValue *value = new JSONValue(root_out);
	std::wcout << value->Stringify().c_str() << std::endl;
}

void SendFramerate(HWND pView,double framerate){
	double *frPtr = &framerate;
	COPYDATASTRUCT data;
	data.dwData = SETFRAMERATE;
	data.cbData = sizeof(framerate);
	data.lpData = frPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendStopRecording(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = STOPRECORDING;
	data.cbData = sizeof(filename);
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendPath(HWND pView, char* path){
	COPYDATASTRUCT data;
	data.dwData = SETPATH;
	data.cbData = strlen(path) + 1;
	data.lpData = path;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendStoreCondition(HWND pView, short storeCondition){
	short *scPtr = &storeCondition;
	COPYDATASTRUCT data;
	data.dwData = SETSTORECONDITION;
	data.cbData = sizeof(storeCondition);
	data.lpData = scPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}


void SendStopCondition(HWND pView, short stopCondition){
	short *scPtr = &stopCondition;
	COPYDATASTRUCT data;
	data.dwData = SETSTOPCONDITION;
	data.cbData = sizeof(stopCondition);
	data.lpData = scPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendStartCondition(HWND pView, short startCondition){
	short *scPtr = &startCondition;
	COPYDATASTRUCT data;
	data.dwData = SETSTARTCONDITION;
	data.cbData = sizeof(startCondition);
	data.lpData = scPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendStartValue(HWND pView, double startValue){
	double *svPtr = &startValue;
	COPYDATASTRUCT data;
	data.dwData = SETSTARTVALUE;
	data.cbData = sizeof(startValue);
	data.lpData = svPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendStopValue(HWND pView, double stopValue){
	double *svPtr = &stopValue;
	COPYDATASTRUCT data;
	data.dwData = SETSTOPVALUE;
	data.cbData = sizeof(stopValue);
	data.lpData = svPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendStoreValue(HWND pView, double storeValue){
	double *svPtr = &storeValue;
	COPYDATASTRUCT data;
	data.dwData = SETSTOREVALUE;
	data.cbData = sizeof(storeValue);
	data.lpData = svPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendRecordFormat(HWND pView, short recordFormat){
	short *rfPtr = &recordFormat;
	COPYDATASTRUCT data;
	data.dwData = SETRECORDFORMAT;
	data.cbData = sizeof(recordFormat);
	data.lpData = rfPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendRecordConditions(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = PRINTRECORDCONDITIONS;
	data.cbData = sizeof(filename);
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendStatusQuery(HWND pView, short propertyId){
	statusQueryStruct stat;
	stat.propertyId = propertyId;
	COPYDATASTRUCT data;
	data.dwData = STATUSQUERY;
	data.cbData = sizeof(stat);
	data.lpData = &stat;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendSimulateTrigger(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = SIMULATETRIGGER;
	data.cbData = sizeof(filename);
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendTriggerSource(HWND pView, short triggerSource){
	short *tsPtr = &triggerSource;
	COPYDATASTRUCT data;
	data.dwData = SETTRIGGERSOURCE;
	data.cbData = sizeof(triggerSource);
	data.lpData = tsPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendAutoShutter(HWND pView, short autoShutter){
	short *asPtr = &autoShutter;
	COPYDATASTRUCT data;
	data.dwData = SETAUTOSHUTTER;
	data.cbData = sizeof(autoShutter);
	data.lpData = asPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendImageCorrection(HWND pView, short imageCorrection){
	short *icPtr = &imageCorrection;
	COPYDATASTRUCT data;
	data.dwData = SETIMAGECORRECTION;
	data.cbData = sizeof(imageCorrection);
	data.lpData = icPtr;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}

void SendEnableRecording(HWND pView){
	char *filename = "filename";
	COPYDATASTRUCT data;
	data.dwData = ENABLERECORDING;
	data.cbData = sizeof(filename);
	data.lpData = filename;
	SendMessage(pView,WM_COPYDATA,0,(LPARAM)&data);
}



HANDLE CreatePipe(){
	HANDLE npipe;
	npipe = CreateNamedPipe(PIPENAME,
							PIPE_ACCESS_DUPLEX,
							PIPE_TYPE_MESSAGE | PIPE_WAIT,  
							PIPE_UNLIMITED_INSTANCES ,
							sizeof(stat),
							sizeof(stat),
							50000,
							NULL);
	if( npipe == NULL ){
		printf("Error: cannot create named pipe\n");
	}
	else{
		printf("Named pipe created\n");
	}

	return npipe;
}

int ReadPipe(HANDLE npipe){
	int status;

	statusQueryStruct stat;
	DWORD bread;

	double tstart, ttime;
	tstart = (double)clock()/CLOCKS_PER_SEC;
	ttime = 0;
	int readSuccess = 0;

	while(!readSuccess &&  ttime < TIMEOUT ){
		readSuccess = ReadFile(npipe, &stat, sizeof(stat), &bread, NULL);
		ttime = (double) clock()/CLOCKS_PER_SEC - tstart;
	}

	if(readSuccess){
		status = stat.status;
		printf("status: %d\n", status);
	}
	else{
		status = 240;
		printf("status: %d\n", status);
	}

	return status;
}


	
