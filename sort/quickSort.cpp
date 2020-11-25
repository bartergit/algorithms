#include <bits/stdc++.h>
#include <chrono> 
#include "C:\_git\working-stuff\c++\representation\utility.h"
using namespace std;
using namespace std::chrono; 

int randInt(int min, int max){
	return min + rand() % (max - min);
}

void insertionSortByPtr(int * start, int * end){
	for (int i = 1; i < end - start; i++){
		int x = *(start + i);
		int j = i - 1;
		while (j >= 0 && x < *(start + j)) {
			*(start + j + 1) = *(start + j); 
			j--;
		}
		*(start + j + 1) = x; 	
	}
}

vector<int> insertionSort(vector<int> &array){
	for (int i = 1; i < array.size(); i++){
		int x = array[i];
		int j = i - 1;
		while (j >= 0 && x < array[j]) {
			array[j + 1] = array[j]; 
			j--;
		}
		array[j + 1] = x; 	
	}
	return array;
}

void recursiveStep(int * start, int * end, int k){
	if (start >= end) return;
	if (end - start <= k){
		insertionSortByPtr(start, end);
		return;
	}
	int * i = start; int * j = end;
 	int divider = *j;
	while (i <= j){
		while (*i < divider) i++;
		while (*j > divider) j--;
		if (i <= j) swap(*i++, *j--);
	}
	recursiveStep(start, j, k);
	recursiveStep(i, end, k);
}

vector<int> quickSort(vector<int> &array, int k = 0){
	recursiveStep(&array[0], &array[array.size() - 1], k);
	return array;
}

vector<int> createRandomedVector(int size, int from, int to){
	vector<int> array(size);
	for (int i = 0; i < array.size(); i++){
		array[i] = randInt(from, to);
	}
	return array;
}


int main(){
	srand(time(0));
	int sumDuration = 0;
	const int HOW_MANY_SORTS = 100, ARRAY_SIZE = 10000, VALUE_RANGE = 10000, K_RANGE = 10;
	for (int k = 0; k < K_RANGE; k++){
		auto start = high_resolution_clock::now(); 
		for (int j = 0; j < HOW_MANY_SORTS; j++){
			vector<int> array = createRandomedVector(ARRAY_SIZE, 0, VALUE_RANGE + j % 2);
			quickSort(array, k);
		}
		auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();
		sumDuration += duration;
	}
	cout << sumDuration;
}