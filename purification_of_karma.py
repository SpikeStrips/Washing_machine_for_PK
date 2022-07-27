
# Даже падая на пол,
# Улыбнусь и повторю:
# К черту Эпик, Замок, Холл
# Больше это не ценю!
#
# Мало сможет кто понять,
# И до самой той поры..
# Буду нежно умертвлять
# Обитателей игры
# © Enemy

# Привет всем красным с астериоса х5 и в особенности всем ребятам из BetOnRed, Enemy и Crips =))

import random
import pyautogui
import keyboard
import time
from ahk.window import Window
from ahk import AHK
from playsound import playsound

ahk = AHK()

try:
    # Ищём айдишник окна №1 и записываем его в переменную.
    win = ahk.win_wait(title='Asterios', timeout=5)
    win = str(win)
    start_search_id = win.find('=') + 1
    end_search_id = win.find('>')
    win_id = win[start_search_id:end_search_id]
    print('\nайдишник окна #1 записан в переменную!'.upper(), '\n    его значение = {}\n'.upper().format(win_id))
    print('скрипт готов к работе!\n'.upper())
    print('-----------------------------------------------------')
    print('теперь можно смело заводить окно №2 и мыться =)'.upper())
    print('-----------------------------------------------------')
    time.sleep(2)
    print('\n  Основные комбинации клавиш:'.upper())
    print('\n    1. Пробел + 1 - Начать отмывку!')
    print('    2. Пробел + 2  - Закончить отмывку!')

    while True:
        if keyboard.is_pressed("space + 1"):  # ===> Начать мойку.
            time.sleep(3)
            playsound('sounds\pukane-28.mp3') # ===> Тот самый пук xD.
            print('\n Скрипт запущен!')
            while True:
                win = Window(ahk, ahk_id=win_id) # ===> Задаем программе наше окно (указывая, найденый ранее айдишник)
                random_numberF = random.randint(1, 12) # ===> Генерирует случайное число от 1 до 12 (Это клавиши f1-f12)
                random_numberF = str(random_numberF)
                win.send('{F' + (random_numberF) + '}') # ===> Рандомно нажимает в окне №1 клавишу от f1 до f12 (Тем самым ресает)
                time.sleep(15)
                startButton = pyautogui.locateOnScreen('accept.png', confidence=0.7) # ===> Ищет в окне №2 координаты 'ПРИНЯТЬ'
                time.sleep(1)
                if keyboard.is_pressed("space + 2"): # ===> Закончить мойку.
                    playsound('sounds\pukane-35.mp3') # ===> Еще один пук xD.
                    print('\n Скрипт остановлен!')
                    break

                if startButton == None:
                    print('', end='')

                # Жмякает по кнопке 'ПРИНЯТЬ' и автоматически встает после реса!
                else:             
                    pyautogui.click(x=startButton[0], y=startButton[1])
                    pyautogui.mouseDown();
                    pyautogui.mouseUp()



except TimeoutError:
    print('-------------------------------------')
    print(' АЙДИШНИК ОКНА №1 НЕ НАЙДЕН!\n ПОПРОБУЙТЕ ЕЩЕ РАЗ!')
    print('-------------------------------------')
    time.sleep(15)

