team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / (score_1 + score_2), 1)
def get_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'
challenge_result = get_result()

print('В команде Мастера кода участников: %(num)s !' % {'num': team1_num})

print('Итого сегодня в командах участников: %(t1)s и %(t2)s !' % {'t1': team1_num, 't2': team2_num})

print('Команда Волшебники данных решила задач: {} !'.format(score_2))

print('Волшебники данных решили задачи за {} с !'.format(team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')

print(f'Результат битвы: победа команды {challenge_result}!')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
