import pandas as pd
import requests

def translate_text(text, target_language="id"):
    api_key = "YOUR_API_KEY"
    endpoint = "https://api-free.deepl.com/v2/translate"

    params = {
        "auth_key": api_key,
        "text": text,
        "target_lang": target_language,
    }

    response = requests.post(endpoint, data=params)

    if response.status_code == 200:
        result = response.json()
        translations = result["translations"]
        translated_text = translations[0]["text"]
        return translated_text
    else:
        print(f"Error: {response.status_code}")
        return None

input_file = "split-id-to-en.csv"
output_file = "en-to-id.csv"
df = pd.read_csv(input_file)

df["id"] = df["en"].apply(translate_text, target_language="id")

df.to_csv(output_file, index=False)

print(f"Translation completed. Output saved to {output_file}")