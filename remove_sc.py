import pdfplumber

def rmspec_char(text):
    cleaned_text = ''.join(c for c in text if c.isalnum() or c.isspace())
    return cleaned_text

def text_extractor(pdf_path, output_path):
    with pdfplumber.open(pdf_path) as pdf:
        metadata = pdf.metadata
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    cleaned_text = rmspec_char(text)
    
    metadata_str = "\n".join(f"{key}: {value}" for key, value in metadata.items())
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("Text: "+cleaned_text.lower()" + "\n\nMetadata:\n" + metadata_str)
    
    print(f"text:{output_path}")

if __name__ == "__main__":
    pdf_path = 'C:/Users/SURAJ/Documents/Project/RAG/Resume.pdf'
    output_path = 'output.txt'
    text_extractor(pdf_path, output_path)
