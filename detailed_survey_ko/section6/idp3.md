### iDP3: Improved 3D Diffusion Policy via Egocentric Point Clouds

**전체 제목:** Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies

**저자:** Yanjie Ze, Zixuan Chen, Wenhao Wang, Peract Chen, Xialin He, Jianglong Ye, Ying Yuan, Huazhe Xu (Stanford / Tsinghua)

**학회/연도:** IROS 2025

**아키텍처:** iDP3 extends DP3 to real-world dexterous humanoid manipulation by addressing three practical challenges: (1) egocentric point cloud processing from head-mounted depth cameras, (2) scalable 3D representation for large workspaces, and (3) high-DoF action spaces for humanoid bodies with dexterous hands. The visual encoder uses a sparse 3D backbone (e.g., Minkowski engine) processing egocentric point clouds, with a diffusion action head generating joint-space commands. Architecture size is approximately 30-50M parameters.

**행동 공간:** Up to 25+ DoF: arm joints + dexterous hand joints (Inspire hand: 6 DoF per hand on the Fourier GR1 humanoid). Actions are continuous joint positions generated via diffusion.

**다지 핸드 지원:** ✅ --- Deployed on the Fourier GR1 humanoid with Inspire dexterous hands (6 DoF per hand, 25 DoF total for upper body). Demonstrated on real-world dexterous manipulation tasks including object handovers, tabletop manipulation, and tool use.

**힘/임피던스 출력:** ✗ --- Joint position targets only.

**핵심 방법론:** iDP3 adapts the 3D diffusion policy framework for practical humanoid deployment. Key innovations include: (1) egocentric point cloud processing from the robot's head-mounted stereo cameras, eliminating the need for external depth cameras; (2) a point cloud cropping and normalization scheme that handles variable workspace sizes while maintaining spatial precision for fine manipulation; and (3) demonstration that the 3D diffusion policy framework scales to real-world dexterous humanoid control with minimal sim-to-real gap. The system uses teleoperation via Apple Vision Pro or similar devices for demonstration collection.

**훈련 데이터:** Real-world teleoperated demonstrations on the Fourier GR1 humanoid. Typically 20-50 demonstrations per task. No simulation pretraining.

**주요 기여:**
- Among the first real-world deployments of 3D diffusion policies on a dexterous humanoid, demonstrating that DP3's 3D representation scales to high-DoF systems.
- Introduced egocentric point cloud processing for manipulation, enabling practical head-mounted depth camera usage.
- Demonstrated generalization to novel objects and scenes with minimal demonstrations on a real humanoid.

**정량적 결과:**

| Benchmark / Task | iDP3 | Notes |
|---|---|---|
| *(Consult the IROS 2025 paper for per-task success rates on Fourier GR1 humanoid manipulation tasks.)* | | |

**한계점:**
- Requires stereo depth cameras for point cloud generation; sensitive to depth noise at close range.
- Real-world evaluation on a limited number of tasks; generalization across diverse dexterous tasks not yet demonstrated at scale.
- No language conditioning; task-specific policies only.
- No force/compliance output; relies on joint PD control.

**공개 가중치/코드:** ✅ Code: [GitHub](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy). ✗ No pre-trained weights (task-specific training).

## 추론 / 배포

- **추론 지연 시간:** Not explicitly benchmarked. Similar architecture size to DP3 (~30-50M parameters), with egocentric point cloud processing adding overhead for larger workspace coverage. Estimated ~5-15 Hz on a desktop GPU with DDIM acceleration.
- **배포 하드웨어:** Fourier GR1 humanoid with head-mounted stereo depth cameras. Desktop GPU for policy inference (specific model not reported). Real-world deployment demonstrated.
- **실시간 가능 여부:** Yes, for demonstrated tasks. The system was deployed on a real humanoid (Fourier GR1) for dexterous manipulation, implying real-time operation. The 25-DoF action space and egocentric point cloud processing are more demanding than DP3's simulation setup, but the lightweight architecture supports practical control rates.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Real-world teleoperated demonstrations on Fourier GR1 humanoid with Inspire dexterous hands (6 DoF per hand, 25 DoF total upper body). No simulation pretraining.
- **수집 방법:** Teleoperation via Apple Vision Pro or similar VR devices. Egocentric point clouds from head-mounted stereo depth cameras. Real-world only -- no sim-to-real transfer.
- **데이터 규모:** 20-50 demonstrations per task. Small-data regime demonstrating sample efficiency of 3D diffusion policies.
- **원격 조작 장비:** Apple Vision Pro (or similar VR headset) for upper-body teleoperation of Fourier GR1 humanoid.
- **데이터 포맷:** Egocentric point clouds + joint positions (25 DoF). Task-specific datasets.
- **공개 여부:** Code at https://github.com/YanjieZe/Improved-3D-Diffusion-Policy. Demonstration datasets not released.

---
