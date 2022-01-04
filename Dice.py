def dice():
    import random
    n = random.randint(1, 6)
    print("Rolling...")
    import time
    time.sleep(2)
    print("The dice has rolled a", n)