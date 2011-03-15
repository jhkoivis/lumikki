// FSViewerView.cpp : implementation of the CFSViewerView class
//

#include "stdafx.h"
#include "FSViewer.h"

#include "camera.h"
#include "FSViewerDoc.h"
#include "FSViewerView.h"

#include <string>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

//static UINT WM_MYWRITE = RegisterWindowMessage(_T("YOURAPP_FIND_MSG"));

// CFSViewerView

IMPLEMENT_DYNCREATE(CFSViewerView, CFormView)

BEGIN_MESSAGE_MAP(CFSViewerView, CFormView)
	ON_BN_CLICKED(IDC_MYDISCONNECT, &CFSViewerView::OnBnClickedMydisconnect)
	ON_BN_CLICKED(IDC_AUTOFOCUS, &CFSViewerView::OnBnClickedAutofocus)
	ON_BN_CLICKED(IDC_GETIMAGE, &CFSViewerView::OnBnClickedGetimage)
	ON_BN_CLICKED(IDC_MYCONNECT, &CFSViewerView::OnBnClickedMyconnect)
	//ON_REGISTERED_MESSAGE(WM_MyWriteFunc, MyWriteFunc)
	ON_MESSAGE(WM_MyWriteFunc, MyWriteFunc)
    ON_MESSAGE(WM_MyConnectFunc, MyConnectFunc)
	ON_MESSAGE(WM_MyDisconnectFunc, MyDisconnectFunc)
	ON_MESSAGE(WM_MyAutofocusFunc, MyAutofocusFunc)
	ON_MESSAGE(WM_MyGetImageFunc, MyGetImageFunc)
	ON_WM_COPYDATA()
END_MESSAGE_MAP()

// CFSViewerView construction/destruction

CFSViewerView::CFSViewerView()
	: CFormView(CFSViewerView::IDD)
{
	// TODO: add construction code here
	m_hImage = NULL;
	m_pThread = NULL;
	m_bConnected = false;
}

CFSViewerView::~CFSViewerView()
{
  if (m_hImage) {
    GlobalFree(m_hImage);
    m_hImage = NULL;
  }
}

void CFSViewerView::DoDataExchange(CDataExchange* pDX)
{
	CFormView::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_LVCAMCTRL1, m_Camera);
	DDX_Control(pDX, IDC_LIST1, m_Events);
	DDX_Control(pDX, IDC_IMAGE, m_ctrlImage);
}

BOOL CFSViewerView::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: Modify the Window class or styles here by modifying
	//  the CREATESTRUCT cs

	return CFormView::PreCreateWindow(cs);
}

void CFSViewerView::OnInitialUpdate()
{
	CFormView::OnInitialUpdate();
	GetParentFrame()->RecalcLayout();
	ResizeParentToFit();

}


// CFSViewerView diagnostics

#ifdef _DEBUG
void CFSViewerView::AssertValid() const
{
	CFormView::AssertValid();
}

void CFSViewerView::Dump(CDumpContext& dc) const
{
	CFormView::Dump(dc);
}

CFSViewerDoc* CFSViewerView::GetDocument() const // non-debug version is inline
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CFSViewerDoc)));
	return (CFSViewerDoc*)m_pDocument;
}
#endif //_DEBUG


// CFSViewerView message handlers
BEGIN_EVENTSINK_MAP(CFSViewerView, CFormView)
	ON_EVENT(CFSViewerView, IDC_LVCAMCTRL1, 103, CFSViewerView::CameraEventLvcamctrl1, VTS_I4)
END_EVENTSINK_MAP()

void CFSViewerView::CameraEventLvcamctrl1(long Id)
{
	TRACE("Camera event %ld\n", Id);
	CString sEvent;

	switch (Id) 
	{
		case EV_CONNECTED:
			sEvent = _T("Connected");
			m_bConnected = true;
			//m_pThread = AfxBeginThread(GrabberProc, (LPVOID)this);
			//m_pThread->m_bAutoDelete = false;
			break;
		case EV_DISCONNECTED:
			m_bConnected = false;
			sEvent = _T("Disconnected");
			break;
		case EV_CONN_BROKEN:
			sEvent = _T("Connection broken");break;
		case EV_RECONNECTED:
			sEvent = _T("Reconnected");break;
		case EV_DISCONNECTING:
			sEvent = _T("Disconnecting...");break;
		case EV_AUTOADJUST:
			sEvent = _T("Auto adjust");break;
		case EV_RECALIB_START:
			sEvent = _T("Start of recalibration");break;
		case EV_RECALIB_STOP:
			sEvent = _T("End of recalibration");break;
		case EV_LUT_UPDATED:
			sEvent = _T("Look-up table updated");break;
		case EV_REC_UPDATED:
			sEvent = _T("Recording settings updated");break;
		case EV_IMAGE_CAPTURED:
			sEvent = _T("Image captured");break;
		case EV_INIT_COMPLETED:
			sEvent = _T("Init completed");break;
		case EV_FRAME_RATE_TABLE_AVAILABLE:
			sEvent = _T("Frame rate table available");break;
		case EV_FRAME_RATE_CHANGE_COMPLETED:
			sEvent = _T("Frame rate change completed");break;
		case EV_RANGE_TABLE_AVAILABLE:
			sEvent = _T("Temperature range table available");break;
		case EV_RANGE_CHANGE_COMPLETED:
			sEvent = _T("Temperature range change completed");break;
		case EV_IMAGE_SIZE_CHANGED:
			sEvent = _T("Image size changed");break;
		default:
			sEvent.Format(_T("Unknown event %ld"),  Id);break;
	}

	m_Events.InsertString(0, sEvent);
}

void CFSViewerView::DisplayImage(int nImageType, HGLOBAL hMem) 
{
	int w, h;
	VARIANT va;

    va = m_Camera.GetCameraProperty(PROP_IMAGE_WIDTH);
	w = (int)va.iVal;
	VariantClear(&va);
    va = m_Camera.GetCameraProperty(PROP_IMAGE_HEIGHT);
	h = (int)va.iVal;
	VariantClear(&va);

	if (m_hImage) {
		GlobalFree(m_hImage);
		m_hImage = NULL;
	}

	// Calculate size and allocate memory
	HANDLE hDIB;
	int imgSize;
	int xAlignSize = ((w + 3) & ~3);  // Must be 4 byte aligned
	imgSize  = sizeof(BITMAPINFOHEADER);
	imgSize += 256 * sizeof(RGBQUAD);
	imgSize += (xAlignSize * h);
	hDIB = GlobalAlloc(GMEM_MOVEABLE | GMEM_DISCARDABLE, imgSize);
	if (hDIB == NULL) {
		AfxMessageBox(_T("Unable to allocate memory"));
		return;
	}

	BYTE* pDIB = (BYTE*)GlobalLock(hDIB);
	BYTE* pBits = pDIB + sizeof(BITMAPINFOHEADER) + 256 * sizeof(RGBQUAD);

	// Allocate and copy image to local buffer
	VARTYPE vt = (nImageType < 2 ? VT_I2 : (nImageType < 4 ? VT_R4 : VT_UI1));
	int pixSize = (vt == VT_UI1 ? 1 : (vt == VT_I2 ? 2 : 4));

	imgSize = xAlignSize * h * pixSize;
	m_hImage = GlobalAlloc(GMEM_MOVEABLE | GMEM_DISCARDABLE, imgSize);
	if (m_hImage == NULL) {
		AfxMessageBox(_T("Unable to allocate image memory"));
		return;
	}

	BYTE* pImage = (BYTE *)GlobalLock(m_hImage);

	if (vt == VT_UI1)
	{
		BYTE *pSrc;
		pSrc = (BYTE*)GlobalLock(hMem);
		int rowsize = xAlignSize;
		for (int y = 0; y < h; y++)
			memcpy(&pImage[y * rowsize], &pSrc[y * w], rowsize);
		GlobalUnlock(hMem);
	}
	else if (vt == VT_I2)
	{
		WORD *pSrc;
		pSrc = (WORD*)GlobalLock(hMem);

		int rowsize = xAlignSize * pixSize;
		for (int y = 0; y < h; y++)
			memcpy(&pImage[y * rowsize], &pSrc[y * w], rowsize);
		GlobalUnlock(hMem);
	}
	else if (vt == VT_R4)
	{
		float *pSrc;
		pSrc = (float*)GlobalLock(hMem);
		
		int rowsize = xAlignSize * pixSize;
		for (int y = 0; y < h; y++)
			memcpy(&pImage[y * rowsize], &pSrc[y * w], rowsize);
		GlobalUnlock(hMem);
	}

	// Copy pixel data
	BYTE* pDst = pBits;
	int sz = xAlignSize * h;
	if (vt == VT_UI1)
	{
		sz = xAlignSize * h;
		BYTE* pSrc = (BYTE *)pImage;
		while (sz--) {
			*pDst++ = *pSrc++;
		}
	}
	else if (vt == VT_I2)
	{
		WORD smin = 65535, smax = 0;
		WORD* pSrc = (WORD *)pImage;
		while (sz--) {
			smin = __min(*pSrc, smin);
			smax = __max(*pSrc, smax);
			pSrc++;
		}

		sz = xAlignSize * h;
		pSrc = (WORD *)pImage;
		WORD span = smax - smin;
		if (span == 0) span = 1;
		while (sz--) {
			long sample = ((*pSrc++ - smin) * 256 / span );
			*pDst++ = (BYTE)sample;
		}
	}
	else if (vt == VT_R4)
	{
		// Temperature or object value image
		float smin = 5000.0, smax = 0.0;
		float* pSrc = (float *)pImage;
		while (sz--) {
			smin = __min(*pSrc, smin);
			smax = __max(*pSrc, smax);
			pSrc++;
		}

		sz = xAlignSize * h;
		pSrc = (float *)pImage;
		float span = smax - smin;
		if (span < 1) span = 1.0;

		while (sz--) {
			BYTE sample = (BYTE)((*pSrc++ - smin) * 256.0 / span );
			*pDst++ = sample;
		}
	}

	// Set bitmap info header
	BITMAPINFOHEADER   bihS;  // Temporary structure
	LPBITMAPINFOHEADER bitHeadP = (LPBITMAPINFOHEADER)pDIB;

	bihS.biSize          = sizeof(BITMAPINFOHEADER);
	bihS.biWidth         = w;
	// Specifies the height of the bitmap, in pixels.
	// If biHeight is positive, the bitmap is a bottom-up DIB and
	// its origin is the lower-left corner. If biHeight is negative,
	// the bitmap is a top-down DIB and its origin is the upper-left corner. 
	bihS.biHeight        = -h;
	bihS.biPlanes        = 1;
	bihS.biBitCount      = 8;
	bihS.biCompression   = BI_RGB;
	bihS.biSizeImage     = xAlignSize * h;
	bihS.biXPelsPerMeter = 0;
	bihS.biYPelsPerMeter = 0;
	bihS.biClrUsed       = 256;
	bihS.biClrImportant  = 0;
	*bitHeadP            = bihS;  // Copy struct into DIB

	// Set palette (grey scale)
	RGBQUAD *palP = (RGBQUAD*)&((LPBITMAPINFO)pDIB)->bmiColors[0];
	for (WORD i = 0; i < 256; i++) {
		palP->rgbBlue = (BYTE)i;
		palP->rgbGreen = (BYTE)i; 
		palP->rgbRed = (BYTE)i;
		palP->rgbReserved = 0;
		palP++;
	}

	CDC* dc = m_ctrlImage.GetDC();
	CRect rect;
	m_ctrlImage.GetClientRect((LPRECT)rect);

	// Set mode and draw the image
	int oldMode = SetStretchBltMode(dc->m_hDC, COLORONCOLOR);

	int ret = ::StretchDIBits(dc->m_hDC,
		rect.left, rect.top, rect.Width(), rect.Height(),
		0, 0, w, h, pBits, (LPBITMAPINFO)pDIB, DIB_RGB_COLORS, SRCCOPY);

	SetStretchBltMode(dc->m_hDC, oldMode); // Restore mode

	GlobalUnlock(m_hImage);
	GlobalUnlock(hDIB);
	GlobalFree(hDIB);
}

int CFSViewerView::ShowImage(int nImageType) 
{
	COleVariant va;
	HGLOBAL h;

	// The camera control uses GlobalAlloc for image allocation if the image
	// type is 20-23. No risk for memory leakage.
	va = m_Camera.GetImage(20 + nImageType);

	if (va.vt == VT_I2) { // Error
		VariantClear(&va);
		return (int)va.iVal;
	}
	else if (va.vt != VT_I4) {
		VariantClear(&va);
		return -1;
	}

	h = (HGLOBAL)(va.lVal);

	DisplayImage(nImageType, h);

	// Free memory
	GlobalFree(h);
	VariantClear(&va);

	return 0;
}

//Thread used to display images
UINT CFSViewerView::GrabberProc(LPVOID pParam)
{
	CFSViewerView* pView = (CFSViewerView*)pParam;

	while (pView->IsConnected()) 
	{
		if (pView->ShowImage(3) != 0) {
			Sleep(500);
		}
	}

	return 0;
}

void CFSViewerView::OnBnClickedMyconnect()
{
	short status;
	status = m_Camera.Connect(12,0,8,4,_T("192.168.1.2"));	
}

void CFSViewerView::OnBnClickedMydisconnect()
{
	m_Camera.Disconnect();
	
}

void CFSViewerView::OnBnClickedAutofocus()
{
	m_Camera.DoCameraAction(12);
	
}

void CFSViewerView::OnBnClickedGetimage()
{
	VARIANT image;
	int pictureok = -1;

	while(pictureok == -1){

		image = m_Camera.GetImage(20+3);
		Sleep(500);
		if (image.vt == VT_I2) { // Error
			pictureok = -1;
			TRACE("Error in picture taking: %d",image.iVal);
		}
		else if (image.vt != VT_I4) {
			pictureok = -1;
			TRACE("image.vt != VT_I4");
		}
		else{
			pictureok = 0;
			TRACE("OK");
		}
	}
	
	HGLOBAL h;
	h = (HGLOBAL)(image.lVal);
	MyDisplayImage(20,h,NULL);
	
}


void CFSViewerView::MyDisplayImage(int nImageType, HGLOBAL hMem, HBITMAP* hBmp) 
{
	int w, h;
	VARIANT va;
	HANDLE m_hImage = NULL;

    va = m_Camera.GetCameraProperty(PROP_IMAGE_WIDTH);
	w = (int)va.iVal;
	VariantClear(&va);
    va = m_Camera.GetCameraProperty(PROP_IMAGE_HEIGHT);
	h = (int)va.iVal;
	VariantClear(&va);

	if (m_hImage) {
		GlobalFree(m_hImage);
		m_hImage = NULL;
	}

	// Calculate size and allocate memory
	HANDLE hDIB;
	int imgSize;
	int xAlignSize = ((w + 3) & ~3);  // Must be 4 byte aligned
	imgSize  = sizeof(BITMAPINFOHEADER);
	imgSize += 256 * sizeof(RGBQUAD);
	imgSize += (xAlignSize * h);

	FILE* imagefile;
	imagefile = fopen("image.dat","w");
	//fprintf(imagefile,"size: %d\n",imgSize);

	int rowsize = xAlignSize;
	int *pSrc;
	pSrc = (int*)GlobalLock(hMem);
		
	for(int i=0; i<imgSize; i++){
		fprintf(imagefile,"%d\n",pSrc[i]);
	}
		

	GlobalUnlock(hMem);
		
	fclose(imagefile);
		
}

LRESULT CFSViewerView::MyWriteFunc(WPARAM wParam, LPARAM lParam)
{
	long a = 1;

	TRACE("CFSViewerView::MyWriteFunc message recieved");
    
	FILE* msgwrite = fopen("msgwrite.txt","a");
	fprintf(msgwrite,"MyWriteFunc wrote data\n");
	fclose(msgwrite);


	return a;
}

LRESULT CFSViewerView::MyConnectFunc(WPARAM wParam, LPARAM lParam)
{
	long a = 1;

	TRACE("CFSViewerView::MyConnectFunc message recieved\n");
    short status;
	status = m_Camera.Connect(12,0,8,4,_T("192.168.1.2"));

	FILE* msgwrite = fopen("msgwrite.txt","a");
	fprintf(msgwrite,"MyConnectFunc wrote data\n");
	fclose(msgwrite);

	return a;
}

LRESULT CFSViewerView::MyDisconnectFunc(WPARAM wParam, LPARAM lParam)
{
	long a = 1;

	TRACE("CFSViewerView::MyDisconnectFunc message recieved");
    m_Camera.Disconnect();

	FILE* msgwrite = fopen("msgwrite.txt","a");
	fprintf(msgwrite,"MyDisconnectFunc wrote data\n");
	fclose(msgwrite);


	return a;
}

LRESULT CFSViewerView::MyAutofocusFunc(WPARAM wParam, LPARAM lParam)
{
	long a = 1;

	TRACE("CFSViewerView::MyAutoFunc message recieved");
    m_Camera.DoCameraAction(12);


	return a;
}

LRESULT CFSViewerView::MyGetImageFunc(WPARAM wParam, LPARAM lParam){

	long a = 1;

	VARIANT image;
	int pictureok = -1;

	while(pictureok == -1){

		image = m_Camera.GetImage(20+3);
		Sleep(500);
		if (image.vt == VT_I2) { // Error
			pictureok = -1;
			TRACE("Error in picture taking: %d",image.iVal);
		}
		else if (image.vt != VT_I4) {
			pictureok = -1;
			TRACE("image.vt != VT_I4");
		}
		else{
			pictureok = 0;
			TRACE("OK");
		}
	}
	
	HGLOBAL h;
	h = (HGLOBAL)(image.lVal);
	MyDisplayImage(20,h,NULL);

	return a;

}

void CFSViewerView::MyGetImageFunc2(char* filename){

	VARIANT image;
	int pictureok = -1;

	while(pictureok == -1){

		image = m_Camera.GetImage(20+3);
		Sleep(500);
		if (image.vt == VT_I2) { // Error
			pictureok = -1;
			TRACE("Error in picture taking: %d",image.iVal);
		}
		else if (image.vt != VT_I4) {
			pictureok = -1;
			TRACE("image.vt != VT_I4");
		}
		else{
			pictureok = 0;
			TRACE("PictureOK\n");
		}
	}
	
	HGLOBAL h;
	h = (HGLOBAL)(image.lVal);
	MyDisplayImage2(20,h,NULL,filename);
}



BOOL CFSViewerView::OnCopyData(CWnd* pWnd, COPYDATASTRUCT* pData) {
    

	//TRACE("OnCopyData Accessed\n");
	std::string *msg = (std::string*)pData->lpData;
	//TRACE("CFSViewerView       msg: %s\n",msg->c_str());

	int msgId = pData->dwData;
	int msgSize = pData->cbData;
	char *filename = (char*)pData->lpData;
	TRACE("message: %s\n",filename);
	
	
	
	TRACE("command: %d     filename: %s\n",msgId,filename);

	switch (msgId){
		case 100:
			short status;
			status = m_Camera.Connect(12,0,8,4,_T("192.168.1.2"));
			TRACE("m_Camera.Connect(12,0,8,4,_T(192.168.1.2)\n");
			break;
		case 200:
			m_Camera.Disconnect();
			TRACE("m_Camera.Disconnect()\n");
			break;
		case 300:
			if (m_bConnected == true){}
			TRACE("connected: %d\n",m_bConnected);
			break;
		case 400:
			m_Camera.DoCameraAction(12);
			TRACE("m_Camera.DoCameraAction(12)\n");
			return 0;
		case 500:
			CFSViewerView::MyGetImageFunc2(filename);
			TRACE("CFSViewerView::MyGetImageFunc2(filename)\n");
			return 0;
	}


	//TRACE("msgID: %d   msgSize: %d    filename: %s\n",msgId, msgSize, filename->c_str());

	

	return TRUE;
}

void CFSViewerView::MyDisplayImage2(int nImageType, HGLOBAL hMem, HBITMAP* hBmp, char* filename) 
{
	int w, h;
	VARIANT va;
	HANDLE m_hImage = NULL;

    va = m_Camera.GetCameraProperty(PROP_IMAGE_WIDTH);
	w = (int)va.iVal;
	VariantClear(&va);
    va = m_Camera.GetCameraProperty(PROP_IMAGE_HEIGHT);
	h = (int)va.iVal;
	VariantClear(&va);

	if (m_hImage) {
		GlobalFree(m_hImage);
		m_hImage = NULL;
	}

	// Calculate size and allocate memory
	HANDLE hDIB;
	int imgSize;
	int xAlignSize = ((w + 3) & ~3);  // Must be 4 byte aligned
	imgSize  = sizeof(BITMAPINFOHEADER);
	imgSize += 256 * sizeof(RGBQUAD);
	imgSize += (xAlignSize * h);

	FILE *imagefile = fopen(filename,"w");

	//fprintf(imagefile,"size: %d\n",imgSize);

	int rowsize = xAlignSize;
	int *pSrc;
	pSrc = (int*)GlobalLock(hMem);
		
	for(int i=0; i<imgSize; i++){
		fprintf(imagefile,"%d\n",pSrc[i]);
	}
	TRACE("MyDisplayImage2 printed file\n");
		

	GlobalUnlock(hMem);
		
	fclose(imagefile);
		
}