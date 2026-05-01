from langchain_text_splitters import CharacterTextSplitter
text ='''The National Testing Agency has opened applications for the UGC-NET June 2026, to be held from June 22-30 with two new subjects added. It also issued detailed guidelines for NEET-UG 2026 on May 3, including mandatory biometric checks and alternative manual verification in case of technical or physical issues. The measures aim to maintain exam integrity while preventing candidate exclusion.'''

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('roadmap.pdf')
docs = loader.load()

splitter =CharacterTextSplitter(
    chunk_size = 100 , 
    chunk_overlap = 5 , 
    separator = ''

)


result = splitter.split_documents(docs)
print(result[1].page_content)





