#include <iostream>
#include <fstream>

using std::cout;
using std::endl;
using std::string;

void readNumbers() {
    // Create our ifstream and make it open the file
    // ifstream是一类类型，下面是声明了一个对象，然后这个对象有很多方法
    // 比方说>>就是这个 对象的方法^-^
    std::ifstream input("numbers.txt");

    // This will store the values  as we get them form the stream
    int value;
    while(true) {
        // Extract next number from input
        input >> value;

        // If input is in a fail state, neither a value couldn't
        // be converted, or we are at the end of the file

        if(input.fail())
            break;
        cout << "Value read: " << value << endl;
    }
}

void readHaikuWord() {
    // Create  our ifstream and make it open the file
    std::ifstream input("haiku.txt");
    string word;
    while(true) {
        // Extract next word from input
        input >> word;
        // If input is in a fail state, either a value couldn't 
        // be converted, or we are at the end of the file
        if(input.fail())
            break;
        cout << "Word read: " << word << endl;
    }
}

void readHaikuLine() {
    // Create our ifstreams and make it open the file
    std::ifstream input("haiku.txt");

    // This will store the lines as we get them form the stream
    string line;
    while(true) {
        std::getline(input, line);

        // If input is in a fail state, either a value couldn't
        // be converted, or we are at the end of the file
        if(input.fail())
            break;
        cout << line << endl;
    }
}

int main() {
    readNumbers();
    cout << "==================================" << endl;
    readHaikuWord();
    cout << "==================================" << endl;
    readHaikuLine();
    return 0;
}