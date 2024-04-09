#include <iostream>
#include <string>

using namespace std;

int main()
{
    string nome, sobrenome; // Declaração de variáveis e seu tipo [string]

    // Solicitação de entrada do usuário
    cout << "Digite seu nome: ";
    cin >> nome;
    cout << "Digite seu sobrenome: ";
    cin >> sobrenome;

    // Imprimir o sobrenome e primeira letra do nome
    cout << sobrenome << ", " << nome[0] << endl;

    // Contar o número de caracteres
    int num_caracteres = nome.size();

    // Definir qual posição mostrar
    int ultima_posicao = nome.size() - 1;

    //  Imprimir o primeiro nome e última letra dele
    cout << "O seu nome possui " << num_caracteres << " caracteres." << endl;
    cout << "A ultima letra do seu nome eh " << nome[ultima_posicao] << "." << endl;
    return 0;
}
