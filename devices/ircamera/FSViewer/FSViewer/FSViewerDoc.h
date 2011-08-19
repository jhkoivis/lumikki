// FSViewerDoc.h : interface of the CFSViewerDoc class
//


#pragma once


class CFSViewerDoc : public CDocument
{
protected: // create from serialization only
	CFSViewerDoc();
	DECLARE_DYNCREATE(CFSViewerDoc)

// Attributes
public:

// Operations
public:

// Overrides
public:
	virtual BOOL OnNewDocument();
	virtual void Serialize(CArchive& ar);

// Implementation
public:
	virtual ~CFSViewerDoc();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	DECLARE_MESSAGE_MAP()
};


