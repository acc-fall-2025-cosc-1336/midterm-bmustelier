#add import
import question_c as qc

def main():
    print("Property tax calculator. Enter 'q' to quit.")
    while True:
        user_input = input("Enter actual property value (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Goodbye!")
            return
        try:
            value = float(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value < 0:
            print("Please enter a non-negative value.")
            continue

        assessment = qc.get_assessment_value(value)
        tax = qc.get_tax_assessed(assessment)

        print(f"Assessment value: ${assessment:,.2f}")
        print(f"Property tax: ${tax:,.2f}")
if __name__ == "__main__":
    main()