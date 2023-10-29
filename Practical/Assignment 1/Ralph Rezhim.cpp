#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>

using namespace std;

int main() {
    
    int allChocoloates, allDays, input;
    int chocoloatesNumSum = 0;

    scanf("%d%d", &allChocoloates, &allDays);

    int chocoloatesNum[allChocoloates];
    int doneChocoloates[allChocoloates];
    int indiceChocoloates[allChocoloates];
    int answer[allDays];
    int indice[allChocoloates];

    for (int i = 0; i < allChocoloates; i++){
        scanf("%d", &input);
        chocoloatesNumSum += input;
        chocoloatesNum[i] = input;
        doneChocoloates[i] = 0;
        indice[i] = 0;
    }

    int sum2 = 2 * chocoloatesNumSum;

    for (int i = 1; i <= allDays; i++) {
        int min = numeric_limits<int>::max();
        int indiceX = 0;
        for (int j = 0; j < allChocoloates; j++) {
            int min2 = sum2 + indice[j] - i * chocoloatesNum[j];
            if (min2 < min) {
                min = min2;
                indiceX = j;
            }
        }
        indice[indiceX] = indice[indiceX] + chocoloatesNumSum;
        answer[i-1] = indiceX + 1;
    }
    
    for (int i = 0; i < allDays; i++){
        printf("%d ", answer[i]);
    }

}