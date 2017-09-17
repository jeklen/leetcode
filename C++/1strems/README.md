## Streams
A stream is an abstraction for input/output

### Output Streams
- std::cout is an example 
- all output streams are of type std::ostream
- use operator << 
- use std::ofstream to send the data to a file

### Input Streams

- the std::cin streams is an example of an input stream
- all input streams are type std::istream
- use opereator >>
- use std::ifstream to read data form a file

### Reading Data From a File

- using >> will only read a single word, not the whole line
- for a whole line: getline(istream& stream, string& line);

### Stream Miscellany

- input.get(ch);    // read one char at a time
- input.close();    // closes stream
- input.clear();    // resets any fail bits
- input.open("filename");   // open stream on file
- input.seekg(0);   // rewinds stream to start
