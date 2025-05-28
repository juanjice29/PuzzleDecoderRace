
from collections import defaultdict

class Checker:
    def __init__(self, name: str):
        self.fragmentos = defaultdict(str)
        self.indices_encontrados = set()
    
    def add_pieza(self, index, text):
        if index not in self.fragmentos:
            self.fragmentos[index] = text
            self.indices_encontrados.add(index)
            return True
        return False

    def check(self):
        if not self.fragmentos:
            return False
        
        max_index = max(self.fragmentos.keys())
        return len(self.fragmentos) == max_index + 1
    
    def armar(self):
        srtd_fragmentos = [self.fragmentos[i] for i in sorted(self.fragmentos.keys())]
        return ''.join(srtd_fragmentos)

   