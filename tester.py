def minmax(self, node, alpha, beta, im_max, depth):
        if node.is_end():
            return int(node.comment)
        pointer = None
        if im_max:
            value = GLOBAL_MIN
            for child in node.variations:
                res = self.minmax(child, alpha, beta, False, depth + 1)
                if res > value:
                    value = res
                    pointer = child
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            if depth == 0:
                return pointer
            else:
                return value
        else:
            value = GLOBAL_MAX
            for child in node.variations:
                res  = self.minmax(child, alpha, beta, True, depth + 1)
                if res < value:
                    value = res
                    pointer = child
                beta = min(beta, value)
                if beta <= alpha:
                    break
            if depth == 0:
                return pointer
            else:
                return value
