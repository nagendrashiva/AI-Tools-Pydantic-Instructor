class User(BaseModel):
    name: str
    age: int

user = User(name="John Doe", age=30)

print(user.__origin__)
my_list = list(range(1, 11))
from helpers import openai_model,prompt,custom_moel

#Replace With Your Output
class Titles(BaseModel):
    titles: List[str]

#Replace with your input
input = "Instagram marketing"

#Replace with your prompt
prompt = f"generate 5 titles for a video about {input}" 

#Replace With Your Model
openai_model = "gpt-3.5-turbo"

result = structured_generator(openai_model,prompt,Titles)
print(result.titles)