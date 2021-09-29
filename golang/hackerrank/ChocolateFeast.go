// https://www.hackerrank.com/challenges/chocolate-feast/problem

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
 * Complete the 'chocolateFeast' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n: Bobby's initial amount of money
 *  2. INTEGER c: the cost of a chocolate bar
 *  3. INTEGER m: the number of wrappers he can turn in for a free bar
 * return
 * int: number of chocolate bars, taking full advantage of the promotion
  */

func chocolateFeast(n int32, c int32, m int32) int32 {
    // Write your code here
    var eat int32 = 0
    var bars int32 = 0
    var wrappers int32 = 0
    bars = n/c
    c -= (n/c)*c
    for bars > 0 {
        eat += bars
        wrappers += bars
        bars = wrappers/m
        wrappers = wrappers%m
    }
    return eat
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    tTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    t := int32(tTemp)

    for tItr := 0; tItr < int(t); tItr++ {
        firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

        nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
        checkError(err)
        n := int32(nTemp)

        cTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
        checkError(err)
        c := int32(cTemp)

        mTemp, err := strconv.ParseInt(firstMultipleInput[2], 10, 64)
        checkError(err)
        m := int32(mTemp)

        result := chocolateFeast(n, c, m)

        fmt.Fprintf(writer, "%d\n", result)
    }

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

