
// https://leetcode.com/problems/valid-number/

class Solution {
public:
    bool isNumber(string s) {
        bool digitsFound = false;
        bool decimalFound = false;
        bool expFound = false;
        int sign = 0;
        int expSign = 0;

        int state = START;

        for ( int idx = 0; idx < s.length(); idx++ ) {
            switch(state) {
                case START : {
                    if ( ch == '+' ) {
                        sign = 1;
                        state = INTEGER;
                    }
                    if ( ch == '-' ) {
                        sign = -1;
                        state = INTEGER;
                    }
                    if ( ch == '.' ) {
                        sign = -1;
                        state = DECIMAL;
                    }
                    if ( tolower(ch) == 'e' ) {
                        state = ERROR;
                    }
                    if ( isdigit(ch) ) {
                        state = INTEGER;
                    }
                }
                case SIGN : {
                }
                case INTEGER : {
                    if ( isdigit(ch) ) {
                        state = INTEGER;
                    }
                    if ( ch == '.' ) {
                        state = DECIMAL;
                    }
                }
                case DECIMAL: {
                    if ( isdigit(ch) ) {
                        state = INTEGER;
                    }

                }
                case SIGN : {
                }
            }
        }

        if ( isdigit(ch) ) {
        }
        else if ( ch == '.') {
            next = ch;
            if ( isdigit(next) ) {
            }
        }
    }

    string digitStr(string s) {
        if ( isdigit(ch) ) {
            while ( isdigit(ch) ) {
            }
        }
    }

};

