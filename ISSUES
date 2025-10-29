# Technical Issues Log

## Issue 1: Original Baseline Won't Install

**Repository:** github.com/HybridRobotics/cassie_rl_walking

**Error:**
```
ERROR: No matching distribution found for tensorflow==1.15
```

**Root Cause:**
- Repo requires TensorFlow 1.15 (released 2019, EOL)
- TensorFlow 1.15 not available for Python 3.8+
- No pip wheels for Windows

**Attempted Solutions:**
1. ❌ Install with Python 3.6 - conda conflicts
2. ❌ Use tensorflow-cpu==1.15 - still unavailable
3. ❌ Build from source - SWIG dependency issues

**Final Resolution:**
- Focus on paper analysis and understanding
- Create analogous demos with modern tools
- Document MDP formulation from paper
- Generate visualizations showing concept mastery

## Issue 2: Box2D Installation Failed

**Error:**
```
error: command 'swig.exe' failed: None
```

**Root Cause:**
- box2d-py requires SWIG compiler
- Not available on Windows without manual install

**Resolution:**
- Use CartPole instead (built-in to Gymnasium)
- Still demonstrates balance control concepts
- Sufficient for midterm demo

## Lessons Learned
- Always check dependency compatibility early
- Have backup plans for legacy codebases
- Understanding concepts > running exact baseline
- Documentation is critical when code won't run
