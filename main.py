import asyncio
from solver import Solver

async def main():
    solver = Solver()
    await solver.solve()

if __name__ == "__main__":
    asyncio.run(main())