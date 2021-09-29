// https://www.hackerrank.com/challenges/minimum-distances/problem

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
 * Complete the 'minimumDistances' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

func minimumDistances(a []int32) int32 {
    // Write your code 
    var n int = len(a)
    // Initialize best difference variable as one more than the maximum value(n-1) we can achieve
    var best int = n+1
    // map/dictionary to keep track of element value and last known position in the array
    var mp map[int32]int = make(map[int32]int)

    // traverse each element in the array
    for i,x := range a {
        if v,ok := mp[x]; ok {
            dist := i-v
            if dist < best {
                best = dist
                // which = x
            }
        }
        mp[x] = i
    }
    if best > n {
        best = -1
    }
    return int32(best)
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    n := int32(nTemp)

    aTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var a []int32

    for i := 0; i < int(n); i++ {
        aItemTemp, err := strconv.ParseInt(aTemp[i], 10, 64)
        checkError(err)
        aItem := int32(aItemTemp)
        a = append(a, aItem)
    }

    result := minimumDistances(a)

    fmt.Fprintf(writer, "%d\n", result)

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

