import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode
import os
import platform
import tkinter as tk

def total():

    t = tk.Toplevel()
    t.title("Displaying total number of trees...")
    t.geometry('500x500')
    t.configure(bg = "#85FC91")

    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user = 'root',
                                         password = 'hell',
                                         host = 'localhost',
                                         database = 'carbon_footprints')
        cursor = cnx.cursor()
        query = ("select sum(no_of_trees) from generating_non_recycled_waste")
        cursor.execute(query)

        for x in cursor:    
                for y in x:
                    a= tk.Label(t, text = f"You owe {int(y)} trees to this planet. Go Green!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
                    a.grid()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            tk.Label(t, text = "Wrong Username or Password", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            tk.Label(t, text = "Database does not exist", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        else:
            tk.Label(t, text = "Try Again!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")



def show():

    s = tk.Toplevel()
    s.title("Showing entire history...")
    s.geometry('500x500')
    s.configure(bg = "#85FC91")

    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user = 'root',
                                         password = 'hell',
                                         host = 'localhost',
                                         database = 'carbon_footprints')
        cursor = cnx.cursor()
        query = ("select * generating_non_recycled_waste")
        cursor.execute(query)

        for (s_no, time_of_measurement, waste_in_kgs, co2_in_kgs, no_of_trees) in cursor:
            a = tk.Label(s, text = f'''{time_of_measurement} \n
            Waste (kg) - {waste_in_kgs} \n
            Carbon Dioxide Produced (kg) - {co2_in_kgs} \n
            Number of Trees - {no_of_trees}''', 
            font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
            a.pack()

        cursor.close()
        cnx.close()
        tk.Label(s, text = "Go Green!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            tk.Label(s, text = "Wrong Username or Password", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            tk.Label(s, text = "Database does not exist", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        else:
            tk.Label(s, text = "Try Again!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")



def insert():

    i = tk.Toplevel()
    i.title("Inserting new data...")
    i.geometry('500x500')
    i.configure(bg = "#85FC91")

    def output():
        try:
            os.system('cls')
            cnx = connection.MySQLConnection(user =' root',
                                             password = 'hell',
                                             host = 'localhost',
                                             database = 'carbon_footprints')
            cursor = cnx.cursor()

            waste_in_kgs = int(a2.get(1.0, "end-1c"))
            co2_in_kgs = (waste_in_kgs)*0.0005
            no_of_trees = float(co2_in_kgs/38500)

            a3.configure(text = f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

            query = ('''insert into generating_non_recycled_waste (waste_in_kgs, co2_in_kgs, no_of_trees) 
            values (%f, %f, %f)''')
            data = (waste_in_kgs, co2_in_kgs, no_of_trees)
            cursor.execute(query, data)
            cnx.commit()
            cursor.close()
            cnx.close()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                tk.Label(i, text = "Wrong Username or Password", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                tk.Label(i, text = "Database does not exist", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
            else:
                tk.Label(i, text = "Try Again!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")

        else:
            cnx.close()

    a1 = tk.Label(i, text = "Enter Waste Produced (in kgs):", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    a1.grid()
    a2 = tk.Text(i, width = 5, height = 1, font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    a2.grid()
    a3 = tk.Label(i, text = "", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    a3.grid()

    a4 = tk.Button(i, text = "Submit", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91", command = output)
    a4.grid()



def delete():

    d = tk.Toplevel()
    d.title("Deleting previous data...")
    d.geometry('500x500')
    d.configure(bg = "#85FC91")

    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user = 'root',
                                         password = 'hell',
                                         host = 'localhost',
                                         database = 'carbon_footprints')
        cursor = cnx.cursor()

        time = input("Enter time of entry:")
        query = ('''delete from generating_non_recycled_waste
                 where time_of_measurement = %s''')
        time_of_measurement = (time, )
        cursor.execute(query, time_of_measurement)
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Successfully deleted. Hope you had planted those trees.")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            tk.Label(d, text = "Wrong Username or Password", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            tk.Label(d, text = "Database does not exist", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        else:
            tk.Label(d, text = "Try Again!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")

def search():

    q = tk.Toplevel()
    q.title("Inserting new data...")
    q.geometry('500x500')
    q.configure(bg = "#85FC91")

    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user = 'root',
                                         password = 'hell',
                                         host = 'localhost',
                                         database = 'carbon_footprints')
        cursor = cnx.cursor()
        
        time = input("Enter time of entry:")
        
        query = ('''select * from generating_non_recylced_waste
                 where time_of_measurement = %s''')
        time_of_measurement = (time, )
        cursor.execute(query, time_of_measurement)

        for (s_no, time_of_measurement, waste_in_kgs, co2_in_kgs, no_of_trees) in cursor:
            print(f'''{time_of_measurement} \n
            Waste (kg) - {waste_in_kgs} \n
            Carbon Dioxide Produced (kg) - {co2_in_kgs} \n
            Number of Trees - {no_of_trees}''')

        cnx.commit()
        cursor.close()
        cnx.close()
        print("Go Green!")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            tk.Label(q, text = "Wrong Username or Password", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            tk.Label(q, text = "Database does not exist", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        else:
            tk.Label(q, text = "Try Again!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")