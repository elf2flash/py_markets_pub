import bot0
#import matplotlib.pyplot as plt

#*************************************************************************#
def f_find_str_inx0_inx1( TmpStr, inx1 ):
    inx0 = inx1 + 1
    inx1 = TmpStr.find(';',inx0)
    S = TmpStr[inx0:inx1]
    return [ S , inx0 , inx1 ]




#*************************************************************************#
#############################       MAIN      #############################
#*************************************************************************#
StrFileName = 'GAZP_200406_200406_small.txt'
StrFileName = 'GAZP_200406_200406.txt'
StrFileName = 'GAZP_200101_200408.txt'
StrFileName = 'test.txt'
print(StrFileName)

pFile = open(StrFileName)
FileLine = pFile.readline()

ArrKData = []
k = 0
while FileLine:
    if (k>0):
        
        ArrFileString = []
        
        inx0 = 0
        inx1 = FileLine.find(';',0)
        # if end file, then exit
        if (inx1 < 0):
            break
        TmpStr = FileLine[inx0:inx1]
        ArrFileString.append(TmpStr)
        for j in range(8):
            [TmpStr, inx0, inx1] = f_find_str_inx0_inx1( FileLine, inx1)
            ArrFileString.append(TmpStr)
        # collect and trasnform data
        ArrFileValue = []
        ArrFileValue.append(ArrFileString[0])               # 0
        ArrFileValue.append(ArrFileString[1])               # 1
        ArrFileValue.append(int(ArrFileString[2][0:4]))     # 2 year
        ArrFileValue.append(int(ArrFileString[2][4:6]))     # 3 month
        ArrFileValue.append(int(ArrFileString[2][5:7]))     # 4 day
        ArrFileValue.append(ArrFileString[3][0:2])          # 5 hour
        ArrFileValue.append(ArrFileString[3][2:4])          # 6 minute
        ArrFileValue.append(ArrFileString[3][4:6])          # 7 secund
        ArrFileValue.append(float(ArrFileString[4]))        # 8  OPEN
        ArrFileValue.append(float(ArrFileString[5]))        # 9  HIGH
        ArrFileValue.append(float(ArrFileString[6]))        # 10 LOW
        ArrFileValue.append(float(ArrFileString[7]))        # 11 CLOSE
        ArrFileValue.append(int(ArrFileString[8]))          # 12 VOL
        #collect data to 2D array
        ArrKData.append(ArrFileValue)
        
        if (1==0):
            j = 0
            for i in ArrFileValue:
                print('j=' + str(j) + " : " + str(i) )
                j = j + 1
    FileLine = pFile.readline()
    k = k + 1
pFile.close()


#-----------------------------------------------------------------------------------------------
# Work with ArrKData
LData = len(ArrKData)
print("LData = " + str(LData))

bot0.f_bot0( ArrKData, LData )



#fig, ax = plt.subplots()                        # будет 1 график, на нем:
#x = range(0,LData)
#H = []
#L = []
#for i in range(0,LData):
#    CurrData = ArrKData[i]
#    H.append(CurrData[9])
#    L.append(CurrData[10])
#ax.plot(x, H, color="blue", label="y(x)",linestyle="-")      # функция y1(x), синий, надпись y(x)
#ax.plot(x, L, color="red", label="y'(x)",linestyle="-")      # функция y2(x), красный, надпись y'(x)
#ax.set_xlabel("x")                              # подпись у горизонтальной оси х
#ax.set_ylabel("y")                              # подпись у вертикальной оси y
#ax.legend()                                     # показывать условные обозначения
#plt.show()                                      # показать рисунок

print("end")



