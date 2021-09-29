// https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "sort"
    "strconv"
    "strings"
)

/*
 * Complete the 'organizingContainers' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts 2D_INTEGER_ARRAY container as parameter.
 */

func organizingContainers(container [][]int32) string {
    var n int32 = int32(len(container))
    if n < 1 {
        return "Impossible"
    }
    var result string = "Possible"
    var balls []int32 = make([]int32, n) // number balls each container
    var types []int32 = make([]int32, n) // number of balls each type
    for i,row := range container {
        for j,_ := range row {
            balls[i] += container[i][j]
            types[j] += container[i][j]
        }
    }
    
    // sort ascending
    sort.Slice(balls, func(i, j int) bool {
        return balls[i] < balls[j]
    })
    sort.Slice(types, func(i, j int) bool {
        return types[i] < types[j]
    })
    for idx:=0; idx<int(n); idx++ {
        if balls[idx] != types[idx] {
            result = "Impossible"
            break
        }
    }

    return result
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    qTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    q := int32(qTemp)

    for qItr := 0; qItr < int(q); qItr++ {
        nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
        checkError(err)
        n := int32(nTemp)

        var container [][]int32
        for i := 0; i < int(n); i++ {
            containerRowTemp := strings.Split(strings.TrimRight(readLine(reader)," \t\r\n"), " ")

            var containerRow []int32
            for _, containerRowItem := range containerRowTemp {
                containerItemTemp, err := strconv.ParseInt(containerRowItem, 10, 64)
                checkError(err)
                containerItem := int32(containerItemTemp)
                containerRow = append(containerRow, containerItem)
            }

            if len(containerRow) != int(n) {
                panic("Bad input")
            }

            container = append(container, containerRow)
        }

        result := organizingContainers(container)

        fmt.Fprintf(writer, "%s\n", result)
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

