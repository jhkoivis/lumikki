

#include "stdafx.h"
#include <windows.h>
#include <string.h>
#include <ctype.h>
#include <samplePlaybackGenerator.h>
#include <singen.h>

BOOL WINAPI  DllMain (
            HANDLE    hModule,
            DWORD     dwFunction,
            LPVOID    lpNot)
{
    return TRUE;
}


_declspec (dllexport) float *sinWaveform(float t0, float step, float *output, int outputLen){

	return singen(t0, step, output, outputLen)
}

/* Add two integers */
_declspec (dllexport) long add_num(long a, long b){
    return((long)(a+b));}

/* This function finds the average of an array of single precision numbers */
_declspec (dllexport)  long  avg_num(float  *a, long size, float  *avg)
{
    float sum=0;

    if(a != NULL)
    {
        for(int i=0;i < size; i++)
        sum = sum + a[i];
    }
    else
        return (1);
    *avg = sum / size;
    return (0);
}

// Counts the number of integer numbers appearing in a string. */
// Note that this function does not check for sign, decimal, or exponent
_declspec (dllexport) unsigned int numIntegers (char *inputString) {
	int      lastDigit = 0;
  int      numberOfNumbers = 0;
  int      stringSize;

  stringSize = strlen(inputString);
  for(int i = 0; i < stringSize; i++){
		if (!lastDigit && isdigit(inputString[i]))   
 	   	numberOfNumbers++;
			lastDigit = isdigit(inputString[i]);                                                     
		}

	return numberOfNumbers;                                                             
}


