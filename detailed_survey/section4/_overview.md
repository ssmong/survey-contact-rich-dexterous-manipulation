# 4. VLM-guided Impedance Control

Systems where a VLM/LLM generates or retrieves impedance parameters (K, D) for a low-level controller. These approaches leverage large vision-language models to bridge the gap between high-level semantic scene understanding and low-level compliance regulation, eliminating the need for manual impedance tuning.

**Papers in this section:**
1. [CompliantVLA-adaptor](compliantvla_adaptor.md) — VLM zero-shot impedance generation for frozen VLAs
2. [OmniVIC](omnivic.md) — VLM + self-improving RAG for omnidirectional impedance
3. [HumanoidVLM](humanoidvlm.md) — Open-weight VLM impedance for humanoid pHRI
4. [SafeHumanoid](safehumanoid.md) — Safety-constrained VLM impedance for humanoid pHRI
5. [ImpedanceGPT](impedancegpt.md) — VLM impedance for drone swarm formation (out-of-scope comparison)

---

### Cross-cutting Observations

**1. Uniform reliance on VLM zero-shot or RAG-based reasoning.** All five papers use VLMs to generate impedance parameters via prompting (zero-shot or few-shot via RAG), rather than training neural networks to predict impedance. This makes these systems training-free or nearly so, but means impedance quality is bounded by the VLM's reasoning capability and the quality of the RAG database. None of these systems learn impedance from demonstration data or RL.

**2. No dexterous hand support.** Every system in this section operates on a parallel-jaw gripper (Franka Panda), a humanoid with simple integrated grippers (Unitree G1), or a non-manipulation platform (drone swarm). None addresses multi-finger impedance control, which would require generating per-finger or per-joint stiffness/damping matrices -- a substantially higher-dimensional output than the 6D Cartesian parameters these systems produce.

**3. Task-level rather than continuous impedance adaptation.** All systems generate impedance parameters at the task or phase level (e.g., "for insertion, use Kz=500, Dz=20"), not continuously during contact. VLM inference latency (~100ms-1s) limits impedance updates to ~1-10 Hz, three orders of magnitude below the 100-1000 Hz required by real-time impedance controllers. This is a fundamental architectural limitation of the VLM-in-the-loop approach.

**4. IIT Genoa / TU Darmstadt group dominates.** CompliantVLA-adaptor and OmniVIC share authors and represent an evolving line of work from the same group, with OmniVIC adding self-improving RAG to the basic VLM prompting approach. HumanoidVLM and SafeHumanoid form another pair from a single group. The field is small and concentrated.

**5. Open-weight vs. commercial VLMs.** CompliantVLA-adaptor and OmniVIC depend on GPT-4o-mini (commercial API), while HumanoidVLM, SafeHumanoid, and ImpedanceGPT use Molmo (open-weight). The open-weight approaches enable on-device deployment and reproducibility, but may sacrifice reasoning quality relative to larger commercial models.

**6. No formal stability guarantees (except possibly SafeHumanoid).** VLM-generated impedance parameters have no inherent guarantee of producing stable closed-loop behavior. If the VLM generates excessively high stiffness or mismatched K/D ratios, the system could become unstable or oscillatory. Only SafeHumanoid explicitly addresses safety constraints, but details on formal guarantees are limited.

**7. Gap: VLM-guided impedance for dexterous hands.** The intersection of VLM-guided impedance control and multi-finger dexterous hands is entirely unexplored. A system that uses VLM reasoning to generate per-finger compliance profiles for a Shadow or Allegro hand during contact-rich manipulation (e.g., adjusting fingertip stiffness when grasping fragile vs. rigid objects) would address a clear gap in both the VLM-guided impedance and dexterous manipulation literatures.
