from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = lambda: stdin.readline().rstrip()

def get_pre(ins, ine, posts, poste):
    if ins > ine or posts > poste:
        return
    
    if ins == ine or posts == poste:
        preorder.append(inorder[ins])
        return
    
    r = postorder[poste]
    preorder.append(r)
    r_idx = indices[r]

    get_pre(ins, r_idx - 1, posts, posts + r_idx - 1 - ins)
    get_pre(r_idx + 1, ine, posts + r_idx - 1 - ins + 1, poste - 1)
    return


N = int(input())
inorder = list(map(int, input().split()))
indices = {inorder[i]: i for i in range(N)}
postorder = list(map(int, input().split()))
preorder = []

get_pre(0, N - 1, 0, N - 1)
print(' '.join((map(str, preorder))))