
def generate_sequence(n):
    sequence = [n] 
    while n != 1:   
        if n % 2 == 0:  
            n //= 2     
        else:           
            n = n * 3 + 1  
        sequence.append(n)  
    return sequence


def cached_sequence(n):
    cache = cached_sequence.__dict__.setdefault('cache', {})
    if n in cache:
        return cache[n]
    
    sequence = [n]
    current = n
    
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1
        sequence.append(current)

    cache[n] = sequence
    return sequence

def main():
    print(cached_sequence(10))

if __name__ == "__main__":
    main()


def main():
  print("generate sequcne :",generate_sequence(10))
  print("cached sequence :", cached_sequence(10))
if __name__ == "__main__":
    main()