#include <iostream>

void printArray(int arr[], int size) {
    std::cout << "[";
    for (int i=0; i<size; i++) { 
        std::cout << arr[i] << ", "; 
    }
    std::cout << "\b\b]" << std::endl;
}

void merge(int array[], int left, int mid, int right) {

    int leftSize = mid - left + 1;
    int rightSize = right - mid;

    int *leftArray = new int[leftSize];
    int *rightArray = new int[rightSize];
    
    for (int i=0; i<leftSize; i++)
        leftArray[i] = array[left + i];
    for (int i=0; i<rightSize; i++)
        rightArray[i] = array[mid + 1 + i];

    int lindex = 0, rindex = 0;
    int i = left;

    while (lindex < leftSize && rindex < rightSize) {
        if (leftArray[lindex] < rightArray[rindex]) {
            array[i++] = leftArray[lindex++];
        } else {
            array[i++] = rightArray[rindex++];
        }
    }

    while (lindex < leftSize)
        array[i++] = leftArray[lindex++];
    while (rindex < rightSize)
        array[i++] = rightArray[rindex++];

    delete[] leftArray;
    delete[] rightArray;
}

void mergesort(int array[], int const left, int const right) {
    if (left >= right) 
        return;

    int mid = (left + right) / 2;
    mergesort(array, left, mid);
    mergesort(array, mid + 1, right);
    merge(array, left, mid, right);
}

int main() {
     int arr[] = {12, 11, 13, 5, 6, 7};
     int size = sizeof(arr) / sizeof(int);
     printArray(arr, size);
     mergesort(arr, 0, size-1);
     printArray(arr, size);
     return 0;
}
