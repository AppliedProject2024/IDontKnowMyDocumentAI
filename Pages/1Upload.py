import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from pypdf import PdfReader

#function to read PDF file
def ExtractAndChunk(uploaded_file):
    #extract pdf text
    pdf_reader = PdfReader(uploaded_file)
    full_text = ""
    #extract text from each page
    for page in pdf_reader.pages:
        full_text += page.extract_text()
    
    #chunk text using langchain TextSplitter
    text_splitter = CharacterTextSplitter(
        separator="\n", #split by newline
        chunk_size=1000, #maximun chunk size
        chunk_overlap=100 #overlap between chunks preserves context
    )
    #split text into chunks
    chunks = text_splitter.split_text(full_text)
    #return chunks as list of Documents
    return [Document(page_content=chunk) for chunk in chunks]

#header for Upload Section
st.header("Upload Your Documents")

#upload multiple files
uploaded_files = st.file_uploader(
    "Upload one or more PDF files", 
    type=["pdf"], #only accept pdf files
    accept_multiple_files=True #accept multiple files
)

#check if any files are uploaded
if uploaded_files:
    st.subheader("Uploaded Files")
    
    #loop through each uploaded file
    for uploaded_file in uploaded_files:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        #placeholder for processing the document
        st.write(f"Processing '{uploaded_file.name}'...")
        chunks = ExtractAndChunk(uploaded_file)

        #display the extracted text
        st.subheader("Extracted Text:")
        for idx, chunk in enumerate(chunks):
            st.write(f"Chunk {idx+1}:")
            st.write(chunk.page_content)
