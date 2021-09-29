
type Stack []int

// IsEmpty: check if stack is empty
func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

// Push a new value onto the stack
func (s *Stack) Push(v int) {
	*s = append(*s, v) // Simply append the new value to the end of the stack
}

// Remove and return top element of stack. Return false if stack is empty.
func (s *Stack) Pop() (int, bool) {
	if s.IsEmpty() {
		return -1, false
	}
    index := len(*s) - 1 // Get the index of the top most element.
    element := (*s)[index] // Index into the slice and obtain the element.
    *s = (*s)[:index] // Remove it from the stack by slicing it off.
    return element, true
}

// Remove and return top element of stack. Return false if stack is empty.
func (s *Stack) Peek() (int, bool) {
	if s.IsEmpty() {
		return -1, false
	}
    last := len(*s) - 1 // Get the index of the top most element.
    element := (*s)[last] // Index into the slice and obtain the element.
    return element, true
}

func longestValidParentheses(s string) int {
    var maxans int = 0;
    var stack Stack
    stack.Push(-1)
    for idx := 0; idx < len(s); idx++ {
        switch ch := s[idx]; ch {
            case '(':
                stack.Push(idx)
            case ')':
                stack.Pop()
                if stack.IsEmpty() {   
                    stack.Push(idx)
                } else {
                    tip, ok := stack.Peek()
                    if ok && (idx - tip) > maxans { maxans = (idx - tip) }
                }
        }
    }
    return maxans;
}

