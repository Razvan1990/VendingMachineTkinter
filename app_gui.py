# from datetime import datetime, timedelta
import os
import time
import constants
from tkinter import *


class CoffeeMachine:

    def __init__(self):
        # this will store the balance from the vending machine
        self.balance = 0.0

    def check_balance_and_background(self, money_label):
        if 2 <= self.balance < 2.5:
            # color red
            money_label["text"] = "Credit: " + str(self.balance)
            money_label["bg"] = "#D3D68A"
        elif 2.5 <= self.balance < 3:
            # color yellow
            money_label["text"] = "Credit: " + str(self.balance)
            money_label["bg"] = "#F2644D"
        elif 3 <= self.balance < 4:
            # color blue
            money_label["text"] = "Credit: " + str(self.balance)
            money_label["bg"] = "#89DBF7"
        elif self.balance >= 4:
            # color green -> mint
            money_label["text"] = "Credit: " + str(self.balance)
            money_label["bg"] = "#459368"
        else:
            money_label["text"] = "Credit: " + str(self.balance)
            money_label["bg"] = "#ECF1F0"

    def add_money(self, value, money_label, message_label):
        if message_label["text"] == "Not enough credit for this item":
            message_label["text"] = "Hello! Insert coins/bills and select the product!"
            message_label["bg"] ="#ECF1F0"
        self.balance += value
        # check to see what values are there and based on that color the label to see what I can select
        self.check_balance_and_background(money_label)

    def make_selection(self, dict_coffees, index_selection, money_label, message_label, coffee_pick_label,
                       button_pickup):
        # first see if we selected something and if we did not pick it -> if so put a message there
        if button_pickup["state"] == NORMAL:
            message_label["text"] = "Please pick up you selection before ordering a new item"
            message_label["bg"] = "#F13812"
        else:
            # get key to see what value we are using -> -1 is to start the function from 1 in the command of the button
            index_key = list(dict_coffees)[index_selection - 1]
            # check first if we can select the item
            if self.balance - dict_coffees[index_key][1] < 0:
                message_label["text"] = "Not enough credit for this item"
                message_label["bg"] = "#F13812"
            else:
                # first we need to calculate the new balance based on the new balance and update the label
                self.balance -= dict_coffees[index_key][1]
                self.check_balance_and_background(money_label)
                '''now update the labels
                1. first say the coffee is preparing
                2. after 10 seconds change the label for the message, for the coffee_pickup and the state of the button
                '''

                message_label["bg"] = "#ECF1F0"

                # not working correctly (not showing Preparing...)
                time.sleep(10)
                message_label["text"] = "Product ready! Thank you and goodbye!"
                message_label["bg"] = "#28E5CE"

                # rechange label
                # change label for pickup and the state button
                coffee_pick_label["text"] = "Coffee is ready! Please pick up"
                button_pickup["state"] = NORMAL

    def handle_pickup_button(self, message_label, coffee_pick_label, button_pick_up):
        # message label original message
        message_label["text"] = "Hello! Insert coins/bills and select the product!"
        message_label["bg"] = "#ECF1F0"
        # pick-up label original message
        coffee_pick_label["text"] = "Pick up the coffee from here when it is ready"
        # put back disabled state for button
        button_pick_up["state"] = DISABLED

    def create_inform(self, window_place):
        '''
        Need 3 frames
            a. One in which we have the buttons for the coffees - > big frame
                a1. 15 buttons for coffee
            b. One in which we keep the cash buttons and 2 labes: one for money and one for message
            c. An empty frame which will have an image label when coffee finishes
        :param window_place:
        :return: nothing returns, here we will appeal the functions for the buttons
        '''
        global coffee1
        global coffee2
        global coffee3
        global coffee4
        global coffee5
        global coffee6
        global coffee7
        global coffee8
        global coffee9
        global coffee10
        global coffee11
        global coffee12
        global coffee13
        global coffee14
        global coffee15

        # lables
        global label_money
        global label_message
        global label_coffee_image

        # money buttons
        # global fity_bani
        # global one_leu
        # global five_lei

        # create the frames
        width_frame = 600
        height_frame = 500
        coffee_frame = LabelFrame(window_place, text="RAZVAN COFFEE", bg="#ABCABD", fg="#EEEEFC",
                                  font=("Comic Sans", 20, "bold"), labelanchor="n", width="600", cursor="target",
                                  height=700)
        coffee_frame.grid(padx=width_frame / 12, pady=height_frame / 25, row=0, column=0, )  # put it in the middle
        coffee_frame.grid_rowconfigure(0, weight=1)
        coffee_frame.grid_columnconfigure(0, weight=1)
        coffee1 = Button(coffee_frame, fg="#151714", bg="#D3D68A", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee1"][0], wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 1, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))
        coffee1.grid(row=0, column=0, padx=20, pady=7)
        coffee2 = Button(coffee_frame, fg="#151714", bg="#D3D68A", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee2"][0],
                         wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 2, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))

        coffee2.grid(row=0, column=1, padx=20, pady=7)
        coffee3 = Button(coffee_frame, fg="#151714", bg="#D3D68A", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee3"][0],
                         wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 3, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))

        coffee3.grid(row=0, column=2, padx=20, pady=7)
        coffee4 = Button(coffee_frame, fg="#151714", bg="#D3D68A", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee4"][0],
                         wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 4, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))

        coffee4.grid(row=1, column=0, padx=20, pady=7)
        coffee5 = Button(coffee_frame, fg="#151714", bg="#D3D68A", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee5"][0],
                         wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 5, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))

        coffee5.grid(row=1, column=1, padx=20, pady=7)
        coffee6 = Button(coffee_frame, fg="#151714", bg="#D3D68A", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee6"][0],
                         wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 6, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))
        coffee6.grid(row=1, column=2, padx=20, pady=7)
        coffee7 = Button(coffee_frame, fg="#151714", bg="#F2644D", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee7"][0],
                         wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 7, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))
        coffee7.grid(row=2, column=0, padx=20, pady=7)
        coffee8 = Button(coffee_frame, fg="#151714", bg="#F2644D", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee8"][0],
                         wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 8, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))
        coffee8.grid(row=2, column=1, padx=20, pady=7)
        coffee9 = Button(coffee_frame, fg="#151714", bg="#F2644D", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=15, height=4, justify="center",
                         text=constants.DICTIONARY_COFFEES["coffee9"][0],
                         wraplength=80,
                         command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 9, label_money,
                                                             label_message, label_coffee_image, button_pick_up,
                                                             ))
        coffee9.grid(row=2, column=2, padx=20, pady=7)
        coffee10 = Button(coffee_frame, fg="#151714", bg="#F2644D", font=("Comic Sans", 9, "bold"), bd=5,
                          cursor="target", width=15, height=4, justify="center",
                          text=constants.DICTIONARY_COFFEES["coffee10"][0],
                          wraplength=80,
                          command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 10, label_money,
                                                              label_message, label_coffee_image, button_pick_up,
                                                              ))
        coffee10.grid(row=3, column=0, padx=20, pady=7)
        coffee11 = Button(coffee_frame, fg="#151714", bg="#F2644D", font=("Comic Sans", 9, "bold"), bd=5,
                          cursor="target", width=15, height=4, justify="center",
                          text=constants.DICTIONARY_COFFEES["coffee11"][0],
                          wraplength=80,
                          command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 11, label_money,
                                                              label_message, label_coffee_image, button_pick_up,
                                                              ))
        coffee11.grid(row=3, column=1, padx=20, pady=7)
        coffee12 = Button(coffee_frame, fg="#151714", bg="#F2644D", font=("Comic Sans", 9, "bold"), bd=5,
                          cursor="target", width=15, height=4, justify="center",
                          text=constants.DICTIONARY_COFFEES["coffee12"][0],
                          wraplength=80,
                          command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 12, label_money,
                                                              label_message, label_coffee_image, button_pick_up,
                                                              ))
        coffee12.grid(row=3, column=2, padx=20, pady=7)
        coffee13 = Button(coffee_frame, fg="#151714", bg="#89DBF7", font=("Comic Sans", 9, "bold"), bd=5,
                          cursor="target", width=15, height=4, justify="center",
                          text=constants.DICTIONARY_COFFEES["coffee13"][0],
                          wraplength=80,
                          command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 13, label_money,
                                                              label_message, label_coffee_image, button_pick_up,
                                                              ))
        coffee13.grid(row=4, column=0, padx=20, pady=7)
        coffee14 = Button(coffee_frame, fg="#151714", bg="#89DBF7", font=("Comic Sans", 9, "bold"), bd=5,
                          cursor="target", width=15, height=4, justify="center",
                          text=constants.DICTIONARY_COFFEES["coffee14"][0],
                          wraplength=80,
                          command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 14, label_money,
                                                              label_message, label_coffee_image, button_pick_up,
                                                              ))
        coffee14.grid(row=4, column=1, padx=15, pady=7)
        coffee15 = Button(coffee_frame, fg="#151714", bg="#459368", font=("Comic Sans", 9, "bold"), bd=5,
                          cursor="target", width=15, height=4, justify="center",
                          text=constants.DICTIONARY_COFFEES["coffee15"][0],
                          wraplength=80,
                          command=lambda: self.make_selection(constants.DICTIONARY_COFFEES, 15, label_money,
                                                              label_message, label_coffee_image, button_pick_up,
                                                              ))
        coffee15.grid(row=4, column=2, padx=20, pady=7)
        # FRAME 2 CREATION
        money_frame = LabelFrame(window_place, text="INSERT MONEY", bg="#ABCABD", fg="#EEEEFC",
                                 font=("Comic Sans", 10, "bold"), labelanchor="n", width=500, cursor="target",
                                 height=350)
        money_frame.grid_rowconfigure(0, weight=1)
        money_frame.grid_columnconfigure(0, weight=1)
        money_frame.grid(row=0, column=1)
        money_frame.config(width=500, height=350)
        # create  labels and money buttons
        label_message = Label(money_frame, fg="#3B5711", bg="#ECF1F0", font=("Comic Sans", 8, "bold"), bd=7,
                              cursor="exchange", width=25, justify="center",
                              text="Hello! Insert coins/bills and select the product!", wraplength=170, height=3, )

        label_message.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)
        label_money = Label(money_frame, fg="#3B5711", bg="#ECF1F0", font=("Comic Sans", 11, "bold"), bd=7,
                            cursor="exchange", width=20, justify="center",
                            text="Credit: " + str(self.balance), )

        label_money.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)
        # add money buttons
        fity_bani = Button(money_frame, fg="#151714", bg="#90783A", font=("Comic Sans", 9, "bold"), bd=5,
                           cursor="target", width=6, height=1, justify="center",
                           text="50bani", wraplength=80,
                           command=lambda: self.add_money(constants.MONEY[0], label_money, label_message))
        fity_bani.grid(row=2, column=0, padx=7, pady=5, )
        one_leu = Button(money_frame, fg="#151714", bg="#73BF71", font=("Comic Sans", 9, "bold"), bd=5,
                         cursor="target", width=6, height=1, justify="center",
                         text=str(constants.MONEY[1]) + "lei", wraplength=80,
                         command=lambda: self.add_money(constants.MONEY[1], label_money,label_message))
        one_leu.grid(row=2, column=1, padx=7, pady=5, )
        five_lei = Button(money_frame, fg="#151714", bg="#B589C0", font=("Comic Sans", 9, "bold"), bd=5,
                          cursor="target", width=6, height=1, justify="center",
                          text=str(constants.MONEY[2]) + "lei", wraplength=80,
                          command=lambda: self.add_money(constants.MONEY[2], label_money,label_message))
        five_lei.grid(row=2, column=2, padx=7, pady=5, )
        # label product CREATION
        product_frame = LabelFrame(window_place, text="", bg="#81A293", fg="#EEEEFC",
                                   font=("Comic Sans", 20, "bold"), labelanchor="n", width="500", cursor="target",
                                   height=200)
        product_frame.grid_rowconfigure(0, weight=1)
        product_frame.grid_columnconfigure(0, weight=1)
        product_frame.grid(row=1, column=0)
        product_frame.config(width=500, height=350)
        label_coffee_image = Label(product_frame, text="Pick up the coffee from here when it is ready", anchor=W,
                                   justify="center", bg="#81A289", fg="#151514", font=("Comic Sans", 10, "bold"), )
        label_coffee_image.grid(row=0, column=0, sticky=W, padx=60)
        # make a button to pick up coffee
        button_pick_up = Button(product_frame, text="PICK UP", justify="center", font=("Comic Sans", 10, "bold"),
                                bg="#4D8DA7", fg="#151514", state=DISABLED,
                                command=lambda: self.handle_pickup_button(label_message, label_coffee_image, button_pick_up))
        button_pick_up.grid(row=0, column=1)

    def create_outform(self, window_place):
        window_place.title("VENDING MACHINE")
        window_place.geometry("950x650")
        icon_name = os.path.join(os.getcwd(), r"files\coffee.ico")
        window_place.iconbitmap(icon_name)
        window_place.configure(background="#133637")

    def run_gui(self):
        root = Tk()
        coffee_frame = LabelFrame(root, text="VENDING MACHINE", bg="#ABCABD", fg="#C35337",
                                  font=("Comic Sans", 20, "bold"), labelanchor="n", width=1050, cursor="dotbox",
                                  height=950)
        coffee_frame.grid(row=0, column=0, padx=60)
        self.create_outform(root)
        self.create_inform(coffee_frame)
        root.mainloop()
