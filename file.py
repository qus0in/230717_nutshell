import streamlit as st
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

def handle_pdf():
    label = "✅ 파이썬 학습 PDF 파일을 올려주세요"
    # PDF 문서 경로 지정
    # pdf_path = 'example.pdf'
    uploaded_file = st.file_uploader(
        label,
        type="pdf")
    if uploaded_file is not None:
        # PDF에서 텍스트 추출
        extracted_text = extract_text_from_pdf(uploaded_file.name)
        if extracted_text:
            with st.expander("📝 추출한 텍스트"):
                st.write(extracted_text)

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    return_string = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(resource_manager, return_string, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)
    with open(pdf_path, 'rb') as pdf_file:
        for page in PDFPage.get_pages(pdf_file, check_extractable=True):
            interpreter.process_page(page)

        text = return_string.getvalue()
    device.close()
    return_string.close()
    return text

