#include <iostream>
#include <fstream>

using namespace std;

bool podwojna_suma(int num)
{
    int sum = 1 + num;

    for (int i = 2; i <= num / 2; ++i)
    {
        if (num % i == 0)
        {
            sum += i;
        }
    }

    if (sum == 2 * num)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main() {
    ifstream in("in1.txt");
    ofstream out("out1.txt");

    int a;

    while(in >> a)
    {
        if(podwojna_suma(a))
        {
            out << a << endl;
        }
    }

    in.close();
    out.close();

    return 0;
}
