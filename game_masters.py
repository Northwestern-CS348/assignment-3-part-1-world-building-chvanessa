from logical_classes import *
from kb_and_inference_engine import *
from read import *
from abc import ABC, abstractmethod
import os

class GameMaster(ABC):

    TXTS_DIRECTORY_PATH='flatfiles'

    def __init__(self):
        self.kb = KnowledgeBase([], [])
        self.moveableQuery = self.produceMovableQuery()

    @abstractmethod
    def produceMovableQuery(self):
        raise NotImplementedError('Subclasses must override produceMovableQuery() '\
            'to provide the query for facts starting with MOVABLE predicate')

    def getMovables(self):        
        listOfBindings = self.kb.kb_ask(self.moveableQuery)
        if listOfBindings:
            return [instantiate(self.moveableQuery.statement,bindings)\
                     for bindings in listOfBindings]
        else:
            return listOfBindings

    def read(self, file_name, path=TXTS_DIRECTORY_PATH):
        final_path = os.path.join(path, file_name)
        for fr in read_tokenize(final_path):
            self.kb.kb_assert(fr)

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()
        
    def produceMovableQuery(self):
        return parse_input('fact: (movable ?disk ?init ?target)')

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')


