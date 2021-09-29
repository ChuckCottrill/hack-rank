

type Stack []int

class Stack
{
private:
    stack<int> c;

public:
    // empty: check if stack is empty
    bool empty() {
        return this.c.length() == 0
    }

    // push value onto the stack
    void push(int v) {
        this.c.append(v) // Simply append the new value to the end of the stack
    }

    // Remove and return top element of stack. Return false if stack is empty.
    int pop() {
        if ( this.empty() ) {
            return -1; // false
        }
        int tip = this.pop(); // get tip from stack
        return tip;
    }

    // remove tip of stack, replace
    int peek() {
        if ( this.empty() ) {
            return -1; // false
        }
        int tip = this.top(); // get tip from stack
        return tip;
    }
}

int longestValidParentheses(string s) {
    std::stack<int> stack;
    stack.push(-1);
    int maxans = 0;
    // for ( auto idx, ch : s )
    for ( int idx = 0; idx < s.length(); idx++ ) {
        int ch = s[idx];
        switch ( ch ) {
            case '(': {
                stack.push(idx)
                break;
            }
            case ')': {
                if (! stack.empty() ) {
                    stack.pop();
                }
                if ( stack.empty() ) {   
                    stack.push(idx);
                } else {
                    // if (! stack.empty() ) {
                    int tip = stack.top();
                    maxans = max( maxans, (idx - tip));
                    // }
                }
                break;
            }
        }
    }
    return maxans;
}

