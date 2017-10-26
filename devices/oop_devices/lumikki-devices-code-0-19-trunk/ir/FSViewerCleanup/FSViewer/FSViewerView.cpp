// FSViewerView.cpp : implementation of the CFSViewerView class
//

#include "stdafx.h"
#include "FSViewer.h"

#include "camera.h"
#include "FSViewerDoc.h"
#include "FSViewerView.h"
#include "message.h"

#include <time.h>
#include <comdef.h>
#include <string>
#include <iostream>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

// CFSViewerView

IMPLEMENT_DYNCREATE(CFSViewerView, CFormView)

BEGIN_MESSAGE_MAP(CFSViewerView, CFormView)
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



void CFSViewerView::MyGetImageFunc(char* filename){

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
	MyDisplayImage(20,h,NULL,filename);
}




BOOL CFSViewerView::OnCopyData(CWnd* pWnd, COPYDATASTRUCT* pData) {
   
	int msgId = (int)pData->dwData;
	int msgSize = (int)pData->cbData;
	// Status code returned by camera
	short statusCode = -1;
	// Status returned to message sender
	int status = 0;
		
	switch (msgId){
		case CONNECT:
		{
			statusCode = m_Camera.Connect(12,0,8,4,_T("170.1.1.2"));
			break;
		}
		case DISCONNECT:
		{
			statusCode = m_Camera.Disconnect();
			break;
		}
		case AUTOFOCUS:
		{
			statusCode = m_Camera.DoCameraAction(12);
			break;
		}		
		case GETIMAGE:
		{
			char *filename;
			filename = (char*)pData->lpData;
			CFSViewerView::MyGetImageFunc(filename);
			break;
		}	
		case GETIMAGESERIES:
		{
			statusCode = m_Camera.DoCameraAction(0);
			break;
		}
		case SETFRAMERATE:
		{
			double* framerate_p = (double*)pData->lpData;
			double framerate = *framerate_p;
			VARIANT fr;
			fr.dblVal = framerate;
			statusCode = m_Camera.SetCameraProperty(43, fr);
			VariantClear(&fr);
			break;
		}
		case SETSTOPVALUE:
		{
			double *stopValue_p = (double*)pData->lpData;
			VARIANT sv;
			sv.dblVal = *stopValue_p;
			statusCode = m_Camera.SetCameraProperty(36, sv);
			VariantClear(&sv);
			break;
		}
		case SETFILENAME:
		{
			char *filename;
			filename = (char*)pData->lpData;
			statusCode = CFSViewerView::SetFilename(filename);
			break;
		}
		case STOPRECORDING:
		{
			statusCode = m_Camera.DoCameraAction(CAM_ACTION_RECORDING_STOP);
			break;
		}
		case SETPATH:
		{
			USES_CONVERSION;
			char *path;
			path = (char*)pData->lpData;
			CreateDirectory(A2W(path), NULL);
			statusCode = CFSViewerView::SetPath(path);
			break;
		}
		case SETSTORECONDITION:
		{
			short *storeCondition_p = (short*)pData->lpData;
			VARIANT sc;
			sc.iVal = *storeCondition_p;
			statusCode = m_Camera.SetCameraProperty(27, sc);
			VariantClear(&sc);
			break;
		}
		case SETSTOPCONDITION:
		{
			short *stopCondition_p = (short*)pData->lpData;
			VARIANT sc;
			sc.iVal = *stopCondition_p;
			statusCode = m_Camera.SetCameraProperty(28, sc);
			VariantClear(&sc);
			break;
		}
		case SETSTARTCONDITION:
		{
			short *startCondition_p = (short*)pData->lpData;
			VARIANT sc;
			sc.iVal = *startCondition_p;
			statusCode = m_Camera.SetCameraProperty(29, sc);
			VariantClear(&sc);
			break;
		}
		case SETSTARTVALUE:
		{
			double *startValue_p = (double*)pData->lpData;
			VARIANT sv; 
			sv.dblVal = *startValue_p;
			statusCode = m_Camera.SetCameraProperty(34, sv);
			if(statusCode == 28){
				status = 210;
			}
			VariantClear(&sv);
			break;
		}
		case SETSTOREVALUE:
		{
			double *storeValue_p = (double*)pData->lpData;
			VARIANT sv;
			sv.dblVal = *storeValue_p;
			statusCode = m_Camera.SetCameraProperty(35, sv);
			if(statusCode == 28){
				status = 210;
			}
			VariantClear(&sv);
			break;
		}
		case SETRECORDFORMAT:
		{
			short *recordFormat_p = (short*)pData->lpData;
			VARIANT rf;
			rf.iVal = *recordFormat_p;
			statusCode = m_Camera.SetCameraProperty(33, rf);
			VariantClear(&rf);
			break;
		}
		case PRINTRECORDCONDITIONS:
		{
			CFSViewerView::ShowRecordingProperties();
			break;
		}
		case STATUSQUERY:
		{
			statusQueryStruct *stat = (statusQueryStruct*)pData->lpData;
			short propertyId = stat->propertyId;
			int status = CFSViewerView::GetStatus();
			CFSViewerView::Reply(propertyId, status);
			return TRUE;
		}
		case SIMULATETRIGGER:
		{
			statusCode = m_Camera.DoCameraAction(16);
			break;
		}
		case SETTRIGGERSOURCE:
		{
			short *triggerSource_p = (short*)pData->lpData;
			VARIANT ts;
			ts.iVal = *triggerSource_p;
			statusCode = m_Camera.SetCameraProperty(31, ts);
			VariantClear(&ts);
			break;
		}
		case SETAUTOSHUTTER:
		{
			short *autoShutter_p = (short*)pData->lpData;
			VARIANT as;
			as.iVal = *autoShutter_p;
			statusCode = m_Camera.SetCameraProperty(47, as);
			VariantClear(&as);
			break;
		}
		/* Image correction does not work:
		   statuscode = 29: invalid parameter       */	
		case SETIMAGECORRECTION:
		{
			TRACE("Set image correction\n");
			short *imageCorrection_p = (short*)pData->lpData;
			VARIANT ic;
			ic.iVal = *imageCorrection_p;
			TRACE("Image Correction: %hi\n", ic.iVal);
			statusCode = m_Camera.SetCameraProperty(82, ic);
			VariantClear(&ic);
			break;
		}
		case ENABLERECORDING:
		{
			// configure digital input port 1 on A315
			COleVariant prop;
			prop = COleVariant(_T(".power.settings.diginFunc1"));
			m_Camera.SetCameraProperty(PROP_RESOURCE_PATH, prop);
			prop = COleVariant(_T("markRise"));
			statusCode = m_Camera.SetCameraProperty(PROP_RESOURCE_VALUE, prop);
			VariantClear(&prop);
			//statusCode = m_Camera.DoCameraAction(2);
			break;
		}
		default:
		{
			status = 240;
			break;
		}
	}

	if(statusCode == 0 && status == 0){
		status = 210;
	}
	else if(statusCode != 0 && status == 0){
		status = 240;
	}
	CFSViewerView::Reply(0, status);

	return TRUE;
}

void CFSViewerView::MyDisplayImage(int nImageType, HGLOBAL hMem, HBITMAP* hBmp, char* filename) 
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
	int imgSize;
	int xAlignSize = ((w + 3) & ~3);  // Must be 4 byte aligned
	imgSize  = sizeof(BITMAPINFOHEADER);
	imgSize += 256 * sizeof(RGBQUAD);
	imgSize += (xAlignSize * h);

	FILE *imagefile = fopen(filename,"w");

	int rowsize = xAlignSize;
	int *pSrc;
	pSrc = (int*)GlobalLock(hMem);
		
	for(int i=0; i<imgSize; i++){
		fprintf(imagefile,"%d\n",pSrc[i]);
	}
	TRACE("MyDisplayImage printed file\n");
		

	GlobalUnlock(hMem);
		
	fclose(imagefile);
		
}

void CFSViewerView::ListFrameRates(){
	double framerates;
	long ix = 1;
	VARIANT frs;
	frs = m_Camera.GetCameraProperty(75);
	//Need to find out: How to get number of elements (nmax) properly?
	int nmax = 5; 
	for(int i=0; i<nmax; i++){
		HRESULT z = SafeArrayGetElement(frs.parray,&ix,&framerates);
		TRACE("Possible framerates: %lf \n",framerates);
		ix++;
	}

	//TRACE("z: %x\n",z);
	//TRACE("Possible framerates: %lf \n",x);
	//TRACE("Dimensions: %u\n",SafeArrayGetDim(frs.parray));
	//TRACE("%x %x\n",frs.vt,VT_ARRAY);
	//TRACE("%ls\n",VarToStr(frs));

	VariantClear(&frs);
}

void CFSViewerView::ShowRecordingProperties(){
	VARIANT prop;
	prop = m_Camera.GetCameraProperty(27);
	TRACE("Recording store condition: %hi\n",prop.iVal);
	prop = m_Camera.GetCameraProperty(28);
	TRACE("Recording stop condition: %hi\n",prop.iVal);
	prop = m_Camera.GetCameraProperty(29);
	TRACE("Recording start condition: %hi\n",prop.iVal);
	prop = m_Camera.GetCameraProperty(30);
	TRACE("Recording state: %hi\n",prop.iVal);
	prop = m_Camera.GetCameraProperty(31);
	TRACE("Source for recording trigs: %hi\n",prop.iVal);
	prop = m_Camera.GetCameraProperty(32);
	TRACE("Recording trig port: %hi\n",prop.iVal);
	prop = m_Camera.GetCameraProperty(33);
	TRACE("Recording file format: %hi\n",prop.iVal);
	prop = m_Camera.GetCameraProperty(34);
	TRACE("Recording start value: %lf\n",prop.dblVal);
	prop = m_Camera.GetCameraProperty(35);
	TRACE("Recording store value: %lf\n",prop.dblVal);
	prop = m_Camera.GetCameraProperty(36);
	TRACE("Recording stop value: %lf\n",prop.dblVal);
	prop = m_Camera.GetCameraProperty(91);
	TRACE("Camera file format: %hi\n",prop.iVal);
	
	prop = m_Camera.GetCameraProperty(37);
	BSTR bstrStart = prop.bstrVal;
	char* filename;
	CStringA c_filename(bstrStart);
	filename = (char*) (LPCSTR) c_filename;
	TRACE("Recording file base name: %s\n",filename);

	prop = m_Camera.GetCameraProperty(38);
	TRACE("Presentation mode: %hi\n",prop.iVal);

	prop = m_Camera.GetCameraProperty(39);
	bstrStart = prop.bstrVal;
	char* path;
	CStringA c_path(bstrStart);
	path = (char*) (LPCSTR) c_path;
	TRACE("Recording file base name: %s\n",path);
	VariantClear(&prop);
}



short CFSViewerView::SetFilename(char* filename){
	short statusCode;
	CString fn_CStr = CString(filename);
    BSTR fn_BSTR = fn_CStr.AllocSysString();
	VARIANT fn;
	fn.bstrVal = fn_BSTR;
	statusCode = m_Camera.SetCameraProperty(37, fn);
	VariantClear(&fn);
	return statusCode;
}

short CFSViewerView::SetPath(char* path){
	short statusCode;
	CString path_CStr = CString(path);
    BSTR path_BSTR = path_CStr.AllocSysString();
	VARIANT pa;
	pa.bstrVal = path_BSTR;
	statusCode = m_Camera.SetCameraProperty(39, pa);
	VariantClear(&pa);
	TRACE("Path name: %s\n", path);
	return statusCode;
}

int CFSViewerView::GetStatus(){
	int statusCode;
	short recordingStatus = m_Camera.GetCameraProperty(30).iVal;

	if(recordingStatus == 2){
		statusCode = 220;
	}
	else if (recordingStatus == 1){
		statusCode = 210;
	}
	else{
		statusCode = 240;
	}

	return statusCode;
}

void CFSViewerView::Reply(short propertyId, int status){
	statusQueryStruct stat;
	stat.propertyId = propertyId;
	stat.status = status;
	
	HANDLE npipe;
	DWORD bread;

	npipe = CreateFile(PIPENAME,
                       GENERIC_READ | GENERIC_WRITE,
                       0, NULL, OPEN_EXISTING, 0, NULL);
	

    if( npipe == INVALID_HANDLE_VALUE ){
		TRACE("Error: cannot open named pipe\n");
    }
	else{
		TRACE("Opened named pipe\n");
	}
	
	if( !WriteFile(npipe, &stat, sizeof(stat), &bread, NULL) ){
         TRACE("Error writing the named pipe\n");
    }
	else{
		TRACE("Wrote to named pipe\n");
	}
	
	
}
