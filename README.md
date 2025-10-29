# Cassie RL Midterm Demo - Team 3

## Team Members
- Yash Chaudhary (ygc2)
- Gnana Midde (gam54)
- Kaviya Sree Ravikumar Meenakshi (kr549)

## Project Status: Midterm Demo Ready ✅

## Known Issues with Original Repo
The baseline repository (github.com/HybridRobotics/cassie_rl_walking) has the following issues:
- Requires TensorFlow 1.15 (EOL, incompatible with Python 3.8+)
- `pip install -e .` fails with dependency errors
- SWIG compilation issues on Windows

## Our Approach
Since the original repo is incompatible with modern environments, we:
1. Analyzed the paper and code structure thoroughly
2. Created demonstration using CartPole (analogous balance control problem)
3. Generated all visualizations showing understanding of concepts
4. Documented complete MDP formulation from paper

## Files Overview

### Demo Scripts
- `quick_demo.py` - Basic RL demo (CartPole)
- `better_demo.py` - Enhanced demo with visualizations
- `make_figures.py` - Generate training curves
- `explain_mdp.py` - Print MDP formulation

### Generated Figures
- `training_curve.png` - Training progress visualization
- `training_stages.png` - 3-stage curriculum learning
- `complete_demo.png` - Comprehensive episode analysis
- `architecture.png` - Dual-history policy architecture

### Presentation Materials
- `slide_content.txt` - Complete slide content (15 slides)
- `presentation_notes.txt` - Speaking script (10 minutes)
- `recording_checklist.txt` - Recording procedure

## Setup Instructions
```bash
conda create -n cassie_rl python=3.8 -y
conda activate cassie_rl
pip install mujoco gymnasium numpy torch matplotlib scipy

# Run demo
python quick_demo.py

# Generate all figures
python better_demo.py
python make_figures.py
```

## Presentation Structure

**Total Time: 10 minutes**

- Slides 1-2 (Kaviya): Introduction & Motivation - 1.5 min
- Slides 3-6 (Yash): MDP Formulation & Method - 3 min
- Slides 7-9 (Gnana): Training & Demo - 2 min
- Slides 10-15 (Kaviya): Extensions & Summary - 3.5 min

## Extensions Planned (Final Project)
1. Energy-efficient locomotion via reward shaping
2. LSTM-based architecture replacing CNN
3. Disturbance recovery training

## Academic Integrity Note
All code is original or properly attributed. We could not run the baseline due to dependency issues, so we created analogous demonstrations showing our understanding of the RL concepts and paper methodology.
