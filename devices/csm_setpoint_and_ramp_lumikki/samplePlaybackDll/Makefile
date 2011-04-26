

all:
	gcc -fPIC -lm -c singen.c -I. -o singen.o
	ld -G singen.o -o singen.so

tests:
	python testSinGen.py
	