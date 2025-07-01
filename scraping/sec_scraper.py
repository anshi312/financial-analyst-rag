# scraping/earnings_scraper.py
import pdfplumber
import requests
import os

def download_pdf(url, save_path):
    r = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(r.content)

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

if __name__ == "__main__":
    # Example Apple Q1 2024 earnings PDF
    pdf_url = "https://www.apple.com/newsroom/pdfs/FY24_Q1_Consolidated_Financial_Statements.pdf"
    local_path = "data/raw/apple_q1_2024.pdf"

    os.makedirs("data/raw", exist_ok=True)
    download_pdf(pdf_url, local_path)
    content = extract_text_from_pdf(local_path)
    print(content[:500])  # Print preview