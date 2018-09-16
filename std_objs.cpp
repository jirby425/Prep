#include <iostream>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>

using namespace std;

void array (int size){
	int arr [size];
	for (int i =0; i < size; i++)
		arr[i] = i;

	for (int i = 0; i < size; i++)
		cout << i << " ";
	cout << endl;
}

void vectorExample (int size){
	vector<int> vec;
	for (int i = 0; i < size; i++)
		vec.push_back(i);

	for(int i = 0; i < size; i++)
		cout << vec.at(i) << " ";

	cout << endl;
}

void dequeExample (int size){
	deque<int> deq;
	for(int i = 0; i < size; i++)
		deq.push_back(i);
	
	for(int i = 0; i < size; i++)
		cout << deq.at(i) << " ";
	
	cout << endl;

	for (int i = 0; i < size; i++)
		deq.push_front(i);

	for (int i = 0; i < size; i++)
		cout << deq.at(i) << " ";	

	cout << endl;
}

void listExample (int size){
	list<int> l;
	for(int i = 0; i < size; i++)
		l.push_front(i);
}

void mapExample (int size){
	map<string, int> m;
	
}


int main(){
	
	cout << "hello world" <<endl;
	array(4);
	vectorExample(5);
	dequeExample(5);
	listExample(4);
	return 0;

}
