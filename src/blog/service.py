from sentence_transformers import SentenceTransformer
model = SentenceTransformer("/home/mousavi-m/Documents/talk-to-django/all-MiniLM-L6-v2")

def get_embedding(text):
    embedding = model.encode([text])
    return embedding[0]
 