// https://www.hackerrank.com/challenges/kaprekar-numbers/problem

/*
A modified Kaprekar number is a positive whole number with a special property.
If you square it, then split the number into two integers and sum those integers,
you have the same value you started with.

Consider a positive whole number n, with d, digits.
We square n to arrive at a number that is either (2 x d) digits long or (2 x d) digits long.
Split the string representation of the square into two parts, l and r.
The right hand part r must be d digits long.
The left is the remaining substring.
Convert those two substrings back to integers, add them and see if you get.
*/

package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

func isKaprekar(x int32) (int32,bool) {
    number := strconv.Itoa(int(x)*int(x))
    n := len(number)
    digits := n/2
    s := number[0:digits]
    var left int64 = 0
    var right int64 = 0
    if len(s) > 0 {
        left,_ = strconv.ParseInt(s, 10, 64)
        // if err != nil {
        //     left = 0
        // }
    }
    s = number[digits:]
    if len(s) > 0 {
        right,_ = strconv.ParseInt(s, 10, 64)
        // if err != nil {
        //     right = 0
        // }
    }
    if int(left+right) == int(x) {
        return x, true
    }
    return 0, false
}
/*
 * Complete the 'kaprekarNumbers' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER p: the lower limit
 *  2. INTEGER q: the upper limit
 */

func kaprekarNumbers(p int32, q int32) {
    // Write your code here
    var kaprekar []string = make([]string,0)
    for x:=p; x<=q; x++ {
        if _,ok := isKaprekar(x); ok {
            kaprekar = append(kaprekar,strconv.Itoa(int(x)))
        }
    }
    if len(kaprekar) == 0 {
        fmt.Println("INVALID RANGE")
    } else {
        fmt.Println(strings.Join(kaprekar," "))
    }
    return
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    pTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    p := int32(pTemp)

    qTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    q := int32(qTemp)

    kaprekarNumbers(p, q)
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}

