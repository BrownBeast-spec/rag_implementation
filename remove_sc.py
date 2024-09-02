import pdfplumber

def rmspec_char(text):
    cleaned_text = ''.join(c for c in text if c.isalnum() or c.isspace())
    return cleaned_text

def text_extractor(pdf_path, output_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    cleaned_text = rmspec_char(text)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_text.lower())
    
    print(f"{output_path}")

if __name__ == "__main__":
    pdf_path = 'C:/Users/SURAJ/Documents/Project/RAG/Resume.pdf'
    output_path = 'output.txt'
    text_extractor(pdf_path, output_path)
