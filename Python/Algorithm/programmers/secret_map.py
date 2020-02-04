# [secret_map.py]
# [1차] 비밀지도

# first
def binary(a):
    if a < 2 :
        return a % 2
    return str(binary(a // 2)) + str(a % 2)

def solution1(n, arr1, arr2):
    answer = []
    arr1 = [binary(i) for i in arr1]
    arr1 = ["0"*(n-len(str(i)))+str(i) if len(str(i)) < n else i for i in arr1]
    arr2 = [binary(i) for i in arr2]
    arr2 = ["0"*(n-len(str(i)))+str(i) if len(str(i)) < n else i for i in arr2]

    for i in range(n):
        temp = ""
        for j in range(n):
            if arr1[i][j] == "1" or arr2[i][j] == "1":
                temp += "#"
            else:
                temp += " "
        answer.append(temp)

    return answer

    # second
    def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer