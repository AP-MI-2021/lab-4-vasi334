def citire_lista():
    """
    Returneaza o lista citita de la tastatura.

    """
    l = []
    lista = input('Scrieti o lista de numere separate prin virgula: ')
    lista_numere = lista.split(',')
    for x in lista_numere:
        l.append(int(x))

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

    return int(numar_concatenat)


def test_concatenare_numere():
    assert concatenare_numere([0, 8, 9, 10, 0]) == 89100
    assert concatenare_numere([8, 9, 10, 0, -7, 5]) == 891005
    assert concatenare_numere([0, -4, 9, 10, 0]) == 9100


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
    suma = 0
    for digit in str(nr):
        suma += int(digit)
    return suma


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


def verif_numar_patrat_perfect(num):
    i = 1
    while (i * i <= num):
        if ((num % i == 0) and (num / i == i)):
            return True
        i = i + 1

    return False


def patrat_perfect(num):
    i = 1
    while (i * i <= num):
        if ((num % i == 0) and (num / i == i)):
            return i
        i = i + 1


def patrate_perfecte_mai_mici(nr):
    lista = []
    for i in range(1, nr):
        if verif_numar_patrat_perfect(i):
            lista.append(i)

    return lista


def lista_patrat_perfect(l):
    """Returneaza lista obținuta din lista inițială în care numerele pătrat perfect sunt înlocuite cu radicalul
    acestora. Altfel sunt inlocuite cu o lista cu divizorii sai.
    """

    noua_lista = []

    for num in l:
        if verif_numar_patrat_perfect(num):
            noua_lista.append(patrat_perfect(num))
        elif num > 0:
            noua_lista.append(patrate_perfecte_mai_mici(num))
        else:
            noua_lista.append(num)

    return noua_lista


def test_lista_patrat_perfect():
    assert lista_patrat_perfect([25, 13, 26, 9, -4, 0]) == [5, [1, 4, 9], [1, 4, 9, 16, 25], 3, -4, 0]
    assert lista_patrat_perfect([25, 16, 26, 9, 2, 0]) == [5, 4, [1, 4, 9, 16, 25], 3, [1], 0]
    assert lista_patrat_perfect([25, 13, 26, 36, -4, 9]) == [5, [1, 4, 9], [1, 4, 9, 16, 25], 6, -4, 3]


def meniu():
    test_concatenare_numere()
    test_suma_max_min()
    test_suma_cifrelor()
    test_lista_patrat_perfect()

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
            print(concatenare_numere(lista))
        elif alegere == '3':
            print(suma_max_min(lista))
        elif alegere == '4':
            nr = int(input('Introduceti un numar: '))
            print(suma_cifrelor(lista, nr))
        elif alegere == '5':
            print(lista_patrat_perfect(lista))

        alegere = input(user_choice)


if __name__ == '__main__':
    meniu()
