
#include <stdio.h>

#define MAX_LENGTH 1000
#define LOG_FILE_NAME "c:/tmp/test.log"

int main(void)
{
	int i = 0;
	char text[MAX_LENGTH];
	FILE *testFile;
	
	testFile = fopen(LOG_FILE_NAME, "a");
	while((text[i] = fgetc(stdin)) != EOF)
	{
		fprintf(testFile,"%c", text[i]);
		fflush(testFile);
		i++;
		if (i >= (MAX_LENGTH - 1)) break;	
	}
	text[i] = '\0';

	fprintf(stdout, "Content Type: application/javascript\n\n");
	fprintf(stdout, "%s", text);
	fclose(testFile);
	
	return 0;
}