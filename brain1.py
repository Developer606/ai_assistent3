import openai
from speek import say
openai.api_key = "ENTER YOUR OPEN AI API KEY"
def pro(a):
    prompt = a
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text
while True:
    say(pro(input("enter: ")))

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="how are you",
#   temperature=0.51,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
