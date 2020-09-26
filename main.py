#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict:
            return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за {} попыток".format(score))
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Находим значение числа, которое равно середине отрезка и потом в зависимости от того больше оно или меньше, загаданного числа, изменяем границы отрезка.'''
    a=0
    b=101
    count = 1
    predict=(a+b)//2 # число равное середине отрезка
    while number != predict:
        count+=1
        if number < predict:
            b=predict # меняем границу числа если оно меньше загаданного числа
        elif number > predict:
            a = predict # меняем границу числа если оно больше загаданного числа
        predict = (a+b)//2 # находим значение числа равное середине нового отрезка
    return(count) # выход из цикла если угадали

score_game(game_core_v3)
