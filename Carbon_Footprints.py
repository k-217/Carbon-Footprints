import browsing_internet
import commute_and_travel
import data_storage
import generating_non_recycled_waste
import home_or_workplace
import using_smartphone

import tkinter as tk

main = tk.Tk()
main.title("Carbon Footprint Calculator")
main.geometry('500x500')
main.configure(bg = "#85FC91")

welc = tk.Label(main, text = "Welcome to Carbon Footprint Calculator", font = ("Yu Gothic", 24, "bold"), fg = "#000000", bg = "#85FC91")
welc.grid(row = 0, column = 0, pady = 3)

slct = tk.Label(main, text = "Select", font = ("Yu Gothic", 18, "bold"), anchor = "w", fg = "#000000", bg = "#85FC91")
slct.grid(row= 1, column = 0, sticky = 'w', pady = 1)

bro_int = tk.Button(main, text = "Browsing Internet" , font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85E8FC", activebackground = "#85FC91", command = lambda: brow_inte())
bro_int.grid(row = 2, column = 0, sticky = 'w', pady = 1)

com_tra = tk.Button(main, text = "Commute and Travel" , font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#F68282", activebackground = "#85FC91", command = lambda: comm_trav())
com_tra.grid(row = 3, column = 0, sticky = 'w', pady = 1)

dat_sto = tk.Button(main, text = "Data Storage" , font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85E8FC", activebackground = "#85FC91", command = lambda: data_stor())
dat_sto.grid(row = 4, column = 0, sticky = 'w', pady = 1)

gen_was = tk.Button(main, text = "Generating Non Recycled Waste" , font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#F68282", activebackground = "#85FC91", command = lambda: gene_wast())
gen_was.grid(row = 5, column = 0, sticky = 'w', pady = 1)

usi_sma = tk.Button(main, text = "Using Smartphone" , font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85E8FC", activebackground = "#85FC91", command = lambda: usin_smar())
usi_sma.grid(row = 6, column = 0, sticky = 'w', pady = 1)

def brow_inte():
    br_in = tk.Toplevel()
    br_in.title("Browsing Internet")
    br_in.geometry('500x500')
    br_in.configure(bg = "#85FC91")

    slct = tk.Label(br_in, text = "Select", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    slct.grid(row= 0, column = 0, sticky = 'w', pady = 1)

    btn1 = tk.Button(br_in, text = "Display total number of trees", font = ("Yu Gothic", 18, "bold"), command = lambda: browsing_internet.total())
    btn1.grid(row = 1, column = 0, sticky = 'w', pady = 1)

    btn2 = tk.Button(br_in, text = "Show entire history", font = ("Yu Gothic", 18, "bold"), command = lambda: browsing_internet.show())
    btn2.grid(row = 2, column = 0, sticky = 'w', pady = 1)

    btn3 = tk.Button(br_in, text = "Insert new data", font = ("Yu Gothic", 18, "bold"), command = lambda: browsing_internet.insert())
    btn3.grid(row = 3, column = 0, sticky = 'w', pady = 1)

    btn4 = tk.Button(br_in, text = "Delete previous data", font = ("Yu Gothic", 18, "bold"), command = lambda: browsing_internet.delete())
    btn4.grid(row = 4, column = 0, sticky = 'w', pady = 1)

    btn5 = tk.Button(br_in, text = "Search for an entry", font = ("Yu Gothic", 18, "bold"), command = lambda: browsing_internet.search())
    btn5.grid(row = 5, column = 0, sticky = 'w', pady = 1)

    br_in.mainloop()

def comm_trav():
    co_tr = tk.Toplevel()
    co_tr.title("Commute and Travel")
    co_tr.geometry('500x500')
    co_tr.configure(bg = "#85FC91")

    slct = tk.Label(co_tr, text = "Select", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    slct.grid(row= 0, column = 0, sticky = 'w', pady = 1)

    btn1 = tk.Button(co_tr, text = "Display total number of trees", font = ("Yu Gothic", 18, "bold"), command = lambda: commute_and_travel.total())
    btn1.grid(row = 1, column = 0, sticky = 'w', pady = 1)

    btn2 = tk.Button(co_tr, text = "Show entire history", font = ("Yu Gothic", 18, "bold"), command = lambda: commute_and_travel.show())
    btn2.grid(row = 2, column = 0, sticky = 'w', pady = 1)

    btn3 = tk.Button(co_tr, text = "Insert new data", font = ("Yu Gothic", 18, "bold"), command = lambda: commute_and_travel.insert())
    btn3.grid(row = 3, column = 0, sticky = 'w', pady = 1)

    btn4 = tk.Button(co_tr, text = "Delete previous data", font = ("Yu Gothic", 18, "bold"), command = lambda: commute_and_travel.delete())
    btn4.grid(row = 4, column = 0, sticky = 'w', pady = 1)

    btn5 = tk.Button(co_tr, text = "Search for an entry", font = ("Yu Gothic", 18, "bold"), command = lambda: commute_and_travel.search())
    btn5.grid(row = 5, column = 0, sticky = 'w', pady = 1)

    co_tr.mainloop()

def data_stor():
    da_st = tk.Toplevel()
    da_st.title("Data Storage")
    da_st.geometry('500x500')
    da_st.configure(bg = "#85FC91")

    slct = tk.Label(da_st, text = "Select", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    slct.grid(row= 0, column = 0, sticky = 'w', pady = 1)

    btn1 = tk.Button(da_st, text = "Display total number of trees", font = ("Yu Gothic", 18, "bold"), command = lambda: data_storage.total())
    btn1.grid(row = 1, column = 0, sticky = 'w', pady = 1)

    btn2 = tk.Button(da_st, text = "Show entire history", font = ("Yu Gothic", 18, "bold"), command = lambda: data_storage.show())
    btn2.grid(row = 2, column = 0, sticky = 'w', pady = 1)

    btn3 = tk.Button(da_st, text = "Insert new data", font = ("Yu Gothic", 18, "bold"), command = lambda: data_storage.insert())
    btn3.grid(row = 3, column = 0, sticky = 'w', pady = 1)

    btn4 = tk.Button(da_st, text = "Delete previous data", font = ("Yu Gothic", 18, "bold"), commmand = lambda: data_storage.delete())
    btn4.grid(row = 4, column = 0, sticky = 'w', pady = 1)

    btn5 = tk.Button(da_st, text = "Search for an entry", font = ("Yu Gothic", 18, "bold"), command = lambda: data_storage.search())
    btn5.grid(row = 5, column = 0, sticky = 'w', pady = 1)

    da_st.mainloop()

def gene_wast():
    ge_wa = tk.Toplevel()
    ge_wa.title("Generating Non Recycled Waste")
    ge_wa.geometry('500x500')
    ge_wa.configure(bg = "#85FC91")

    slct = tk.Label(ge_wa, text = "Select", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    slct.grid(row= 0, column = 0, sticky = 'w', pady = 1)

    btn1 = tk.Button(ge_wa, text = "Display total number of trees", font = ("Yu Gothic", 18, "bold"), command = lambda: generating_non_recycled_waste.total())
    btn1.grid(row = 1, column = 0, sticky = 'w', pady = 1)

    btn2 = tk.Button(ge_wa, text = "Show entire history", font = ("Yu Gothic", 18, "bold"), command = lambda: generating_non_recycled_waste.show())
    btn2.grid(row = 2, column = 0, sticky = 'w', pady = 1)

    btn3 = tk.Button(ge_wa, text = "Insert new data", font = ("Yu Gothic", 18, "bold"), command = lambda: generating_non_recycled_waste.insert())
    btn3.grid(row = 3, column = 0, sticky = 'w', pady = 1)

    btn4 = tk.Button(ge_wa, text = "Delete previous data", font = ("Yu Gothic", 18, "bold"), command = lambda: generating_non_recycled_waste.delete())
    btn4.grid(row = 4, column = 0, sticky = 'w', pady = 1)

    btn5 = tk.Button(ge_wa, text = "Search for an entry", font = ("Yu Gothic", 18, "bold"), command = lambda: generating_non_recycled_waste.search())
    btn5.grid(row = 5, column = 0, sticky = 'w', pady = 1)

    ge_wa.mainloop()

def home_work():
    ho_wo = tk.Toplevel()
    ho_wo.title("Home or Workplace")
    ho_wo.geometry('500x500')
    ho_wo.configure(bg = "#85FC91")

    slct = tk.Label(ho_wo, text = "Select", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    slct.grid(row= 0, column = 0, sticky = 'w', pady = 1)

    btn1 = tk.Button(ho_wo, text = "Display total number of trees", font = ("Yu Gothic", 18, "bold"), command = lambda: home_or_workplace.total())
    btn1.grid(row = 1, column = 0, sticky = 'w', pady = 1)

    btn2 = tk.Button(ho_wo, text = "Show entire history", font = ("Yu Gothic", 18, "bold"), command = lambda: home_or_workplace.show())
    btn2.grid(row = 2, column = 0, sticky = 'w', pady = 1)

    btn3 = tk.Button(ho_wo, text = "Insert new data", font = ("Yu Gothic", 18, "bold"), command = lambda: home_or_workplace.insert())
    btn3.grid(row = 3, column = 0, sticky = 'w', pady = 1)

    btn4 = tk.Button(ho_wo, text = "Delete previous data", font = ("Yu Gothic", 18, "bold"), command = lambda: home_or_workplace.delete())
    btn4.grid(row = 4, column = 0, sticky = 'w', pady = 1)

    btn5 = tk.Button(ho_wo, text = "Search for an entry", font = ("Yu Gothic", 18, "bold"), command = lambda: home_or_workplace.search())
    btn5.grid(row = 5, column = 0, sticky = 'w', pady = 1)

    ho_wo.mainloop()

def usin_smar(): 
    us_sm = tk.Toplevel()
    us_sm.title("Using Smartphone")
    us_sm.geometry('500x500')
    us_sm.configure(bg = "#85FC91")

    slct = tk.Label(us_sm, text = "Select", font = ("Yu Gothic", 18, "bold"), fg = "#000000", bg = "#85FC91")
    slct.grid(row= 0, column = 0, sticky = 'w', pady = 1)

    btn1 = tk.Button(us_sm, text = "Display total number of trees", font = ("Yu Gothic", 18, "bold"), command = lambda: using_smartphone.total())
    btn1.grid(row = 1, column = 0, sticky = 'w', pady = 1)

    btn2 = tk.Button(us_sm, text = "Show entire history", font = ("Yu Gothic", 18, "bold"), command = lambda: using_smartphone.show())
    btn2.grid(row = 2, column = 0, sticky = 'w', pady = 1)

    btn3 = tk.Button(us_sm, text = "Insert new data", font = ("Yu Gothic", 18, "bold"), command = lambda: using_smartphone.insert())
    btn3.grid(row = 3, column = 0, sticky = 'w', pady = 1)

    btn4 = tk.Button(us_sm, text = "Delete previous data", font = ("Yu Gothic", 18, "bold"), command = lambda: using_smartphone.delete())
    btn4.grid(row = 4, column = 0, sticky = 'w', pady = 1)

    btn5 = tk.Button(us_sm, text = "Search for an entry", font = ("Yu Gothic", 18, "bold"), command = lambda: using_smartphone.search())
    btn5.grid(row = 5, column = 0, sticky = 'w', pady = 1)

    us_sm.mainloop()


main.mainloop()