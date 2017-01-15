# -*- coding:utf-8 -*-
# 根据西南大学给出的成绩和学分直接计算GPA
# 计算公式为
# (课程1成绩*课程1学分+课程2成绩*课程2学分+...+课程n成绩*课程n学分)*4/总学分*100

def gpa( grade_list ):
    sum = 0.0
    xf = 0.0
    for i in grade_list:
        sum += float(i['cj']) * float(i['xf'])
        xf += float(i['xf'])

    return sum * 4 / (xf * 100);


def method( ):
    return "(课程1成绩*课程1学分+课程2成绩*课程2学分+...+课程n成绩*课程n学分)*4/总学分*100";
