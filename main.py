import json

## 宣告陣列
stu_data = []
line_account = []
line_name = []
line_data = []
raw_data = []
output_data = []
output_id = [[] for i in range(2)]
list_data = []
list_id = ['stu_account.json', 'stu_name.json']
survey_name =[]
class_name = {}
survey = 0
grade = 0
classname = 0

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
    with open('survey_name.json', 'r', encoding="utf-8") as file:
        survey_name = json.load(file)
    with open('class_name.json', 'r', encoding="utf-8") as file:
        class_name = json.load(file)
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
    # for i in range (len(class_name)):
    #     print('(' + i + ')' + str(class_name[i]), end = '')
    # classname = int(input(": "))

## 輸入資料
def input_data(path):
    with open(path, 'r', encoding="utf-8") as input:
        for line in input.readlines():
            raw_data = line.split("\t")
            stu_account = raw_data[0]
            stu_name = raw_data[1]
            stu_data = raw_data[2:]
            for i in range(len(stu_data), 0, -1):
                if stu_data[i] == ' ':
                    del stu_data[i]
                stu_data.append(' ')
            string = ' '.join(stu_data)
            line_data.append(string)
            line_account.append(stu_account)
            line_name.append(stu_name)

## 將資料讀入資料庫
def w_data(n,m,l):
    blank = 0
    x = 0
    with open(list_id[0], 'r', encoding="utf-8") as file:
        output_id[0] = json.load(file)
    with open(list_id[1], 'r', encoding="utf-8") as file:
        output_id[1] = json.load(file)
        star = '* '
        for i in range(len(line_data[0])/2 - 1):
            star = star + '* '
        for i in range(len(output_id[1])):
            if output_id[1][i] not in line_name:
                line_data.insert(i, star)
        for i in range(len(line_name)):
            if line_name[i-x] in output_id[1]:
                del line_name[i-x]
                del line_account[i-x]
                x += 1
            else:
                blank += 1            #blank代表要加上的行數
    with open(list_id[0], 'w', encoding="utf-8") as file:
        output_id[0] = output_id[0] + line_account
        json.dump(output_id[0], file)
    with open(list_id[1], 'w', encoding="utf-8") as file:
        output_id[1] = output_id[1] + line_account
        json.dump(output_id[1], file)
    with open(list_data[n][m][l]+'.json', 'w', encoding="utf-8") as file:
        json.dump(line_data, file)
    for n in range(len(list_data)):
        for m in range(len(list_data[n])):
            for l in range(len(list_data[n][m])):
                with open(list_data[n][m][l]+'.json', 'r', encoding="utf-8") as file:
                    output_data = json.load(file)
                with open(list_data[n][m][l]+'.json', 'w', encoding="utf-8") as file:
                    star = '* '
                    for i in range(len(output_data)/2 - 1):
                        star = star + '* '
                    for i in range(blank):
                        output_data = output_data + star
                with open(list_data[n][m][l]+'.json', 'w', encoding="utf-8") as file:
                    json.dump(output_data, file)

##取得新資料庫編號
def list_record():
    with open('list_record.txt', 'r') as record:
        x = int(record.read())
    with open('list_record.txt', 'w') as record:
        record.write(str(x+1))
    return str(x)

##創建新資料庫
def add_new_file():
    survey = input('問卷名稱: ')
    grade = int(input('年級: '))
    classname = input('班級名稱: ')
    with open('survey_name.json', 'r', encoding="utf-8") as file:
        survey_name = json.load(file)
    with open('class_name.json', 'r', encoding='utf-8') as file:
        class_name = json.load(file)
    with open('survey_name.json', 'w', encoding="utf-8") as file:
        if survey not in survey_name: 
            list_data.append([[] for i in range(4)])
            survey_name.append(survey)
        json.dump(survey_name, file)
    with open('class_name.json', 'w', encoding='utf-8') as file:
        if classname not in class_name:
            list_data[survey][grade].append(list_record())
            class_name[survey+grade+classname] = len(list_data[survey][grade])
        json.dump(class_name, file)
    grade -= 1
    grade = str(grade)

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
def r_data(n, m, l): 
    with open(list_data[n][m][l]+'.json', 'r', encoding="utf-8") as file:
        output_data = json.load(file)

## 將資料初始化
def initialize_data():
    for i in range(2):
        with open(list_id[i], 'w', encoding='utf-8') as file:
            json.dump([], file)
    for n in range(len(list_data)):
        for m in range(len(list_data[n])):
            for l in range(len(list_data[n][m])):
                with open(list_data[n][m][l]+'.json', 'w', encoding="utf-8") as file:
                    json.dump([], file)

## 輸出一段資料
def output_data(sheet,index):
    if output_data[sheet] != []:
        print(' ', end = '')
        print(output_data[sheet][index], end = '')

##主程式
while(True):
    question = input('模式選擇(W/R): ').upper()
    if question == 'W':
        mode = int(input("請選擇輸入模式 (1)輸入新資料 (2)初始化 (3)修改已建檔之資料: "))
        ## mode 1: create new file
        if mode == 1:
            add_new_file()
            path = input("請輸入數據之檔名: ")
            input_data(path)
            w_data(survey_name.index(survey), grade, class_name[survey+grade+classname])
        ## mode 2: initialize
        elif mode == 2:
            pattern = int(input('(1)初始化全部資料(2)初始化指定資料: '))
            ## initialize all file
            if pattern == 1:
                initialize_data()
            ## initialize specific file
            elif pattern == 2:
                    locate_file()
                    with open(list_data[survey][grade][classname] + '.json', 'w', encoding='utf-8') as file:
                        json.dump([], file)
            ## users enter garbage : skip this round
            else: break
        ## mode 3: rewrite data into exist file
        elif mode == 3:
            ## choose which file user want to rewrite
            locate_file()
            path = input("請輸入數據之檔名: ")
            input_data(path)
        ## if users enter garbage: skip this round
        else: break
    elif question == 'R':
        ## 讓使用者決定欲使用之部分
        pattern = int(input("請選擇所需資料模式(1)所有資料(2)以人名提取資料(3)以年級提取資料(4)以問卷提取資料(5)選擇不同問卷的受測者名單: "))
        r_id()
        ## num stands for total sheet we have
        num = r_data()
        ## 印出所有資料
        if pattern == 1:
            print("所有資料:\n")
            ## 最外層迴圈 : 以學生人數計數
            for id in range(len(output_id[0])) :
                ## 印出學生資訊(帳號 + 姓名)
                print(output_id[0][id] + ' ' + output_id[1][id], end = '')
                ## 印出此學生擁有的一串資料
                for i in range(num) :
                    output_data(i,id)
                ## 換行
                print("\n")
        ## 以人名提取資料
        elif pattern == 2:
            ## user enter data's name they want
            name = str(input("請輸入欲搜尋之人名: "))
            ## find which index is the name    
            index = output_id[1].index(name)
            ## print out student's id (account and name)
            print(output_id[0][index] + ' ' + output_id[1][index], end = '')
            ## print out student's data
            ## 4 grades
            for i in range(num) :
                output_data(i,index)
            print('\n')
        
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
