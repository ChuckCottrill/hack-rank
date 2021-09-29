// https://www.hackerrank.com/challenges/flatland-space-stations/problem

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

// Complete the flatlandSpaceStations function below.
func flatlandSpaceStations(n int32, c []int32) int32 {
    // var n int = len(c)
    var dist int32 = 0
    
    if len(c) == 0 {
        return n
    }
    
    // sort ascending
    sort.Slice(c, func(i,j int) bool {
        return c[i] < c[j]
    })
    fmt.Printf("%d: %v\n",n,c)
    dist = c[0]
    fmt.Printf("c[0]:%d\n",dist)
    if n-1 - c[len(c)-1] > dist {
        dist = n-1 - c[len(c)-1]
        fmt.Printf("c[%d]:%d\n",len(c)-1,dist)
    }

    for city:=1; city<len(c); city++ {
        gap:=int(c[city] - c[city-1])-1
        fmt.Printf("gap:%d\n",gap-gap/2)
        if int32(gap - gap/2) > dist {
            dist = int32(gap - gap/2)
        }
    }
    return dist
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 1024 * 1024)

    nm := strings.Split(readLine(reader), " ")

    nTemp, err := strconv.ParseInt(nm[0], 10, 64)
    checkError(err)
    n := int32(nTemp)

    mTemp, err := strconv.ParseInt(nm[1], 10, 64)
    checkError(err)
    m := int32(mTemp)

    cTemp := strings.Split(readLine(reader), " ")

    var c []int32

    for i := 0; i < int(m); i++ {
        cItemTemp, err := strconv.ParseInt(cTemp[i], 10, 64)
        checkError(err)
        cItem := int32(cItemTemp)
        c = append(c, cItem)
    }

    result := flatlandSpaceStations(n, c)

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

