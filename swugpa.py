# -*- coding:utf-8 -*-
import json

import requests

import gpa.swugpa as swu


# 查询成绩
# xnm,xqm 为空时查询所有学年学期
# 教务系统查询API详见https://github.com/xndxcsd
def get_grade( swuid, password, xnm='', xqm='' ):
    value = {
        "swuID": swuid,
        "password": password,
        "xnm": xnm,
        "xqm": xqm
    }

    url = 'http://opensource.desu.pub:29527/openswu/grade/'
    # url = 'http://localhost:29527/openswu/grade/'
    param = json.dumps(value).encode()
    head = {
        "Authorization": "Basic %s" % ("b3BlbnNvdXJjZTpmcmVlZG9t"),
        "Content-Type": "application/json; charset=utf-8",
    }

    return json.loads(requests.post(url, data=param, headers=head).text)['items']


# unicode to utf-8
def u2u( grade ):
    for i in grade:
        for k in i:
            i[k] = i[k].encode('utf-8')

    return grade


# 解析成绩
# 将必修课和所有课分别返回到必修课列表和选修课数组中
def prase_grade( grade ):
    bxgrade = []
    allgrade = []

    for i in grade:
        allgrade.append(i)
        if '必修课' in i['kcxzmc']:
            bxgrade.append(i)

    return bxgrade, allgrade


# main:
if __name__ == '__main__':

    # 处理成绩信息
    swuid = raw_input("swuid : ")
    password = raw_input("password : ")

    try:
        grade_list = u2u(get_grade(swuid, password))
    except:
        print "gg 服务器崩溃啦"
        exit()

    bxgrade, allgrade = prase_grade(grade_list)

    print '您的必修课GPA为 : %.2f\n' \
          '您的所有课GPA为 : %.2f\n' \
          '计算方法为 : %s' % \
          (swu.gpa(bxgrade),
           swu.gpa(allgrade),
           swu.method())
