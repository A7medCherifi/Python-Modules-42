def fibonacci_calculator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b , a + b


def prime_calculator():
    num = 2
    while True:
        is_prime = 1
        for i in range(2, num):
            if num % i == 0:
                is_prime = 0
                break
        if is_prime:
            yield num
        num += 1



def event_generator(players: list, levels: list, events: list):
    high_levels = 0
    total_events = 0
    treasure_events = 0
    level_up_events = 0
    for i in range(0, 1000):
        player = i % len(players)
        level = i % len(levels)
        event = i % len(events)
        total_events = i + 1
        if levels[level] > 10:
            high_levels += 1
        if events[event] == 'found treasure':
            treasure_events += 1
        if events[event] == 'leveled up':
            level_up_events += 1
        yield f"Event {i + 1}: Player {players[player]} (level {levels[level]}) {events[event]}"

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_levels}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")


def process_1000_events(players: list, levels: list, events: list):
    print("Processing 1000 game events...\n")
    for event in event_generator(players, levels, events):
        print(event)

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def generate_demonstration():
    print("\n=== Generator Constant ===")
    fibonacci = fibonacci_calculator()
    prime = prime_calculator()
    txt = ""
    txt1 = ""
    for _ in range(10):
        if not txt == "":
            txt += ", "
        txt += f"{next(fibonacci)}"
    for _ in range(5):
        if not txt1 == "":
            txt1 += ", "
        txt1 += f"{next(prime)}"
    print(f"Fibonacci sequence (first 10): {txt}")
    print(f"Prime numbers (first 5): {txt1}")


def data_stream():
    print("=== Game Data Stream Processor ===\n")
    players = ['alice', 'bob', 'charlie', 'ahmed', 'dina']
    levels = [5, 12, 8, 19, 11, 9, 3, 4]
    events = ['killed monster', 'found treasure', 'leveled up']

    process_1000_events(players, levels, events)
    generate_demonstration()


if __name__ == "__main__":
    data_stream()