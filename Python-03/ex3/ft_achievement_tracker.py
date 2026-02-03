def achievement_tracker():
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")
    unique_achieves = bob.union(alice, charlie)
    print(f"All unique achievements: {unique_achieves}")
    print(f"Total unique achievements: {len(unique_achieves)}\n")

    common_achieves = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_achieves}")

    rare_achieves = set()
    for achieve in unique_achieves:
        count = 0
        if achieve in alice:
            count += 1
        if achieve in bob:
            count += 1
        if achieve in charlie:
            count += 1

        if count == 1:
            rare_achieves.add(achieve)
    print(f"Rare achievements (1 player): {rare_achieves}\n")

    common_alice_bob = alice.intersection(bob)
    print(f"Alice vs Bob common: {common_alice_bob}")
    unique_alice = alice.difference(bob)
    print(f"Alice unique: {unique_alice}")
    unique_bob = bob.difference(alice)
    print(f"Bob Unique: {unique_bob}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievement_tracker()
