#include <iostream>
#include <fstream>

using std::cout;
using std::endl;
using std::string;

void readNumbers() {
    std::ifstream input("numbers.txt");
    int value;
    while(true) {
        input << vlaue;
        if(input.fail())
            break;
        cout << "Value read: " << value << endl;
    }
}

void readHaikuWord() {
    std::ifstream input("haiku.txt");
    string word;
    while(true) {
        input >> word;
        if(input.fail())
            break;

        cout << "Word read: " << word << endl;
    }
}

void readHaikuLine() {
    std::ifstream input("haiku.txt");
    string line;
    while(true) {
        std::getline(input, line);
        if(input.fail())
            break;
        cout << line << endl;
    }
}

int main()
{
}
