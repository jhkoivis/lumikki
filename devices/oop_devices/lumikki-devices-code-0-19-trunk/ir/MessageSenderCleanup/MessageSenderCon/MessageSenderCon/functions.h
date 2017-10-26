void SendConnect(HWND pView);
void SendDisconnect(HWND pView);
void SendIsConnected(HWND pView);
void SendAutofocus(HWND pView);
void SendGetImage(HWND pView, char *filename);
void SendGetImageSeries(HWND pView);
void SendFramerate(HWND pView, double framerate);
void SendFilename(HWND pView, char* filename);
void SendStopRecording(HWND pView);
void SendPath(HWND pView, char* path);
void SendStoreCondition(HWND pView, short storeCondition);
void SendStopCondition(HWND pView, short stopCondition);
void SendStartCondition(HWND pView, short startCondition);
void SendStartValue(HWND pView, double startValue);
void SendStopValue(HWND pView, double stopValue);
void SendStoreValue(HWND pView, double storeValue);
void SendRecordFormat(HWND pView, short recordFormat);
void SendRecordConditions(HWND pView);
void SendSimulateTrigger(HWND pView);
void SendTriggerSource(HWND pView, short triggerSource);
void SendAutoShutter(HWND pView, short autoShutter);
void SendImageCorrection(HWND pView, short imageCorrection);
void SendEnableRecording(HWND pView);
void char_to_wchar(wchar_t* wide, char* normal);
void wchar_to_char(char* normal, wchar_t* wide);
void printStatus(int status);
void SendStatusQuery(HWND pView, short propertyId);
HANDLE CreatePipe();
int ReadPipe(HANDLE npipe);

//#define BUFSIZE 1024
//#define PIPE_TIMEOUT 5000