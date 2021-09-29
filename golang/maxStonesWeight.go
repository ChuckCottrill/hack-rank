

func lastStoneWeightII(stones []int) int {

    var N = len(stones)
    var s int = 0
    for i:=0; i<N; i++ {
        s += stones[i];
    }

    var maxs int = 0
    var dp []bool = make([]bool,s/2+1)
    dp[0] = true
    for i:=0; i<N; i++ {
        for j:=s/2; j>=stones[i]; j--{
            dp[j] = dp[j] || dp[j-stones[i]]
            if dp[j] {
                // maxs = max(maxs,j)
                if j > maxs {
                    maxs = j
                }
            }
        }
    }
    return s - 2*maxs
}


func lastStoneWeight(weights []int32) int32 {
    //  var N = len(weights)
     var s int64 = 0 // total weight
     var stoneW map[int32]int32 = make(map[int32]int32)
     var K map[int32]int32 = make(map[int32]int32)
     // what is total weights
     for _, stone := range weights {
         s = s + int64(stone)
         stoneW[stone] = stone
     }
     
     var maxW int32 = 0
     for _, stone := range weights{
         for _, stone2 := range stoneW {
             if _, ok := K[stone2]; !ok {
                 K[stone2] = K[stone]
             }
             if _,ok := K[stone2]; ok {
                 if stone2 > maxW {
                     maxW = int32(stone2)
                 }
             }
         }
     }
     return int32(s - int64(2*maxW))
}



