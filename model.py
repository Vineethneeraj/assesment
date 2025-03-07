from mysql import connector
from mysql.connector import errorcode
import pandas as pd
import logging


class Model:
    def __init__(self):
        try:
            #mySQLDB connection
            self.conn = connector.connect(
                        host="mysql-3dc860f7-kedasuvineethnaidu-9c59.c.aivencloud.com",
                        user="avnadmin",
                        password="AVNS_9DzNZ1yk4-i9AWxFlAQ",
                        database="employee"
                        )
            self.cursor = self.conn.cursor()

        except errorcode as err:
            logging.basicConfig(
                filename='app.log',  # Log file name
                filemode='w',
                level=logging.DEBUG,  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
            )

            # Example logs
            logging.debug("This is a debug message")
            logging.info("This is an info message")
            logging.warning("This is a warning message")

#Flushing data into Database
    def upload(self,data):
        self.df = pd.read_csv(data)
        for _, row in self.df.iterrows():
            self.cursor.execute(
                "INSERT INTO employees (employee_id, name, email, department, designation, salary, date_of_joining) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                tuple(row)
            )
        self.conn.commit()
        print("CSV data successfully imported into MySQL!")
        self.cursor.close()
        self.conn.close()
        return True

