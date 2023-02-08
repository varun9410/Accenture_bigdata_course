class test:
    def __init__(self):
        self.score=0
        self.subject=['Apptitude','English','Math','GK']
        self.attempted_subject=[]
    def choose_subject(self):
        print('Please choose the subject:')
        for i in range(0,len(self.subject)):
            print(i+1,'.',self.subject[i])
        print('5.Exit')
        chose_subject=int(input('Enter the no: '))
        return chose_subject
    def show_question(self,subject):
        if subject==1 and subject not in self.attempted_subject:
            self.attempted_subject.append(subject)
            answer=int(input('result of 3*12 is:'))
            if answer==36:
                self.score+=10
        elif subject==2 and subject not in self.attempted_subject:
            self.attempted_subject.append(subject)
            answer=str(input('result of 10+10:'))
            if answer==20:
                self.score+=10
        elif subject==3 and subject not in self.attempted_subject:
            self.attempted_subject.append(subject)
            answer=str(input('''this ... a bird!
         1.is
         2.a '''))
            if answer==1:
                self.score+=10
        elif subject==4 and subject not in self.attempted_subject:
            self.attempted_subject.append(subject)
            answer=str(input('''Capital of India
            1.Delhi
            2.Noida'''))
            if answer==1:
                self.score+=10  
        else:
          print('You have attempted this subject and please choose subject')     
    def show_score(self):
        print(self.score)
    def show_point(self):
        if self.score==10:
            print('points:',0)
        if self.score==20:
            print('points:',2)
        if self.score==30:
            print('points:',5)
        if self.score==40:
            print('points:',10)
    def show_statement(self):
        if self.score>=40:
            print('You are genuis')
        if self.score>=30:
            print('You are intelligent')
        if self.score>=20:
            print('Your IQ level is average')
        if self.score>=10:
            print('Your IQ level below average')
    def attempted_question(self,subject):
      self.attempted_subject.append(subject)

        
# Execution of Code   
test=test()
while True:
    attempt_no=int(input('Enter the Number of attempts:'))
    if attempt_no>2:
        print('You can only attempt once')
    if attempt_no==5:
        print('You have exited the Exam')
        break
    else:
        subject=test.choose_subject()
        test.show_question(subject)
        test.show_score()
        test.show_point()
        test.show_statement()
    
    
        
        
