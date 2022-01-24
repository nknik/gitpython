# # def chrck(strr):
# #     n = len(strr)
# #     count = 0
# #     res = strr[0]
# #     cur_count = 1
# #     for i in range(n):
# #         if i < n - 1 and strr[i] == strr[i + 1]:
# #             cur_count += 1
# #         else:
# #             if cur_count > count:
# #                 count = cur_count
# #                 res = strr[i]
# #             cur_count = 1
# #     return count


# # for i in range(int(input())):
# #     n = int(input())
# #     n = list(input())
# #     nn = int(input())
# #     nn = list(map(int, input().split()))
# #     nk = input().split()
# #     for i in range(len(nn)):
# #         n[nn[i] - 1] = nk[i]
# #         print(chrck("".join(n)), end=" ")
# # # 1
# # # 6
# # # ababcc
# # # 3
# # # 6 3 2
# # # d b a
# # # 1 3 2
# # ============================================
# # s = []
# # r = []
# # q = []
# # nk = input()
# # try:
# #     for i in nk:
# #         if i == "(":
# #             r.append(1)
# #         elif i == "[":
# #             s.append(1)
# #         elif i == "{":
# #             q.append(1)
# #         elif i == ")":
# #             r.pop()
# #         elif i == "]":
# #             s.pop()
# #         elif i == "}":
# #             q.pop()
# #     if r == q == s == []:
# #         print("correct")
# #     else:
# #         print("error")
# # except Exception as e :
# #     print("error")

# # ============================================
# # n=int(input())
# # f=1
# # z=0
# # for i in range(1,n+1):
# #     f=f*i
# # for i in str(f)[::-1]:
# #     if i=='0':
# #         z+=1
# #     else :
# #          break
# # print(z)
# # +++++++++++++++++++++++++++++
# def count(n):
#     der = [0 for i in range(n + 1)]
#     der[1] = 0
#     der[2] = 1
#     for i in range(3, n + 1):
#         der[i] = (i - 1) * (der[i - 1] + der[i - 2])
#     print(der[n])


# n = int(input())
# count(n)