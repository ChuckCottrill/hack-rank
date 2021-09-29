

Revenue Milestones

### see: https://www.schwid.com/posts/revenue-milestones/

'''
Revenue Milestones
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones.
Given an array of the revenue on each day, and an array of milestones Facebook wants to reach,
return an array containing the days on which Facebook reached every milestone.
Signature
int[] getMilestoneDays(int[] revenues, int[] milestones)
Input
revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
Output
Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.
Example
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
Explanation
On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue.
'''

def getMilestoneDays(revenues, milestones):
    """ getMilestoneDays
        return int[]
        int[] revenues
        int[] milestones
    """
    n, k = len(revenues), len(milestones)
    result = [0 for x in milestones]
    print(result)
    milestones.sort()
    revenuetotal = [ x for x in revenues ]
    #
    kx = 0 # milestones index
    for rx in range(len(revenues)):
        if rx > 0:
            prev = revenuetotal[rx-1]
        else:
            prev = 0
        revenuetotal[rx] += prev
        # if kx < k and revenuetotal[rx] >= milestones[kx]:
        while kx < k and revenuetotal[rx] >= milestones[kx]:
            print("revenue[",rx+1,"]:",revenuetotal[rx])
            print("result[",kx,"]:",result[kx])
            result[kx] = rx+1
            kx += 1
    # print(result)
    return result

revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
result = getMilestoneDays(revenues, milestones)
print("result:",result)
print("expected:",output)

revenues = [700, 800, 600, 400, 600, 700]
milestones = [3100, 2200, 800, 2100, 1000]
output = [2,2,3,4,5]
result = getMilestoneDays(revenues, milestones)
print("result:",result)
print("expected:",output)



'''
Golang version:
package main

import "fmt"
import "sort"

type PrList []int

func (p PrList) Len() int           { return len(p) >> 1 }
func (p PrList) Less(i, j int) bool { return p[i << 1] < p[j << 1] }
func (p PrList) Swap(i, j int)      { p[i << 1], p[j << 1],  p[(i << 1)+1], p[(j << 1)+1]  = p[j << 1], p[i << 1], p[(j << 1)+1], p[(i << 1)+1] }

func getMilestoneDays(revenues []int, milestones []int) []int {

  n, k := len(revenues), len(milestones)
  out := make([]int, k)

  p := make([]int, k << 1)
  for i := 0; i < k; i++ {
    p[i << 1] = milestones[i]
    p[(i << 1) + 1] = i
  }

  sort.Sort(PrList(p))

  sum := 0
  for i, j := 0, 0; j < k; {
    if sum >= p[j << 1] {
      out[p[(j << 1)+1]] = i
      j++
    } else if i < n {
      sum += revenues[i]
      i++
    } else {
      break
    }
  }
	return out;
}

func main() {

  revenues := []int {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
  milestones := []int {100, 200, 500}
  expected := []int {4, 6, 10}
  output := getMilestoneDays(revenues, milestones)
  fmt.Printf("Test#1 expected=%v, actual=%v\n", expected, output)

  revenues = []int {700, 800, 600, 400, 600, 700}
  milestones = []int {3100, 2200, 800, 2100, 1000}
  expected = []int {5, 4, 2, 3, 2}
  output = getMilestoneDays(revenues, milestones)

  fmt.Printf("Test#2 expected=%v, actual=%v\n", expected, output)

}
'''

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  revenues_1 = [100, 200, 300, 400, 500]
  milestones_1 = [300, 800, 1000, 1400]
  expected_1 = [2, 4, 4, 5]
  output_1 = getMilestoneDays(revenues_1, milestones_1)
  check(expected_1, output_1)

  revenues_2 = [700, 800, 600, 400, 600, 700]
  milestones_2 = [3100, 2200, 800, 2100, 1000] 
  expected_2 = [5, 4, 2, 3, 2]
  output_2 = getMilestoneDays(revenues_2, milestones_2)
  check(expected_2, output_2)

  # Add your own test cases here


