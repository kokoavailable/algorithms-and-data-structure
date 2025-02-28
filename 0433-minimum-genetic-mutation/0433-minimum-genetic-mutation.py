class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        visited = set()
        visited.add(startGene)
        queue = deque([(startGene, 0)])

        while queue:
            current_gene, steps = queue.popleft()
            if current_gene == endGene:
                return steps

            for i in range(8):
                for c in ['A', 'C', 'G', 'T']:
                    if current_gene[i] == c:
                        continue

                    new_gene = current_gene[:i] + c + current_gene[i+1:]
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))

        return -1
