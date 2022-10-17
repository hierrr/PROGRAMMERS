def solution(numbers, hand):
    answer = ''
    lpos = 10
    rpos = 12
    for n in numbers:
        if n == 0:
            n = 11
        if n%3 == 1:
            lpos = n
            answer += "L"
        elif n%3 == 0:
            rpos = n
            answer += "R"
        else:
            if lpos%3 == 1:
                lx = abs(n-lpos-1)//3+1
            else:
                lx = abs(n-lpos)//3
            if rpos%3 == 0:
                rx = abs(n-rpos+1)//3+1
            else:
                rx = abs(n-rpos)//3
            if lx < rx or (lx == rx and hand == "left"):
                lpos = n
                answer += "L"
            elif lx > rx or (lx == rx and hand == "right"):
                rpos = n
                answer += "R"
    return answer

numbers1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand1 = "right"
hand2 = "left"
hand3 = "right"
result1 = "LRLLLRLLRRL"
result2 = "LRLLRRLLLRR"
result3 = "LLRLLRLLRL"
answer1 = solution(numbers1, hand1)
answer2 = solution(numbers2, hand2)
answer3 = solution(numbers3, hand3)
ox = lambda res, ans: True if res==ans else False
print(f"test1\nresult: {result1}\nanswer: {answer1}\n{ox(result1, answer1)}\n")
print(f"test2\nresult: {result2}\nanswer: {answer2}\n{ox(result2, answer2)}\n")
print(f"test3\nresult: {result3}\nanswer: {answer3}\n{ox(result3, answer3)}\n")