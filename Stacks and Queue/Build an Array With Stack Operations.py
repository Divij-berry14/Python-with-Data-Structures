class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
      final_arr = []
      temp = 1
      last = target[-1]
      for i in range(1, last+1):
          if i in target:
              final_arr.append("Push")
          else:
              final_arr.append("Push")
              final_arr.append("Pop")
          temp += 1

            # print(final_arr)
      return final_arr

target = [2,3,4]
n = 4
s = Solution()
print(s.buildArray(target, n))
