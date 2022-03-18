# Compiler and linker
CC = g++

# Flags
CFLAGS = -Wall -O2

compile: 
	${CC} ${CFLAGS} -o matrix matrix.cpp -lpapi

clean:	
	@rm -f matrix Matrix.class