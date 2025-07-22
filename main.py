import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
from docx import Document
from openai import AzureOpenAI

# Load .env secrets
load_dotenv()

# Azure settings
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "friendscorpus"
download_dir = "corpus"

# Create folder
os.makedirs(download_dir, exist_ok=True)

# Connect to Azure Blob
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

# Download .docx files
def download_corpus():
    print("Downloading files from Azure Blob Storage...")
    for blob in container_client.list_blobs():
        file_path = os.path.join(download_dir, blob.name)
        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(container_client.get_blob_client(blob).download_blob().readall())
                print(f"Downloaded: {blob.name}")

# Read .docx files
def read_corpus():
    corpus_text = ""
    for file in os.listdir(download_dir):
        if file.endswith(".docx"):
            doc = Document(os.path.join(download_dir, file))
            corpus_text += "\n".join([para.text for para in doc.paragraphs]) + "\n"
    return corpus_text

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)
def generate_script(prompt):
    completion = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": "You are a witty sitcom writer like the creators of Friends.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_tokens=4096,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return completion.choices[0].message.content



# Run the pipeline
if __name__ == "__main__":
    download_corpus()
    print("\nCorpus loaded. Now generating script...\n")

    while True:
        prompt = input("\n🎤 Enter your sitcom prompt (or type 'exit' to quit):\n> ")
        
        if prompt.lower() in ["exit", "quit"]:
            print("👋 Exiting script generator. Bye!")
            break

        result = generate_script(prompt)
        print("\n📝 Generated Sitcom Script:\n")
        print(result)

