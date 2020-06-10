# -*- coding: utf-8 -*-
'''
This code is on the way.
It needs to be modified.
'''

from datetime import datetime 
from dateutil import relativedelta
import os,shutil as shut
#Copy files from current dir to new dir.
def duplicate_copy(path,files,npath):
    # Need to set path to duplicate files
    # cur_dir_name=input('Plz input a name of directory.')
    # path='./' + cur_dir_name
    # #Get filenames as list
    # files=os.listdir(path)
    # new_dir_name=input('Plz input a name of directory for replacement.')
    # new_path='./' + new_dir_name
    
    # new_path='./' + new_dir_name
    # try:     
    #     os.mkdir(new_path)
    # except:
    # print('The file has already existed in the directory')
    
    # Loop till the last file in new directory
    for file in files:
        #Need to set path that is to placing duplicatede files

        #Set a unique name to duplicated file(second argument)
        #If the file has already existed, print a notification
        # file=file[:-16] +duration
        # new_file=file[:-16] + duration
        if os.path.exists(npath + '/' + file) == False:
            shut.copy2(path + '/' + file,npath)
        else:
            print('The file has already existed in the directory')

# #Getting a start date from directory's name    
"""
Making new file(There are some rules to name it.
So needs to follow it.)
"""
def convert_time(file,rep_person):
    #Getting current year from sysdate.
    now=datetime.now()
    now=format(now,'%Y%m%d')
    now=int(now)
    now=datetime.now()
    now=format(now,'%Y')
    cur_time=file[-8:]
    cur_time=(cur_time.replace('-',''))
    # timetest=timetest.replace('日','')
    
    cur_time=datetime.strptime(cur_time,'%Y%m%d')
    # timedayago=cur_time+relativedelta.relativedelta(days=1)
    timetwoweekago=cur_time+relativedelta.relativedelta(days=13)
    cur_time=format(cur_time,'%Y-%m-%d')
    timetwago=format(timetwoweekago,'%m-%d')
    duration=cur_time+'～'+timetwago
    # newstr=file.replace(file[-16:-5],timedago+'～'+timetwago)
    
    #Make directory for adding duplicatied files 
    # rep_name=input('Input representative employee\'s name')
    try:
        new_dir='./'+rep_person+' 営業報告書 '+duration
        os.mkdir(new_dir)
    except FileExistsError:
        print('The same name file has already existed.')
    return new_dir

# Loop till inputting the value that is expected.
# have to use 8 chars and each of them should be num.
while True:    
    start_day=input('Plz input start date(Use format like "20200609":')
    if len(start_day)!=8 and start_day.isnumeric()==False:
        print('Invalid input was detected, plz input correct date')
        continue
    else:
        break

rep_person=input('Plz input representative person name:')
file=rep_person + '　営業報告書　' + str(start_day)
new_dir=convert_time(file,rep_person)
old_dir=input('input source directory name to duplicate:')
path='./' + old_dir
files=os.listdir(path)
#Copy cur files to new dir.
duplicate_copy(path,files,new_dir)

# Rename files and get values from analysis sheets.
# Then, insert the values to new files.
new_files=os.listdir(new_dir)
duration=new_dir[-16:]
for file in new_files:
    os.rename(new_dir + '/' + file,new_dir + '/' + file[:-21] + duration + '.xlsm')

import openpyxl as xl, csv,os,xlrd,random as rnd
at_ana=input('Input filename that you downloaded from at home' \
             '(Copy the name and paste it.):')

at_file=open(at_ana + '.csv')
at_reader=csv.reader(at_file)
at_data=list(at_reader)
at_list=[]

su_ana=input('Input filename that you downloaded from SUUMO' \
             '(Copy the name and paste it.):')
wb=xlrd.open_workbook(su_ana + '.xls')
su_name=wb.sheet_names()
sheet=wb.sheet_by_name(su_name[0])

def get_suumo(col,su_list):
    for elm in sheet.col(col):
        if elm=='\'\'':
            continue
        else:
            su_list.append(elm.value)
suumo_list=[]
su_address=[]
su_price=[]
su_count=[]
get_suumo(15,su_address)
get_suumo(33,su_price)
get_suumo(65,su_count)

for elm in range(len(su_price)):
    if len(su_address[elm])==0:
        continue
    else:
        temp_list=[]
        su_address[elm]=su_address[elm].replace('大字','')
        temp_list.append(su_address[elm][0:5])
        su_price[elm]=su_price[elm].replace('万円','')
        # if isinstance(su_price[elm],int)==True:
        try:
            temp_list.append(int(su_price[elm]))
        except:
            pass
        if isinstance(su_count[elm],float)==True:
            temp_list.append(int(su_count[elm]))
            suumo_list.append(temp_list)
    
def get_portal_data(place,price,count,datas,plist):
    for data in datas:
        temp=[]
        elm=data[place].replace('大字','')
        temp.append(elm[3:8])
        # at_temp.append(data[4])
        temp.append(data[price])
        temp.append(data[count])
        plist.append(temp)
        

#Getting data from at home's collecting csv file
get_portal_data(4,6,13,at_data,at_list)

#Getting data from SUUMO's collectiong  xls file
# path='C:/Users/kazum/hangman'
# files=os.listdir(path)
# file_list=[]
#Duplicate files and make new files in new folder
# for file in files:
#     filepath=path + file
#     customer_file=open(file)
#     reader=

files=os.listdir(new_dir)

def match_portal(plist,match):
    match_cnt=0
    for data in plist:
        # if data[0]==temp_list[0] and int(data[1])==temp_list[1]:
        try:
            if address == data[0] and str(temp_plist[match_cnt]) == str(data[1]):
                print('The same nums were found')
                print(data[1])
                print(data[2])
                match.append(data[2])
                match_cnt+=1
        except:
            break
#return -3 to 3(Zero is excepted)
def make_rndnum():
    rand = 0
    while rand == 0:
        rand=rnd.randint(-3,+3)
        return rand


for file in files:
    wb=xl.load_workbook(new_dir + '/' + file,keep_vba=True)
    # print(wb.sheetnames)
    sheet=wb['営業報告書']
    temp_plist=[]
    colval='i'
    vcell=0
    for i in range(3):
        address=sheet['i' + '23'].value.replace('大字','')
        address=address[0:5]
        price=sheet[colval + '24'].value
        price=str(price)
        price=price.replace('万円','')
        price=int(price)
        temp_plist.append(price)
        colval=ord(colval)
        if i > 0:
            vcell=5
        else:
            vcell=6
        colval=chr(colval + vcell)
        temp_col=sheet[colval + '24'].value
        if temp_col != None:
            continue
        else:
            break
    at_match=[]
    su_match=[]
    match_portal(at_list,at_match)
    suumo_list=sorted(suumo_list,key=lambda x:(x[1]))
    match_portal(suumo_list,su_match)
            #This is for sheet that has multiple values.
            # if sheet['w33'].value=='':
            #     break
            # else:
            #     continue
     
    if len(at_match)>0:
        for i in range(len(at_match)):
            rains1=make_rndnum()
            colval=ord('r')
            if i == 0:
                colval=chr(colval)
            elif i == 1:
                vcol=5
                colval=chr(colval + vcol)
            else:
                colval='ab'
            sheet[colval + '31']= sheet[colval + '31'].value + rains1
            sheet[colval + '33']=int(at_match[i])
            sheet[colval + '35']=int(su_match[i])
            se_duration=duration.replace('-','/')
            this_year=se_duration[:4]
            st_date=se_duration[5:-6]
            end_date=se_duration[-5:]
            #What happens at the end of year... Should use 'relativedelta or something later'
            sheet['ae34']=this_year + st_date
            sheet['ae37']=this_year + end_date
    wb.save(new_dir + '/' + file)

# timetest=int(timetest)
# Need to convert int to datetime for using relativedelta
