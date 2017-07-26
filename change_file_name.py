#! /usr/bin/env python  
# -*- coding:utf-8 -*- 

# __author__ = "Ferry Zhu"  
# Version:1.0.0
# 替换iOS项目目录、文件

import os
import re

def change_file_name(path, find, replace):
    ret = []
    current_root = ''
    for root, dirs, files in os.walk(path):
        for filepath in files:
        	oldFile = os.path.join(root,filepath)
        	# 匹配.h .m
        	match = re.match('[a-zA-Z+]*\.(h|m|pch)', filepath)
        	if match:
        		with open(oldFile, 'r', encoding='utf-8') as f:
        			file = f.read()
        		if re.search(find, file):
        			newFile = file.replace(find, replace)
        			with open(oldFile, 'w') as f:
        				f.write(newFile)
        	matchObject = re.match(find, filepath)
        	if matchObject:
	        	newFile = oldFile.replace(find, replace)
	        	os.renames(oldFile, newFile)
	        	print('%s 已改为：%s' % (os.path.join(root,filepath), newFile))

def change_dir_name(path, find, replace, find_file, replace_file):
	for root, dirs, files in os.walk(path):
		for dir in dirs:
			matchObject = re.match(find, dir)	# 从头匹配
			if matchObject:
				# 修改目录名称
				new_name = dir.replace(find, replace)
				os.renames(dir, new_name)
				match_xcodeproj = re.search('xcodeproj', new_name)
				if match_xcodeproj:
					# 切换至*.xcodeproj目录下
					os.chdir(new_name)
					# 写出project.pbxproj
					with open('project.pbxproj', 'r') as f:
						project = f.read()
					# 修改project.pbxproj
					new_project = project.replace(find, replace)
					new_project = new_project.replace(find_file, replace_file)
					# 重新写入project.pbxproj
					with open('project.pbxproj', 'w') as f:
						f.write(new_project)

def change_entitlements_name(path, find, replace):
	for root, dirs, files in os.walk(path):
		for filepath in files:
			match_entitlements = re.search('entitlements', filepath)
			if match_entitlements:
				print(filepath)
				oldFile = os.path.join(root, filepath)
				newFile = os.path.join(root, filepath.replace(find, replace))
				os.renames(oldFile, newFile)
				print('%s 已改为: %s' % (oldFile, newFile))

if __name__ == '__main__':
	print("修改文件名称：")
	find_file = input("请输入要查找的文本：")
	replace_file = input('请输入替换的文本:')
	change_file_name("./", find_file, replace_file)
	print("修改目录名称：")
	find = input("请输入要查找的文本：")
	replace = input("请输入替换的文本：")
	change_entitlements_name("./", find, replace)
	change_dir_name("./", find, replace, find_file, replace_file)
	print("替换完成！")
