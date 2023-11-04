class Solution:
    def binaryArray(self, n, arr):
        self.res = []
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return[1 if (arr[1]%2 if idx == 0 else arr[0] %2) == 0 else 0 for idx, ele in enumerate(arr)]
        else:
            for idx, ele in enumerate(arr):
                if idx == 0:
                     self.res.append(1) if sum(arr[1:])%2 == 0 else self.res.append(0)
                elif idx == n-1:
                     self.res.append(1) if sum(arr[0:idx])%2 == 0 else self.res.append(0)
                else:
                     self.res.append(1) if (sum(arr[0:idx]) + sum(arr[idx+1:]))%2 == 0 else self.res.append(0)

        return self.res
obj = Solution()
print(obj.binaryArray(4, [1,32,7,9]))