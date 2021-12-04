CXXFLAGS = -g -Wall -Werror

INPUT = input.txt
OUTPUT = output.txt

TARGET = main

all: $(TARGET)

run: $(TARGET)
	./$(TARGET) $(INPUT) | tee $(OUTPUT)

clean:
	$(RM) $(TARGET)

python:
	./$(TARGET).py $(INPUT) | tee $(OUTPUT)

.PHONY: all clean
