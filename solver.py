from checker import Checker
from config import Config
import time
from fragment import Fragment
import asyncio

class Solver:
    def __init__(self):
        self.config = Config()
        self.checker =Checker()
        self.start_time = time.time()
        self.completed = False
        self.paralell_requests = 10
        self.found_ids = set()

    async def get_fragment(self, frag, id):
        if self.completed:
            return

        data = await frag.get(id)
        if data and not self.completed:
            index = data["index"]
            text = data["text"]
            
            if self.checker.add_pieza(index, text):
                if self.checker.check():
                    await self.print_solver()
                    self.completed = True

    async def solve(self):
        current_id=1
        async with Fragment() as fragment:
            while not self.completed:
                tasks = []
                for id in range(current_id, current_id + self.paralell_requests):
                    task = asyncio.create_task(self.get_fragment(fragment, id))
                    tasks.append(task)
                print("piezas a solicitar"+ str(current_id) + " a " + str(current_id + self.paralell_requests - 1))
                await asyncio.gather(*tasks)

                if not self.completed:
                    current_id += self.paralell_requests
                    if current_id > max(self.found_ids, default=0) + self.paralell_requests:
                        self.paralell_requests = min(self.paralell_requests * 2, 50)

    async def print_solver(self):
        end_time = time.time()
        total_time = end_time - self.start_time
        
        full_message = self.checker.armar()
        
        print("Puzzle completado en "+ str(total_time) +"segundos")
        print(f"{full_message}")
        
        if total_time < 1.0:
            print("Bonus")


