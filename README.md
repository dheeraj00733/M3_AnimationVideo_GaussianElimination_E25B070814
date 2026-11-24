# Linear Algebra and Calculus (M3) • Internal Assessment
## Project Option 1: Animation Video — Gaussian Elimination

![Assessment](https://img.shields.io/badge/Assessment-M3%20Internal%20(10%25)-blue)
![Topic](https://img.shields.io/badge/Topic-Gaussian%20Elimination-yellow)
![Resolution](https://img.shields.io/badge/Video-1080p%2016%3A9%20MP4-green)
![Duration](https://img.shields.io/badge/Duration-05%3A11%20(5--6%20min)-brightgreen)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

### Student & Project Credentials
- **Student Name:** Dheeraj
- **Student ID:** E25B070814
- **Course:** Linear Algebra and Calculus (M3)
- **Submission Requirement:** Public GitHub Repository with Rendered Video, Source Code, and Storyboard
- **Video Duration:** **05:11 (5 minutes, 11 seconds)** — Perfectly within the **5 to 6 minute** window (strictly below 7 minutes).

---

## 📽️ Project Overview
This project presents an animated instructional video that teaches **Gaussian Elimination and Row Echelon Form (REF)** from first principles. Rather than simply presenting static definitions or final formulas, the video guides the viewer through:
1. **The Motivation:** Why ad-hoc algebraic substitution fails as linear systems scale in science and engineering.
2. **The Representation:** Compacting equations into an Augmented Matrix $[A \mid b]$ and establishing the 3 Elementary Row Operations (EROs).
3. **The Target Structure & Numerical Stability:** Understanding the Upper Triangular Staircase of Row Echelon Form, the role of Pivots, handling zero pivots, and **Partial Pivoting**.
4. **Step-by-Step Forward Elimination:** Animating exact scratchpad arithmetic for a concrete $3 \times 3$ system until echelon form is achieved.
5. **Back-Substitution, 3D Geometry & Rank Analysis:** Unwinding the decoupled matrix into exact solutions $(x, y, z) = (1, 4, -1)$, interpreting them as intersecting 3D planes, and classifying system solvability (Unique vs. Inconsistent vs. Infinite Solutions).
6. **Key Takeaways & Algorithmic Horizons:** Contrasting Gaussian Elimination (REF) with Gauss-Jordan (RREF) and computational efficiency ($\sim \frac{2}{3}n^3$).

---

## 📂 Repository File Structure
```
M3_AnimationVideo_GaussianElimination_E25B070814/
│
├── _Video.mp4                   # Final 1080p 16:9 MP4 Video (05:11 duration)
│
├── Storyboard.md                # Official 6-Scene Storyboard with visual & math plan
├── Voiceover_Script.md          # Second-by-second synchronized narration script
├── Viva_QA_Preparation.md       # Comprehensive Viva defense & Q&A guide
│
├── _Code/                       # Full animation source code
│   ├── gaussian_elimination.py  # Production Manim Python script (all 6 scenes)
│   └── render_1080p.sh          # Bash script to render 1080p video with FFmpeg
│
└── README.md                    # Project documentation & GitHub homepage
```

---

## 🎬 6-Scene Storyboard Breakdown
| Scene | Title & Focus | Duration | Key Learning Outcome |
| :---: | :--- | :---: | :--- |
| **Scene 1** | **Opening Title & Problem Hook** | `00:00 - 00:37` | Introduces Dheeraj (ID: E25B070814) and illustrates why substitution fails for large systems. |
| **Scene 2** | **Augmented Matrix & 3 EROs** | `00:37 - 01:18` | Strips variable clutter into $[A \mid b]$ and establishes valid row operations. |
| **Scene 3** | **Row Echelon Form, Pivots & Partial Pivoting** | `01:18 - 02:02` | Visualizes the staircase, defines pivots, handles zero pivots, and introduces **Partial Pivoting** for numerical stability. |
| **Scene 4** | **Step-by-Step Forward Elimination** | `02:02 - 03:26` | Walks through $R_2 - 2R_1$, $R_3 - 3R_1$, and $R_3 - 2R_2$ with live scratchpad calculations. |
| **Scene 5** | **Back-Substitution, Geometry & Rank Analysis** | `03:26 - 04:24` | Solves $z = -1, y = 4, x = 1$, explains 3D plane intersection, and diagnoses system solvability (Unique, Inconsistent, Infinite). |
| **Scene 6** | **Summary, REF vs RREF & Credits** | `04:24 - 05:11` | Recaps 3 key takeaways, contrasts REF with Reduced Row Echelon Form (Gauss-Jordan), and displays official student submission credentials. |

---

## 🛠️ Reproduction & Rendering Instructions

### Prerequisites
- Python 3.9+
- [Manim Community Edition](https://www.manim.community/) (`pip install manim` or `brew install manim`)
- [FFmpeg](https://ffmpeg.org/) (`brew install ffmpeg`)

### Step-by-Step Commands
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/M3_AnimationVideo_GaussianElimination_E25B070814.git
   cd M3_AnimationVideo_GaussianElimination_E25B070814
   ```

2. **Render individual scenes or the full video:**
   ```bash
   cd _Code
   chmod +x render_1080p.sh
   ./render_1080p.sh
   ```
   The compiled video will be saved directly to `_Video.mp4`.

---

## 📜 Mathematical Verification of the Worked Example
The system solved in the video is:
$$\begin{cases}
1x + 2y + 1z = 8 \\
2x + 5y + 3z = 19 \\
3x + 8y + 6z = 29
\end{cases}$$

1. **Matrix Initial State:**
   $$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 8 \\ 2 & 5 & 3 & 19 \\ 3 & 8 & 6 & 29 \end{array}\right]$$

2. **Row Operations Applied:**
   - $R_2 \to R_2 - 2R_1 \implies [0, 1, 1 \mid 3]$
   - $R_3 \to R_3 - 3R_1 \implies [0, 2, 3 \mid 5]$
   - $R_3 \to R_3 - 2R_2 \implies [0, 0, 1 \mid -1]$

3. **Row Echelon Form Reached:**
   $$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 8 \\ 0 & 1 & 1 & 3 \\ 0 & 0 & 1 & -1 \end{array}\right]$$

4. **Back-Substitution Results:**
   - $z = -1$
   - $y = 3 - (-1) = 4$
   - $x = 8 - 2(4) - (-1) = 8 - 8 + 1 = 1$
   - **Unique Solution Vector:** $(x, y, z) = (1, 4, -1)$

5. **Analytical Check:**
   $$1(1) + 2(4) + 1(-1) = 1 + 8 - 1 = 8 \quad \checkmark$$
   $$2(1) + 5(4) + 3(-1) = 2 + 20 - 3 = 19 \quad \checkmark$$
   $$3(1) + 8(4) + 6(-1) = 3 + 32 - 6 = 29 \quad \checkmark$$

---

## ⚖️ AI Tools & Academic Integrity Disclosure
In accordance with the official M3 Internal Assessment guidelines:
- **Mathematical Derivations & Verification:** Designed, checked, and solved independently.
- **Visual Animation Code:** Programmed using Python 3 and Manim Community Edition v0.22.1, with assistance from Antigravity AI for script templating, modular scene architecture, and storyboard formatting.
- **Voiceover Narration:** Recorded independently by student Dheeraj following the accompanying synchronized script.
