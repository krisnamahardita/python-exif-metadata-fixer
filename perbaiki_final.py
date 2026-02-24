import os
import re
import piexif
from datetime import datetime

# --- PASTE LOKASI FOLDER GOOGLE PHOTOS DI SINI ---
target_folder = r"C:\Perbaikan Foto 14 Februari 2026\Proses_Python\takeout-20260214T074117Z-3-001\Takeout\Google Photos"
# -------------------------------------------------

def perbaiki_sesuai_nama_file():
    print(f"--- MULAI MEMPROSES FOTO ---")
    print(f"Target: {target_folder}\n")
    
    # Ini adalah "Rumus" untuk mencari tahun-bulan-tanggal di nama file
    # (\d{4}) artinya cari 4 angka (Tahun)
    # (\d{2}) artinya cari 2 angka (Bulan)
    # (\d{2}) artinya cari 2 angka (Tanggal)
    pola_tanggal = re.compile(r'(\d{4})(\d{2})(\d{2})')
    
    jumlah_sukses = 0
    jumlah_dilewati = 0

    for root, dirs, files in os.walk(target_folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg')):
                
                # Cek apakah nama file mengandung angka tanggal?
                temukan = pola_tanggal.search(filename)
                
                if temukan:
                    # Ambil angka tahun, bulan, hari dari nama file
                    tahun, bulan, tanggal = temukan.groups()
                    
                    full_path = os.path.join(root, filename)
                    
                    # Format tanggal baru sesuai nama file tersebut
                    tanggal_baru = f"{tahun}:{bulan}:{tanggal} 12:00:00"
                    
                    try:
                        # Load data foto
                        try:
                            exif_dict = piexif.load(full_path)
                        except:
                            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}, "thumbnail": None}
                        
                        # Masukkan tanggal yang didapat dari nama file
                        b_tanggal = tanggal_baru.encode('utf-8')
                        exif_dict['0th'][piexif.ImageIFD.DateTime] = b_tanggal
                        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = b_tanggal
                        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = b_tanggal
                        
                        # Simpan
                        exif_bytes = piexif.dump(exif_dict)
                        piexif.insert(exif_bytes, full_path)
                        
                        # Print bukti ke layar
                        print(f"[OK] {filename} -> Diubah ke Tgl: {tanggal}-{bulan}-{tahun}")
                        jumlah_sukses += 1
                        
                    except Exception as e:
                        print(f"[ERROR] {filename}: {e}")
                else:
                    # Jika nama file tidak ada tanggalnya (misal: 'image.jpg'), biarkan saja
                    jumlah_dilewati += 1

    print(f"\n--- SELESAI ---")
    print(f"Total Foto Diperbaiki: {jumlah_sukses}")
    print(f"Total Foto Dilewati (Tanpa Tgl di Nama): {jumlah_dilewati}")
    input("Tekan Enter untuk keluar...")

if __name__ == "__main__":
    perbaiki_sesuai_nama_file()