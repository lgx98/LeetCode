# @before-stub-for-debug-begin
from python3problem297 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        buf = []

        def enc_helper(root: Optional[TreeNode]):
            nonlocal buf
            num = root.val+1024 +\
                ((1 << 15) if root.left else 0) +\
                ((1 << 14) if root.right else 0)
            buf += [num & 0xFF, num >> 8]
            if root.left:
                enc_helper(root.left)
            if root.right:
                enc_helper(root.right)

        enc_helper(root)
        return bytes(buf).decode(encoding='IBM437')

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        get_node = ((lo+((hi & 0x3F) << 8)-1024, hi & 0x80, hi & 0x40)
                    for lo, hi in zip(*[iter(data.encode(encoding='IBM437'))]*2))

        def dec_helper() -> TreeNode:
            val, has_l, has_r = next(get_node)
            ret = TreeNode(val)
            ret.left = dec_helper() if has_l else None
            ret.right = dec_helper() if has_r else None
            return ret

        return dec_helper()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
