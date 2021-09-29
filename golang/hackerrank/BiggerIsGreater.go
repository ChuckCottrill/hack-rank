// https://www.hackerrank.com/challenges/bigger-is-greater/problem

package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

func storune(s string) []rune {
    rns := []rune(s)
    return rns
}
func reverse(s string) string {
    rns := []rune(s)
    for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {
        rns[i], rns[j] = rns[j], rns[i]
    }
    return string(rns)
}

/*
 * Complete the 'biggerIsGreater' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING w as parameter.
 */

func biggerIsGreater(w string) string {

    var n int = len(w)
    var last int = n-1
    // find non-increasing suffix (from right)
    var pivot int = last
    var succ int = last
    for pivot = last; (pivot>0) && (w[pivot-1] >= w[pivot]); {
        pivot--
    }
    if pivot<=0 {
        return "no answer"
    }
    // find pivot successor (from right)
    for succ = last; succ>pivot-1 && w[succ] <= w[pivot-1]; {
        succ--
    }
    // swap successor with pivot
    alt := storune(w)
    alt[pivot-1], alt[succ] = alt[succ], alt[pivot-1]
    // reverse suffix
    rev := reverse(string(alt[pivot:]))
    // prefix
    prefix := string(alt[0:pivot])

    return prefix + rev
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    TTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    T := int32(TTemp)

    for TItr := 0; TItr < int(T); TItr++ {
        w := readLine(reader)

        result := biggerIsGreater(w)

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

