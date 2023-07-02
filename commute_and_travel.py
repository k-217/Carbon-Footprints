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
        query = ("select sum(no_of_trees) from commute_and_travel")
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
        query = ("select * commute_and_travel")
        cursor.execute(query)

        for (s_no, time_of_measurement, vehicle, distance_kms, co2_in_kgs, no_of_trees) in cursor:
            a = tk.Label(s, text = f'''{time_of_measurement} \n
                Vehicle - {vehicle} \n
                Distance Travelled (km) - {distance_kms} \n
                Carbon Dioxide Produced (kg) - {co2_in_kgs} \n
                Number of Trees - {int(no_of_trees)}''', 
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
            cnx = connection.MySQLConnection(user = 'root',
                                            password = 'hell',
                                            host = 'localhost',
                                            database = 'carbon_footprints')
            cursor = cnx.cursor()

            distance_kms = float(a4.get(1.0, "end-1c"))

            vehicle = str(default.get())

            if vehicle == "Domestic Flight":
                co2_in_kgs = (distance_kms)*0.255
                no_of_trees = float(co2_in_kgs/38500)
                a6.configure(text = f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

            elif vehicle == "Haul Flight":
                co2_in_kgs = (distance_kms)*0.155
                no_of_trees = float(co2_in_kgs/38500)
                a6.configure(text = f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

            elif vehicle == "Diesel Car":
                co2_in_kgs = (distance_kms)*0.171
                no_of_trees = float(co2_in_kgs/38500)
                a6.configure(text = f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

            elif vehicle == "Petrol Car":
                co2_in_kgs = (distance_kms)*0.096
                no_of_trees = float(co2_in_kgs/38500)
                a6.configure(text = f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

            elif vehicle == "Motorcylce":
                co2_in_kgs = (distance_kms)*0.103
                no_of_trees = int(co2_in_kgs/38500)
                a6.configure(text = f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

            elif vehicle == "Bus":
                co2_in_kgs = (distance_kms)*0.105
                no_of_trees = int(co2_in_kgs/38500)
                a6.configure(text = f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

            elif vehicle == "Railway":
                co2_in_kgs = (distance_kms)*0.041
                no_of_trees = int(co2_in_kgs/38500)
                a6.configure(text = f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

            else:
                a6.configure(text = "Please choose a correct option")

            query = ('''insert into commute_and_travel (vehicle, distance_in_kms, co2_in_kgs, no_of_trees) 
                    values (%s, %f, %f, %i)''')
            data = (vehicle, distance_kms, co2_in_kgs, no_of_trees)
            cursor.execute(query, data)
            cnx.commit()
            cursor.close()
            cnx.close()
            print(f"You produced {co2_in_kgs} kg of carbon footprints and owe {int(no_of_trees)} trees to the planet. \n Go Green!")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                tk.Label(i, text = "Wrong Username or Password", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                tk.Label(i, text = "Database does not exist", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
            else:
                tk.Label(i, text = "Try Again!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    
    a1 = tk.Label(i, text = "Select the most appropriate mode of travel", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    a1.grid()
    
    options = ["Select the most appropriate mode of travel", "Domestic Flight", "Haul Flight", "Diesel Car", "Petrol Car", "Motorcycle", "Bus", "Railway"]
    default = tk.StringVar()
    default.set("Select the most appropriate mode of travel")
    
    a2 = tk.OptionMenu(i, default, *options)
    a2.grid()
    
    a3 = tk.Label(i, text = "Enter distance travelled in kms:", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    a3.grid()
    a4 = tk.Text(i, width = 5, height = 1, font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    a4.grid()
    a5 = tk.Label(i, text = "", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    a5.grid()

    a6 = tk.Button(i, text = "Submit", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91", command = output)
    a6.grid()

def delete():

    d = tk.Toplevel()
    d.title("Inserting new data...")
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
        query = ('''delete from commute_and_travel
                 where time_of_measurement = %s''')
        time_of_measurement = (time, )
        cursor.execute(query, time_of_measurement)
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Successfully deleted. Hope you had planted those trees.")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.er_access_denied_error:
            tk.Label(d, text = "Wrong Username or Password", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        elif err.errno == errorcode.er_bad_db_error:
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
        
        query = ('''select * from commte_and_travel
                 where time_of_measurement = %s''')
        time_of_measurement = (time, )
        cursor.execute(query, time_of_measurement)

        for (s_no, time_of_measurement, vehicle, distance_kms, co2_in_kgs, no_of_trees) in cursor:
            print(f'''{time_of_measurement} \n
                Vehicle - {vehicle} \n
                Distance Travelled (km) - {distance_kms} \n
                Carbon Dioxide Produced (kg) - {co2_in_kgs} \n
                Number of Trees - {int(no_of_trees)}''')

        cnx.commit()
        cursor.close()
        cnx.close()
        print("Go Green!")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.er_access_denied_error:
            tk.Label(q, text = "Wrong Username or Password", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        elif err.errno == errorcode.er_bad_db_error:
            tk.Label(q, text = "Database does not exist", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
        else:
            tk.Label(q, text = "Try Again!", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")

