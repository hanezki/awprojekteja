import time

def find_prime_numbers(num):
    start_time = time.time()
    prime_numbers = []
    for i in range(2, num + 1):
        prime_numbers.append(i)


    i = 2
    while i < num:
        i += 2
        if i <= num:
            if i in prime_numbers:
                prime_numbers.remove(i)


    i = 3
    while i < num:
        i += 3
        if i <= num:
            if i in prime_numbers:
                prime_numbers.remove(i)

    i = 5
    while i < num:
        i += 5
        if i <= num:
            if i in prime_numbers:
                prime_numbers.remove(i)

    i = 7
    while i < num:
        i += 7
        if i <= num:
            if i in prime_numbers:
                prime_numbers.remove(i)

    print(prime_numbers)
    total_time = time.time() - start_time
    print(f"Program took {total_time} seconds to run")




def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    start_time = time.time()
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            print
            print(p)
    total_time = time.time() - start_time
    print(f"Program took {total_time} seconds to run")



try:
    numero = int(input("Anna numero ja ohjelma laskee alkuluvut siihen numeroon asti\n>"))
    find_prime_numbers(numero)
    #sieve_of_eratosthenes(numero)

except ValueError:
    print("Virheellinen inputti")