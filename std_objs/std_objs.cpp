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

void arrayExample (int size){
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

	for(auto& i : vec)
		cout << i << " ";

	cout << endl;
}

void dequeExample (int size){
	deque<int> deq;
	for(int i = 0; i < size; i++)
		deq.push_back(i);
	
	for(auto& i : deq)
		cout << i << " ";

	deq.clear();
	
	cout << "\n";

	for (int i = 0; i < size; i++)
		deq.push_front(i);

	for (auto& i : deq)
		cout << i << " ";	

	cout << "\n";
}

void listExample (int size){
	list<int> l;
	for(int i = 0; i < size; i++)
		l.push_front(i);
}

void mapExample (int size){
	map<string, int> m = {{"hello", 1}, {"i'm", 2}, {"jackson", 3}};
	
	for(auto& x: m)
		cout << x.first << ": " << x.second << endl;

	cout << m.at("hello") << endl;
}


int main(){
	
	cout << "hello world" <<endl;
	arrayExample(4);
	vectorExample(5);
	dequeExample(6);
	mapExample(2);
	return 0;

}
