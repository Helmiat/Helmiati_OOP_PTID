# multiple inheritance = mendapatka warisan lebih dari satu parent

# multilevel inheritance = mendapat warisan dari paren yg mendapat warisan juga



# Parent Class
class Identitas:
    def __init__(self, nama, nim, ktp, kk):
        self.nama = nama
        self.nim = nim
        self.ktp = ktp
        self.kk = kk

    def tampil_identitas(self):
        print("=== DATA IDENTITAS ===")
        print("Nama        :", self.nama)
        print("NIM         :", self.nim)
        print("No KTP      :", self.ktp)
        print("No KK       :", self.kk)


class Akademik:
    def __init__(self, tahun_masuk, tahun_lulus, ipk):
        self.tahun_masuk = tahun_masuk
        self.tahun_lulus = tahun_lulus
        self.ipk = ipk

    def tampil_akademik(self):
        print("=== DATA AKADEMIK ===")
        print("Tahun Masuk :", self.tahun_masuk)
        print("Tahun Lulus :", self.tahun_lulus)
        print("IPK         :", self.ipk)


class Beasiswa:
    def __init__(self, jenis_beasiswa):
        self.jenis_beasiswa = jenis_beasiswa

    def tampil_beasiswa(self):
        print("=== DATA BEASISWA ===")
        print("Jenis Beasiswa :", self.jenis_beasiswa)


class Kampus:
    def __init__(self, jurusan, universitas):
        self.jurusan = jurusan
        self.universitas = universitas

    def tampil_kampus(self):
        print("=== DATA KAMPUS ===")
        print("Jurusan     :", self.jurusan)
        print("Universitas :", self.universitas)


# Child class menggunakan multiple inheritance
class Mahasiswa(Identitas, Akademik, Beasiswa, Kampus):
    def __init__(self, nama, nim, ktp, kk, tahun_masuk, tahun_lulus, ipk,
                 jenis_beasiswa, ijazah, jurusan, universitas):

        Identitas.__init__(self, nama, nim, ktp, kk)
        Akademik.__init__(self, tahun_masuk, tahun_lulus, ipk)
        Beasiswa.__init__(self, jenis_beasiswa)
        Kampus.__init__(self, jurusan, universitas)

        self.ijazah = ijazah

    def tampil_data(self):
        print("\n===== DATA PENDAFTARAN MAHASISWA =====")
        self.tampil_identitas()
        self.tampil_kampus()
        self.tampil_akademik()
        self.tampil_beasiswa()
        print("Ijazah      :", self.ijazah)
        print("========================================")


# Membuat objek mahasiswa dengan data lengkap
mhs = Mahasiswa(
    nama="Helmiati",
    nim="24241120",
    ktp="5201xxxxxxxxxxx",
    kk="5201xxxxxxxxxxx",
    tahun_masuk=2024,
    tahun_lulus=2025,
    ipk=3.75,
    jenis_beasiswa="Beasiswa KIP Kuliah",
    ijazah="Ada",
    jurusan="Pendidikan Teknologi Informasi",
    universitas="Universitas Pendidikan Mandalika (UNDikMA)"
)

# Menampilkan hasil
mhs.tampil_data()