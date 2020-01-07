from random import randint
import os
import re

Questions =[]
Question = []
AnswerKey= []

TestQuestions = []
Score = 0
QCheck = re.compile('QUESTION')
ACheck = re.compile('Answer:')
MCheck = re.compile('^.\.')
print("Comptia Sys-401 Comprehensive Exam Tester V#1.5")
print("Generating Questions")

#Generate Question/s
with open('401.txt','r') as f:
    for line in f:
        lineA = line[:-1]#remove end of line return
        if  re.match(QCheck,lineA) != None:
            ##Line is new Question
            Question.append(lineA)
        elif re.match(ACheck,lineA) != None:
            ##Line is end of Question
            #Set answer into key
            AnswerKey.append(lineA[8:])
            Question.append(lineA)
            Questions.append(Question)
            Question = []

        else:
            ##Line is part of current question
            Question.append(lineA)
##

#pre-test setup
t = True
while t == True:
    NumQ = int(input("Enter number of Questions for the test (1-1000)\n"))
    if((NumQ > 0)&(NumQ < 1001)):
        t = False
    elif NumQ == 0:
        print("Debug mode enabled, type question number to review")
        while True:
            print('Type EXIT to close or type the question number to review\n')
            IN = input()
            if (int(IN)>0)&(int(IN)<1020):
                print(str(Questions[int(IN)-1])+'\n')
            if IN == 'EXIT':
                close()
            else:
                print("ERROR: Invalid Entry\n\n\n")
##


#Testing
os.system('cls')
IncorrectAnswers = []
for i in range(NumQ):
    rand = randint(0,1018)
    print('\n\n#'+str(i+1)+'/'+str(NumQ)+':'+str(Questions[rand][0]))
    #TestQuestions[i] = randint(0,1018)
    #print(+'\n')
    j=1
    S=""
    while(re.match(MCheck,Questions[rand][j])==None):
        if(S.endswith(' ') == False):
           S = S+' '
        S = S+Questions[rand][j]
        j=j+1
    print(S+'\n')

    for k in range(j,len(Questions[rand])-1):
        print(Questions[rand][k])
    
    Answer = input('Answer: ')
    if Answer == AnswerKey[rand]:
           Score = Score+1
    else:
        IncorrectAnswers.append(rand+1)
    os.system('cls')
##


#Post Test
def results():
    print(str(Score)+'/'+str(NumQ)+' Correct - %'+str((Score/NumQ)*100))
    if((Score/NumQ)*100) > 83:
        print("You've scored high enough to pass the exam!")
    print('Following questions were incorrect: '+str(IncorrectAnswers[:]))

results()
while True:
    print('Type EXIT to close or type the question number to review\n')
    IN = input()   
    if IN == '':
        os.system('cls')
        results()

    elif IN == 'EXIT':
        close()

    elif (int(IN)>0)&(int(IN)<1020):
        print(str(Questions[int(IN)-1])+'\n')
    else: print('Invalid Command')    
#



#print(Question)

#print(AnswerKey)
#print(FT)
#QuestionCount = int(input("Enter number of questions for test (1-500)"))

#(^.*$)*(?!^(QUESTION))
#r'^QUESTION [0-9]{1,4}$'
