from time import perf_counter

time1 = perf_counter()
hospitals = {'Atlanta': ['Xavier', 'Yolanda', 'Zeus'],
        'Boston': ['Yolanda', 'Xavier', 'Zeus'],
        'Chicago' : ['Xavier', 'Yolanda', 'Zeus']}


students = {'Xavier': ['Boston', 'Atlanta', 'Chicago'],
            'Yolanda': ['Atlanta', 'Boston', 'Chicago'],
            'Zeus': ['Atlanta', 'Boston', 'Chicago']}

answers = {'Xavier': 'Atlanta',
          'Zeus' : 'Boston',
           'Yolanda': 'Chicago'}


for selected_student, selected_hospital in answers.items():
    stud_to_check = hospitals[selected_hospital][:hospitals[selected_hospital].index(selected_student)]

    flag = False
    for student in stud_to_check:
        for hospital in students[student]:
            if hospital == answers[student]:
                break

            if hospital == selected_hospital:
                flag = True
                break

    if flag:
        break

print('Нестабильное распределение' if flag else 'Стабильное распределение')

time2 = perf_counter()

print(f'Затраченное время : {time2-time1}')