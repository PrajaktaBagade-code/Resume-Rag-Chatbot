# Step 1: Load Resume PDF

loader = PyPDFLoader("resume/resume praj.pdf")

documents = loader.load()


#Step 2: Split Resume
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)


# Step 3: Create Embeddings


embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Step 4: Store in ChromaDB

db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="chroma_db"
)

# Step 5: Create Retriever
retriever = db.as_retriever(
    search_kwargs={"k":3}
)

# Step 6: Load GPT

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# Step 7: Create RAG Chain


prompt = ChatPromptTemplate.from_template("""
Answer the question using only the provided context.

Context:
{context}

Question:
{input}
""")

document_chain = create_stuff_documents_chain(llm, prompt)

retrieval_chain = create_retrieval_chain(
    retriever,
    document_chain
)

response = retrieval_chain.invoke(
    {"input": "What are my skills?"}
)

print(response["answer"])

# ask questions
while True:

    question = input("Ask Question : ")

    if question.lower() == "exit":
        break

    answer = retrieval_chain.invoke(
        {"input":question}
        )
    print(type(answer))
    print(answer.keys())

    print("\nAnswer:")
    print(answer["answer"])  
