# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:14:17 2017

@author: GIS
"""

import os
import time

source = ['"input_folder", "input_folder"']

target_dir = 'output_folder' 

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Введите комментарий --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_')fgh + '.zip'

if not os.path.exists(today):
    os.mkdir(today) 
print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
