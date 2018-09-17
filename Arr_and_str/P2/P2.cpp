#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool checkPerm(string& str1, string& str2){
	
		
	cout << str1 << " " << str2 <<endl;
	
	if (str1.length() != str2.length()) return false;
	
	int char_count[128];		
	for(int i = 0; i < str1.length(); i++)
		
	
	return true;
}


int main(){
	
	vector<string> vec1 = {"jackson", "sonjack"};
	vector<string> vec2 = {"jackson", "notperm"};

	cout << checkPerm(vec1.at(0), vec1.at(1)) << endl;
	cout << checkPerm(vec2.at(0), vec2.at(1)) << endl;

	return 0;
}
