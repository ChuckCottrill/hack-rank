// https://www.hackerrank.com/challenges/the-time-in-words/problem

package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the 'timeInWords' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER h
 *  2. INTEGER m
 */

func timeInWords(h int32, m int32) string {
    // Write your code here
    var hourText map[int32]string = map[int32]string{
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
    }
    var minuteText map[int32]string = map[int32]string{
        0: "oh",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twent four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eight",
        29: "twenty nine",
        30: "thirty",
    }
    var hs string
    var ms string
    var desc string

    if m == 0 {
        hs = hourText[h]
        ms = ""
        desc = hs + " o' clock"
    } else if m == 1 {
        hs = hourText[h] // + " o' clock"
        ms = minuteText[m] + " minute past "
        desc = ms + hs
    } else if m == 15 {
        hs = hourText[h] // + " o' clock"
        ms = "quarter past "
        desc = ms + hs
    } else if m < 30 {
        hs = hourText[h] // + " o' clock"
        ms = minuteText[m] + " minutes past "
        desc = ms + hs
    } else if m == 30 {
        hs = hourText[h] // + " o' clock"
        ms = "half past "
        desc = ms + hs
    } else if m == 45 {
        h = (h+1)%12
        hs = hourText[h] // + " o' clock"
        ms = "quarter to "
        desc = ms + hs
    } else if m == 59 {
        h = (h+1)%12
        m = 60 - m
        hs = hourText[h] // + " o' clock"
        ms = minuteText[m] + " minute to "
        desc = ms + hs

    } else if m > 30 {
        h = (h+1)%12
        m = 60 - m
        hs = hourText[h] // + " o' clock"
        ms = minuteText[m] + " minutes to "
        desc = ms + hs
    }
    return desc
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    hTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    h := int32(hTemp)

    mTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    m := int32(mTemp)

    result := timeInWords(h, m)

    fmt.Fprintf(writer, "%s\n", result)

    writer.Flush()
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

