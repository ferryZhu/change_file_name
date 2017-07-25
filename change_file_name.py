#! /usr/bin/env python  
# -*- coding:utf-8 -*- 

# __author__ = "Ferry Zhu"  
# Version:1.0.0
# 替换此目录下的所有文件

import os
import re

def change_file_name(path, find, replace):
    ret = []
    current_root = ''
    for root, dirs, files in os.walk(path):
        for filepath in files:
        	matchObject = re.match(find, filepath)
        	if matchObject:
	        	oldFile = os.path.join(root,filepath)
	        	newFile = oldFile.replace(find, replace)
	        	os.renames(oldFile, newFile)
	        	print('%s 已改为：%s' % (os.path.join(root,filepath), newFile))

if __name__ == '__main__':
	find = input("请输入要查找的文本：")
	replace = input('请输入替换的文本:')
	change_file_name("./", find, replace)
