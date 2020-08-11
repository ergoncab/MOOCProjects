class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        #if self.ledger['amount'] > amount:
        if self.check_funds(amount) == True:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for list in self.ledger:
            balance += list['amount']
        return balance

    def transfer(self, amount, other):
        #if self.amount >= amount:
        if self.check_funds(amount) == True:
            self.withdraw(amount, 'Transfer to ' + other.name)   
            other.deposit(amount, 'Transfer from ' + self.name) 
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else: 
            return False

    def __str__(self):
        if len(self.name) % 2 == 0:
            half = len(self.name) / 2
            n_ast = int(15 - half)
            str_final = n_ast * '*' + self.name + n_ast * '*' + '\n' 
        else:
            half = (len(self.name) - 1)/ 2
            n_ast = int(14 - half)
            str_final = n_ast * '*' + self.name + (n_ast + 1) * '*' + '\n'

        for record in self.ledger:
            desc_len = len(record['description']) 
            n_spaces = (23 - desc_len) if desc_len < 24 else 0 
            int_len = len(str(record['amount'] // 1))
            num = "{:.2f}".format(round(record['amount'], 2))

            n_spaces += (7 - len(num)) 

            str_final += record['description'][0:23] + n_spaces * ' ' + num + '\n'

        str_final += 'Total: ' + str(self.get_balance())   
        return str_final
         

def create_spend_chart(categories):
    spent = []
    temp_spent = 0
    for categ in categories:
        for register in categ.ledger:
            if register['amount'] < 0:
                temp_spent += abs(register['amount']) 
        spent.append(temp_spent)
        temp_spent = 0

    total_spent = sum(spent)

    percent = []
    for index in range(len(categories)):
        percent.append(round(spent[index] * 100 / total_spent, -1))
    
    circles = []

    iter = 0
    for value in percent:
        blanks = (100 - value) / 10
        blanks += (1 if iter == 0 else 0)
        iter += 1

        circles.append(int(blanks) * ' ' + (11 - int(blanks)) * 'o')

    cat_len = len(categories)
    score = cat_len * 3 + 1
    line = 4 * ' ' + score * '-' + '\n'
    
    string = 'Percentage spent by category\n'
    level = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
    for i in range(11):
        string +=  level[i] + ' '
        for k in range(len(categories)):
            string += circles[k][i] + 2 * ' ' + ('\n' if k == len(categories) - 1 else '')            
      
    string += line
    
    max_len = 0
    for cat in categories:
        if len(cat.name) > max_len:
            max_len = len(cat.name)  

    names = []
    for cat in categories:
        names.append(cat.name + (max_len - len(cat.name)) * ' ')

    for j in range(max_len):
        string += 5 * ' ' 
        for l in range(len(names)):
            string += names[l][j] + 2 * ' ' + ('\n' if l == len(names) - 1 else '')

    string = string[:-1]
    return string