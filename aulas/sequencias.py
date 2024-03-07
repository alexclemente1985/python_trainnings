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


def sequencias():
    lists()

if __name__ == '__main__':
    sequencias()