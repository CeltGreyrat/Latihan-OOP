from data.mahasiswa import Mahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

if __name__ == '__main__':
    data = DataMahasigma()
 while True:
        print("\n=====Menu Daftar Mahasiswa=====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")  
        print("5. Keluar")
        
        try :
             pilihan = int(input("Masukan PIlihan (1-5): "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            nama = input("Masukkan nama mahasiswa: ")
            nim = int(input("Masukkan nim mahasiswa: "))
            try:
             prodi = (input("Masukkan prodi mahasiswa: "))
             data.tambah(nama, nim, prodi)
            except ValueError:
                print("Nilai harus berupa angka!")
                
        elif pilihan == 2:
            data.tampilkan()
            
        elif pilihan == 3:
            Nama = input("Masukan Nama Yang Ingin Di Hapus: ")
            data.hapus(Nama)

        elif pilihan == 4:
            Nama = input("Masukan Nama Mahasiswa Yang Ingin Di Ubah Prodi-nya: ")
            try:
                prodi = input("Masukan prodi Baru: ")
                data.ubah(Nama, prodi)
            except ValueError:
                print("Prodi Tidak Ada")
                
        elif pilihan == 5:
            print("Program telas Selesai, Terima Kasih")
            break 
        
        else:
            print("Pilihan Tidak Valid, Silakan Pilih Menu (1-5).")
