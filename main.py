def citire_lista():
    """
    Returneaza o lista citita de la tastatura.

    """
    l = []
    lista = input('Scrieti o lista de numere separate prin virgula: ')
    lista_numere = lista.split(',')
    for x in lista_numere:
        l = l.append(int(x))

    return l


def concatenare_numere(l):
    """
    Returneaza numarul obtinut prin concatenarea tuturor numerelor pozitive din listă.

    """
    numar_concatenat = ''
    for nr in l:
        if nr == 0 and numar_concatenat == '':
            continue
        if nr >= 0:
            numar_concatenat += str(nr)

    return numar_concatenat


def test_concatenare_numere():
    assert concatenare_numere([0, 8, 9, 10, 0]) == 89100
    assert concatenare_numere([8, 9, 10, 0, -7, 5]) == 891005
    assert concatenare_numere([0, -4, 9, 10, 0]) == 910


def suma_max_min(l):
    """
    Returneaza suma celui mai mic si celui mai mare numar.

    """

    return max(l) + min(l)


def test_suma_max_min():
    assert suma_max_min([10, -7, 4, -2, 8]) == 3
    assert suma_max_min([0, 9, 1, 5]) == 9
    assert suma_max_min([10, -10, 4, -2, 8]) == 0


def suma_cifrelor_unui_numar(nr):
    """
    Returneaza suma cifrelor unui numar.

    """
    sum = 0
    for digit in str(nr):
        sum += int(digit)
    return sum


def suma_cifrelor(l, n):
    """
    Returneaza toate numerelor care au suma cifrelor mai mare sau
    egală decat un număr n citit de la tastatură.

    """
    lista = []
    for numar in l:
        if suma_cifrelor_unui_numar(numar) >= n:
            lista.append(numar)

    return lista


def test_suma_cifrelor():
    assert suma_cifrelor([25, 11, 10, 24, 39], 7) == [25, 39]
    assert suma_cifrelor([25, 11, 10, 24, 39], 0) == [25, 11, 10, 24, 39]
    assert suma_cifrelor([25, 11, 10, 24, 39], 10) == [39]


def meniu():
    test_concatenare_numere()
    test_suma_max_min()
    test_suma_cifrelor()
    #test_

    lista = []

    user_choice = """
    Alegeti:
    1. Citirea listei.
    2. Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.
    3. Să se afișeze suma dintre cel mai mare număr din listă și cel mai mic număr din listă.
    4. Afișarea tuturor numerelor care au suma cifrelor mai mare 
    sau egală decat un număr n citit de la tastatură.
    5. Afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite cu
    radicalul acestora. În cazul numerelor care nu sunt pătrat perfect, acestea sunt înlocuite cu o listă
    cu numerele pătrat perfect mai mici decât numărul inițial. Modificările se aplică doar pe numerele
    pozitive.
    6. Iesire
    """

    alegere = input(user_choice)

    while alegere != '6':
        if alegere == '1':
            lista = citire_lista()
        elif alegere == '2':
            concatenare_numere(lista)
        elif alegere == '3':
            suma_max_min(lista)
        elif alegere == '4':
            nr = int(input('Introduceti un numar: '))
            suma_cifrelor(lista, nr)
        elif alegere == '5':
            pass

        alegere = input(user_choice)


if __name__ == '__main__':
    meniu()