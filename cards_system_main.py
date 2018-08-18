import cards_system_tools


while 1:
    num = 0
    print('*' * 70)
    print('欢迎使用名片管理系统\n')
    print('1.新建名片\n2.显示全部\n3.查询名片\n')
    print('0.退出系统')
    print('*' * 70)
    option_str = input('请选择想要执行的功能（1 or 2 or 3 or 0）:')
    if option_str in ['1', '2', '3']:
        if option_str == '1':       #  新增名片
            print('-' * 70)
            print('您选择的功能是新增名片！')
            cards_system_tools.new_card()
        elif option_str == '2':     #  显示全部
            print('-' * 70)
            print('您选择的功能是显示全部名片！')
            cards_system_tools.show_cards()
        else:                       # 查询名片
            print('-' * 70)
            print('您选择的功能是查询名片！')
            cards_system_tools.search_card()
    elif option_str == '0':         #  退出程序
        break
    else:
        print('您输入有误，请重新输入！')
        # print('\n\n\n')
print('您已经退出了名片管理系统！！！')



