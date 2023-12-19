from functions import find_all_free_interval, find_free_time
from busy import busy
from pprint import pprint

sorted_busy = sorted(busy, key=lambda elem: elem['start']) # получаем отсортированный словарь
free_time = find_free_time(sorted_busy) # получаем свободные интервалы
all_free_interval = find_all_free_interval(free_time) # получаем свободные интервалы по 30 минут
pprint(all_free_interval) # выводим полученный список c возможными записями