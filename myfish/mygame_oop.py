''' MAIN SETTINGS:
1. set the screen resolution as 1920X1080
2. if you want to stop the main game, just enter <p>
3. the boss key is <space>
4. the cheat code is actived when you enter <q> key
    if you enter the 'cheat code' mode, you will be invincible, which means you will not be eaten by the pufferfish
5. this fish game is to control the green fish to eat other blue & red fish;
    Totally there are 3 rounds; Warning: if meet the pufferfish, you will lose!
6. you should use the array key to control your green fish! 
    Remember to avoid meet those ugly pufferfish! And try to move your fish to eat the blue and red ones!
7. user can use both array key or mouse dragging to move the user green fish
'''

"""
question:!!!如何升级？？？
"""


from tkinter import *
import tkinter.messagebox
from  tkinter import ttk
import time
import subprocess
import os
from random import randint as rand
# from concurrent import futures
from threading import Thread
import threading
import json
import  collections

# The global stuff:

# calculate the time for user to stop/pause, and boss key
time_block = 0
move_flag = 2 # default as use array key to move user fish
# round one
count1 = 0  # blue fish count
count2 = 0  # red fish count

# round two
count3 = 0
count4 = 0

# round three
count5 = 0
count6 = 0
count7 = 0
count8 = 0

# s1,s2,s3 for seeds
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []

# user info
# original setting:
json_data = {"ID":0,"Name":"Local","Score":0,"Round":0,"Time":0.0}
original = [{"ID":0,"Name":"Local","Score":0,"Round":0,"Time":0.0}]
user_ID = 0
user_round = 0
user_count = []
user_name = []
user_time = []
temp_dict = {}
result = []

def photo_pool():
    global fish0, fish1, fish2, fish3, fish4, fish5, fish6
    global fish7, fish8, fish9, fish10, fish11, fish12
    global fish_enemy1, fish_enemy2, fish_enemy3, fish_enemy4
    global fish_enemy5, fish_enemy6, fish_enemy7, fish_enemy8
    global background,seed1,seed2,seed3,seed4,seed1_m,seed2_m,seed3_m,seed4_m
    global correct
    fish2 = PhotoImage(file="fish2_3.png")
    fish3 = PhotoImage(file="fish3.png")
    fish5 = PhotoImage(file="fish2_3_right.png")
    fish6 = PhotoImage(file="fish6.png")
    fish8 = PhotoImage(file="fish2_3.png")  # size: 3cm, which is mininum
    fish9 = PhotoImage(file="fish3.png")
    fish10 = PhotoImage(file="fish2_3_right.png")
    fish11 = PhotoImage(file="fish6.png")

    # setting for user fish>> from smallest to largest(3cm, 3.5cm, 4cm, 4.52cm)
    fish1 = PhotoImage(file="fish1.1_3.png")  # user's fish 1
    fish0 = PhotoImage(file="fish1.2_3.5.png") # user fish 2
    fish7 = PhotoImage(file="fish1.3_4.png") #user fish 3
    fish12 = PhotoImage(file="fish1.png") #user fish 4

    # special fish
    fish_enemy1 = PhotoImage(file="fish4.png") # huge ugly fish to eat user fish!
    fish_enemy2 = PhotoImage(file="fish4_right.png")
    fish_enemy3 = PhotoImage(file="fish4_right.png")
    fish_enemy4 = PhotoImage(file="fish4.png")
    fish_enemy5 = PhotoImage(file="fish4_right.png")
    fish_enemy6 = PhotoImage(file="fish4.png")
    fish_enemy7 = PhotoImage(file="fish4_right.png")
    fish_enemy8 = PhotoImage(file="fish4.png")

    # background settings:
    background = PhotoImage(file = "sea_2.png")
    seed1 = PhotoImage(file="seed1.png")
    seed2 = PhotoImage(file="seed2.png")
    seed3 = PhotoImage(file="seed3.png")
    seed4 = PhotoImage(file="seed1.png")
    # set for seed mirrors
    seed1_m = PhotoImage(file="seed1_m.png")
    seed2_m = PhotoImage(file="seed2_m.png")
    seed3_m = PhotoImage(file="seed3_m.png")
    seed4_m = PhotoImage(file="seed1_m.png")

    # image for cheat code
    correct = PhotoImage(file="correct.png")


def configure_window(window):
    global window_for_log_in, window1, window2
    if window == "window2" :
        window.title("Fish Game")
        window.geometry("1000x1000")
        window.configure(bg = "#b3ffff")

    # elif window == "window1" :
    #     window.title("MAIN MENU")
    #     window.geometry("800x800")
    #     window.configure(bg = "#b3ffff")


def program_quit():
    print("Thank you for your time! Have a nice day!")
    os._exit(0)

def sys_pause(event):
    global time_block
    ''' when you enter '<p>', u can stop the game
        if you want to contine the game, just enter any key in the terminal
        and than game will continue '''
    if event.keysym == "p":
        tick1 = time.time()
        text = input("Enter any key to back to the game: \n")
        # subprocess.call("pause",shell=True)
        # os.system("pause")
        tick2 = time.time()
        time_block = time_block + tick2 - tick1

    return time_block


def boss_key(event):
    global canvas, window, time_block
    if event.keysym == "space":
        window_for_boss_key = Tk()
        window_for_boss_key.title("Monthly/Weekly Plan")
        window_for_boss_key.geometry("1200x900")
        # create a treeview
        tree = ttk.Treeview(window_for_boss_key)
        ttk.Style().configure("tree", background="#383838", height = 20)
        tree["columns"]=("Name", "Age", "Height")
        tree.column("Name",width=300)   #not display
        tree.column("Age",width=300)
        tree.column("Height",width=300)
        # display headings
        tree.heading("Name",text="Name-name")
        tree.heading("Age",text="Age-age")
        tree.heading("Height",text="Height-tall")
        # insert data
        variable = "abcdefghijklmnopqrstuvwxyz"
        for i in range(20):
            txt = variable[rand(0,25)] + variable[rand(0,25)] + variable[rand(0,25)]
            txt1 = variable[rand(0,25)] + variable[rand(0,25)]
            txt2 = variable[rand(0,25)] + variable[rand(0,25)] +variable[rand(0,25)]\
                 + variable[rand(0,25)] + variable[rand(0,25)]
            txt3 = rand(0, 999)
            tree.insert("", i, text = txt, values=(txt1, txt2, txt3))
         
        tree.pack()

        '''this 'input' function can do the same thing to stop the main game
            enter a 'None'/<enter> key in the terminal to back to the fish game'''
        tick1 = time.time()
        text = input("Enter <enter> to back to the game or enter <space>\n")
        tick2 = time.time()
        time_block = time_block + tick2 - tick1

        if text == "":
            try:
                window_for_boss_key.destroy()
            except:
                print("Have already close the boss key window! Back to game!")
            # delete the rectangle and text made as the boss key entered

        else:
            print("default to save and quit!")
            save_game()
            program_quit()

            return time_block


def cheat_code(event):
    global cheat_code_flag
    if event.keysym == "q":
        print("Cheat code!")
        cheat_code_flag = 1

        return cheat_code_flag

def time_count():
    global count
    global txt, scoreText
    count += 1
    txt = "Score: " + str(count)
    canvas.itemconfig(scoreText, text = txt)

    return count






class LogInSetting(object):
    """docstring for LogInSetting"""
    # def __init__(self, master):
    #     super(LogInSetting, self).__init__()
    #     self._master = master
        
    # def get_master(self):
    #     return self._master


    # def Log_In_Page(self, master):
    def __init__(self, master):
        super(LogInSetting, self).__init__()
        self._master = master
        global user_name,user_count,user_round, window_for_log_in, user_ID,T1
        with open("game_info.json", mode = "r+") as myFile:
            try:
                data = json.load(myFile)
                result = data

            except:
                with open("game_info.json", mode = "w+") as f:
                    json.dump(original,f)
                    data = json.load(f)
                
                print("No previous history")

        print("user_ID: " + str(user_ID))
        # self._master = Tk()
        # self._master.grab_set()
        # self._master.geometry("500x300")
        # self._master.title("LOG IN")

        #user history
        Tx = []
        Ty = []
        length = len(data)

        # list all the previous history users:
        for i in range(length):
            Tx.append(Label(self._master, fg = "dark red", bg="#b3ffff", \
                font = ("Times New Roman", 12), text = data[i]['Name'], width = 18))
            Tx[i].grid(column = 4, row = 11+i)

            # title for the user history
            Ty.append(Label(self._master, fg = "dark red", bg="#b3ffff", \
                font = ("Times New Roman", 12), text = "users list:", width = 8))
            Ty[i].grid(column = 3, row = 11+i)

        # get new user or back to the saved game:
        T1 = Entry(self._master, fg = "dark red", bg="#b3ffff", font = ("Times New Roman", 12))
        T1.grid(column = 4, row = 10)
        T1_1 = Label(self._master, fg = "dark red", bg="#b3ffff", \
            font = ("Times New Roman", 12), text = "new user: ", width = 8)
        T1_1.grid(column = 3, row = 10)
        L0 = Button(self._master,text = "Enter a new user", \
            font = ("Times New Roman", 12), command = lambda: [self.get_user_name()])
        L0.grid(column = 5, row = 10)

        self._master.mainloop()


    def get_user_name(self):
        global T1,user_ID, flag
        global data
        # first to read the data from json file
        with open("game_info.json", mode = "r+") as myFile:
            try:
                data = json.load(myFile)
            except:
                with open("game_info.json", mode = "w+") as f:
                    json.dump(original,f)
                    data = json.load(f)
                print("No previous history")

        # enter and get a user name
        if T1.get() != "":
            for x in range(len(data)):
                # get a existed user(back to the saved game)
                if T1.get() == data[x]['Name']:
                    user_name.append(T1.get())
                    user_ID = data[x]['ID']
                    user_round = data[x]['Round']
                    count = data[x]['Score']
                    flag = data[x]['Flag']
                    print(user_round, "check for user_round")
                    print(user_count)
                    self.log_in_quit()
                    return user_name, user_round, user_count, flag, count

            else:
                user_name.append(T1.get())
                print(user_name, "Create a new record!")
                user_ID = data[x]['ID'] + 1  # add one more record for user_ID, which should be unique
                flag = 0
                self.log_in_quit_new()

        else:
            # overwritten the record of 'Local' user
            user_ID = 0 # 0 is the ID for default user 'Local'
            print("You have not enter a name!\nDefault use as the 'Local' name.")
            user_name.append("Local")
            print(user_name)
            self.log_in_quit_new()


    def log_in_quit(self):
        global user_ID, user_round, user_count, T1, flag
        with open("game_info.json", mode = "r+") as myFile:
            try:
                data = json.load(myFile)
            except:
                with open("game_info.json", mode = "w+") as f:
                    json.dump(original,f)
                    data = json.load(f)
                print("No previous history")

        # read the correct user name and back to the saved game
        for x in range(len(data)):
            if T1.get() == data[x]['Name']:
                user_name.append(T1.get())
                user_ID = data[x]['ID']
                user_round = data[x]['Round']
                count = data[x]['Score']
                flag = data[x]['Flag']

        print("Hello " + user_name[len(user_name) - 1]+  " Welcome to my fish game!")
        print("User Number/ID: " + str(user_ID))
        self._master.destroy()
        return user_name, user_round, user_count, flag, count


    def log_in_quit_new(self):
        global user_ID, flag
        flag = 0
        print("Hello " + user_name[len(user_name) - 1]+  " Welcome to my fish game!")
        print("User Number/ID: " + str(user_ID))
        self._master.destroy()
        return flag



class MainMenu(object):
    """docstring for app_menu"""
    def __init__(self, master):
        # super(app_menu, self).__init__()
        self._master = master
        # self._maincanvas = maincanvas
        self.maincanvas = Canvas(self._master, width = 400, height = 400, bg = "#D8BFD8")  # set the main canvas
        # self._main_game = main_game


    # def main_menu(self, master):
        

        # self.maincanvas = Canvas(self._master, width = 400, height = 400, bg = "#D8BFD8")  # set the main canvas
        self.maincanvas.pack()
        rect1 = self.maincanvas.create_rectangle(50, 15, 350, 45, fill = '#4B0082') # #4682B4
        Text1 = self.maincanvas.create_text(200, 30, text = "Leader Board", font = ("Times New Roman Bold", 20), fill = 'white')
        rect2 = self.maincanvas.create_rectangle(50, 355, 350, 45, fill = '#483D8B')
        mainline = self.maincanvas.create_line(0, 50, 400, 50, fill = '#FFDAB9', width = 5)
        line1 = self.maincanvas.create_line(50, 100, 350, 100, fill = '#FFDAB9')
        line2 = self.maincanvas.create_line(50, 160, 350, 160, fill = '#FFDAB9')
        line3 = self.maincanvas.create_line(50, 220, 350, 220, fill = '#FFDAB9')
        line4 = self.maincanvas.create_line(50, 280, 350, 280, fill = '#FFDAB9')

        # ...... start new game button......
        button1 = Button(self._master, text = "***Start***", font = ("Times New Roman Bold", 12), command = self._master.destroy, anchor = CENTER)
        button1.configure(width = 18, activebackground = "#33B5E5", bg = "#FFE4E1", relief = FLAT) # bg is MistyRose
        button1_window = self.maincanvas.create_window(100, 300, anchor=NW, window=button1)

        # check for count board/leader board
        self.count_board()
        # text_max = text_next = ""
        Label2 = Label(self._master, text = "", font = ("Times New Roman", 12), anchor = CENTER)
        Label2.configure(width = 28, fg = "#B22222", relief = FLAT, bg = "#E0FFFF", text=text_max) # font color:FireBrick
        Label2_window = self.maincanvas.create_window(65, 110, anchor=NW, window=Label2)

        Label3 = Label(self._master, text = "No.2", font = ("Times New Roman Bold", 12), anchor = CENTER)
        Label3.configure(width = 24, bg = "#E0FFFF", fg = "#8B4513", relief = FLAT)
        Label3_window = self.maincanvas.create_window(65, 180, anchor=NW, window=Label3)

        Label4 = Label(self._master, text = "", font = ("Times New Roman", 12), anchor = CENTER)
        Label4.configure(width = 28, bg = "#E0FFFF", fg = "#B22222", relief = FLAT, text=text_next)
        Label4_window = self.maincanvas.create_window(65, 230, anchor=NW, window=Label4)

        Label5 = Label(self._master, text = "No.1", font = ("Times New Roman Bold", 12), anchor = CENTER)
        Label5.configure(width = 24, bg = "#E0FFFF", fg = "#8B4513", relief = FLAT) # front color:SaddleBrown
        Label5_window = self.maincanvas.create_window(65, 60, anchor=NW, window=Label5)

        # force quit the whole program
        button6 = Button(self._master, text = "Quit", font = ("Times New Roman", 12), command = program_quit, anchor = CENTER)
        button6.configure(width = 8, activebackground = "#33B5E5", relief = FLAT, font = ("Times New Roman Bold", 12), bg = "#E0FFFF", fg = "#008080")
        button6_window = self.maincanvas.create_window(400, 360, anchor=NE, window=button6)

        # check for count board
        button7 = Button(self._master, text = "Count Board", font = ("Times New Roman", 12), command = self.rank_page, anchor = CENTER)
        button7.configure(width = 10, activebackground = "#33B5E5", relief = FLAT, font = ("Times New Roman Bold", 12), bg = "#E0FFFF", fg = "#008080")
        button7_window = self.maincanvas.create_window(120, 360, anchor=NE, window=button7)

        # costumize user to move the user fish
        move_flag = 2
        button8 = Button(self._master, text = "customize fish move seting", font = ("Times New Roman", 12), command = self.fish_move_page, anchor = CENTER)
        button8.configure(width = 10, activebackground = "#33B5E5", relief = FLAT, font = ("Times New Roman Bold", 12), bg = "#E0FFFF", fg = "#008080")
        button8_window = self.maincanvas.create_window(270, 360, anchor=NE, window=button8)

        # # prompt a message box for guiding
        # tkinter.messagebox.showinfo(title='WELCOME', message='The game is about to control your fish(the green one) to eat others(similar blue and red fish);\nHowever, if you meet those Pufferfish, you will be eaten and fail the game!') 

        # return move_flag
    def get_move_flag(self):
        """Returns:
            (str) : The move flag to control user fish.
        """
        return move_flag






    def fish_move_page(self):
        global move_flag

        move_flag = 2
        button1 = Button(self._master, text = "array key move", font = ("Times New Roman", 12), command = lambda: [self.move_set(1)], anchor = CENTER)
        button1.pack()
        button2 = Button(self._master, text = "WASD key move", font = ("Times New Roman", 12), command = lambda: [self.move_set(2)], anchor = CENTER)
        button2.pack()
        button3 = Button(self._master, text = "mouse move", font = ("Times New Roman", 12), command = lambda: [self.move_set(3)], anchor = CENTER)
        button3.pack()

        return move_flag

    def move_set(self, event):
        global move_flag
        if event == 1:
            move_flag = 2
            print(move_flag, "set the move_flag to 2")
            return move_flag
        elif event == 2:
            move_flag = 3
            print(move_flag, "set the move_flag to 3")
            return move_flag
        elif event == 3:
            move_flag = 1
            print(move_flag, "set the move_flag to 1")
            return move_flag

        return move_flag

    def count_board(self):
        global user_name,user_ID,user_count,user_round
        global text_max,text_next
        with open("game_info.json", "r+") as f:
        # add the new name gamer in the text file with his/her ID and score
            text_score_max = 0
            text_score_next = 0
            text_ID_max = 0
            text_ID_next = 0
            text_round_max = 0
            text_round_next = 0
            text_time_max = 0.0
            text_time_next = 0.0
            text_Name_max = ""
            text_Name_next = ""
            text_max = ""
            text_next = ""

            try:
                data = json.load(f)

            except:
                # no previous history so no data for rank board
                return text_max, text_next

            # sort data
            sort_line = sorted(data, key =lambda x: x.get('Score'), reverse = True)
            # line two max store users:
            Score_max = {'ID':0,'Name':'Local','Score':0,'Round':0,'Time':0.0}
            text_ID_max = sort_line[0]['ID']
            text_ID_next = sort_line[1]['ID']
            text_Name_max = sort_line[0]['Name']
            text_Name_next = sort_line[1]['Name']
            text_score_max = sort_line[0]['Score']
            text_score_next = sort_line[1]['Score']
            text_round_max = sort_line[0]['Round']
            text_round_next = sort_line[1]['Round']
            text_time_max = sort_line[0]['Time']
            text_time_next = sort_line[1]['Time']

        # print the leader board info in the terminal to check
        text_max = "ID: "+ str(text_ID_max) + " Name: " + text_Name_max + " Score: "\
        + str(text_score_max) + " \nRound: " + str(text_round_max) + " Time: " + str(text_time_max)

        text_next = "ID: "+ str(text_ID_next) + " Name: " + text_Name_next + " Score: "\
        + str(text_score_next) + " \nRound: " + str(text_round_next) + " Time: " + str(text_time_next)
        if text_ID_next == text_time_max:
            text_next = ""
        else:
            # print(text_next)
            pass

        return text_max, text_next, Score_max, sort_line


    def rank_page(self):
        window_for_rank = Tk()
        window_for_rank.grab_set()
        window_for_rank.geometry("280x600")
        window_for_rank.title("game rank")
        with open("game_info.json", "r+") as f:
            try:
                data = json.load(f)

            except:
                data = None
        # global sort_line
        sort_line = sorted(data, key =lambda x: x.get('Score'), reverse = True)
        text = []
        x = []
        if len(sort_line) > 10:
            length_count = 10
        else:
            length_count = len(sort_line)
        x1 = Label(window_for_rank, fg = "dark red", bg="#b3ffff", \
                               font = ("Times New Roman bold", 14), text = "Ranking", width = 20)
        x1.grid(column = 4, row = 10)
        for i in range(length_count):
            text.append("ID: "+ str(sort_line[i]['ID']) + " Name: " + sort_line[i]['Name'] + " Score: "\
                    + str(sort_line[i]['Score']) + " \nRound: " + str(sort_line[i]['Round']) \
                    + " Time: " + str(sort_line[i]['Time']))
            x.append(Label(window_for_rank, fg = "dark red", bg="#b3ffff", \
                        font = ("Times New Roman", 12), text = text[i], width = 30))
            x[i].grid(column = 4, row = 11+i)






class MainFishGame():
    """docstring for MainFishGame
        Parameters:
            master (tk.Tk): tkinter root widget"""
    def __init__(self, master):
        super(MainFishGame, self).__init__()
        self._master = master

        # set the size of canvas
        maincanvas = Canvas(self._master, width = 800, height = 500)
        self.canvas = maincanvas

        # self._main_game = main_game

        # # Set some of player's attributes according to the configuration file.
        # self._player = Player(name = self._player_config["Name"], \
        #                 ID = self._player_config["ID"], \
        #                 Score = self._player_config["Score"], \
        #                 time = self._player_config["Time"], \
        #                 round = self._player_config["Round"], \
        #                 )

        # create a toplevel menu
        menubar = Menu(self._master)

        # save the game
        menubar.add_command(label="Save", command=self.save_game)
        # quit the whole program forcely:
        menubar.add_command(label="Force Quit!", command=program_quit)
        # display the menu
        self._master.config(menu=menubar)

        # setting background:
        self.set_bg(self._master)

        # start main game loop:
        self.Main_game_loop()

    def save_game(self):
        global round_one, round_two, round_three, user_round, user_ID, user_name, \
        user_count, user_time, count
        global tick, time_block
        time_end = time.time()
        time_end_array = time.localtime(time_end)
        time_end_for_read = time.strftime("%Y-%m-%d %H:%M:%S", time_end_array)
        print("time for end this game: " + time_end_for_read)
        tick = time_end- time_start - time_block
        tick_array = time.strftime("%H:%M:%S", time.gmtime(tick))
        print(tick_array)
        user_time = round(tick,2)  # reserve 2 decimal places

        if round_one and round_two and round_three:
            user_round = 3
        elif not round_three and round_two and round_one:
            user_round = 2
        elif not round_two and round_one:
            user_round = 1
        else:
            user_round = 0

        print("You are in round ", user_round)
        with open("game_info.json", mode = "r+") as f:
            try:
                data = json.load(f)
                # print(data)

            except:
                data = original
                print("NO data/history before!")
                print("Default: ", data)
            result = data

            # if the ID /user already exist
            if user_ID <= data[len(data) - 1]['ID']:
                print("ID already exist and now update it!")

                temp_dict['ID'] = user_ID
                temp_dict['Name'] = user_name[len(user_name)-1]
                temp_dict['Score'] = count
                temp_dict['Round'] = user_round
                if flag == 0:
                    temp_dict['Flag'] = flag
                else:
                    temp_dict['Flag'] = flag - 1
                temp_dict['Time'] = user_time
                result[user_ID] = temp_dict

            else:
                temp_dict2 = {}
                temp_dict2['ID'] = user_ID  # add a new record
                temp_dict2['Name'] = user_name[len(user_name)-1]
                temp_dict2['Score'] = count
                temp_dict2['Round'] = user_round
                if flag == 0:
                    temp_dict2['Flag'] = flag
                else:
                    temp_dict2['Flag'] = flag - 1
                temp_dict2['Time'] = user_time

                result.append(temp_dict2)

            # overwrite the json file
            with open("game_info.json", mode = "w+") as f:

                json.dump(result,f)



    def set_bg(self, master):
        # global canvas, f, r1,r2,r3
        # global window
        self._master = master
        # set the size of canvas
        self.canvas = Canvas(self._master, width = 800, height = 500)
        # set the focus to the canvas widget
        self.canvas.grab_set()
        self.canvas.pack() #display the main canvas for game
        self.canvas.create_image(0,0,image = background, anchor = CENTER) # event ID: 1

        # set several stars
        star = []
        c = ["white", "#fefefe", "#dfdfdf"]
        for i_star in range(400):
            x_star = rand(1,799)
            y_star = rand(1,500)
            size = rand(2,5)
            f_star = rand(0,2)
            xy = (x_star, y_star, x_star+size, y_star+size)
            tmp_star = self.canvas.create_oval(xy)
            self.canvas.itemconfig(tmp_star, fill=c[f_star])
            star.append(tmp_star)

        # insert photos for seed
        for n in range(0, 800, 99):
            seed_time = time.time()
            # if n % 2 == 0:
            s1.append(self.canvas.create_image(n,400,image = seed1, anchor = NW))
            # print(s1) # [3, 8, 13, 18, 23, 28, 33, 38, 43]  x8
            s4.append(self.canvas.create_image(n+99,450,image = seed4, anchor = CENTER))
            s2.append(self.canvas.create_image(n+33,400,image = seed3, anchor = CENTER))
            s3.append(self.canvas.create_image(n+66,400,image = seed2, anchor = CENTER))
            s5.append(self.canvas.create_image(n,480,image = seed2, anchor = CENTER))
            s1.append(self.canvas.create_image(n+10,400,image = seed1_m, anchor = NW))
            s2.append(self.canvas.create_image(n+40,420,image = seed3_m, anchor = CENTER))
            s3.append(self.canvas.create_image(n+70,420,image = seed2_m, anchor = CENTER))
            s4.append(self.canvas.create_image(n+100,450,image = seed4_m, anchor = CENTER))
            s5.append(self.canvas.create_image(n+10,480,image = seed2_m, anchor = CENTER))
            s5.append(self.canvas.create_image(n+60,480,image = seed3_m, anchor = CENTER))


    def Main_game_loop(self):
        global window2, background,fish1,fish2,fish3,seed1,seed2,seed3, root
        global round_one,round_two,round_three
        global count
        global time_start,time_start_array
        global cheat_code_flag
        # configure_window(window2)

        # window.focus_set()
        # window2.grab_set()
        count = 0
        cheat_code_flag = 0

        # set the round:
        if user_round == 3:
            round_three = 1
            round_two = 1
            round_one = 1
        elif user_round == 2:
            round_two = 1
            round_three = 0
            round_one = 1
        elif user_round == 1:
            round_one = 1
            round_two = 0
            round_three = 0
        else:
            round_one = 0
            round_three = 0
            round_two = 0

        # calculate the time for start
        time_start = time.time()
        time_start_array = time.localtime(time_start)
        time_start_for_read = time.strftime("%Y-%m-%d %H:%M:%S", time_start_array)
        print("time for start a new game: " + time_start_for_read)

        self.bind()

        # main loop for the main fish game: to start a main loop keeping update
        # while 1:
            # self.bind()
        # # FishAppear(self._master)
        # self.myfish(self._master)
        # start my fish game
        # target = self.myfish
        # myfish_loop = self.myfish(self._master)
        thread1 = threading.Thread(target = self.myfish, args = (self._master,))
        # target = self.enemyfish
        # myfish_loop = self.myfish(self._master)

        # thread2 = threading.Thread(target = self.enemyfish, args = (self._master,))
        # thread2.start()
        thread1.start()
        # window2.update()

        print("My flag: (for passed round)" + str(flag))  # game end




    """ define all event to bind different keys to control or trigger
        specific event"""
    def bind(self):
        # when you enter '<p>', u can stop the game
        self.canvas.bind_all("<p>", sys_pause)
        # boss key
        self.canvas.bind_all("<space>", boss_key)
        # cheat code
        self.canvas.bind_all("<q>", cheat_code)

        # can add some option for user to choose: whether use array key or
        # mouse to move the user fish
        if move_flag == 1:
            self.canvas.bind_all('<B1-Motion>', self.mouse_move) 
        # bind the array key with the moving event
        elif move_flag == 2:
            self.canvas.bind_all("<KeyRelease-Up>", self.user_fish_move) 
            self.canvas.bind_all("<KeyRelease-Down>", self.user_fish_move)
            self.canvas.bind_all("<KeyRelease-Left>", self.user_fish_move)
            self.canvas.bind_all("<KeyRelease-Right>", self.user_fish_move)
        elif move_flag == 3:
            self.canvas.bind_all("<KeyRelease-w>", self.user_fish_move) 
            self.canvas.bind_all("<KeyRelease-s>", self.user_fish_move)
            self.canvas.bind_all("<KeyRelease-a>", self.user_fish_move)
            self.canvas.bind_all("<KeyRelease-d>", self.user_fish_move)

    def mouse_move(self, event):
        global x, y, f, r1, r2, r3
        x = event.x
        y = event.y
        if round_one == 0:
            self.canvas.coords(f, x, y)
        elif round_one == 1 and round_two == 0:
            self.canvas.coords(r1, x, y)
        elif round_two == 1:
            self.canvas.coords(r2, x, y)
        elif round_three == 1:
            self.canvas.coords(r3, x, y)
        # time_count()
        # check_for_upgrade()

        return x, y


    def user_fish_move(self, event):
        global count, r, r3, r2, r1, flag
        global x, y
        global count1, count2
        global round_one, user_fish_num

        # if round_one == 0:
        #     # user_fish_num = 2
        #     user_fish_num = f

        # elif round_one == 1 and round_two == 0:
        #     # upgrade fish is created after n*seed photos
        #     user_fish_num = r1

        # elif round_two == 1 and r2 != None:
        #     user_fish_num = r2
        # # will not enter this condistion since complete function'myfish()'
        # elif round_three == 1 and r3 != None: 
        #     user_fish_num = r3

        if event.keysym == "Up" or event.keysym == "w":
            self.canvas.move(user_fish_num, 0, -20)
            y -= 20
        elif event.keysym == "Down" or event.keysym == "s":
            self.canvas.move(user_fish_num, 0, 20)
            y += 20
        elif event.keysym == "Left" or event.keysym == "a":
            self.canvas.move(user_fish_num, -20, 0)
            x -= 20
        elif event.keysym == "Right" or event.keysym == "d":
            self.canvas.move(user_fish_num, 20, 0) 
            x += 20

        # # count will increase when move your fish
        # time_count()
        # check_for_upgrade()

        return x, y



# class FishAppear(object):
#     """docstring for FishAppear"""
#     def __init__(self, master):
#         super(FishAppear, self).__init__()
#         self._master = master

#         print("yes/ok")
#         print(move_flag)
#         self.myfish()
#         pass

    def myfish(self, master):
        global user_fish_num
        global canvas, f, r1, r2, r3
        global window, move_flag
        global x, y
        global round_one, round_control_1, round_two, round_three, flag
        global enemyfish1, enemyfish2, enemyfish3, enemyfish4
        global enemyfish5, enemyfish6, enemyfish7, enemyfish8
        global f1, f2, f3, f4
        global f8, f9, f10, f11, f12
        global round_one, x1,x2,x3,x4,y1,y2,y3,y4
        global count1,count2,count3,count4
        global x_enemy1, y_enemy1, x_enemy2, y_enemy2
        global x_enemy3, y_enemy3, x_enemy4, y_enemy4
        # self.bind()
        x = 150
        y = 400
        # print(move_flag)
        # set the global control stuff
        if count2 >= 1 and count1 >= 10:
            round_one = 1
        if (count3 >= 10 and count4 >= 1):
            round_two= 1
        if count5 >= 10 and count6 >=1 and count7 >= 10 and count8 >= 1 and round_three == 0:
            round_three = 1

        # print("111  ", Canvas)
        # print("222  ", round_one)
        # self.canvas = Canvas(self._master, width = 800, height = 500)

        global txt, scoreText
        txt = "Score: " + str(count)
        scoreText = self.canvas.create_text(600, 80, fill = "white", font=("Times 20 italic bold"), text = txt)
        i = 1
        print(i, "1111111")
        global i_flag, i_main
        i_flag = 1
        # i_main = 1
        for i in range(5):
            print("user looopp")
            # check for round/ ocean update
            if not round_one:
                # f is the envent ID for original user fish
                f = self.canvas.create_image(150,400,image = fish1)
                user_fish_num = f
                print("333  ", f)
                # self.ocean_fish_move(1)
                i += 1
                i_flag += 1
                print(i, "+++1111111")

                x_enemy1 = rand(200,800)
                y_enemy1 = rand(10,320)
                x_enemy2 = rand(0,600)
                y_enemy2 = rand(10,300)

                f1 = self.canvas.create_image(0, 180, image = fish3)
                f2 = self.canvas.create_image(0, 280, image = fish2)
                enemyfish1 = self.canvas.create_image(x_enemy1, y_enemy1, image = fish_enemy2)
                enemyfish2 = self.canvas.create_image(x_enemy2, y_enemy2, image = fish_enemy1)
                # f1 & f2 are for round one ocean fish
                # ocean_fish_move_lefttoright(f1, f2, enemyfish1, enemyfish2)
                self.ocean_fish_move(1)
                print("enemyfish-1")


            elif not round_two and flag == 0:
                print("Cool! Pass round one!")
                fish1.blank()
                r1 = self.canvas.create_image(x,y,image = fish0)
                user_fish_num = r1
                flag = 1
                # self.ocean_fish_move(2)
                i += 1
                i_flag += 1
                print(i, "+++1111111")

                fish_enemy1.blank()
                fish_enemy2.blank()
                # new fish's ID: right to left
                f3 = self.canvas.create_image(800,380,image = fish5)
                f4 = self.canvas.create_image(800,80,image = fish6)
                x_enemy3 = rand(200,800)
                y_enemy3 = rand(10,500)
                x_enemy4 = rand(0,600)
                y_enemy4 = rand(10,500)
                avoid_flag = 1
                while avoid_flag:
                    # avoid that the user lost at the same time when round upgrade
                    if x_enemy4 < x + 20 or x_enemy4 > x - 20 | y_enemy3 < y + 20 or y_enemy3 > y - 20\
                    | y_enemy4 < y + 20 or y_enemy4 > y - 20:
                        x_enemy4 = rand(0,600)
                        y_enemy3 = rand(0,500)
                        y_enemy4 = rand(0,500)
                    else:
                        avoid_flag = 0

                enemyfish1 = self.canvas.create_image(x_enemy3, y_enemy3, image = fish_enemy3)
                enemyfish2 = self.canvas.create_image(x_enemy4, y_enemy4, image = fish_enemy4)
                self.ocean_fish_move(2)
                print("enemyfish-2")

            # elif round_two == 1 and not round_three and flag == 1:
            if round_one and round_two and not round_three and flag == 1:
                print("Cool! Pass round two!")
                fish0.blank()
                r2 = self.canvas.create_image(x,y,image = fish7)  # upgrade user fish
                user_fish_num = r2
                flag = 2
                # self.ocean_fish_move(3)
                i += 1
                i_flag += 1

                fish_enemy3.blank()
                fish_enemy4.blank()
                # f8, f9, f10 & f 11 are for round three ocean fish
                f8 = self.canvas.create_image(0,100,image = fish8)
                f9 = self.canvas.create_image(0,200,image = fish9)
                f10 = self.canvas.create_image(700,100,image = fish10)
                f11 = self.canvas.create_image(700,200,image = fish11)

                x_enemy3 = rand(200,800)
                y_enemy3 = rand(10,500)
                x_enemy4 = rand(0,600)
                y_enemy4 = rand(10,500)
                x_enemy1 = rand(200,800)
                y_enemy1 = rand(10,500)
                x_enemy2 = rand(0,600)
                y_enemy2 = rand(10,500)

                enemyfish1 = self.canvas.create_image(x_enemy3, y_enemy3, image = fish_enemy5)
                enemyfish2 = self.canvas.create_image(x_enemy4, y_enemy4, image = fish_enemy6)
                enemyfish3 = self.canvas.create_image(x_enemy1, y_enemy1, image = fish_enemy7)
                enemyfish4 = self.canvas.create_image(x_enemy2, y_enemy2, image = fish_enemy8)

                self.ocean_fish_move(3)
                print("enemyfish-3")


            if round_one and round_two and round_three and flag == 2:
            # elif round_three and flag == 2:
                fish7.blank()
                r3 = self.canvas.create_image(x,y,image = fish12)  # upgrade user fish 3
                user_fish_num = r3
                flag = 3
                # self.ocean_fish_move(3)
                i += 1
                i_flag += 1

                fish_enemy5.blank()
                fish_enemy6.blank()
                fish_enemy7.blank()
                fish_enemy8.blank()
                global canvas,user_ID,user_name,user_round,user_ID
                text = self.canvas.create_text(x,y+30, fill = "white", text = "Congratulations! Finished three rounds!", font = ("Arial Bold", 20))
                user_round = 3

                print("Congratulations! Finished three rounds!")

                # write the data/info into the txt file 'game_info.txt'
                self.save_game()
                time.sleep(5)
                program_quit()


            # i += 1
            # i_flag += 1
            print("loop flag", i, "1111111")






        return round_one, round_two, round_three, flag



    def ocean_fish_move(self, level):
        global x3,y3,x4,y4,x1,x2,y1,y2
        global x,y
        global count1, count2
        global count3, count4
        global x_enemy1, y_enemy1, x_enemy2, y_enemy2
        global x_enemy3, y_enemy3, x_enemy4, y_enemy4
        global enemyfish1, enemyfish2, enemyfish3, enemyfish4
        global enemyfish5, enemyfish6, enemyfish7, enemyfish8
        global f1, f2, f3, f4
        global round_one, round_two, round_three, flag
        print("move 1111!!!")
        if level == 1:
            print("enemyfish- 1 move!!!")
            y1 = 180
            y2 = 280
            # if not round_one and not round_control_1:
            if not round_one:
                for t in range(100):
                    # canvas.move(fish_num1,10,0)
                    self.canvas.move(f1,10,0)
                    x1 = 10 * t
                    # canvas.move(fish_num2,10,0)
                    self.canvas.move(f2,10,0)
                    x2 = 10 * t
                    x_rand1 = rand(-20, -10)
                    x_rand2 = rand(10, 20)
                    # enemy fish1 move from right to left; enemy fish2 move from left to right
                    # canvas.move(fish_num3, x_rand1, 0)
                    self.canvas.move(enemyfish1, x_rand1, 0)
                    # canvas.move(fish_num4, x_rand2, 0)
                    self.canvas.move(enemyfish2, x_rand2, 0)
                    x_enemy1 += x_rand1
                    x_enemy2 += x_rand2
                    self._master.after(60)
                    self._master.update()
                    # time_count()
                    self.collisions(1)
                    if count2 >= 1 and count1 >= 10:
                        round_one = 1
                        flag = 0
                        return round_one, flag, x1,x2,y1,y2, x_enemy1, x_enemy2, y_enemy1, y_enemy2

                print("My fish:" + str(x) + "," + str(y))
                print(str(x1) + "," + str(y1))
                print(str(x2) + "," + str(y2))
                print("Too long time to pass this round! game over")
                self.save_game()
                time.sleep(10)
                program_quit()

            return x1,x2,y1,y2, x_enemy1, x_enemy2, y_enemy1, y_enemy2

        elif level == 2:

            y3 = 380
            y4 = 80
            print("enemyfish- 2 move!!!")
            for t in range(100):
                # move more fish after the user fish upgraded
                self.canvas.move(f3,-10,0)
                x3 = 800 - 10 * t
                self.canvas.move(f4,-10,0)
                x4 = 800 - 10 * t

                x_rand1 = rand(-20, -10)
                x_rand2 = rand(10, 20)
                # enemy fish1 move from right to left; enemy fish2 move from left to right
                self.canvas.move(enemyfish1, x_rand1, 0)
                self.canvas.move(enemyfish2, x_rand2, 0)
                x_enemy3 += x_rand1
                x_enemy4 += x_rand2

                self._master.after(50)
                self._master.update()
                # time_count()
                self.collisions(2)
                if count4 >= 1 and count3 >= 10:
                    round_two = 1
                    flag = 1
                    return round_two, flag, x1,x2,y1,y2, x_enemy1, x_enemy2, y_enemy1, y_enemy2

            print("My fish:" + str(x) + "," + str(y))
            print(str(x3) + "," + str(y3))
            print(str(x4) + "," + str(y4))
            print("Too long time to pass this round! game over")
            self.save_game()
            time.sleep(10)
            program_quit()

            # return x3, x4, y3, y4, x_enemy1, x_enemy2, y_enemy1, y_enemy2

        elif level == 3:
            y1 = 100
            y2 = 200
            y3 = 100
            y4 = 200
            print("enemyfish- 3 move!!!")
            for t in range(100):
                # right to left
                self.canvas.move(f10,-10,0)
                x3 = 700 - 10 * t
                self.canvas.move(f11,-10,0)
                x4 = 700 - 10 * t
                # left to right
                self.canvas.move(f8,10,0)
                x1 = 10 * t
                self.canvas.move(f9,10,0)
                x2 = 10 * t

                x_rand1 = rand(-20, -10)
                x_rand2 = rand(10, 20)
                # enemy fish1 move from right to left; enemy fish2 move from left to right
                self.canvas.move(enemyfish1, x_rand1, 0)
                self.canvas.move(enemyfish2, x_rand2, 0)
                x_enemy3 += x_rand1
                x_enemy4 += x_rand2
                self.canvas.move(enemyfish3, x_rand1, 0)
                self.canvas.move(enemyfish4, x_rand2, 0)
                x_enemy1 += x_rand1
                x_enemy2 += x_rand2
                
                self._master.after(60)
                self._master.update()
                self.collisions(3)
                if count5 >= 10 and count6 >=1 and count7 >= 10 and count8 >= 1 and round_three == 0:
                    round_three = 1
                    flag = 2
                    return round_three, flag, x1,x2,y1,y2, x_enemy1, x_enemy2, y_enemy1, y_enemy2

            print("My fish:(at round three)" + str(x) + "," + str(y))
            print(str(x1) + "," + str(y1))
            print(str(x2) + "," + str(y2))
            print(str(x3) + "," + str(y3))
            print(str(x4) + "," + str(y4))
            print("Too long time to pass this round! game over")
            self.save_game()
            time.sleep(10)
            program_quit()

    def collision_check(self, a, b):
        temp1 = (b["x"] <= a["x"] + a["width"] <= b["x"] + b["width"])
        temp2 = (b["y"] <= a["y"] + a["height"] <= b["y"] + b["height"])
        return temp1 and temp2


    def collisions(self, level):
        global x1,y1,x2,y2
        global x,y,count1, count2,count
        global f1,f2,f3,f4
        global canvas
        global x3,y3,x4,y4,count3,count4
        global count5,count6,count7,count8
        global cheat_code_flag
        global x_enemy1, x_enemy2, y_enemy1, y_enemy2
        global x_enemy3, x_enemy4, y_enemy3, y_enemy4

        f_rect = {"x":x, "y":y, "width":100, "height":100}  # myfish

        if level == 1:

            # f_rect = {"x":x, "y":y, "width":100, "height":100}  # myfish
            f_rect2 = {"x":x1, "y":y1, "width":20, "height":20}  # fish3
            f_rect3 = {"x":x2, "y":y2, "width":30, "height":30}  # fish2
            f_rect_enemy1 = {"x":x_enemy1, "y":y_enemy1, "width":5, "height":5}
            f_rect_enemy2 = {"x":x_enemy2, "y":y_enemy2, "width":5, "height":5}

            if not cheat_code_flag:

                if (self.collision_check(f_rect, f_rect_enemy1) or self.collision_check(f_rect_enemy1, f_rect))\
                    or (self.collision_check(f_rect, f_rect_enemy2) or self.collision_check(f_rect_enemy2, f_rect)):
                    print("No! You're eaten!\nSorry, failed this round...")
                    self.canvas.create_text(x, y, text = "Sorry, failed this round...", 
                                        font = ("Arial Bold", 20), fill = "white")
                    count -= 10
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)
                    self.print(str(count))
                    self.save_game()
                    time.sleep(5)
                    program_quit()

                elif count1 == 0 and (self.collision_check(f_rect, f_rect2) or self.collision_check(f_rect2, f_rect)):
                    print("Collison2!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish2:" + str(x1) + "," + str(y1))
                    fish3.blank()
                    count1 += 10
                    count += 10
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                elif count2 == 0 and (self.collision_check(f_rect, f_rect3) or self.collision_check(f_rect3, f_rect)):
                    print("Collison1!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish1:" + str(x2) + "," + str(y2))
                    fish2.blank()
                    count2 += 1
                    count += 5
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

            else:

                if count1 == 0 and (self.collision_check(f_rect, f_rect2) or self.collision_check(f_rect2, f_rect)):
                    print("Collison2!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish2:" + str(x1) + "," + str(y1))
                    fish3.blank()
                    count1 += 10
                    count += 10
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                if count2 == 0 and (self.collision_check(f_rect, f_rect3) or self.collision_check(f_rect3, f_rect)):
                    print("Collison1!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish1:" + str(x2) + "," + str(y2))
                    fish2.blank()
                    count2 += 1
                    count += 5
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

            txt = "Score: " + str(count)
            self.canvas.itemconfig(scoreText, text = txt)

            return count

        elif level == 2:

            f_rect5 = {"x":x3, "y":y3, "width":40, "height":40}  # fish5
            f_rect4 = {"x":x4, "y":y4, "width":30, "height":30}  # fish4
            f_rect_enemy3 = {"x":x_enemy3, "y":y_enemy3, "width":5, "height":5}
            f_rect_enemy4 = {"x":x_enemy4, "y":y_enemy4, "width":5, "height":5}

            if not cheat_code_flag:

                if (self.collision_check(f_rect, f_rect_enemy3) or self.collision_check(f_rect_enemy3, f_rect))\
                    or (self.collision_check(f_rect, f_rect_enemy4) or self.collision_check(f_rect_enemy4, f_rect)):
                    print("No! You're eaten!\nSorry, failed this round...")
                    self.canvas.create_text(x, y, text = "Sorry, failed this round...", font = ("Arial Bold", 20), fill = "white")
                    count -= 10
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)
                    # print(str(count))
                    self.save_game()
                    time.sleep(5)
                    program_quit()

                elif count3 == 0 and (self.collision_check(f_rect, f_rect4) or self.collision_check(f_rect4, f_rect)):
                    print("Collison3!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish3:" + str(x4) + "," + str(y4))
                    fish6.blank()
                    count3 += 10
                    count += 30
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                elif count4 == 0 and (self.collision_check(f_rect, f_rect5) or self.collision_check(f_rect5, f_rect)):
                    print("Collison4!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish4:" + str(x3) + "," + str(y3))
                    fish5.blank()
                    count4 += 1
                    count += 45
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

            else:

                if count3 == 0 and (self.collision_check(f_rect, f_rect4) or self.collision_check(f_rect4, f_rect)):
                    print("Collison3!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish3:" + str(x4) + "," + str(y4))
                    fish6.blank()
                    count3 += 10
                    count += 30
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                if count4 == 0 and (self.collision_check(f_rect, f_rect5) or self.collision_check(f_rect5, f_rect)):
                    print("Collison4!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish4:" + str(x3) + "," + str(y3))
                    fish5.blank()
                    count4 += 1
                    count += 45
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)
            txt = "Score: " + str(count)
            self.canvas.itemconfig(scoreText, text = txt)
            return count

        elif level == 3:
            f_rect8 = {"x":x1, "y":y1, "width":35, "height":35}  # fish8
            f_rect9 = {"x":x2, "y":y2, "width":26, "height":26}  # fish9
            f_rect10 = {"x":x3, "y":y3, "width":15, "height":15}  # fish10
            f_rect11 = {"x":x4, "y":y4, "width":24, "height":24}  # fish11
            f_rect_enemy1 = {"x":x_enemy1, "y":y_enemy1, "width":5, "height":5}
            f_rect_enemy2 = {"x":x_enemy2, "y":y_enemy2, "width":5, "height":5}
            f_rect_enemy3 = {"x":x_enemy3, "y":y_enemy3, "width":5, "height":5}
            f_rect_enemy4 = {"x":x_enemy4, "y":y_enemy4, "width":5, "height":5}

            if not cheat_code_flag:

                if (self.collision_check(f_rect, f_rect_enemy3) or self.collision_check(f_rect_enemy3, f_rect))\
                    or (self.collision_check(f_rect, f_rect_enemy4) or self.collision_check(f_rect_enemy4, f_rect))\
                    or (self.collision_check(f_rect, f_rect_enemy1) or self.collision_check(f_rect_enemy1, f_rect))\
                    or (self.collision_check(f_rect, f_rect_enemy2) or self.collision_check(f_rect_enemy2, f_rect)):
                    print("No! You're eaten!\nSorry, failed this round...")
                    self.canvas.create_text(x, y, text = "Sorry, failed this round...", font = ("Arial Bold", 20), fill = "white")
                    count -= 100
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)
                    # print(str(count))
                    self.save_game()
                    time.sleep(5)
                    program_quit()

                elif count5 == 0 and (self.collision_check(f_rect, f_rect8) or self.collision_check(f_rect8, f_rect)):
                    print("Collison5!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish8:" + str(x1) + "," + str(y1))
                    fish8.blank()
                    count5 += 10
                    count += 80
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                elif count6 == 0 and (self.collision_check(f_rect, f_rect9) or self.collision_check(f_rect9, f_rect)):
                    print("Collison6!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish9:" + str(x2) + "," + str(y2))
                    fish9.blank()
                    count6 += 1
                    count += 100
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                elif count7 == 0 and (self.collision_check(f_rect, f_rect10) or self.collision_check(f_rect10, f_rect)):
                    print("Collison7!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish10:" + str(x3) + "," + str(y3))
                    fish10.blank()
                    count7 += 10
                    count += 80
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                elif count8 == 0 and (self.collision_check(f_rect, f_rect11) or self.collision_check(f_rect11, f_rect)):
                    print("Collison8!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish11:" + str(x4) + "," + str(y4))
                    fish11.blank()
                    count8 += 1
                    count += 100
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

            else:

                if count5 == 0 and (self.collision_check(f_rect, f_rect8) or self.collision_check(f_rect8, f_rect)):
                    print("Collison5!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish8:" + str(x1) + "," + str(y1))
                    fish8.blank()
                    count5 += 10
                    count += 80
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                if count6 == 0 and (self.collision_check(f_rect, f_rect9) or self.collision_check(f_rect9, f_rect)):
                    print("Collison6!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish9:" + str(x2) + "," + str(y2))
                    fish9.blank()
                    count6 += 1
                    count += 100
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                if count7 == 0 and (self.collision_check(f_rect, f_rect10) or self.collision_check(f_rect10, f_rect)):
                    print("Collison7!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish10:" + str(x3) + "," + str(y3))
                    fish10.blank()
                    count7 += 10
                    count += 80
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

                if count8 == 0 and (self.collision_check(f_rect, f_rect11) or self.collision_check(f_rect11, f_rect)):
                    print("Collison8!")
                    print("myfish: " + str(x) + "," + str(y) +"\nfish11:" + str(x4) + "," + str(y4))
                    fish11.blank()
                    count8 += 1
                    count += 100
                    txt = "Score: " + str(count)
                    self.canvas.itemconfig(scoreText, text = txt)

            txt = "Score: " + str(count)
            self.canvas.itemconfig(scoreText, text = txt)

            return count




    # def user_fish_upgrade(self, level):
    #     # create two more fish>> from right to left
    #     global x3, x4, f3, f4
    #     global x_enemy3, x_enemy4, y_enemy3, y_enemy4
    #     # new fish's ID: right to left
    #     f3 = canvas.create_image(800,380,image = fish5)
    #     f4 = canvas.create_image(800,80,image = fish6)
    #     x_enemy3 = rand(200,800)
    #     y_enemy3 = rand(10,500)
    #     x_enemy4 = rand(0,600)
    #     y_enemy4 = rand(10,500)
    #     avoid_flag = 1
    #     while avoid_flag:
    #         # avoid that the user lost at the same time when round upgrade
    #         if x_enemy4 < x + 20 or x_enemy4 > x - 20 | y_enemy3 < y + 20 or y_enemy3 > y - 20\
    #         | y_enemy4 < y + 20 or y_enemy4 > y - 20:
    #             x_enemy4 = rand(0,600)
    #             y_enemy3 = rand(0,500)
    #             y_enemy4 = rand(0,500)
    #         else:
    #             avoid_flag = 0

    #     enemyfish1 = canvas.create_image(x_enemy3, y_enemy3, image = fish_enemy3)
    #     enemyfish2 = canvas.create_image(x_enemy4, y_enemy4, image = fish_enemy4)

    #     # f3 & f4 are for round two ocean fish
    #     ocean_fish_move_righttoleft(f3, f4, enemyfish1, enemyfish2)


# class FishMove(FishAppear):
#     """docstring for FishMove"""
#     def __init__(self, master):
#         super(FishMove, self).__init__(master)
#         # self._master = master







def main():
    """The main() function is used to construct a gui interface for the user."""
    # window1 for main menu; window2 for main game

    window1 = Tk()
    window1.title("MAIN MENU")
    # configure_window(window1)
    # main_game = MainFishGame(window1)
    main_menu = MainMenu(window1)
    # Construct the menu bar for the fish game.
    window1.mainloop()

    window_for_log_in = Tk()
    window_for_log_in.grab_set()
    window_for_log_in.geometry("500x300")
    window_for_log_in.title("LOG IN")
    # LogInSetting.Log_In_Page(window_for_log_in)
    LogInSetting(window_for_log_in)
    # second tk window:
    window2 = Tk()
    window2.title("MAIN GAME")
    # window.focus_set()
    # window2.grab_set()

    configure_window(window2)  #name 'window2' is not defined
    photo_pool()

    # window2.grab_set() # useless

    # start the main fish game
    main_game = MainFishGame(window2)
    window2.mainloop()


if __name__ == "__main__":
    main()
