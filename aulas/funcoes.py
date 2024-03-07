def native_functions():
    print(f'type(10): {type(10)}')
    print(f'int(10.7): {int(10.7)}')
    print(f'float(10): {float(10)}')
    print(f'str(10): {str(10)}')
    print(f'max(10, 20, 30): {max(10, 20, 30)}')
    print(f'min(10, 20, 30): {min(10, 20, 30)}')
    print(f'abs(-10): {abs(-10)}')
    print(f'sum(10, 20, 30): {sum([10, 20, 30])}')
    print(f'round(10.3555, 2): {round(10.3555, 2)}')
    print(f'pow(2, 10): {pow(2, 10)}')
    print(f'len("mathematics"): {len("mathematics")}')

def subtract_bc(a,b,c):
    result = a - b*c
    return result

def add_10(m):
    if m >= 100:
        m = m + 10
        return m
    else:
        return "Save more!"

def wage(hours):
    return hours * 25

def with_bonus(hours):
    return wage(hours) + 50

def plus_ten(a):
    return a + 10
def funcoes():
    print("My first function")
    print(plus_ten(20))

    print(wage(8), with_bonus(8))

    print(add_10(37))
    print(add_10(137))

    print(subtract_bc(20,34,2))
    native_functions()

if __name__ == '__main__':
    funcoes()