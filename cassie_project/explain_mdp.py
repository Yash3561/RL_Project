print("=" * 70)
print("CASSIE ROBOT - MDP FORMULATION FOR SLIDES")
print("=" * 70)

print("\n📊 STATE SPACE (Observations):")
print("-" * 70)
states = [
    ("Joint Positions", "16", "Angles of all joints"),
    ("Joint Velocities", "16", "Angular velocities"),
    ("Pelvis Orientation", "4", "Quaternion (x,y,z,w)"),
    ("Pelvis Angular Velocity", "3", "Rotation rates"),
    ("Foot Contacts", "2", "Left/Right ground contact"),
    ("Command", "1-3", "Desired speed or jump target")
]

total = 0
for name, dim, desc in states:
    print(f"  • {name:25} | Dim: {dim:4} | {desc}")
    total += int(dim.split('-')[0])

print(f"\n  TOTAL DIMENSION: ~{total}-{total+2} (Partially Observable)")

print("\n🎯 ACTION SPACE:")
print("-" * 70)
print("  • 10 continuous values (one per actuated joint)")
print("  • Range: [-1, 1] (normalized)")
print("  • Represents target torques → PD controller → motors")

print("\n🎁 REWARD FUNCTION:")
print("-" * 70)
print("  r(s,a) = w₁·velocity_forward")
print("         + w₂·orientation_upright")
print("         - w₃·energy_consumption")
print("         - w₄·foot_impact")
print("         - w₅·termination_penalty")
print("\n  Encourages: fast, stable, efficient locomotion")

print("\n⚙️ DYNAMICS:")
print("-" * 70)
print("  • Physics: MuJoCo simulator")
print("  • Frequency: 30 Hz (Δt = 0.033s)")
print("  • Contact model: Soft contacts with friction")

print("\n👁️ PARTIAL OBSERVABILITY:")
print("-" * 70)
print("  Cannot directly observe:")
print("    ❌ Ground friction coefficient")
print("    ❌ External forces (wind, pushes)")
print("    ❌ Robot mass/inertia changes")
print("\n  Solution: Use observation history → Dual-history controller")

print("\n" + "=" * 70)
print("✅ Copy this information into your presentation slides!")
print("=" * 70)