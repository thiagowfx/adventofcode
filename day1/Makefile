CXXFLAGS = -g -Wall -Werror

INPUT = input.txt
OUTPUT = output.txt
TEST = test.txt

TARGET = main

all: $(TARGET)

run: $(TARGET)
	./$(TARGET) $(INPUT) | tee $(OUTPUT)

test: $(TARGET)
	./$(TARGET) $(TEST)

clean:
	$(RM) $(TARGET) $(OUTPUT)

.PHONY: all clean
