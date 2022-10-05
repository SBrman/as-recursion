#include <iostream>

int sumDivConq(int array[], unsigned int size) {
    if (size == 0) { 
        return 0; 
    } else if (size == 1) {
        return array[0];
    } else {
        int arr1Size = size / 2;
        int arr2Size = size - arr1Size;
        int *arr1 = new int[arr1Size];
        int *arr2 = new int[arr2Size];
        
        for (int i=0; i<arr1Size; i++)
            arr1[i] = array[i];
        for (int i=0; i<arr2Size; i++)
            arr2[i] = array[i + arr1Size];
        
        int leftHalfSum = sumDivConq(arr1, arr1Size);
        int rightHalfSum = sumDivConq(arr2, arr2Size);

        delete[] arr1;
        delete[] arr2;

        return leftHalfSum + rightHalfSum;
    }
}


int main() {
    
    int nums[] = {1, 2, 3, 4, 5};
    int size = sizeof(nums) / sizeof(int);
    std::cout << "Sum is: " << sumDivConq(nums, size) << std::endl;
}
