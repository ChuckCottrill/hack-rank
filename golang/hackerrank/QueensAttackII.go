// https://www.hackerrank.com/challenges/queens-attack-2/problem

/*
You are given a square chess board with one queen and a number of obstacles placed on it.
Determine how many squares the queen can attack.

A queen is standing on an n x n chessboard.
The chess board's rows are numbered from 1 to n, going from bottom to top.
The columns are numbered from 1 to n, going from left to right.
Each square is referenced by a tuple (r,c), describing the row, r, and the column, c, where the square is located.

The queen is standing at position (r_q, c_q).
In a single move, the queen can attack any square in any of the eight directions
(left, right, up, down, and the four diagonals).
In the diagram below, the green circles denote all the cells the queen can attack from:

Complete the queensAttack function in the editor below.

queensAttack has the following parameters:
- int n: the number of rows and columns in the board
- int k: the number of obstacles on the board
- int r_q: the row number of the queen's position
- int c_q: the column number of the queen's position
- int obstacles[k][2]: each element is an array of  integers, the row and column of an obstacle
return
- int: the number of squares the queen can attack

constraints
0 <= n <= 10^5
0 <= k <= 10^5
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

type RowCol struct {
    r int32
    c int32
}

func buildBoard(n int32, obstacles [][]int32) map[RowCol]int32 {
    var result map[RowCol]int32 = make(map[RowCol]int32)
    for _, pair := range obstacles {
        var rc RowCol = RowCol{ r: pair[0]-1, c: pair[1]-1, }
        // fmt.Printf("r:%d,c:%d\n",rc.r,rc.c)
        result[rc] = 1
    }
    return result
}

func isBoard(n int32, r int32, c int32, blocked map[RowCol]int32) bool {
    if ! ( (r>=0) && (r<n) ) {
        return false
    }
    if ! ( (c>=0) && (c<n) ) {
        return false
    }
    // fmt.Printf("r:%d,c:%d\n",r,c)
    var rc RowCol = RowCol{ r: r, c: c, }
    if _,ok := blocked[rc]; ok {
        // fmt.Printf("[%d,%d]\n",r,c)
        return false
    }
    return true
}

/*
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 * obstacles 
 */

func queensAttack(n int32, k int32, r_q int32, c_q int32, obstacles [][]int32) int32 {
    // Write your code here
    var count int32 = 0
    if n < 2 {
        return 0
    }
    var r int32 // row index
    var c int32 // column index
    var rq int32 = r_q-1
    var cq int32 = c_q-1
    var blocked map[RowCol]int32 = buildBoard(n, obstacles)
    // run down column
    // var dir int32 = -1
    for c=cq-1; isBoard(n,rq,c,blocked); c-- {
        // if obstacles[r_q][c]==0 { break }
        count++
    }
    // dir = +1
    for c=cq+1; isBoard(n,rq,c,blocked); c++ {
        // if obstacles[r_q][c]==0 { break }
        count++
    }
    // run across row
    for r=rq-1; isBoard(n,r,cq,blocked); r-- {
        // if obstacles[r][c_q]==0 { break }
        count++
    }
    for r=rq+1; isBoard(n,r,cq,blocked); r++ {
        // if obstacles[r][c_q]==0 { break }
        count++
    }
    // diagonal positive slope (ascending)
    c=cq-1
    for r=rq-1; isBoard(n,r,c,blocked); r-- {
        // if obstacles[r][c]==0 { break }
        count++
        c--
    }
    c=cq+1
    for r=rq+1; isBoard(n,r,c,blocked); r++ {
        // if obstacles[r][c]==0 { break }
        count++
        c++
    }
    // diagonal negative slope (descending)
    c=cq-1
    for r=rq+1; isBoard(n,r,c,blocked); r++ {
        // if obstacles[r][c]==0 { break }
        count++
        c--
    }
    c=cq+1
    for r=rq-1; isBoard(n,r,c,blocked); r-- {
        // if obstacles[r][c]==0 { break }
        count++
        c++
    }
    return count
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

    secondMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    r_qTemp, err := strconv.ParseInt(secondMultipleInput[0], 10, 64)
    checkError(err)
    r_q := int32(r_qTemp)

    c_qTemp, err := strconv.ParseInt(secondMultipleInput[1], 10, 64)
    checkError(err)
    c_q := int32(c_qTemp)

    var obstacles [][]int32
    for i := 0; i < int(k); i++ {
        obstaclesRowTemp := strings.Split(strings.TrimRight(readLine(reader)," \t\r\n"), " ")

        var obstaclesRow []int32
        for _, obstaclesRowItem := range obstaclesRowTemp {
            obstaclesItemTemp, err := strconv.ParseInt(obstaclesRowItem, 10, 64)
            checkError(err)
            obstaclesItem := int32(obstaclesItemTemp)
            obstaclesRow = append(obstaclesRow, obstaclesItem)
        }

        if len(obstaclesRow) != 2 {
            panic("Bad input")
        }

        obstacles = append(obstacles, obstaclesRow)
    }

    result := queensAttack(n, k, r_q, c_q, obstacles)

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

