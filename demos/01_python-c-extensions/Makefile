CC = gcc
CFLAGS = -Wall -Werror -shared -fPIC
INCLUDES = -I/usr/include/python3.10

double_nums: double_nums.c
	$(CC) $(CFLAGS) double_nums.c -o double_nums.so $(INCLUDES)

clean:
	rm -rf double_nums.so