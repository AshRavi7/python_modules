# Logging - Logging can help develop a better understanding of the flow of a program and discover scenarios that might not even have thought of while developing.Logs provide developers with an extra set of eyes that are constantly looking at the flow that an application is going through.They can store information,like which user accessed the application.If an error occurs,then they can provide more insights than a stack trace by tellinh the user what the state of the program was before it arrived at the line of code where the error can possibly occur. Python provides a logging system as a part of its standard library so you can quickly add logging to your application. The logging module is a ready to use and powerful module.
import logging 
# By default, there are 5 standard levels indicating the severity of events.Each has a corresponding method that can be used to log events at that level of severity.The defined levels,in order of increasing severity are as follows: 1.DEBUG 2.INFO 3.WARNING 4.ERROR 5.CRITICAL

# The logging module provides the user with a default logger that allows you get started without needing to do much configuration. 
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# After executing the above program, you will notice debug() and info() messages did not get logged. This is because , by default the logging module logs the messages with a severity level of WARNING or above. You can change that by configuring the logging module to log events of all levels if you want.You can also define your own severity levels by changing configurations. 

def add(x=0,y=0):
    if type(x)!=int or type(y)!=int:
        logging.error("Parameter values are not integers")
        return None
    else:
        logging.info(f'x is {x} and y is {y} and the result is {x+y}')
        return x+y
    
def product(a=1,b=1):
    if type(a)!=int or type(b)!=int:
        logging.warning("parameters entered are not integers")
        return None
    else:
        logging.info(f'x is {a} and y is {b} and the result is {a*b}')
        return a*b

if __name__=='__main__':
    logging.basicConfig(filename='function_logs.log',filemode='a',format='%(asctime)s>>>%(process)d---%(name)s---%(levelname)s---%(message)s',level=logging.DEBUG) # creating own configurations with logging
    logging.debug('Executing python add function')
#     print(add(30,50))
#     print(add(15.5,30.5))
    print(add(20,30))
    logging.debug('Executing python product function')
#     print(product('10','10'))
    print(product(10,10))
    
    