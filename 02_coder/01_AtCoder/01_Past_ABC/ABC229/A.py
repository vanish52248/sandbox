# 2 行 2 列のグリッドを表す文字列
grid_strings = ["##.", ".##"]

# 黒マスを表す文字
BLACK_CELL = "#"

# 白マスを表す文字
WHITE_CELL = "."

# 頂点のリスト
vertices = []

# 辺のリスト
edges = []

# 文字列からグラフを構築する
for i in range(len(grid_strings)):
  for j in range(len(grid_strings[i])):
    # 文字が黒マスを表す文字である場合
    if grid_strings[i][j] == BLACK_CELL:
      # 頂点を追加
      vertices.append((i, j))

      # 上下左右に隣接する頂点が存在するか調べる
      for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # 隣接する頂点が存在する場合
        if (i + di, j + dj) in vertices:
          # 辺を追加
          edges.append(((i, j), (i + di, j + dj)))

# 連通グラフかどうかを判定する
is_connected = True

# 各頂
print(is_connected)
