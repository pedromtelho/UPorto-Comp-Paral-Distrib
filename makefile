# Compiler and linker
CC = g++

# Flags
CFLAGS = -Wall -O2

compile: 
	${CC} ${CFLAGS} -o matrix matrix.cpp -lpapi

compileOMP: 
	${CC} ${CFLAGS} -o matrix matrix.cpp -lpapi -fopenmp

clean:	
	@rm -f matrix Matrix.class