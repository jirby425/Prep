#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[]){

  if (argc < 2){
    cout << "no input file provided, please pass in as command line argument" << endl;
    return 0;
  }

  fstream file;
  string input;
  string filePath = argv[1];

  file.open(filePath);
  if(file.is_open()){
    while (file >> input){
        cout << input << endl;
    }
  }
  else{
    cout << "file: " << filePath << " failed to open" << endl;
  }
return 0;
}
