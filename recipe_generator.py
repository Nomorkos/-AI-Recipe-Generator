import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recipe(ingredients):
    """Generates a creative recipe using provided ingredients."""
    prompt = f"Generate a creative recipe using these ingredients: {ingredients}. Provide step-by-step instructions."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a master chef who creates delicious recipes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    ingredients = input("Enter a list of ingredients (separated by commas): ")
    recipe = generate_recipe(ingredients)
    print("\nGenerated Recipe:\n", recipe)
