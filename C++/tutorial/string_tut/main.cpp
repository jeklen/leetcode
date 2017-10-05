#include <iostream>
#include <string>

using namespace std;

int main()
{
    int number, i, j, tmpScore;
    int* scores;
    string* students = NULL;
    string tmp;
    cout << "Please input numbers: ";
    cin >> number;
    students = new string[number];
    scores = new int[number];
    for (i=0; i<number; i++) {
        cin >> students[i];
        cin >> scores[i];
    }

    for (i=1; i<number; i++) {
        for (j=i-1; j>=0; j--) {
            tmpScore = scores[i];
            tmp = students[i];
            if (scores[j]>tmpScore) {
                students[j+1] = students[j];
                scores[j+1] = scores[j];
            }
            else {
                break;
            }
        }
        students[j+1] = tmp;
        scores[j+1] = tmpScore;
        for (int index=0; index<number; index++) {
            cout << scores[index] << " ";
        }
        cout << endl;
    }
    for (i=0; i< number; i++) {
        cout << students[i] << " " << scores[i] << endl;
    }
    delete [] students;
    delete [] scores;
    return 0;
}

