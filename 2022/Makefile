DAY ?= 1
DEBUG ?= 1

SAMPLE = day$(DAY)/sample.txt
INPUT = day$(DAY)/input.txt
OUTPUT = day$(DAY)/output.txt
TARGET = day$(DAY)/main

ifeq ($(DEBUG), 0)
	ACTUAL_INPUT = $(INPUT)
else
	ACTUAL_INPUT = $(SAMPLE)
endif

all:
	./$(TARGET).py $(ACTUAL_INPUT) | tee $(OUTPUT)

clean:
	$(RM) $(TARGET)

new:
	mkdir day$(DAY)
	touch $(INPUT) $(SAMPLE) $(TARGET).py
	chmod +x $(TARGET).py

.PHONY: all clean new
