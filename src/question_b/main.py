import question_b as qb

def main():
    qb.global_counter = 0
    print(f"Initial global_counter: {qb.global_counter}")
    new_value = qb.use_global()
    print(f"global_counter after use_global(): {new_value}")

if __name__ == "__main__":
    main()