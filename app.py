from typing import List
from pydantic import BaseModel
from helpers import structured_generator  # Corrected import statement

class User(BaseModel):
    name: str
    age: int

user = User(name="John Doe", age=30)

print(user.__origin__)
my_list = list(range(1, 11))

# Replace With Your Output
class Titles(BaseModel):
    titles: List[str]

# Replace with your input
input_text = "Instagram marketing"

# Replace with your prompt
prompt = f"generate 5 titles for a video about {input_text}"

# Replace With Your Model
openai_model = "gpt-3.5-turbo"

result = structured_generator(openai_model, prompt, Titles)
print(result.titles)
