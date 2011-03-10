/*
This closes calculator
*/

#include <Windows.h>
#include <atlstr.h>

int main (void)
{
	HWND HWnd = FindWindow(NULL, CStringW("Calculator"));
	SendMessage(HWnd, WM_CLOSE, 0, 0);

	return 0;
}
