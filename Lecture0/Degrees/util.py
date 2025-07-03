from collections import deque
from typing import List, Tuple

class SearchFrontier:
    def __init__(self, start_id):
        self.queue = deque([start_id])
        self.nodes = {start_id: Node(start_id, None, None)}
        self.visited = {start_id}

    def contains(self, person_id):
        return person_id in self.visited

    def add(self, person_id, parent, movie_id):
        self.queue.append(person_id)
        self.nodes[person_id] = Node(person_id, parent, movie_id)
        self.visited.add(person_id)

    def pop(self):
        return self.queue.popleft()

    def __len__(self):
        return len(self.queue)
    
    def build_path_to(self, meeting_node: int, forward: bool) -> List[Tuple[int, int]]:
        path = []
        node = self.nodes[meeting_node]

        while node.parent is not None:
            person_id = node.state if forward else node.parent.state
            path.append((node.action, person_id))
            node = node.parent

        return path[::-1] if forward else path


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
