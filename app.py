from pydantic import BaseModel
from typing import List
from helpers import structured_generator

#Replace With Your Output
class Titles(BaseModel):
    titles: List[str]

input = "Instagram marketing"

prompt = f"generate 5 titles for a video about {input}" 

#Replace With Your Model
openai_model = "gpt-3.5"

result = structured_generator(openai_model,prompt,Titles)
print(result.titles)