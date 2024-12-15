class hotelfarecal:


    def _init_(self,rt='',u=0,s=0,p=0,r=0,t=0,a=1800,name='',phoneno='',address='',cindate='',coutdate='',rno=101):

        print ("\n\n**WELCOME TO GATHBANDHAN**\n")

        

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.u=u

        self.s=s
        self.a=a
        self.phoneno=phoneno
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        self.phoneno=input("\nEnter phoneno:")
        print("Your Id no.:",self.rno,"\n")
        
    def LAUDGE(self):

        print ("We have the following LAUDGE for you:-")

        print ("1. KRISHNA KUNJ rs 110000 PN\-")

        print ("2.  SARANG rs 100000 PN\-")

        print ("3.  MANDPAM rs 90000 PN\-")

        print ("4. DEVINE rs 200000 PN\-")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("how many days"))

        if(x==1):

            print ("SELECTED KRISHNA KUNJ")

            self.s=110000*n

        elif (x==2):

            print ("SELECTED SARANG")

            self.s=100000*n

        elif (x==3):

            print ("SELECTED MANDPAM")

            self.s=90000*n

        elif (x==4):
            print ("SELECTED DEVINE")

            self.s=200000*n

        else:

            print ("please choose a room")


        print ("your laudge rent is =",self.s,"\n")

    def CATERING(self):

        print("**CATERING**")

        print("TABLE SETTING")
        print("1.Table cloth----->Rs2000","2.napkin----->Rs1000","3.dinnerware--->Rs5000","4.flatware---->Rs6000","5.charger plates--->Rs7000","6.Glass ware----->Rs9000","7.Water Piters--->Rs10000")
        print("TRANSPORT SUPPLY")
        print("8.Food Pan Carier----->Rs2000","9.Glass Racks--->Rs5000","10.Outdoor Coolers---->Rs6000","11.Food Storage Boxes--->Rs7000")
        print("FURNITER AND SETTING")
        print("12.Tables--->5000","13.Chairs--->20000","14.Benches--->60000","15.cooktail Tables--->10000","16.Bars--->70000","17.Canopy/Tents--->500000","18.exit")

                                                                                                                                                                                                                                                                                    


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+2000*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+1000*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+5000*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+6000*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+7000*d
                 
            elif (c==6):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+9000*d

            elif (c==7):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+10000*d

            elif (c==8):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+2000*d
                 
            elif (c==9):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+5000*d
                 
            elif (c==10):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+6000*d

            elif (c==11):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+7000*d

            elif (c==12):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+5000*d

            elif(c==13):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+20000*d

            elif (c==14):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+60000*d

            elif (c==15):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+10000*d

            elif (c==16):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+70000*d

            elif (c==17):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+500000*d


            elif (c==18):
                break;
            else:
                print("Invalid option")

        print ("Total catering Cost=Rs",self.r,"\n")

    def	MENU(self):
        print ("***MENU**")
        print("-------------------------------------------------------------------------")
        print("                                               26 Dal Fry................ 140.00") 
        print("----------------------------------             27 Dal Makhani............ 150.00") 
        print(" 1  Regular Tea............. 20.00             28 Dal Tadka.............. 150.00") 
        print(" 2  Masala Tea.............. 25.00") 
        print(" 3  Coffee.................. 25.00             ROTI") 
        print(" 4  Cold Drink.............. 25.00             ----------------------------------") 
        print(" 5  Bread Butter............ 30.00             29 Plain Roti.............. 15.00") 
        print(" 6  Bread Jam............... 30.00             30 Butter Roti............. 15.00") 
        print(" 7  Veg. Sandwich........... 50.00             31 Tandoori Roti........... 20.00") 
        print(" 8  Veg. Toast Sandwich..... 50.00             32 Butter Naan............. 20.00") 
        print(" 9  Cheese Toast Sandwich... 70.00") 
        print(" 10 Grilled Sandwich........ 70.00             RICE")  
        print("                                               ----------------------------------") 
        print(" SOUPS                                         33 Plain Rice.............. 90.00") 
        print("----------------------------------             34 Jeera Rice.............. 90.00") 
        print(" 11 Tomato Soup............ 110.00             35 Veg Pulao.............. 110.00") 
        print(" 12 Hot & Sour............. 110.00             36 Peas Pulao............. 110.00") 
        print(" 13 Veg. Noodle Soup....... 110.00") 
        print(" 14 Sweet Corn............. 110.00             SOUTH INDIAN") 
        print(" 15 Veg. Munchow........... 110.00             ----------------------------------") 
        print("                                               37 Plain Dosa............. 100.00") 
        print(" MAIN COURSE                                   38 Onion Dosa............. 110.00") 
        print("----------------------------------             39 Masala Dosa............ 130.00") 
        print(" 16 Shahi Paneer........... 110.00             40 Paneer Dosa............ 130.00") 
        print(" 17 Kadai Paneer........... 110.00             41 Rice Idli.............. 130.00") 
        print(" 18 Handi Paneer........... 120.00             42 Sambhar Vada........... 140.00") 
        print(" 19 Palak Paneer........... 120.00") 
        print(" 20 Chilli Paneer.......... 140.00             ICE CREAM") 
        print(" 21 Matar Mushroom......... 140.00             ----------------------------------") 
        print(" 22 Mix Veg................ 140.00             43 Vanilla................. 60.00") 
        print(" 23 Jeera Aloo............. 140.00             44 Strawberry.............. 60.00") 
        print(" 24 Malai Kofta............ 140.00             45 Pineapple............... 60.00") 
        print(" 25 Aloo Matar............. 140.00             46 Butter Scotch........... 60.00")
        print("                                                47 exit")



        

        while (1):
            

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+20*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+25*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+25*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+25*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+30*f
                
            elif (e==6):
                f=int(input("Enter the quantity:"))
                self.t=self.t+30*f

            elif (e==7):
                f=int(input("Enter the quantity:"))
                self.t=self.t+50*f

            elif (e==8):
                f=int(input("Enter the quantity:"))
                self.t=self.t+50*f

            elif (e==9):
                f=int(input("Enter the quantity:"))
                self.t=self.t+70*f
                
            elif (e==10):
                f=int(input("Enter the quantity:"))
                self.t=self.t+70*f

            elif (e==11):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f

            elif (e==12):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f

            elif (e==13):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f
            elif (e==14):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f

            elif (e==15):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f

            elif (e==16):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f

            elif (e==17):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f
            elif (e==18):
                f=int(input("Enter the quantity:"))
                self.t=self.t+120*f

            elif (e==19):
                f=int(input("Enter the quantity:"))
                self.t=self.t+120*f

            elif (e==20):
                f=int(input("Enter the quantity:"))
                self.t=self.t+140*f

            elif (e==21):
                f=int(input("Enter the quantity:"))
                self.t=self.t+140*f
            elif (e==22):
                f=int(input("Enter the quantity:"))
                self.t=self.t+140*f

            elif (e==23):
                f=int(input("Enter the quantity:"))
                self.t=self.t+140*f

            elif (e==24):
                f=int(input("Enter the quantity:"))
                self.t=self.t+140*f

            elif (e==25):
                f=int(input("Enter the quantity:"))
                self.t=self.t+140*f
            elif (e==26):
                f=int(input("Enter the quantity:"))
                self.t=self.t+140*f

            elif (e==27):
                f=int(input("Enter the quantity:"))
                self.t=self.t+150*f

            elif (e==28):
                f=int(input("Enter the quantity:"))
                self.t=self.t+150*f

            elif (e==29):
                f=int(input("Enter the quantity:"))
                self.t=self.t+15*f
                
            elif (e==30):
                f=int(input("Enter the quantity:"))
                self.t=self.t+15*f

            elif (e==31):
                f=int(input("Enter the quantity:"))
                self.t=self.t+20*f

            elif (e==32):
                f=int(input("Enter the quantity:"))
                self.t=self.t+20*f

            elif (e==33):
                f=int(input("Enter the quantity:"))
                self.t=self.t+90*f
                
            elif (e==34):
                f=int(input("Enter the quantity:"))
                self.t=self.t+90*f

            elif (e==35):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f

            elif (e==36):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f

            elif (e==37):
                f=int(input("Enter the quantity:"))
                self.t=self.t+100*f
            elif (e==38):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f

            elif (e==39):
                f=int(input("Enter the quantity:"))
                self.t=self.t+130*f

            elif (e==40):
                f=int(input("Enter the quantity:"))
                self.t=self.t+130*f

            elif (e==41):
                f=int(input("Enter the quantity:"))
                self.t=self.t+130*f
                
            elif (e==42):
                f=int(input("Enter the quantity:"))
                self.t=self.t+140*f

            elif (e==43):
                f=int(input("Enter the quantity:"))
                self.t=self.t+60*f

            elif (e==44):
                f=int(input("Enter the quantity:"))
                self.t=self.t+60*f

            elif (e==45):
                f=int(input("Enter the quantity:"))
                self.t=self.t+60*f
                
            elif (e==46):
                f=int(input("Enter the quantity:"))
                self.t=self.t+60*f
            elif (e==47):
                break;
            else:

                print ("Invalid option")



        print ("Total menu Cost=Rs",self.t,"\n")

    def TRAVEL(self):
        print ("***TRAVELS**")
        print("cars")
        print ("1.car----->Rs2000/Day")
        print("Bus")
        print ("2.AC Bus----->Rs100000/Day")
        print ("3.NORMAL Bus----->Rs50000/Day")
        print("Groom & Bride")
        print ("4.Car----->Rs50000/Day")
        print ("5.exit")


        while (1):

            
            g=int(input("Enter your choice:"))


            if (g==1):
                h=int(input("No. of days:"))
                self.p=self.p+2000*h

            elif (g==2):
                h=int(input("No. of days:"))
                self.p=self.p+100000*h

            elif (g==3):
                h=int(input("No. of days:"))
                self.p=self.p+50000*h

            elif (g==4):
                h=int(input("No. of days:"))
                self.p=self.p+50000*h

            elif (g==5):
                break;

            else:

                print ("Invalid option")




        print ("Total taravel=Rs",self.p,"\n")

    def PHOTOGRAPHY(self):
        print ("***PHOTOGRAPHYGRAPH**")
        print(" 1 Traditional wedding PHOTOGRAPHYgrapy......................50000.00") 
        print(" 2 PHOTOGRAPHYjournalist Wedding PHOTOGRAPHYgraphy.............. 80000.00") 
        print(" 3 Illustrative Wedding PHOTOGRAPHYgraphy.................. 100000.00") 
        print(" 4 Potrait Wedding PHOTOGRAPHYgraphy.............. 120000.00") 
        print(" 5  Natural Wedding PHOTOGRAPHYgraphy............ 150000.00") 
        print ("6.exit")
        
        while (1):

            
            k=int(input("Enter your choice:"))


            if (k==1):
                v=int(input("No. of days:"))
                self.u=self.u+2000*v

            elif (k==2):
                v=int(input("No. of days:"))
                self.u=self.u+100000*v

            elif (k==3):
                v=int(input("No. of days:"))
                self.u=self.u+50000*v

            elif (k==4):
                v=int(input("No. of days:"))
                self.u=self.u+50000*v


            elif (k==5):
                v=int(input("No. of days:"))
                self.u=self.u+50000*v

            elif (k==6):
                break;

            else:
                print ("Invalid option")
                print ("Total Photography=Rs",self.u,"\n")

    def display(self):
        print ("***LAUDGE BILL***")
        print ("Customer details:")
        
        print ("Customer name:",self.name)
        
        print ("Customer address:",self.address)
        
        print ("Check in date:",self.cindate)
        
        print ("Check out date:",self.coutdate)
        
        print ("PhoneNo:",self.phoneno)
        
        print ("Room no:",self.rno)
        
        print ("Your Laudge is:",self.s)
        
        print ("Your Catering is:",self.r)
        
        print ("Your Menu is:",self.t)
        
        print ("Your Travel is:",self.p)

        print ("Your Photography is:",self.u)

        self.rt=self.s+self.t+self.p+self.r+self.u

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1
        print("**********THANKS FOR VISITING***********")

            

        

        

def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.LAUDGE")

        print("3.CATERING")

        print("4.MENU")

        print("5.TRAVEL")

        print("6.PHOTOGRAPHYGRAPHY")

        print("7.Show total cost")

        print("8.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.LAUDGE()

        if (b==3):

            a.CATERING()

        if (b==4):

            a.MENU()

        if (b==5):

            a.TRAVEL()

        if (b==6):

            a.PHOTOGRAPHY()

        if (b==7):

            a.display()

        if (b==8):

            quit()



main()