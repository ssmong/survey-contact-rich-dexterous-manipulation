### 4.5 ImpedanceGPT

**Full title:** ImpedanceGPT: VLM-Based Impedance Control of Swarm Drones for Safe Physical Human-Drone Interaction

**Authors:** Faryal Batool, et al.

**Venue/Year:** IROS 2025

**Note: This paper addresses drone swarm formation control, not robot manipulation. Included for methodological comparison only.**

**How K/D are determined:** VLM (Molmo, open-weight) + RAG retrieval. The VLM receives visual scene information (including human presence and proximity) and retrieves appropriate impedance parameters from a knowledge base. The system generates virtual impedance parameters that govern the drone swarm's collective compliance behavior relative to a human interacting physically with the swarm.

**What is output:** Virtual stiffness K and damping D parameters for impedance-based formation control of drone swarms. These are not physical joint impedances but virtual impedance parameters that govern how the swarm collectively responds to external forces (e.g., a human pushing a drone).

**Robot platform:** Drone swarm (not a manipulation robot). N/A for dexterous hand. This paper is included in the survey because it demonstrates the VLM-guided impedance control paradigm, though applied to aerial rather than manipulation systems.

**Tasks:** Physical human-drone interaction (pHDI): humans physically interacting with (pushing, guiding) individual drones in a swarm, with the swarm adapting its collective compliance to ensure safety and maintain formation.

**Key methodology:** ImpedanceGPT applies the VLM-guided impedance control paradigm to drone swarm formation control. The VLM processes visual input of the human-drone interaction scene and reasons about appropriate virtual impedance for the swarm's formation controller. RAG retrieval from a database of prior interaction scenarios improves parameter selection. The virtual impedance governs how individual drones respond to physical perturbations while maintaining swarm cohesion, analogous to how Cartesian impedance governs a robot arm's response to contact forces.

**Architecture/Parameters:** Molmo (open-weight VLM) for scene understanding. RAG database for impedance retrieval. Virtual impedance formation controller for the drone swarm. The system processes camera feeds, generates impedance parameters via VLM + RAG, and applies them to the swarm's distributed controller.

**Main contributions:**
- Extends VLM-guided impedance control to drone swarms, demonstrating the generality of the paradigm beyond manipulation
- Applies RAG-augmented VLM reasoning for physical human-drone interaction safety
- Open-source implementation available on GitHub

**Limitations/Gaps:**
- Not a manipulation system -- drone swarm application, no robot arm or hand
- Virtual impedance (formation stiffness/damping) is conceptually different from physical joint/Cartesian impedance in manipulation
- Limited relevance to dexterous manipulation; included primarily for methodological comparison of VLM-guided impedance approaches
- Drone dynamics and contact physics differ substantially from manipulation contact
- VLM inference latency (~100ms-1s) limits impedance updates to ~1-10 Hz, three orders of magnitude below the 100-1000 Hz required by real-time impedance controllers.

**Results:** Demonstrated safe physical human-drone interaction with VLM-generated impedance parameters adapting to different interaction contexts. The swarm maintained formation integrity while being compliant to human pushes. Code released at github.com/Faryal-Batool/ImpedanceGPT.

## Inference / Deployment

- **Inference latency:** Not explicitly benchmarked. VLM (Molmo) inference plus RAG retrieval provides impedance updates at ~1-10 Hz. Navigation speed adjustments range from 0.6-1.4 m/s depending on obstacle type.
- **Deployment hardware:** Mini-drone swarm platform. VLM inference hardware not specified. Obstacle detection and retrieval accuracy reported at 80% under optimal lighting.
- **Real-time capable?** Partially. Drone navigation operates in real-time, but VLM-based impedance parameter updates are limited to ~1-10 Hz. This is more acceptable for drone formation control (slower dynamics) than for manipulation contact control.

## Dataset / Data Collection

- **Dataset used:** Custom RAG knowledge base for drone swarm impedance scenarios. No standard manipulation benchmark.
- **Collection method:** VLM-driven obstacle detection combined with RAG retrieval from prior navigation scenarios. Experimental evaluation in dynamic environments with both static and dynamic (human) obstacles. Obstacle detection and retrieval accuracy reported at 80% under optimal lighting.
- **Data scale:** Not reported. Number of episodes/trials and RAG database size not specified in available materials.
- **Teleop equipment:** Not applicable (drone swarm system, not manipulation).
- **Data format:** RAG database entries with scene descriptions and virtual impedance parameters.
- **Publicly available?** Yes -- code at https://github.com/Faryal-Batool/ImpedanceGPT
