# ==========================================
# Aplikasi Class Variable dan Instance Variable
# Contoh: Data Motor Helmiati
# ==========================================

class Motor:
    # === Class Variable ===
    # Berlaku untuk semua objek dari kelas Motor
    jenis_kendaraan = "Motor"

    def __init__(self, nama_pemilik, merk, warna, cc, surat, mesin, tahun):
        # === Instance Variable ===
        # Berlaku hanya untuk objek yang dibuat
        self.nama_pemilik = nama_pemilik
        self.merk = merk
        self.warna = warna
        self.cc = cc
        self.surat = surat
        self.mesin = mesin
        self.tahun = tahun

    def tampil_info(self):
        # Menampilkan semua data motor (aplikasi class & instance variable)
        print("=== DATA MOTOR ===")
        print(f"Jenis Kendaraan : {Motor.jenis_kendaraan}")   # Class variable
        print(f"Nama Pemilik    : {self.nama_pemilik}")       # Instance variable
        print(f"Merek           : {self.merk}")
        print(f"Warna           : {self.warna}")
        print(f"CC              : {self.cc}")
        print(f"Mesin           : {self.mesin}")
        print(f"Surat           : {self.surat}")
        print(f"Tahun           : {self.tahun}")

    def kondisi(self):
        # Aplikasi instance variable (tahun) untuk menentukan kondisi motor
        umur = 2025 - self.tahun
        if umur <= 1:
            return "Masih baru banget, siap diajak nongkrong 😎"
        elif umur <= 3:
            return "Masih bagus, tapi udah waktunya servis rutin."
        else:
            return "Udah agak tua, tapi masih bisa diandalkan."

    @classmethod
    def ubah_jenis_kendaraan(cls, jenis_baru):
        # Aplikasi class variable dengan @classmethod
        cls.jenis_kendaraan = jenis_baru


# === Contoh Penggunaan ===
if __name__ == "__main__":
    # Membuat objek motor Helmiati
    motor_helmiati = Motor(
        nama_pemilik="Helmiati",
        merk="Honda Beat",
        warna="Hitam Doff",
        cc=110,
        surat="Lengkap",
        mesin="4 Langkah SOHC eSP",
        tahun=2024
    )

    # Menampilkan semua data motor (instance & class variable)
    motor_helmiati.tampil_info()
    print("Kondisi         :", motor_helmiati.kondisi())
    print()

    # Mengubah class variable menggunakan method khusus
    Motor.ubah_jenis_kendaraan("Sepeda Motor")
    print("=== Setelah Class Variable Diubah ===")
    motor_helmiati.tampil_info()
    print("Kondisi         :", motor_helmiati.kondisi())