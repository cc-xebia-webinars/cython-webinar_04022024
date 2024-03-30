CC = gcc
CC_FLAGS = -fPIC -shared

double_nums_lib: double_nums_lib.c
	$(CC) $(CC_FLAGS) double_nums_lib.c -o double_nums_lib.so

clean:
	rm -f double_nums_lib.so
