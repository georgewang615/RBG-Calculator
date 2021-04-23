CC = gcc
CFLAGS = -fPIC -shared -Wall -Werror
TARGET = c_functions


$(TARGET): $(TARGET).c
		$(CC) $(CFLAGS) -o $(TARGET).so $(TARGET).c