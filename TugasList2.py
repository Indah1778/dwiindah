# a. Membuat list awal sesuai urutan tempat duduk
penumpang = ["Wiliam", "Kate", "Anderson", "James", "Mandy"]
print("a. List awal:" , penumpang)

# b. Menambahakan "Jones" di posisi terakhir
penumpang.append("Jones")
print("b. Setelah Jones bergabung:" , penumpang)

# c. Mengubah data "Anderson" menjadi "Grace"
penumpang[2] = "Grace"
print("c. Setelah Anderon diganti Grace:" , penumpang)

# d. Mengecek keberadaan "Thompson" menggunakan operator membership (in)
ada_thompson = "Thompson" in penumpang
print("d. Apakah ada penumpang bernama Thompson:" , ada_thompson)

# e. Mengurutkan list sesuai abjad nama orang (A-Z)
penumpang.sort()
print("e. Mengurutkan nama sesuai abjad:" , penumpang)

# f. Menampilkan seluruh nama penumapang menggunakan perulangan (for)
print("f. Daftar penumpang yang samapai di Yogyakarta:")
for nama in penumpang:
    print(" -", nama)

# g. Mengosongkan list secara keseluruhan
penumpang.clear()
print("g. List setelah kososng:" , penumpang)

