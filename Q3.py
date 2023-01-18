#Build a counter generator
import time 

def counter():          
    n=0              #starts counting from 0
    while True:      
        yield n
        n+=1         #increments by 1 after each yield
    
            
gen=counter()

print(gen.__next__())
print(gen.__next__())

#we can also use a for loop to generate counts on the go till we need without overloading the memory!

for i in gen:
    print(i)
    time.sleep(2)

