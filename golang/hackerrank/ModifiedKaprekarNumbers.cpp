// https://www.hackerrank.com/challenges/kaprekar-numbers/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int
isKkaprekar(int x) {
    long long sq = x*x;
    string s = to_string(sq);
    int d = s.size()/2;
    if(d == 0) {
        return (x == sq);
res.push_back(x);
    }
    long long left = stoll(s.substr(0,d));
    long long right = stoll(s.substr(d,s.size()-d));
    return (left + right == i);
}

int
main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    long long p;
    long long q;
    cin>>p;
    cin>>q;

    vector<long long> res;
    for(long long x=p; x<=q; ++x) {
        if ( isKkaprekar(x) ) {
            res.push_back(x);
        }
    }
    if ( res.size()>0 ) {
        for(int x=0; x<res.size(); ++x) {
            cout<<res[x]<<" ";
        }
        cout<<endl;
    }
    else{
        cout<<"INVALID RANGE"<<endl;
    }
    return 0;
}

