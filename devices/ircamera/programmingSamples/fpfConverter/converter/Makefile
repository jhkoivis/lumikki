

all:
	gcc -m32 -c fpfConverterLib.c -o fpfConverterLib.o
	gcc -m32 fpfConverter.c fpfConverterLib.o -o fpfConverter

clean:
	rm -f *.o
	rm -f fpfConverter

tests:
	./fpfConverter test/1.fpf test/1.pgm
	#open test/1.pgm
