def solution(participant, completion):
    hashDict = {}
    hashValue = 0
    for p in participant:
        hashDict[hash(p)] = p
        hashValue += hash(p)
    for c in completion:
        hashValue -= hash(c)
    return hashDict[hashValue]