// operator new[] example
#include <iostream>     // std::cout
//#include <new>          // ::operator new[]

struct MyClass {
  int data;
  MyClass() {std::cout << '*';}  // print an asterisk for each construction
};

int main () {
  std::cout << "constructions (1): ";
  // allocates and constructs five objects:
  MyClass * p1 = new MyClass[5];
  std::cout << '\n';

  std::cout << "constructions (2): ";
  // allocates and constructs five objects (nothrow):
  MyClass * p2 = new (std::nothrow) MyClass[5];
  std::cout << '\n';

  delete[] p2;
  delete[] p1;

  int* a = NULL;    // Pointer to int, initialize to nothing
  int n;            // Size needed for the array
  cin >> n;         // Read in the size
  a = new int[n];   // Allocate n ints and szve ptr in a
  for (int i =0; i<n; i++) {
    a[i] = 0;
  }
  delete [] a;      // When done, free memory pointer to by a
  a = NULL;         // Clear a to prevent using invalid memory reference


  return 0;
}
