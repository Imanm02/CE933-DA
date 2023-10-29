#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

int coloring(const int ar[], int left, int right, int numberOfColumn);

int main() {

    int input, a;

    scanf("%d", &input);

    int arrays[input];

    for (int i = 1; i <= input; i++){
        scanf("%d", &a);
        arrays[i-1] = a;
    }

    int output = coloring(arrays, 0, input-1, 0);

    printf("%d", output);

    return 0;
}

int coloring(const int ar[], int left, int right, int numberOfColumn){

    if (right < left){
        return 0;
    }
    
    int minimum = ar[left];
    int indexMinimum = left;

    for(int j = left; j <= right; j++){
        if (minimum > ar[j]){
            minimum = ar[j];
            indexMinimum = j;
        }
    }

    int direction = right - left;
    int columns = direction + 1;
    int bothColoring = coloring(ar, left, indexMinimum - 1, minimum) + coloring(ar, indexMinimum + 1, right, minimum);
    int columns2 = bothColoring + minimum - numberOfColumn;

    if (columns < columns2){
        return columns;
    }
    else{
        return columns2;
    }
}