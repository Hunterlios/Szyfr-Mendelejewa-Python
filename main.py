from os import walk
filenames = next(walk('input'), (None, None, []))[2]


def encrypt(text):
    elements = {
        "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
        "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,
        "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30,
        "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40,
        "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50,
        "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60,
        "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70,
        "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80,
        "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90,
        "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100,
        "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109,
        "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118,
    }

    for i in text:
        if not i.isalpha():
            text = text.replace(i, '')
    words = text.split()
    result = []

    for word in words:
        code = []
        i = 0
        while i < len(word):
            if word[i].upper() in elements:
                code.append(str(elements[word[i].upper()]))
                i += 1
            else:
                if i < len(word) - 1:
                    symbol = word[i:i + 2]
                    if symbol.capitalize() in elements:
                        code.append(str(elements[symbol.capitalize()]))
                        i += 2
                    else:
                        return "Error: '" + word[i:i+2].capitalize() + "' nie jest pierwiastkiem."
                else:
                    return "Error: '" + word[i] + "' nie jest symbolem pierwiastka."
        code = '*'.join(code)
        result.append(code)

    result = '**'.join(result)

    return result


def load_data(filename):
    with open(f'input/{filename}', 'r') as file:
        data = file.read()
    return data


def save_data(data):
    with open(f'output/{filename}', 'w') as file:
        file.write(data)


for filename in filenames:
    data = load_data(filename)
    data = encrypt(data)
    save_data(data)

