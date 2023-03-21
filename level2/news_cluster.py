def solution(str1, str2):
    list_str1 = []
    list_str2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)-1):
        temp_str = str1[i:i+2]
        if temp_str.isalpha():
            list_str1.append(temp_str)
    for i in range(len(str2)-1):
        temp_str = str2[i:i+2]
        if temp_str.isalpha():
            list_str2.append(temp_str)
    gyo = set(list_str1) & set(list_str2)
    hap = set(list_str1) | set(list_str2)
    A = []
    for i in gyo:
        for _ in range(min(list_str1.count(i),list_str2.count(i))):
            A.append(i)
    B = []
    for i in hap:
        for _ in range(max(list_str1.count(i),list_str2.count(i))):
            B.append(i)

    if len(A) == 0 and len(B) == 0:
        return 65536
    else:
        return int(len(A) / len(B) * 65536)


print(solution('FRANCE','french'))