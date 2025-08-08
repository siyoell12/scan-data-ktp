# KTP Checker - Indonesian ID Card Validator

A Python-based desktop application for validating and checking Indonesian ID Cards (KTP) with comprehensive data analysis and reporting capabilities.

## 🎯 Overview

**DEA KTP Checker** is a GUI application built with Tkinter that provides detailed analysis of Indonesian ID Cards (KTP) by extracting and validating information from the 16-digit NIK (Nomor Induk Kependudukan). The application offers both individual checking and batch processing capabilities with PDF export functionality.

## ✨ Features

- **🔍 NIK Analysis**: Parse and extract detailed information from 16-digit NIK
- **📍 Province Detection**: Automatically identify province based on NIK prefix
- **👤 Personal Data**: Extract birth date, gender, and age from NIK
- **🌐 Online Validation**: Check registration status across multiple platforms
- **📊 Comprehensive Reports**: Generate detailed PDF reports with all findings
- **🖥️ User-Friendly GUI**: Easy-to-use desktop interface with Tkinter
- **📁 File Export**: Save results as PDF reports

## 🛠️ Technical Details

### Core Components

- **Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **PDF Generation**: ReportLab
- **HTTP Requests**: Requests library
- **Date Processing**: datetime module

### Key Functions

#### `parse_nik(nik)`
- **Purpose**: Extract detailed information from NIK
- **Returns**: Dictionary with province, birth date, gender, and age
- **Usage**: `parse_nik("1234567890123456")`

#### `get_full_data_check(nik, email, phone)`
- **Purpose**: Comprehensive data validation across multiple platforms
- **Platforms Checked**:
  - BPJS Ketenagakerjaan
  - Dukcapil (Civil Registry)
  - Tax Office
  - BPJS Kesehatan
  - Social Media platforms
  - E-commerce platforms
- **Returns**: Complete validation report with registration status

#### `export_to_pdf(data, filename)`
- **Purpose**: Generate professional PDF reports
- **Features**: Structured layout with all validation results
- **Output**: Professional PDF document ready for sharing

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies
```bash
pip install tkinter requests reportlab
```

### Run the Application
```bash
python dea.py
```

## 📋 Usage Guide

### 1. Launch the Application
```bash
python dea.py
```

### 2. Using the GUI
1. **Enter NIK**: Input the 16-digit NIK number
2. **Provide Contact Info**: Enter email and phone number for validation
3. **Click "Cek Data"**: Process the KTP information
4. **Review Results**: View detailed analysis in the text area
5. **Export PDF**: Save results as PDF report

### 3. Sample Usage
```python
# Import the module
from dea import get_full_data_check, parse_nik

# Parse NIK information
nik_info = parse_nik("1234567890123456")
print(f"Province: {nik_info['province']}")
print(f"Birth Date: {nik_info['birth_date']}")
print(f"Gender: {nik_info['gender']}")
print(f"Age: {nik_info['age']}")

# Get comprehensive data check
full_report = get_full_data_check("1234567890123456", "user@example.com", "081234567890")
print(json.dumps(full_report, indent=2))
```

## 📊 Output Format

### NIK Information Structure
```json
{
  "province": "DKI Jakarta",
  "birth_date": "15-08-1990",
  "gender": "Laki-laki",
  "age": 33
}
```

### Full Validation Report
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

## 🔍 NIK Structure Analysis

### Province Codes
The application recognizes all 34 Indonesian provinces based on NIK prefix:
- **11**: Aceh
- **31**: DKI Jakarta
- **32**: Jawa Barat
- **33**: Jawa Tengah
- **34**: DIY Yogyakarta
- **35**: Jawa Timur
- And 28 other provinces...

### Birth Date Extraction
- **Format**: DDMMYY from positions 7-12
- **Gender Indicator**: Day > 40 indicates female (day - 40)
- **Century**: YY < 30 = 2000s, YY ≥ 30 = 1900s

## 🎨 GUI Features

### Main Window
- **Title**: "DEA SAPUTRA CHECKER KTP"
- **Size**: 500x600 pixels
- **Components**:
  - NIK input field
  - Email input field
  - Phone number input field
  - "Cek Data" button
  - "Export PDF" button
  - Results display area

### Interactive Elements
- **Real-time validation** of input formats
- **Progress indicators** during processing
- **Error messages** for invalid inputs
- **Success confirmations** for operations

## 📄 PDF Report Features

### Report Structure
1. **Header**: "Laporan Pengecekan KTP"
2. **NIK Information**: Detailed breakdown of NIK data
3. **Registration Status**: Across all checked platforms
4. **Dark Web Status**: Data breach monitoring
5. **Timestamp**: When the check was performed

### Sample Report Content
```
Laporan Pengecekan KTP
====================

=== Informasi NIK ===
Province: DKI Jakarta
Birth Date: 15-08-1990
Gender: Laki-laki
Age: 33

=== NIK Registration Status ===
BPJS Ketenagakerjaan: Terdaftar
Dukcapil: Terdaftar
Tax Office: Tidak Terdaftar
...
```

## 🛡️ Privacy & Security

- **Local Processing**: All data processing happens locally on your machine
- **No Data Storage**: No personal information is stored or transmitted
- **HTTPS**: Secure connections for online validation
- **Input Validation**: Sanitization of all user inputs

## 🐛 Troubleshooting

### Common Issues

1. **"Module not found" error**
   ```bash
   pip install tkinter requests reportlab
   ```

2. **GUI not opening**
   - Ensure you're running Python 3.7+
   - Check if tkinter is available

3. **PDF export fails**
   - Ensure write permissions in current directory
   - Check if ReportLab is installed

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

