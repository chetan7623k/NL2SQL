"""
Database task delegator
"""

import pymysql
from flask import jsonify
import json
from operator import itemgetter, attrgetter

# class for on the fly database interface objects
class DBTasks(object) :

    def __init__(self) :
        self.mysql = None

    def configDB(self, userName, passWord, dbName, hostName) :
        try :
            self.mysql = pymysql.connect(hostName, userName, passWord, dbName)
        except pymysql.Error as e :
            return 'error : ' + str(e) 
    
    # Execute any query provided
    def execQuery(self, query) :
        try :
            cursor = self.mysql.cursor()
            cursor.execute(query)
            self.mysql.commit()
            cursor.close()
        except pymysql.Error as e :
            self.mysql.rollback()
            return 'error : ' + str(e)


    # Fetch Event Data for heatmap
    def fetchDataFromDB(self, NL_sentence) :
        try :
            '''
            self.fetchTimeLineData(start_date, end_date)
            cursor = self.mysql.cursor()
            cursor.execute("""SELECT EventID, COUNT(*) FROM Events WHERE EventTimeStamp >= '%s' 
                    GROUP BY EventID;""" % (start_date))
            events_data = cursor.fetchall()
            events = []
            for data_elem in events_data:
                events.append((data_elem[0], data_elem[1]))
            cursor.close()
            '''
            return "SELECT * FROM TEST_DB"
        except pymysql.Error as e :
            return 'error : ' + str(e)

    def close() :
        self.mysql.close()
