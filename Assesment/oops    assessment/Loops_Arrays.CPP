#include <iostream>
using namespace std;

int main() {
    // 7 din ke data ke liye array
    int screenTime[7];
    int total = 0;

    cout << "=== 7-Day Screen Time Tracker ===" << endl;

    // Loop chalakar 7 din ka data input lena
    for(int i = 0; i < 7; i++) {
        cout << "Enter screen time for Day " << (i + 1) << " (in hours): ";
        cin >> screenTime[i];
        total += screenTime[i]; // Total mein add karte ja rahe hain
    }

    // Average nikalna (float use kiya taaki decimal mein aaye)
    float average = (float)total / 7;

    cout << "\n--- Weekly Report ---" << endl;
    cout << "Total screen time: " << total << " hours" << endl;
    cout << "Average screen time: " << average << " hours/day" << endl;

    // Condition check: Agar average 4 ghante se zyada hai toh warning
    if(average > 4.0) {
        cout << "WARNING: Your average screen time exceeds the healthy limit (4 hours)!" << endl;
    } else {
        cout << "Great job! You have a healthy screen time." << endl;
    }

    return 0;
}