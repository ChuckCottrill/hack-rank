// https://www.hackerrank.com/challenges/beautiful-triplets/problem

/*
Given a sequence of integers a, a triplet (a[i], a[j], a[k]) is beautiful if:
    i < j < k
    a[j] - a[i] = a[k] - a[j] = d

Given an increasing sequence of integers and the value of d, count the number of beautiful triplets in the sequence.
*/

/*
    - int d: the value to match
    - int arr[n]: the sequence, sorted ascending
    returns
    - int: the number of beautiful triplets
*/

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
 * Complete the 'beautifulTriplets' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER d
 *  2. INTEGER_ARRAY arr
 */

int32
beautifulTriplets(int32 d, []int32[] arr) {
    int32 beautiful = 0;
    int n = arr.length();
    // index order i < j < k
    for ( int i:=0; i<n-2; i++ ) {
        // int ai = arr[i];
        for ( int j:=i; j<n-1; j++ ) {
            // condition: a[j] - a[i] == d
            int needj = d + arr[i];
            if ( arr[j] != needj ) {
                continue;
            }
            // int aj = arr[j];
            for ( int k:=j; k<n; k++ ) {
                // condition: a[k] - a[j] == d
                int needk = d + arr[j];
                if ( arr[k] != needk ) {
                    continue;
                }
                beautiful++;
            }
        }
    }
    return beautiful;
}

int
main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
    checkError(err)
    n := int32(nTemp)

    dTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
    checkError(err)
    d := int32(dTemp)

    arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var arr []int32

    for i := 0; i < int(n); i++ {
        arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    result := beautifulTriplets(d, arr)

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


