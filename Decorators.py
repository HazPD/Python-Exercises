import time

def ticktock(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1 
        print("Took " + str(t2) + "seconds")
    return wrapper

@ticktock
def do_this():
    #This simulates running code
    time.sleep(1.3)#
@ticktock
def do_that():
    #This simulates running code
    time.sleep(6.7)#


do_this()
do_that()
print("Finished running code")