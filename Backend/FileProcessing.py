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


