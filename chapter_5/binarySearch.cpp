#include <iostream>
#include <string>

int binarySearch(int list[], int item, int left, int right);


int main() {
    
    int list[] = {1, 4, 8, 11, 13, 16, 19, 19};
    int size = sizeof(list) / sizeof(int);
    int item = 13;
    
    int index = binarySearch(list, item, 0, size-1);
    std::cout << "Index is " << index << std::endl;
    return 0;
}


int binarySearch(int list[], int item, int left, int right) {
    
    if (left > right) 
        return -1;
    
    // Integer div rounds down.
    int ret;
    int mid = (left + right) / 2;

    if (list[mid] == item) { 
        ret = mid;
    } else if (list[mid] < item) {
        ret = binarySearch(list, item, mid+1, right);
    } else if (list[mid] > item) {
        ret = binarySearch(list, item, left, mid-1);
    }

    return ret;
}

