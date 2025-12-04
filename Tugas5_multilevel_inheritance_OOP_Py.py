# multi level inheritance
class jenisKelamin:
    def jenis(self):
        print("Jenis Kelamin : Perempuan")

class statusHidup:
    def status(self):
        print("Status mahasiswa : Masih hidup")

class mhs_Alumni(statusHidup):
    def lulus(self):
        print("Mahasiswa lulus tahun 2025")

class mhs_Aktif(jenisKelamin):
    def Masuk(self):
        print("Mahasiswa dengan NIM : 24241120")

# class child
class KTM(mhs_Aktif):
    def identitas(self):
        print("Nama : Helmiati")
        print("Universitas : Undikma")
        print("Program Studi : Pendidikan Teknologi Informasi")

class Ijazah(mhs_Alumni):
    pass

class Beasiswa(mhs_Alumni, mhs_Aktif):
    pass


# Object / instance
ktm = KTM()
ijazah = Ijazah()
beasiswa = Beasiswa()

# Output (Run)
ktm.identitas()
ktm.Masuk()
ktm.jenis()

ijazah.status()