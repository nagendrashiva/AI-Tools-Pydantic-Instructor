from typing import List, Type
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Define the structured_generator function with correct typing
def structured_generator(openai_model: str, prompt: str, custom_model: Type[BaseModel]) -> custom_model:
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    result = openai.Completion.create(
        engine=openai_model, 
        prompt=prompt,
        max_tokens=100  # Adjust the max_tokens parameter as needed
    )

    # Assuming custom_model has a 'titles' attribute
    titles_data = {'titles': [result['choices'][0]['text']]}
    return custom_model(**titles_data)

class User(BaseModel):
    name: str
    age: int

user = User(name="John Doe", age=30)

print(user.__class__.__name__)  # To print the class name
my_list = list(range(1, 11))

# Replace With Your Output
class Titles(BaseModel):
    titles: List[str]

# Replace with your input
input_text = "Instagram caption"

# Replace with your prompt
prompt = f"generate 5 titles for an Instagram post about {input_text}"

# Replace With Your Model
openai_model = "text-davinci-003"  # Use the appropriate GPT-3.5 model name

result = structured_generator(openai_model, prompt, Titles)
print(result.titles)
