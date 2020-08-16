def add_time(start, duration, starting_day = ''):

    space_index = start.find(' ')
    start_int = start[0:space_index]
    formato_ini = start[space_index + 1:]

    hora_ini = start_int[:start_int.find(':')]
    min_ini = start_int[start_int.find(':') + 1:]

    hora_add = duration[:duration.find(':')]
    min_add = duration[duration.find(':') + 1:]

    suma_min = int(min_ini) + int(min_add)
    sol_min = '0' + str(suma_min % 60) if suma_min % 60 < 10  else str(suma_min % 60)
    suma_hora = str(int(hora_ini) + int(hora_add) + (1 if suma_min > 60 else 0))

    vueltas = int(suma_hora) // 12 
    sol_hora = str(int(suma_hora) % 12)

    if vueltas % 2 == 0:
        sol_formato = formato_ini
    else:
        sol_formato = 'PM' if 'AM' == formato_ini else 'AM'

    new_time = ('12' if sol_hora == '0' else sol_hora) + ':' + sol_min + ' ' + sol_formato

    # Print week day
    week = {"monday": "0", "tuesday": "1", "wednesday": "2", "thursday": "3", "friday": "4", "saturday": "5", "sunday": "6"}
    week_rev = {"0": "monday", "1": "tuesday", "2": "wednesday", "3": "thursday", "4": "friday", "5": "saturday", "6": "sunday"}
    extra_days = 0
    sol_day = ''

    
    if formato_ini == sol_formato:
        if vueltas > 0:
            extra_days = vueltas // 2 

    elif formato_ini == 'PM' and sol_formato == 'AM':
        extra_days = 1 + (vueltas -1) // 2 
           
    elif formato_ini == 'AM' and sol_formato == 'PM':
        extra_days = vueltas // 2 


    if starting_day != '':
        if vueltas == 0:
            sol_day = starting_day.lower()
        else:
            day_index = int(week[starting_day.lower()])
            sol_day = week_rev[str((extra_days + day_index) % 7)]
        
        new_time += ', ' + sol_day.capitalize()        


    # Print n days
    if extra_days == 1:
        new_time += ' (next day)'
    elif extra_days > 1:
        new_time += ' (' + str(extra_days) + ' days later)'

    return new_time