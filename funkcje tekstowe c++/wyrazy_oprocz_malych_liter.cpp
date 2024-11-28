#include <iostream>
#include <fstream>
#include <sstream>
#include <cctype>

using namespace std;

// bool isAllLowerCase(const string& word) {
//     for (char c : word) {
//         if (!(c >= 'a' && c <= 'z')) {
//             return false;
//         }
//     }
//     return true;
// }

bool isAllLowerCase(const string& word) {
    for (char c : word) {
        if (!islower(c)) {
            return false;
        }
    }
    return true;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    string word;

    while (in >> word) {
        if (!isAllLowerCase(word))
        {
            out << word << " ";
        }
    }

    in.close();
    out.close();

    return 0;
}
