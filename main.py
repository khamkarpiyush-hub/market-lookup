from backend import SERPAPI, ProductSorter, Scoring
from query import Query

if __name__ == "__main__":
    while True:    
        query = input("Enter product to search: ") 
        query = Query.refine(query)
    
        print(f"\nSearching Google and Amazon for '{query}'...")
        api = SERPAPI()
        products_g = api.google(query)
        products_a = api.amazon(query)
        all_products = products_g + products_a
    
        if not all_products:
            print("No products found.")
        else:
            products = ProductSorter.filter_out_buyback_sites(all_products)
            products = Scoring.evaluate_products(products)
            print("\nHow would you like to view the results?")
            print("1. Sort by Lowest Price")
            print("2. Filter by High Rating (4.0+)")
            print("3. Sort by Best Value")
            print("4. Sort by Highest Trust Score")
        
            try:
                ch = int(input("\nEnter your choice (1-4): "))
            
                if ch == 1:
                    display_list = ProductSorter.sort_price(products)
                elif ch == 2:
                    display_list = ProductSorter.min_rating(products, 4.0)
                elif ch == 3:
                    display_list = ProductSorter.sort_by_recommendation(products)
                elif ch == 4:
                    display_list = ProductSorter.sort_by_trust(products)
                else:
                    print("Invalid choice. Defaulting to AI Recommendation.")
                display_list = ProductSorter.sort_by_recommendation(products)
                
                print("\n--- Search Results ---")
                for i, p in enumerate(display_list):
                    print(f"{i+1}. {p}")
                
                choice = int(input("\nEnter product number to open link: "))
                if 1 <= choice <= len(display_list):
                    display_list[choice - 1].user_link()
                else:
                    print("Invalid product number.")
                
            except ValueError:
                print("Error: Please enter numbers only.")
