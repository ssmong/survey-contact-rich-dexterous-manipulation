# 11.4 RUKA Hand

- **Full title:** RUKA: A Low-Cost Dexterous Robotic Hand for General Manipulation
- **Authors:** Lerrel Pinto group (NYU)
- **Venue/Year:** 2025
- **DoF:** 15
- **Cost:** <$1,300
- **Tactile sensing:** None built-in
- **Sim-to-real:** Demonstrated
- **Sim model:** Available

## Quantitative specs

| Spec | Value |
|------|-------|
| Actuator control bandwidth | Not reported in available documentation |
| Maximum fingertip force | Not reported in available documentation |
| Durability | Not reported in available documentation (design optimized for robustness and ease of maintenance) |

## Key methodology/design

RUKA Hand is designed by the NYU robotics group (Lerrel Pinto lab) as a low-cost, robust platform for general dexterous manipulation research. The 15-DoF design makes pragmatic tradeoffs -- slightly fewer DoF than LEAP (16) or ISyHand (18) -- in exchange for mechanical simplicity and build robustness. The hand prioritizes ease of assembly and maintenance, with a design that minimizes the number of custom parts and assembly steps.

## Main contributions

- Sub-$1,300 cost with proven sim-to-real transfer capability
- Design optimized for ease of assembly and maintenance, reducing the barrier for labs to build and operate
- Robust mechanical design suitable for repeated real-world experimentation

## Limitations/Gaps

- 15 DoF is the lowest in this comparison, potentially limiting manipulation dexterity for complex tasks
- No tactile sensing
- Less community adoption than LEAP Hand; fewer published results using this platform

## Open-source status

Open-source. Project page: [ruka-hand.github.io](https://ruka-hand.github.io/)
