from transformers import pipeline

# Use 'text2text-generation' for T5 models like FLAN-T5
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

query = "Tell me about Apple's revenue in Q1 2024"
result = pipe(query, max_new_tokens=50)

print("💬 Result:\n", result[0]["generated_text"])