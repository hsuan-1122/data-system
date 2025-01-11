## 宣告陣列
stu_data = []
line_account = []
line_name = []
line_data = []
raw_data = []
output_data = [[] for i in range(2)]
output_id = [[] for i in range(2)]
# list_data = [[[] for i in range(m)] for i in range(n)]
# list_data[n][m][l]  
# n=問卷 m=年級 l=班級


list_data = ['stu_data1.txt', 'stu_data2.txt']
list_id = ['stu_account.txt', 'stu_name.txt']

survey_name =[]
class_name = []

survey = 0
grade = 0
classname = 0

# list_record.txt, survey_name.txt,  class_name.txt, stu_name.txt, stu_account.txt


for i in range(list_record()):
    with open(str(i)+'.txt', 'w') as file:





##取得新資料庫編號
def list_record():
    with open('list_record.txt', 'r') as record:
        x = int(record.read())
    with open('list_record.txt', 'w') as record:
        record.write(str(x+1))
    return x

##創建新資料庫
def add_new_file():
    survey = input('問卷名稱: ')
    grade = input('年級: ')
    classname = input('班級名稱: ')
    survey_name.append(survey)
    class_name.append(classname)
    with open(list_record+'.txt', 'w') as file:
        w_data(survey, grade, classname)

## 定位使用者資料位置(survey_name, grade, classname)
## function: 1. find survey name
##                  open "survey_name.txt" to check how many surveys we have
##           2. input grade
##           3. find class name 
##                  method same as 1.
## element: (global variable) survey, grade, classname
##          (list) survey_name, class_name
def locate_file():
## section 1: ask survey name
## create list survey_name by open survey_name.txt
## same as class name
    with open('survey_name.txt', 'w', encoding="utf-8") as file:
        survey_name.clear()
        for line in file.readlines():
            survey_name.append(line[:-1]) ## delete '\n'
    with open('class_name.txt', 'w', encoding="utf-8") as file:
        class_name.clear()
        for line in file.readlines():
            class_name.append(line[:-1]) ## delete '\n'
    ## user
    ## ask for survey name
    print("請選擇問卷", end = '')
    for i in range (len(survey_name)) :
        print('(' + str(i + 1) + ')' + str(survey_name[i]), end = '')
    survey = int(input(": "))
    ## ask for grade
    grade = int(input("請選擇年級: "))
    ## ask for classname
    print("請選擇班級", end = '')
    for i in range (len(class_name)) :
        print('(' + i + ')' + str(class_name[i]), end = '')
    classname = int(input(": "))








## 輸入資料
def input_data(path):
    with open(path, 'r', encoding="utf-8") as input:
        for line in input.readlines():
            raw_data = line.split("\t")
            stu_account = raw_data[0]
            stu_name = raw_data[1]
            stu_data = raw_data[2:]
            string = ' '.join(stu_data)
            line_data.append(string)
            line_account.append(stu_account+'\n')
            line_name.append(stu_name+'\n')

## 將資料讀入資料庫
def w_data(n,m,l):
    blank = []
    output_id[1].clear()
    x = 0
    with open(list_id[1], 'r', encoding="utf-8") as file:
        for line in file.readlines():
            output_id[1].append(line)
        for i in range(len(output_id[1])):
            if output_id[1][i] not in line_name:
                line_data.insert(i, '* * * * * * * * * * * *    \n')    #星號數量操作由菌菇處理
        for i in range(len(line_name)):
            if line_name[i-x] in output_id[1]:
                del line_name[i-x]
                del line_account[i-x]
                x += 1
            else:
                blank.append('* * * * * * * * * * * *   \n')            #星號數量操作由菌菇處理
    with open(list_id[0], 'a', encoding="utf-8") as file:
        file.writelines(line_account)
    line_account.clear()
    with open(list_id[1], 'a', encoding="utf-8") as file:
        file.writelines(line_name)
    line_name.clear()
    with open(list_data[n][m][l], 'w', encoding="utf-8") as file:
        file.writelines(line_data)
        file.write('\n')
    line_data.clear()
    for i in range(2):
        if i != k:
            output_data[i].clear()
            with open(list_data[i], 'r', encoding="utf-8") as file:
                for line in file.readlines():
                    s = line.split(' ')
                    for k in range(len(s)):
                        if s[k] == '':
                            del s[k:]
                            break
                    s = ' '.join(s)
                    output_data[i].append(s[:-1])
                if output_data[i] != []:
                    with open(list_data[i], 'a', encoding="utf-8") as file:
                        # file.write('\n')
                        file.writelines(blank)
                        blank.clear()

## 將學生資訊從資料庫中讀出
def r_id():
    output_id[0].clear()
    output_id[1].clear()
    with open(list_id[0], 'r', encoding="utf-8") as file:
        for line in file.readlines():
            s = line.split(' ')
            s = ' '.join(s)
            output_id[0].append(s[:-1])
    with open(list_id[1], 'r', encoding="utf-8") as file:
        for line in file.readlines():
            s = line.split(' ')
            s = ' '.join(s)
            output_id[1].append(s[:-1])

## 將學生數據從資料庫中讀出
def r_data(i): 
    output_data[i].clear()
    with open(list_data[i], 'r', encoding="utf-8") as file:
        for line in file.readlines():
            s = line.split(' ')
            for k in range(len(s)):
                if s[k] == '':
                    del s[k:]
                    break
            s = ' '.join(s)
            output_data[i].append(s)

## 將資料初始化
def initialize_data():
    for i in range(2):
        with open(list_id[i], 'w') as file:
            file.write("")
        with open(list_data[i], 'w') as file:
            file.write("")

## 將資料整合並輸出
def output_all_data():
    for i in range(len(output_id[1])):
        print(output_id[0][i] + ' ' + output_id[1][i], end = '')
        if output_data[0] != []:
            print(' ', end = '')
            print(output_data[0][i], end = '')
        if output_data[1] != []:
            print(' ', end = '')
            print(output_data[1][i], end = '')
        print('\n')

##主程式
while(True):
    question = input('模式選擇(W/R): ').upper()
    if question == 'W':
        mode = int(input("請選擇輸入模式 (1)輸入新資料 (2)初始化 (3)修改已建檔之資料: "))
        ## mode 1: create new file
        if mode == 1:
            add_new_file()
        ## mode 2: initialize
        elif mode == 2:
            pattern = int(input('(1)初始化全部資料(2)初始化指定資料: '))
            ## initialize all file
            if pattern == 1:
                initialize_data()
            ## initialize specific file
            elif pattern == 2:
                    locate_file()
                    with open(list_data[survey][grade][classname] + '.txt', 'w') as file:
                        file.write("")
            ## users enter garbage : skip this round
            else: break
        ## mode 3: rewrite data into exist file
        elif mode == 3:
            ## choose which file user want to rewrite
            locate_file()
            ## 剩下的酷酷酷不知道還沒寫
            raw_data = input("請選擇欲修改的數據: ")
        ## if users enter garbage: skip this round
        else: break
    elif question == 'R':
        ## 讓使用者決定欲使用之部分
        pattern = int(input("請選擇所需資料模式(1)所有資料(2)以人名提取資料(3)以年級提取資料(4)以問卷提取資料(5)選擇不同問卷的受測者名單: "))
        ##r_id()
        ##for i in range(len(output_data)):
            ##r_data(i)
        ##決定模式選擇
        if pattern == 1:
            print("所有資料:\n")
            output_all_data()
        elif pattern == 2:
            ## user enter data's name they want
            name = str(input("請輸入欲搜尋之人名: "))
            ## find which index is the name
            ## open stu_name.txt, put them into output[1](name list)
            with open('stu_name.txt', 'r', encoding="utf-8") as file:
                output_id[1].clear()
                for line in file.readlines():
                    output_id[1].append(line[:-1]) 
            ## find its index      
            index = output_id[1].index(name)
            ## print out student account / id / and statistic (combined all survey)
            print(output_id[0][index] + ' ' + output_id[1][index], end = '')
            for i in range(2):
                if output_data[i] != []:
                    print(' ', end = '')
                    print(output_data[i][index], end = '')
            print('\n')
            ## clear output list, prepared for further survey
            output_id.clear()
            output_data.clear()
        elif pattern == 3 :
            while(True):
                pattern = int(input("請選擇年級(1)大一(2)大二: "))
                pattern -= 1 ## 0 for freshmen, 1 for sophomore
                if pattern == 0 or pattern == 1:
                    for i in range(len(output_id[1])):
                        if output_data[pattern] != []:
                            if output_data[pattern][i][0] != '*':
                                print(output_id[0][i] + ' ' + output_id[1][i], end = '')
                                print(' ', end = '')
                                print(output_data[pattern][i])
                    break
                else: break
    else:
        continue

