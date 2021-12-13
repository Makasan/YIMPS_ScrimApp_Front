#####Real
import base64
from tkinter import*
from tkinter import ttk
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import hashlib
import requests
import time
from datetime import datetime
import os

window_width = 1280
window_height = 720
win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")
back_ground = 'white'
checkstart = True

global thisPath
thisPath=os.path.dirname(os.path.abspath(__file__))
thisPath=thisPath.replace("\\",'/')



Logo_Image = ImageTk.PhotoImage((Image.open( thisPath + "/Image/Icon/Logo.png")).resize((50,50)))  
hiddenpass_Image = ImageTk.PhotoImage((Image.open(thisPath + "/Image/Icon/hidden.png")).resize((10,10)))
showpass_Image = ImageTk.PhotoImage((Image.open(thisPath + "/Image/Icon/show.png")).resize((10,10)))
BGimage = ImageTk.PhotoImage(Image.open(thisPath + "/BG/XboxBG.jpeg").resize((window_width,window_height)))
searchTeam_Text = ImageTk.PhotoImage(Image.open(thisPath + "/PicText/SearchTeam.png").resize((130,25)))
sortBy_Text = ImageTk.PhotoImage(Image.open(thisPath + "/PicText/SortBy.png").resize((100,20))) #adBox.png
adBox_Picture = ImageTk.PhotoImage(Image.open(thisPath + "/BG/adBox.png").resize((120,450)))
underbar_Picture = ImageTk.PhotoImage(Image.open(thisPath + "/BG/Underbar.png").resize((1280,50)))
scrimTemp_picture = ImageTk.PhotoImage(Image.open(thisPath + "/BG/kawaii2.png").resize((40,40)))
# def clock():
#     global dayNow
#     dayNow = time.strftime("%d")   
#     global monthNow
#     monthNow = time.strftime("%m")
#     global yearNow
#     yearNow = time.strftime("%Y")
#     global minuteNow
#     minuteNow = time.strftime("%M")
#     global hourNow
#     hourNow = time.strftime("%H")

#     time_label =  Label(win).place(x=1000,y=1000)
#     time_label.after(500, clock)

def Login ():
    
    win['bg'] = "black"
    background_login = Label(win,image=BGimage)
    background_login.place(width=window_width,height=window_height)

    check = False
    test_Register =[]
    login_Frame = LabelFrame(win)
    mycanvas_login = Canvas(login_Frame,bg="pink")
    mycanvas_login.pack(fill=BOTH, expand=YES)
    mycanvas_login.bind('<Configure>', lambda e: mycanvas_login.configure(scrollregion = mycanvas_login.bbox('all')))
    myFrame_login = Frame(mycanvas_login) # ใช้
    mycanvas_login.create_window((0,0), window=myFrame_login, anchor=NW)
    login_Frame.place(x=350,y=60,height=600,width=600)

    def login_page():
        
        check_pass = False

        clear_Label = Label(mycanvas_login,font=('Arial',50),bg=back_ground)
        clear_Label.place(x=0,y=0,width=600,height=600)
        login_Label = Label(mycanvas_login,text="Login",font=('Arial',50),bg=back_ground)
        login_Label.place(x=220,y=50)
        input_UserName = Entry(mycanvas_login, font=('Arial',15),bg=back_ground)
        input_UserName.insert(0,"MakasanKawaii") #####################################################
        input_UserName.place(x=270,y=200,width=300,height=30)
        #input_UserName.get
        #input_UserName.insert(0,"        8-16 character ")
        input_Label = Label(mycanvas_login,text="User Name       :",font=('Arial',20),bg=back_ground)
        input_Label.place(x=50,y=200,width=210,height=30)

        input_Password = Entry(mycanvas_login, show="*" ,font=('Arial',15),bg=back_ground)
        input_Password.insert(0,"123456789")  #####################################################
        input_Password.place(x=270,y=250,width=300,height=30)
        #input_Password.get
        #input_Password.insert(0,"Password")
        Password_Label = Label(mycanvas_login,text="Password         :",font=('Arial',20),bg=back_ground)
        Password_Label.place(x=50,y=250,width=210,height=30)

        def checkLogin():
            password = hashlib.md5(input_Password.get().encode("utf-8"))
            global id_user
            id_user = {
                "username": str(input_UserName.get()) , 
                "password": str(password.hexdigest()) , 
            }
            respone = requests.get("http://34.124.169.53:8000/api/login",data=id_user, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            #print(respone.text)
            checkID = dict(respone.json()) 
            #print(checkID)
            print("UID = " + str(checkID["currentUserID"]))
            if 'Wrong Username' in checkID['message']  :
                warning_UserName = Label(mycanvas_login,text="User Name Incorrect",font=('Arial',15),bg=back_ground,fg="red")
                warning_UserName.place(x=10,y=300,width=250,height=30)
            elif 'Wrong Password' in checkID["message"] :
                warning_Password = Label(mycanvas_login,text="Password Incorrect",font=('Arial',15),bg=back_ground,fg="red")
                warning_Password.place(x=10,y=300,width=250,height=30)
            else:
                #print("Go Home")
                #mycanvas_login.destroy()
                global user
                user = dict(respone.json()) 
                #print(user['teamID'])
                login_Frame.destroy()
                #ScrimBorad()
                Profile()
                #HomePage()
                

        def showpass():
            input_Password.config(show='')
            showpass_Button = Button(mycanvas_login,image=showpass_Image,command=hiddenpass,text="")
            showpass_Button.place(x=575,y=255,width=20,height=20)
        #input_ConfirmPass.insert(0,"Confirm Password")
        def hiddenpass():
            input_Password.config(show='*')
            showpass_Button = Button(mycanvas_login,image=hiddenpass_Image,command=showpass,text="")
            showpass_Button.place(x=575,y=255,width=20,height=20)

        register_Button = Button(mycanvas_login,text="Register", font=('Arial',15),command=register_page)
        register_Button.place(x=500,y=10,width=90,height=30)
        login_Button = Button(mycanvas_login,text="Login", font=('Arial',15),command=checkLogin)
        login_Button.place(x=400,y=290,width=80,height=35)

        if check_pass == False:
            hiddenpass()
            check_pass = True


    def register_page():
        checkShowpass = True
        def register():
            warning = Label(mycanvas_login,text="                                          ",font=('Arial',15),bg=back_ground)
            warning.place(x=0,y=350,width=400,height=30)
            print(len(input_UserName.get()))
            if input_UserName.get() == '' or int(len(input_UserName.get())) < 8 or int(len(input_UserName.get()) > 16):
                warning = Label(mycanvas_login,text="User Name has 8-16 characters",font=('Arial',15),fg="red",bg=back_ground)
                warning.place(x=10,y=350,width=280,height=30)
            elif input_Password.get() == ''or int(len(input_Password.get())) < 8 or int(len(input_Password.get()) > 16):
                warning = Label(mycanvas_login,text="Password has 8-16 characters",font=('Arial',15),fg="red",bg=back_ground)
                warning.place(x=10,y=350,width=280,height=30)
            elif input_Password.get() != input_ConfirmPass.get() :
                warning = Label(mycanvas_login,text="Passwords do not match",font=('Arial',15),fg="red",bg=back_ground)
                warning.place(x=0,y=350,width=250,height=30)
            else:
                test_Register.append(input_UserName.get())
                test_Register.append(input_Password.get())
                #print(test_Register)
                password = hashlib.md5(input_Password.get().encode("utf-8")) 
                dict = {
                "username": str(input_UserName.get()) , 
                "password": str(password.hexdigest()) , 
                }
                respone = requests.post("http://34.124.169.53:8000/api/createUser", data=dict, headers={'Content-Type': 'application/x-www-form-urlencoded'})
                #print(respone.text)
                #print(dict)
                if "username is already exist" in respone.text:
                    warning = Label(mycanvas_login,text="Username is already !",font=('Arial',15),fg="red",bg=back_ground)
                    warning.place(x=0,y=350,width=250,height=30)
                    dict = {
                        "username": "",
                        "password": ""
                    }
                else:
                    login_page()

        def showpass_register():
            input_Password.config(show='')
            input_ConfirmPass.config(show='')
            showpass_Button = Button(mycanvas_login,image=showpass_Image,command=hiddenpass_register,text="")
            showpass_Button.place(x=575,y=255,width=20,height=20)
        
        def hiddenpass_register():
            input_Password.config(show='*')
            input_ConfirmPass.config(show='*')
            showpass_Button = Button(mycanvas_login,image=hiddenpass_Image,command=showpass_register,text="")
            showpass_Button.place(x=575,y=255,width=20,height=20)

        
        #clear_Label = Label(mycanvas_login,font=('Arial',50),bg="pink")
        #clear_Label.place(x=200,y=50)
        clear_Label = Label(mycanvas_login,font=('Arial',50),bg=back_ground)
        clear_Label.place(x=0,y=0,width=600,height=600)
        Register_Label = Label(mycanvas_login,text="Register",font=('Arial',50),bg=back_ground)
        Register_Label.place(x=200,y=50)

        input_UserName = Entry(mycanvas_login, font=('Arial',15),bg=back_ground)
        input_UserName.place(x=270,y=200,width=300,height=30)
        #input_UserName.insert(0," 8-16 character ")
        input_Label = Label(mycanvas_login,text="User Name       :",font=('Arial',20),bg=back_ground)
        input_Label.place(x=50,y=200,width=210,height=30)

        input_Password = Entry(mycanvas_login, show="*" ,font=('Arial',15),bg=back_ground)
        input_Password.place(x=270,y=250,width=300,height=30)
        #input_Password.insert(0,"Password")
        Password_Label = Label(mycanvas_login,text="Password         :",font=('Arial',20),bg=back_ground)
        Password_Label.place(x=50,y=250,width=210,height=30)


        input_ConfirmPass = Entry(mycanvas_login, show="*",font=('Arial',15), bg=back_ground)
        input_ConfirmPass.place(x=270,y=300,width=300,height=30)
        
        ConfirmPass_Label = Label(mycanvas_login,text="Confirm Password :",font=('Arial',20),bg=back_ground)
        ConfirmPass_Label.place(x=10,y=300,width=250,height=30)

        login_backpage = Button(mycanvas_login,text="login", font=('Arial',15),bg=back_ground,command=login_page)
        login_backpage.place(x=5,y=10,width=90,height=30)
        register_Button = Button(mycanvas_login,text="Register", font=('Arial',15),command=register)
        #register_Button.place(x=150,y=500,width=150,height=50)
        register_Button.place(x=250,y=500,width=150,height=50)

        if checkShowpass:
            hiddenpass_register()
            checkShowpass = False


    if check == False:
        login_page()
        check = True

def ScrimBorad ():
    respone = requests.get("http://34.124.169.53:8000/api/login",data=id_user, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    user = dict(respone.json()) 
    clear = Label(win,bg="white").place(x=0,y=0,width=window_width,height=window_height) 
    if user['teamID'] != '':
        responeTeam = requests.get("http://34.124.169.53:8000/api/getteam/"+user['teamID'])
        myTeam = (dict(responeTeam.json())['reqTeam']['teamData']['teamName'])
        myTeamRank = (dict(responeTeam.json())['reqTeam']['teamData']['teamRank'])
    #global data_backEnd
    #print(user)
    #win['bg'] = "#344150"
    
    background_Scrim = Label(win,image=BGimage).place(height=window_height,width=window_width) #7e8382
    framLabel = Label(win,bg='white',border=10).place(x=225,y=110,height=500,width=900)
    #backLayer = Label(win,bg="white").place(height=100,width=850,x=220,y=120)
    #background_Scrim = Label(win,image=BGimage_white).place(height=window_height,width=window_width)
    hour_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    for i in range(10,24): hour_list.append(str(i))
    min_list =["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    for i in range(10,60): min_list.append(str(i))
    day_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    for i in range(10,32): day_list.append(str(i))
    month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    year_list = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
    count_month = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    for i in range(10,32): count_month.append(str(i))


    respone = requests.get("http://34.124.169.53:8000/api/getallposts")
    data_backEnd = dict(respone.json()) 
    #print("KUY")

    def KMPSearch(pat, txt):
        M = len(pat)
        N = len(txt)
        lps = [0]*M
        j = 0 
        computeLPSArray(pat, M, lps)
        i = 0 
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            if j == M:
                return True
            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return False
  
    def computeLPSArray(pat, M, lps):
        len = 0 
        lps[0] 
        i = 1
        while i < M:
            if pat[i]== pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len-1]
                else:
                    lps[i] = 0
                    i += 1

    def sortScrimBoard(choice):
        choice = dropdown_SortBy.get()
        respone = requests.get("http://34.124.169.53:8000/api/getposts-sorted",data={'method':str(choice)}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        #print(dropdown_SortBy.get())
        
        data_backEnd = dict(respone.json()) 
        print("SortDatabase")
        print(data_backEnd["allPosts"])
        show_boardscrim(data_backEnd)

    def searchTeam():
        teamSearch = input_SearchBox.get()
        show_boardscrim(data_backEnd,teamSearch)
        

    def show_boardscrim(data_backEnd,search = ''):
        coutCol = 0
        coutRow = 0
        clear = Label(myFrame).place(height=1000,width=1000)
        
        print("Search = " + str(search))
        if search != '' :
            for i in data_backEnd["allPosts"]:
                if KMPSearch(str(search),i["teamName"]) and not(i["isReady"]):
                #if str(search) in i["teamName"] :
                    print(i)
                    checkbuttonScrim  = True
                    label_TeamName = Label(myFrame,image=scrimTemp_picture).grid(row=coutRow,column=coutCol,ipadx=0,ipady=10,padx=10)
                    coutCol += 1
                    label_TeamName = Label(myFrame,text='         '+i["teamName"]+'              ',font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                    label_Server = Label(myFrame,text="Server             ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                    for j in l:
                        label = Label(myFrame,text=i[j],font=('Arial',12))
                        label.grid(row=coutRow,column=coutCol)
                        coutCol += 1
                        label_space = Label(myFrame,text='                 ')
                        label_space.grid(row=coutRow,column=coutCol)
                        coutCol += 1
                        #Button(myFrame, text="Button" + str(i)).pack()
                    #label_space = Label(myFrame,text='')
                    #label_space.grid(row=coutRow,column=coutCol)
                    #coutCol += 1
                    id_post = i['id']
                    id_req = i['req']
                    #button_Request = Button(myFrame, text="  Request \n for Scrim",bg=bgl[p],command= lambda: request(i['id']))
                    #print(user['teamID']) 
                    
                    for id_req_i in id_req:
                        # print(id_req_i['teamId'])
                        # print(user['teamID'])
                        if user['teamID'] == id_req_i['teamId']:
                            
                            button_noTeam= Button(myFrame, text=" You already \n Scrim Team",bg="red") 
                            button_noTeam.grid(row=coutRow,column=coutCol,pady=10,padx=0,ipadx=0,ipady=5)
                            checkbuttonScrim = False 
                
                    if user['teamID'] != '':
                        if checkbuttonScrim:
                            if i['createdby'] == user['teamID']:
                                button_ViewRequest = Button(myFrame, text="  View \n Request",command=showMyRequest) 
                                button_ViewRequest.grid(row=coutRow,column=coutCol,pady=10,padx=0,ipadx=0,ipady=5)
                            else:
                                button_Request = Button(myFrame, text="  Request \n for Scrim",command= lambda id_post=id_post:request(id_post)) 
                                button_Request.grid(row=coutRow,column=coutCol,pady=10,padx=0,ipadx=0,ipady=5)
                    coutCol = 0
                    coutRow += 1
        
        else:
            #print(data_backEnd["allPosts"])
            for i in data_backEnd["allPosts"]:
                if not(i["isReady"]):
                    checkbuttonScrim  = True
                    #print("MY ALL POST")
                    #print(i)
                    #print(i['createdby'])
                    label_TeamName = Label(myFrame,image=scrimTemp_picture).grid(row=coutRow,column=coutCol,ipadx=0,ipady=10,padx=10)
                    coutCol += 1
                    label_TeamName = Label(myFrame,text='         '+i["teamName"]+'              ',font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                    label_Server = Label(myFrame,text="Server             ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                    for j in l:
                        label = Label(myFrame,text=i[j],font=('Arial',12))
                        label.grid(row=coutRow,column=coutCol)
                        coutCol += 1
                        label_space = Label(myFrame,text='                 ')
                        label_space.grid(row=coutRow,column=coutCol)
                        coutCol += 1
                        #Button(myFrame, text="Button" + str(i)).pack()
                    #label_space = Label(myFrame,text='')
                    #label_space.grid(row=coutRow,column=coutCol)
                    #coutCol += 1
                    id_post = i['id']
                    id_req = i['req']
                    #button_Request = Button(myFrame, text="  Request \n for Scrim",bg=bgl[p],command= lambda: request(i['id']))
                    #print(user['teamID']) 
                    
                    for id_req_i in id_req:
                        if user['teamID'] == id_req_i['teamId']:
                            #print("You already Scrim")
                            button_noTeam= Button(myFrame, text=" You already \n Scrim Team",bg="red") 
                            #button_noTeam.place(x=300,y=100,height=10000,width=10000)
                            button_noTeam.grid(row=coutRow,column=coutCol,pady=10,padx=0,ipadx=0,ipady=5)
                            checkbuttonScrim = False 
                    
                    if user['teamID'] != '':
                        if checkbuttonScrim:
                            if i['createdby'] == user['teamID']:
                                button_ViewRequest = Button(myFrame, text="  View \n Request",command=showMyRequest) 
                                button_ViewRequest.grid(row=coutRow,column=coutCol,pady=10,padx=0,ipadx=0,ipady=5)
                            else:
                                button_Request = Button(myFrame, text="  Request \n for Scrim",command= lambda id_post=id_post:request(id_post)) 
                                button_Request.grid(row=coutRow,column=coutCol,pady=10,padx=0,ipadx=0,ipady=5)
                    
                    else:
                        button_noTeam= Button(myFrame, text=" You don't \n Have Team") 
                        button_noTeam.grid(row=coutRow,column=coutCol,pady=10,padx=0,ipadx=0,ipady=5)
                    coutCol = 0
                    coutRow += 1
       
            
            

    def request(id_post) :
        dict = {
            "teamId" : user["teamID"],
        }
        print("idPost = "+ str(id_post))
        print("teamID = " + str(user["teamID"]))
        #respone = requests.post("http://34.124.169.53:8000/api/getteam/teamid", data=dict, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        respone = requests.put("http://34.124.169.53:8000/api/request-to-scrim/" + str(id_post), data=dict, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        print(respone.text)
        ScrimBorad()

    
    def showMyRequest():
        
        clear = Label(myFrame).place(height=1000,width=1000)
        clearsort = Label(win,bg=back_ground).place(relx=0.45,rely=0.18,height=70,width=170)
        #myFrame.destroy()
        # myFrame = Frame(mycanvas)
        # mycanvas.create_window((0,0), window=myFrame, anchor=NW)
        checkhavePost = True
        coutCol = 0
        coutRow = 0
        showMyList_Button.destroy()
        search_Box.destroy()
        input_SearchBox.destroy()
        addTeam_Button.destroy()

        allMyList_Button = Button(win,text="Show All",command=ScrimBorad)
        allMyList_Button.place(x=1000,y=150,width=60,height=45)
        myPost_Label = Label(win,text="Post All My Request",bg=back_ground,font=('Arial',20))
        myPost_Label.place(x=250,y=160,width=320,height=45)
        #showMyList_Button = Button(win,text="Show",command=showMyRequest)
        #showMyList_Button.place(x=980,y=150,width=45,height=45)
        
        print(data_backEnd["allPosts"])
        for i in data_backEnd["allPosts"]:
            if i['createdby'] == user['teamID'] and not(i["isReady"]):
                for j in i["req"]:
                    print()
                    responeTeam = requests.get("http://34.124.169.53:8000/api/getteam/"+j['teamId'])
                    data = dict(responeTeam.json())
                    enemyTeam = data['reqTeam']['teamData']['teamName']
                    # print(data['reqTeam']['teamData'])
                    checkhavePost = False
                    # print("ShowMyReQuest")
                    label_TeamName = Label(myFrame,image=scrimTemp_picture).grid(row=coutRow,column=coutCol,ipadx=0,ipady=10,padx=10)
                    coutCol += 1
                    label_TeamName = Label(myFrame,text='      '+enemyTeam+'  ',font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                    label_Server = Label(myFrame,text="Server",font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                    label_Time = Label(myFrame,text='           '+i["time"],font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                    label_Date = Label(myFrame,text='           '+i["date"],font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                    label_TeamRank = Label(myFrame,text='           '+data['reqTeam']['teamData']['teamRank'],font=('Arial',12)).grid(row=coutRow,column=coutCol)
                    coutCol += 1
                   
                    # for k in l:
                    #     label = Label(myFrame,text='           '+i[j][k],font=('Arial',12))
                    #     label.grid(row=coutRow,column=coutCol)
                    #     coutCol += 1
                        # label_space = Label(myFrame,text='')
                        # label_space.grid(row=coutRow,column=coutCol)
                        # coutCol += 1
                    #coutCol += 1
                    id_post = i['id']
                    #button_Request = Button(myFrame, text="  Request \n for Scrim",bg=bgl[p],command= lambda: request(i['id'])) 
                    if i['createdby'] == user['teamID']:
                        button_ViewRequest = Button(myFrame, text="View \n Request",command=lambda id_post=id_post:viewMyRequest(id_post)) 
                        #button_ViewRequest.place(x=750,y=10,height=50)
                        button_ViewRequest.grid(row=coutRow,column=coutCol,pady=10,padx=50,ipadx=0,ipady=5)
                    coutCol = 0
                    coutRow += 1
        if checkhavePost:
            noTeam_label = Label(win,text="You don't have a post team",font=('Arial',20),fg='red')
            noTeam_label.place(x=450,y=350,height=50,width=500)
        #boradFrame.place(x=250,y=210,height=350,width=850)
    
    def viewMyRequest (id_post):
        def goShowMyRequest():
            #clear = Label(myFrame,bg=back_ground).place(height=1000,width=1000)
            boradFrame.place(x=250,y=210,height=350,width=850)
            boradMyRequest_Frame.place(x=2500,y=2200,height=70,width=850)
            # respone = requests.get("http://34.124.169.53:8000/api/getallposts")
            # data_backEnd = dict(respone.json()) 
            # show_boardscrim(data_backEnd)
            showMyRequest()
            
            

        def accept_Request(teamID):
            dictData = {
                'teamId' : teamID
                }
            #print(dictData)
            respone_accept = requests.put("http://34.124.169.53:8000/api/post/"+id_post+"/accept-request", data=dictData, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            #print(respone_accept.text)
            ScrimBorad ()
            
        def reject_Request(teamID):
            #print("RejectPost")
            dictData = {
                'teamId' : teamID
                }
            respone_reject = requests.put("http://34.124.169.53:8000/api/post/"+id_post+"/reject-request", data=dictData, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            #print(respone_reject.text)
            ScrimBorad ()

        clear = Label(myFrame).place(height=1000,width=1000)
        boradMyRequest_Frame = LabelFrame(win)
        mycanvas3 = Canvas(boradMyRequest_Frame)
        mycanvas3.pack(side=LEFT, fill=BOTH, expand=YES)
        myRequest = Frame(mycanvas3) # ใช้ตัวนี้
        mycanvas3.create_window((0,0), window=myRequest, anchor=NW)
        coutCol = 0
        coutRow = 0
        respone = requests.get("http://34.124.169.53:8000/api/getpost/"+str(id_post))
        #print(dict(respone.json()))
        dataPost = dict(respone.json())['reqPost']['postData']
        teamDataPost = (dict(respone.json())['reqPost']['req'])
        #print(teamDataPost)

        label_TeamName = Label(myRequest,image=scrimTemp_picture).grid(row=coutRow,column=coutCol,ipadx=20,ipady=0,padx=10,pady=10)
        coutCol += 1
        label_TeamName = Label(myRequest,text='        '+dataPost['teamName']+'             ',font=('Arial',12)).grid(row=coutRow,column=coutCol)
        coutCol += 1
        label_Server = Label(myRequest,text="Server",font=('Arial',12)).grid(row=coutRow,column=coutCol)
        coutCol += 1
        label_Time = Label(myRequest,text='              '+dataPost['time'],font=('Arial',12)).grid(row=coutRow,column=coutCol)
        coutCol += 1
        label_Date = Label(myRequest,text='              '+dataPost['date'],font=('Arial',12)).grid(row=coutRow,column=coutCol)
        coutCol += 1
        label_teanRank = Label(myRequest,text='              '+dataPost['teamRank'],font=('Arial',12)).grid(row=coutRow,column=coutCol)

        backAllBorad_Button = Button(boradMyRequest_Frame,text="Back",bg="pink",command=goShowMyRequest)
        backAllBorad_Button.place(x=750,y=5,height=50,width=60)
        print(teamDataPost)
        if teamDataPost != [] :
            coutCol = 0
            teamScrimID = (teamDataPost[0])['teamId']
            responeTeam = requests.get("http://34.124.169.53:8000/api/getteam/"+teamScrimID)
            #print(dict(responeTeam.json()))
            scrimTeam = (dict(responeTeam.json())['reqTeam']['teamData'])
            #print(scrimTeam)

            for i in range(len(teamDataPost)):
                # print("teamData post")
                # print(i)
                label_TeamName = Label(myFrame,image=scrimTemp_picture).grid(row=coutRow,column=coutCol,ipadx=0,ipady=10,padx=10)
                coutCol += 1
                label_TeamName = Label(myFrame,text=scrimTeam["teamName"],font=('Arial',12)).grid(row=coutRow+i,column=coutCol)
                coutCol += 1
                label_Server = Label(myFrame,text="Server",font=('Arial',12)).grid(row=coutRow+i,column=coutCol)
                coutCol += 1
                label_Time = Label(myFrame,text=dataPost['time'],font=('Arial',12)).grid(row=coutRow+i,column=coutCol)
                coutCol += 1
                label_Date = Label(myFrame,text=dataPost['date'],font=('Arial',12)).grid(row=coutRow+i,column=coutCol)
                coutCol += 1
                label_teanRank = Label(myFrame,text=scrimTeam['teamRank'],font=('Arial',12)).grid(row=coutRow+i,column=coutCol)
                
                button_Reject = Button(myFrame, text="Reject",bg='red',command=lambda teamScrimID=teamScrimID:reject_Request(teamScrimID)) 
                button_Reject.place(x=770,y=10,height=50,width=55)
                button_Accept = Button(myFrame, text="Accept",bg='green',command=lambda teamScrimID=teamScrimID:accept_Request(teamScrimID)) 
                button_Accept.place(x=710,y=10,height=50,width=55)
                coutCol = 0
        else:
            noTeam_label = Label(myFrame,text="No one wants to play with you ! ei ei",font=('Arial',20),fg='red')
            noTeam_label.place(x=225,y=100)
        boradFrame.place(x=250,y=300,height=300,width=850)
        boradMyRequest_Frame.place(x=250,y=220,height=70,width=850)
    
    def addTeam () :
        
        coutCol = 0
        coutRow = 0
        hour = StringVar()
        hour.set("Hr")
        #drop_Hr = OptionMenu(boradAddFrame, hour, *hour_list)
        drop_Hr = ttk.Combobox(boradAddFrame, width = 3, textvariable = hour,state='readonly')
        drop_Hr['values'] = hour_list
        minute = StringVar()
        minute.set("Min")
        #drop_min = OptionMenu(boradAddFrame, min, *min_list)
        drop_min = ttk.Combobox(boradAddFrame, width = 3, textvariable = minute,state='readonly')
        drop_min['values'] = min_list

        day = StringVar()                                                       
        day.set("Day")
        drop_day = ttk.Combobox(boradAddFrame, width = 3, textvariable = day,state='readonly')
        drop_day['values'] = day_list
        month = StringVar()
        month.set("Month")
        drop_month = ttk.Combobox(boradAddFrame, width = 3, textvariable = month,state='readonly')
        drop_month['values'] = month_list
        year = StringVar()
        year.set("Year")
        drop_year = ttk.Combobox(boradAddFrame, width = 3, textvariable = year,state='readonly')
        drop_year['values'] = year_list
            

        boradFrame.place(x=250,y=300,height=300,width=850)
        boradAddFrame.place(x=250,y=220,height=70,width=850)
        

        emty_label = Label(myAddBorad,bg='black')
        emty_label.grid(row=coutRow,column=coutCol,ipadx=20,ipady=10,padx=10,pady=10)
        coutCol += 1
        myteam_label = Label(myAddBorad,text=myTeam,font=('Arial',12))
        myteam_label.grid(row=coutRow,column=coutCol,ipadx=20,ipady=10,padx=10,pady=10)
        coutCol += 1
        mysever_label = Label(myAddBorad,text="JP",font=('Arial',12))
        mysever_label.grid(row=coutRow,column=coutCol,ipadx=20,ipady=10,padx=10,pady=10)
        #myteamrank_label = Label(boradAddFrame,text=myTeamRank,font=('Arial',12))
        #myteamrank_label.place(x=600,y=15,height=30,width=80)

        # for i in range(1,3):
        #     emty_label = Label(myAddBorad,text=myData[i-1],font=('Arial',12))
        #     emty_label.grid(row=coutRow,column=coutCol+i,ipadx=20,ipady=10,padx=10,pady=10)
        # emty_label = Label(boradAddFrame,text=myData[2],font=('Arial',12))
        # emty_label.place(x=600,y=15,height=30,width=80)
        #drop_Hr.grid(row=coutRow,column=coutCol+2,ipadx=20,ipady=10,padx=10,pady=10)
        #drop_min.grid(row=coutRow,column=coutCol+4,ipadx=20,ipady=10,padx=10,pady=10)
        #drop_day.grid(row=coutRow,column=coutCol+5,ipadx=20,ipady=10,padx=10,pady=10)
        #drop_month.grid(row=coutRow,column=coutCol+6,ipadx=20,ipady=10,padx=10,pady=10)
        #drop_year.grid(row=coutRow,column=coutCol+7,ipadx=20,ipady=10,padx=10,pady=10)

        drop_Hr.place(x=290,y=15,height=30,width=40)
        drop_min.place(x=335,y=15,height=30,width=50)
        drop_day.place(x=400,y=15,height=30,width=50)
        drop_month.place(x=455,y=15,height=30,width=50)
        drop_year.place(x=510,y=15,height=30,width=50)
        
            ######## บัค for out of rang แล้ว แสดงผลปกติ #########
        
        # for i in range(5,7):
        #     emty_label = Label(myAddBorad,text=myData[i-1],font=('Arial',12))
        #     emty_label.grid(row=coutRow,column=coutCol+i,ipadx=20,ipady=10,padx=10,pady=10)

            ######## บัค for out of rang แล้ว แสดงผลปกติ #########
        def confirm() :
            clewarning_1 = Label(boradAddFrame,text="                  ")
            clewarning_1.place(x=420,y=45,height=20,width=100)
            clewarning_2 = Label(boradAddFrame,text="                  ")
            clewarning_2.place(x=290,y=45,height=20,width=100)
            #print(count_month)
            check_error = False
            #if month.get() in month_list and day.get() in day_list and year.get() in year_list and hour.get() in hour_list and minute.get() in min_list :
                  

            if str(month.get()) in ["01","03","05","07","08","10","12"] :  #31
                if str(day.get()) not in count_month:
                    warning = Label(boradAddFrame,text="Invalid date",fg='red')
                    warning.place(x=420,y=45,height=20,width=100)
                    check_error = True 
            elif str(month.get()) in ["02"] :  # 28
                if str(day.get()) not in count_month[0:29]:
                    warning = Label(boradAddFrame,text="Invalid date",fg='red')
                    warning.place(x=420,y=45,height=20,width=100)
                    check_error = True 
            elif str(month.get()) in ["04","06","09","11"]: # 30
                if str(day.get()) not in count_month[0:31]:
                    warning = Label(boradAddFrame,text="Invalid date",fg='red')
                    warning.place(x=420,y=45,height=20,width=100)
                    check_error = True 
            else:
                warning = Label(boradAddFrame,text="Invalid date",fg='red')
                warning.place(x=420,y=45,height=20,width=100)
                check_error = True 
            #print(str(minute.get()))
            #print(str(hour.get()))
            if (str(minute.get()) not in min_list):
                warning = Label(boradAddFrame,text="Invalid time",fg='red')
                warning.place(x=290,y=45,height=20,width=100)
                check_error = True
            elif (str(hour.get()) not in hour_list):
                warning = Label(boradAddFrame,text="Invalid time",fg='red')
                warning.place(x=290,y=45,height=20,width=100)
                check_error = True
                
            if check_error == False:
                input_dateTime = datetime(int(year.get()),int(month.get()),int(day.get()),int(hour.get()),int(minute.get()))
                today_dateTime = datetime.now()
                print(today_dateTime < input_dateTime)
                if today_dateTime > input_dateTime :
                    warning = Label(boradAddFrame,text="Invalid date",fg='red')
                    warning.place(x=420,y=45,height=20,width=100)
                    check_error = True 
            if check_error == False:

                responeTeam = requests.get("http://34.124.169.53:8000/api/getteam/"+user['teamID'])
                #print("responeTeam")
                #print(dict(responeTeam.json()))
                myTeam = (dict(responeTeam.json())['reqTeam']['teamData']['teamName'])
                #print(myTeam)
                time = str(hour.get()) + ":" + str(minute.get())
                date = str(day.get()) + "/" + str(month.get()) + "/" + str(year.get())
                dictData = {
                "date": date , 
                "time":  time ,
                "createdby": str(user['teamID']),
                "teamName" : myTeam
                }
                #print(dictData)
                respone = requests.post("http://34.124.169.53:8000/api/createpost", data=dictData, headers={'Content-Type': 'application/x-www-form-urlencoded'})
                #print(respone.text)
                warning = Label(boradAddFrame,text="                      ")
                warning.place(x=420,y=45,height=20,width=100)
                boradFrame.place(x=250,y=210,height=350,width=850)
                boradAddFrame.place(x=1000,y=1000)
                respone = requests.get("http://34.124.169.53:8000/api/getallposts")
                data_backEnd = dict(respone.json()) 
                show_boardscrim(data_backEnd)
            


        def cancel() :
            warning = Label(boradAddFrame,text="                      ")
            warning.place(x=420,y=45,height=20,width=100)
            boradFrame.place(x=250,y=210,height=350,width=850)
            boradAddFrame.place(x=1000,y=1000)
        
        confirmAdd = Button(boradAddFrame,text="Comfirm",bg="pink",command=confirm)
        confirmAdd.place(x=710,y=5,height=50,width=60)
        cancelAdd = Button(boradAddFrame,text="Cancel",bg="pink",command=cancel)
        cancelAdd.place(x=780,y=5,height=50,width=60)

        # label_TeamName = Label(boradAddFrame,bg='black').grid(row=coutRow,column=coutCol,ipadx=20,ipady=10,padx=10)
        # coutCol += 1
        # label_TeamName = Label(boradAddFrame,text="   Team Name          ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
        # coutCol += 1
        # label_Server = Label(boradAddFrame,text="Server          ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
        # coutCol += 1
        

    search_Box = Label(win,image=searchTeam_Text,bd=0)
    search_Box.place(relx=0.2,rely=0.18)
    input_SearchBox = Entry(win, width=20,font=('Arial',15))
    input_SearchBox.place(relx=0.2,rely=0.23)
    search_button = Button(win,text="Search",command=searchTeam)
    search_button.place(relx=0.4,rely=0.23)
    if user["teamID"] != '':
        addTeam_Button = Button(win,text="Add",command=addTeam)                                         # Add Team
        addTeam_Button.place(x=1040,y=150,width=45,height=45)
        showMyList_Button = Button(win,text="Show",command=showMyRequest)
        showMyList_Button.place(x=980,y=150,width=45,height=45)



    #########################################    Test Frame ScrimBorad ####################################
    boradFrame = LabelFrame(win)
    mycanvas = Canvas(boradFrame)
    mycanvas.pack(side=LEFT, fill=BOTH, expand=YES)
    myScrollbar = ttk.Scrollbar(boradFrame, orient=VERTICAL, command=mycanvas.yview)
    myScrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.config(yscrollcommand=myScrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    myFrame = Frame(mycanvas)
    mycanvas.create_window((0,0), window=myFrame, anchor=NW)
    boradFrame.place(x=250,y=210,height=350,width=850)   # height 300 เหลือ 4 ทีม

    boradAddFrame = LabelFrame(win)
    mycanvas2 = Canvas(boradAddFrame)
    mycanvas2.pack(side=LEFT, fill=BOTH, expand=YES)
    myAddBorad = Frame(mycanvas2)
    mycanvas2.create_window((0,0), window=myAddBorad, anchor=NW)




    #wrapper1.place(x=250,y=300,height=300,width=850) 
    #sortType = [ "Team Name", "Server", "Rank", "Date&Time", "Rating"]
    sortType = ["rank", "date"]
    l = ["time","date","teamRank"]

    start = False
    sortby_Label = Label(win,image=sortBy_Text,bd=0)                          #Sort By 
    sortby_Label.place(relx=0.49,rely=0.18)
    dropdown_SortBy = StringVar()
    dropdown_SortBy.set(sortType[1])
    drop = OptionMenu(win, dropdown_SortBy, *sortType, command=sortScrimBoard)
    drop.place(relx=0.5,rely=0.23)
    #Button(win,text='Sort',font=('Arial',20),command = sortScrimBoard).place(relx=0.6,rely=0.2)
    adBox = Label(win, image=adBox_Picture)
    adBox.place(relx=0.03,rely=0.2)

    if start == False:
        show_boardscrim(data_backEnd)
        start = True

    #########################################    Test Frame ScrimBorad ####################################
    frame_Topbar = Frame(win, width=window_width, height=70,bg='#232323')
    frame_Topbar.place(relx=0,rely=0)
    frame_Underbar = Label(win, image=underbar_Picture,bd=0)
    frame_Underbar.place(relx=0,rely=0.93)
    

    button_Home = Button(win, text='Home Page',font=('Arial',12),command=HomePage)
    button_Home.place(x=100,y=10,height=50,width=120)

    label_stay = Label(win,bg='#b20000')
    label_stay.place(x=260,y=0,height=70,width=170)
    button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',12),command=ScrimBorad)
    button_Scrim.place(x=270,y=10,height=50,width=150)

    button_Team = Button(win, text='Create Team Page',font=('Arial',12),command=CreateTeam)
    button_Team.place(x=470,y=10,height=50,width=150)
    button_Profile = Button(win, text='Profile Page',font=('Arial',12),command=Profile)
    button_Profile.place(x=1015,y=10,height=50,width=120)

    logo_profile = Label(win,image=logo_profile_Image,bd=0)
    logo_profile.place(x=1180,y=5,width=60,height=60)
    logo_label = Label(win,image=Logo_Image)
    logo_label.place(x=30,y=10,height=50,width=50)


def Profile():
    respone = requests.get("http://34.124.169.53:8000/api/login",data=id_user, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    user = dict(respone.json()) 
    clear = Label(win,image=BGimage).place(x=0,y=0,width=window_width,height=window_height) 
    def updateProfile():
        download_respone = requests.get("http://34.124.169.53:8000/api/getProfileImage/"+str(user["currentUserID"]))
        picture = dict(download_respone.json())
        #print(type(picture["image"]))
        image_ = picture["image"].encode('utf-8')
        image_ = base64.decodebytes(image_)
        download = (thisPath + '/Image/PictureProfile/' + user["currentUserID"] + ".png")
        #print("mynameImage = " + download)
        output = open(download, 'wb')
        output.write(image_)
        output.close()
        
        pathPicture = thisPath + "/Image/PictureProfile/" + user["currentUserID"] + ".png"
        #print(check)
        imagepic = Image.open(pathPicture)
        #print(imagepic)
        global profile_Image
        global logo_profile_Image
        profile_Image = ImageTk.PhotoImage(imagepic.resize((300, 300)))
        logo_profile_Image = ImageTk.PhotoImage(imagepic.resize((50, 50)))
        myProfile_Label = Label(profileFrame, image= profile_Image).place(relx=0.1,rely=0.05)
        #Label(win, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        
    
    rank_list = ['Iron1',
              'Iron2',
              'Iron3',
              'Bronze1',
              'Bronze2',
              'Bronze3',
              'Silver1',
              'Silver2',
              'Silver3',
              'Gold1',
              'Gold2',
              'Gold3',
              'Platinum1',
              'Platinum2',
              'Platinum3',
              'Diamond1',
              'Diamond2',
              'Diamond3',
              'Immortal1',
              'Immortal2',
              'Immortal3',
              'Radiant']  
    
    
    # global profile_Image
    # image = Image.open("Image/" + myID + ".png")
    # profile_Image = ImageTk.PhotoImage(image.resize((300, 300)))

    responeInfoID = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+user["currentUserID"])
    myRank = (dict(responeInfoID.json())['userInfo']['rank'])
    #print(myRank)
    myInfo = dict(responeInfoID.json()['userInfo'])
    #print(user['teamID'])
    if user['teamID'] != '':
        responeTeam = requests.get("http://34.124.169.53:8000/api/getteam/"+user['teamID'])
        #print(dict(responeTeam.json()))
        myTeam = (dict(responeTeam.json())['reqTeam']['teamData']['teamName'])
    else:
        myTeam = ''
    
    #print(myRank)
    # print(myInfo['userInfo']['username'])
    # print(myInfo['userInfo']['bio'])
    # print(myInfo['userInfo']['rank'])
    # print(myInfo['userInfo']['team'])
    profileFrame = LabelFrame(win,bg="black",border=10)
    my_profile = Canvas(profileFrame,bg=back_ground)
    my_profile.pack(side=LEFT, fill=BOTH, expand=YES)
    myFrame = Frame(my_profile)
    my_profile.create_window((0,0), window=myFrame, anchor=NW)
    profileFrame.place(x=150,y=110,height=520,width=1000)
    line_label = Label(profileFrame,bg="gray")
    line_label.place(relx=0.5,rely=0,relheight=1,relwidth=0.01)


    # myProfile_Label = Label(profileFrame, image= profile_Image,bg=back_ground)
    # myProfile_Label.place(relx=0.1,rely=0.05) #x=100,y=30
    name_Label = Label(profileFrame,text="Name :",font=('Arial',30),bg=back_ground).place(relx=0.05,rely=0.75)
    myname_Label = Label(profileFrame,text=myInfo['username'],font=('Arial',25),bg=back_ground).place(relx=0.21,rely=0.76)

    name2_Label = Label(profileFrame,text="Name :",font=('Arial',25),bg=back_ground).place(relx=0.55,rely=0.05)
    myname2_Label = Label(profileFrame,text=myInfo['username'],font=('Arial',25),bg=back_ground).place(relx=0.68,rely=0.05)

    rank_Label = Label(profileFrame,text="Rank  :",font=('Arial',25),bg=back_ground).place(relx=0.55,rely=0.15)
    myrank_Label = Label(profileFrame,text=myInfo['rank'],font=('Arial',25),bg=back_ground).place(relx=0.68,rely=0.15)
    team_Label = Label(profileFrame,text="Team :",font=('Arial',25),bg=back_ground).place(relx=0.55,rely=0.25)
    myteam_Label = Label(profileFrame,text=myTeam,font=('Arial',25),bg=back_ground).place(relx=0.68,rely=0.25)

    mybio_Label = Label(profileFrame,text="My Bio  :",font=('Arial',20),bg=back_ground).place(relx=0.55,rely=0.40)
    bio_Label = Label(profileFrame,text=myInfo['bio'],font=('Arial',20),bg=back_ground)
    bio_Label.place(relx=0.55,rely=0.5)
    updateProfile()

    def edit_profile():
        
        my_bio = Text(win, width=60,height=20,font=('Arial',20),bd=3,bg=back_ground)
        my_bio.insert(INSERT,myInfo['bio'])
        my_bio.place(relx=0.54,rely=0.5,height=200,width=400)

        rank = StringVar()
        if myRank == '':
            rank.set("Rank")
        else:
            rank.set(myRank)
        #clear = Label(profileFrame,text='',bg=back_ground,font=('Arial',25)).place(relx=0.68,rely=0.15)
        rankdropdown = ttk.Combobox(profileFrame, textvariable = rank,font=('Arial',15),state='readonly')
        rankdropdown['values'] = rank_list
        rankdropdown.place(relx=0.68,rely=0.16,width=120,height=30)

        #input_Rank = Entry(profileFrame,font=('Arial',20),bd=3)
        #input_Rank.place(relx=0.68,rely=0.155,width=170)

        Chooseprofile_Button = Button(profileFrame,text="Choose Profile",command=ChooseProfile)
        Chooseprofile_Button.place(relx=0.40,rely=0.915)
        uploadprofile_Button = Button(profileFrame,text="Upload Profile",command=uploadProfile)
        uploadprofile_Button.place(relx=0.3,rely=0.915)

        cancelProfile_Button = Button(profileFrame,text="Cancel",command=cancelProfile_edit)
        cancelProfile_Button.place(relx=0.84,rely=0.915)
        confirm_Button = Button(profileFrame,text="Comfirm",command= lambda : comfirm_edit_profile(my_bio.get(1.0,END),rank.get()))
        confirm_Button.place(relx=0.90,rely=0.915)

    def cancelProfile_edit():
        Profile()

    def comfirm_edit_profile(my_bio,input_Rank):
        if input_Rank in rank_list :
            myEditProfile = {
                "_id" : user["currentUserID"],
                "bio": str(my_bio),
                "rank":  str(input_Rank)
            }
            #print(myEditProfile)
            respone = requests.put("http://34.124.169.53:8000/api/editProfile", data=myEditProfile, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            #print(respone.text)
            Profile()
        else:
            warning_edit = Label(profileFrame,text="Invalid Rank",font=('Arial',12),bg=back_ground,fg='red')
            warning_edit.place(relx=0.82,rely=0.17)
            edit_profile()

    def ChooseProfile():
        file_path = askopenfile(mode='rb', filetypes=[('Image Files', '*png')])
        if file_path is not None:
            pass
        data = file_path.read()
        data = base64.encodebytes(data)
        global dictPic
        dictPic = {
            "_id" : user["currentUserID"],
            "pictureProfile" : data
        }
        clear = Label(profileFrame,text="                    ",bg=back_ground,font=('Arial',10))
        clear.place(relx=0.30,rely=0.86)
        choose_warning_Button = Label(profileFrame,text="Already file",font=('Arial',10),bg=back_ground,fg='green')
        choose_warning_Button.place(relx=0.41,rely=0.86)
    def uploadProfile():
        if dictPic == None:
            warning = Label(profileFrame,text="Choose Picture",fg='red',bg=back_ground,font=('Arial',10))
            warning.place(relx=0.30,rely=0.86)
        else:
            #print("Upload")
            respone = requests.put("http://34.124.169.53:8000/api/setProfileImage", data=dictPic, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            updateProfile()
        
    

    
        
    editProfile_Button = Button(profileFrame,text="Edit Profile",command=edit_profile)
    editProfile_Button.place(relx=0.92,rely=0.02)






    frame_Topbar = Frame(win, width=window_width, height=70,bg='#232323')
    frame_Topbar.place(relx=0,rely=0)
    frame_Underbar = Label(win, image=underbar_Picture,bd=0)
    frame_Underbar.place(relx=0,rely=0.93)
    button_Home = Button(win, text='Home Page',font=('Arial',12),command=HomePage)
    button_Home.place(x=100,y=10,height=50,width=120)
    button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',12),command=ScrimBorad)
    button_Scrim.place(x=270,y=10,height=50,width=150)
    button_Team = Button(win, text='Create Team Page',font=('Arial',12),command=CreateTeam)
    button_Team.place(x=470,y=10,height=50,width=150)
    label_stay = Label(win,bg='#b20000')
    label_stay.place(x=1000,y=0,height=70,width=150)
    button_Profile = Button(win, text='Profile Page',font=('Arial',12),command=Profile)
    button_Profile.place(x=1015,y=10,height=50,width=120)

    
    logo_profile = Label(win,image=logo_profile_Image,bd=0)
    logo_profile.place(x=1180,y=5,width=60,height=60)
    logo_label = Label(win,image=Logo_Image)
    logo_label.place(x=30,y=10,height=50,width=50)

def HomePage():
    respone = requests.get("http://34.124.169.53:8000/api/login",data=id_user, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    checkID = dict(respone.json())  
    print(checkID)
    user_id = checkID["currentUserID"]

    respone_1 = requests.get("http://34.124.169.53:8000/api/getNextFiveMatch/"+str(user_id))
    #print(respone_1.text)
    fivemath = dict(respone_1.json())
    temp = Canvas(win, bg=back_ground, width=window_width, height=window_height)
    temp.place(x=1 , y=1)
    background_Home = Label(win,image=BGimage).place(height=window_height,width=window_width)
    framLabel = Label(win,bg=back_ground,bd=10).place(x=220,y=110,height=480,width=930)
    yourScrim_Label = Label(win, text="Your Scrim", font=('Arial',20),bg=back_ground)
    yourScrim_Label.place(x=250,y=135)
    incom_Label = Label(win, text="Incoming Match :  ", font=('Arial',15),bg=back_ground)
    incom_Label.place(x=720,y=150)
    if fivemath['nextFivePost'] != []:    
        match_Incom_Label = Label(win, text=((fivemath['nextFivePost'][0])['teamName'])+"  VS  "+((fivemath['nextFivePost'][0])['enemyTeamName']),fg='red' ,font=('Arial',15),bg=back_ground)
        match_Incom_Label.place(x=900,y=150)
    else:
        match_Incom_Label = Label(win, text="Don't have",fg='red' ,font=('Arial',15),bg=back_ground)
        match_Incom_Label.place(x=900,y=150)
    adBox = Label(win, image=adBox_Picture)
    adBox.place(relx=0.03,rely=0.2)
    
    #########################################    Test Frame Borad ####################################
    wrapper1 = LabelFrame(win)
    mycanvas = Canvas(wrapper1)
    mycanvas.pack(side=LEFT, fill=BOTH, expand=YES)
    """ 
    yScrollbar = ttk.Scrollbar(wrapper1, orient=VERTICAL, command=mycanvas.yview)
    yScrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.config(yscrollcommand=yScrollbar.set)
    """
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
    myFrame = Frame(mycanvas)
    
    mycanvas.create_window((0,0), window=myFrame, anchor=NW)
    wrapper1.place(x=250,y=180,height=370,width=870)
    l = ["Team","date","time","CD"]
    coutCol = 0
    coutRow = 0
    check_VS = True
    #respone = requests.get("http://34.124.169.53:8000/api/getallposts")
    #temp = dict(respone.json()) 
    
    print("Five Post !!!!!!")
    count = 0
    for i in fivemath["nextFivePost"] :
        
        count += 1 
        label_Match = Label(myFrame,text=(str(i['teamName']) +" VS " + str(i['enemyTeamName'])),font=('Arial',15))
        label_Match.grid(row=coutRow,column=coutCol,pady=20,padx=20)
        coutCol += 1
        label_Date = Label(myFrame,text=("   Date : " + str(i['date'])),font=('Arial',15))
        label_Date.grid(row=coutRow,column=coutCol,pady=20,padx=20)
        coutCol += 1
        label_Time = Label(myFrame,text=("   Time : " + str(i['time'])),font=('Arial',15))
        label_Time.grid(row=coutRow,column=coutCol,pady=20,padx=20)
        coutCol += 1
        label_Time = Label(myFrame,text=("Status : "+str(i['countdown'])),font=('Arial',15))
        label_Time.grid(row=coutRow,column=coutCol,pady=20,padx=20)
        coutCol = 0
        coutRow += 1

        


    frame_Topbar = Frame(win, width=window_width, height=70,bg='#232323')
    frame_Topbar.place(relx=0,rely=0)
    frame_Underbar = Label(win, image=underbar_Picture,bd=0)
    frame_Underbar.place(relx=0,rely=0.93)

    label_stay = Label(win,bg='#b20000')
    label_stay.place(x=89,y=0,height=70,width=140)
    button_Home = Button(win, text='Home Page',font=('Arial',12),command=HomePage)
    button_Home.place(x=100,y=10,height=50,width=120)

    button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',12),command=ScrimBorad) 
    button_Scrim.place(x=270,y=10,height=50,width=150)
    button_Team = Button(win, text='Create Team Page',font=('Arial',12),command=CreateTeam)
    button_Team.place(x=470,y=10,height=50,width=150)
    button_Profile = Button(win, text='Profile Page',font=('Arial',12),command=Profile)
    button_Profile.place(x=1015,y=10,height=50,width=120)

    logo_profile = Label(win,image=logo_profile_Image,bd=0)
    logo_profile.place(x=1180,y=5,width=60,height=60)
    logo_label = Label(win,image=Logo_Image)
    logo_label.place(x=30,y=10,height=50,width=50)

def CreateTeam():
    window_width = 1280
    window_height = 720
    UserID = id_user
    back_ground = 'black' #ใส่ BlackGround เป็นรูปด้วย
    pageChoose = True
    ########## เริ่มทำตรงนี้ #############

    respone = requests.get("http://34.124.169.53:8000/api/login",data=id_user, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    checkID = dict(respone.json())
    UserID = checkID["currentUserID"]

    ####################################################
   

    temp = Canvas(win,bg=back_ground, width=window_width, height=window_height)
    temp.place(x=0 , y=0)

    bg_Image = Label(win,image=BGimage)
    #bg_Image = Label(win,bg="red")
    #FFF8F8
    bg_Image.place(x=-2,y=0)


    #---------------------------------------------No Team Page--------------------------------------------------------#

    def noTeamPage():
        Middle_BG = Label(win,bg='white')
        Middle_BG.place(x=340,y=100,width=600,height=590)

        text_label = Label(win,text="Oops You Don't Have Team Yet",font=('Arial',30),bg='white')
        text_label.place(x=360,y=120)

        btn_createTeam_page = Button(win,text="Create Your Team NOW!!!",font=('Arial',20),command=createTeamPage)
        btn_createTeam_page.place(x=470,y=200)

    #---------------------------------------------Create Team Page----------------------------------------------------#

    def createTeamPage():
        Middle_BG = Label(win,bg='white')
        Middle_BG.place(x=150,y=70,width=980,height=650)

        pic_box = Label(win,text="PIC 500x500??",font=('Arial',10),bg='grey')
        pic_box.place(x=170,y=90,width=150,height=150)

        name_team = Label(win,text='Team Name',font=('Arial',12),bg='white')
        name_team.place(x=340,y=90)

        input_teamName = Entry(win,font=('Arial',12),bg='lightgrey')
        input_teamName.place(x=440,y=90,width=200,height=20)

        name_bio = Label(win,text='BIO',font=('Arial',12),bg='white')
        name_bio.place(x=340,y=120)

        bioBox = Text(win,width=570,height=90,font=('Arial',12),bg='lightblue')
        bioBox.place(x=340,y=150,width=570,height=90)

        def createTeamFuction():
            #Get UserID from Login Scene
            respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(UserID))
            checkRank = dict(respone.json())
            teamRank = checkRank['userInfo']['rank']
            teamName = input_teamName.get()
            bio = bioBox.get(1.0,END)
            dictdata = {
                "teamName":teamName,
                "teamRank":teamRank,
                "teamLead":UserID,
                "bio":bio,
            }
            print(dictdata)
            if dictdata['teamName'] == '':
                print("TeamName cannnot be Blank")
            else:
                respone = requests.post("http://34.124.169.53:8000/api/createteam", data=dictdata, headers={'Content-Type': 'application/x-www-form-urlencoded'})
                print(respone.text)
                CreateTeam()
                #teamPage()

        createTeam = Button(win,text='Create Team',command=createTeamFuction)
        createTeam.place(x=580,y=280,width=120,height=40)

    #---------------------------------------------Team Page--------------------------------------------------------#

    def teamPage():
        Middle_BG = Label(win,bg='white')
        Middle_BG.place(x=150,y=70,width=980,height=650)

        # Get TeamName Data
        respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(UserID))
        checkTeamID = dict(respone.json())
        loginUserID = checkTeamID['userInfo']['_id']
        teamID_Create = checkTeamID['userInfo']["team"]

        respone = requests.get("http://34.124.169.53:8000/api/getteam/"+str(teamID_Create))
        teamData = dict(respone.json())
        memberList = teamData['reqTeam']['teamMember']

        nMember = len(memberList)   #Use for FOR-LOOP and Pos of Box
        teamName = teamData['reqTeam']['teamData']['teamName']
        teamRank = teamData['reqTeam']['teamData']['teamRank']
        teamBio = teamData['reqTeam']['teamData']['bio']

        def downloadMemberPicture():
            global memberData
            memberData = []
            for n in range(nMember):
                memberID = memberList[n]['userid']
                download_respone = requests.get("http://34.124.169.53:8000/api/getProfileImage/"+str(memberID))
                picture = dict(download_respone.json())
                image_ = picture["image"].encode('utf-8')
                image_ = base64.decodebytes(image_)
                download = (thisPath + '/Image/PictureProfile/' + memberID + ".png")
                output = open(download, 'wb')
                output.write(image_)
                output.close()  

        def updateMemberPicture():
            for n in range(nMember):
                memberID = memberList[n]['userid']
                pathPicture = thisPath + "/Image/PictureProfile/" + memberID + ".png"
                imagepic = Image.open(pathPicture)
                memberData.append(ImageTk.PhotoImage(imagepic.resize((150, 150))))
                member_Image = Label(win, image= memberData[n])
                member_Image.place(x=180+(190*n),y=300)

        def updateTeamPicture():
            download_respone = requests.get("http://34.124.169.53:8000/api/getTeamImage/"+str(teamID_Create))
            picture = dict(download_respone.json())
            image_ = picture["image"].encode('utf-8')
            image_ = base64.decodebytes(image_)
            download = (thisPath + '/Image/PictureTeam/' + teamID_Create + ".png")
            output = open(download, 'wb')
            output.write(image_)
            output.close()
            global profile_Image
            pathPicture = thisPath + "/Image/PictureTeam/" + teamID_Create + ".png"

            imagepic = Image.open(pathPicture)
            profile_Image = ImageTk.PhotoImage(imagepic.resize((150, 150)))
            myProfile_Label = Label(win, image= profile_Image).place(x=170,y=90,width=150,height=150)
            
        def chooseFile():
            file_path = askopenfile(mode='rb', filetypes=[('Image Files', '*png')])
            if file_path is not None:
                pass
            data = file_path.read()
            data = base64.encodebytes(data)
            global dictPic
            dictPic = {
                "_id" : teamID_Create,
                "pictureProfile" : data
            }
            label = Label(win,text="Comeplete")
            label.place(x=920,y=190,height=20,width=80)
            
        def uploadFile():
            print("uploadFile")
            respone = requests.put("http://34.124.169.53:8000/api/setTeamImage", data=dictPic, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print(respone.text)
            teamPage()

        updateTeamPicture()
        updateMemberPicture()
        #downloadMemberPicture()

        name_team = Label(win,text='Team Name :',font=('Arial',12),bg='white')
        name_team.place(x=340,y=90)

        userTeamName = Label(win,text=teamName,font=('Arial',12),bg='white')
        userTeamName.place(x=450,y=90)

        avg_team = Label(win,text='Avg Team Rank :',font=('Arial',12),bg='white')
        avg_team.place(x=700,y=90)

        userTeamRank = Label(win,text=teamRank,font=('Arial',12),bg='white')
        userTeamRank.place(x=830,y=90)

        name_bio = Label(win,text='BIO',font=('Arial',12),bg='white')
        name_bio.place(x=340,y=120)

        userBio = Label(win,text=teamBio,font=('Arial',12),bg='lightblue',anchor='nw')
        userBio.place(x=340,y=150,width=570,height=90)

        line = Label(win,bg='black')
        line.place(x=150,y=260,width=980,height=10)

        #---------------------------------------------Edit Page--------------------------------------------------------#
        def editButton():
            # userTeamName = Entry(win,text=teamName,font=('Arial',12),bg='white')
            # userTeamName.delete(0,END)
            # userTeamName.insert(0,teamName)
            # userTeamName.place(x=450,y=90)

            userBio = Text(win,width=570,height=90,font=('Arial',12),bg='lightblue')
            userBio.insert(INSERT,teamBio)
            userBio.place(x=340,y=150,width=570,height=90)

            rdyRemoveRMember = []
            #Remove Member BTN
            for n in range(1,nMember):
                memberID = memberList[n]['userid']
                rMember = Button(win,text='-',font=('Arial',15),bg='red',command= lambda data=[memberID,n]:removeMemberConfirm(data))
                rMember.place(x=315+(190*n),y=300,width=15,height=15)
                rdyRemoveRMember.append(rMember)

            
            def comfirmEdit():
                teamNameText = teamName
                bioText = userBio.get(1.0,END)
                editData = {
                    'teamName':teamNameText,
                    'bio':bioText,
                }
                respone = requests.put('http://34.124.169.53:8000/api/editteam/'+teamID_Create, data=editData, headers={'Content-Type': 'application/x-www-form-urlencoded'})
                print(respone.text)
                teamPage()

            def cancelEdit():
                #userTeamName.destroy()
                userBio.destroy()
                Yedit_Button.destroy()
                Nedit_Button.destroy()
                choose_file_btn.destroy()
                upload_file_btn.destroy()
                for btn in rdyRemoveRMember:
                    btn.destroy()

            
            Yedit_Button = Button(win,text='Y',font=('Arial',12),bg='lightgreen',command=comfirmEdit)
            Yedit_Button.place(x=980,y=90,width=50,height=30)

            Nedit_Button = Button(win,text='N',font=('Arial',12),bg='red',command=cancelEdit)
            Nedit_Button.place(x=1050,y=90,width=50,height=30)

            choose_file_btn = Button(win,text='Choose File',font=('Arial',10),command=chooseFile)
            choose_file_btn.place(x=920,y=220,width=80,height=20)

            upload_file_btn = Button(win,text='Upload File',font=('Arial',10),command=uploadFile)
            upload_file_btn.place(x=1010,y=220,width=80,height=20)

        respone = requests.get("http://34.124.169.53:8000/api/getteam/"+str(teamID_Create))
        teamData = dict(respone.json())
        teamLeadID = teamData['reqTeam']['teamData']['teamLead']

        def leaveTeam():
        
            def cancelLeave():
                checkLeaveTeamBG.destroy()
                confirmLeaveBTN.destroy()
                cancelLeaveBTN.destroy()

            def confirmLeave():
                dictMember = {
                    "userid":UserID
                }
                respone = requests.put('http://34.124.169.53:8000/api/removemember/'+str(teamID),data=dictMember,headers={'Content-Type': 'application/x-www-form-urlencoded'})
                print(respone.text)
                CreateTeam()

            checkLeaveTeamBG = Label(win,background='white')
            checkLeaveTeamBG.place(x=920,y=220,width=200,height=20)

            confirmLeaveBTN = Button(win,text='YAH',font=('Arial',10),background='lightgreen',command=confirmLeave)
            confirmLeaveBTN.place(x=920,y=220,width=50,height=20)

            cancelLeaveBTN = Button(win,text='NAH',font=('Arial',10),background='red',command=cancelLeave)
            cancelLeaveBTN.place(x=980,y=220,width=50,height=20)

            

        if loginUserID == teamLeadID:
            edit_Button = Button(win,text='EDIT',font=('Arial',12),command=editButton)
            edit_Button.place(x=1050,y=90,width=50,height=30)
        else:
            leave_team_Button = Button(win,text='LEAVE TEAM',font=('Arial',8),background='pink',command=leaveTeam)
            leave_team_Button.place(x=920,y=220,width=80,height=20)

        #---------------------------------------------Add Member--------------------------------------------------------#
        def addMember():

            def cancelAddMember():
                BGadd.destroy()
                backBtn.destroy()
                text_enterUsername.destroy()
                input_username.destroy()
                addMemberConfirm.destroy()
            
            def confirmAddMember():
                username = input_username.get()
                respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByName/"+str(username))
                usernameCheck = dict(respone.json())
                userID = usernameCheck['userInfo']['_id']

                dictMember = {
                    'userid':userID
                }
                respone = requests.put('http://34.124.169.53:8000/api/addmember/'+str(teamID_Create),data=dictMember, headers={'Content-Type': 'application/x-www-form-urlencoded'})
                print(respone.text)
                downloadMemberPicture()
                teamPage()

            BGadd = Label(win)
            BGadd.place(x=180+(190*nMember),y=300,width=150,height=150)

            backBtn = Button(win,text='X',font=('Arial',15),command=cancelAddMember,bg='red')
            backBtn.place(x=315+(190*nMember),y=300,width=15,height=15)

            text_enterUsername = Label(win,text='Enter Username',font=('Arial',12))
            text_enterUsername.place(x=180+(190*nMember),y=320,width=150,height=20)

            input_username = Entry(win,font=('Arial',12),bg='lightgrey')
            input_username.place(x=200+(190*nMember),y=350,width=110,height=20)

            addMemberConfirm = Button(win,text='Confirm',font=('Arial',15),command=confirmAddMember)
            addMemberConfirm.place(x=210+(190*nMember),y=390,width=90,height=30)

        #---------------------------------------------Remove Member--------------------------------------------------------#

        def removeMemberConfirm(data):
            userID = data[0]
            n = data[1]

            def nRemove():
                text_enterUsername.destroy()
                BGremove.destroy()
                Y_remove.destroy()
                N_remove.destroy()

            def yRemove():
                dictMember = {
                    "userid":userID
                }
                respone = requests.put('http://34.124.169.53:8000/api/removemember/'+str(teamID_Create),data=dictMember,headers={'Content-Type': 'application/x-www-form-urlencoded'})
                print(respone.text)
                downloadMemberPicture()
                teamPage()

            BGremove = Label(win)
            BGremove.place(x=180+(190*n),y=300,width=150,height=150)

            text_enterUsername = Label(win,text='Are You Sure?',font=('Arial',12))
            text_enterUsername.place(x=180+(190*n),y=320,width=150,height=20)

            Y_remove = Button(win,text='Y',font=('Arial',12),command=yRemove)
            Y_remove.place(x=220+(190*n),y=350,width=30,height=20)

            N_remove = Button(win,text='N',font=('Arial',12),command=nRemove)
            N_remove.place(x=270+(190*n),y=350,width=30,height=20)

        #------------------------------------------Create Profile Box-----------------------------------------------------#
        
        updateMemberPicture()
        
        for n in range(0,nMember):
            #Get Each Member ID
            memberID = memberList[n]['userid']

            #Get Name From Each Member ID
            respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(memberID))
            checkMemberData = dict(respone.json())
            memberName = checkMemberData['userInfo']['username']
            rankMember = checkMemberData['userInfo']['rank']

            playerName = Label(win,text=memberName,font=('Arial',15))
            playerName.place(x=180+(190*n),y=460,width=150,height=28)

            respone = requests.get("http://34.124.169.53:8000/api/getteam/"+str(teamID_Create))
            teamData = dict(respone.json())
            teamLeadID = teamData['reqTeam']['teamData']['teamLead']

            rank_text = Label(win,text=rankMember,font=('Arial',13))
            rank_text.place(x=180+(190*n),y=490,width=150,height=28)

            if memberID == teamLeadID:
                playerPos = Label(win,text="Leader",font=('Arial',8))
                playerPos.place(x=180+(190*n),y=520,width=150,height=28)
            else:
                playerPos = Label(win,text="Member",font=('Arial',8))
                playerPos.place(x=180+(190*n),y=520,width=150,height=28)

        #Create Add Member Button
        if nMember < 5 and loginUserID == teamLeadID:
            addMember = Button(win,text='+',font=('Arial',20),command=addMember)
            addMember.place(x=180+(190*nMember),y=300,width=150,height=150)

        
    global memberData

    #Check User have team or not
    respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(UserID))
    teamCheck = dict(respone.json())
    teamID = teamCheck['userInfo']['team']
    if teamID == '':
        noTeamPage()
    else:
        respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(UserID))
        checkTeamID = dict(respone.json())
        loginUserID = checkTeamID['userInfo']['_id']
        teamID = checkTeamID['userInfo']["team"]

        respone = requests.get("http://34.124.169.53:8000/api/getteam/"+str(teamID))
        teamData = dict(respone.json())
        memberList = teamData['reqTeam']['teamMember']

        nMember = len(memberList)   #Use for FOR-LOOP and Pos of Box
        teamName = teamData['reqTeam']['teamData']['teamName']
        teamRank = teamData['reqTeam']['teamData']['teamRank']
        teamBio = teamData['reqTeam']['teamData']['bio']

        memberData = []
        for n in range(nMember):
            memberID = memberList[n]['userid']
            download_respone = requests.get("http://34.124.169.53:8000/api/getProfileImage/"+str(memberID))
            picture = dict(download_respone.json())
            image_ = picture["image"].encode('utf-8')
            image_ = base64.decodebytes(image_)
            download = (thisPath + '/Image/PictureProfile/' + memberID + ".png")
            output = open(download, 'wb')
            output.write(image_)
            output.close()
        
        teamPage()

    ########## จบตรงนี้ #############

    frame_Topbar = Frame(win, width=window_width, height=70,bg='#232323')
    frame_Topbar.place(relx=0,rely=0)
    frame_Underbar = Label(win, image=underbar_Picture,bd=0) ##1A181F
    frame_Underbar.place(relx=0,rely=0.93)
    button_Home = Button(win, text='Home Page',font=('Arial',12),command=HomePage)
    button_Home.place(x=100,y=10,height=50,width=120)
    button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',12),command=ScrimBorad)
    button_Scrim.place(x=270,y=10,height=50,width=150)
    label_stay = Label(win,bg='#b20000')
    label_stay.place(x=455,y=0,height=70,width=180)
    button_Team = Button(win, text='Create Team Page',font=('Arial',12),command=CreateTeam)
    button_Team.place(x=470,y=10,height=50,width=150)
    button_Profile = Button(win, text='Profile Page',font=('Arial',12),command=Profile)
    button_Profile.place(x=1015,y=10,height=50,width=120)
    logo_profile = Label(win,image=logo_profile_Image,bd=0)
    logo_profile.place(x=1180,y=5,width=60,height=60)
    logo_label = Label(win,image=Logo_Image)
    logo_label.place(x=30,y=10,height=50,width=50)





if checkstart:
    check = False
    Login()
    #ScrimBorad()



win.mainloop()