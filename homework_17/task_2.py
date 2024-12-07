
graph = {
    "A":["B", "C"],
    "B": ["D"],
    "C":["E"]
}
def alphabet_sequence(graph, start, target):
    queue = [start] 
    while queue:
        current = queue.pop()  
        if current == target:  
            return True
        if current in graph:
            queue.extend(graph[current])
    return False  
def main():
    start = input("Please enter the starting alphabet: ")
    target = input("Please enter the target alphabet: ")
    print(alphabet_sequence(graph, start, target))

if __name__ == "__main__":
    main()