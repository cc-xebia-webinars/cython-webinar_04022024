# Compiler to use
CC = gcc

# Compiler flags
# -Wall: turn on all warnings
# -Werror: treat warnings as errors
CFLAGS = -Wall -Werror

# Output directory to place the executable
OUTPUT_DIR = ./out

# Target Executable : C Source File
app: app.c
# Create the output directory
	mkdir -p $(OUTPUT_DIR)
# Compile app.c into an executable called app and place it
# in the output directory
	$(CC) $(CFLAGS) -o $(OUTPUT_DIR)/app app.c

# Delete the output folder to clean up
clean:
	rm -rf $(OUTPUT_DIR)