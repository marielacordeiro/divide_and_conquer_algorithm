# PUCRS
# Projeto e Otimizacao de Algoritmos
# Prof Joao Batista
# O karatsuba mortal triplo carpado
# @author Mariela Pontes Cordeiro

import sys

def zeroPad(numberString, zeros, left=True):
    # retorna a string com x zeros na esquerda ou direita
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString

def sum(str1, str2):
    if (len(str1) > len(str2)):
        t = str1
        str1 = str2
        str2 = t

    str = ""
 
    len1 = len(str1)
    len2 = len(str2)

    # inverte as strings
    str1 = str1[::-1]
    str2 = str2[::-1]
 
    carry = 0
    # multiplica usando ASCII
    for i in range(len1):
        sum = ((ord(str1[i]) - 48) +
              ((ord(str2[i]) - 48) + carry))
        str += chr(sum % 10 + 48)
 
        carry = int(sum / 10)
 
    # soma os digitos que faltam do numero maior
    for i in range(len1, len2):
        sum = ((ord(str2[i]) - 48) + carry)
        str += chr(sum % 10 + 48)
        carry = (int)(sum / 10)
 
    if (carry):
        str += chr(carry + 48)
 
    # inverte o resultado 
    str = str[::-1]
 
    return str

def karatsubaMultiplication(x, y):
    x = str(x)
    y = str(y)

    # parada da recursao
    if len(x) == 1 and len(y) == 1:
        return str(int(x) * int(y))

    # balanceia x e y
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))

    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))

    if len(x) == 2:
        x = zeroPad(x, 1)
        y = zeroPad(y, 1)

    # shifts e divisao das strings
    n = len(x)
    remaining_sections = n // 3

    if (n % 2) != 0 or (n % 3) != 0:
        first_section = remaining_sections + n % 3
    else:
        first_section = remaining_sections

    BZeroPadding = remaining_sections
    AZeroPadding = remaining_sections * 2

    splitsX = []
    splitsY = []
    splitsX.append(x[:first_section])
    splitsY.append(y[:first_section])
    curr = first_section
    while curr < len(x):
        splitsX.append(x[curr:curr+remaining_sections])
        splitsY.append(y[curr:curr+remaining_sections])
        curr += remaining_sections

    a = splitsX[0]
    b = splitsX[1]
    c = splitsX[2]
    d = splitsY[0]
    e = splitsY[1]
    f = splitsY[2]

    # calcula recursivamente
    ad = karatsubaMultiplication(a, d)
    ae = karatsubaMultiplication(a, e)
    af = karatsubaMultiplication(a, f)
    bd = karatsubaMultiplication(b, d)
    be = karatsubaMultiplication(b, e)
    bf = karatsubaMultiplication(b, f)
    cd = karatsubaMultiplication(c, d)
    ce = karatsubaMultiplication(c, e)
    cf = karatsubaMultiplication(c, f)
    AD = zeroPad(ad, AZeroPadding * 2, False)
    AE = zeroPad(ae, AZeroPadding + BZeroPadding, False)
    AF = zeroPad(af, AZeroPadding, False)
    BD = zeroPad(bd, AZeroPadding + BZeroPadding, False)
    BE = zeroPad(be, BZeroPadding + BZeroPadding, False)
    BF = zeroPad(bf, BZeroPadding, False)
    CD = zeroPad(cd, AZeroPadding, False)
    CE = zeroPad(ce, BZeroPadding, False)
    return sum(AD, sum(sum(AE, BD), sum(sum(AF, CD), sum(BE, sum(sum(CE, BF), cf)))))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Por favor insira os dois valores a serem multiplicados precedidos pelo nome do arquivo python.")
        sys.exit()
    else:
        x = sys.argv[1]
        y = sys.argv[2]

    # caso o numero seja negativo
    xIsNeg = False
    yIsNeg = False
    if x.startswith("-"):
        x = x[len("-"):]
        xIsNeg = True
    if y.startswith("-"):
        y = y[len("-"):]
        yIsNeg = True

    if x.isdigit() and y.isdigit():
        result = karatsubaMultiplication(x.strip(), y.strip())
        if (xIsNeg and not yIsNeg) or (yIsNeg and not xIsNeg):
            if len(result) > 1:
                print("-" + result.lstrip("0"))
            else:
                print(result)
        else:
            if len(result) > 1:
                print(result.lstrip("0"))
            else:
                print(result)
    else: 
        print("Apenas valores numericos podem ser multiplicados.")