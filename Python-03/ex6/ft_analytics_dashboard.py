def lis_comprehension(players: list) -> None:
    print("=== List Comprehension Dashboard ===")
    high_scores = [value['name'] for value in players if value['score'] > 2000]
    scores_double = [value['score'] * 2 for value in players]
    active_players = [value['name'] for value in players if value['active']]

    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_double}")
    print(f"Active players: {active_players}")


def dict_comprehension(players: list) -> None:
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {value['name']: value['score'] for value in players}
    score_category = {
        "high": sum(1 for value in players if value['score'] > 2000),
        "medium": sum(1 for value in players if 1900 < value["score"] <= 2150),
        "low": sum(1 for value in players if value['score'] <= 1900)
    }
    count_ach = {
        value['name']: len(value['achievements']) for value in players
    }

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_category}")
    print(f"Achievement counts: {count_ach}")


def set_comprehension(players: list) -> None:
    print("\n=== Set Comprehension Examples ===")
    unique_players = {value['name'] for value in players}
    first_ach = set()
    for ach in players:
        if ach['name'] == "alice":
            first_ach = ach['achievements']
    ach = {
        ach for value in players
        if not value['name'] == "alice" for ach in value['achievements']
    }
    unique_ach = first_ach.difference(ach)
    active_regions = {value['region'] for value in players if value['active']}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_ach}")
    print(f"Active regions: {active_regions}")


def combined_analysis(players: list) -> None:
    print("\n=== Combined Analysis ===")
    total_players = sum(1 for _ in players)
    total_unique_ach = len({
        ach for value in players for ach in value['achievements']
    })
    len_num = len(players)
    sum_num = sum(value['score'] for value in players)
    average_num = sum_num / len_num
    max_score = max(value['score'] for value in players)
    top_performer = None
    for value in players:
        if value['score'] == max_score:
            top_performer = value
            break

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {average_num}")
    print(f"Top performer: {top_performer['name']} ({top_performer['score']} "
          f"points, {len(value['achievements'])} achievements)")


def analytics_dashboard() -> None:
    print("=== Game Analytics Dashboard ===\n")
    players = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": {
                "first_kill",
                "boss_slayer",
                "level_10",
                "legendary_warrior",
                "perfectionist"
            },
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": {
                "treasure_hunter",
                "dragon_slayer",
                "speed_master"
            },
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": {
                "speed_master",
                "treasure_hunter",
                "legendary_warrior",
                "explorer",
                "first_blood",
                "collector",
                "perfectionist"
            },
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "region": "west",
            "achievements": {
                "speed_demon",
                "collector",
            }
        }
    ]

    try:
        lis_comprehension(players)
        dict_comprehension(players)
        set_comprehension(players)
        combined_analysis(players)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    analytics_dashboard()
