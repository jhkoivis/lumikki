

BOOL WINAPI DllMain(HINSTANCE hinstDLL,DWORD,LPVOID);
_declspec (dllexport) long  add_num(long, long);
_declspec (dllexport) long  avg_num(float *, long, float *);
_declspec (dllexport) unsigned int  numIntegers (unsigned char *);

_declspec (dllexport) double *sinWave(double	t0, 
									  double	tStep, 
									  double	*output,
									  int		outputLength);

