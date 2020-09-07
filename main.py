import serial
import threading
import loadcell
import TechBinFinger
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
import time

comPort="/dev/ttyUSB0"
baurdRate=9600
old_weight=0
###########################################
user="192.168.43.138"
password="Padhu@1999"
host="192.168.43.185"
database="fingerprintdb5"
port=3306


############################################
comport=str(comPort)
baurdrate=int(baurdRate)
arduinoData = serial.Serial(comport,baurdrate)
def techBinWeight():
    print("ENTER THE WEIGHT IN GRAMS")
    weight=input()
    return int(weight)
#######################################
import mysql.connector
from mysql.connector import Error
def getWeightDetail(id,weight):
    try:
        mySQLConnection = mysql.connector.connect(user=user,password=password,host=host,database=database,port=port)
        cursor = mySQLConnection.cursor(buffered=True)
        sql_select_query = """select * from UserDetails where UserId = %s"""
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchall()
        a=record[0]
        #print(a[0])
        a[0]
        #if(str(a[0])==id):
            #print("yes")
        #print(id)
        if(record[0]==id):
            print("Hi")
        for row in record:
          #  print("UserId=", row[0])
          #  print("Weight=", row[1])
            old_weight=row[1]
           # print("Frequency = ", row[2])
           # print("TokenNum =", row[3], "\n")
        return old_weight
    except:
        mySql_insert_query = """INSERT INTO UserDetails(UserId, Weight, Frequency, TokenNum)
                                VALUES (%s, %s, %s, %s) """
        frequency=0
        token=1
        recordTuple = (id, weight, frequency, token)
        cursor.execute(mySql_insert_query, recordTuple)
        mySQLConnection.commit()
        print("Record inserted successfully into user table")
        old_weight=0
        return old_weight
    """finally:
        if (mySQLConnection.is_connected()):
            cursor.close()
            mySQLConnection.close()
            print("MySQL connection is closed")"""
########################################
def getFrequencyDetail(id):
    try:
        mySQLConnection = mysql.connector.connect(user=user,password=password,host=host,database=database,port=port)
        cursor = mySQLConnection.cursor(buffered=True)
        sql_select_query = """select * from UserDetails where UserId = %s"""
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchall()
        a=record[0]
        #print(a[0])
        a[0]
        #if(str(a[0])==id):
            #print("yes")
        #print(id)
        if(record[0]==id):
            print("Hi")
        for row in record:
          #  print("UserId=", row[0])
           # print("Weight=", row[1])
           # print("Frequency = ", row[2])
            Frequency=row[2]
           # print("TokenNum =", row[3], "\n")
        return (int(Frequency)+1)
    except:
        #mySql_insert_query = """INSERT INTO UserDetails(UserId, Weight, Frequency, TokenNum)
        #                        VALUES (%s, %s, %s, %s) """
        """frequency=0
        token=1
        recordTuple = (id, weight, frequency, token)
        cursor.execute(mySql_insert_query, recordTuple)
        mySQLConnection.commit()
        print("Record inserted successfully into Laptop table")"""
        frequency=0
        return int(frequency)
#########################################
def updateDetail(id, weight):
    try:
        mySQLConnection = mysql.connector.connect(user="192.168.43.138",password="Padhu@1999",host="192.168.43.185",database="fingerprintdb5",port=3306)
        cursor = mySQLConnection.cursor()
        sql_update_query = """Update UserDetails set Weight = %s where UserId = %s"""
        inputData = (weight, id)
        cursor.execute(sql_update_query, inputData)
        mySQLConnection.commit()
        #print("Record Updated successfully ")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
        
###########################################
def updateFrequency(id, frequency):
    try:
        mySQLConnection = mysql.connector.connect(user=user,password=password,host=host,database=database,port=port)
        cursor = mySQLConnection.cursor()
        sql_update_query = """Update UserDetails set Frequency = %s where UserId = %s"""
        inputData = (frequency, id)
        cursor.execute(sql_update_query, inputData)
        mySQLConnection.commit()
        #print("Record Updated successfully ")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))


##########################################
def techBinFingerPrint():
    try:
        f = PyFingerprint('/dev/ttyUSB1', 57600, 0xFFFFFFFF, 0x00000000)
        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
    try:
        print('Waiting for finger...')
    
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x01)

        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]
        if ( positionNumber == -1 ):
            print('New user welcome...')
#################################################
            print("Don't Remove finger...")
            time.sleep(2)

            print('Waiting for same finger again...')
        
            while ( f.readImage() == False ):
                pass

            f.convertImage(0x02)

            if ( f.compareCharacteristics() == 0 ):
                raise Exception('Fingers do not match')

            f.createTemplate()

            positionNumber = f.storeTemplate()
            print('Finger enrolled successfully!')
            print('New template position #' + str(positionNumber))
            return str(positionNumber)
        else:
            print('Found template at position #' + str(positionNumber))
            return str(positionNumber)
           # print('The accuracy score is: ' + str(accuracyScore))

    
        f.loadTemplate(positionNumber, 0x01)

        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

       # print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
    

############################################################





def TechBin():
    i=0
    while(i<10):
        if(arduinoData.in_waiting >0):
            result=arduinoData.readline()
            if(str(result.strip())=="1"):
                #weight=Loadcell();
                print("GARBAGE")
                garbage_weight=techBinWeight()
                idd=techBinFingerPrint()
                old_weight=getWeightDetail(idd,garbage_weight)
                total_weight=int(garbage_weight)+int(old_weight)
                if(garbage_weight>1):
                    frequency=getFrequencyDetail(idd)
                    #frequency+=1
                    updateFrequency(idd,frequency)
                if(total_weight>=1000):
                    total_weight=total_weight%1000
                    print("##################TOKEN####################")
                   # updateFReq()
                    updateDetail(idd,total_weight)
                if(total_weight==garbage_weight):
                    pass
                else:
                    updateDetail(idd,total_weight)
                print("user id : " +str(idd))
                print("total weight : " +str(total_weight))
                print("frequency : " +str(frequency))
                i+=1
                continue
                time.sleep(2)
                    




TechBin()

"""DetectionThread= threading.Thread(target=TechBin)
DetectionThread.start()"""
