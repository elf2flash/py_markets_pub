#*************************************************************************#
def f_find_str_inx0_inx1( tmp_str, inx1 ):
    inx0 = inx1 + 1
    inx1 = tmp_str.find(';',inx0)
    s = tmp_str[inx0:inx1]
    return [ s , inx0 , inx1 ]

#*************************************************************************#
#############################       MAIN      #############################
#*************************************************************************#
#str_file_name = 'GAZP_200406_200406.txt'
str_file_name = 'GAZP_200406_200406_small.txt'


f = open(str_file_name)
line = f.readline()
k = 0
while line:
    if (k>0):
        
        ArrFileString = []
        
        inx0 = 0
        inx1 = line.find(';',0)
        tmp_str = line[inx0:inx1]
        ArrFileString.append(tmp_str)
        for j in range(8):
            [tmp_str, inx0, inx1] = f_find_str_inx0_inx1( line, inx1)
            ArrFileString.append(tmp_str)
        for i in ArrFileString:
            print(i)
        print('----------')

        ArrFileValue = []
        ArrFileValue.append(ArrFileString[0])
        ArrFileValue.append(ArrFileString[1])
        ArrFileValue.append(int(ArrFileString[2][0:4]))
        ArrFileValue.append(int(ArrFileString[2][4:6]))
        ArrFileValue.append(int(ArrFileString[2][5:7]))
        ArrFileValue.append(int(ArrFileString[3][0:2]))
        ArrFileValue.append(int(ArrFileString[3][2:4]))
        ArrFileValue.append(int(ArrFileString[3][4:6]))
        ArrFileValue.append(float(ArrFileString[4]))
        ArrFileValue.append(float(ArrFileString[5]))
        ArrFileValue.append(float(ArrFileString[6]))
        ArrFileValue.append(float(ArrFileString[7]))
        ArrFileValue.append(int(ArrFileString[8]))

        j = 0
        for i in ArrFileValue:
            print('j=' + str(j) + " : " + str(i) )
            j = j + 1

        print(ArrFileValue[8])
        print(float(ArrFileValue[8])+1)


        
        #print(CN_date + " " + str(inx0) + " " + str(inx1))
        #[CN_time, inx0, inx1] = f_find_str_inx0_inx1( tmp_str, inx1)
        
        break
    #print (line),
    line = f.readline()
    k = k + 1
    
f.close()


