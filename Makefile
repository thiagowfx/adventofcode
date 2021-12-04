DAY=1

INPUT = day$(DAY)/input.txt
OUTPUT = day$(DAY)/output.txt
TARGET = day$(DAY)/main

CXXFLAGS = -g -Wall -Werror

all: python

clean:
	$(RM) $(TARGET)

cpp: $(TARGET)
	./$(TARGET) $(INPUT) | tee $(OUTPUT)

python:
	./$(TARGET).py $(INPUT) | tee $(OUTPUT)

.PHONY: all clean cpp python
