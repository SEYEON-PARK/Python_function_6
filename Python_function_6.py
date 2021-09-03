def is_prime(a): # is_prime() 함수 정의
  if (a==1): # 만약, a가 1이라면
    return False # False 반환
  if (a==2): # 만약, a가 2라면
    return True # True 반환
  else: #만약 a가 2가 아니라면
    for x in range(2, a): # 2부터 a-1까지 반복
      if (a%x==0): # 만약, a가 x로 나누어 떨어진다면
        return False # False 반환
    return True # if문에서 한 번도 안 걸리면 True 반환

# 프로그램 시작
a=int(input("정수: ")) # 사용자로부터 정수 입력받기

if (is_prime(a)): # 만약 is_prime(a)가 True라면
  print(a, "은 소수입니다.", sep="") # 소수라고 출력하기
else: # 만약 is_prime(a)가 True가 아니라면
  print(a, "은 소수가 아닙니다.", sep="") # 소수가 아니라고 출력하기

  
