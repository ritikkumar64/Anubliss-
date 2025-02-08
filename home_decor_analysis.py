import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import seaborn as sns

# Example: Scrape product data from a website
url = "https://example.com/home-decor"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = []
for item in soup.find_all('div', class_='product'):
    name = item.find('h2').text
    price = item.find('span', class_='price').text
    products.append({'name': name, 'price': price})

# Convert to DataFrame
df_products = pd.DataFrame(products)
print("Scraped Product Data:")
print(df_products.head())



# Example: Analyze customer reviews for sentiment
# Load sample review data (you can replace this with real data)
data = {
    'comment': [
        'I love this product!',
        'Great quality and fast shipping.',
        'Not worth the price.',
        'Excellent customer service.',
        'The product broke after a week.'
    ]
}
reviews = pd.DataFrame(data)

# Analyze sentiment (using a simple keyword approach)
positive_keywords = ['love', 'great', 'excellent']
reviews['sentiment'] = reviews['comment'].apply(
    lambda x: 'positive' if any(word in x for word in positive_keywords) else 'neutral'
)

print("\nCustomer Review Sentiment Analysis:")
print(reviews['sentiment'].value_counts())

# Example: Bar chart of product sales
data = {'Product A': 150, 'Product B': 200, 'Product C': 120}
products = list(data.keys())
sales = list(data.values())

plt.bar(products, sales, color='skyblue')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product Sales Performance')
plt.show()

# Example insights
print("\nKey Insights:")
print("- Sustainable and customizable products are trending.")
print("- Competitive pricing and fast shipping are key drivers for customer satisfaction.")
print("- Positive reviews often mention 'love', 'great', and 'excellent'.")