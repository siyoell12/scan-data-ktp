Oke, ini sudah saya rapikan dalam format **Markdown** siap tempel ke GitHub, dengan heading, emoji, dan format yang konsisten.

---

````markdown
# 🆔 KTP Checker - Validator Kartu Tanda Penduduk Indonesia

Aplikasi desktop berbasis Python untuk memvalidasi dan memeriksa KTP (Kartu Tanda Penduduk) Indonesia dengan analisis data lengkap dan kemampuan pembuatan laporan.

---

## 🎯 Gambaran Umum

**KTP Checker** adalah aplikasi GUI berbasis Tkinter yang memberikan analisis detail dari KTP dengan mengekstrak serta memvalidasi informasi dari NIK (Nomor Induk Kependudukan) 16 digit.  
Aplikasi ini mendukung pengecekan individu maupun batch, serta dapat mengekspor hasil menjadi file PDF.

---

## ✨ Fitur

- 🔍 **Analisis NIK** – Mengurai dan mengekstrak informasi detail dari NIK 16 digit
- 📍 **Deteksi Provinsi** – Mengidentifikasi provinsi otomatis berdasarkan prefix NIK
- 👤 **Data Pribadi** – Mengekstrak tanggal lahir, jenis kelamin, dan umur
- 🌐 **Validasi Online** – Mengecek status pendaftaran di berbagai platform
- 📊 **Laporan Lengkap** – Membuat laporan PDF detail hasil pengecekan
- 🖥️ **Antarmuka GUI** – Tampilan desktop sederhana dengan Tkinter
- 📁 **Ekspor File** – Simpan hasil pengecekan dalam format PDF

---

## 🛠️ Detail Teknis

**Bahasa**: Python 3.7+  
**Framework GUI**: Tkinter  
**Pembuatan PDF**: ReportLab  
**HTTP Request**: Requests  
**Pengolahan Tanggal**: datetime  

### Fungsi Utama

#### `parse_nik(nik)`
- Mengambil informasi detail dari NIK  
- Hasil: provinsi, tanggal lahir, jenis kelamin, umur  
- Contoh:  
```python
parse_nik("1234567890123456")
````

#### `get_full_data_check(nik, email, phone)`

* Validasi data secara menyeluruh di berbagai platform:

  * BPJS Ketenagakerjaan
  * Dukcapil
  * Direktorat Pajak
  * BPJS Kesehatan
  * Media Sosial
  * E-commerce
* Mengembalikan laporan lengkap status pendaftaran

#### `export_to_pdf(data, filename)`

* Membuat laporan PDF profesional dengan semua hasil validasi

---

## 🚀 Instalasi & Penggunaan

### Persyaratan

* Python 3.7 atau lebih baru
* pip
```
git clone https://github.com/siyoell12/scan-data-ktp.git
cd scan-data-ktp
```
### Instalasi Dependensi
```bash
pip install tkinter requests reportlab
```
### Menjalankan Aplikasi

```bash
python dea.py
```

---

## 📋 Panduan Penggunaan

1. **Masukkan NIK** – Isi NIK 16 digit
2. **Masukkan Kontak** – Email & nomor HP untuk validasi
3. **Klik "Cek Data"** – Proses informasi KTP
4. **Lihat Hasil** – Analisis ditampilkan di area teks
5. **Ekspor PDF** – Simpan hasil pengecekan

### Contoh Kode

```python
from dea import get_full_data_check, parse_nik

nik_info = parse_nik("1234567890123456")
print(f"Provinsi: {nik_info['province']}")
print(f"Tanggal Lahir: {nik_info['birth_date']}")
print(f"Jenis Kelamin: {nik_info['gender']}")
print(f"Umur: {nik_info['age']}")

full_report = get_full_data_check("1234567890123456", "user@example.com", "081234567890")
print(json.dumps(full_report, indent=2))
```

---

## 📊 Format Output

### Informasi NIK

```json
{
  "province": "DKI Jakarta",
  "birth_date": "15-08-1990",
  "gender": "Laki-laki",
  "age": 33
}
```

### Laporan Validasi Lengkap

```json
{
  "nik_info": {...},
  "nik_registration": {
    "bpjsketenagakerjaan": {"registered": true, "url": "..."},
    "dukcapil": {"registered": true, "url": "..."}
  },
  "phone_registration": {...},
  "email_registration": {...},
  "darkweb_sale": {"sold": false, "details_url": "..."}
}
```

---

## 🔍 Analisis Struktur NIK

* **Kode Provinsi**: Mengenali semua 34 provinsi berdasarkan prefix NIK

  * 11: Aceh
  * 31: DKI Jakarta
  * 32: Jawa Barat
  * 33: Jawa Tengah
  * 34: DIY Yogyakarta
  * 35: Jawa Timur
  * ...dan lainnya

* **Ekstraksi Tanggal Lahir**:

  * Format DDMMYY (digit ke-7–12)
  * Hari > 40 → perempuan (hari - 40)
  * Tahun < 30 → 2000-an, ≥ 30 → 1900-an

---

## 🎨 Fitur GUI

* **Judul**: "DEA SAPUTRA CHECKER KTP"
* **Ukuran**: 500x600 px
* **Komponen**:

  * Input NIK
  * Input Email
  * Input Nomor HP
  * Tombol Cek Data
  * Tombol Ekspor PDF
  * Area Hasil

---

## 📄 Fitur Laporan PDF

**Struktur Laporan**:

1. Header: *Laporan Pengecekan KTP*
2. Informasi NIK
3. Status Pendaftaran di berbagai platform
4. Status di Dark Web
5. Timestamp pengecekan

**Contoh**:

```
Laporan Pengecekan KTP
====================

=== Informasi NIK ===
Provinsi: DKI Jakarta
Tanggal Lahir: 15-08-1990
Jenis Kelamin: Laki-laki
Umur: 33

=== Status Pendaftaran NIK ===
BPJS Ketenagakerjaan: Terdaftar
Dukcapil: Terdaftar
Direktorat Pajak: Tidak Terdaftar
...
```

---

## 🛡️ Privasi & Keamanan

* Pemrosesan lokal di komputer pengguna
* Tidak ada data yang disimpan/ditransmisikan
* Koneksi HTTPS untuk validasi online
* Sanitasi input sebelum diproses

---

## 🐛 Pemecahan Masalah

1. **Module not found**

   ```bash
   pip install tkinter requests reportlab
   ```
2. **GUI tidak terbuka** – pastikan Python 3.7+ & Tkinter terinstal
3. **Ekspor PDF gagal** – pastikan izin tulis & ReportLab terinstal

---

## 🌐 Komunitas & Sosial Media

Ingin berdiskusi, bertanya, atau berbagi ide? Bergabunglah dengan komunitas kami!

💬 Telegram Group: [t.me/airdropindependen](https://t.me/independendropers)

🐦 Twitter/X: [twitter.com/deasaputra12](https://x.com/Deasaputra_12)

🎮 Discord Server: [discord.gg/airdropindependen](https://discord.gg/Tuy2bR6CkU)


## Buy Me a Coffee

- **EVM:** 0x905d0505Ec007C9aDb5CF005535bfcC5E43c0B66
- **TON:** UQCFO7vVP0N8_K4JUCfqlK6tsofOF4KEhpahEEdXBMQ-MVQL
- **SOL:** BmqfjRHAKXUSKATuhbjPZfcNciN3J2DA1tqMgw9aGMdj

Thank you for visiting this repository, don't forget to contribute in the form of follows and stars.
If you have questions, find an issue, or have suggestions for improvement, feel free to contact me or open an *issue* in this GitHub repository.

**deasaputra**

