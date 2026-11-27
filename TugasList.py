# Buatlah 2 set untuk menampung pembeli8an bedasarkan hari pertama dan pembelian hari kedua
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam" , "gula", "coklat", "kecap"}
print("Set awal dibuat")
print("Hari pertama: ", hari_pertama)
print("Hari kedua: ", hari_kedua)

# Tambahkan "keju" pada hari kedua
hari_kedua.add("keju")
print("Tambahkan keju pada hari kedua: ", hari_kedua)

# Cari barang yang sama pada pembelian hari pertama dan pembelian hari kedua
barang_sama = hari_pertama.intersection(hari_kedua)
print("Barang yang sama: ", barang_sama)

# Dibeli dihari pertama tapi tidak dihari kedua
hari_pertama_bukan_hari_kedua = hari_pertama.difference(hari_kedua)
print("Dibeli dihari pertama tapi tidak dihari kedua: ", hari_pertama_bukan_hari_kedua)

# Hapus garam pada hari pertama
hari_pertama.remove("garam")
print("Hari pertama setelah garam dihapus: ", hari_pertama)

# Dibeli dihari kedua tapi tidak dihari pertama
hari_kedua_bukan_hari_pertama = hari_kedua.difference(hari_pertama)
print("Dibeli dihari kedua tapi tidak dihari pertama: ", hari_kedua_bukan_hari_pertama)
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}

# Barang yang berbeda
barang_berbeda = hari_pertama.symmetric_difference(hari_kedua)
print("Barang yang berbeda: ", barang_berbeda)

# Tampilan semua keperluan rumah tangga yang dibeli pada hari pertama
print("Hari pertama: ", hari_pertama)

# Tampilan semua keperluan rumah tangga yang dibeli pada hari kedua
print("Hari kedua: ", hari_kedua)
