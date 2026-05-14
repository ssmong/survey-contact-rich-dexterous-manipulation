# 5. Learned Impedance / Variable Compliance Control

Systems that learn or optimize impedance/stiffness/damping parameters without a VLM backbone. Unlike the VLM-guided approaches in section 4, these methods use imitation learning (IL), reinforcement learning (RL), diffusion models, or optimization to produce impedance parameters from data. Papers that use force as input but output only positions (e.g., FoAR, FACTR) appear in section 3 instead.

> **Note:** FILIC, DexForce, and IndustReal use fixed hand-tuned impedance; they are included because they operate within an impedance control framework but do not perform impedance learning.

**Papers in this section:**
1. [Comp-ACT](compact.md) — Cholesky-parameterized stiffness via ACT imitation learning
2. [Diff-Impedance](diff_impedance.md) — Diffusion-based joint position + impedance trajectory learning
3. [VICES](vices.md) — Variable impedance as RL action space
4. [CHIP](chip.md) — Hindsight impedance perturbation for robust humanoid RL
5. [FILIC](filic.md) — Force-impedance learning with fixed impedance framework (fixed K/D)
6. [CHEQ](cheq.md) — Hybrid contact-aware Q-learning for variable impedance
7. [DA-VIL](davil.md) — Dual-arm RL + QP variable impedance
8. [DexForce](dexforce.md) — Force-relevant dexterous manipulation (fixed k_f, dexterous hand)
9. [Force Policy](force_policy.md) — Learned force targets via hybrid position-force control
10. [IndustReal](industreal.md) — Sim-to-real assembly with fixed impedance (fixed K/D)
11. [Divide et Impera](divide_et_impera.md) — Impedance family optimization for assembly
12. [DCM](dcm.md) — Impedance-conditioned diffusion contact model

---

### Cross-cutting Observations

**1. Only one paper uses a dexterous hand.** DexForce is the sole system in this section operating on a multi-finger hand (Allegro, 16 DoF). All other 11 papers use robot arms with parallel-jaw grippers. This matches the broader pattern observed in the survey: force/impedance learning has developed almost entirely in the gripper/arm context, creating a clear gap for dexterous hand impedance control.

**2. Diverse learning paradigms, no consensus approach.** The 12 papers span imitation learning (Comp-ACT, FILIC, Force Policy), reinforcement learning (VICES, CHIP, CHEQ, DA-VIL), diffusion models (Diff-Impedance, DCM), neural network optimization (Divide et Impera), hand-tuning (DexForce, IndustReal), and hybrid approaches. No single paradigm dominates, and direct comparisons between these approaches on shared benchmarks are absent.

**3. Stiffness is learned more often than damping.** Of the papers that learn impedance parameters, most learn stiffness K but omit or fix damping D: Comp-ACT (K only, D derived), CHIP (K only), DA-VIL (K only, D not reported), FILIC (both fixed), IndustReal (both fixed), DexForce (fixed k_f). Only VICES, Diff-Impedance, CHEQ, and Divide et Impera independently learn both K and D. This may reflect the fact that stiffness has a more direct effect on task performance (force = K * position_error) while damping primarily affects transient behavior, but neglecting damping can cause oscillatory or underdamped contact responses.

**4. Simulation-only vs. real-robot evaluation is split.** VICES, CHIP, and DA-VIL are simulation-only. IndustReal, DexForce, Force Policy, CHEQ, and Divide et Impera are real-robot only or primarily real. Diff-Impedance, FILIC, and Comp-ACT evaluate in both. The simulation-only papers benefit from controlled evaluation but face unknown sim-to-real gaps, while real-only papers demonstrate practical applicability but lack the controlled ablations that simulation enables.

**5. Fixed impedance as a baseline strategy.** IndustReal (RSS 2023, NVIDIA) demonstrated that fixed hand-tuned impedance + RL-learned positions achieves strong sim-to-real results for assembly tasks. DexForce similarly uses fixed force scaling. These results raise the question of when variable impedance is truly necessary vs. when fixed impedance with learned position targets suffices. The answer likely depends on task diversity: fixed impedance works well for narrow task distributions but fails when the policy must handle varying contact stiffnesses, object types, or force requirements within a single deployment.

**6. Cholesky parameterization for physical validity.** Comp-ACT introduced Cholesky decomposition to guarantee that predicted stiffness matrices are symmetric positive definite. This is an important practical detail: unconstrained neural network outputs can produce invalid stiffness matrices (non-symmetric, negative eigenvalues) that cause controller instability. Other papers either use diagonal K (avoiding the problem) or do not address SPD constraints explicitly. Cholesky parameterization should be standard for any system predicting full stiffness matrices.

**7. No system combines variable impedance with VLA-scale generalization.** All learned impedance systems in this section are task-specific: trained on narrow task distributions (insertion, polishing, assembly). None demonstrates broad task generalization analogous to VLA models (which handle dozens to hundreds of tasks). Integrating variable impedance into VLA-scale generalist policies -- where the same model adjusts compliance across diverse contact conditions -- remains an open direction.

**8. Gap: learned per-finger impedance for dexterous hands.** The only dexterous hand entry (DexForce) uses hand-tuned fixed force scaling. No system learns per-finger or per-joint stiffness/damping for multi-finger hands from data (IL, RL, or diffusion). This would require: (a) high-dimensional impedance output (16+ joints for Allegro, 24+ for Shadow), (b) demonstrations or RL rewards that capture per-finger force application, and (c) impedance controllers that can operate at the per-joint level on dexterous hand hardware. The Cholesky parameterization from Comp-ACT could extend to this setting but has not been applied.

**9. DCM occupies a distinct niche.** Unlike all other papers in this section, DCM does not output impedance but takes impedance as input to a contact dynamics model. This "impedance-conditioned world model" approach is complementary to impedance learning: a system could use DCM-style models to evaluate candidate impedance parameters generated by any of the other methods. The combination of learned impedance generation + diffusion-based outcome prediction is unexplored.
