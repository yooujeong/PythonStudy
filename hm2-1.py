m = int(input("투입할 돈을 입력하세요"))
c = int(input("뽑고싶은 커피의 수를 입력하세요"))

def Coffee(var1, var2 ):
     cm = var1-(200*var2)
     return cm

print("거스름돈은 %d원 입니다."%Coffee(m,c))
