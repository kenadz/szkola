#include <iostream>
#include <vector>

using namespace std;

void najdluzszyciag_niemalejacy(const vector<int>& a, int& pierw_elem, int& dlg)
{
    int maxDlg = 1;
    int index = 0;
    int aktualnaDlg = 1;
    int aktualnyIndex = 0;

    for (int i = 1; i < a.size(); ++i)
    {
        if (a[i] >= a[i - 1])
        {
            aktualnaDlg++;
            if (aktualnaDlg > maxDlg)
            {
                maxDlg = aktualnaDlg;
                index = aktualnyIndex;
            }
        } 
        else
        {
            aktualnyIndex = i;
            aktualnaDlg = 1;
        }
    }

    pierw_elem = a[index];
    dlg = maxDlg;
}

int main() {
    vector<int> a = {2, 3, 4, 5, 2, 4, 6, 8, 10, 5, 4, 3, 2, 1};

    int pierw_elem, length;
    najdluzszyciag_niemalejacy(a, pierw_elem, length);

    cout << "Pierwszy element najdłuższego niemalejącego ciągu: " << pierw_elem << endl;
    cout << "Liczba elementów w ciągu: " << length << endl;

    return 0;
}