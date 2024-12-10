class DataMahasigma : 
    def __init__(self):
        self.DataMahasigma = []
    
    def tambah(self, nama, nim, prodi,): 
        self.DataMahasigma.append({"nama" : nama, "nim": nim, "prodi": prodi})
        print(f'data {nama} berhasil di tambahkan')
        
    def tampilkan (self):
        if not self.DataMahasigma:
            print("Data Tidak Di Temukan")
        else:
            print("Daftar Nilai Mahasiswa")
            for i, mahasiswa in enumerate(self.DataMahasigma, start= 1) :
                print(f"{i}. Nama: {mahasiswa['nama']}\n nim: {mahasiswa['nim']}\n  prodi: {mahasiswa['prodi']}")
                
    def hapus (self, nama):
        for mahasiswa in self.DataMahasigma:
            if mahasiswa ['nama'] == nama:
                self.DataMahasigma.remove(mahasiswa)
                print(f"Data {nama} Mahaiswa Berhasil Di Hapus")
                return
        print("Data Tidak Di Temukan")
    
    def ubah (self, nama, nim, prodi):
        for mahasiswa in self.DataMahasigma:
            if mahasiswa ["nama"] == nama:
                mahasiswa ["nim"] == nim
                mahasiswa ["prodi"] = prodi
                print(f"Data {nama} Berhasil Di Ubah")
                return
            print("Data Tidak Di Temukan")
