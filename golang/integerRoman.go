
// https://leetcode.com/problems/integer-to-roman/

func intToRoman(int num) string {
    var romani = []string { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" }
    var values = []int {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 }
    var encoded string = ""

    for idx := 0; num > 0; {
        if num < values[idx] {
            idx++
        } else {
            encoded += romani[idx] // append roman numeral(s)
            num -= values[idx]
        }
    }
    return encoded
}

func intToRomanAlt2(int num) string {
    var romani = map[int]string {
            1000: "M",
             900: "CM",
             500: "D",
             400: "CD",
             100: "C",
              90: "XC",
              50: "L",
              40: "XL",
              10: "X",
               9: "IX",
               5: "V",
               4: "IV",
               1: "I",
        }
    var values []int = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 }
    var encoded string = ""

    for idx := 0; num > 0; {
        if num < values[idx] {
            idx++
        } else {
            encoded += romani[ values[idx] ] // append roman numeral(s)
            num -= values[idx]
        }
    }
    return encoded
}

func intToRomanAlt(int num) string {
    var digit1    []string = {"","I","II","III","IV","V","VI","VII","VIII","IX"}
    var digit10   []string = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"}
    var digit100  []string = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"}
    var digit1000 []string = {"","M","MM","MMM"}

    return digit1000[num/1000] + digit100[(num%1000)/100] + digit10[(num%100)/10] + digit1[num%10]
}

