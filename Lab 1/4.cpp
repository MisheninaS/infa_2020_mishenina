#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i+=1){
        for (int j = 0; j < i + 1; j+=1){
            std::cout << "*";
        }
        std::cout << std::endl;
    }
}
