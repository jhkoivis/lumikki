

BOOL WINAPI DllMain(HINSTANCE hinstDLL,DWORD,LPVOID);
_declspec (dllexport) long  add_num(long, long);
_declspec (dllexport) long  avg_num(float *, long, float *);
_declspec (dllexport) unsigned int  numIntegers (unsigned char *);

_declspec (dllexport) float *sinWave(float *t0, float *tMax, float *tStep, float *output);


