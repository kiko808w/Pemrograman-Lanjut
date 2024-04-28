def main():
    print("Program Menghitung Nilai Akhir Mahasiswa")
    print("=======================================")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    # Hitung nilai akhir
    nilai_akhir = hitung_nilai(tugas, uts, uas)
    
    # Tentukan nilai huruf
    nilai_huruf = tentukan_huruf(nilai_akhir)
    
    # Tampilkan hasil
    print(f"Nilai Akhir: {nilai_akhir:.2f}")
    print(f"Nilai Huruf: {nilai_huruf}")

def hitung_nilai(tugas, uts, uas):
    # Menghitung nilai akhir berdasarkan bobot
    nilai = (0.25 * tugas) + (0.35 * uts) + (0.40 * uas)
    return nilai

def tentukan_huruf(nilai):
    # Menentukan nilai huruf berdasarkan kriteria
    if nilai > 85:
        return "A"
    elif nilai > 80:
        return "A-"
    elif nilai > 75:
        return "B+"
    elif nilai > 70:
        return "B"
    elif nilai > 65:
        return "B-"
    elif nilai > 60:
        return "C+"
    elif nilai > 55:
        return "C"
    elif nilai > 50:
        return "C-"
    elif nilai > 30:
        return "D"
    else:
        return "E"

if __name__ == "__main__":
    main()
