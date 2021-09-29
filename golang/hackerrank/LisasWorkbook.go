// https://www.hackerrank.com/challenges/lisa-workbook/problem

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
 * Complete the 'workbook' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n: total chapters
 *  2. INTEGER k: max problems per page
 *  3. INTEGER_ARRAY arr: total problems per chapter, arr[i] problems in chapter i+1
 */

func workbook(n int32, k int32, arr []int32) int32 {
    // Write your code here
    var special int32 = 0
    // var chapter int32 = 0
    var page int = 1
    var problem int = 1
    
    // var n = len(arr)
    // var chapterPages []int32 = make([]int32, n)
    for _, problems := range arr {
        // pages := (int(problems)+(int(k)-1))/int(k)
        for problem=0; problem<int(problems); problem += int(k) {
            last := problem + int(k)
            if last > int(problems) {
                last = int(problems)
            }
            // is page in range [problem+1, min(problem+k,problems)]
            // fmt.Printf("page:%d, problem:[%d..%d]\n",page,problem+1,last)
            if problem+1 <= page && page <= last {
                // fmt.Printf("chapter:%d, page:%d, problem:%d\n",chapter+1,page,problem+1)
                special++ // (chapter+1, page, problem+1)
            }
            page++
        }
    }
    
    return special
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

    kTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
    checkError(err)
    k := int32(kTemp)

    arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var arr []int32

    for i := 0; i < int(n); i++ {
        arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    result := workbook(n, k, arr)

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

