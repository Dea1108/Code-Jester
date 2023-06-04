"""This code is a Python program that helps users calculate their body mass index (BMI),
      BMI rating, basal metabolic rate (BMR), total daily energy expenditure (TDEE), daily calorie
         needs for weight loss, and provides a summary report of their body statistics."""

# აქედან იწყება GUI ნაწილის შექმნა

import tkinter as tk
from tkinter import ttk, Tk,  END
from ttkbootstrap import Style
from ttkbootstrap import *
from tkinter import *

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text="თქვენი BMI არის : {:.2f}".format(bmi))

def calculate_bmr():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = int(age_entry.get())
    bmr = 88.362 + (13.397 * weight) + (479.9 * height) - (5.677 * age)
    bmr_label.config(text="თქვენი BMR არის: {:.2f}".format(bmr))

def clear_entries():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    target_weight_entry.delete(0, tk.END)
    time_frame_entry.delete(0, tk.END)
    activity_entry.delete(0, tk.END)
    bmi_label.config(text="")
    bmr_label.config(text="")
    tdee_label.config(text="")
    calorie_needs_label.config(text="")

def calculate_tdee():
    bmr = float(bmr_label.cget("text").split(":")[1].strip())
    activity_level = float(activity_entry.get())
    tdee_result = bmr * activity_level
    tdee_label.config(text="თქვენი TDEE არის: {:.2f}".format(tdee_result))

def calculate_daily_calorie_needs():
    weight_kg = float(weight_entry.get())
    target_weight = float(target_weight_entry.get())
    time_frame = int(time_frame_entry.get())

    weight_loss = weight_kg - target_weight
    calorie_deficit = weight_loss * 7700 / time_frame
    daily_calorie_needs = 2000 - calorie_deficit / 7

    if daily_calorie_needs <= 800:
        calorie_needs_label.config(text=" სწრაფი კლება ჯანმრთელობისთვის საფრთხის შემცველია , \n "
                                        "გთხოვთ მიუთითოთ კვირების გაზრდილი მაჩვენებელი.  ")
    else:
        calorie_needs_label.config(text="თქვენი დღიური კალორიული ნორმა უნდა იყოს  : {:.2f}".format(daily_calorie_needs))



# menubar

def vinvart():
    new_window11 = tk.Toplevel(root)
    new_window11.title("ჩვენ შესახებ")
    new_window11.resizable(True, True)
    label_chven= tk.Label(new_window11, text ='\n'
                                              '\n'
                                              'ჩვენ ვართ ორი ბიოლოგი, გვიყვარს საინტერესო ცხოვრება და ვმუშობთ ენთუზიაზმით. \n'
                                              'ჩვენი ისტორია იწყება ჩვენი სამეცნიერო ცხოვრების დასრულების შემდეგ. \n'
                                              'გადავწყვიტეთ საკუთარი ყურადღება და დრო დაგვეთმო პროგრამირებისთვის.\n'
                                              'დავიწყეთ 2023 წლის 10 იანვარს და აი უკვე აქ ვართ...2023 წლის 4 ივნისი...\n'
                                              'დღეს ჩვენი აპლიკაციის პირველი ვერსიის რელიზია.\n'
                                              '\n'
                                              'ჩვენი პორტფოლიო შეგიძლიათ იხილოთ:'
                                              '\n'
                                              'https://github.com/Dea1108 \n'
                                              'https://github.com/kristiELLL \n'
                                              '\n'
                                              'საჭიროებისამებრ, შეგიძლიათ დაგვიკავშირდეთ ელ-ფოსტით:\n'
                                              '\n'
                                              '\n'
                                              '1medea.gejadze@gmail.com \n'
                                              'kristine.eliosidze20@gmail.com \n'
                                              '\n'
                                              '\n '
                                              'დეა და ქრისტინე. \n'
                                              '\n'
                                              '\n')
    label_chven.grid(row=5, column=1, sticky= W, pady=1)


def raarisBMI():
    new_window = tk.Toplevel(root)
    new_window.title("რა არის BMI")

    label_bmi= tk.Label(new_window, text = '\n'
                                           'მეცნიერებმა და მედიკოსებმა შეიმუშავეს სპეციალური ფორმულა, რომელსაც ეწოდება სხეულის მასის ინდექსი (Body Mass Index). \n'
                                           'სწორედ სხეულის მასის ინდექსის საშუალებით გამოითვლება, თუ რამდენად შეესაბამება არსებული პროპორცია ბიოლოგიურ ნორმას.\n'
                                           'თქვენი სხეულის მასის ინდექსის გამოსათვლელად შესაბამის ველებში უნდა მიუთითოთ სიმაღლე და წონა.\n'
                                           '\n'
                                           'შედეგი ასეთია: \n'
                                           'თუ სხეულის მასის ინდექსი \n'
                                           '\n'
                                           '1. 16–ზე ნაკლებია, ადამიანს აქვს სხეულის მასის დიდი დეფიციტი;\n'
                                           '\n'
                                           '2. 16–დან 18.5–მდე მიუთითებს სხეულის მასის დეფიციტზე (წონის დეფიციტი);\n'
                                           '\n'
                                           '3. 18.5–დან 25–მდე პიროვნება ნორმალური წონისაა;\n'
                                           '\n'
                                           '4. 25–დან 30–მდე მაჩვენებელი ზედმეტ წონას (ჭარბი წონა) განსაზღვრავს;\n'
                                           '\n'
                                           '5. 30–ზე მეტი შედეგი კი სიმსუქნეზე მიუთითებს.'
                                           '\n'
                                           '\n'
                                           '\n'
                                            '            პერსონალური რჩევისთვის მიმართეთ პროფესიონალებს.'
                                           '\n'
                                            '\n')
    label_bmi.grid(row=5, column=1)

def raarisBMR():
    new_window2= tk.Toplevel(root)
    new_window2.title("რა არის BMR")

    label_bmr= tk.Label(new_window2, text = '\n'
                                            'BMR (Basal Metabolic Rate) არის ის ენერგია, რომელიც თქვენს სხეულს სჭირდება \n'
                                            '\n'
                                            ' ყველაზე ნაკლები დატვირთვის შემთხვევაში. მისი გამოთვლისათვის დაგჭირდებათ, ასაკის, წონისა და სიმაღლის მონაცემები.\n'
                                            '\n'
                                            ' BMR-ის შეფასება ხელს უწყობს საბაზისო კალორიული საჭიროებების განსაზღვრას.\n'
                                            '\n'
                                            ' ის სასარგებლოა წონის მართვისთვის, მაგრამ შეიძლება განსხვავდებოდეს ინდივიდუალურად. \n'
                                            '\n'
                                            '\n'
                                            '\n'
                                            '            პერსონალური რჩევისთვის მიმართეთ პროფესიონალებს.\n'
                                            '\n'
                                            '\n')
    label_bmr.grid(row=5, column=1)

def raarisTDEE():
    new_window3= tk.Toplevel(root)
    new_window3.title("რა არის TDEE")

    label3= tk.Label(new_window3, text = '\n'
                                         '\n'
                                         'TDEE ( Total Daily Energy Expediture), წარმოადგენს კალორიების იმ რაოდენობას,\n'
                                         'რომელიც ინდივიდი წვავს დღე-ღამის განმავლობაში.TDEE გამოსათვლელად დაგჭირდებათ თქვენი BMR-ის\n'
                                         'გამოთვლა და აქტივობის დონის განსაზღვრა. \n'
                                         '\n'
                                         'TDEE-ის გაანგარიშებით, ინდივიდებს შეუძლიათ დაგეგმონ დღიური კალორიების რაოდენობა, \n'
                                         'სასურველი წონის მისაღწევად ან შესანარჩუნებლად.'
                                         '\n'
                                         '\n')
    label3.grid(row=5, column=1)

def raarisaktiuroba():
    new_window4= tk.Toplevel(root)
    new_window4.title("რა არის აქტიურობის დონე?")

    label4= tk.Label(new_window4, text = '\n'
                                         '\n'
                                         'თქვენი აქტივობის დონის განსაზღვრისათვის შეგიძლიათ იხელმძღვანელოთ ჩვენი მონაცემებით, რომელიც აქტივობას განსაზღვრავს 1.2-დან 2.2-მდე შკალაში:\n'
                                         '\n'
                                         '-> შეიყვანე 1.2 : მინიმალური ფიზიკური აქტივობა.\n'
                                         '\n'
                                         '-> შეიყვანე 1.5: მსუბუქი ვარჯიში ან აქტივობა, კვირაში 1-3 დღის განმავლობაში.\n'
                                         '\n'
                                         '-> შეიყვანე 1.7: ზომიერი ვარჯიში ან აქტივობა, კვირაში 3-5 დღე.\n'
                                         '\n'
                                         '-> შეიყვანე 1.9: რეგულარული, საკმაოდ ინტენსიური ფიზიკური აქტივობა ან ვარჯიში კვირაში 6-7 დღის განმავლობაში.\n'
                                         '\n'
                                         '-> შეიყვანე 2.2: ძალიან აქტიური ცხოვრების წესი, ხშირად ასოცირდება პროფესიონალ სპორტსმენებთან.\n'
                                         '\n'
                                         'აქტივობის ეს მაჩვენებლები უწყობს დღიური კალორიების რაოდენობის განსაზღვრას თქვენი ფიზიკური აქტივობის დონის მიხედვით. \n'
                                         'მნიშვნელოვანია აირჩიოთ შესაბამისი აქტივობის დონე, რომელიც შეესაბამება თქვენი რეალური ცხოვრების წესს და საჭიროებისამებრ \n'
                                         'შეცვალეთ იგი პროფესიონალ კვების ინსტრუქტორთან შეთანხმებით.'
                                         '\n'
                                         '\n')
    label4.grid(row=5, column=1)

root = Tk()
style = Style()
style.theme_use('solar')
root.title("ფიტნეს აპლიკაცია - Me&Dea")
root.resizable(True, True)

mb= Menubutton(root, text = "პარამეტრები", bg= "red")
mb.grid(row=0, sticky= 'nw', columnspan= 2)
mb_menu=Menu(mb)
mb['menu']= mb_menu
mb_menu.add_checkbutton(label= "რა არის BMI", command= raarisBMI)
mb_menu.add_checkbutton(label= "რა არის BMR", command= raarisBMR)
mb_menu.add_checkbutton(label= "რა არის TDEE", command= raarisTDEE)
mb_menu.add_checkbutton(label= "რა არის აქტიურობის დონე", command= raarisaktiuroba)
mb_menu.add_separator()
mb_menu.add_checkbutton(label= "აპლიკაციიდან გასვლა", command= root.destroy)

cb= Menubutton(root, text='კონტაქტი')
cb.grid(row=0, column=0, sticky= 'nw', padx=89)
cb_menu=Menu(cb)
cb['menu']= cb_menu
cb_menu.add_checkbutton(label= "ჩვენ შესახებ", command= vinvart)

# Create labels
empty_label = ttk.Label(root, text="\nმოგესალმებით \n\nMe&Dea\n\n ჩვენ დაგეხმარებით თქვენთვის საჭირო ინფორმაციის მიღებაში.",
                                    font=("Helvetica", 12),foreground="pink",borderwidth=10,relief="solid",padding=(2, 3),justify="center",anchor="center")

empty_label.grid(row=0, column=0, columnspan=3)
empty_label.grid_columnconfigure(0, weight=1)
empty_label.grid_columnconfigure(1, weight=1)
empty_label.grid_columnconfigure(2, weight=1)

weight_label = ttk.Label(root, text=" წონა (კგ):")
weight_label.grid(row=1, column=0, sticky="e")
height_label = ttk.Label(root, text="სიმაღლე (მ):")
height_label.grid(row=2, column=0, sticky="e")
age_label = ttk.Label(root, text="ასაკი:")
age_label.grid(row=3, column=0, sticky="e")
target_weight_label = ttk.Label(root, text="რა არის თვენი სასურველი წონა ? (კგ):")
target_weight_label.grid(row=4, column=0, sticky="e")
time_frame_label = ttk.Label(root, text="რა დროში გსურთ მიზნის მიღწევა? (კვირა):")
time_frame_label.grid(row=5, column=0, sticky="e")
activity_label = ttk.Label(root, text="აქტიურობის დონე:")
activity_label.grid(row=6, column=0, sticky="e")
bmi_label = ttk.Label(root, text="")
bmi_label.grid(row=7, column=0, columnspan=2, sticky="s")
bmr_label = ttk.Label(root, text="")
bmr_label.grid(row=8, column=0, columnspan=2, sticky="s")
tdee_label = ttk.Label(root, text="")
tdee_label.grid(row=9, column=0, columnspan=2, sticky="s")
calorie_needs_label = ttk.Label(root, text="")
calorie_needs_label.grid(row=10, column=0, columnspan=2, sticky="s")

# Create entry fields
weight_entry = ttk.Entry(root)
weight_entry.grid(row=1, column=1, padx=90, pady=10, sticky="ns")
height_entry = ttk.Entry(root)
height_entry.grid(row=2, column=1, padx=90, pady=10, sticky="ns")
age_entry = ttk.Entry(root)
age_entry.grid(row=3, column=1, padx=90, pady=10, sticky="ns")
target_weight_entry = ttk.Entry(root)
target_weight_entry.grid(row=4, column=1, padx=90, pady=10, sticky="ns")
time_frame_entry = ttk.Entry(root)
time_frame_entry.grid(row=5, column=1, padx=90, pady=10, sticky="ns")
activity_entry = ttk.Entry(root)
activity_entry.grid(row=6, column=1, padx=90, pady=10, sticky="ns")

# Create button
bmi_button = ttk.Button(root, text="გამოთვალე BMI",  command=calculate_bmi)
bmi_button.grid(row=1, column=2, ipadx=57)
bmr_button = ttk.Button(root, text="გამოთვალე BMR", command=calculate_bmr)
bmr_button.grid(row=2, column=2, ipadx=56)
tdee_button = ttk.Button(root, text="გამოთვალე TDEE", command=calculate_tdee)
tdee_button.grid(row=3, column=2, ipadx=55)
calorie_needs_button = ttk.Button(root, text="გამოთვალე დღიური კალორიები", command=calculate_daily_calorie_needs)
calorie_needs_button.grid(row=4, column=2, ipadx=4)
clear_entries_button= ttk.Button(root, text= "გასუფთავება", command= clear_entries, style= 'warning')
clear_entries_button.grid(row= 6, column=2, ipadx=61)



print(root.mainloop())