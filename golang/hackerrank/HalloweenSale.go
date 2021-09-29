// https://www.hackerrank.com/challenges/halloween-sale/problem

/*
You wish to buy video games from the famous online video game store Mist.

Usually, all games are sold at the same price, p dollars.
However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price.
Specifically, the first game will cost p dollars,
and every subsequent game will cost d, dollars less than the previous one.
This continues until the cost becomes less than or equal to m dollars,
after which every game will cost m dollars.
How many games can you buy during the Halloween Sale?

int p: the price of the first game
int d: the discount from the previous game price
int m: the minimum cost of a game
int s: the starting budget
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
 * Complete the 'howManyGames' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER p
 *  2. INTEGER d
 *  3. INTEGER m
 *  4. INTEGER s
 */

func howManyGames(p int32, d int32, m int32, s int32) int32 {
    // Return the number of games you can buy
    var buy int32 = 0
    if s < p {
        return 0
    }
    var remain int32 = s
    var price int32 = p
    for ; remain >= price; {
        if remain >= price {
            buy++
            remain -= price
        }
        if price > m {
            price -= d
        }
        if price < m {
            price = m
        }
    }
    return buy
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    pTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
    checkError(err)
    p := int32(pTemp)

    dTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
    checkError(err)
    d := int32(dTemp)

    mTemp, err := strconv.ParseInt(firstMultipleInput[2], 10, 64)
    checkError(err)
    m := int32(mTemp)

    sTemp, err := strconv.ParseInt(firstMultipleInput[3], 10, 64)
    checkError(err)
    s := int32(sTemp)

    answer := howManyGames(p, d, m, s)

    fmt.Fprintf(writer, "%d\n", answer)

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

