card_list = []


def new_card():
    """
    新增名片
    """
    print('-' * 70)
    name_str = input('请输入名字：')
    age_str = input('请输入年龄：')
    phone_str = input('请输入电话：')
    print('-' * 70)
    card_dict = {'name': name_str,
                 'age': age_str,
                 'phone': phone_str}
    card_list.append(card_dict)
    print('新建名片成功！')
    print('*' * 70)
    print('按回车键回到上一级菜单')
    print('*' * 70)
    input()


def show_cards():
    """
    显示所有名片
    """
    print('=' * 70)
    if len(card_list) == 0:
        print('系统里并没有存入名片！')
    else:
        for caption_list in ['姓名', '年龄', '电话']:
            print('%s' % caption_list, end='\t\t\t|\t\t\t')
        print('')
    print('=' * 70)
    for card_dict in card_list:
        print('%s\t\t\t|\t\t\t%s\t\t\t|\t\t\t%s\t\t\t|' % (card_dict['name'],
                                                        card_dict['age'],
                                                        card_dict['phone']))
        print('-' * 70)
    print('*' * 70)
    print('按回车键回到上一级菜单')
    print('*' * 70)
    input()


def search_card():
    """

    名片查找功能函数
    """
    print('欢迎使用名片查找功能！')
    search_name = input('请输入想要寻找的名字:')
    for card_dict in card_list:
        if card_dict['name'] == search_name:
            print('找到啦！！！')
            for caption_list in ['姓名', '年龄', '电话']:
                print(caption_list, end='\t\t|\t\t')
            print('\n')
            print('%s\t\t|\t\t%s\t\t|\t\t%s\t\t|\t\t' % (card_dict['name'],
                                                             card_dict['age'],
                                                             card_dict['phone']))
            deal_card(card_dict)
            return
    else:
        print('很遗憾，查无此人！')
        print('*' * 70)
        print('按回车键回到上一级菜单')
        print('*' * 70)
        input()


def deal_card(find_dict):
    """

    :param find_dict: 对名片系统中的名片进行修改
    """
    while 1:
        deal = input('想要修改名片请输入1、想要删除名片请输入2、返回主菜单请输入0')
        if deal in ['1', '2']:
            if deal == '1':
                print('xiugai')
                name_change_str = input('请输入修改后的名字（回车不修改）：')
                if len(name_change_str) > 0:
                    find_dict['name'] = name_change_str
                age_change_str = input('请输入修改后的年龄（回车不修改）：')
                if len(age_change_str) > 0:
                    find_dict['age'] = age_change_str
                phone_change_str = input('请输入修改后的电话（回车不修改）：')
                if len(phone_change_str) > 0:
                    find_dict['phone'] = phone_change_str
                print('修改成功！')
                print('*' * 70)
                print('按回车键回到上一级菜单')
                print('*' * 70)
                input()
                break
            else:
                card_list.remove(find_dict)
                print('删除成功！')
                print('*' * 70)
                print('按回车键回到上一级菜单')
                print('*' * 70)
                input()
                break
        elif deal == '0':
            break
        else:
            print('您输入的有误，请重新输入！！')



