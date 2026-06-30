class Query:
    @staticmethod
    def refine(query):

        query = query.lower().strip()
        
        broad_terms = {
            # Photography & Imaging 
            "camera": ["Sony Mirrorless Body", "Nikon DSLR", "Cinematic Cinema Camera", "Point and Shoot Compact", "Action Camera"],
            "lens": ["50mm Prime Lens", "Wide Angle Landscape Lens", "Telephoto Zoom Lens", "Macro Lens", "Anamorphic Lens"],
            "lighting": ["RGB Video Light", "Softbox Studio Light", "Ring Light", "Camera Flash Speedlite"],
            "tripod": ["Carbon Fiber Travel Tripod", "Heavy Duty Fluid Head Tripod", "Flexible GorillaPod", "Smartphone Gimbal"],
            
            # Computing & Engineering Tech
            "laptop": ["High-Performance Gaming Laptop", "MacBook Pro", "Budget Student Laptop", "Engineering Workstation Laptop"],
            "keyboard": ["Mechanical Keyboard", "Wireless Membrane Keyboard", "Ergonomic Split Keyboard", "60% Gaming Keyboard"],
            "monitor": ["144Hz Gaming Monitor", "4K Color-Accurate Monitor", "Ultrawide Curved Monitor", "Portable USB-C Monitor"],
            "mouse": ["Wireless Gaming Mouse", "Ergonomic Vertical Mouse", "Travel Bluetooth Mouse", "Trackball Mouse"],
            "calculator": ["Graphing Calculator", "Scientific Engineering Calculator", "Financial Calculator"],
            "software": ["Python IDE License", "Photo Editing Software", "Video Editing Suite", "Antivirus Software"],
            
            # Audio & Entertainment
            "headphones": ["Wireless Noise Cancelling Earbuds", "Over-Ear Studio Headphones", "Wired Gaming Headset", "Bone Conduction Headphones"],
            "speaker": ["Portable Bluetooth Speaker", "Soundbar with Subwoofer", "Bookshelf Studio Monitors", "Smart Home Speaker"],
            "tv": ["OLED 4K Smart TV", "QLED Gaming TV", "Budget LED TV", "Outdoor Weatherproof TV"],
            
            # Skincare & Grooming
            "skincare": ["Daily Facial Cleanser", "Vitamin C Serum", "SPF 50 Face Sunscreen", "Overnight Hydrating Moisturizer", "Chemical Exfoliant"],
            "cleanser": ["Foaming Gel Cleanser", "Oil-Based Makeup Remover", "Salicylic Acid Acne Cleanser", "Gentle Hydrating Cleanser"],
            "trimmer": ["Electric Beard Trimmer", "Body Groomer", "Nail Care Kit", "Hair Clippers"],
            
            # Writing & Stationery
            "book": ["Hardcover Fiction Novel", "Blank Page Journal", "Technical Reference Book", "Biography", "Leatherbound Sketchbook"],
            "pen": ["Fountain Pen", "Fine-Liner Drawing Pens", "Premium Ballpoint Pen", "Calligraphy Set"],
            "desk": ["Standing Adjustable Desk", "L-Shaped Corner Desk", "Compact Laptop Desk", "Drafting Table"],
            
            # Mobile & Wearables
            "phone": ["iPhone Unlocked", "Samsung Galaxy Flagship", "Budget Android Smartphone", "Refurbished Smartphone"],
            "charger": ["65W GaN Fast Charger", "MagSafe Wireless Charger", "Car Charger Adapter", "High-Capacity Power Bank"],
            "watch": ["Smartwatch", "Analog Automatic Watch", "Fitness Tracker Band", "Rugged Outdoor GPS Watch"],
            
            # Home, Lifestyle & Hobbies
            "coffee": ["Instant Coffee Powder", "Whole Roast Coffee Beans", "Espresso Machine", "Cold Brew Maker", "French Press"],
            "shoes": ["Running Shoes", "Casual Everyday Sneakers", "Formal Leather Oxfords", "Heavy Duty Hiking Boots"],
            "bag": ["Photography Camera Backpack", "Laptop Messenger Bag", "Canvas Tote Bag", "Hiking Rucksack"],
            "telescope": ["Refractor Telescope", "Newtonian Reflector Telescope", "Smart Computerized Telescope", "Binoculars"],
            "art supplies": ["Chalk Pastels", "Acrylic Paint Set", "Floor Art Stencils", "Charcoal Drawing Kit"]
        }
        
        if query in broad_terms:
            print(f"\n[SYSTEM] '{query.title()}' is a massive category. Let's narrow that down so the API doesn't choke.")
            options = broad_terms[query]
            
            for i, opt in enumerate(options):
                print(f"[{i+1}] {opt}")
                
            try:
                choice = input(f"\nEnter a number [1-{len(options)}]: ")
                if choice.strip().isdigit() and 0 < int(choice) <= len(options):
                    refined_term = options[int(choice)-1]
                    print(f"Searching for: {refined_term}")
                    return refined_term
            except Exception:
                pass 
                
        return query
