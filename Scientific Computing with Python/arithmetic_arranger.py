def arithmetic_arranger(problems, option = False):
    data = []
    sol = []

    # Primera condición
    if len(problems) > 5:
        return("Error: Too many problems.")

    for operation in problems:
        # Segunda condición
        operator_index = operation.find(' ') + 1
        if not (operation[operator_index] == '+' or operation[operator_index] == '-'):
            return("Error: Operator must be '+' or '-'.")   
        # Tercera condición
        if not(operation[:operator_index-1].isnumeric() and operation[operator_index+2:].isnumeric()):
            return("Error: Numbers must only contain digits.")   
        # Cuarta condición
        if not(len(operation[:operator_index-1]) < 5 and len(operation[operator_index+2:]) < 5):
            return("Error: Numbers cannot be more than four digits.")

        data.append([operation[:operator_index-1],
                     operation[operator_index],
                     operation[operator_index+2:],
                 str(int(operation[:operator_index-1]) + int(operation[operator_index+2:]) if operation[operator_index] == "+" 
                else int(operation[:operator_index-1]) - int(operation[operator_index+2:]))])
        
    # Mostrar operación sin solución
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    for i in range(len(problems)):    
        long_total = max(len(data[i][0]), len(data[i][2])) + 2
        
        sol.append([long_total,
                    (long_total - len(data[i][0])) * ' ' + data[i][0],
                    data[i][1]  + (long_total - len(data[i][2]) - 1) * ' ' + data[i][2],
                    long_total * '-',
                    (long_total - len(data[i][3])) * ' ' + data[i][3]])

        first_line += sol[i][1] + 4 * ' '   
        second_line +=  sol[i][2] + 4 * ' '
        third_line += sol[i][3] + 4 * ' '
        fourth_line += sol[i][4] + 4 * ' '

    arranged_problems = first_line[:-4] + '\n' + second_line[:-4] + '\n' + third_line[:-4]

    # Mostrar solución si especificado
    if option == True:
        arranged_problems += '\n' + fourth_line[:-4]
           
    return arranged_problems