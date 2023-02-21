#include <iostream>
#include <cctype>

using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(),s.end(),s.begin(), :: tolower);
        cout << s << endl;
        string newstr = "";
        for(int i = 0; i < s.size(); i++){
            if( iswalnum(s[i]) ){
                newstr.push_back(s[i]);
            }
        }
        cout<<newstr<<endl;
        if(newstr =="")
            return true;

        for(int left = 0, right = newstr.size()-1; left < right; left++,right--){
            if(newstr[left] != newstr[right])
                return false;
        }

        return true;
        
    }
};