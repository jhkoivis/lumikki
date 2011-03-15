#include <stdio.h>
#include <windows.h>
#include <atlstr.h>
#include <iostream>
#include "JSON.h"
#include "message.h"

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

void printStatus(char* expId, char* format, const wchar_t* ip, int type, int port, int isConnected ){
	JSONObject root_out;
	wchar_t expId_t[256];
	char_to_wchar(expId_t, expId);
	wchar_t format_t[256];
	char_to_wchar(format_t, format);
			
	root_out[L"expId"] = new JSONValue(expId_t);
	root_out[L"isConnected"] = new JSONValue((double)isConnected);
	root_out[L"format"] = new JSONValue(format_t);
	root_out[L"type"] = new JSONValue((double)type);
	root_out[L"ip"] = new JSONValue(ip);
	root_out[L"port"] = new JSONValue((double)port);
	
	JSONValue *value = new JSONValue(root_out);
	std::wcout << value->Stringify().c_str() << std::endl;
}