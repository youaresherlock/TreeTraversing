# -*- coding: utf-8 -*-
# @Author: xiweibo
# @Date:   2018-08-21 12:26:38
# @Last Modified by:   xiweibo
# @Last Modified time: 2018-08-21 15:16:31
"""
其实我们在学习图论或者图相关的算法的时候会遇到两个基本的算法，
深度优先遍历和广度优先遍历，在树中，前序遍历类似于深度优先遍历，
后序遍历类似于广度优先遍历，而一般通常使用栈来实现深度，队列实现广度。
我们可以使用递归或者非递归的方法实现。

将使用Python实现树的构造和几种遍历算法
树的构造
递归实现先序遍历、中序遍历、后序遍历
非递归实现先序遍历，中序遍历，后序遍历
队列实现层次遍历
"""

class Node(object):
	""" 节点类 """
	def __init__(self, elem = -1, lchild = None, rchild = None):
		self.elem = elem # 是节点的data,如果是-1表示为空节点
		self.lchild = lchild
		self.rchild = rchild

class Tree(object):
	""" 树类 """
	def __init__(self):
		self.root = Node()
		self.myQueue = []

	def add(self, elem):
		""" 为树添加节点 是按照层次遍历来插入的，队列中的是子节点没有满的节点的层次遍历 """
		node = Node(elem)
		# 如果树是空的，则对根节点赋值，赋值之后树一直不为空
		if self.root.elem == -1: 
			self.root = node
			self.myQueue.append(self.root)
		else:
			"""
			此节点的子树没有齐，在此节点上插入左右子节点
			"""
			treeNode = self.myQueue[0] 
			if treeNode.lchild == None:
				treeNode.lchild = node
				self.myQueue.append(treeNode.lchild)
			elif treeNode.rchild == None:
				treeNode.rchild = node
				self.myQueue.append(treeNode.rchild)
				# 删除已经有左右子节点的节点
				self.myQueue.pop(0)

	def preorder_recursive(self, root):
		""" 利用递归的先序遍历 根左右"""
		if root == None:
			return 
		print root.elem # 打印出先序节点的值
		self.preorder_recursive(root.lchild)
		self.preorder_recursive(root.rchild)

	def miorder_recursive(self, root):
		""" 利用递归的中序遍历 左根右 """
		if root == None:
			return 
		self.miorder_recursive(root.lchild)
		print root.elem # 打印出根的值
		self.miorder_recursive(root.rchild)

	def laterorder_recursive(self, root):
		""" 利用递归的后序遍历 左右根 """
		if root == None:
			return 
		self.laterorder_recursive(root.lchild)
		self.laterorder_recursive(root.rchild)
		print root.elem #打印出沿途的值

	def preorder_stack(self, root):
		""" 利用堆栈实现先序遍历 """
		if root == None:
			return
		myStack = []
		node = root
		while node or myStack:
			while node:
				print node.elem
				myStack.append(node) #将沿途的最左节点打印出来并按顺序入队
				node = node.lchild
			node = myStack.pop() 
			node = node.rchild # 将根左的左右节点重新来进行先序遍历，同时队列不断加入最左节点

	def miorder_stack(self, root):
		""" 利用堆栈实现中序遍历 """
		if root == None:
			return 
		myStack = []
		node = root
		while node or myStack:
			while node:
				myStack.append(node)
				node = node.lchild
			node = myStack.pop()
			print node.elem
			node = node.rchild

	def laterorder_stack(self, root):
		""" 
		利用两个栈实现后序遍历 左右根
		"""
		
		if root == None:
			return 
		myStack1 = []
		myStack2 = []
		node = root
		myStack1.append(node)
		while myStack1:
			node = myStack1.pop() # 弹出顺序是根右左
			if node.lchild:
				myStack1.append(node.lchild) #加入顺序是左右，弹出顺序就是右左
			if node.rchild:
				myStack1.append(node.rchild)
			myStack2.append(node) # 与Stack1弹出顺序一致

		while myStack2:
			print myStack2.pop().elem


	def level_queue(self, root):
		"""
		利用队列实现层次遍历
		"""
		if root == None:
			return
		myQueue = []
		node = root
		myQueue.append(node)
		while myQueue:
			# 先进先出，pop第一个元素，pop默认是弹出最后一个元素
			node = myQueue.pop(0)
			print node.elem
			if node.lchild != None:
				myQueue.append(node.lchild)
			if node.rchild != None:
				myQueue.append(node.rchild)


if __name__ == '__main__':
    """主函数"""
    elems = range(10)           #生成十个数据作为树节点
    tree = Tree()          #新建一个树对象
    for elem in elems:                  
        tree.add(elem)           #逐个添加树的节点

    print '队列实现层次遍历:'
    tree.level_queue(tree.root)

    print '\n\n递归实现先序遍历:'
    tree.preorder_recursive(tree.root)
    print '\n递归实现中序遍历:' 
    tree.miorder_recursive(tree.root)
    print '\n递归实现后序遍历:'
    tree.laterorder_recursive(tree.root)

    print '\n\n堆栈实现先序遍历:'
    tree.preorder_stack(tree.root)
    print '\n堆栈实现中序遍历:'
    tree.miorder_stack(tree.root)
    print '\n堆栈实现后序遍历:'
    tree.laterorder_stack(tree.root)



"""
执行结果:
队列实现层次遍历:
0
1
2
3
4
5
6
7
8
9


递归实现先序遍历:
0
1
3
7
8
4
9
2
5
6

递归实现中序遍历:
7
3
8
1
9
4
0
5
2
6

递归实现后序遍历:
7
8
3
9
4
1
5
6
2
0


堆栈实现先序遍历:
0
1
3
7
8
4
9
2
5
6

堆栈实现中序遍历:
7
3
8
1
9
4
0
5
2
6

堆栈实现后序遍历:
7
8
3
9
4
1
5
6
2
0
[Finished in 0.1s]
"""


















