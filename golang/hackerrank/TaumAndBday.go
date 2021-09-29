// https://www.hackerrank.com/challenges/taum-and-bday/problem

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
 * Complete the 'taumBday' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER b: the number of black gifts
 *  2. INTEGER w: the number of white gifts
 *  3. INTEGER bc: the cost of a black gift
 *  4. INTEGER wc: the cost of a white gift
 *  5. INTEGER z: the cost to convert one color gift to the other color
 */

func taumBday(b int32, w int32, bc int32, wc int32, z int32) int64 {
    // Write your code here
    var cost int64 = 0
    var bb int64 = int64(b) // black buy
    var wb int64 = int64(w) // white buy
    var bcc int64 = int64(bc) // black cost
    var wcc int64 = int64(wc) // white cost
    var bcost int64 = 0
    var wcost int64 = 0
    if bc+z < wc {
        // black+conversion cheaper, buy black and convert to white
        bcc = int64(bc)
        wcc = int64(bc+z)
        bcost = bb*bcc
        wcost = wb*wcc
    } else if wc+z < bc {
        // white+conversion cheaper, buy white and convert to black
        bcc = int64(wc+z)
        wcc = int64(wc)
        bcost = bb*bcc
        wcost = wb*wcc
    } else {
        // same cost, or no cost advantage to conversion
        bcc = int64(bc)
        wcc = int64(wc)
        bcost = bb*bcc
        wcost = wb*wcc
    }
    cost = bcost + wcost
    return cost
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

        bTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
        checkError(err)
        b := int32(bTemp)

        wTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
        checkError(err)
        w := int32(wTemp)

        secondMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

        bcTemp, err := strconv.ParseInt(secondMultipleInput[0], 10, 64)
        checkError(err)
        bc := int32(bcTemp)

        wcTemp, err := strconv.ParseInt(secondMultipleInput[1], 10, 64)
        checkError(err)
        wc := int32(wcTemp)

        zTemp, err := strconv.ParseInt(secondMultipleInput[2], 10, 64)
        checkError(err)
        z := int32(zTemp)

        result := taumBday(b, w, bc, wc, z)

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

