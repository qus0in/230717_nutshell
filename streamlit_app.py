import streamlit as st

def handle_pdf():
    label = "✅ 파이썬 학습 PDF 파일을 올려주세요"
    pdf_path = st.file_uploader(
        label,
        type="pdf")
    st.write(pdf_path)

def main():
    handle_pdf()

if __name__ == "__main__":
    main()
