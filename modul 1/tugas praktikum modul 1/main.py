
class PersegiPanjang:

    # class variabel
    jumlah = 0  # menghitung jumlah objek yang dibuat

    def __init__(self, panjang, lebar):
        # instance variabel
        self.panjang = panjang
        self.lebar = lebar
        PersegiPanjang.jumlah += 1

    # method untuk menghitung luas
    def hitung_luas(self):
        return self.panjang * self.lebar

    # method untuk menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    # method untuk menampilkan info objek
    def info(self):
        return f"Persegi Panjang dengan panjang {self.panjang} dan lebar {self.lebar}"


# Membuat beberapa objek persegi panjang
pp1 = PersegiPanjang(10, 5)
pp2 = PersegiPanjang(8, 3)

# Menampilkan hasil per objek
print(pp1.info())
print(f"Luas = {pp1.hitung_luas()}")
print(f"Keliling = {pp1.hitung_keliling()}\n")

print(pp2.info())
print(f"Luas = {pp2.hitung_luas()}")
print(f"Keliling = {pp2.hitung_keliling()}\n")

# Menampilkan jumlah total objek
print(f"Jumlah objek Persegi Panjang = {PersegiPanjang.jumlah}")