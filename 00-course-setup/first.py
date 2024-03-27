import os
from openai import AzureOpenAI

openaibase = os.environ.get('AZURE_OPENAI_ENDPOINT')
openaikey = os.environ.get('AZURE_OPENAI_KEY')
openaideployment= os.environ.get('AZURE_OPENAI_DEPLOYMENT')
openaiapiversion = os.environ.get('AZURE_OPENAI_API_VERSION')

print(f"The key is {openaikey}")
print(f"The version is {openaiapiversion}")

client = AzureOpenAI(azure_endpoint=openaibase,
                     api_key=openaikey, 
                     azure_deployment=openaideployment,
                     api_version=openaiapiversion)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message.content)
