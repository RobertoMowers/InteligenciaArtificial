#include <iostream>
#include <string>
#include <vector>
using namespace std;

int changeNumber(char letra){
    switch(letra){
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
    }

}

int Sumatoria(vector<int> arreglo){
    int total = 0;
    int preSum = arreglo[0];
    for(int i=1;i<arreglo.size();i++){
        if(preSum == 0){
            preSum = arreglo[i];
            continue;
        }
        if(arreglo[i]>preSum){
            total = total + arreglo[i] - preSum;
            preSum = 0;
        }
        if(arreglo[i]==preSum){
            preSum += arreglo[i];
        }

    }
    return total;
}

int main(){
    string romano = "XXLIIV";
    vector<int> arreglo;
    
    for(int i=0;i<romano.size();i++){
        int newNum = changeNumber(romano[i]);
        arreglo.push_back(newNum);
    }
    int suma = Sumatoria(arreglo);
    cout << suma;

    return 0;
}