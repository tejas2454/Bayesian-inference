import pandas as pd
import numpy as np
import sys

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                          ''' FUNCTIONS start'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

def dependent_variables(dependent_mat,n): #for returning dependent variables from the given matrix of nxn size
    lst=[]
    lst1=[]
    for i in range(n):
        for j in range(n):
            if dependent_mat[i,j]==1:
                lst.append((j))# here i represents the independent variable and j represents the dependent variable
                lst1.append((j,i))
    return(lst,lst1)

def check_dependency(lst,a): # here lst is list of dependent variables and a will be the element which will be compaired if that exits in the 'lst' or not
    if a in lst:
        val='yes'
    else:
        val='no'
    return(val)

def var3(l):
    count000=0
    count001=0
    count010=0
    count011=0
    count100=0
    count101=0
    count110=0
    count111=0
    for x in range(l.shape[0]):
        if (l[x,0]==0 and l[x,1]==0  and l[x,2]==0):
            count000+=1
        elif (l[x,0]==0 and l[x,1]==0  and l[x,2]==1):
            count001+=1
        elif (l[x,0]==0 and l[x,1]==1  and l[x,2]==0):
            count010+=1
        elif (l[x,0]==0 and l[x,1]==1  and l[x,2]==1):
            count011+=1
        elif (l[x,0]==1 and l[x,1]==0  and l[x,2]==0):
            count100+=1
        elif (l[x,0]==1 and l[x,1]==0  and l[x,2]==1):
            count101+=1
        elif (l[x,0]==1 and l[x,1]==1  and l[x,2]==0):
            count110+=1
        else:
            count111+=1
    prob_N3=[]
    
    p111=count111/l.shape[0]
    p110=count110/l.shape[0]
    p101=count101/l.shape[0]
    p100=count100/l.shape[0]
    p011=count011/l.shape[0]
    p010=count010/l.shape[0]
    p001=count001/l.shape[0]
    p000=count000/l.shape[0]
    try:
        prob_N3.append(round(p111/(p100+p101+p110+p111),4))
    except:
        prob_N3.append(p111)
    try:
        prob_N3.append(round(p110/(p100+p101+p110+p111),4))
    except:
        prob_N3.append(p110)
    try:
        prob_N3.append(round(p101/(p100+p101+p110+p111),4))
    except:
        prob_N3.append(p101)
    try:
        prob_N3.append(round(p100/(p100+p101+p110+p111),4))
    except:
        prob_N3.append(p100)
    try:
        prob_N3.append(round(p010/(p011+p010+p001+p000),4))
    except:
        prob_N3.append(p010)
    try:
        prob_N3.append(round(p001/(p011+p010+p001+p000),4))
    except:
        prob_N3.append(p010)
    try:
        prob_N3.append(round(p001/(p011+p010+p001+p000),4))
    except:
        prob_N3.append(p001)
    try:
        prob_N3.append(round(p000/(p011+p010+p001+p000),4))   
    except:
        prob_N3.append(p000)

    return(prob_N3)


def var4(l):
    count0000=0
    count0001=0
    count0010=0
    count0011=0
    count0100=0
    count0101=0
    count0110=0
    count0111=0
    count1000=0
    count1001=0
    count1010=0
    count1011=0
    count1100=0
    count1101=0
    count1110=0
    count1111=0
    for x in range(l.shape[0]):
        if  (l[x,0]==0 and l[x,1]==0  and l[x,2]==0 and l[x,3]==0):
            count0000+=1
        elif (l[x,0]==0 and l[x,1]==0  and l[x,2]==0 and l[x,3]==1):
            count0001+=1
        elif (l[x,0]==0 and l[x,1]==0  and l[x,2]==1 and l[x,3]==0):
            count0010+=1
        elif (l[x,0]==0 and l[x,1]==0  and l[x,2]==1 and l[x,3]==1):
            count0011+=1
        elif (l[x,0]==0 and l[x,1]==1  and l[x,2]==0 and l[x,3]==0):
            count0100+=1
        elif (l[x,0]==0 and l[x,1]==1  and l[x,2]==0 and l[x,3]==1):
            count0101+=1
        elif (l[x,0]==0 and l[x,1]==1  and l[x,2]==1 and l[x,3]==0):
            count0110+=1
        elif (l[x,0]==1 and l[x,1]==1  and l[x,2]==1 and l[x,3]==1):
            count1111+=1
        elif (l[x,0]==1 and l[x,1]==0  and l[x,2]==0 and l[x,3]==0):
            count1000+=1
        elif (l[x,0]==1 and l[x,1]==0  and l[x,2]==1 and l[x,3]==1):
            count1001+=1
        elif (l[x,0]==1 and l[x,1]==0  and l[x,2]==1 and l[x,3]==0):
            count1010+=1
        elif (l[x,0]==1 and l[x,1]==0  and l[x,2]==1 and l[x,3]==1):
            count1011+=1
        elif (l[x,0]==1 and l[x,1]==1  and l[x,2]==0 and l[x,3]==0):
            count1100+=1
        elif (l[x,0]==1 and l[x,1]==1  and l[x,2]==0 and l[x,3]==1):
            count1101+=1
        elif (l[x,0]==1 and l[x,1]==1  and l[x,2]==1 and l[x,3]==0):
            count1110+=1
        else:
            count1111+=1
    prob_N4=[]
    try:
        prob_N4.append(count1111/l.shape[0])
        prob_N4.append(count1110/l.shape[0])
        prob_N4.append(count1101/l.shape[0])
        prob_N4.append(count1100/l.shape[0])
        prob_N4.append(count1011/l.shape[0])
        prob_N4.append(count1010/l.shape[0])
        prob_N4.append(count1001/l.shape[0])
        prob_N4.append(count1000/l.shape[0])
        prob_N4.append(count0111/l.shape[0])
        prob_N4.append(count0110/l.shape[0])
        prob_N4.append(count0101/l.shape[0])
        prob_N4.append(count0100/l.shape[0])
        prob_N4.append(count0011/l.shape[0])
        prob_N4.append(count0010/l.shape[0])
        prob_N4.append(count0001/l.shape[0])
        prob_N4.append(count0000/l.shape[0])
    except:
        g=0
    
    return(prob_N4)

def var2(l):
    count00=0
    count10=0
    count01=0
    count11=0
    for x in range(l.shape[0]):
        if (l[x,0]==0 and l[x,1]==0 ):
            count00+=1
        elif (l[x,0]==1 and l[x,1]==0):
            count10+=1
        elif (l[x,0]==0 and l[x,1]==1):
            count01+=1
        else:
            count11+=1
    prob_N2=[]
    
        #prob_N2.append(count11/l.shape[0])
    p11=count11/l.shape[0]
    p01=count01/l.shape[0]
    p10=count10/l.shape[0]
    p00=count00/l.shape[0]
    try:
        t1=round((p11/(p11+p10)),4)
    except:
        t1=p11
    try:
        t2=round((p01/(p01+p00)),4)
    except:
        t2=p01
    try:
        t3=round((p10/(p10+p11)),4)
    except:
        t3=p10
    try:
        t4=round((p00/(p00+p01)),4)
    except:
        t4=p00
     
    
    prob_N2.append(t1)
    prob_N2.append(t2)    
    prob_N2.append(t3)
    prob_N2.append(t4)
    
       
    
    #prob_N2.append(count10/l.shape[0])
    #prob_N2.append(count01/l.shape[0])
    #prob_N2.append(count00/l.shape[0])
    
    return(prob_N2)

def var1(l):
    count0=0
    count1=0
    
    for x in range(l.shape[0]):
        if (l[x]==0):
            count0+=1
       
        else:
            count1+=1
    prob_N1=[]
    try:
        prob_N1.append(count1/l.shape[0])
    except:
        prob_N1.append(count1/l.shape[0])
    try:
        prob_N1.append(count0/l.shape[0]) 
    except:
        prob_N1.append(count0/l.shape[0])

    return(prob_N1)


def out_dependent(dependent_relations): 
    output=[]
    for x in dependent_relations:
        for y in dependent_relations:
            lst=[]
            if x[0]==y[0] and x[1]!=y[1]:
                if x[0]==y[0]:
                    lst.append(x)
                    lst.append(y)
                    g=np.unique(lst)
                    output.append(g)
            elif x[0]!=y[0]:
                output.append(x)


    output=list(output)
    dependent=[]
    for x in output:
        if list(x) not in dependent:
            dependent.append(list(x))
    return(dependent)  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #                                                                           ''' FUNCTIONS end'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #----------------------------------------------------------------------------------Input 1--------------------------------------------------------------------------
input1_file=open(sys.argv[1])
f=input1_file.readlines()
n=int(f[0])
input_1=[]
for x in f:
    input_1.append(x)
input_1.pop(0)

 #----------------------------------------------------------------------------------Input 2--------------------------------------------------------------------------
input_2_csv=pd.read_csv(sys.argv[2],header=-1)
input_2_csv=input_2_csv.drop(0,axis=0)
N=len(input_2_csv)
prob_lst=[]
count_1=0
rows=len(input_2_csv)
for j in range(0,input_2_csv.shape[1]):
    count_1=0
    for i in range(1,input_2_csv.shape[0]+1):          
        if input_2_csv.loc[i,j]=='yes' or '1':            
            count_1+=1
            input_2_csv.loc[i,j]=1
        elif input_2_csv.loc[i,j]=='no' or '2':
            input_2_csv.loc[i,j]=0
        else:
            g=0
    prob_lst.append(count_1/rows)
input_2_array=np.array(input_2_csv)
    
#-------------------------------------------------------------------- Dependent Variable Calculation--------------------------------------------------------------------
dependent_mat=[]
for each in input_1[n:]:
    for i in each.split():
        i=int(i)
        dependent_mat.append(i)
dependent_mat=(np.array(dependent_mat)).reshape((n,n))

dependent_var,dependent_relations=dependent_variables(dependent_mat,n)


j=0
possible_values=[]
for i in input_1:    #print(i)
    
    while (j<n): 
        possible_values.append((i.split(',')))
        j+=1


count=0
final_output=[]
for i in range(n):
    for j in range(len(input_2_array)):
        if i not in dependent_var:
            bob=input_2_array[:,i]
            if var1(bob) not in final_output:
                final_output.append(var1(bob))
                #final_output.append('/n')
        else:
            ggg=0

l=[]
vb=out_dependent(dependent_relations)

for i in vb:
    if len(i)==2:
        bob=input_2_array[:,i]
        final_output.append(var2(bob))
        #final_output.append('/n')
    elif len(i)==3:
        bob=input_2_array[:,i]
        final_output.append(var3(bob))
        #final_output.append('/n')
    elif len(i)==4:
        bob=input_2_array[:,i]
        final_output.append(var4(bob))
        #final_output.append('/n')
output1=np.array(final_output)

fo=open(sys.argv[3],'w')
for l in output1:        
        fo.write(" ".join(str(elem) for elem in l) + "\n")
fo.close()

            
for x in final_output:
    print(x)
