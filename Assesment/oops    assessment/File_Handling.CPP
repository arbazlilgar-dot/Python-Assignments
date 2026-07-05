#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string savedData;

    cout << "=== File Handling Program ===" << endl;

    // 1. Sabse pehle hum check karenge ki purani file me koi data hai ya nahi (Read mode)
    ifstream inFile("mydata.txt");
    if (inFile.is_open()) {
        cout << "[Restart Check] Previous Saved Data:" << endl;
        while (getline(inFile, savedData)) {
            cout << "-> " << savedData << endl;
        }
        inFile.close();
    } else {
        cout << "No previous data found. Starting fresh." << endl;
    }

    // 2. Ab hum user se naya data le kar file me save karenge (Append mode)
    ofstream outFile("mydata.txt", ios::app); 
    if (outFile.is_open()) {
        string newData;
        cout << "\nEnter new text to save in file: ";
        getline(cin, newData);
        
        outFile << newData << endl; // File me write kar diya
        cout << "Data saved successfully! Restart the program to read this again." << endl;
        outFile.close();
    } else {
        cout << "Error: Unable to open file for writing." << endl;
    }

    return 0;
}