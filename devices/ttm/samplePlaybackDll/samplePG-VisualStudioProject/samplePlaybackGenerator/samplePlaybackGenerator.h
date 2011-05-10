
#include "singen.h"
#include "creepWithLinearStartRamp.h"

BOOL WINAPI DllMain(HINSTANCE hinstDLL,DWORD,LPVOID);

_declspec (dllexport) double *dllSinWave(double	t0, 
									  double	tStep, 
									  double	*output,
									  int		outputLength);

_declspec (dllexport) double *dllCreepWithLinearStartRamp(double	t0,
													   double	tStep,
													   double	*output,
													   int		outputLength,
													   double	load,
													   double	rampTime);



