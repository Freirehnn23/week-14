def bilangan_prima(n, pembagi=2):
    if n <= 1:
        return False
    if pembagi * pembagi > n:
        return True
    if n % pembagi == 0:
        return False
    return bilangan_prima(n, pembagi + 1)

def main():
    bilangan = int(input("Masukkan bilangan yang Ingin di Check: "))
    if bilangan_prima(bilangan):
        print(f"{bilangan} merupakan bilangan prima.")
    else:
        print(f"{bilangan} bukan bilangan prima.")
    
if __name__ == "__main__":
    main()
