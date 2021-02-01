#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    for (int i = n; i > 0; i-=2){
        for (int j = 0; j < (n - i)/2; j+=1){
            std::cout << " ";
        }
        for (int j = 0; j < i; j+=1){
            std::cout << "*";
        }
        std::cout << std::endl;
    }
}
