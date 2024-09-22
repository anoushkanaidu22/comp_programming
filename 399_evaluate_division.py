from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_dict = {}
        for i in range(len(equations)):
            x,y = equations[i]
            if x not in adj_dict:
                adj_dict[x] = {}
            adj_dict[x][y] = values[i]
            if y not in adj_dict:
                adj_dict[y] = {}
            adj_dict[y][x] = 1/(values[i])

        results = []

        for query in queries:
            a,target = query
            added = False
            if (a not in adj_dict) or (target not in adj_dict):
                results.append(float(-1))
                added = True

            queue = deque()
            queue.append((a,a,1))
            seen = set()
            seen.add((a,a))

            while (queue and not added):
                i,j,prod = queue.pop()
                if j == target:
                    adj_dict[a][target] = prod
                    adj_dict[target][a] = float(1) / (prod)
                    results.append(prod)
                    added = True
                    break
                else:
                    for x in adj_dict[j]:
                        new_prod = adj_dict[j][x] * prod
                        adj_dict[a][x] = new_prod
                        adj_dict[x][a] = 1/new_prod
                        if (j,x) not in seen:
                            queue.append((j,x, new_prod))
                            seen.add((j,x))
            if not added:
                results.append(float(-1))

        return results

