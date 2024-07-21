# # generate_embeddings.py
# from llama_index import GPTListIndex, LLMPredictor, ServiceContext
# from langchain import OpenAI

# def generate_embeddings(data):
#     llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="gpt-4"))
#     service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
#     documents = [Document(text) for text in data]
#     index = GPTListIndex.from_documents(documents, service_context=service_context)
#     return index

from sentence_transformers import SentenceTransformer

def generate_embeddings(data):
    # Load a pre-trained model from sentence-transformers
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for the provided data
    embeddings = model.encode(data, show_progress_bar=True)
    
    return embeddings
