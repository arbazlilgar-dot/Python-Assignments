#include <iostream>
using namespace std;

int main() {
    // Variable banaya jisme user ke padhai ke ghante (hours) save honge
    int hours;

    // User se input lene ke liye message print kiya
    cout << "=== Study Mood Assistant ===" << endl;
    cout << "Enter the number of hours you studied today: ";
    cin >> hours;

    // if-else ladder use karke conditions check kar rahe hain
    if (hours < 0) {
        // Agar koi minus (-) mein value daale toh error dikhayega
        cout << "Invalid input! Hours cannot be negative." << endl;
    } 
    else if (hours == 0) {
        cout << "Message: You haven't started yet! Pick up a book and start studying." << endl;
    } 
    else if (hours >= 1 && hours <= 3) {
        cout << "Message: Good start! But you need to push yourself a little more." << endl;
    } 
    else if (hours >= 4 && hours <= 6) {
        cout << "Message: Great job! You are studying well. Keep it up!" << endl;
    } 
    else {
        // Agar 6 ghante se zyada padha ho
        cout << "Message: Outstanding! You are a study machine. But don't forget to take a break!" << endl;
    }

    return 0;
}