# 10.6 DEX-Mouse

- **Full title:** DEX-Mouse: A Handheld Interface for Dexterous Teleoperation with Universal Applicability
- **Authors:** Not specified in survey
- **Venue/Year:** arXiv 2604.15013, April 2026
- **Input modality:** Handheld physical interface (mouse-like device)
- **Target hand:** Universal (any dexterous hand)
- **Force feedback:** Kinesthetic feedback through device mechanics
- **Cost:** <$150

## Key methodology/design

DEX-Mouse reimagines dexterous teleoperation input as a handheld device rather than a worn glove or exoskeleton. The operator manipulates a compact physical interface -- resembling a mouse in form factor -- that maps hand motions to dexterous robot hand commands. The device provides kinesthetic feedback through its mechanical structure. At under $150, it represents the lowest-cost teleoperation interface in this survey, democratizing access to dexterous data collection.

## Main contributions

- Lowest-cost dexterous teleoperation interface surveyed (<$150), dramatically reducing the barrier to dexterous data collection
- Handheld form factor eliminates wearable calibration and donning/doffing overhead
- Universal applicability across different robot hand platforms
- Kinesthetic feedback through device mechanics

## Limitations/Gaps

- Handheld interface cannot capture independent finger motions with the same fidelity as glove-based systems
- Kinesthetic feedback is limited to device-level forces, not per-finger contact rendering
- Mapping from device motion to high-DoF hand commands may require non-intuitive operator training
- Very recent (2026); limited community validation

## Data quality impact

The handheld form factor fundamentally limits the dimensionality of captured demonstrations: a single device cannot independently command all 15-20+ finger joints simultaneously, so the mapping from device motion to hand joint commands introduces coupling and reduces the expressiveness of collected trajectories. Policies trained on DEX-Mouse data may learn coarser grasp strategies (e.g., power grasps) effectively, but lack the independent finger control needed for precision manipulation (e.g., in-hand reorientation, pen spinning). The kinesthetic feedback through device mechanics provides some contact awareness, but at the device level rather than the per-finger level, limiting force-modulated behaviors in downstream policies.

## Open-source status

Open-sourced (hardware + software).
