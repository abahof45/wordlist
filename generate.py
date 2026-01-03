keywords = ["epicentre", "epiguesthouse"]
years = [str(y) for y in range(2000, 2027)]
specials = ["!", "@", "#", "$", "*", "_", "."]

def generate_list():
    wordlist = set()
    
    # 1. Standard combinations: word + year, Year + word
    for word in keywords:
        for year in years:
            # Case variations
            variants = [word.lower(), word.capitalize(), word.upper()]
            # Leetspeak variant (e=3, i=1, s=5, o=0)
            leets = word.replace('e','3').replace('i','1').replace('s','5').replace('o','0')
            variants.append(leets)

            for v in variants:
                wordlist.add(f"{v}{year}")         # epicentre2024
                wordlist.add(f"{year}{v}")         # 2024epicentre
                
                # 2. Adding special characters
                for s in specials:
                    wordlist.add(f"{v}{s}{year}")  # epicentre@2024
                    wordlist.add(f"{s}{v}{year}")  # !epicentre2024
                    wordlist.add(f"{v}{year}{s}")  # epicentre2024!
                    wordlist.add(f"{year}{s}{v}")  # 2024!epicentre

                # 3. Padding/Doubling (common for meeting length requirements)
                wordlist.add(f"{v}{v}")
                wordlist.add(f"{v}{year}{year}")

    # Convert to list and trim or pad to exactly 10,000
    final_list = list(wordlist)
    return final_list[:10000]

# Generate and save
results = generate_list()
with open("wordlist.txt", "w") as f:
    for item in results:
        f.write(item + "\n")

print(f"Generated {len(results)} words in wordlist.txt")
