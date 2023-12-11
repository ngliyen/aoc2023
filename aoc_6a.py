from typing import List


def beat_record(times: List[int], distance: List[int]) -> int:
    num_ways = 1
    for i in range(len(times)):
        num_ways *= win_race(times[i], distance[i])
    return num_ways

# calculate number of ways to win race
def win_race(time: int, min_distance: int) -> int:
    num_ways = 0
    for i in range(1, time):
        distance = i * (time-i)
        if distance > min_distance:
            num_ways +=1
    return num_ways


print(beat_record([7,15,30], [9,40,200]))
print(beat_record([55,82,64,90], [246,1441,1012,1111]))
print(beat_record([71530],[940200]))
print(beat_record([55826490], [246144110121111]))

