#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
	ifstream input(argv[1]);
	string line;
	vector<int> numbers;
	while (std::getline(input, line)) {
		numbers.push_back(atoi(line.c_str()));
	}

	// Part 1
	unsigned int answer = 0;
	for (auto it = numbers.begin() + 1; it != numbers.end(); ++it) {
		if (*it > *(it - 1)) {
			++answer;
		}
	}
	cout << answer << endl;

	// Part 2
	answer = 0;
	for (auto it = numbers.begin() + 3; it != numbers.end(); ++it) {
		if (*it > *(it - 3)) {
			++answer;
		}
	}
	cout << answer << endl;

	return 0;
}
