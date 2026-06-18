import pdfplumber
import docx
import io
import PyPDF2

# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_pdf(bytes_data):
    try:
        with pdfplumber.open(io.BytesIO(bytes_data)) as pdf:
            return "\n".join([(page.extract_text() or "") for page in pdf.pages])
    except:
        reader = PyPDF2.PdfReader(io.BytesIO(bytes_data))
        return "\n".join([(page.extract_text() or "") for page in reader.pages])


# -----------------------------
# Extract text from DOCX
# -----------------------------
def extract_docx(bytes_data):
    with open("temp.docx", "wb") as f:
        f.write(bytes_data)

    d = docx.Document("temp.docx")
    return "\n".join([p.text for p in d.paragraphs])


# -----------------------------
# Main Extract Function
# -----------------------------
def extract_resume_text(filename, content):
    """
    Always returns: (text, skills_list, experience_list)
    Fix: ensure filename is STRING
    """
    filename = str(filename).lower()

    if filename.endswith(".pdf"):
        text = extract_pdf(content)

    elif filename.endswith(".docx") or filename.endswith(".doc"):
        text = extract_docx(content)

    else:
        try:
            text = content.decode("utf-8", errors="ignore")
        except:
            text = ""

    # RETURN must be EXACTLY 3 values
    return text, [], []
