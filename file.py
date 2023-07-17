import streamlit as st
import pdfplumber

def handle_pdf():
    label = "✅ 파이썬 학습 PDF 파일을 올려주세요"
    # PDF 문서 경로 지정
    # pdf_path = 'example.pdf'
    uploaded_file = st.file_uploader(
        label,
        type="pdf")
    if uploaded_file is not None:
        extracted_text = extract_data(uploaded_file)
        with st.expander("📝 추출한 텍스트"):
            st.write(extracted_text)

def extract_data(pdf_file):
    data = []
    with pdfplumber.load(pdf_file) as pdf:
        pages = pdf.pages
        for p in pages:
            data.append(p.extract_tables())
    return "\n".join(data)

