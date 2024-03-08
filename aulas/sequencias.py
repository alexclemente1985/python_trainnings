def square_info(x):
    A = x ** 2
    P = 4 * x
    print(f"Area and Perimeter: {A,P}")

def lists():
    participants = ['John', 'Leila', 'Gregory', 'Cate']
    print(f'type(participants): {type(participants)}')
    print(f'participants[1]: {participants[1]}')
    print(f'participants[-1]: {participants[-1]}')
    print(f'participants[-2]: {participants[-2]}')

    participants[3] = "Maria"
    print(f'participants (após troca de Cate por Maria): ', participants)

    del participants[2]
    print(f'participants (após saída de Gregory): ', participants)

    participants.append("Dwayne")
    print(f'participants (após entrada de Dwayne): ', participants)

    participants.extend(['George', 'Catherine'])
    print(f'participants (após entrada de George e Catherine): ', participants)

    print(f'tamanho da lista: {len(participants)}')

    #slicing

    participants_sl_1_2 = participants[1:3]
    participants_sl_0_2 = participants[:2]
    participants_sl_4_last = participants[4:]
    participants_sl_minus_2_last = participants[-2:]

    print(participants_sl_1_2)
    print(participants_sl_0_2)
    print(participants_sl_4_last)
    print(participants_sl_minus_2_last)

    #index
    print(f'posição de Maria: {participants.index("Maria")}')

    #concatenação
    newcomers = ['Joshua', 'Brittany']

    bigger_list = [participants, newcomers]
    print(f'Bigger List: {bigger_list}')

    #ordenação
    print(f'participants antes do sort: {participants}')

    participants.sort()
    print(f'participants após sort: {participants}')

    participants.sort(reverse=True)
    print(f'participants após sort reverse: {participants}')

    #Tuplas
    x = (40,41,42)
    y = 50,51,52

    a,b,c = 1,2,3

    print(f'Tuplas: {x} e {y}')

    print(f"x[0] = {x[0]}")

    List = [x,y]

    print(f"Lista: {List}")

    #Tuplas: úteis com diferentes valores separados por vírgulas

    (age, year_of_school) = "30,17".split(",")
    print(f"age: {age}, year: {year_of_school}")

    square_info(3)

    #Dicionários (par chave:valor)

    dict = {'k1': 'cat', 'k2': 'dog', 'k3': 'mouse', 'k4': 'fish'}

    print(f"dicionário: {dict}")
    print(f"dict[k1]: {dict['k1']}")

    dict['k5'] = 'parrot'
    print(f"dicionário com adição da chave 'k5': {dict}")

    dict['k2'] = 'squirrel'
    print(f"dicionário alterado na chave 'k2': {dict}")

    dep_workers = {'dep1': 'Peter', 'dep2': ['Jennifer', 'Michael', 'Tommy']}

    print(f"dep_workers['dep2']: {dep_workers['dep2']}")

    team = {}
    team['Point Guard'] = 'Dirk'
    team['Shooting Guard'] = 'Al'
    team['Small Forward'] = 'Sean'
    team['Power Forward'] = 'Alexander'
    team['Center'] = 'Hector'

    print(f'team: {team}')
    print(f"team['Center']: {team['Center']}")

    #Verifica se a chave existe no dicionário
    print(f"team.get('Coach'): {team.get('Coach')}")
    print(f"team.get('Power Forward'): {team.get('Power Forward')}")


def sequencias():
    lists()

if __name__ == '__main__':
    sequencias()