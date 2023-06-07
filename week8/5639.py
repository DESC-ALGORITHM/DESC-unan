import sys

tree = {}

def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')
    

# 마지막 node안에 숫자보다 작으면, 완쪽 노드임.
def compare():
    return None
# 마지막 node 안에 숫자보다 크면, 부모 노드의 오른쪽 노드임.
# 2개 전 index의 오른쪽 node
while True:
    N = int(input())