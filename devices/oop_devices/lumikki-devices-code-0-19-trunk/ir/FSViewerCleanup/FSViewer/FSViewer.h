// FSViewer.h : main header file for the FSViewer application
//
#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"       // main symbols


// CFSViewerApp:
// See FSViewer.cpp for the implementation of this class
//

class CFSViewerApp : public CWinApp
{
public:
	CFSViewerApp();


// Overrides
public:
	virtual BOOL InitInstance();

// Implementation
	afx_msg void OnAppAbout();
	DECLARE_MESSAGE_MAP()
};

extern CFSViewerApp theApp;