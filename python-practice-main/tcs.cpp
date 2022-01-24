#include<iostream>
using namespace std;
class PM{
public: void designation() {cout << "PM";}
};
class CEO
{
public: CEO() 
  {    pmPtr = new PM;   }
 PM *operator -> () 
 {    return pmPtr;   }
 void designation() 
 {  cout << "CEO";}
 private: PM *pmPtr;
};
int main() {
CEO*ceoPtr;
ceoPtr = new CEO;
ceoPtr ->designation();
delete ceoPtr;
} 