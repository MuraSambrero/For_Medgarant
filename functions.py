import datetime


def find_free_time(sorted_busy) -> list:
	
	'''Создаем список - free_time, 
	со свободными интервалами на основе данного списка'''

	free_time = []
	for i in range(len(sorted_busy)):
		try:
			interval = {
			'begin': sorted_busy[i]['stop'] + ':00',
			'end': sorted_busy[i+1]['start'] + ':00'
			}
			free_time.append(interval)
		except IndexError:
			pass
		
	if sorted_busy[0]['start'] != '09:00:00':
		interval = {
		'begin': '09:00:00',
		'end': sorted_busy[0]['start'] + ':00'
		}
		if interval['begin'] != interval['end']:
			free_time.insert(0, interval)

	last_index = len(sorted_busy)-1		
	if sorted_busy[last_index]['stop'] != '21:00':
		interval = {
		'begin': sorted_busy[last_index]['stop'] + ':00',
		'end': '21:00:00'
		}
		free_time.append(interval)
	return free_time


def find_all_free_interval(free_time):

	'''К каждому элементу списка free_time 
	применяем функцию calculation_interval'''

	all_free_interval = []
	for elem in free_time:
		first = datetime.datetime.strptime(elem['begin'], "%H:%M:%S")
		last = datetime.datetime.strptime(elem['end'], "%H:%M:%S")
		standart_interval = datetime.datetime.strptime('01:00:00', "%H:%M:%S")\
							- datetime.datetime.strptime('00:30:00', "%H:%M:%S")
		while first < last and last - first >= standart_interval:
			all_free_interval.append(str(first.time()))
			first = first + standart_interval
	return all_free_interval

		