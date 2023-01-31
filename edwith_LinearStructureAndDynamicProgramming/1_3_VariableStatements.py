def main():
    numYearBase10 = 2019    #integer in decimal
    numYearBase8 = 0o3743   #integer in octal
    numYearBase16 = 0x7E3   #integer in hexadecimal

    print ("Year by base 10: %d, by base 8: %d, by base 16: %d"%(numYearBase10, numYearBase8, numYearBase16))

    numComplex1 = complex(3,4)
    numComplex2 = 4+3j #'j' meaning imaginary number

    print ("Complex value:", numComplex1)
    print ("Absoulute value:", abs(numComplex2))
    print ("Real value:", numComplex2.real)
    print ("Image value:", numComplex2.imag)

    strDeptame = "Department of~"
    strUnivName = "KAIST"
    print ("Department:", strDeptame)
    print ("Full name of dept.:", (strDeptame+", "+strUnivName))

main()