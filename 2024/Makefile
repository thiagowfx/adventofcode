# Usage:
#
# Initially:
#   make DAY=1 DEBUG=1
#
# Then:
#   make DAY=1 DEBUG=0

DAY ?= 5
DEBUG ?= 1

SAMPLE = day$(DAY)/sample.txt
INPUT = day$(DAY)/input.txt
OUTPUT = day$(DAY)/output.txt
TARGET = day$(DAY)/main.py
TEMPLATE = ../template.py

ifeq ($(DEBUG), 0)
	ACTUAL_INPUT = $(INPUT)
else
	ACTUAL_INPUT = $(SAMPLE)
endif

all:
	./$(TARGET) $(ACTUAL_INPUT) | tee $(OUTPUT)

new:
	mkdir day$(DAY)
	touch $(INPUT) $(SAMPLE)
	cp $(TEMPLATE) $(TARGET)

.PHONY: all new
