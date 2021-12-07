DAY ?= 5
DEBUG ?= 0

SAMPLE = day$(DAY)/sample.txt
INPUT = day$(DAY)/input.txt
OUTPUT = day$(DAY)/output.txt
TARGET = day$(DAY)/main

ifeq ($(DEBUG), 0)
	ACTUAL_INPUT = $(INPUT)
else
	ACTUAL_INPUT = $(SAMPLE)
endif

CXXFLAGS = -g -Wall -Werror

all: python

clean:
	$(RM) $(TARGET)

cpp: $(TARGET)
	./$(TARGET) $(ACTUAL_INPUT) | tee $(OUTPUT)

new:
	mkdir day$(DAY)
	touch $(INPUT) $(SAMPLE) $(TARGET).py
	chmod +x $(TARGET).py

python:
	./$(TARGET).py $(ACTUAL_INPUT) | tee $(OUTPUT)

.PHONY: all clean cpp new python
