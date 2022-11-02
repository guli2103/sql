import threading as th
import time



def son1():
    for x in range(150):
        time.sleep(0.1)
        print(x)
        if a == 50:
            print("50 soniga yetib keldik")
            break
        
          
           
       

def son2():
    for x in range(150):
        time.sleep(0.1)
        print(x)
        if a == 100:
            print("100 soniga yetib keldik")
            break
        
            
         

def son3():
    for x in range(150):
        time.sleep(0.1)
        print(x)
    print("150 ga keldik")    

t1 = th.Thread(target=son1)
t2 = th.Thread(target=son2)
t3 = th.Thread(target=son3)

t1.start()
t2.start()
t3.start()

            

