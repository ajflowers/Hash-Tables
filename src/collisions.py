import random

def how_many_before_collision(buckets, loops=1):
    """
    Roll random hash indexes into buckets and print how many
    rolls it takes before a collision

    run loops times
    """
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            tries += 1
            if hash_index not in tried:
                tried.add(hash_index)                
            else:
                #we have found a collision
                break
        print(f"{buckets} buckets, {tries} hashes before collision, ({tries/buckets * 100:.1f}%)")

how_many_before_collision(1000,10)