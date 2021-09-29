
/*

sort.Slice(members, func(i, j int) bool {
    if members[i].FirstName != members[j].FirstName {
        return members[i].FirstName < members[j].FirstName
    }
    return members[i].LastName < members[j].LastName
})


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
 * Complete the 'getUnallottedUsers' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. 2D_INTEGER_ARRAY bids
 *  2. INTEGER totalShares
 *
 * If you want to import any other packages from the standard library, just add import statements in this section.
 */

func getUnallottedUsers(bids [][]int32, totalShares int32) []int32 {

}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    bidsRows, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)

    bidsColumns, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)

    var bids [][]int32
    for i := 0; i < int(bidsRows); i++ {
        bidsRowTemp := strings.Split(strings.TrimRight(readLine(reader)," \t\r\n"), " ")

        var bidsRow []int32
        for _, bidsRowItem := range bidsRowTemp {
            bidsItemTemp, err := strconv.ParseInt(bidsRowItem, 10, 64)
            checkError(err)
            bidsItem := int32(bidsItemTemp)
            bidsRow = append(bidsRow, bidsItem)
        }

        if len(bidsRow) != int(bidsColumns) {
            panic("Bad input")
        }

        bids = append(bids, bidsRow)
    }

    totalSharesTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    totalShares := int32(totalSharesTemp)

    result := getUnallottedUsers(bids, totalShares)

    for i, resultItem := range result {
        fmt.Fprintf(writer, "%d", resultItem)

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
 * Complete the 'getUnallottedUsers' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. 2D_INTEGER_ARRAY bids
 *  2. INTEGER totalShares
 *
 * If you want to import any other packages from the standard library, just add import statements in this section.
 */

// type Bid struct {
//     User int32;
//     Shares int32;
//     Price int32; // [2]
//     timestamp int32; // [3]
// }

func getUnallottedUsers(bids [][]int32, totalShares int32) []int32 {
    
    // shares each user gets
    var shares map[int32]int32 = make(map[int32]int32)
    // prices
    var prices map[int32]int32 = make(map[int32]int32)
    var pricelist []int32
    for k,bid := range bids {
        shares[bid[0]] = 0
        prices[bid[2]] = bid[2]
        if _,ok 
        userPrice[bid[2]] = 
    }
    for k,_ := range prices {
        pricelist.append(k)
    }
    pricelist = sort.Slice(pricelist, func(i,j int) bool {
        return pricelist[i] > pricelist[j]
    })
    // sort by price, timestamp descending
    var sorted = sort.Slice(bids, func(i,j int) bool {
        if bids[i][2] != bids[j][2] {
            return bids[i][2] > bids[j][2]
        }
        if bids[i][3] != bids[j][3] {
            return bids[i][3] > bids[j][3]
        }
        return bids[i][2] > bids[j][2]
    })
    for _,p := range pricelist {
        for _,u := range useratprice[p] {
            shares[u]++
            totalShares--
    }
    
    
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    bidsRows, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)

    bidsColumns, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)

    var bids [][]int32
    for i := 0; i < int(bidsRows); i++ {
        bidsRowTemp := strings.Split(strings.TrimRight(readLine(reader)," \t\r\n"), " ")

        var bidsRow []int32
        for _, bidsRowItem := range bidsRowTemp {
            bidsItemTemp, err := strconv.ParseInt(bidsRowItem, 10, 64)
            checkError(err)
            bidsItem := int32(bidsItemTemp)
            bidsRow = append(bidsRow, bidsItem)
        }

        if len(bidsRow) != int(bidsColumns) {
            panic("Bad input")
        }

        bids = append(bids, bidsRow)
    }

    totalSharesTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    totalShares := int32(totalSharesTemp)

    result := getUnallottedUsers(bids, totalShares)

    for i, resultItem := range result {
        fmt.Fprintf(writer, "%d", resultItem)

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


