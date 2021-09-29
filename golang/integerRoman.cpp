
// https://leetcode.com/problems/integer-to-roman/

class Solution {
public:
    string intToRoman(int num) {

        string romani[] = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        int values[] = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        string encoded = "";

        for ( int idx = 0; num > 0; ) {
            if ( num < values[idx] ) {
                idx++;
            }
            else {
                encoded += romani[idx]; // append roman numeral(s)
                num -= values[idx];
            }
        }
        return encoded;
    }

    string intToRomanAlt2(int num) {

        map<int,string> romani = {
            {1000, "M"},
            { 900, "CM"},
            { 500, "D"},
            { 400, "CD"},
            { 100, "C"},
            {  90, "XC"},
            {  50, "L"},
            {  40, "XL"},
            {  10, "X"},
            {   9, "IX"},
            {   5, "V"},
            {   4, "IV"},
            {   1, "I"}
        };
        int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string encoded = "";

        for ( int idx = 0; num > 0; ) {
            if ( num < values[idx] ) {
                idx++;
            }
            else {
                encoded += romani[ values[idx] ]; // append roman numeral(s)
                num -= values[idx];
            }
        }
        return encoded;
    }

    string intToRomanAlt(int num) {
        string digit1[]    = {"","I","II","III","IV","V","VI","VII","VIII","IX"};
        string digit10[]   = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        string digit100[]  = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        string digit1000[] = {"","M","MM","MMM"};
        
        return digit1000[num/1000] + digit100[(num%1000)/100] + digit10[(num%100)/10] + digit1[num%10];
    }
};

