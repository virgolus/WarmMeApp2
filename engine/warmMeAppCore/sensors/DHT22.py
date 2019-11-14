import sys
import time
import DB
       
class DHT():

    def initSensor(self):
        # Get db connection
        cur = DB.con.cursor()
        
        # Get temperature correction parameter
        queryGetTempCorrectionPar = "select value from sensor_parameters where name like 'TempCorrectionValue'"
        cur.execute(queryGetTempCorrectionPar)
        global tempCorrectionParameter
        tempCorrectionParameter = float(cur.fetchone()[0])

    def __init__(self):
        self.initSensor()
