import tkinter as tk
from tkinter import messagebox, filedialog
import requests
from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def parse_nik(nik):
    wilayah = {
        '11': 'Aceh', '12': 'Sumatera Utara', '13': 'Sumatera Barat',
        '14': 'Riau', '15': 'Jambi', '16': 'Sumatera Selatan',
        '17': 'Bengkulu', '18': 'Lampung', '19': 'Kepulauan Bangka Belitung',
        '21': 'Kepulauan Riau', '31': 'DKI Jakarta', '32': 'Jawa Barat',
        '33': 'Jawa Tengah', '34': 'Daerah Istimewa Yogyakarta',
        '35': 'Jawa Timur', '36': 'Banten', '51': 'Bali',
        '52': 'Nusa Tenggara Barat', '53': 'Nusa Tenggara Timur',
        '61': 'Kalimantan Barat', '62': 'Kalimantan Tengah',
        '63': 'Kalimantan Selatan', '64': 'Kalimantan Timur',
        '65': 'Kalimantan Utara', '71': 'Sulawesi Utara',
        '72': 'Sulawesi Tengah', '73': 'Sulawesi Selatan',
        '74': 'Sulawesi Tenggara', '75': 'Gorontalo',
        '76': 'Sulawesi Barat', '81': 'Maluku', '82': 'Maluku Utara',
        '91': 'Papua', '92': 'Papua Barat'
    }
    province_code = nik[:2]
    province = wilayah.get(province_code, 'Tidak diketahui')
    
    birth_part = nik[6:12]
    try:
        day = int(birth_part[:2])
        month = int(birth_part[2:4])
        year = int(birth_part[4:6])
        gender = 'Perempuan' if day > 40 else 'Laki-laki'
        if day > 40:
            day -= 40
        year += 1900 if year > 30 else 2000
        birth_date = date(year, month, day)
    except:
        birth_date = None
        gender = 'Tidak diketahui'
    
    if birth_date:
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    else:
        age = None
    
    return {
        'province': province,
        'birth_date': birth_date.strftime('%d-%m-%Y') if birth_date else 'Tidak valid',
        'gender': gender,
        'age': age
    }

def get_full_data_check(nik, email, phone):
    platforms = {
        'bpjsketenagakerjaan': f'https://www.google.com/search?q="{nik}" site:bpjsketenagakerjaan.go.id',
        'dukcapil': f'https://www.google.com/search?q="{nik}" site:dukcapil.kemendagri.go.id',
        'tax': f'https://www.google.com/search?q="{nik}" site:tax.go.id',
        'bpjs_kesehatan': f'https://www.google.com/search?q="{nik}" site:bpjs-kesehatan.go.id'
    }
    
    nik_info = parse_nik(nik)
    
    # Simulasi registrasi
    nik_reg = {k: {'registered': int(nik[-1]) % 2 == 0, 'url': v} for k, v in platforms.items()}
    phone_reg = {k: {'registered': int(phone[-1]) % 2 == 0, 'url': f'https://example.com/{phone}'} for k in ['Facebook', 'Instagram', 'Twitter', 'Tokopedia', 'Shopee', 'Bukalapak']}
    email_reg = {k: {'registered': len(email) % 2 == 0, 'url': f'https://example.com/{email}'} for k in ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Tokopedia', 'Shopee', 'Bukalapak']}
    
    return {
        'nik_info': nik_info,
        'nik_registration': nik_reg,
        'phone_registration': phone_reg,
        'email_registration': email_reg,
        'darkweb_sale': {'sold': False, 'details_url': f'https://example.com/darkweb/{nik}'}
    }

def export_to_pdf(data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Laporan Pengecekan KTP")
    
    y = height - 100
    c.setFont("Helvetica", 12)
    
    # NIK Info
    c.drawString(100, y, "=== Informasi NIK ===")
    y -= 20
    for k, v in data['nik_info'].items():
        c.drawString(120, y, f"{k}: {v}")
        y -= 15
    
    # Registrations
    for section in ['nik_registration', 'phone_registration', 'email_registration']:
        y -= 20
        c.drawString(100, y, f"=== {section.replace('_', ' ').title()} ===")
        y -= 20
        for platform, info in data[section].items():
            status = "Terdaftar" if info['registered'] else "Tidak Terdaftar"
            c.drawString(120, y, f"{platform}: {status}")
            y -= 15
    
    # Dark Web
    y -= 20
    c.drawString(100, y, "=== Status Penjualan Data di Dark Web ===")
    y -= 20
    c.drawString(120, y, f"Data dijual: {'Ya' if data['darkweb_sale']['sold'] else 'Tidak'}")
    
    c.save()

class KTPCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DEA SAPUTRA CHECKER KTP")
        self.root.geometry("500x600")
        
        # Input fields
        tk.Label(root, text="NIK (16 digit):").pack()
        self.nik_entry = tk.Entry(root)
        self.nik_entry.pack()
        
        tk.Label(root, text="Email:").pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()
        
        tk.Label(root, text="Nomor HP:").pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()
        
        # Buttons
        tk.Button(root, text="Cek Data", command=self.check_data).pack(pady=10)
        tk.Button(root, text="Export PDF", command=self.export_pdf).pack(pady=5)
        
        # Result display
        self.result_text = tk.Text(root, height=20, width=60)
        self.result_text.pack()
        
    def check_data(self):
        nik = self.nik_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        
        if len(nik) != 16 or not nik.isdigit():
            messagebox.showerror("Error", "NIK tidak valid. Harus 16 digit angka.")
            return
        
        self.data = get_full_data_check(nik, email, phone)
        
        # Display results
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "=== Informasi NIK ===\n")
        for k, v in self.data['nik_info'].items():
            self.result_text.insert(tk.END, f"{k}: {v}\n")
        
        for section in ['nik_registration', 'phone_registration', 'email_registration']:
            self.result_text.insert(tk.END, f"\n=== {section.replace('_', ' ').title()} ===\n")
            for platform, info in self.data[section].items():
                status = "Terdaftar" if info['registered'] else "Tidak Terdaftar"
                self.result_text.insert(tk.END, f"{platform}: {status}\n")
        
        self.result_text.insert(tk.END, "\n=== Status Penjualan Data di Dark Web ===\n")
        self.result_text.insert(tk.END, f"Data dijual: {'Ya' if self.data['darkweb_sale']['sold'] else 'Tidak'}\n")
    
    def export_pdf(self):
        if not hasattr(self, 'data'):
            messagebox.showerror("Error", "Silakan cek data terlebih dahulu.")
            return
        
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filename:
            export_to_pdf(self.data, filename)
            messagebox.showinfo("Sukses", f"Data berhasil diekspor ke {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KTPCheckerApp(root)
    root.mainloop()
