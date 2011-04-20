// MainFrm.cpp : implementation of the CMainFrame class
//

#include "stdafx.h"
#include "FSViewer.h"

#include "MainFrm.h"

#include <string>
#include <memory>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

//static UINT WM_MYWRITE = RegisterWindowMessage(_T("YOURAPP_FIND_MSG"));
//static UINT WM_CONNECT = RegisterWindowMessage(_T("YOURAPP_FIND_MSG"));
//static UINT WM_DISCONNECT = RegisterWindowMessage(_T("YOURAPP_FIND_MSG"));
//static UINT WM_AUTOZOOM = RegisterWindowMessage(_T("YOURAPP_FIND_MSG"));
//static UINT WM_TAKEIMAGE = RegisterWindowMessage(_T("YOURAPP_FIND_MSG"));


// CMainFrame

IMPLEMENT_DYNCREATE(CMainFrame, CFrameWnd)

BEGIN_MESSAGE_MAP(CMainFrame, CFrameWnd)
	ON_WM_CREATE()
	ON_WM_COPYDATA()
	//ON_REGISTERED_MESSAGE(WM_CONNECT, SendMessageToViewer)
	//ON_REGISTERED_MESSAGE(WM_DISCONNECT, SendMessageToViewer)
END_MESSAGE_MAP()

static UINT indicators[] =
{
	ID_SEPARATOR,           // status line indicator
	ID_INDICATOR_CAPS,
	ID_INDICATOR_NUM,
	ID_INDICATOR_SCRL,
};


// CMainFrame construction/destruction

CMainFrame::CMainFrame()
{
	// TODO: add member initialization code here
}

CMainFrame::~CMainFrame()
{
}


int CMainFrame::OnCreate(LPCREATESTRUCT lpCreateStruct)
{
	if (CFrameWnd::OnCreate(lpCreateStruct) == -1)
		return -1;
	
	if (!m_wndToolBar.CreateEx(this, TBSTYLE_FLAT, WS_CHILD | WS_VISIBLE | CBRS_TOP
		| CBRS_GRIPPER | CBRS_TOOLTIPS | CBRS_FLYBY | CBRS_SIZE_DYNAMIC) ||
		!m_wndToolBar.LoadToolBar(IDR_MAINFRAME))
	{
		TRACE0("Failed to create toolbar\n");
		return -1;      // fail to create
	}

	if (!m_wndStatusBar.Create(this) ||
		!m_wndStatusBar.SetIndicators(indicators,
		  sizeof(indicators)/sizeof(UINT)))
	{
		TRACE0("Failed to create status bar\n");
		return -1;      // fail to create
	}

	// TODO: Delete these three lines if you don't want the toolbar to be dockable
	m_wndToolBar.EnableDocking(CBRS_ALIGN_ANY);
	EnableDocking(CBRS_ALIGN_ANY);
	DockControlBar(&m_wndToolBar);

	return 0;
}

BOOL CMainFrame::PreCreateWindow(CREATESTRUCT& cs)
{
	if( !CFrameWnd::PreCreateWindow(cs) )
		return FALSE;
	// TODO: Modify the Window class or styles here by modifying
	//  the CREATESTRUCT cs

	return TRUE;
}


// CMainFrame diagnostics

#ifdef _DEBUG
void CMainFrame::AssertValid() const
{
	CFrameWnd::AssertValid();
}

void CMainFrame::Dump(CDumpContext& dc) const
{
	CFrameWnd::Dump(dc);
}

#endif //_DEBUG

/*LRESULT CMainFrame::SendMessageToViewer(WPARAM wParam, LPARAM lParam)
{

	long a = 1;
	
	TRACE("CMainFrame::SendMessageToViewer message recieved\n");
	CView *pView = GetActiveView();


	
	
	switch(lParam)
	{
	case 100:

		if (pView == NULL){
			TRACE("pView == NULL\n");
		}
		else{
			pView->SendMessage(WM_MyConnectFunc);
			TRACE("CMainFrame::MyConnectFunc message sent\n");
			return 0;
		}

	case 200:

		if (pView == NULL){
			TRACE("pView == NULL\n");
		}
		else{
			pView->SendMessage(WM_MyAutofocusFunc);
			TRACE("CMainFrame::MyAutoFocusFunc message sent\n");
			return 0;
		}

	case 300:

		if (pView == NULL){
			TRACE("pView == NULL\n");
		}
		else{
			pView->SendMessage(WM_MyGetImageFunc);
			TRACE("CMainFrame::MyGetImageFunc message sent\n");
			return 0;
		}

	case 400:

		if (pView == NULL){
			TRACE("pView == NULL\n");
		}
		else{
			pView->SendMessage(WM_MyDisconnectFunc);
			TRACE("CMainFrame::MyDisconnectFunc message sent\n");
			return 0;
		}

	}
	


	if (pView == NULL){
		TRACE("pView == NULL\n");
	}
	else{
	    pView->SendMessage(WM_MyWriteFunc);
		TRACE("CMainFrame::MyWriteFunc message sent\n");
	}


	
	//std::auto_ptr<std::string> msg(reinterpret_cast<std::string*>(lParam));
	//std::string msg = reinterpret_cast<std::string*>(lParam);
	std::string *msg = (std::string*)lParam;
	//char *msg = (char*) lParam;

	TRACE("lParam: %lu\n",lParam);


	FILE* logfile = fopen("logfile.txt","a");
	fprintf(logfile,"wParam: %d, msg: %c\n",wParam,msg->c_str());
	fflush(logfile);
	//fprintf(logfile,"wParam: %d, lParam: %c\n",wParam,reinterpret_cast<std::string*>(lParam));
	fclose(logfile);

	return a;
}*/


BOOL CMainFrame::OnCopyData(CWnd* pWnd, COPYDATASTRUCT* pData) {
    
	//TRACE("OnCopyData Accessed\n");
	//std::string *msg = (std::string*)pData->lpData;
	//TRACE("CMainframe     msg: %s\n",msg->c_str());

	//int msgId = pData->dwData;
	//int msgSize = pData->cbData;
	//std::string *filename = (std::string*)pData->lpData;

	COPYDATASTRUCT data;
	//data.dwData = msgId;
	//data.cbData = msgSize;
	//data.lpData = msg;
	data.dwData = pData->dwData;
	data.cbData = pData->cbData;
	data.lpData = pData->lpData;


		
	CView *pView = GetActiveView();
	if (pView == NULL){
		TRACE("pView == NULL\n");
	}
	else{
	    pView->SendMessage(WM_COPYDATA,0,(LPARAM)&data);
		//TRACE("CMainFrame::OnCopyData message sent\n");
	}
	

	return TRUE;
}



// CMainFrame message handlers



