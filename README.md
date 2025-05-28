# Puzzle Decoder Race Solution
##How to run your solution
1. **Set up the puzzle server**:
   ```bash
   docker run -p 8080:8080 ifajardov/puzzle-server
2. **Set up the python environment
  ```bash
  python -m venv venv           # Create virtual environment
  source venv/bin/activate      # On Windows use: venv\Scripts\activate
  pip install -r requirements.txt
  ```
3. **Run the solution
   ```bash
   python main.py
   
Your strategy for speed and correctness

Asynchronous requests: Uses aiohttp to make concurrent API calls (10 parallel requests by default)

Dynamic request scaling: Automatically increases parallel requests when detecting available fragments

The exceution stops immediately when puzzle is complete
