# 入力値を変数maxに格納。
tmp=input("最大値を入力してください。>>>");
print("==============================");
max=int(tmp);

for i in range(max):
    num=i+1;
    if num%3==0 and num%5==0:
        print(str(num) +" " + "FizzBuzz");
    else:
        print(num);