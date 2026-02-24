# 📸 EXIF Metadata Batch Fixer

A high-performance Python automation utility designed to bulk-correct missing or improperly formatted EXIF temporal data (Date/Time) across massive datasets of image files. 

## 🚀 The Problem & The Solution

**The Problem:** During a large-scale data migration from cloud storage (Google Photos) to local drives, the original creation dates of over 16,000 images were stripped or modified to the download date. Manually correcting the metadata for this volume of files was practically impossible and highly inefficient.

**The Solution:**
I engineered this Python script to automate the extraction of correct temporal data (often embedded in the filename or JSON sidecar files) and safely inject it back into the image's EXIF metadata header. What would have taken weeks of manual data entry was completed in minutes.

## ✨ Key Features
* **Bulk Processing:** Capable of iterating through thousands of high-resolution images rapidly.
* **EXIF Injection:** Modifies the `DateTimeOriginal` and `DateTimeDigitized` tags without degrading image quality.
* **Automated Parsing:** Intelligently extracts intended dates directly from complex filename structures.
* **Safe Execution:** Built-in error handling to skip unsupported file types or corrupted images without halting the entire batch process.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.x
* **Core Libraries:** `os`, `datetime`
* **Image Processing:** `Pillow` (PIL) / `piexif` *(Note: Adjust based on your actual imports)*

## 💻 Usage Instructions

**⚠️ IMPORTANT DISCLAIMER:** *Always create a secure backup of your images before running any batch-modification scripts. This tool alters file metadata directly.*

**1. Clone the repository:**
```bash
git clone [https://github.com/krisnamahardita/python-exif-metadata-fixer.git](https://github.com/krisnamahardita/python-exif-metadata-fixer.git)
cd python-exif-metadata-fixer

2. Install dependencies (if any):
Bash
pip install -r requirements.txt

3. Run the script:
Place your images in the designated target directory (update the path in the script if necessary), then execute:
Bash
python main.py
(Replace main.py with the actual name of your script file).

🧑‍💻 Author
I Putu Krisna Mahardita

LinkedIn: linkedin.com/in/iputukrisnamahardita

Email: krisnamahardita@gmail.com
