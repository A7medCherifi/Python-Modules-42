import sys


def process_arguments():
    list_score = []
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            i = 1
            try:
                while i < len(sys.argv):
                    score = int(sys.argv[i])
                    list_score.append(score)
                    i += 1
            except ValueError:
                print(
                    f"Nasty Nasty. YOU did '{sys.argv[i]}' instead of Number!")
                return

            print(f"Scores processed: {list_score}")
            print(f"Total players: {len(list_score)}")
            print(f"Total score {sum(list_score)}")
            average = sum(list_score) / len(list_score)
            print(f"Average score: {average}")
            print(f"High score: {max(list_score)}")
            print(f"Low score: {min(list_score)}")
            range_score = max(list_score) - min(list_score)
            print(f"Score range: {range_score}\n")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    process_arguments()
