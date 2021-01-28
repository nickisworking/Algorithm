#include <iostream>
#include <cstring>

using namespace std;

int main() {
	const char* c[] = { "ENTER", "NEW", "POINT", "FIRST" };
	
	const char** cp[] = { c+3 , c+2 , c+1, c};
	
	const char*** cpp = cp;


	cout <<"c : "<< c << endl;
	cout << "cp: " << cp << endl;
	cout << "cpp: " << cpp << endl;

	cout << "*cpp :" << *cpp << endl;
	cout << "**cpp: "<<**cpp<<endl;
	cout << "***cpp: "<<***cpp<<endl;

	printf("%s", **++cpp); 

	
	printf("%s ", *--* ++cpp + 3);
	
	printf("%s", *cpp[-2] + 3); 
	
	printf("%s\n", cpp[-1][-1] + 1);
	
  //POINTER STEW0
}