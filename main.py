import json
import os

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
class_name = []
class_name_dict = {}
global survey
global grade
global classname
global final_output

## 定位使用者資料位置(survey_name, grade, classname)
## function: 1. find survey name
##                  open "survey_name.txt" to check how many surveys we have
##           2. input grade
##           3. find class name 
##                  method same as 1.
## element: (global variable) survey, grade, classname
##          (list) survey_name, class_name
def locate_file():
    global survey
    global grade
    global classname
## section 1: ask survey name
## create list survey_name by open survey_name.txt
## same as class name
    with open('survey_name.json', 'r', encoding="utf-8") as file:
        survey_name = json.load(file)
    with open('class_name.json', 'r', encoding='utf-8') as file:
        class_name = json.load(file)
    with open('class_name_dict.json', 'r', encoding='utf-8') as file:
        class_name_dict = json.load(file)
    with open('list_data.json', 'r', encoding='utf-8') as file:
        list_data = json.load(file)
    ## user
    ## ask for survey name
    print("請選擇問卷", end = '')
    for i in range (len(survey_name)) :
        print(' (' + str(i + 1) + ')' + str(survey_name[i]), end = '')
    survey = survey_name[int(input(": "))-1]
    ## ask for grade
    print("請選擇年級，目前有", end = '')
    for i in range(len(list_data[survey_name.index(survey)])):
        if list_data[survey_name.index(survey)][i] != []:
            print(' ' + str(i + 1) + "年級", end = '')
    grade = int(input(": ")) - 1
    ## ask for classname
    x = 0
    choice = []
    print("請選擇班級", end = '')
    for i in range (len(class_name)):
        if survey+str(grade)+class_name[i] in class_name_dict:
            print(' (' + str(i + 1 - x) + ')' + str(class_name[i]), end = '')
            choice.append(i)
        else:
            x += 1
    classname = class_name[choice[int(input(": "))-1]]

## 輸入資料
def input_data(path):
    with open(path, 'r', encoding="utf-8") as input:
        for line in input.readlines():
            raw_data = line.split("\t")
            stu_account = raw_data[0]
            stu_name = raw_data[1]
            stu_data = raw_data[2:]
            # print(stu_data)
            for i in range(len(stu_data)):
                if stu_data[i] == '' or stu_data[i] == ' ':
                    del stu_data[i:]
                    break
            string = ' '.join(stu_data)
            string = string + ' '
            line_data.append(string)
            line_account.append(stu_account)
            line_name.append(stu_name)

## 將資料讀入資料庫
def w_data(n,m,l):
    blank = 0
    x = 0
    new_name = []
    new_account = []
    with open('list_data.json', 'r', encoding='utf-8') as file:
        list_data = json.load(file)
    with open(list_id[0], 'r', encoding="utf-8") as file:
        output_id[0] = json.load(file)
    with open(list_id[1], 'r', encoding="utf-8") as file:
        output_id[1] = json.load(file)
    if output_id[1] != []:
        for i in range(len(line_name)):
            if line_name[i] not in output_id[1]:
                new_name.append(line_name[i])
                new_account.append(line_account[i])
                blank += 1            #blank代表要加上的行數
                store = line_data[i-x]
                del line_data[i-x]
                line_data.append(store)
                x += 1
    else:
        new_name = line_name
        new_account = line_account
    star = ''
    for i in range(len(line_data[1])):
        if line_data[1][i] == ' ':
            star = star + '* '
    for i in range(len(output_id[1])):
        if output_id[1][i] not in line_name:
            line_data.insert(i, star)
    with open(list_id[0], 'w', encoding="utf-8") as file:
        output_id[0] = output_id[0] + new_account
        json.dump(output_id[0], file)
        line_account.clear()
    with open(list_id[1], 'w', encoding="utf-8") as file:
        output_id[1] = output_id[1] + new_name
        json.dump(output_id[1], file)
        line_name.clear()
    with open(list_data[n][m][l]+'.json', 'w', encoding="utf-8") as file:
        json.dump(line_data, file)
        line_data.clear()
    for a in range(len(list_data)):
        for b in range(len(list_data[a])):
            for c in range(len(list_data[a][b])):
                if a != n or b != m or c != l:
                    with open(list_data[a][b][c]+'.json', 'r', encoding="utf-8") as file:
                        output_data = json.load(file)
                    with open(list_data[a][b][c]+'.json', 'w', encoding="utf-8") as file:
                        star = ''
                        for i in range(len(output_data[1])):
                            if output_data[1][i] == ' ':
                                star = star + '* '
                        for i in range(blank):
                            output_data.append(star)
                        json.dump(output_data, file)
    with open('list_data.json', 'w', encoding='utf-8') as file:
        json.dump(list_data, file)

##取得新資料庫編號
def list_record():
    with open('list_record.txt', 'r') as record:
        x = int(record.read())
    with open('list_record.txt', 'w') as record:
        record.write(str(x+1))
    return str(x)

##創建新資料庫
def add_new_file():
    global survey
    global grade
    global classname
    survey = input('問卷名稱: ')
    grade = int(input('年級: '))
    grade -= 1
    classname = input('班級名稱: ')
    with open('list_data.json', 'r', encoding='utf-8') as file:
        list_data = json.load(file)
    with open('survey_name.json', 'r', encoding="utf-8") as file:
        survey_name = json.load(file)
    with open('class_name.json', 'r', encoding='utf-8') as file:
        class_name = json.load(file)
    with open('class_name_dict.json', 'r', encoding='utf-8') as file:
        class_name_dict = json.load(file)
    with open('survey_name.json', 'w', encoding="utf-8") as file:
        if survey not in survey_name: 
            list_data.append([[] for i in range(4)])
            survey_name.append(survey)
        json.dump(survey_name, file)
    with open('class_name.json', 'w', encoding="utf-8") as file:
        if classname not in class_name: 
            class_name.append(classname)
        json.dump(class_name, file)
    with open('class_name_dict.json', 'w', encoding='utf-8') as file:
        if classname not in class_name_dict:
            list_data[survey_name.index(survey)][grade].append(list_record())
            class_name_dict[survey+str(grade)+classname] = len(list_data[survey_name.index(survey)][grade])-1
        json.dump(class_name_dict, file)
    with open('list_data.json', 'w', encoding='utf-8') as file:
        json.dump(list_data, file)

## 將學生資訊從資料庫中讀出
def r_id():
    with open(list_id[0], 'r', encoding="utf-8") as file:
        output_id[0] = json.load(file)
    with open(list_id[1], 'r', encoding="utf-8") as file:
        output_id[1] = json.load(file)

## 將資料初始化
def initialize_data():
    with open('list_data.json', 'r', encoding='utf-8') as file:
        list_data = json.load(file)
    for i in range(2):
        with open(list_id[i], 'w', encoding='utf-8') as file:
            json.dump([], file)
    for n in range(len(list_data)):
        for m in range(len(list_data[n])):
            for l in range(len(list_data[n][m])):
                os.remove(list_data[n][m][l]+'.json')
    with open('class_name_dict.json', 'w', encoding='utf-8') as file:
        json.dump({}, file)
    with open('survey_name.json', 'w', encoding='utf-8') as file:
        json.dump([], file)
    with open('class_name.json', 'w', encoding='utf-8') as file:
        json.dump([], file)
    with open('list_data.json', 'w', encoding='utf-8') as file:
        json.dump([], file)

## 輸出一段資料
def output_data_f(n, m, l, i):
    global final_output
    with open('list_data.json', 'r', encoding='utf-8') as file:
        list_data = json.load(file)
    if list_data[n][m][l] != "*":
        with open(list_data[n][m][l]+'.json', 'r', encoding="utf-8") as file:
            output_data = json.load(file)
        print(output_data[i], end = '')
        print('|', end=" ")
        final_output += output_data[i]
        final_output += '| '

##主程式
def main():
    while(True):
        global survey
        global grade
        global classname
        global final_output
        final_output = ''
        with open('list_data.json', 'r', encoding='utf-8') as file:
            list_data = json.load(file)
        question = input('模式選擇(W/R): ').upper()
        if question == 'W':
            mode = input("請選擇輸入模式 (1)輸入新資料 (2)初始化 (3)修改已建檔之資料: ")
            ## mode 1: create new file
            while(True):
                if mode == '1':
                    path = input("請輸入數據之檔名: ")
                    input_data(path)
                    add_new_file()
                    with open('survey_name.json', 'r', encoding='utf-8') as file:
                        survey_name = json.load(file)
                    with open('class_name_dict.json', 'r', encoding='utf-8') as file:
                        class_name_dict = json.load(file)
                    w_data(survey_name.index(survey), grade, class_name_dict[survey+str(grade)+classname])
                    break
                ## mode 2: initialize
                elif mode == '2':
                    pattern = int(input('(1)初始化全部資料(2)初始化指定資料: '))
                    ## initialize all file
                    if pattern == 1:
                        initialize_data()
                        break
                    ## initialize specific file
                    elif pattern == 2:
                        locate_file()
                        with open('list_data.json', 'r', encoding='utf-8') as file:
                            list_data = json.load(file)
                        with open('survey_name.json', 'r', encoding="utf-8") as file:
                            survey_name = json.load(file)
                        with open('class_name_dict.json', 'r', encoding='utf-8') as file:
                            class_name_dict = json.load(file)  
                        os.remove(list_data[survey_name.index(survey)][grade][class_name_dict[survey+str(grade)+classname]]+'.json')                        
                        list_data[survey_name.index(survey)][grade][class_name_dict[survey+str(grade)+classname]] = "*"
                        count = 0
                        for i in range (4):
                            for j in range (len(list_data[survey_name.index(survey)][i])) :
                                if list_data[survey_name.index(survey)][i][j] == "*" :
                                    count += 1
                            if count == len(list_data[survey_name.index(survey)][i]) :
                                list_data[survey_name.index(survey)][i].clear()
                            count = 0
                        if list_data[survey_name.index(survey)] == [[], [], [], []]:
                            k = survey_name.index(survey)
                            del list_data[k]
                            del survey_name[k]
                        ## delete in class_name_dict
                        del class_name_dict[survey + str(grade) + classname]
                        ## delete from survey name
                        with open('list_data.json', 'w', encoding='utf-8') as file:
                            json.dump(list_data, file)
                        with open('survey_name.json', 'w', encoding='utf-8') as file:
                            json.dump(survey_name, file)
                        with open('class_name_dict.json', 'w', encoding='utf-8') as file:
                            json.dump(class_name_dict, file)
                        break
                    ## users enter garbage : skip this round
                    else: break
                ## mode 3: rewrite data into exist file
                elif mode == '3':
                    ## choose which file user want to rewrite
                    locate_file()
                    with open('survey_name.json', 'r', encoding="utf-8") as file:
                        survey_name = json.load(file)
                    with open('class_name_dict.json', 'r', encoding='utf-8') as file:
                        class_name_dict = json.load(file)
                    path = input("請輸入數據之檔名: ")
                    input_data(path)
                    w_data(survey_name.index(survey), grade, class_name_dict[survey+str(grade)+classname])
                    break
                ## if users enter garbage: skip to the previous question
                else: break
        elif question == 'R':
            r_id()
            ## 讓使用者決定欲使用之部分
            pattern = input("請選擇輸出資料模式 (1)輸出所有資料 (2)以人名輸出資料 (3)輸出指定資料 (4)輸出多指定資料中的共同受測者 (5)輸出目前有哪些問卷: ")
            ## 印出所有資料
            if pattern == '1':
                print("所有資料:\n")
                for i in range(len(output_id[1])):
                    print(output_id[0][i] + ' ' + output_id[1][i], end = ' ')
                    final_output += output_id[0][i] + ' ' + output_id[1][i] + ' '
                    for n in range(len(list_data)):
                        for m in range(len(list_data[n])):
                            for l in range(len(list_data[n][m])):
                                output_data_f(n, m, l, i)
                    print('\n', end = '')
                    final_output += '\n'
            ## 以人名輸出資料
            elif pattern == '2':
                ## user enter data's name they want
                name = str(input("請輸入欲搜尋之人名: "))
                ## find which index is the name    
                index = output_id[1].index(name)
                ## print out student's id (account and name)
                print(output_id[0][index] + ' ' + output_id[1][index], end = ' ')
                final_output += output_id[0][i] + ' ' + output_id[1][i] + ' '
                for n in range(len(list_data)):
                    for m in range(len(list_data[n])):
                        for l in range(len(list_data[n][m])):
                            output_data_f(n, m, l, index)
                print('\n', end = '')
                final_output += '\n'
            ## 輸出多份指定資料
            elif pattern == '3' :
                multioutput_data = []
                while (True) :
                    locate_file()
                    ## read in specific data
                    with open('survey_name.json', 'r', encoding="utf-8") as file:
                        survey_name = json.load(file)
                    with open('class_name_dict.json', 'r', encoding='utf-8') as file:
                        class_name_dict = json.load(file)           
                    with open(list_data[survey_name.index(survey)][grade][class_name_dict[survey+str(grade)+classname]]+'.json', 'r', encoding="utf-8") as file:
                        output_data = json.load(file)
                        multioutput_data.append(output_data)
                    ## ask if user want to enter more data
                    repeat = int(input("是否要再輸出其他數據 (1)是 (2)否: "))
                    if repeat == 2 : break
                ## check if the student has data in here
                for i in range(len(multioutput_data[0])): ## to check all student
                    to_print = False
                    for j in range(len(multioutput_data)):  ## to run all choosed survey
                        if multioutput_data[j][i][0] != '*' : to_print = True     ## need to print
                    if to_print:
                        print(output_id[0][i] + ' ' + output_id[1][i], end = ' ') ## print out student
                        final_output += output_id[0][i] + ' ' + output_id[1][i] + ' '
                        for j in range(len(multioutput_data)):
                            print(multioutput_data[j][i], end = '')
                            print('|', end=" ")
                            final_output += multioutput_data[j][i]
                            final_output += '| '
                        print('\n', end = '')
                        final_output += '\n'
            ##輸出多份指定資料的共同受試者
            elif pattern == '4':
                multioutput_data = []
                while(True):
                    locate_file()
                    with open('survey_name.json', 'r', encoding="utf-8") as file:
                        survey_name = json.load(file)
                    with open('class_name_dict.json', 'r', encoding='utf-8') as file:
                        class_name_dict = json.load(file)
                    with open(list_data[survey_name.index(survey)][grade][class_name_dict[survey+str(grade)+classname]]+'.json', 'r', encoding='utf-8') as file:
                        output_data = json.load(file)
                        multioutput_data.append(output_data)
                    repeat = input("是否要再輸出其他數據 (1)是 (2)否: ")
                    if repeat == '2': break
                for i in range(len(multioutput_data[0])):
                    to_print = True
                    for j in range(len(multioutput_data)):
                        if multioutput_data[j][i][0] == '*': to_print = False
                    if to_print:
                        print(output_id[0][i] + ' ' + output_id[1][i], end = ' ')
                        final_output += output_id[0][i] + ' ' + output_id[1][i] + ' '
                        for j in range(len(multioutput_data)):
                            print(multioutput_data[j][i], end = '')
                            print('|', end=" ")
                            final_output += multioutput_data[j][i]
                            final_output += '| '
                        print('\n', end = '')
                        final_output += '\n'
            ##輸出目前有哪些問卷
            elif pattern == '5':    
                with open('survey_name.json', 'r', encoding="utf-8") as file:
                    survey_name = json.load(file)
                with open('class_name.json', 'r', encoding='utf-8') as file:
                    class_name = json.load(file)
                with open('class_name_dict.json', 'r', encoding='utf-8') as file:
                    class_name_dict = json.load(file)
                for i in range(len(survey_name)):
                    for j in range(4):
                        for k in range(len(class_name)):
                            if survey_name[i]+str(j)+class_name[k] in class_name_dict:
                                print(survey_name[i], str(j+1)+"年級", class_name[k], sep = ' ')
        else:
            continue
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(final_output)

if __name__ == '__main__':
    main()
