#Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec

#______________________APPROACH USING TWO DECORATORS________________________________ 
import time
def retrytime(func):
    def action(n):
        for i in range(3):
            print(time.ctime())      
            func(n)
    return action    
    
def retryinterval(func):
    def action(n):
        func(n)
        time.sleep(3)
    return action        


@retrytime              
@retryinterval
def printsquare(num):
    print(num**2)
    
printsquare(5)    
    
# For printsquare() function we are applying 2 decorator functions.
# Firstly the inner decorator will work and then the outer decorator.










#__________________________________________________________________________________
#_____________________Approach using one single decorator__________________________
# import time 

# def retry(func):
#     def repetitions(n):
#         for i in range(3):
#             func(n)
#             time.sleep(3)
#     return repetitions


# @retry
# def printsquare(num):
#     print(num**2)
    
    
# printsquare(5)    