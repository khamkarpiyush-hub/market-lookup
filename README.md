# 🛒 Market Lookup

A command-line tool that aggregates product listings from Google Shopping and Amazon using SerpAPI, filters irrelevant results, computes a Bayesian Trust Score, and recommends the best-value products.

---

## Features

- 🔍 Search products across Google Shopping and Amazon
- 🤝 Merge results from multiple search engines
- 🧹 Filter out common reseller and accessory listings
- 📊 Bayesian Trust Score for ranking products
- 💰 Sort by:
  - Lowest Price
  - Highest Trust Score
  - High Rating (4.0+)
  - Best Value Recommendation
- 🌐 Open any product directly in your default web browser
- 🖥️ Interactive Command Line Interface

---

## How it Works

1. Enter a product name.
2. For selected product categories (such as laptops), the application asks follow-up questions to refine the search.
3. Results are collected from:
   - Google Shopping
   - Amazon
4. The datasets are merged.
5. Irrelevant listings (such as trade-ins, resellers, and common accessories) are filtered.
6. Each product receives a Bayesian Trust Score.
7. Results are sorted according to the user's preference.
8. Selecting a product opens its listing in your default browser.

---

## Project Structure

```
market-lookup/
│
├── backend.py      # API calls, filtering, scoring and sorting
├── main.py         # CLI entry point
├── query.py        # Query refinement
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

## Example

```
Enter product to search:
iphone 17

Searching Google and Amazon...

Choose sorting:

1. Lowest Price
2. High Rating
3. Best Value
4. Highest Trust Score
```

---

## Technologies Used

- Python
- SerpAPI
- Google Shopping
- Amazon Search
- python-dotenv

---

## Known Limitations

- Search quality depends on the information returned by SerpAPI.
- Some products may include closely related variants (e.g., Pro, Air, or Max models).
- Filtering is rule-based and may not remove every irrelevant listing.

---

## Future Improvements

- Smarter product classification
- Better duplicate detection
- Export results to CSV
- Improved recommendation algorithm
- More query refinement categories

---
