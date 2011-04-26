
#include <math.h>

#define PI 3.1415265
//(atan(1.0)*4)

float *singen(
		float t0,
		float tStep,
		float *output,
		int outputLength)
{
	int i;
	float 	tCurr,
			pi;

	pi = PI;

	for(i = 0; i < outputLength; i++)
	{
		tCurr = t0 + i*tStep;
		output[i] = sin(tCurr*2*pi);
	}

	return output;

}

/*
int main(int argc, char **argv) {

	float
		t0,
		tMax,
		tStep;

	singen(t0, tMax, tStep, output)
}

*/
