#define CONNECT 100
#define DISCONNECT 200
#define ISCONNECTED 300
#define AUTOFOCUS 400
#define GETIMAGE 500

#define MAX_LENGTH 1000

void SendConnect(HWND pView);
void SendDisconnect(HWND pView);
void SendIsConnected(HWND pView);
void SendAutofocus(HWND pView);
void SendGetImage(HWND pView, char *filename);
void char_to_wchar(wchar_t* wide, char* normal);
void wchar_to_char(char* normal, wchar_t* wide);
void printStatus(char* expId, char* format, const wchar_t* ip, int type, int port, int isConnected);