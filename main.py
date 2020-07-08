import tkinter as tk
from tkinter import ttk
from booth import *
import bitstring

class Solver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("12.5COA")
        self.geometry("800x500")
        self.my_notebook = ttk.Notebook(self)
        self.my_notebook.grid(row=0,column=0)
        self.mainframe1 = tk.Frame(self.my_notebook)
        self.mainframe1.grid(row=0,column=0)
        self.frame_1 = tk.Frame(self.mainframe1, height  =20  , width  = 100)
        self.frame_1.grid(row=0,column=0)
        self.frame_2 = tk.Frame(self.mainframe1)
        self.frame_2.grid(row=4,column=0)
        self.my_notebook.add(self.mainframe1, text = 'Booth')
        self.l = tk.Label( self.frame_1, text ="  BOOTH ALGORITHM \n")
        self.l.grid(column = 3, row = 0)
        self.l1 = tk.Label( self.frame_1, text ="Enter bit of digits")
        self.l1.grid(column = 4, row = 4)
        self.l2 = tk.Label( self.frame_1,text = "Enter first no")
        self.l2.grid(column = 4, row = 6)
        self.l3 = tk.Label( self.frame_1,text = "Enter second no")
        self.l3.grid(column = 4, row = 8)
        self.e1 = ttk.Entry( self.frame_1,width = 15)
        self.e1.grid(column = 5, row = 4)
        self.e2 = ttk.Entry( self.frame_1,width = 15)
        self.e2.grid(column = 5, row = 6)
        self.e3 = ttk.Entry( self.frame_1,width = 15)
        self.e3.grid(column = 5, row = 8)
        self.b2 = ttk.Button(self.frame_1, text ="Calculate",command = self.mew)
        self.b2.grid(column = 8, row = 6)
#-----------------------------------------------------------------------------------------------
        self.mainframe2 = tk.Frame(self.my_notebook)
        self.mainframe2.grid(row=0,column=0)
        self.my_notebook.add(self.mainframe2,text = 'IEEE-754')
        self.frame_3 = tk.Frame(self.mainframe2)
        self.frame_3.grid(row = 0, column = 0)
        self.flabel1 = tk.Label(self.frame_3 , text = "Deciaml to IEEE 754 format")
        self.flabel1.grid(row = 0 , column = 0)
        self.flabel2 = tk.Label(self.frame_3 , text = "Enter the no (decimal format with sign) ")
        self.flabel2.grid(row = 3 , column = 0)
        self.fentry = tk.Entry(self.frame_3 , width = 15)
        self.fentry.grid(row = 3 , column = 1)
        self.fbut = ttk.Button(self.frame_3 , text = "CONVERT" , command = self.conv )
        self.fbut.grid(row = 5 , column = 0)

#---------------------------------------------------------------------------------------------------
    def conv(self):
        digit = self.fentry.get()
        txtbx1 = tk.Text(self.frame_3 , height  =20  , width  = 90)
        txtbx1.grid(row = 6 , column = 0)
        ans_32 = bitstring.BitArray(float = float(digit) , length = 32)
        ans_32h = str(ans_32.hex)
        ans_32 = str(ans_32.bin)
        txtbx1.insert(tk.END , "\n#  Single Precision :\n\n")
        txtbx1.insert(tk.END , ans_32[0] + "\t" + ans_32[1:9] + "\t\t" + ans_32[9:]+"\n")
        txtbx1.insert(tk.END , "Sign      Bias                   Mantissa\n\n")
        txtbx1.insert(tk.END , "Bias : %d\n\n"%int(ans_32[1:9],2))
        txtbx1.insert(tk.END , "Format : (-1)^" + ans_32[0] + " X 1." + ans_32[9:] + " X (10)^%d"%(int(ans_32[1:9],2)-127) + "\n\n") 
        txtbx1.insert(tk.END , "In HEXADECIMAL value : " + ans_32h + "\n\n")
        ans_64 = bitstring.BitArray(float = float(digit) , length = 64)
        ans_64h = str(ans_64.hex)
        ans_64 = str(ans_64.bin)
        sgn = "-"
        txtbx1.insert(tk.END , 50*sgn ) 
        txtbx1.insert(tk.END , "\n\n#  Double Precision :\n\n")
        txtbx1.insert(tk.END , ans_64[0] + "\t" + ans_64[1:12] + "\t\t" + ans_64[12:]+"\n")
        txtbx1.insert(tk.END , "Sign      Bias                            Mantissa\n\n")
        txtbx1.insert(tk.END , "Bias : %d\n\n"%int(ans_64[1:12],2))
        txtbx1.insert(tk.END , "Format : (-1)^" + ans_64[0] + " X 1." + ans_64[12:] + " X (10)^%d"%(int(ans_64[1:12],2)-1023) + "\n\n") 
        txtbx1.insert(tk.END , "In HEXADECIMAL value : " + ans_64h + "\n\n")


#------------------------------------------------------------------------------------------------   
    def mew(self):
        txtbx = tk.Text(self.frame_2 , height  =20  , width  = 100)
        txtbx.grid(row = 0 , column  = 0)
        rlen = int(self.e1.get().strip())
        mlen = rlen
        m = int(self.e2.get().strip())
        r = int(self.e3.get().strip())
        if m < 0:
            m = TwoComp( ("{0:0%db}" % mlen).format(m) )    #Calculate the two's complement number of m
        else:
            m = ("{0:0%db}" % mlen).format(m)   #Convert to bits and assign directly
        if r < 0:
            r = TwoComp( ("{0:0%db}" % rlen).format(r) )
        else:
            r = ("{0:0%db}" % rlen).format(r)
        a = m + GenZeroStr(rlen + 1)            #A: place M in leftmost position. Fill the left bits with 0.
        s = TwoComp(m) + GenZeroStr(rlen + 1)   #S: place negative M in leftmost position.
        p = GenZeroStr(mlen) + r + "0" 
        txtbx.insert(tk.END ,"M : " + m+ "\n")
        txtbx.insert(tk.END , "Q : "+ r+ "\n")
        txtbx.insert(tk.END ,"Mbar + 1 (2's Complement of M)= %s" % s[:mlen] + "\n")
        txtbx.insert(tk.END , "Qn+1 = 0\n")

        
        for i in range(rlen):
            sign = '-'
            space = " "
            txtbx.insert(tk.END , "\n" + 50*sign + "\n\n")
            txtbx.insert(tk.END , "Step %s : \n"%str(i+1))
            txtbx.insert(tk.END , "\t\t\t   M" + space*rlen + "Q" + space*rlen + "Qn+1\n")
            txtbx.insert(tk.END , "\t\t\t" + p[0:rlen] + "   " + p[rlen : rlen*2] + "   " + p[-1:]+"\n")
            op = p[-2:]
            txtbx.insert(tk.END , "Last 2 bits: %s\n" % "".join(op))
            if   op == "10":
                txtbx.insert(tk.END ,"A+Mbar+1 and ARshift\n")
                p = BitAdd(p, s, len(p))
            elif op == "01":
                txtbx.insert(tk.END , "A+M and ARshift\n")
                p = BitAdd(p, a, len(p))
            elif op == "00":
                txtbx.insert(tk.END , "ARshift\n")
            elif op == "11":
                txtbx.insert(tk.END , "ARshift\n")

            txtbx.insert(tk.END , "Add :\t\t\t"+p[0:rlen] + "   " + p[rlen  : rlen*2] + "   " + p[-1:] + "\n")
            p = BitShift(p, 1)
            txtbx.insert(tk.END , "Shift :    \t\t\t"+p[0:rlen] + "   " + p[rlen : rlen*2] + "   " + p[-1:]+ "\n")
        
        final = tk.Label(self.frame_2 ,bg = 'white' , text ="Final ans is : "+p[0:rlen] + " " + p[rlen : rlen*2] )
        final.grid(row = 7 , column  = 0)

#-----------------------------------------------------------------------------------------------------------------------
    





if __name__ == "__main__":
    g =  Solver()
    g.mainloop()