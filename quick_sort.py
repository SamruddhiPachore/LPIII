#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int randomPartition(int low, int high, vector<int> &arr) {
  srand(time(NULL));
  int random = low + rand() % (high - low + 1);

  int pivot = arr[random];

  // Swap the random to the last
  swap(arr[random], arr[high]);

  int i = low;
  for (int j = low; j <= high - 1; j++) {
    if (arr[j] < pivot) {
      swap(arr[j], arr[i]);
      i++;
    }
  }

  swap(arr[i], arr[high]);
  return i;
}

void randomQuickSort(int low, int high, vector<int> &arr) {
  if (low < high) {
    int pivot = randomPartition(low, high, arr);
    randomQuickSort(low, pivot - 1, arr);
    randomQuickSort(pivot + 1, high, arr);
  }
}

int partition(int low, int high, vector<int> &arr) {
  int pivot = arr[high];
  int i = low;

  for (int j = low; j <= high - 1; j++) {
    if (arr[j] < pivot) {
      swap(arr[j], arr[i]);
      i++;
    }
  }

  swap(arr[i], arr[high]);
  return i;
}

void quickSort(int low, int high, vector<int> &arr) {
  if (low < high) {
    int pivot = partition(low, high, arr);
    quickSort(low, pivot - 1, arr);
    quickSort(pivot + 1, high, arr);
  }
}

int main() {
  cout << "Quick Sort Program" << endl;

  // Quick Sort
  vector<int> arr1 = {8, 2, 1, 3, 6, 2, 4, 5, 2};
  quickSort(0, arr1.size() - 1, arr1);

  cout << "Sorted Array Normal Quick Sort: ";
  for (auto num : arr1) {
    cout << num << " ";
  }
  cout << endl;

  // Random Quick Sort
  vector<int> arr2 = {8, 2, 1, 3, 6, 2, 4, 5, 2};
  randomQuickSort(0, arr2.size() - 1, arr2);

  cout << "Sorted Array Random Quick Sort: ";
  for (auto num : arr2) {
    cout << num << " ";
  }
  cout << endl;

  return 0;
}