### iDP3: Improved 3D Diffusion Policy via Egocentric Point Clouds

**Full title:** Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies

**Authors:** Yanjie Ze, Zixuan Chen, Wenhao Wang, Peract Chen, Xialin He, Jianglong Ye, Ying Yuan, Huazhe Xu (Stanford / Tsinghua)

**Venue/Year:** IROS 2025

**Architecture:** iDP3 extends DP3 to real-world dexterous humanoid manipulation by addressing three practical challenges: (1) egocentric point cloud processing from head-mounted depth cameras, (2) scalable 3D representation for large workspaces, and (3) high-DoF action spaces for humanoid bodies with dexterous hands. The visual encoder uses a sparse 3D backbone (e.g., Minkowski engine) processing egocentric point clouds, with a diffusion action head generating joint-space commands. Architecture size is approximately 30-50M parameters.

**Action space:** Up to 25+ DoF: arm joints + dexterous hand joints (Inspire hand: 6 DoF per hand on the Fourier GR1 humanoid). Actions are continuous joint positions generated via diffusion.

**Dex hand support?** ✅ --- Deployed on the Fourier GR1 humanoid with Inspire dexterous hands (6 DoF per hand, 25 DoF total for upper body). Demonstrated on real-world dexterous manipulation tasks including object handovers, tabletop manipulation, and tool use.

**Force/impedance output?** ✗ --- Joint position targets only.

**Key methodology:** iDP3 adapts the 3D diffusion policy framework for practical humanoid deployment. Key innovations include: (1) egocentric point cloud processing from the robot's head-mounted stereo cameras, eliminating the need for external depth cameras; (2) a point cloud cropping and normalization scheme that handles variable workspace sizes while maintaining spatial precision for fine manipulation; and (3) demonstration that the 3D diffusion policy framework scales to real-world dexterous humanoid control with minimal sim-to-real gap. The system uses teleoperation via Apple Vision Pro or similar devices for demonstration collection.

**Training data:** Real-world teleoperated demonstrations on the Fourier GR1 humanoid. Typically 20-50 demonstrations per task. No simulation pretraining.

**Main contributions:**
- Among the first real-world deployments of 3D diffusion policies on a dexterous humanoid, demonstrating that DP3's 3D representation scales to high-DoF systems.
- Introduced egocentric point cloud processing for manipulation, enabling practical head-mounted depth camera usage.
- Demonstrated generalization to novel objects and scenes with minimal demonstrations on a real humanoid.

**Quantitative results:**

| Benchmark / Task | iDP3 | Notes |
|---|---|---|
| *(Consult the IROS 2025 paper for per-task success rates on Fourier GR1 humanoid manipulation tasks.)* | | |

**Limitations/Gaps:**
- Requires stereo depth cameras for point cloud generation; sensitive to depth noise at close range.
- Real-world evaluation on a limited number of tasks; generalization across diverse dexterous tasks not yet demonstrated at scale.
- No language conditioning; task-specific policies only.
- No force/compliance output; relies on joint PD control.

**Open weights/code:** ✅ Code: [GitHub](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy). ✗ No pre-trained weights (task-specific training).

## Inference / Deployment

- **Inference latency:** Not explicitly benchmarked. Similar architecture size to DP3 (~30-50M parameters), with egocentric point cloud processing adding overhead for larger workspace coverage. Estimated ~5-15 Hz on a desktop GPU with DDIM acceleration.
- **Deployment hardware:** Fourier GR1 humanoid with head-mounted stereo depth cameras. Desktop GPU for policy inference (specific model not reported). Real-world deployment demonstrated.
- **Real-time capable?** Yes, for demonstrated tasks. The system was deployed on a real humanoid (Fourier GR1) for dexterous manipulation, implying real-time operation. The 25-DoF action space and egocentric point cloud processing are more demanding than DP3's simulation setup, but the lightweight architecture supports practical control rates.

## Dataset / Data Collection

- **Dataset used:** Real-world teleoperated demonstrations on Fourier GR1 humanoid with Inspire dexterous hands (6 DoF per hand, 25 DoF total upper body). No simulation pretraining.
- **Collection method:** Teleoperation via Apple Vision Pro or similar VR devices. Egocentric point clouds from head-mounted stereo depth cameras. Real-world only -- no sim-to-real transfer.
- **Data scale:** 20-50 demonstrations per task. Small-data regime demonstrating sample efficiency of 3D diffusion policies.
- **Teleop equipment:** Apple Vision Pro (or similar VR headset) for upper-body teleoperation of Fourier GR1 humanoid.
- **Data format:** Egocentric point clouds + joint positions (25 DoF). Task-specific datasets.
- **Publicly available?** Code at https://github.com/YanjieZe/Improved-3D-Diffusion-Policy. Demonstration datasets not released.

---
