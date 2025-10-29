import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("BIPEDAL LOCOMOTION DEMO")
print("=" * 60)

# Create environment
try:
    env = gym.make('BipedalWalker-v3')
    print("✅ BipedalWalker environment loaded")
except:
    print("⚠️ BipedalWalker not available, using CartPole")
    env = gym.make('CartPole-v1')

# Print MDP components
print(f"\nState space: {env.observation_space}")
print(f"Action space: {env.action_space}")
print(f"State dimensions: {env.observation_space.shape[0]}")

# Run demo episodes
print("\nRunning 3 demo episodes...")
rewards = []

for episode in range(3):
    obs, info = env.reset()
    episode_reward = 0
    
    for step in range(500):
        action = env.action_space.sample()  # Random action
        obs, reward, terminated, truncated, info = env.step(action)
        episode_reward += reward
        
        if terminated or truncated:
            break
    
    rewards.append(episode_reward)
    print(f"Episode {episode+1}: Reward = {episode_reward:.2f}, Steps = {step+1}")

print(f"\nAverage Reward: {np.mean(rewards):.2f}")
print("✅ Demo complete!")

env.close()