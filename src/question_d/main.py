#add import
import question_d as qd

def main():
    num = 5
    print(f"Before calling use_local_variable: num = {num}")
    qd.use_local_variable(num)
    print(f"After calling use_local_variable: num = {num}")

if __name__ == "__main__":
    main()