// FSViewerDoc.cpp : implementation of the CFSViewerDoc class
//

#include "stdafx.h"
#include "FSViewer.h"

#include "FSViewerDoc.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CFSViewerDoc

IMPLEMENT_DYNCREATE(CFSViewerDoc, CDocument)

BEGIN_MESSAGE_MAP(CFSViewerDoc, CDocument)
END_MESSAGE_MAP()


// CFSViewerDoc construction/destruction

CFSViewerDoc::CFSViewerDoc()
{
	// TODO: add one-time construction code here

}

CFSViewerDoc::~CFSViewerDoc()
{
}

BOOL CFSViewerDoc::OnNewDocument()
{
	if (!CDocument::OnNewDocument())
		return FALSE;

	// TODO: add reinitialization code here
	// (SDI documents will reuse this document)

	return TRUE;
}




// CFSViewerDoc serialization

void CFSViewerDoc::Serialize(CArchive& ar)
{
	if (ar.IsStoring())
	{
		// TODO: add storing code here
	}
	else
	{
		// TODO: add loading code here
	}
}


// CFSViewerDoc diagnostics

#ifdef _DEBUG
void CFSViewerDoc::AssertValid() const
{
	CDocument::AssertValid();
}

void CFSViewerDoc::Dump(CDumpContext& dc) const
{
	CDocument::Dump(dc);
}
#endif //_DEBUG


// CFSViewerDoc commands
