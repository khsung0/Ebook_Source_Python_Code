
data=[2,3,1,5,4]
print("정렬 전 배열 :",data)
print("\n버블 정렬 과정")
for i in range(len(data),0,-1):
    for j in range(0,i-1):
        #왼쪽 값이 클 경우 원소 교환
        if data[j]>data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
        print(data)
print("\n정렬 후 배열 :",data)

