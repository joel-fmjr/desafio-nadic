#include <iostream>
#include <chrono>

using namespace std;

const int TAMANHO = 1000000;
unsigned num_passos[TAMANHO] = {};

int numDePassos(int n)
{
    int numPassos = 0;
    unsigned aux = n;

    do
    {
        if (aux < n)
        {
            int passos = num_passos[aux];
            if (passos > 0)
            {
                numPassos += passos;
                break;
            }
        }

        if (aux % 2 == 0)
        {
            numPassos++;
            aux = aux / 2;
        }
        else
        {
            numPassos += 2;
            aux = (3 * aux + 1) / 2;
        }

    } while (aux > 1);

    num_passos[n] = numPassos;
    return numPassos;
}

int main()
{
    auto start = chrono::steady_clock::now();
    int maniorNumPassos = 0;
    unsigned maiorN = 0;

    for (int i = 1; i < TAMANHO; i++)
    {
        int passos = numDePassos(i);

        if (passos > maniorNumPassos)
        {
            maniorNumPassos = passos;
            maiorN = i;
        }
    }

    cout << maiorN << " - " << maniorNumPassos << endl;
    auto end = chrono::steady_clock::now();
    auto diff = end - start;
    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
}