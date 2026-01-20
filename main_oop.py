# FILE: main_oop.py
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def info(self):
        return f"Nama: {self.nama} | NIM: {self.nim} | Jurusan: {self.jurusan}"

data_mahasiswa = []

def tambah_data():
    print("\n--- Input Data ---")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan Jurusan: ")
    data_mahasiswa.append(Mahasiswa(nama, nim, jurusan))
    print(">> Data tersimpan!")

def lihat_data():
    print("\n--- Data Mahasiswa ---")
    if not data_mahasiswa:
        print(">> Data kosong.")
    else:
        for mhs in data_mahasiswa:
            print(mhs.info())

def main():
    while True:
        print("\n1. Tambah  2. Lihat  3. Keluar")
        pilihan = input("Pilih: ")
        if pilihan == '1': tambah_data()
        elif pilihan == '2': lihat_data()
        elif pilihan == '3': break

if __name__ == "__main__":
    main()
	  