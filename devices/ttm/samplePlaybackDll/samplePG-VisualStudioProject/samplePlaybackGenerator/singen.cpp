
#include <math.h>

double *singen(
		double t0,
		double tStep,
		double *output,
		int outputLength)
{
	int i;
	double 	tCurr;
	double	pi;

	pi = 3.14159265;

	for(i = 0; i < outputLength; i++)
	{
		tCurr = t0 + i*tStep;
		output[i] = sin(tCurr*2*pi);
	}

	return output;

}

