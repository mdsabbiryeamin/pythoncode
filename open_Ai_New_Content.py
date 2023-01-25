import openai

openai.api_key = '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'
prompt=input('Enter Your Tital for Keyword :')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=260,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
text =response.get('choices')[0].get('text')
print(text)
print(len(text))



