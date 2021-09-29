// https://www.hackerrank.com/challenges/encryption/problem


/*
English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

    floor(sqrt(L)) <= row <= column <= ceil(sqrt(L))
    where rows * columns >= L
*/

package main

import (
    "bufio"
    "fmt"
    "io"
    "math"
    "os"
    "strings"
)

/*
 * Complete the 'encryption' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

func encryption(s string) string {
    // remove spaces " "
    var nospaces string = strings.Replace(s," ","",-1)
    var L int = len(nospaces)
    var sL int = int(math.Sqrt(float64(L)))
    // fmt.Printf("L:%d, /L:%d\n",L,sL)
    var rows int = sL
    var columns int = sL
    if L > rows*columns {
        columns++
    }
    if L > rows*columns {
        rows++
    }
    var erows int = columns
    // var ecolumns int = rows
    // fmt.Printf("rows:%d, columns:%d\n",rows,columns)
    // fmt.Println("str:",nospaces)
    var matrix []string = make([]string,rows)
    var encode []string = make([]string,erows)
    var row int = 0
    var col int = 0
    for idx:=0; idx<L; idx++ {
        row = idx/columns
        // col = idx%rows
        matrix[row] += string(nospaces[idx:idx+1])
    }
    // fmt.Println("matrix:",strings.Join(matrix," "))
    // fmt.Printf("erows:%d, ecolumns:%d\n",erows,ecolumns)
    for col=0; col<columns; col++ {
        for row=0; row<rows; row++ {
            if row < len(matrix) && col < len(matrix[row]) {
                encode[col] += string(matrix[row][col])
            }
        }
    }
    // fmt.Println("encode:",strings.Join(encode," "))

    return strings.Join(encode," ")
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    s := readLine(reader)

    result := encryption(s)

    fmt.Fprintf(writer, "%s\n", result)

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

