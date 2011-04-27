

sourceDir=../samplePG-VisualStudioProject/samplePlaybackGenerator/

all:
	ln -s $(sourceDir)/singen.cpp singen.c
	gcc -fPIC -lm -c singen.c -I$(sourceDir) -o singen.o
	ld -G singen.o -o singen.so
	rm singen.o singen.c

tests:
	python testSinGen.py

clean:
	rm -f *.o *.so *.pyc
	
