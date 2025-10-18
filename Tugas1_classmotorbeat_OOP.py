class Motor:
    def __init__(self, merk, warna, cc, surat, mesin, tahun):
        # inisialisasi atribut motor
        self.merk = merk
        self.warna = warna
        self.cc = cc
        self.surat = surat
        self.mesin = mesin
        self.tahun = tahun

    def tampil_info(self):
        # menampilkan informasi motor
        print("=== Data Motor ===")
        print("Merek       :", self.merk)
        print("Warna       :", self.warna)
        print("CC          :", self.cc)
        print("Mesin       :", self.mesin)
        print("Surat       :", self.surat)
        print("Tahun       :", self.tahun)

    def kondisi(self):
        # menentukan kondisi berdasarkan tahun motor
        umur = 2025 - self.tahun
        if umur <= 1:
            return "Masih baru banget, siap diajak nongkrong 😎"
        elif umur <= 3:
            return "Masih bagus, tapi udah waktunya servis rutin."
        else:
            return "Udah agak tua, tapi masih bisa diandalkan."

# contoh penggunaan
if __name__ == "__main__":
    motor_beat = Motor(
        merk = "Honda",
        warna = "Matte Black / Hitam Doff",
        cc = 109.5,
        surat = "Lengkap",
        mesin = "4 Langkah SOHC eSP",
        tahun = 2024
    )

    motor_beat.tampil_info()
    print("Kondisi     :", motor_beat.kondisi())