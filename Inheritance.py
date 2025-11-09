 # inheritance (warisan)

# Parent class
class Person:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("Usia:", self.usia)

# Child class Dosen (mewarisi Person)
class Dosen(Person):
    def __init__(self, nama, usia, nidn, mata_kuliah):
        super().__init__(nama, usia)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def tampilkan_data(self):
        super().tampilkan_data()
        print("NIDN:", self.nidn)
        print("Mata Kuliah:", self.mata_kuliah)

    def mengajar(self):
        print(f"{self.nama} sedang mengajar {self.mata_kuliah}.")

# Child class Mahasiswa (mewarisi Person)
class Mahasiswa(Person):
    def __init__(self, nama, usia, nim, jurusan, universitas):
        super().__init__(nama, usia)
        self.nim = nim
        self.jurusan = jurusan
        self.universitas = universitas

    def tampilkan_data(self):
        super().tampilkan_data()
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan)

    def belajar(self):
        print(f"{self.nama} sedang belajar di jurusan PTI.")

# ==========================
# DATA OBJEK
# ==========================
dosen1 = Dosen("Edy", 17, "12345", "Pemrograman Berorientasi Objek")
mhs1 = Mahasiswa("Helmiati", 21, "24241120", "Pendidikan Teknologi Informasi", "Universitas Pendidikan Mandalika")

# ==========================
# OUTPUT
# ==========================
print("inheritance (warisan)\n")

print("=== Data Dosen ===")
dosen1.tampilkan_data()
dosen1.mengajar()

print("\n=== Data Mahasiswa ===")
mhs1.tampilkan_data()
mhs1.belajar()