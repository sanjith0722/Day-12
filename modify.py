from tkinter import*
import random
import os
from tkinter import messagebox


#===============main=====================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#badc57"
        
    # ================variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.syrup = IntVar()
        self.cream = IntVar()
        self.thermal_gun = IntVar()
    # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.spices = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        #=============coldDrinks=============================
        self.sprite = IntVar()
        self.mineral = IntVar()
        self.juice = IntVar()
        self.coke = IntVar()
        self.lassi = IntVar()
        self.mountain_duo = IntVar()
    # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============customer retail details======================
       
    # ===================Medical====================================
       

    # ==========GroceryItems=========================
       
    # ===========ColdDrinks================================
       

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=500, y=100, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
 

     # =======================ButtonFrame=============
       

    # =======Buttons-======================================
        btn_f = Frame(F5, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_s_p = self.sanitizer.get()*2
        self.m_m_p = self.mask.get()*5
        self.m_s_p = self.syrup.get()*30
        self.m_c_p = self.cream.get()*5
        self.m_t_g_p = self.thermal_gun.get()*15
        self.total_medical_price = float(self.m_m_p+self.m_h_g_p+self.m_s_p+self.m_c_p+self.m_t_g_p+self.m_s_p)

        self.medical_price.set("Rs. "+str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price*0.05), 2)
        self.medical_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*10
        self.g_f_o_p = self.food_oil.get()*10
        self.g_w_p = self.wheat.get()*10
        self.g_s_p = self.spices.get()*6
        self.g_f_p = self.flour.get()*8
        self.g_m_p = self.maggi.get()*5
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_s_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*5), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*10
        self.c_d_w_p = self.mineral.get()*10
        self.c_d_j_p = self.juice.get()*10
        self.c_d_c_p = self.coke.get()*10
        self.c_d_l_p = self.lassi.get()*10
        self.c_m_d = self.mountain_duo.get()*10
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_w_p+self.c_d_j_p+self.c_d_c_p+self.c_d_l_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_medical_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Grocery Retail")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============medical===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        if self.syrup.get() != 0:
            self.txtarea.insert(END, f"\n Syrup\t\t{self.syrup.get()}\t\t{self.m_s_p}")
        if self.cream.get() != 0:
            self.txtarea.insert(END, f"\n Cream\t\t{self.cream.get()}\t\t{self.m_c_p}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END, f"\n Thermal Gun\t\t{self.sanitizer.get()}\t\t{self.m_t_g_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.spices.get() != 0:
            self.txtarea.insert(END, f"\n Spices\t\t{self.spices.get()}\t\t{self.g_s_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
        #================ColdDrinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        if self.mineral.get() != 0:
            self.txtarea.insert(END, f"\n Mineral\t\t{self.mineral.get()}\t\t{self.c_d_w_p}")
        if self.juice.get() != 0:
            self.txtarea.insert(END, f"\n Juice\t\t{self.juice.get()}\t\t{self.c_d_j_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.lassi.get() != 0:
            self.txtarea.insert(END, f"\n Lassi\t\t{self.cream.get()}\t\t{self.c_d_l_p}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.sanitizer.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
    # ===============taxes==============================
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.syrup.set(0)
            self.cream.set(0)
            self.thermal_gun.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.spices.set(0)
            self.flour.set(0)
            self.maggi.set(0)
    # =============coldDrinks=============================
            self.sprite.set(0)
            self.mineral.set(0)
            self.juice.set(0)
            self.coke.set(0)
            self.lassi.set(0)
            self.mountain_duo.set(0)
    # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()