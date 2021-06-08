class State:
	def __init__(self, data, level, fval):
		self.data = data
		self.level = level
		self.fval = fval

	def gen_child_state(self):
		x, y = self.find(self.data, '_')
		move_list = [[x, y-1], [x+1, y], [x, y+1], [x-1, y]]
		children = []
		for i in move_list:
			child = self.move(self.data, x, y, i[0], i[1])
			if child is not None:
				child_state = State(child, self.level + 1, 0)
				children.append(child_state)
		return children

	def move(self, st, x1, y1, x2, y2):
		if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
			temp = []
			temp = self.copy(st)
			temp_val = temp[x2][y2]
			temp[x2][y2] = temp[x1][y1]
			temp[x1][y1] = temp_val
			return temp
		else:
			return None

	def copy(self, root):
		temp = []
		for i in root:
			t = []
			for j in i:
				t.append(j)
			temp.append(t)
		return temp

	def find(self, st, x):
		for i in range(0, len(self.data)):
			for j in range(0, len(self.data)):
				if st[i][j] == x:
					return i,j

class Board:
	def __init__(self):
		self.n = 3
		self.start = []
		self.goal = []

	def accept(self):
		p = []
		for i in range(0, self.n):
			temp = input().split(" ")
			p.append(temp)
		return p

	def generate(self):
		# print("Enter the start state matrix")
		self.start = self.accept()
		# self.start = [[1, 2, 3], ['_', 4, 6], [7, 5, 8]]
		# print("Enter the goal state matrix")
		self.goal = self.accept()
		# self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, '_']]

	def run(self):
		self.generate()
		a = AStar()
		a.astar(self.start, self.goal)
		b = BFS()
		b.bfs(self.start, self.goal)

class AStar:
	def __init__(self):
		self.n = 3
		self.open = []
		self.closed = []

	def f(self, start, goal):
		return self.h(start.data, goal)+start.level

	def h(self, start, goal):
		temp = 0
		for i in range(0,self.n):
			for j in range(0,self.n):
				if start[i][j] != goal[i][j] and start[i][j] != '_':
					temp += 1
		return temp

	def astar(self, start, goal):
		print("astar: ")
		start = State(start, 0, 0)
		start.fval = self.f(start, goal)
		self.open.append(start)

		moves = 0
		while True:
			moves += 1
			cur = self.open[0]
			print("")
			print("  | ")
			print("  | ")
			print(" \\\'/ \n")
			for i in cur.data:
				for j in i:
					print(j,end=" ")
				print("")
			if(self.h(cur.data,goal) == 0):
				print("cost:", moves, "// generated states:", len(self.closed)+len(self.open))
				break
			for i in cur.gen_child_state():
				i.fval = self.f(i,goal)
				self.open.append(i)
			self.closed.append(cur)
			del self.open[0]

			""" sort the opne list based on f value """
			self.open.sort(key = lambda x:x.fval,reverse=False)

class BFS:
	def __init__(self):
		self.n = 3

	def bfs(self, start, goal):
		print("\nBFS: ")
		level = 0
		start = State(start, 0, 0)
		queue = []
		gen_state_list = []
		queue.append(start)
		gen_state_list.append(start.data)

		moves = 0
		while queue:
			moves += 1
			cur = queue.pop(0)
			print("")
			print("  | ")
			print("  | ")
			print(" \\\'/ \n")
			for i in cur.data:
				for j in i:
					print(j,end=" ")
				print("")

			if cur.data == goal:
				print("cost:", moves, "// generated states:", len(gen_state_list))
				break

			for i in cur.gen_child_state():
				if i.data not in gen_state_list:
					queue.append(i)
					gen_state_list.append(i.data)

def main():
	board = Board()
	board.run()

main()