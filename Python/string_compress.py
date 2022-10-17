def solution(s):
    answer = ""
    for i in range(len(s)):
        for j in range(1, len(s)-i):
            if s[i] != s[i+j]:
                if j != 1:
                    answer += str(j)
                answer += s[i+j]
                break
    return len(answer)

s1 = "aabbaccc"
s2 = "ababcdcdababcdcd"
s3 = "abcabcdede"
s4 = "abcabcabcabcdededededede"
s5 = "xababcdcdababcdcd"
res1 = 7
res2 = 9
res3 = 8
res4 = 14
res5 = 17
ans1 = solution(s1)
ans2 = solution(s2)
ans3 = solution(s3)
ans4 = solution(s4)
ans5 = solution(s5)
ox = lambda res, ans: True if res==ans else False
print(f"test1\nresult: {res1}\nanswer: {ans1}\n{ox(res1, ans1)}\n")
print(f"test2\nresult: {res2}\nanswer: {ans2}\n{ox(res2, ans2)}\n")
print(f"test3\nresult: {res3}\nanswer: {ans3}\n{ox(res3, ans3)}\n")
print(f"test4\nresult: {res4}\nanswer: {ans4}\n{ox(res4, ans4)}\n")
print(f"test5\nresult: {res5}\nanswer: {ans5}\n{ox(res5, ans5)}\n")