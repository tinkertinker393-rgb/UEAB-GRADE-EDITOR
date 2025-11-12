# SPARK-X | UEAB Student Portal

Welcome to the private student portal and data extractor tool for iCampus UEAB.

## How it Works

1. **HTML portal** (in `portal.html`) shows your grades, timetable, and assignments with Matrix background.
2. **Python script** (`icampus_scraper.py`) lets you (the student) log in to iCampus, automatically download your real grades and timetable.
3. **You copy the exported JSON into the HTML portal.**  
   **No private password is ever uploaded to GitHub!**

## Getting Started

1. Download or fork this repository.
2. Run `icampus_scraper.py` (see below) to extract your data.
3. Copy the resulting `mydata.json` into `portal.html` (see the comments in the code).
4. Open `portal.html` in your browser to see your real data—Matrix style!

## Data Extraction (Python)

- Install requirements (Python 3.8+, [Chrome](https://www.google.com/chrome/) & chromedriver):

    ```sh
    pip install selenium beautifulsoup4
    ```

- Run the script:

    ```sh
    python icampus_scraper.py
    ```

- Enter your iCampus credentials when prompted (used only on your local machine).
- Script will produce a `mydata.json` file with your real records.

## Portal

Open `portal.html`.  
To use real data: paste your exported data as explained in `portal.html` code comments!

---
