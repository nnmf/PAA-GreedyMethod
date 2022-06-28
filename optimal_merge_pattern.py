# Python Program to implement
# Optimal File Merge Pattern


class Heap():
	# Building own implementation of Min Heap
	def __init__(self):

		self.h = []

	def parent(self, index):
		# Returns parent index for given index

		if index > 0:
			return (index - 1) // 2

	def lchild(self, index):
		# Returns left child index for given index

		return (2 * index) + 1

	def rchild(self, index):
		# Returns right child index for given index

		return (2 * index) + 2

	def addItem(self, item):

		# Function to add an item to heap
		self.h.append(item)

		if len(self.h) == 1:

			# If heap has only one item no need to heapify
			return

		index = len(self.h) - 1
		parent = self.parent(index)

		# Moves the item up if it is smaller than the parent
		while index > 0 and item < self.h[parent]:
			self.h[index], self.h[parent] = self.h[parent], self.h[parent]
			index = parent
			parent = self.parent(index)

	def deleteItem(self):

		# Function to add an item to heap
		length = len(self.h)
		self.h[0], self.h[length-1] = self.h[length-1], self.h[0]
		deleted = self.h.pop()

		# Since root will be violating heap property
		# Call moveDownHeapify() to restore heap property
		self.moveDownHeapify(0)

		return deleted

	def moveDownHeapify(self, index):

		# Function to make the items follow Heap property
		# Compares the value with the children and moves item down

		lc, rc = self.lchild(index), self.rchild(index)
		length, smallest = len(self.h), index

		if lc < length and self.h[lc] <= self.h[smallest]:
			smallest = lc

		if rc < length and self.h[rc] <= self.h[smallest]:
			smallest = rc

		if smallest != index:
			# Swaps the parent node with the smaller child
			self.h[smallest], self.h[index] = self.h[index], self.h[smallest]

			# Recursive call to compare next subtree
			self.moveDownHeapify(smallest)

	def increaseItem(self, index, value):
		# Increase the value of 'index' to 'value'

		if value <= self.h[index]:
			return

		self.h[index] = value
		self.moveDownHeapify(index)


class OptimalMergePattern():
	def __init__(self, n, items):

		self.n = n
		self.items = items
		self.heap = Heap()

	def optimalMerge(self):

		# Corner cases if list has no more than 1 item
		if self.n <= 0:
			return 0

		if self.n == 1:
			return self.items[0]

		# Insert items into min heap
		for _ in self.items:
			self.heap.addItem(_)

		count = 0
		while len(self.heap.h) != 1:
			tmp = self.heap.deleteItem()
			count += (tmp + self.heap.h[0])
			self.heap.increaseItem(0, tmp + self.heap.h[0])

		return count


def optimaMergePatern():
	OMP = OptimalMergePattern(6, [2, 3, 4, 5, 6, 7])
	ans = OMP.optimalMerge()
	print(ans)

	##https://www.youtube.com/watch?v=HHIc5JZyenI
	##https://www.geeksforgeeks.org/optimal-file-merge-patterns/

