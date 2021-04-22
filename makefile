CC = gcc
CFLAGS = -fPIC -shared -Wall -Werror
TARGET = functions

all: %(TARGET)

%(TARGET): %(TARGET).c
	%(CC) %(CFLAGS) -o %(TARGET).so %(TARGET).c
	rm %(TARGET)