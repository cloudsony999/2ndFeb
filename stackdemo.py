class Stack:

    def __init__(self,n):
        print('I am a constructor\n')
        self.stack=[]
        self.size=n

    #PUSH 
        
    def push_me(self,element):
        if len(self.stack)==self.size:
            print('No more elements can be added\n')
        else:
            self.stack.append(element)

    #POP
            
    def pop_me(self):
        if self.stack==[]:
            return 'Nothing to POP\n'
        else:
            return self.stack.pop()

s=Stack(5)

s.push_me(12)
s.push_me(13)
s.push_me(14)

print(s.stack)

for i in s.stack:
    print(i)

print(s.pop_me(),' has been popped')
print(s.pop_me(),' has been popped')
print(s.pop_me(),' has been popped')

print(s.stack)









   