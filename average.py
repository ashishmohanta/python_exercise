def find_average(num):
  len=0
  sum=0
  for i in num:
    len=len+1
    print(len)
    sum=sum+i
    print(sum)
    averg=sum/len
    print(averg)
  print("average num",averg)

find_average([10,10,18,10])