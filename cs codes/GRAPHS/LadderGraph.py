import math
from Graph import Graph
from valid_ladders_word_list import get_valid_word_list

class LadderGraph(Graph):
    def __init__(self, word_list:list[str]):
        adj_list = self.build_adj_list(word_list)
        super().__init__(adj_list)
        ### No changes needed. The Graph constructor takes care of everything else.

    def hamming_distance(self, w1:str, w2:str)-> int:
        '''Determines the hamming distance between two words
        
        Args:
            w1 (str): A word
            w2 (str): A word
            
        Returns:
            int: The number of characters that differ between w1 and w2
        '''
        ### BEGIN SOLUTION

        ham = 0

        l1 = len(w1)
        l2 = len(w2)
        if l1 != l2:
            return -1
        for i in range(l1):
          if w1[i] != w2[i]:
            ham +=1
        return ham

        ### END SOLUTION

    def build_adj_list(self, word_list: list[str])-> dict[str, set[str]]:
        '''Builds an adjacency list modeling a graph where nodes are all words
           with the same length, and edges connect words that differ by exactly 1 letter

        Args:
            word_list (list[str]): A list of words

        Returns:
            dict[str, set[str]]: An adjacency list representation of the graph
        '''
        ### BEGIN SOLUTION

        adj = dict()
        for word in word_list:
           word = word.lower()# they're all lowercase in valid word list
           adj[word] = set()
           for compare in word_list:
              compare = compare.lower()
              dis = self.hamming_distance(word, compare)
              if dis == 1:
                 adj[word].add(compare)

        return adj
   
        ### END SOLUTION

    def is_valid_word(self, word:str) -> bool:
        '''Determines whether a word is present in the graph

        Args:
            word (str): A word

        Returns:
            bool: True if the word is in the graph, otherwise False
        '''       
        ### BEGIN SOLUTION

        return self.is_vertex(word.lower())

        ### END SOLUTION

    def is_valid_ladder(self, ladder:tuple[str]) -> bool:
      ''' Determines whether a given ladder is a valid path on the graph

          Args:
            ladder : A list of path vertices

          Returns:
            bool - True if the given path is a valid path on the Graph, otherwise False
      '''
      ### BEGIN SOLUTION

      l = []
      for word in ladder:
        l.append(word.lower())
      return len(ladder)>1 and self.is_valid_path(tuple(l))
    
      ### END SOLUTION

    def get_rung_length(self, ladder:tuple[str]) -> int:
        ''' Finds the number of rungs in the word ladder.

          Args:
            ladder (tuple[str]): a tuple of str representing a word ladder

          Returns:
            int - the number of rungs in a valid word ladder. Invalid word ladders return -1
        '''
        ### BEGIN SOLUTION

        if self.is_valid_ladder(ladder):
          return len(ladder)-2
        return -1
 
        ### END SOLUTION

    def get_shortest_ladder(self, start:str, target:str) -> tuple[str]:
        '''Finds a shortest ladder connecting the start vertex with the target vertex.

          Args:
            start (str): the starting vertex in the path
            target (str): the last vertex in the path

          Returns:
            tuple[str] - a tuple representing a word ladder connecting start and target
        '''
        ### BEGIN SOLUTION

        start = start.lower()
        target = target.lower()
        if self.is_valid_word(start) and self.is_valid_word(target) and len(start) == len(target)and start != target:
          return self.get_shortest_bfs_path(start,target)
        else:
          return tuple()

        ### END SOLUTION

    def get_all_shortest_ladders(self, start:str, target:str) -> set[tuple[str]]:
        ''' Finds all of the shortests ladders connecting the start vertex with the target vertex.

          Args:
            start (str): the starting vertex in the path
            target (str): the last vertex in the path

          Returns:
            set - a set of the shortests paths from start to target
        '''
        ### BEGIN SOLUTION
        start = start.lower()
        target = target.lower()
        if self.is_valid_word(start) and self.is_valid_word(target) and len(start) == len(target) and start != target:
            return self.get_all_shortest_bfs_paths(start,target)
        else:
            return set()

        ### END SOLUTION
    
    def get_all_ladders(self, start:str, target:str, max_rungs=math.inf) -> set[tuple[str]]:
        ''' Finds all of the shortests paths connecting the start vertex with the target vertex.

          Args:
            start (str): the starting vertex in the path
            target (str): the last vertex in the path
            max_rungs (int): the maximum number of rungs to consider

          Returns:
            set[tuple[str]]] - a set of tuples representing word ladders conecting start and target
        '''
        ### BEGIN SOLUTION

        ### END SOLUTION

if __name__ == "__main__":
  small_dictionary=["foul","fool","cool","pool","poll","pole","pope","pale","sale", "sage", "page", "pall", "fall", "fail", "foil"]
  myLadderGraph = LadderGraph(small_dictionary)

  #word_length = 4
  #big_dictionary = [w for w in get_valid_word_list() if len(w) == word_length] 
  #myLadderGraph = LadderGraph(big_dictionary)
  
  print("Vertices:", myLadderGraph.vertices)
  print("Edges:", myLadderGraph.edges)  
  print()

  valid_vertex = "foil"
  invalid_vertex = "ffff"
  print(f"Neighbers ({valid_vertex}):", myLadderGraph.get_neighbors(valid_vertex))
  print(f"Valid word ({valid_vertex}):", myLadderGraph.is_valid_word(valid_vertex))
  print(f"Invalid word ({invalid_vertex}):", myLadderGraph.is_valid_word(invalid_vertex))
  print()

  good_ladder=('fool', 'pool', 'poll', 'pall', 'pale', 'page', 'sage')
  bad_ladder=('fool', 'pool', 'pall', 'pale', 'page', 'sage')
  print(f"Valid Path {good_ladder}:", myLadderGraph.is_valid_ladder(good_ladder))
  print(f"Valid Path Rung Length {good_ladder}:", myLadderGraph.get_rung_length(good_ladder))
  print(f"Invalid Path {bad_ladder}:", myLadderGraph.is_valid_ladder(bad_ladder))
  print(f"Invalid Path Rung Length {bad_ladder}:", myLadderGraph.get_rung_length(bad_ladder))
  print()
  
  start = "foul"
  target= "sage"
  print(f"Shortest ladder from {start} to {target}", myLadderGraph.get_shortest_ladder(start, target))
  print()
  all_shortest_ladders = myLadderGraph.get_all_shortest_ladders(start, target)
  print(f"All {len(all_shortest_ladders)} Shortest Ladders from {start} to {target}", all_shortest_ladders)
  print()
  max_rung_length = 6
  all_ladders = myLadderGraph.get_all_ladders(start, target, max_rung_length )
  print(f"All {len(all_ladders)} Ladders with a max length of {max_rung_length} from {start} to {target}", all_ladders)