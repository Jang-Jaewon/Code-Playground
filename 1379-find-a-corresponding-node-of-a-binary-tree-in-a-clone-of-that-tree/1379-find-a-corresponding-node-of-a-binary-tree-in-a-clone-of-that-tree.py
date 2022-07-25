# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned == None:
            return None

        queue = [cloned]
        result = None
		#the loop will run until the list 'queue' will has the objects:
		
        while len(queue) > 0:
			#We get and remove object from the list:
            current = queue.pop(0)
			#if the object's value equal the target, we return this object:
            if current.val == target.val:
                result = current
            else:
				#We add to the list a left part of the tree if it's not null:
                if current.left != None:
                    queue.append(current.left)
				#We add to the list a right part of the tree if it's not null:
                if current.right != None:
                    queue.append(current.right)
        return result   