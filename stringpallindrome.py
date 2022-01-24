class nk(object):
    @classmethod
    def checkPalindrome(cls, input1):
        s=input1
        n=len(s)
        s = list(s)
        count = 0
        ans = True
        for i in range(n // 2):
            left = i
            right = n - left - 1
            while left < right:
                if s[left] == s[right]:
                    break
                else:
                    right -= 1
            if left == right:
                ans = False
                break
            else:
                for j in range(right, n - left - 1):
                    (s[j], s[j + 1]) = (s[j + 1], s[j])
                    count += 1
        if ans:
            return (count)
        else:
            return -1








if __name__ == "__main__":
    str = "abccaa"
    str = "ntiin"
    str = "naaman"

    nkk = nk()
    print(nkk.checkPalindrome(str))
