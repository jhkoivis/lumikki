#include <stdio.h>
#include <windows.h>
#include <atlstr.h>
#include <iostream>
#include "JSON.h"
#include "message.h"

int main(void){

	HWND pView;
	pView = FindWindow(NULL, CStringW("Untitled - FSViewer"));

	char readline[MAX_LENGTH];
	char filename[256];
	char expId[256];
	char format[256];
	int nImage = 1;
	int isConnected = 0;
	int type = 0;
	int port = 0;
	const wchar_t* ip = L"100.101.102.103";
	sprintf(format,".Raw");
	sprintf(expId,"test");
	sprintf(filename,"test");

	//while(1){
		
	//FILE *testFile = fopen("c:/tmp/log.txt", "a");

		int i=0;
		while((readline[i] = fgetc(stdin)) != EOF){
			//fprintf(testFile,"%c", readline[i]);
			//fflush(testFile);
			i++;
			if (i >= (MAX_LENGTH - 1)) break;       
		}
		//fclose(testFile);

		readline[i] = '\0';
		i = 0;

		//std::cin.getline(readline,256);
		wchar_t readline_t[MAX_LENGTH];
		char_to_wchar(readline_t, readline);
		std::wcout << readline_t << std::endl;
	
		// Parse JSON
		JSONValue *value = JSON::Parse(readline_t);
		if(value == NULL){
			//continue;			
		}

		JSONObject root;
		root = value->AsObject();
		
		if (root.find(L"expId") != root.end() && root[L"expId"]->IsString()){
			const wchar_t* found_text = root[L"expId"]->AsString().c_str();
			//wchar_t expId_t[256];
			//wchar_to_char(expId, expId_t);
			size_t origsize = wcslen(found_text) + 1;
			size_t convertedChars = 0;
			wcstombs_s(&convertedChars, expId, origsize, root[L"expId"]->AsString().c_str(), _TRUNCATE);
			//printf("expId: %s\n",expId);
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if(root.find(L"connect") != root.end() && root[L"connect"]->IsNumber()){
			//printf("connect\n");
			SendConnect(pView);
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if(root.find(L"disconnect") != root.end() && root[L"disconnect"]->IsNumber()){
			//printf("disconnect\n");
			SendDisconnect(pView);
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if (root.find(L"getImage") != root.end() && root[L"getImage"]->IsNumber()){
			sprintf(filename,"%s%d%s",expId,nImage,format);
			nImage++;
			//printf("new filename: %s\n",filename);
			SendGetImage(pView, filename);
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if (root.find(L"getImageSeries") != root.end() && root[L"getImageSeries"]->IsNumber()){
			int imagesToTake = root[L"getImageSeries"]->AsNumber();
			for(int i=0; i<imagesToTake; i++){
				sprintf(filename,"%s%d%s",expId,nImage,format);
				nImage++;
				//printf("new filename: %s\n",filename);
				SendGetImage(pView, filename);
				Sleep(1000);
			}
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if(root.find(L"focus") != root.end() && root[L"focus"]->IsNumber()){
			//printf("focus\n");
			SendAutofocus(pView);
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if(root.find(L"isConnected") != root.end() && root[L"isConnected"]->IsNumber()){
			//JSONObject root_out;
			//double number = 1;
			//root_out[L"isConnected"] = new JSONValue(number);
			//JSONValue *value = new JSONValue(root_out);
			//std::wcout << value->Stringify().c_str() << std::endl;
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if(root.find(L"status") != root.end() && root[L"status"]->IsNumber()){
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
		if(root.find(L"ip") != root.end() && root[L"ip"]->IsString()){
			ip = root[L"ip"]->AsString().c_str();
			//printStatus(expId, format, ip, type, port, isConnected);
			//std::wcout << root[L"ip"]->AsString() << std::endl;
			//std::wcout << ip << std::endl;
			//ip = root[L"ip"]->AsString().c_str();
			//const wchar_t* found_text = root[L"ip"]->AsString().c_str();
			//size_t origsize = wcslen(found_text) + 1;
			//size_t convertedChars = 0;
			//wcstombs_s(&convertedChars, ip, origsize, root[L"expId"]->AsString().c_str(), _TRUNCATE);
		}
		if(root.find(L"format") != root.end() && root[L"format"]->IsString()){
			const wchar_t* found_text = root[L"format"]->AsString().c_str();
			size_t origsize = wcslen(found_text) + 1;
			size_t convertedChars = 0;
			wcstombs_s(&convertedChars, format, origsize, root[L"format"]->AsString().c_str(), _TRUNCATE);
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if(root.find(L"type") != root.end() && root[L"type"]->IsNumber()){
			type = root[L"type"]->AsNumber();
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		if(root.find(L"port") != root.end() && root[L"port"]->IsNumber()){
			port = root[L"port"]->AsNumber();
			//printStatus(expId, format, ip, type, port, isConnected);
		}
		fprintf(stdout, "Content Type: application/javascript\n\n");
		printStatus(expId, format, ip, type, port, isConnected);
		
	//}

	

return 0;
}