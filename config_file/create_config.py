url = 'http://testfk3.chexiao.co/'  # url--测试环境
# url = 'http://fk.chexiao.co'  # url--线上环境
username = "xinxinceshi"    # 账号
password = "961111"     # 密码
code = "535"    # 验证码

# 装机工单的信息
car_name = "车晓测试查车3"                     # 车主姓名
car_tel = "13252635263"                   # 车主电话
car_frame_no = "ZASXCDEDSXCD15551"        # 车架号
car_brand = "大众"                        # 车辆品牌
car_model = "cc"                          # 辆型号
car_placeholder = "广汽中山"                # 所属部门输入搜索的信息
car_shop_name = "广汽中山合益店"          # 所属部门
car_plan_installTime = "2020-02-26 18:29:46"        # 计划安装时间
car_contact_name = "哈哈"                 # 现场联系人
car_contact_status = "身份"               # 现场联系人身份
car_contact_tel = "13205059696"           # 现场联系人电话
car_wire_equip = 1                        # 有线
car_wireless_equip = 0                    # 无线
car_obd_equip = 0                         # OBD
data = {                                  # 工作地址、居住地址、安装地址
    # '工作地址': {
    #     'div_class': '.wP100.mrg0.el-row',
    #     'province': '北京市',
    #     'city': '朝阳区',
    #     'address': '12345',
    # },
    # '居住地址': {
    #     'div_class': '.wP100.mrg0.el-row',
    #     'province': '四川省',
    #     'city': '成都市',
    #     'address': '67890',
    # },
    '安装地址': {
        'div_class': '.installInfo .el-row.el-row--flex',
        'province': '吉林省',
        'city': '松原市',
        'address': '呸呸呸',
    }
}
