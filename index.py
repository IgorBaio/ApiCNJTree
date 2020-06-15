from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import PocArvore as poc
import ViewOfTree
# import Database


#Criar janela#
jan = Tk()
jan.title("Árvore CNJ - Control Panel")
jan.geometry("600x300")
jan.configure(background="black")
jan.resizable(width=False, height=False)
jan.attributes("-alpha",0.93)
# jan.iconbitmap(default="icons/baioSystems_8.ico")

#======================Carregando Imagens======================#
# logo = PhotoImage(file="icons/BaioSystems5.png")


#======================Widgets======================#
LeftFrame = Frame(jan, width=150, height=300, bg="#FF8C00", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=445, height=300, bg="white", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, bg="#FF8C00")
LogoLabel.place(x=30,y=100)

# UserLabel = Label(RightFrame, text="UserName:", font=("Century Gothic",20), bg="black", fg="#DAA520")
# UserLabel.place(x=30,y=85)

# UserEntry = ttk.Entry(RightFrame, width=30)
# UserEntry.place(x=180, y=97)

# PasswordLabel = Label(RightFrame, text="Password:", font=("Century Gothic",20), bg="black", fg="#DAA520")
# PasswordLabel.place(x=30,y=125)

# PassEntry = ttk.Entry(RightFrame, width=30, show="¿")
# PassEntry.place(x=180, y=137)

# def InsertTree():
#     DirectoryLabel = Label(RightFrame, text="Diretorio:", font=("Century Gothic",20), bg="black", fg="#DAA520")
#     DirectoryLabel.place(x=30,y=85)
#     user = str(UserEntry.get())
#     password = PassEntry.get()
   
#     VerifyLogin = Database.VerifyLogin(user,password)
#     try:
#         if user in VerifyLogin and password in str(VerifyLogin):
#             messagebox.showinfo(title="Login Info", message="Confirmed Access, Wellcome")
#     except:
#         messagebox.showwarning(title="Login Info", message="Verify if you are registered in the system")


# #======================Botoes======================#
def InsertData():
    #======================Removendo Botoes iniciais======================#
    InsertTreeButton.place(x=5000)
    ViewTreeButton.place(x=5000)

    DiretorioLabel = Label(RightFrame, text="Diretorio:", font=("Centuric Gothic",16), bg="white", fg="black")
    DiretorioLabel.place(x=30, y=25)
    
    DiretorioEntry = ttk.Entry(RightFrame, width=30)
    DiretorioEntry.place(x=181, y=30)

    EstruturaLabel = Label(RightFrame, text="DumpEstrutura:", font=("Centuric Gothic",16), bg="white", fg="black")
    EstruturaLabel.place(x=30, y=65)
    
    EstruturaEntry = ttk.Entry(RightFrame, width=30)
    EstruturaEntry.place(x=181, y=70)

    DadosLabel = Label(RightFrame, text="DumpDados:", font=("Centuric Gothic",16), bg="white", fg="black")
    DadosLabel.place(x=30, y=105)
    
    DiretorioEntry = ttk.Entry(RightFrame, width=30)
    DiretorioEntry.place(x=181, y=110)

    def CriarArvore():
        diretorio = DiretorioEntry.get()
        ViewOfTree.SaveFile(diretorio)

    CreateTreeViewLabel = ttk.Button(RightFrame, text="Criar Visualização", width="22", command=CriarArvore)
    CreateTreeViewLabel.place(x=223 , y=199)


    def BackToMain():
        #======================Removendo Widgets de Registro======================#
        DiretorioLabel.place(x=5000)
        DiretorioEntry.place(x=5000)

        CreateTreeViewLabel.place(x=5000)

        Back.place(x=5000)

        #======================Trazendo de volta os Widgets de Login======================#
        InsertTreeButton.place(x=34.2 , y=200)

        ViewTreeButton.place(x=223,y=199)

    Back = ttk.Button(RightFrame, text="Back", width="22", command=BackToMain)
    Back.place(x=34.2 , y=200)

InsertTreeButton = ttk.Button(RightFrame, text="Inserir Arvore", width="22", command=InsertData)
InsertTreeButton.place(x=34.2 , y=200)

# def Register():
#     #======================Removendo Widgets de Login======================#
#     InsertTreeButton.place(x=5000)
#     RegisterButton.place(x=5000)

#     #======================Inserindo Widgets de Registro======================#
#     NomeLabel = Label(RightFrame, text="Name:", font=("Centuric Gothic",20), bg="black", fg="#DAA520")
#     NomeLabel.place(x=30, y=5)
    
#     NomeEntry = ttk.Entry(RightFrame, width=30)
#     NomeEntry.place(x=180, y=17)

#     EmailLabel = Label(RightFrame, text="E-mail:",font=("Centuric Gothic",20), bg="black", fg="#DAA520")
#     EmailLabel.place(x=30,y=45)

#     EmailEntry = ttk.Entry(RightFrame,width=30)
#     EmailEntry.place(x=180,y=57)

#     def RegisterToDataBase():
#         Database.CreateTable()

#         name = NomeEntry.get()
#         email = EmailEntry.get()
#         user = UserEntry.get()
#         password = PassEntry.get()

#         if name == '' or email == '' or user == '' or password == '':
#              messagebox.showerror(title="Register Info", message="Some field is empty. Please fill it")
#         else:
#             Database.ExecuteQuery("""insert into Users (Name, Email, User, Password)
#              values('"""+name+"','"+email+"','"+user+"','"+password+"')")
            
#             messagebox.showinfo(title="Register Info", message="Register Sucessful")
        
        

#     Register = ttk.Button(RightFrame, text="Register", width="22", command=RegisterToDataBase)
#     Register.place(x=223,y=199)

#     def BackToLogin():
#         #======================Removendo Widgets de Registro======================#
#         NomeLabel.place(x=5000)
#         NomeEntry.place(x=5000)

#         EmailLabel.place(x=5000)
#         EmailEntry.place(x=5000)

#         Register.place(x=5000)

#         Back.place(x=5000)

#         #======================Trazendo de volta os Widgets de Login======================#
#         InsertTreeButton.place(x=34.2 , y=200)

#         ViewTreeButton.place(x=223,y=199)

#     Back = ttk.Button(RightFrame, text="Back", width="22", command=BackToLogin)
#     Back.place(x=34.2 , y=200)
    
def View():
    #======================Removendo Botoes iniciais======================#
    InsertTreeButton.place(x=5000)
    ViewTreeButton.place(x=5000)

     #======================Inserindo Widgets de Registro======================#
    DiretorioLabel = Label(RightFrame, text="Diretorio:", font=("Centuric Gothic",20), bg="white", fg="black")
    DiretorioLabel.place(x=30, y=50)
    
    DiretorioEntry = ttk.Entry(RightFrame, width=30)
    DiretorioEntry.place(x=181, y=62)

    

    def CriarViewArvore():
        diretorio = DiretorioEntry.get()
        ViewOfTree.SaveFile(diretorio)

    CreateTreeViewLabel = ttk.Button(RightFrame, text="Criar Visualização", width="22", command=CriarViewArvore)
    CreateTreeViewLabel.place(x=223 , y=199)


    def BackToMain():
        #======================Removendo Widgets de Registro======================#
        DiretorioLabel.place(x=5000)
        DiretorioEntry.place(x=5000)

        CreateTreeViewLabel.place(x=5000)

        Back.place(x=5000)

        #======================Trazendo de volta os Widgets de Login======================#
        InsertTreeButton.place(x=34.2 , y=200)

        ViewTreeButton.place(x=223,y=199)

    Back = ttk.Button(RightFrame, text="Back", width="22", command=BackToMain)
    Back.place(x=34.2 , y=200)
     
#     VerifyLogin = Database.VerifyLogin(user,password)
#     try:
#         if user in VerifyLogin and password in str(VerifyLogin):
#             messagebox.showinfo(title="Login Info", message="Confirmed Access, Wellcome")
#     except:
#         messagebox.showwarning(title="Login Info", message="Verify if you are registered in the system")

ViewTreeButton = ttk.Button(RightFrame, text="Visualizar Arvore", width="22", command=View)
ViewTreeButton.place(x=223,y=199)

jan.mainloop()