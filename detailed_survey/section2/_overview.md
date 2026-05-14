# 2. Dexterous VLA / Vision-Language-Action

This section surveys Vision-Language-Action (VLA) models that incorporate dexterous hand support or language-conditioned dexterous manipulation. Unlike the gripper-centric VLA foundation models covered in Section 6 of the main survey, these works explicitly target multi-finger hand embodiments, high-DoF action spaces, or language-guided dexterous grasping.

**Papers in this section:**
- [2.1 UniDex-VLA](unidex_vla.md)
- [2.2 DexGraspVLA](dexgraspvla.md)
- [2.3 DexVLA](dexvla.md)
- [2.4 Dexora](dexora.md)
- [2.5 Grasp as You Say](grasp_as_you_say.md)
- [2.6 HumanoidGen](humanoidgen.md)
- [2.7 VLA + Diffusion Policy Switching](vla_diffusion_switch.md)

---

### Cross-cutting Observations

**1. Position-only action spaces dominate.** All seven systems in this section output joint position targets or end-effector poses. None generates force, torque, impedance, or stiffness commands. Even the VLA+Diffusion Switch work, which uses a mechanically compliant (series-elastic) hand, relies on the hardware for compliance rather than learning force-aware control. This is a significant gap for contact-rich tasks such as tool use, assembly, and handling fragile objects, where force regulation is essential.

**2. Architecture convergence toward VLM + diffusion.** A clear pattern emerges: large pre-trained VLMs handle semantic understanding and language grounding, while diffusion-based models generate the actual dexterous actions. DexVLA (frozen VLM + 1B diffusion expert), DexGraspVLA (Qwen2.5-VL-72B + diffusion controller), HumanoidGen (LLM + diffusion policy), and VLA+Diffusion Switch all follow this two-stage paradigm. UniDex-VLA uses flow matching (closely related to diffusion) as its action head. This separation of semantic reasoning from motor control appears to be the dominant design pattern.

**3. Cross-embodiment generalization remains rare.** UniDex-VLA is the only work that explicitly targets cross-hand generalization, evaluating on 8 different hand platforms via its FAAS representation. All other works are tied to a single hand embodiment. This contrasts with the gripper-based VLA literature, where cross-embodiment transfer (across different robot arms with grippers) is increasingly common.

**4. Data scale varies dramatically.** Dexora provides the largest real-world dexterous dataset (12.2K episodes, 40.5 hours) plus 100K simulated episodes. UniDex-VLA trains on 9M frames across 8 hands. DexGraspVLA leverages a 72B pre-trained VLM to reduce the need for task-specific data. In contrast, Grasp as You Say and VLA+Diffusion Switch operate at much smaller data scales. The field has not yet converged on the data requirements for dexterous VLA training.

**5. Language is used at different granularities.** The surveyed works use language at three distinct levels: (a) task-level specification ("pick up the red mug") in UniDex-VLA, DexGraspVLA, DexVLA, and HumanoidGen; (b) grasp-intent specification ("grasp the mug by its handle") in Grasp as You Say; and (c) policy switching signals in VLA+Diffusion Switch. No work uses language to specify contact parameters (e.g., "grasp gently," "press firmly"), which would be a natural extension for force-aware dexterous VLAs.

**6. VLM backbone sizes span two orders of magnitude.** DexGraspVLA uses a 72B VLM (Qwen2.5-VL-72B), while other systems use significantly smaller backbones. This raises questions about the minimum VLM capacity needed for dexterous manipulation: does dexterous control require the world knowledge and reasoning capability of very large VLMs, or can smaller models suffice when paired with strong action generation heads? The answer likely depends on task complexity and the degree of language conditioning required.

**7. Real-world evaluation depth varies.** Dexora and DexGraspVLA emphasize real-world data and evaluation. DexVLA and HumanoidGen include real-world results but with less emphasis. Grasp as You Say evaluates primarily in simulation. UniDex-VLA demonstrates sim-based cross-hand transfer. VLA+Diffusion Switch targets a real hand but with limited reported experiments. The gap between simulation performance and real-world deployment remains significant for dexterous VLAs.

**8. Tactile and force sensing are absent.** None of the seven works incorporates tactile sensing (e.g., GelSight, DIGIT) or force/torque feedback. This is notable because the force-aware VLA literature (Section 3 of the main survey) has shown that F/T integration improves contact-rich manipulation for grippers. Extending these approaches to dexterous hands -- where contact occurs at multiple fingertips simultaneously -- is an open challenge.
