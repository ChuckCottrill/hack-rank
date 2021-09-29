// https://www.hackerrank.com/challenges/acm-icpc-team/problem

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
 * Complete the 'acmTeam' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts STRING_ARRAY topic as parameter.
 */

func acmTeam(topic []string) []int32 {
    // Write your code here
    var n int32 = int32(len(topic))
    if n == 0 {
        return []int32{ 0, 0 }
    }
    var m int32 = int32(len(topic[0]))
    var covered int32 = 0
    var teams int32 = 0
    for idx:=0; idx<int(n); idx++ {
        si := topic[idx]
        for jdx:=idx+1; jdx<int(n); jdx++ {
            sj := topic[jdx]
            var topiccount int32 = 0
            for sdx:=0; sdx<int(m); sdx++ {
                if si[sdx] == '1' || sj[sdx] == '1' {
                    topiccount++
                }
            }
            if topiccount == covered {
                teams++
            } else if topiccount > covered {
                covered = topiccount
                teams = 1
            }
        }
    }
    var result []int32 = []int32{ covered, teams }
    return result
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
    checkError(err)
    n := int32(nTemp)

    // mTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
    _, err = strconv.ParseInt(firstMultipleInput[1], 10, 64)
    checkError(err)
    // m := int32(mTemp)

    var topic []string

    for i := 0; i < int(n); i++ {
        topicItem := readLine(reader)
        topic = append(topic, topicItem)
    }

    result := acmTeam(topic)

    for i, resultItem := range result {
        fmt.Fprintf(writer, "%d", resultItem)

        if i != len(result) - 1 {
            fmt.Fprintf(writer, "\n")
        }
    }

    fmt.Fprintf(writer, "\n")

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

