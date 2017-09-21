#!/usr/bin/env python

import os,sys

#程序目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#添加环境变量
sys.path.append(BASE_DIR)

from modules import admincenter,shopping,authentication,creditcard

while True:
    print ("\33[35;1m欢迎进入信用卡购物模拟程序\33[0m".center(50,"#"),
            "\n1 购物中心\n"
            "2 信用卡中心\n"
            "3 后台管理\n"
            "q 退出程序\n")
    choice_id  = input("\33[34;0m选择要进入的模式的ID\33[0m:")

    if choice_id == "1":
        res = authentication.user_auth()
        if res != None:
            if res[0] == "True":
                current_user = res[1]
                shopping.Shopping_mall()







        









