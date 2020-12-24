#include <bits/stdc++.h>
#include <chrono> 
#include "C:\_git\working-stuff\c++\representation\utility.h"
using namespace std;
using namespace std::chrono; 

int randInt(int min, int max){
	return min + rand() % (max - min);
}
int binary_search(vector<int> a, int key){    
	if (a.size() == 0)
        return -1;
    int left = 0;
    int right = a.size() - 1; 
    while (left <= right){
        int mid = (right + left)/2;
        if (a[mid] < key){
            left = mid + 1;
        }
        else if (a[mid] > key) {
            right = mid - 1;
        }
        else {
            return mid;
        }
    }
    return -1;
}

int main(){
	srand(time(0));
	for (int i = 100; i < 110; i++){
		vector<int> v(i);
		for (int j = 0; j < i; j++){
			v[j] = randInt(0,101);
		}
    	sort(v.begin(), v.end());
    	int searched = randInt(0,101);
    	int ind = binary_search(v, searched);
    	if (ind != -1){
    		std::cout << (v[ind] == searched) << "\n";
    	}
	}

}