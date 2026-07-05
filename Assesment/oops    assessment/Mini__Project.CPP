#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

// Functions declare kiye hain taaki code clean rahe
void logHours();
void generateReport();

int main() {
    int choice;
    
    // 1. Menu-driven program (do-while loop use karke)
    do {
        cout << "\n=========================================\n";
        cout << "       Student Productivity Tracker      \n";
        cout << "=========================================\n";
        cout << "1. Log Daily Study Hours\n";
        cout << "2. Generate Weekly Report\n";
        cout << "3. Exit\n";
        cout << "Enter your choice (1-3): ";
        cin >> choice;

        switch(choice) {
            case 1:
                logHours();
                break;
            case 2:
                generateReport();
                break;
            case 3:
                cout << "Exiting the tracker. Keep studying hard!\n";
                break;
            default:
                cout << "Invalid choice! Please enter 1, 2, or 3.\n";
        }
    } while(choice != 3);

    return 0;
}

// 2. & 4. Log daily study hours AND Store data using files
void logHours() {
    string day;
    float hours;
    
    cout << "Enter the Day (e.g., Monday, Tuesday): ";
    cin >> day;
    cout << "Enter hours studied today: ";
    cin >> hours;

    // File ko Append (app) mode mein open kiya taaki purana data delete na ho
    ofstream outFile("study_log.txt", ios::app);
    if(outFile.is_open()) {
        outFile << day << " " << hours << "\n";
        outFile.close();
        cout << "-> SUCCESS: Logged " << hours << " hours for " << day << ".\n";
    } else {
        cout << "-> ERROR: Could not open the file to save data.\n";
    }
}

// 3. Generate weekly report
void generateReport() {
    // File ko Read mode mein open kiya
    ifstream inFile("study_log.txt");
    if(!inFile) {
        cout << "-> No data found! Please log some hours first (Option 1).\n";
        return;
    }

    string day;
    float hours;
    float totalHours = 0.0;
    int daysLogged = 0;

    cout << "\n--------- WEEKLY STUDY REPORT ---------\n";
    
    // File se data padh kar screen par print karna
    while(inFile >> day >> hours) {
        cout << "Day: " << day << " | Hours: " << hours << "\n";
        totalHours += hours;
        daysLogged++;
    }
    inFile.close();

    // Total aur Average calculate karke final report dikhana
    if(daysLogged > 0) {
        cout << "---------------------------------------\n";
        cout << "Total Days Logged: " << daysLogged << "\n";
        cout << "Total Study Hours: " << totalHours << " hours\n";
        cout << "Average Hours/Day: " << fixed << setprecision(2) << (totalHours / daysLogged) << " hours\n";
        
        if(totalHours >= 20) {
            cout << "Performance: Excellent work this week!\n";
        } else if(totalHours >= 10) {
            cout << "Performance: Good, but you can push a little harder.\n";
        } else {
            cout << "Performance: Needs improvement. Focus more!\n";
        }
        cout << "---------------------------------------\n";
    }
}