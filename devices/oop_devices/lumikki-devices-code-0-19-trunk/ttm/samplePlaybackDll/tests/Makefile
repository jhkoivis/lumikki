
LD=ld -G

####################################
# OSX
####################################
ISDARWIN=$(shell uname)
ifeq ($(ISDARWIN), Darwin)
LD=libtool -dynamic -lm
endif
####################################

sourceDir=../samplePG-VisualStudioProject/samplePlaybackGenerator/

all: singen creep

singen:
	rm -f *.o *.c
	ln -s $(sourceDir)/singen.cpp singen.c
	gcc -fPIC -lm -c singen.c -I$(sourceDir) -o singen.o
	$(LD) singen.o -o singen.so
	rm *.o *.c
	
creep:
	rm -f *.o *.c
	ln -s $(sourceDir)/creepWithLinearStartRamp.cpp creepWithLinearStartRamp.c
	gcc -fPIC -c creepWithLinearStartRamp.c -I$(sourceDir) -o creepWithLinearStartRamp.o
	$(LD) creepWithLinearStartRamp.o -o creepWithLinearStartRamp.so
	rm -f *.o *.c
	
tests:
	python testSinGen.py
	python testCreep.py

clean:
	rm -f *.o *.so *.pyc
	
