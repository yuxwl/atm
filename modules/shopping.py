#!/usr/bin/env python
import os,json,time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
__db_product = BASE_DIR + r"\database\product_list"
__db_shoping_car = BASE_DIR + r"\database\shoping_car"
__db_users_dict = BASE_DIR + r"\database\users_dict"
__db_creditcard = BASE_DIR + r"\database\creditcard_dict"
__db_shopping_record = BASE_DIR + r"\database\shopping_record"
__db_creditcard_record = BASE_DIR +r"\database\creditcard_record"

'''购物商城'''
def Shopping_mall():
    shopping_list,pro_list = [],[]
    with open(__db_product,"r",encoding="utf-8") as f_product:
        for item in f_product:
            pro_list.append(item.strip("\n").split())

    def pro_inf():
        print ("编号\t\t商品\t\t价格")
        for index,item in enumerate(pro_list):
            print ("%s\t\t%s\t\t%s" %(index,item[0],item[1]))

    while True:
        print (("\33[31;0m目前商城在售的商品信息\33[0m").center(40,"-"))
        pro_inf()
        choice_id = input("\n\33[34;0m选择要购买的商品编号 【购买 ID】/【返回 b】\33[0m")
        if choice_id.isdigit():
            choice_id = int(choice_id)
            if choice_id < len(pro_list) and choice_id >=0:
                pro_item = pro_list[choice_id]
                print ("\33[31;0m商品 %s 加入购物车 价格 %s\33[0m" %(pro_item[0],pro_item[1]))
                shopping_list.append(pro_item)
            else:
                print ("\33[31;0m错误:没有相应的编号,请重新输入: \33[0m")
        elif choice_id == "b":
            with open(__db_shoping_car,"r+") as f_shopping_car:
                list = json.loads(f_shopping_car.read())
                list.extend(shopping_list)
                f_shopping_car.seek(0)
                f_shopping_car.truncate(0)
                list = json.dumps(list)
                f_shopping_car.write(list)
            break
        else:
            print ("\33[31;0m错误:没有相应的编号,请重新输入:\33[0m")

'''清空购物车'''
def Empty_shopping_car():
    with open(__db_shoping_car,"w") as f_shopping_car:
        list = json.dumps([])
        f_shopping_car.write(list)


'''购物车'''
def Shopping_car():
    while True:
        with open(__db_shoping_car,"r+")  as f_shopping_car:
            list = json.loads(f_shopping_car.read())
            sum =0
            print ("\33[32;0m购物车信息清单\33[0m".center(40,"-"))
            for index,item in enumerate(list):
                print (index,item[0],item[1])
                sum += int(item[1])
            print ("\33[31;0m商品总额共计: %s\33[0m"%(sum))
        if_buy = input("\33[34;0m选择要进行的操作 返回【b】/清空【f】\33[0m")
        if if_buy =="b":
            break
        if if_buy == "f":
            Empty_shopping_car()


'''购物记录'''
def Shoppingcar_record(current_user,value):
    with open(__db_shopping_record,"r+") as f_shoppingcar_record:
        record_dict = json.loads(f_shoppingcar_record.read())
        month = time.strftime("%Y-%m-%d",time.localtime())
        times = time.strftime("%H-%M-%S")
        if str(current_user) not in record_dict.keys():
            record_dict[current_user]={month:{time:value}}
        else:
            if month not in record_dict[current_user].keys():
                record_dict[current_user][month] = {times:value}
            else:
                record_dict[current_user][month][times]  = value
        dict = json.dumps(record_dict)
        f_shoppingcar_record.seek(0)
        f_shoppingcar_record.truncate(0)
        f_shoppingcar_record.write(dict)