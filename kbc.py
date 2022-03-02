print('Kaun bnega crorepati me aapka swagat hai , ab first question ye rha aapki screen par....')
lis=['how many continents are there?','what is the capital of india','ng me kaun sa course padhaya jata hai']
option=[['four','nine','seven','eight'],['chandigadh','bhopal','chennai','delhi'],['software engineering','counsling','tourism','agriculture']]
solution=[3,4,1]
option1=[['seven ','eight'],['chennai','delhi'],['software engineering','counsling']]
solution1=[1,2,1]
i=0
b=1
count=0
while i<len(lis):
    print('Ques.',b,lis[i])
    j=0
    a=1
    b=b+1
    while j<len(option[i]):
        print(a,option[i][j])
        j=j+1
        a=a+1
    know=input("kya aapko answer aata hai press yes or no=")
    if know =="no":
        life=input("do you want to use 50-50 lifeline=")
        if life=="yes":
            if count>0:
                print("you already used the lifeline")
                guess=int(input('enter the answer='))
                if guess==solution[i]:
                    print('correct answer')
                    if i==(len(lis))-1:
                        print("good")
                        if i==(len(lis)-1):
                            print('Congratulation You are winner now , you will get 1 crore rupees')
                        else:
                            print('sorry your answer is wrong now you have out of the game')
                            break
            else:
                s=0
                b=1
                while s<len(option1[i]):
                    print(b,option1[i][s])
                    s=s+1
                    b=b+1
                    count+=1
                guess=int(input('enter the ans='))
                if guess==solution1[i]:
                    print("correct answer")
                else:
                    print('sorry your answer is wrong now you have out of the game')
                    break

        else:
            
            guess=int(input('enter the answer='))
            if guess==solution1[i]:
                print("correct answer")
            else:
                print('sorry your answer is wrong now you have out of the game')
                break
    else:
        print("ok we will proceed")
        guess=int(input('enter the answer='))
    
        if guess==solution[i]:
            print('correct answer')
            if i==(len(lis))-1:
                print("good")
                if i==(len(lis)-1):
                    print('Congratulation You are winner now , you will get 1 crore rupees')
        else:
            print('sorry your answer is wrong now you have out of the game')
            break
    i+=1
if count==0:
    print("aapne ek bar bhi 5050 lifeline use nhi kiya hai")