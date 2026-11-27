rahasia=7
tebakan=int(input("masukan tebakan rahasia:"))
while tebakan != rahasia:
    print('tebakan salah')
    if tebakan <rahasia :
        print("tebakan terlalu kecil")
    else:
        print("tebakan terlalu besar")
    tebakan =int(input("masukan angka tebakan: "))
    print("angka tebakan benar")