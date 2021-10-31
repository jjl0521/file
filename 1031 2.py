#21
lang = 'python'
print(lang[0],lang[2])
#22
licensem_plate="24가 2210"
#23
string="홀짝홀짝홀짝"
print(string[::2])
#24
string="python"
print(string[::-1])
#25
phone_number="010-1111-2222"
phone_number1=phone_number.replace("-","")
print(phone_number1)
#26
phone_number="010-1111-2222"
phone_number1=phone_number.replace('_','')
print(phone_number1)
#27
ur1="http://sharebook.kr"
ur1_split=ur1.split('.')
print(ur1_split[-1])
#28


#29
string='abcdfe2a354a32a'
string=string.replace('a','A')
print(string)
#30
string='abcd'
string.replace('b','B')
print(string)
#31
a="3"
b="4"
print(a+b)
#32
print("HI"*3)
#33
print("'-'"*80)
#34
t1="python"
t2="java"
t3=t1+''+t2+''
print(t3*4)
#35
name1="김민수"
age1 =10
name2="이철희"
age2 =13
print("이름:%s나이:%d" %(name1,age1))
print("이름:%s나이:%d" %(name2,age2))
#36
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
#37
name1="김민수"
age1=10
name2="이철희"
age2=13
print(f"이름:{name1}나이:(age1)")
print(f"이름:{name2}나이:{age2)")
#38
상장주식수="5,969,782,550"
컴마제거=상장주식수.replace(",","")
타입변환=int(컴마제거)
print(타입변환,type(타입변환))
#39
분기="2020/03(E)(IFRS연결)"
print(분기[:7]7])
#40
data="   삼성전자   "
data=data.strip()
print(data1)
