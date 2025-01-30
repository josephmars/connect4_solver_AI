# Connect Four AI

## Overview
AI program to play Connect Four. The tasks include implementing a Connect Four game interface, designing an evaluation function, implementing the Minimax algorithm, enhancing the program with the Alpha-Beta Pruning algorithm, and analyzing the program's performance.

<p align="center">
  <img src="https://www.roadtolarissa.com/wp-content/uploads/2012/09/c1.png" width="300">
  <br>
  Figure 1: Connect Four Game
</p>


## AI implementations
1. **Minimax algorithm**: Recursively explores all possible moves and selects the one that maximizes the score.
2. **Alpha-Beta Pruning**: Prunes the search tree by eliminating branches that cannot affect the final result.
3. **Connect Four Game Interface**: A simple text-based interface for playing Connect Four.
4. **Evaluation Function**: A function that evaluates the desirability of a board state.
5. **Experiments**: A notebook for running experiments and analyzing the performance of the AI.

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:801/1*NKzsRiAxa_oiikgbLyLCyw.png" width="600">
  <br>
  Figure 2: State Tree example.
</p>








## Solution Structure
The solution is organized into the following components:

1. **ai_vs_ai.py:** This script contains the implementation of the Connect Four AI vs. AI experiments. It uses the Minimax and Alpha-Beta Pruning algorithms with varying depths to play the game and record the results.

2. **play_vs_ai.py:** This script demonstrates the AI playing against a human. And it is used for the experiment of AI playing against real users online using the https://boardgames.io/en/connect4 website

3. **experiments folder:** This folder contains the recorded results of the experiments in JSON format. The file `ai_vs_ai.json` includes the results of AI vs. AI experiments, and `ai_vs_human.json` contains the outcomes of AI vs. Human experiments.

4. **experiments.ipynb:** This script contains the notebooks for the experiments AI vs AI and AI vs Human.


## Running the Experiments
- To run the AI vs. AI experiments, execute the `src/experiments.ipynb` notebook. The results will be saved in the `experiments` folder in a file named `ai_vs_ai.json`. 

- The AI vs Human experiments results are in the in the `experiments` folder under `ai_vs_human.json` But if you want to play against the AI online, use the `play_vs_ai.py` script. Follow the instructions in the script to log opponent movements and observe AI performance.

## Project Structure
```
connect-four-ai/
├── src/
│ ├── ai_vs_ai.py
│ ├── connect4.py
│ └── play_vs_ai.py
│ └── experiments.ipynb
├── experiments/
│ ├── ai_vs_ai.json
│ └── ai_vs_human.json
├── README.md
└── requirements.txt
```
