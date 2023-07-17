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
        extracted_text = extract_data(uploaded_file)
        st.session_state['extracted_text'] = extracted_text
        with st.expander("📝 추출한 텍스트"):
            st.write(extracted_text)

def extract_data(pdf_file):
    resource_manager = PDFResourceManager()
    return_string = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(resource_manager, return_string, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    for page in PDFPage.get_pages(pdf_file, check_extractable=True):
        interpreter.process_page(page)

    text = return_string.getvalue()

    device.close()
    return_string.close()

    return text

