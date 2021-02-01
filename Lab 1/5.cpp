#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    for (int i = n; i > 0; i-=1){
        for (int j = 0; j < i; j+=1){
            std::cout << "*";
        }
        std::cout << std::endl;
    }
}
