
#include <bits/stdc++.h>
using namespace std;
const int MAX = 10000;

int nkfix[MAX + 1];
void nkbuild()
{
    bool prime[MAX + 1];
    memset(prime, true, sizeof(prime));
    for (int p = 2; p * p <= MAX; p++)
    {
        if (prime[p] == true)
        {
            for (int i = p * 2; i <= MAX; i += p)
                prime[i] = false;
        }
    }
    nkfix[0] = nkfix[1] = 0;
    for (int p = 2; p <= MAX; p++)
    {
        nkfix[p] = nkfix[p - 1];
        if (prime[p])
            nkfix[p]++;
    }
}

int primnk(int L, int R)
{
    return nkfix[R] - nkfix[L - 1];
}
int main()
{
    nkbuild();

    int nk, b;
    // nk=50;
    cin >> nk;
    b = 0;
    while (nk != 1)
    {
        b = b + 1;
        nk = nk - primnk(1, nk);
    }

    cout << b + 1 << endl;
    return 0;
}
