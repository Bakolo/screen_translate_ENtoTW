import re
import os

dict_folder = "dict_src"
def go(text_src):
    word_cnt = analysis_text(text_src)
    record_data(word_cnt)
    output_select_src_file(word_cnt)

def output_select_src_file(word_cnt):
    global dict_folder
    answer = input("select times range('x', 'x,y,z', 'x-y' or 'all'): ")

    file_idx = 0
    while file_idx < (file_idx + 1):
        if not os.path.exists(f"{dict_folder}/en_{file_idx}.txt"):
            break
        file_idx += 1
            
    f_src_name = f"{dict_folder}/en_{file_idx}.txt"
    print(f"create new EN source file: {f_src_name}")
    print(f">====please copy following word's translate and paste to a new file {dict_folder}/tw_{file_idx}.txt============================================\n\n")
    f_src = open(f_src_name, 'w')

    if answer.lower() == 'all':
        for word in word_cnt:
            if type(word) == str:
                print(word)
                f_src.write(f'{word}\n')
    elif '-' in answer:
        try:
            start = int(answer.split('-')[0])
            end = int(answer.split('-')[1])
            show = False
            for word in word_cnt:
                if type(word) == int:
                    show = True if word in range(start, end+1) else False
                elif show:
                    print(word)
                    f_src.write(f'{word}\n')
        except:
            pass
    elif ',' in answer:
        try:
            tmp_list = answer.split(',')
            show = False
            for word in word_cnt:
                if type(word) == int:
                    show = True if str(word) in tmp_list else False
                elif show:
                    print(word)
                    f_src.write(f'{word}\n')
        except:
            pass
    else:
        try:
            start = word_cnt.index(int(answer))
            for word in word_cnt[start+1:]:
                if type(word) == int:
                    break
                print(word)
                f_src.write(f'{word}\n')
        except:
            pass

    f_src.close()
    print("\n<================================================\n\n")


def record_data(word_list):
    with open('word_cnt.txt', 'w') as fw:
        for word in word_list:
            if word in range(1,100):
                fw.write(f'\n{word} times:\n')
                print(f'\n{word} times:\n')
            else:
                fw.write(f'  {word}')
                print(f' {word}', end="")
    print('\n')


def analysis_text(src):
    with open(src, 'r', encoding="utf-8") as fs:
        word_cnt_list = [1]
        for line in fs:
            #replace all symbol by ' '
            lower_split = re.sub(r'[^\w]', ' ', line.lower()).split()
            #count each word 
            for word in lower_split:
                if len(word) < 3:   #filter the word length less than 3
                    continue
                #find the position of word in word_cnt_list
                try:
                    position_current = word_cnt_list.index(word)
                    word_cnt_list.pop(position_current)
                except:
                    position_current = -1
                #find word belone which cnt and the target index(position_new) to insert
                nu_idx = 0
                position_new = -1
                try:
                    #max cnt 100, dont care if cnt >= 99
                    for nu_idx in range(1,100):
                        pos_tmp = word_cnt_list.index(nu_idx)
                        if pos_tmp >= position_current:
                            position_new = pos_tmp + 1
                            break
                    else:
                        pass
                        #position_new = len(word_cnt_list)
                        
                except:
                    word_cnt_list.append(nu_idx)
                    position_new = len(word_cnt_list)
                if position_new > 0:
                    word_cnt_list.insert(position_new, word)
    return word_cnt_list




