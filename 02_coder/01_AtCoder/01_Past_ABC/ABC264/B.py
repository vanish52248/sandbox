r, c = map(int, input().split())

lst = [
    "bbbbbbbbbbbbbbb",
     "bwwwwwwwwwwwwwb",
     "bwbbbbbbbbbbbwb",
     "bwbwwwwwwwwwbwb",
     "bwbwbbbbbbbwbwb",
     "bwbwbwwwwwbwbwb",
     "bwbwbwbbbwbwbwb",
     "bwbwbwbwbwbwbwb",
     "bwbwbwbbbwbwbwb",
     "bwbwbwwwwwbwbwb",
     "bwbwbbbbbbbwbwb",
     "bwbwwwwwwwwwbwb",
     "bwbbbbbbbbbbbwb",
     "bwwwwwwwwwwwwwb",
     "bbbbbbbbbbbbbbb"
]
 
print("black" if lst[r-1][c-1] == "b" else "white")
