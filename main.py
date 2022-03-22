import os
from PIL import Image
import pytesseract as tsr
import sys
import time
import json
import re

import screen_grab as sgrab
import mouse_clk as mclk
import json_operator
import readpic
import train_dict as tdict

lang_dict = dict()
param_train = ['-t', '--train']
param_help = ['-h','--help']


def translate_text(text_in):
    global lang_dict
    trans_src = re.sub(r'[^\w]', ' ', text_in.lower())
    #data = ["xx" if ch not in lang_dict else lang_dict[ch]  for ch in trans_src.split()]
    #data = " ".join(data)
    data = ""
    for ch in trans_src.split():
        data += f"{ch} " if ch not in lang_dict else f"{ch}({lang_dict[ch]}) "

    #print(">--original start---------------------")
    #print(text_in)
    #print(">--original start---------------------")
    #print(trans_src)
    #print(">--translate start---------------------")
    print("$: "+data)
    #print(">--translate end---------------------")

def load_trans_script():
    #data = json_operator.load_json("trans_script.json")
    data = dict()
    en_file_list = [f for f in os.listdir(tdict.dict_folder) if 'en' in f]
    tw_file_list = [f for f in os.listdir(tdict.dict_folder) if 'tw' in f]
    
    print("Load the dictionary source file:")
    print(f"en file: {en_file_list}")
    print(f"tw file: {tw_file_list}")
    for en_file in en_file_list:
        sub_name = en_file.split('_',1)[1]
        tw_file = f"tw_{sub_name}"
        if tw_file not in tw_file_list:
            continue
        f_en = open(f"{tdict.dict_folder}/{en_file}",'r')
        f_tw = open(f"{tdict.dict_folder}/{tw_file}",'r', encoding="utf-8")
        for line in f_en:
            line_en = line.strip()
            line_tw = f_tw.readline().strip()
            if line_en in data:
                data[line_en] += f", {line_tw}"
            else:
                data.setdefault(line_en, line_tw)
    #print(data)
    return data

def show_help():
    print('''
    -h, --help : show help information
    -t, --train: load a text file to and export a en_X.txt file
                 -t xxx.txt
    ''')
    pass

def train_script():
    global param_train
    text_src = [sys.argv[idx+1] for idx, f in enumerate(sys.argv) if f in param_train]
    tdict.go(text_src[0])
    pass

if __name__ == "__main__":
    if [p for p in sys.argv if p in param_help]:
        show_help()
    elif [p for p in sys.argv if p in param_train]:
        train_script()
    else:
        lang_dict = load_trans_script()
        print('>>=== Right-click mouse twice to select the OCR zone')
        zone = mclk.start_listen()

        tsr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pre_text, read_text = "", ""
        
        while True:
            time.sleep(1)
            img = sgrab.screen_grab(zone[0],zone[1],zone[2],zone[3])
            read_text = readpic.read_image(img)
            if pre_text == read_text:
                continue
            pre_text = read_text
            translate_text(read_text)


