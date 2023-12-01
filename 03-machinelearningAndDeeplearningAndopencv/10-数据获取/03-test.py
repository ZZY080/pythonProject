
import os
import openai

openai.organization="org-FtPbxDDLquJa2hkkiVgh6Wtn"
openai.api_key="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"

completion = openai.ChatCompletion.create (
 model="gpt-3.5-turbo",
 messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}]
)


# completion=openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )



print(completion.choices[0].message)