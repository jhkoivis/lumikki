// FSViewerView.h : interface of the CFSViewerView class
//


#pragma once

#include "lvcamctrl1.h"
#include "afxwin.h"

class CFSViewerView : public CFormView
{
protected: // create from serialization only
	CFSViewerView();
	DECLARE_DYNCREATE(CFSViewerView)

public:
	enum{ IDD = IDD_FSVIEWER_FORM };

// Attributes
public:
	CFSViewerDoc* GetDocument() const;
	HANDLE  m_hImage;
	CWinThread* m_pThread;
	bool m_bConnected;

// Operations
public:
	void DisplayImage(int nImageType, HGLOBAL hMem);
    static UINT GrabberProc( LPVOID pParam );  //This is the image grabber thread
	bool IsConnected() { return m_bConnected; }
	int  ShowImage(int nImageType);

// Overrides
public:
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	virtual void OnInitialUpdate(); // called first time after construct

// Implementation
public:
	virtual ~CFSViewerView();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	DECLARE_MESSAGE_MAP()
public:
	CLvcamctrl1 m_Camera;
	CListBox m_Events;
	DECLARE_EVENTSINK_MAP()
	void CameraEventLvcamctrl1(long Id);
	CStatic m_ctrlImage;
	void MyDisplayImage(int nImageType, HGLOBAL hMem, HBITMAP* hBmp, char* filename);
	void MyGetImageFunc(char* filename);
	void ListFrameRates();
	void ShowRecordingProperties();
	short SetFilename(char* filename);
	short SetPath(char* path);
	int GetStatus();
	void Reply(short propertyId, int status);
	afx_msg BOOL OnCopyData(CWnd* pWnd, COPYDATASTRUCT* pData);
};

#ifndef _DEBUG  // debug version in FSViewerView.cpp
inline CFSViewerDoc* CFSViewerView::GetDocument() const
   { return reinterpret_cast<CFSViewerDoc*>(m_pDocument); }
#endif

