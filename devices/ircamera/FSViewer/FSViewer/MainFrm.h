// MainFrm.h : interface of the CMainFrame class
//


#pragma once

#define WM_MyWriteFunc WM_APP+1
#define WM_MyConnectFunc WM_APP+2
#define WM_MyDisconnectFunc WM_APP+3
#define WM_MyAutofocusFunc WM_APP+4
#define WM_MyGetImageFunc WM_APP+5

class CMainFrame : public CFrameWnd
{
	
protected: // create from serialization only
	CMainFrame();
	DECLARE_DYNCREATE(CMainFrame)

// Attributes
public:

// Operations
public:

// Overrides
public:
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);

// Implementation
public:
	virtual ~CMainFrame();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:  // control bar embedded members
	CStatusBar  m_wndStatusBar;
	CToolBar    m_wndToolBar;

// Generated message map functions
protected:
	afx_msg int OnCreate(LPCREATESTRUCT lpCreateStruct);
	//afx_msg LRESULT SendMessageToViewer(WPARAM wParam, LPARAM lParam);
	afx_msg BOOL OnCopyData(CWnd* pWnd, COPYDATASTRUCT* pData);
	DECLARE_MESSAGE_MAP()
};


