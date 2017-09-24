## usage of c_str
### answer 1
c_str returns a const char* that points to a null-terminated string (i.e. a C-style string). It is useful when you want to pass the "contents"¹ of an std::string to a function that expects to work with a C-style string.

For example, consider this code:

std::string str("Hello world!");
int pos1 = str.find_first_of('w');

int pos2 = strchr(str.c_str(), 'w') - str.c_str();

if (pos1 == pos2) {
    printf("Both ways give the same result.\n");
}
See it in action.

Notes:

¹ This is not entirely true because an std::string (unlike a C string) can contain the \0 character. If it does, the code that receives the return value of c_str() will be fooled into thinking that the string is shorter than it really is, since it will interpret \0 as the end of the string.

### answer 2
In C++, you define your strings as

std::string MyString;

instead of

char MyString[20];.

While writing C++ code, you encounter some C functions which require C string as parameter.
Like below:

void IAmACFunction(int abc, float bcd, const char * cstring);

Now there is a problem. You are working with C++ and you are using std::string string variables. But this C function is asking for a C string. How do you convert your std::string to a standard C string?

Like this:

std::string MyString;
// ...
MyString = "Hello world!";
// ...
IAmACFunction(5, 2.45f, MyString.c_str());
This is what c_str() is for.

Note that, for std::wstring strings, c_str() returns a const w_char *.