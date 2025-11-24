# File: main.py
import sys

# --- CORRECTED IMPORTS BELOW ---
# Since 'utils' and 'genetics' are inside the 'Source_code' folder,
# we must reference that folder first using dot notation.

from Source_code.utils import validators
from Source_code.genetics import analyzer, central_dogma, manipulater

def main():
    print("--- Gene-Tool: DNA Sequence Analyzer ---")

    while True:
        print("\nMAIN MENU")
        print("1. Calculate GC Content")
        print("2. Transcribe to RNA")
        print("3. Get Reverse Complement")
        print("4. Exit")

        choice = input("Select option (1-4): ")

        if choice == '4':
            print("Exiting Gene-Tool.")
            sys.exit()

        # Input Phase
        user_seq = input("\nEnter DNA Sequence: ")
        
        # --- LOGIC IMPLEMENTATION (Example of how you might use the imports) ---
        # You will need to implement the logic below based on your modules. 
        # For example:
        # if choice == '1':
        #     result = analyzer.gc_content(user_seq)
        #     print(f"GC Content: {result}%")

if __name__ == "__main__":
    main()
