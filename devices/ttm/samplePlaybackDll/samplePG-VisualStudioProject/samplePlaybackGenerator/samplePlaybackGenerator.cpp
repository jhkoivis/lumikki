

#include "stdafx.h"
#include <windows.h>
#include <string.h>
#include <ctype.h>
#include "samplePlaybackGenerator.h"

BOOL APIENTRY DllMain( HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved ) { return TRUE; } 

_declspec (dllexport) double *dllSinWave(double t0, double step, double *output, int outputLen){

	return singen(t0, step, output, outputLen);
}

_declspec (dllexport) double *dllCreepWithLinearStartRamp(double	t0,
													   double	tStep,
													   double	*output,
													   int		outputLength,
													   double	loadInNewtons,
													   double	rampTimeInSeconds){
	return creepWithLinearStartRamp(t0, tStep, output, outputLength, loadInNewtons, rampTimeInSeconds);
}

