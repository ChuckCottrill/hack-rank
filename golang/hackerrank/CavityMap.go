// https://www.hackerrank.com/challenges/cavity-map/problem

package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

func cavity(cell int, x []int) bool {
    return (cell>x[0]) && (cell>x[1]) && (cell>x[2]) && (cell>x[3])
}

/*
 * Complete the 'cavityMap' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts STRING_ARRAY grid as parameter.
 */

func cavityMap(grid []string) []string {
    // Write your code here
    var n int = len(grid)
    var result []string = make([]string,0)
    if n <= 2 {
        return grid
    }
    var x[][]int = make([][]int,n)
    for r:=0; r<n; r++ {
        x[r] = make([]int, n)
        for c:=0; c<n; c++ {
            digit := grid[r][c:c+1]
            x[r][c],_ = strconv.Atoi(digit)
        }
    }
    result = append(result, grid[0])
    for r:=1; r<n-1; r++ {
        row := grid[r][0:01]
        for c:=1; c<n-1; c++ {
            digit := grid[r][c:c+1]
            cell := x[r][c]
            if cavity(cell, []int{x[r-1][c], x[r][c-1], x[r][c+1], x[r+1][c]}) {
                row += "X"
            } else {
                row += digit
            }
        }
        row += grid[r][n-1:n]
        result = append(result,row)
    }
    result = append(result, grid[n-1])
    return result
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

    var grid []string

    for i := 0; i < int(n); i++ {
        gridItem := readLine(reader)
        grid = append(grid, gridItem)
    }

    result := cavityMap(grid)

    for i, resultItem := range result {
        fmt.Fprintf(writer, "%s", resultItem)

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

