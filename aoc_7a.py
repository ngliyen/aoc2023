# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
from typing import List


def winnings(filepath: str) -> int:
    rank_map = {
        "five of a kind": [],
        "four of a kind": [],
        "full house": [],
        "three of a kind": [],
        "two pair": [],
        "one pair": [],
        "high card": []
    }

    with open(filepath) as file:
        games = [line.rstrip() for line in file]

    for game in games:
        game_details = game.split(" ")
        hand = game_details[0]
        bid = game_details[1]
        htype = hand_type(hand)
        rank_by_type = rank_map.get(htype)
        if len(rank_by_type) == 0:
            rank_by_type.append((hand, bid))
        else:
            idx = insert_game(hand, 0, len(rank_by_type)-1, rank_by_type)
            rank_by_type.insert(idx, (hand, bid))

    # create ranked games
    games_ranked = []
    games_ranked.extend(rank_map.get("five of a kind"))
    games_ranked.extend(rank_map.get("four of a kind"))
    games_ranked.extend(rank_map.get("full house"))
    games_ranked.extend(rank_map.get("three of a kind"))
    games_ranked.extend(rank_map.get("two pair"))
    games_ranked.extend(rank_map.get("one pair"))
    games_ranked.extend(rank_map.get("high card"))
    print(games_ranked)
    score = 0
    rank = len(games_ranked)
    for i in range(len(games_ranked)):
        score += int(games_ranked[i][1]) * rank
        rank -= 1
    return score

def hand_type(s: str) -> str:
    hand_map = dict()
    for char in s:
        if hand_map.get(char) is None:
            hand_map[char] = 1
        else:
            hand_map[char] += 1

    # get frequency in map
    frequency = list(hand_map.values())

    if len(frequency) == 1 and frequency[0] == 5:
        return "five of a kind"
    elif len(frequency) == 2 and 4 in frequency:
        return "four of a kind"
    elif len(frequency) == 2 and 3 in frequency and 2 in frequency:
        return "full house"
    elif len(frequency) == 3 and 3 in frequency and 2 not in frequency:
        return "three of a kind"
    elif len(frequency) == 3 and 2 in frequency and 1 in frequency:
        return "two pair"
    elif len(frequency) == 4 and 2 in frequency and 1 in frequency:
        return "one pair"
    elif len(frequency) == 5:
        return "high card"

def insert_game(hand: str, start: int, end: int, games: List[tuple]) -> int:
    mid = (start + end) // 2

    if mid == len(games) - 1 and not is_stronger(hand, games[mid][0]):
        return mid + 1
    elif mid == 0 and is_stronger(hand, games[mid][0]):
        return mid
    elif not is_stronger(hand, games[mid][0]) and is_stronger(hand, games[mid+1][0]):
        return mid + 1
    elif is_stronger(hand, games[mid][0]):
        return insert_game(hand, start, mid-1, games)
    else:
        return insert_game(hand, mid+1, end, games)
def insert_game_to_type(hand: str, bid: int, games: List[tuple]) -> None:
    if len(games) == 0 or not is_stronger(hand, games[-1][0]):
        games.append((hand, bid))
        return

    elif is_stronger(hand, games[0][0]):
        games.insert(0,(hand, bid))
        return

    for i in range(len(games)-1):
        if not is_stronger(hand,games[i][0]) and is_stronger(hand, games[i+1][0]):
            games.insert(i+1, (hand, bid))

# returns if a is stronger than b
def is_stronger(a: str, b: str) -> int:
    strength_map = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1
    }

    for i in range(len(a)):
        if strength_map[a[i]] > strength_map[b[i]]:
            return True
        elif strength_map[a[i]] < strength_map[b[i]]:
            return False

print(winnings("input/day7.txt"))