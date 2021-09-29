

# https://leetcode.com/problems/last-stone-weight/
/*
Last Stone Weight II: A Leetcode Problem
https://joseiciano.medium.com/last-stone-weight-ii-a-leetcode-problem-a37f49e55d13

We have a collection of rocks, each rock has a positive integer weight.
Each turn, we choose any two rocks and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left. Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)
*/

// basically knapsack (0-1) in disguise
// sum of stone weights = bag weight = S
// stones are values []

// 2D
// for each stone from 1 to n-1
//   for each weitht j from 1 to S/2

func lastStoneWeightII(stones int[]) int {

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


