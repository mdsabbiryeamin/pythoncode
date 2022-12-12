import openai

openai.api_key = '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'
prompt=input('Enter Your Tital or Keyword :')

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
print(response)


