
#include "fpfConverter.h"



int main(int argc, char *argv[])
/*
 * Read fpf file as argument 1 and save pgm file as argument 2.
 * 
 * - Header to header, data to image.
 * - add: 
 * 		minT : min(temperature)
 * 		maxT : max(temperature)
 * - scale:
 * 		minT -> 0
 * 		maxT -> 2^16 = 65536
 * 
 * */
{
	char 	*pFpfFn,
			*pPgnFn,
			header[MAX_STRING_SIZE];
	FILE 	*pFpfFile,
			*pPgnFile;
	FPFHEADER_T 
			fpfHeader;
	float	data,
			tMin,
			tMax,
			fpfData[MAX_FLOAT_ARRAY],
			dataMax,
			dataMin;
	int 	dataInt,
			maxFloatCount = MAX_FLOAT_ARRAY,
			i;
	
	/*
	 *User IO handling
	 */
	if (argc != 3){
		printf("usage:\n  %s inFile.fpf outFile.pgn\n", argv[0]);
		return 1;
	}
	pFpfFn = argv[1];
	pPgnFn = argv[2];
	printf(	"\n  reading: %s\n  saving:  %s\n",
			pFpfFn,
			pPgnFn);
	/*
	 * Read data to memory
	 */
	
	pFpfFile = fopen(pFpfFn,"r");
	fread(&fpfHeader, sizeof(FPFHEADER_T), 1, pFpfFile);
	makeData(pFpfFile, fpfData, &maxFloatCount);


	// find max
	dataMax = fpfData[0];
	dataMin = fpfData[0];
	for (i = 0; i < maxFloatCount; i++)
	{
		if (dataMin > fpfData[i]) dataMin = fpfData[i];
		if (dataMax < fpfData[i]) dataMax = fpfData[i];
	}

	/*
	 * Make PGN file
	 */

	pPgnFile = fopen(pPgnFn, "w");
	makeHeader(&fpfHeader, header, &dataMin, &dataMax);
	fprintf(pPgnFile, "%s", header);

	for (i = 0; i < maxFloatCount; i++)
	{
		data = PGN_MAX_VALUE*(fpfData[i]-dataMin)/(dataMax-dataMin);
		dataInt = (int)(data + 0.5);
		fprintf(pPgnFile, "%d\n", dataInt);
	}

	return 0; 
	
}
