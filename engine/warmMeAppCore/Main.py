#!/usr/bin/python3

# import Scheduler
import DB
#import Activator
import Harvester
import time
from threading import Thread
    
# def scheduler(sec):
#    Scheduler.run()
#    Sleep(sec)

if __name__ == '__main__':
    # initialize DB cnnection
    DB.getDBConnection()

    print('Harverster - start')
    thread = Thread(target = Harvester.start())
    thread.setDaemon(True)
    thread.start()
    print('Harverster - started')

    thread.join()

    
    #Activator.start()
    
    # Start scheduler
#    p = Process(target = scheduler, args = (5,))
 #   p.start()

    
