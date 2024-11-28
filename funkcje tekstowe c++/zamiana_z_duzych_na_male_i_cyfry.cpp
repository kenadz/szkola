#include <iostream>
#include <fstream>
#include <cctype>

using namespace std;

string zamianacyfry(string a)
{
    for (char &c : a)
    {
        if (isdigit(c))
        {
            c = '#';
        }
    }
    return a;
}

string namalelitery(string a)
{
    for (char &c : a)
    {
        if (isupper(c))
        {
            c = tolower(c);
        }
    }
    return a;
}

// int main()
// {
//     ifstream in("in2.txt");
//     ofstream out("out2.txt");

//     if (!in.is_open())
//     {
//         cerr << "Nie można otworzyć pliku wejściowego!" << endl;
//         return 1;
//     }
//     if (!out.is_open())
//     {
//         cerr << "Nie można otworzyć pliku wynikowego!" << endl;
//         return 1;
//     }

//     string zdanie;

//     while (getline(in, zdanie))
//     {
//         zdanie = zamianacyfry(zdanie);
//         zdanie = namalelitery(zdanie);
//         out << zdanie << endl;
//     }

//     in.close();
//     out.close();
//     return 0;
// }

int main()
{
    int i,d;
    string s;
    getline(cin, s);
    d = s.size();
    for(i=0;i<d;i++)
    {
        if(s[i] >= 'A' && s[i] <= 'Z')
            s[i] = s[i] + 32;
        else if(s[i] >= 'a' && s[i] <= 'z')
            s[i] = s[i] - 32;
    }
    cout<<s;
    return 0;
}