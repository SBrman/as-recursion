#include <iostream>


void printArray(int arr[], int size) {
    std::cout << "[";
    for (int i=0; i<size; i++) { 
        std::cout << arr[i] << ", "; 
    }
    std::cout << "\b\b]" << std::endl;
}

void swap(int array[], int i, int j) {
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

void quicksort(int array[], int left, int right) {
    if (left >= right) { return; }
    
    int i = left;
    int pivot = array[right];

    for (int j=left; j<right; j++) {
        if (array[j] < pivot) {
            swap(array, i++, j);
        }
    }
    swap(array, i, right);

    quicksort(array, left, i - 1);
    quicksort(array, i + 1, right);

}

int main() {
    int arr[] = {0, 7, 6, 3, 1, 2, 5, 4};
    int size = sizeof(arr) / sizeof(int);
    printArray(arr, size);
    quicksort(arr, 0, size - 1);
    printArray(arr, size);

    return 0;
}

