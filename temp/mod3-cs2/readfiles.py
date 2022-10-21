from collections import defaultdict

def read_file():
    file_path = 'unmv8h36uh/777_m3_datasets_v1.0/bank-data.csv'
    file_reader = open(file_path)
    
    dict_list=[]
    prof_list=[]
    ddl = defaultdict(list)

    try: 
        for line in file_reader.readlines():
            sline = line.replace('\n','').split(',', maxsplit=4)
            dict_list.append(sline)
        
            if sline[1] not in prof_list:
                prof_list.append(sline[1])            # list created
        
        for x in range(0, len(dict_list)):
            for y in range(0, len(prof_list)):
            
                if prof_list[y] in dict_list[x]:
                    ddl[prof_list[y]].append(dict_list[x] )                     
        
    finally:
        file_reader.close()
        return ddl


def read_input():
    in_prompt = 'What is the profession?  '
    in_prompt += '\n' 
    return input(in_prompt)


def main():
    profs_dict = read_file()

    user_input = ''
    #user_out
    while True:
        try:
            user_input = read_input()  
        except EOFError:
            break
        if user_input != '' and profs_dict[user_input] !='':
            print('List per profession: ',user_input)
            print(profs_dict[user_input])
        else:
            print('Invalid Response')
        break
    
  
if __name__=="__main__" :
    main()
 