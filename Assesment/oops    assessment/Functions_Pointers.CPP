#include <iostream>
using namespace std;

// Yeh ek function hai jo pointer (*) use karke actual variable ki value badal dega
void addBonus(int* marks, int bonus) {
    *marks = *marks + bonus; 
}

int main() {
    int studentMarks = 50; // Original marks

    cout << "=== Pointer Magic ===" << endl;
    cout << "Original Marks: " << studentMarks << endl;

    // Function ko call karte time address (&) pass kiya
    addBonus(&studentMarks, 10); 

    // Pointers ki madad se original variable update ho gaya
    cout << "Updated Marks (after 10 marks bonus): " << studentMarks << endl;

    return 0;
}