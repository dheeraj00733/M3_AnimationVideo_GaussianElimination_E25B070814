"""
Gaussian Elimination - Animation Video Script
Linear Algebra and Calculus (M3) • Internal Assessment
Student: Dheeraj (ID: E25B070814)

Render with:
manim -qh gaussian_elimination.py FullVideo
or run render_all.sh
"""

from manim import *

# Global theme configuration
config.background_color = "#0A0F1D"  # Deep aesthetic navy
FONT_FAMILY = "Helvetica"

# Color Palette
COLOR_TITLE = "#38BDF8"       # Bright Sky Blue
COLOR_ACCENT = "#FACC15"      # Radiant Gold (for pivots)
COLOR_TEXT = "#F8FAFC"        # Crisp Off-White
COLOR_SUBTEXT = "#94A3B8"     # Soft Slate
COLOR_SUCCESS = "#34D399"     # Emerald Green (for echelon zeros/success)
COLOR_TARGET = "#F87171"      # Coral Red (for target entries to eliminate)
COLOR_BOX_BG = "#1E293B"      # Dark Slate for info cards
COLOR_ROW_HIGHLIGHT = "#3B82F6"# Royal Blue for row focus


def create_matrix_mobject(data, font_size=28, col_buff=0.7, row_buff=0.45):
    """
    Creates an augmented 3x4 matrix with bracket lines and vertical separator.
    data: list of 3 rows, each row has 4 elements [a1, a2, a3, b]
    """
    rows = []
    for r in data:
        row_cells = []
        for c_idx, val in enumerate(r):
            txt = Text(str(val), font=FONT_FAMILY, font_size=font_size, color=COLOR_TEXT, weight=BOLD)
            row_cells.append(txt)
        rows.append(row_cells)
    
    # Align columns
    num_rows = len(data)
    num_cols = len(data[0])
    
    # Determine max cell width and height for uniform grid
    grid = VGroup()
    cell_matrix = []
    
    for r in range(num_rows):
        row_group = VGroup()
        for c in range(num_cols):
            row_group.add(rows[r][c])
        cell_matrix.append(row_group)
    
    # Position cells manually for perfect alignment
    col_x = [-1.8, -0.7, 0.4, 1.7]  # x positions for cols 1, 2, 3 and augment col
    row_y = [0.8, 0.0, -0.8]        # y positions for rows 1, 2, 3
    
    all_elements = VGroup()
    for r in range(num_rows):
        for c in range(num_cols):
            rows[r][c].move_to(np.array([col_x[c], row_y[r], 0]))
            all_elements.add(rows[r][c])
            
    # Vertical separator line between col 2 (z) and col 3 (constants)
    sep_line = Line(
        start=np.array([1.05, 1.2, 0]),
        end=np.array([1.05, -1.2, 0]),
        color=COLOR_SUBTEXT,
        stroke_width=2.5
    )
    
    # Brackets
    top_left = np.array([-2.3, 1.25, 0])
    bottom_left = np.array([-2.3, -1.25, 0])
    l_bracket = VGroup(
        Line(top_left + RIGHT * 0.25, top_left, color=COLOR_SUBTEXT, stroke_width=3),
        Line(top_left, bottom_left, color=COLOR_SUBTEXT, stroke_width=3),
        Line(bottom_left, bottom_left + RIGHT * 0.25, color=COLOR_SUBTEXT, stroke_width=3)
    )
    
    top_right = np.array([2.3, 1.25, 0])
    bottom_right = np.array([2.3, -1.25, 0])
    r_bracket = VGroup(
        Line(top_right + LEFT * 0.25, top_right, color=COLOR_SUBTEXT, stroke_width=3),
        Line(top_right, bottom_right, color=COLOR_SUBTEXT, stroke_width=3),
        Line(bottom_right, bottom_right + LEFT * 0.25, color=COLOR_SUBTEXT, stroke_width=3)
    )
    
    # Row labels on the left
    r_labels = VGroup(
        Text("R1", font=FONT_FAMILY, font_size=20, color=COLOR_SUBTEXT).next_to(l_bracket, LEFT, buff=0.25).set_y(row_y[0]),
        Text("R2", font=FONT_FAMILY, font_size=20, color=COLOR_SUBTEXT).next_to(l_bracket, LEFT, buff=0.25).set_y(row_y[1]),
        Text("R3", font=FONT_FAMILY, font_size=20, color=COLOR_SUBTEXT).next_to(l_bracket, LEFT, buff=0.25).set_y(row_y[2])
    )
    
    mat_group = VGroup(all_elements, sep_line, l_bracket, r_bracket, r_labels)
    return mat_group, rows, sep_line, r_labels


class Scene1_HookAndContext(Scene):
    def construct(self):
        # 1. Front Page / Opening Frame
        badge = RoundedRectangle(corner_radius=0.15, width=9.5, height=5.2, color=COLOR_TITLE, stroke_width=2, fill_color=COLOR_BOX_BG, fill_opacity=0.6)
        
        course_tag = Text("LINEAR ALGEBRA & CALCULUS (M3)", font=FONT_FAMILY, font_size=24, color=COLOR_SUBTEXT, weight=BOLD)
        project_tag = Text("INTERNAL ASSESSMENT • PROJECT OPTION 1", font=FONT_FAMILY, font_size=18, color=COLOR_SUBTEXT)
        
        main_title = Text("Gaussian Elimination", font=FONT_FAMILY, font_size=46, color=COLOR_TITLE, weight=BOLD)
        subtitle = Text("Transforming Systems from Chaos to Echelon Form", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT)
        
        div_line = Line(LEFT * 3.5, RIGHT * 3.5, color=COLOR_TITLE, stroke_width=2)
        
        student_name = Text("Name: Dheeraj", font=FONT_FAMILY, font_size=24, color=COLOR_ACCENT, weight=BOLD)
        student_id = Text("Student ID: E25B070814", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT)
        
        title_group = VGroup(
            course_tag,
            project_tag,
            main_title,
            subtitle,
            div_line,
            student_name,
            student_id
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        
        self.play(FadeIn(badge), FadeIn(title_group), run_time=1.5)
        self.wait(10.5)  # Voiceover: Intro & Opening details (Dheeraj, ID: E25B070814)
        
        self.play(FadeOut(badge), FadeOut(title_group), run_time=1.0)
        
        # 2. The Hook / Problem Motivation
        hook_header = Text("The Real-World Problem", font=FONT_FAMILY, font_size=32, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.8)
        self.play(Write(hook_header))
        
        eq_box = RoundedRectangle(corner_radius=0.2, width=6.5, height=2.8, color="#3B82F6", fill_color=COLOR_BOX_BG, fill_opacity=0.7)
        eq1 = Text("  x  +  2y  +   z  =   8", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT)
        eq2 = Text(" 2x  +  5y  +  3z  =  19", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT)
        eq3 = Text(" 3x  +  8y  +  6z  =  29", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT)
        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.35).move_to(eq_box.get_center())
        eq_group = VGroup(eq_box, equations).shift(UP * 0.2)
        
        self.play(FadeIn(eq_group), run_time=1.2)
        self.wait(8.0)  # Voiceover: Here is a 3x3 system of linear equations
        
        q1 = Text("Can we solve this by substitution?", font=FONT_FAMILY, font_size=22, color=COLOR_TARGET)
        q2 = Text("With 3 equations it's messy. With 100 equations it's impossible!", font=FONT_FAMILY, font_size=20, color=COLOR_SUBTEXT)
        q3 = Text("We need an organized, step-by-step algorithm: Gaussian Elimination.", font=FONT_FAMILY, font_size=22, color=COLOR_SUCCESS, weight=BOLD)
        
        qs = VGroup(q1, q2, q3).arrange(DOWN, buff=0.22).next_to(eq_group, DOWN, buff=0.45)
        
        self.play(FadeIn(q1))
        self.wait(5.5)
        self.play(FadeIn(q2))
        self.wait(7.0)
        self.play(FadeIn(q3))
        self.wait(9.0)
        
        self.play(FadeOut(hook_header), FadeOut(eq_group), FadeOut(qs), run_time=1.0)


class Scene2_AugmentedMatrixAndEROs(Scene):
    def construct(self):
        header = Text("Scene 2: The Augmented Matrix & Rules", font=FONT_FAMILY, font_size=30, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.6)
        self.play(Write(header))
        
        # Step 1: Equations to Matrix
        intro_txt = Text("Step 1: Strip away variable names (x, y, z) into an Augmented Matrix", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT)
        intro_txt.next_to(header, DOWN, buff=0.35)
        self.play(FadeIn(intro_txt))
        
        # Left: Equations
        eq_box = RoundedRectangle(corner_radius=0.15, width=4.8, height=2.5, color="#3B82F6", fill_color=COLOR_BOX_BG, fill_opacity=0.7)
        eq1 = Text("1x + 2y + 1z =  8", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT)
        eq2 = Text("2x + 5y + 3z = 19", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT)
        eq3 = Text("3x + 8y + 6z = 29", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT)
        eq_vg = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.3).move_to(eq_box.get_center())
        left_side = VGroup(eq_box, eq_vg).shift(LEFT * 3.4 + DOWN * 0.2)
        
        arrow = Arrow(LEFT * 0.8, RIGHT * 0.8, color=COLOR_ACCENT, stroke_width=4).shift(DOWN * 0.2)
        
        # Right: Augmented Matrix [A | b]
        data = [
            ["1", "2", "1", " 8"],
            ["2", "5", "3", "19"],
            ["3", "8", "6", "29"]
        ]
        mat_mob, _, _, _ = create_matrix_mobject(data, font_size=24)
        mat_mob.shift(RIGHT * 3.2 + DOWN * 0.2)
        
        col_headers = VGroup(
            Text("x", font=FONT_FAMILY, font_size=18, color=COLOR_SUBTEXT).next_to(mat_mob[0][0], UP, buff=0.5),
            Text("y", font=FONT_FAMILY, font_size=18, color=COLOR_SUBTEXT).next_to(mat_mob[0][1], UP, buff=0.5),
            Text("z", font=FONT_FAMILY, font_size=18, color=COLOR_SUBTEXT).next_to(mat_mob[0][2], UP, buff=0.5),
            Text("b", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD).next_to(mat_mob[0][3], UP, buff=0.5)
        )
        
        self.play(FadeIn(left_side), run_time=1.0)
        self.wait(4.0)
        self.play(GrowArrow(arrow), FadeIn(mat_mob), FadeIn(col_headers), run_time=1.2)
        self.wait(13.0)  # Voiceover: Coefficients on the left, constants on the right
        
        self.play(FadeOut(left_side), FadeOut(arrow), FadeOut(mat_mob), FadeOut(col_headers), FadeOut(intro_txt), run_time=0.8)
        
        # Step 2: The Three Elementary Row Operations (EROs)
        ero_title = Text("The 3 Legal Elementary Row Operations (EROs)", font=FONT_FAMILY, font_size=26, color=COLOR_ACCENT, weight=BOLD)
        ero_title.next_to(header, DOWN, buff=0.4)
        self.play(Write(ero_title))
        
        card_w, card_h = 10.5, 1.22
        
        card1 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        ero1_top = VGroup(
            Text("1. Row Swap:", font=FONT_FAMILY, font_size=18, color=COLOR_TITLE, weight=BOLD),
            Text("Ri  <--->  Rj", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        ).arrange(RIGHT, buff=0.35)
        ero1_desc = Text("Reordering equations does not change the intersection point.", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        card1_content = VGroup(ero1_top, ero1_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(card1.get_center())
        ero1_group = VGroup(card1, card1_content)
        
        card2 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        ero2_top = VGroup(
            Text("2. Scalar Scale:", font=FONT_FAMILY, font_size=18, color=COLOR_TITLE, weight=BOLD),
            Text("k * Ri  --->  Ri  (k != 0)", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        ).arrange(RIGHT, buff=0.35)
        ero2_desc = Text("Multiplying both sides by a non-zero constant preserves balance.", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        card2_content = VGroup(ero2_top, ero2_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(card2.get_center())
        ero2_group = VGroup(card2, card2_content)
        
        card3 = RoundedRectangle(corner_radius=0.15, width=card_w, height=card_h, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        ero3_top = VGroup(
            Text("3. Row Addition:", font=FONT_FAMILY, font_size=18, color=COLOR_TITLE, weight=BOLD),
            Text("Ri + k * Rj  --->  Ri", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        ).arrange(RIGHT, buff=0.35)
        ero3_desc = Text("Adding a multiple of one row to another cancels target variables!", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        card3_content = VGroup(ero3_top, ero3_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(card3.get_center())
        ero3_group = VGroup(card3, card3_content)
        
        cards = VGroup(ero1_group, ero2_group, ero3_group).arrange(DOWN, buff=0.25).shift(DOWN * 0.45)
        
        self.play(FadeIn(ero1_group), run_time=0.8)
        self.wait(7.0)
        self.play(FadeIn(ero2_group), run_time=0.8)
        self.wait(7.0)
        self.play(FadeIn(ero3_group), run_time=0.8)
        self.wait(10.0)  # Voiceover: Explaining why row operations keep the exact same solution
        
        self.play(FadeOut(header), FadeOut(ero_title), FadeOut(cards), run_time=0.8)


class Scene3_RowEchelonFormAndPivots(Scene):
    def construct(self):
        header = Text("Scene 3: The Target — Row Echelon Form (REF)", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.6)
        self.play(Write(header))
        
        sub = Text("What is our destination? An Upper Triangular Staircase!", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT)
        sub.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(sub))
        
        # Display target echelon structure
        target_data = [
            ["P1", " *", " *", " d1"],
            [" 0", "P2", " *", " d2"],
            [" 0", " 0", "P3", " d3"]
        ]
        
        t_mob, t_cells, _, _ = create_matrix_mobject(target_data, font_size=28)
        t_mob.shift(LEFT * 2.2 + DOWN * 0.5)
        
        # Staircase line dynamically constructed from cell corners
        p1 = t_cells[0][0].get_corner(DL) + LEFT * 0.25 + DOWN * 0.08
        p2 = t_cells[0][0].get_corner(DR) + RIGHT * 0.25 + DOWN * 0.08
        p3 = t_cells[1][1].get_corner(DL) + LEFT * 0.25 + DOWN * 0.08
        p4 = t_cells[1][1].get_corner(DR) + RIGHT * 0.25 + DOWN * 0.08
        p5 = t_cells[2][2].get_corner(DL) + LEFT * 0.25 + DOWN * 0.08
        p6 = t_cells[2][2].get_corner(DR) + RIGHT * 0.25 + DOWN * 0.08
        
        staircase = VMobject(color=COLOR_SUCCESS, stroke_width=4)
        staircase.set_points_as_corners([
            p1,
            np.array([p2[0], p1[1], 0]),
            np.array([p2[0], p3[1], 0]),
            np.array([p4[0], p3[1], 0]),
            np.array([p4[0], p5[1], 0]),
            np.array([p6[0], p5[1], 0])
        ])
        
        # Right Explanation Card
        info_box = RoundedRectangle(corner_radius=0.15, width=4.8, height=3.2, color="#3B82F6", fill_color=COLOR_BOX_BG, fill_opacity=0.8)
        info_title = Text("Row Echelon Criteria", font=FONT_FAMILY, font_size=20, color=COLOR_ACCENT, weight=BOLD)
        r1 = Text("• Pivot: The first non-zero\n  entry from left in each row.", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT)
        r2 = Text("• Staircase: Each pivot is\n  strictly to the right of\n  the pivot above it.", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT)
        r3 = Text("• Zeros Below: All entries\n  below every pivot MUST be 0.", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD)
        info_body = VGroup(info_title, r1, r2, r3).arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to(info_box.get_center())
        info_card = VGroup(info_box, info_body).shift(RIGHT * 3.4 + DOWN * 0.5)
        
        self.play(FadeIn(t_mob), run_time=1.0)
        self.wait(2.5)
        self.play(Create(staircase), run_time=1.2)
        self.wait(2.5)
        self.play(FadeIn(info_card), run_time=1.0)
        self.wait(4.0)
        
        # Highlight pivots P1, P2, P3
        p1_box = SurroundingRectangle(t_cells[0][0], color=COLOR_ACCENT, buff=0.12, stroke_width=3)
        p2_box = SurroundingRectangle(t_cells[1][1], color=COLOR_ACCENT, buff=0.12, stroke_width=3)
        p3_box = SurroundingRectangle(t_cells[2][2], color=COLOR_ACCENT, buff=0.12, stroke_width=3)
        
        self.play(Create(p1_box), Create(p2_box), Create(p3_box), run_time=1.2)
        self.wait(10.0)  # Voiceover: Highlighting pivots and why upper triangular structure decouples variables
        
        # Highlight zeros
        z1_box = SurroundingRectangle(t_cells[1][0], color=COLOR_SUCCESS, buff=0.12, stroke_width=3)
        z2_box = SurroundingRectangle(t_cells[2][0], color=COLOR_SUCCESS, buff=0.12, stroke_width=3)
        z3_box = SurroundingRectangle(t_cells[2][1], color=COLOR_SUCCESS, buff=0.12, stroke_width=3)
        
        self.play(Create(z1_box), Create(z2_box), Create(z3_box), run_time=1.2)
        self.wait(10.5)  # Voiceover: Once these 3 zeros are created, back-substitution is trivial
        
        # Transition to Special Insight: What if a Pivot is Zero? (Partial Pivoting)
        self.play(
            FadeOut(t_mob), FadeOut(staircase), FadeOut(info_card),
            FadeOut(p1_box), FadeOut(p2_box), FadeOut(p3_box),
            FadeOut(z1_box), FadeOut(z2_box), FadeOut(z3_box),
            FadeOut(sub),
            run_time=0.8
        )
        
        sub_pivot = Text("Crucial Insight: What if a Pivot is Zero? (Row Swaps & Partial Pivoting)", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        sub_pivot.next_to(header, DOWN, buff=0.25)
        self.play(Write(sub_pivot))
        
        piv_card = RoundedRectangle(corner_radius=0.15, width=10.5, height=3.3, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        
        piv_t1 = Text("Problem: If the pivot position has a 0, we cannot divide by 0 or eliminate below!", font=FONT_FAMILY, font_size=15, color=COLOR_TARGET, weight=BOLD)
        piv_t2 = Text("Mathematical Remedy: Swap rows (Ri <---> Rj) with a non-zero row below.", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT)
        piv_t3 = Text("Engineering Insight (Partial Pivoting):", font=FONT_FAMILY, font_size=15, color=COLOR_TITLE, weight=BOLD)
        piv_t4 = Text("In scientific computing (NumPy, MATLAB), computers always swap rows to select the\nLARGEST magnitude pivot. This minimizes rounding errors and avoids numerical instability!", font=FONT_FAMILY, font_size=13.5, color=COLOR_TEXT, line_spacing=0.8)
        
        piv_content = VGroup(piv_t1, piv_t2, piv_t3, piv_t4).arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to(piv_card.get_center())
        piv_group = VGroup(piv_card, piv_content).shift(DOWN * 0.4)
        
        self.play(FadeIn(piv_group), run_time=1.0)
        self.wait(17.0)  # Voiceover: Explaining row swap when pivot is 0 and partial pivoting for numerical stability
        
        self.play(FadeOut(header), FadeOut(sub_pivot), FadeOut(piv_group), run_time=0.8)


class Scene4_WorkedExample(Scene):
    def construct(self):
        header = Text("Scene 4: Step-by-Step Forward Elimination", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(header))
        
        # Left Side: Augmented Matrix
        # Right Side: Scratchpad / Row Operation Card
        
        current_data = [
            ["1", "2", "1", " 8"],
            ["2", "5", "3", "19"],
            ["3", "8", "6", "29"]
        ]
        
        mat_mob, cells, sep, r_lbls = create_matrix_mobject(current_data, font_size=24)
        mat_mob.shift(LEFT * 3.3 + DOWN * 0.2)
        
        self.play(FadeIn(mat_mob), run_time=1.0)
        self.wait(3.0)
        
        # ---------------------------------------------------------
        # STEP 1: PIVOT 1 (Row 1, Col 1) -> Eliminate (2,1)
        # ---------------------------------------------------------
        step_banner = Text("Step 1: Use Pivot 1 to eliminate Row 2, Column 1", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        step_banner.next_to(header, DOWN, buff=0.25)
        self.play(Write(step_banner))
        
        # Highlight Pivot 1
        pivot1_rect = SurroundingRectangle(cells[0][0], color=COLOR_ACCENT, buff=0.1, stroke_width=3)
        p1_text = Text("Pivot = 1", font=FONT_FAMILY, font_size=14, color=COLOR_ACCENT).next_to(pivot1_rect, UP, buff=0.15)
        
        # Highlight Target 1 (Row 2, Col 1 -> value 2)
        target1_rect = SurroundingRectangle(cells[1][0], color=COLOR_TARGET, buff=0.1, stroke_width=3)
        
        self.play(Create(pivot1_rect), Write(p1_text), Create(target1_rect), run_time=1.0)
        self.wait(4.0)  # Voiceover: Pivot is 1. Target below it is 2.
        
        # Scratchpad Card on the right
        scratch_box = RoundedRectangle(corner_radius=0.15, width=5.6, height=3.6, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        scratch_title = Text("Row Operation:  R2 ---> R2 - 2*R1", font=FONT_FAMILY, font_size=18, color=COLOR_TITLE, weight=BOLD)
        calc_line1 = Text("      R2 : [  2,   5,   3  |  19 ]", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT)
        calc_line2 = Text(" - 2 * R1 : [ -2,  -4,  -2  | -16 ]", font=FONT_FAMILY, font_size=16, color=COLOR_TARGET)
        calc_div   = Line(LEFT * 2.3, RIGHT * 2.3, color=COLOR_SUBTEXT, stroke_width=1.5)
        calc_line3 = Text(" New R2 : [  0,   1,   1  |   3 ]", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD)
        
        scratch_group = VGroup(scratch_title, calc_line1, calc_line2, calc_div, calc_line3).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(scratch_box.get_center())
        card1 = VGroup(scratch_box, scratch_group).shift(RIGHT * 3.3 + DOWN * 0.2)
        
        self.play(FadeIn(card1), run_time=1.0)
        self.wait(9.0)  # Voiceover: Explaining R2 - 2R1 gives [0, 1, 1 | 3]
        
        # Update Matrix Row 2
        new_r2_vals = ["0", "1", "1", " 3"]
        anim_list = []
        for c in range(4):
            new_txt = Text(new_r2_vals[c], font=FONT_FAMILY, font_size=24, color=COLOR_SUCCESS if c==0 else COLOR_TEXT, weight=BOLD)
            new_txt.move_to(cells[1][c].get_center())
            anim_list.append(Transform(cells[1][c], new_txt))
            
        self.play(*anim_list, FadeOut(target1_rect), run_time=1.0)
        self.wait(4.0)
        
        # ---------------------------------------------------------
        # STEP 2: PIVOT 1 (Row 1, Col 1) -> Eliminate (3,1)
        # ---------------------------------------------------------
        step2_banner = Text("Step 2: Use Pivot 1 to eliminate Row 3, Column 1", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        step2_banner.next_to(header, DOWN, buff=0.25)
        self.play(Transform(step_banner, step2_banner))
        
        # Target 2 (Row 3, Col 1 -> value 3)
        target2_rect = SurroundingRectangle(cells[2][0], color=COLOR_TARGET, buff=0.1, stroke_width=3)
        self.play(Create(target2_rect), FadeOut(card1), run_time=0.8)
        self.wait(4.0)  # Voiceover: Now eliminate the 3 in Row 3
        
        scratch_title2 = Text("Row Operation:  R3 ---> R3 - 3*R1", font=FONT_FAMILY, font_size=18, color=COLOR_TITLE, weight=BOLD)
        calc2_line1 = Text("      R3 : [  3,   8,   6  |  29 ]", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT)
        calc2_line2 = Text(" - 3 * R1 : [ -3,  -6,  -3  | -24 ]", font=FONT_FAMILY, font_size=16, color=COLOR_TARGET)
        calc2_div   = Line(LEFT * 2.3, RIGHT * 2.3, color=COLOR_SUBTEXT, stroke_width=1.5)
        calc2_line3 = Text(" New R3 : [  0,   2,   3  |   5 ]", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD)
        
        scratch2_group = VGroup(scratch_title2, calc2_line1, calc2_line2, calc2_div, calc2_line3).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(scratch_box.get_center())
        card2 = VGroup(scratch_box, scratch2_group).shift(RIGHT * 3.3 + DOWN * 0.2)
        
        self.play(FadeIn(card2), run_time=1.0)
        self.wait(9.0)  # Voiceover: Explaining R3 - 3R1 gives [0, 2, 3 | 5]
        
        # Update Matrix Row 3
        new_r3_vals = ["0", "2", "3", " 5"]
        anim_list2 = []
        for c in range(4):
            new_txt = Text(new_r3_vals[c], font=FONT_FAMILY, font_size=24, color=COLOR_SUCCESS if c==0 else COLOR_TEXT, weight=BOLD)
            new_txt.move_to(cells[2][c].get_center())
            anim_list2.append(Transform(cells[2][c], new_txt))
            
        self.play(*anim_list2, FadeOut(target2_rect), run_time=1.0)
        self.wait(4.0)
        
        col1_cleared = Text("Column 1 below pivot is completely cleared to 0!", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD)
        col1_cleared.next_to(mat_mob, DOWN, buff=0.35)
        self.play(FadeIn(col1_cleared))
        self.wait(5.0)
        
        self.play(FadeOut(pivot1_rect), FadeOut(p1_text), FadeOut(col1_cleared), FadeOut(card2), run_time=0.8)
        
        # ---------------------------------------------------------
        # STEP 3: PIVOT 2 (Row 2, Col 2) -> Eliminate (3,2)
        # ---------------------------------------------------------
        step3_banner = Text("Step 3: Move to Pivot 2 (Row 2, Col 2) to eliminate Row 3, Col 2", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        step3_banner.next_to(header, DOWN, buff=0.25)
        self.play(Transform(step_banner, step3_banner))
        
        # Pivot 2
        pivot2_rect = SurroundingRectangle(cells[1][1], color=COLOR_ACCENT, buff=0.1, stroke_width=3)
        p2_text = Text("Pivot = 1", font=FONT_FAMILY, font_size=14, color=COLOR_ACCENT).next_to(pivot2_rect, UP, buff=0.15)
        
        # Target 3 (Row 3, Col 2 -> value 2)
        target3_rect = SurroundingRectangle(cells[2][1], color=COLOR_TARGET, buff=0.1, stroke_width=3)
        
        self.play(Create(pivot2_rect), Write(p2_text), Create(target3_rect), run_time=1.0)
        self.wait(4.0)  # Voiceover: Pivot 2 is 1. We must eliminate the 2 underneath it!
        
        scratch_title3 = Text("Row Operation:  R3 ---> R3 - 2*R2", font=FONT_FAMILY, font_size=18, color=COLOR_TITLE, weight=BOLD)
        calc3_line1 = Text("      R3 : [  0,   2,   3  |   5 ]", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT)
        calc3_line2 = Text(" - 2 * R2 : [  0,  -2,  -2  |  -6 ]", font=FONT_FAMILY, font_size=16, color=COLOR_TARGET)
        calc3_div   = Line(LEFT * 2.3, RIGHT * 2.3, color=COLOR_SUBTEXT, stroke_width=1.5)
        calc3_line3 = Text(" New R3 : [  0,   0,   1  |  -1 ]", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD)
        
        scratch3_group = VGroup(scratch_title3, calc3_line1, calc3_line2, calc3_div, calc3_line3).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(scratch_box.get_center())
        card3 = VGroup(scratch_box, scratch3_group).shift(RIGHT * 3.3 + DOWN * 0.2)
        
        self.play(FadeIn(card3), run_time=1.0)
        self.wait(9.0)  # Voiceover: Explaining R3 - 2R2 gives [0, 0, 1 | -1]
        
        # Update Matrix Row 3
        final_r3_vals = ["0", "0", "1", "-1"]
        anim_list3 = []
        for c in range(4):
            new_txt = Text(final_r3_vals[c], font=FONT_FAMILY, font_size=24, color=COLOR_SUCCESS if c in (0,1) else COLOR_TEXT, weight=BOLD)
            new_txt.move_to(cells[2][c].get_center())
            anim_list3.append(Transform(cells[2][c], new_txt))
            
        self.play(*anim_list3, FadeOut(target3_rect), run_time=1.0)
        self.wait(4.0)
        
        self.play(FadeOut(pivot2_rect), FadeOut(p2_text), FadeOut(card3), run_time=0.8)
        
        # ---------------------------------------------------------
        # FINAL ECHELON CELEBRATION
        # ---------------------------------------------------------
        success_banner = Text("Success: Matrix is in Row Echelon Form (REF)!", font=FONT_FAMILY, font_size=20, color=COLOR_SUCCESS, weight=BOLD)
        success_banner.next_to(header, DOWN, buff=0.25)
        self.play(Transform(step_banner, success_banner))
        
        # Highlight all three pivots
        box_p1 = SurroundingRectangle(cells[0][0], color=COLOR_ACCENT, buff=0.1, stroke_width=3)
        box_p2 = SurroundingRectangle(cells[1][1], color=COLOR_ACCENT, buff=0.1, stroke_width=3)
        box_p3 = SurroundingRectangle(cells[2][2], color=COLOR_ACCENT, buff=0.1, stroke_width=3)
        
        self.play(Create(box_p1), Create(box_p2), Create(box_p3), run_time=1.2)
        self.wait(7.0)  # Voiceover: All 3 pivots (1, 1, 1) and zeros below. Ready for back-substitution!
        
        self.play(
            FadeOut(header), FadeOut(step_banner), FadeOut(mat_mob),
            FadeOut(box_p1), FadeOut(box_p2), FadeOut(box_p3),
            run_time=0.8
        )


class Scene5_BackSubstitution(Scene):
    def construct(self):
        header = Text("Scene 5: Back-Substitution & Interpretation", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(header))
        
        sub = Text("Reading the solution directly from bottom to top", font=FONT_FAMILY, font_size=18, color=COLOR_SUBTEXT)
        sub.next_to(header, DOWN, buff=0.25)
        self.play(FadeIn(sub))
        
        # Left: Echelon Matrix
        ref_data = [
            ["1", "2", "1", " 8"],
            ["0", "1", "1", " 3"],
            ["0", "0", "1", "-1"]
        ]
        mat_mob, cells, sep, r_lbls = create_matrix_mobject(ref_data, font_size=24)
        mat_mob.shift(LEFT * 3.3 + DOWN * 0.4)
        
        self.play(FadeIn(mat_mob), run_time=0.8)
        self.wait(1.5)
        
        # Right: Solving Step by Step
        # 1. Row 3 -> z = -1
        r3_box = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.0, color="#10B981", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        r3_txt1 = Text("From Row 3:   0x + 0y + 1z = -1", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT)
        r3_ans  = Text("===>   z = -1", font=FONT_FAMILY, font_size=20, color=COLOR_ACCENT, weight=BOLD)
        r3_group = VGroup(r3_txt1, r3_ans).arrange(RIGHT, buff=0.4).move_to(r3_box.get_center())
        card_r3 = VGroup(r3_box, r3_group).shift(RIGHT * 3.3 + UP * 1.0)
        
        hl_r3 = SurroundingRectangle(cells[2][2], color=COLOR_ACCENT, buff=0.1, stroke_width=3)
        
        self.play(Create(hl_r3), FadeIn(card_r3), run_time=1.0)
        self.wait(6.0)  # Voiceover: Row 3 tells us z = -1 immediately
        
        # 2. Row 2 -> y + z = 3 -> y = 4
        r2_box = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.0, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        r2_txt1 = Text("From Row 2:   1y + 1(-1) = 3", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT)
        r2_ans  = Text("===>   y = 4", font=FONT_FAMILY, font_size=20, color=COLOR_ACCENT, weight=BOLD)
        r2_group = VGroup(r2_txt1, r2_ans).arrange(RIGHT, buff=0.4).move_to(r2_box.get_center())
        card_r2 = VGroup(r2_box, r2_group).shift(RIGHT * 3.3 + DOWN * 0.2)
        
        hl_r2 = SurroundingRectangle(cells[1][1], color=COLOR_TITLE, buff=0.1, stroke_width=3)
        
        self.play(Create(hl_r2), FadeIn(card_r2), run_time=1.0)
        self.wait(6.5)  # Voiceover: Substitute z = -1 into row 2 to get y = 4
        
        # 3. Row 1 -> x + 2(4) + 1(-1) = 8 -> x = 1
        r1_box = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.0, color="#F59E0B", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        r1_txt1 = Text("From Row 1:   x + 2(4) + (-1) = 8", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT)
        r1_ans  = Text("===>   x = 1", font=FONT_FAMILY, font_size=20, color=COLOR_ACCENT, weight=BOLD)
        r1_group = VGroup(r1_txt1, r1_ans).arrange(RIGHT, buff=0.4).move_to(r1_box.get_center())
        card_r1 = VGroup(r1_box, r1_group).shift(RIGHT * 3.3 + DOWN * 1.4)
        
        hl_r1 = SurroundingRectangle(cells[0][0], color=COLOR_ACCENT, buff=0.1, stroke_width=3)
        
        self.play(Create(hl_r1), FadeIn(card_r1), run_time=1.0)
        self.wait(7.0)  # Voiceover: Substitute both into row 1 to get x = 1
        
        self.play(
            FadeOut(mat_mob), FadeOut(card_r3), FadeOut(card_r2), FadeOut(card_r1),
            FadeOut(hl_r3), FadeOut(hl_r2), FadeOut(hl_r1),
            run_time=0.8
        )
        
        # Geometric Interpretation & Final Solution Box
        sol_box = RoundedRectangle(corner_radius=0.2, width=8.5, height=2.8, color=COLOR_SUCCESS, stroke_width=2.5, fill_color=COLOR_BOX_BG, fill_opacity=0.9)
        sol_title = Text("Unique Solution Point in 3D Space", font=FONT_FAMILY, font_size=22, color=COLOR_SUCCESS, weight=BOLD)
        sol_vec = Text("( x ,  y ,  z )  =  ( 1 ,  4 ,  -1 )", font=FONT_FAMILY, font_size=32, color=COLOR_ACCENT, weight=BOLD)
        
        geo_desc = Text("Geometric Meaning: The three 2D planes defined by the original equations\nintersect at exactly ONE single point in 3-dimensional space!", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT, line_spacing=0.8)
        
        sol_content = VGroup(sol_title, sol_vec, geo_desc).arrange(DOWN, buff=0.3).move_to(sol_box.get_center())
        sol_group = VGroup(sol_box, sol_content).shift(DOWN * 0.3)
        
        self.play(FadeIn(sol_group), run_time=1.2)
        self.wait(8.0)  # Voiceover: Explaining the unique intersection of planes and quick verification
        
        self.play(FadeOut(sol_group), FadeOut(sub), run_time=0.8)
        
        # New High-Value Topic: System Structure & Rank (The 3 Outcomes)
        rank_banner = Text("Theoretical Depth: What Echelon Form Tells Us About Any System", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        rank_banner.next_to(header, DOWN, buff=0.25)
        self.play(Write(rank_banner))
        
        c_w, c_h = 10.5, 1.15
        
        c1_box = RoundedRectangle(corner_radius=0.15, width=c_w, height=c_h, color="#10B981", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        c1_title = Text("1. Unique Solution (Our Case):", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD)
        c1_desc  = Text("Pivots in all 3 columns (Rank = 3). Planes intersect at exactly one point: (1, 4, -1).", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT)
        c1_vg = VGroup(c1_title, c1_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(c1_box.get_center())
        card_c1 = VGroup(c1_box, c1_vg)
        
        c2_box = RoundedRectangle(corner_radius=0.15, width=c_w, height=c_h, color="#EF4444", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        c2_title = Text("2. Inconsistent System (No Solution):", font=FONT_FAMILY, font_size=16, color=COLOR_TARGET, weight=BOLD)
        c2_desc  = Text("A row like [ 0  0  0 | 5 ] implies 0 = 5 (contradiction!). Planes do not share a point.", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT)
        c2_vg = VGroup(c2_title, c2_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(c2_box.get_center())
        card_c2 = VGroup(c2_box, c2_vg)
        
        c3_box = RoundedRectangle(corner_radius=0.15, width=c_w, height=c_h, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        c3_title = Text("3. Infinite Solutions (Underdetermined / Dependent):", font=FONT_FAMILY, font_size=16, color=COLOR_TITLE, weight=BOLD)
        c3_desc  = Text("A zero row [ 0  0  0 | 0 ] leaves free variables. Planes intersect along a common line/plane.", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT)
        c3_vg = VGroup(c3_title, c3_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(c3_box.get_center())
        card_c3 = VGroup(c3_box, c3_vg)
        
        cards_cases = VGroup(card_c1, card_c2, card_c3).arrange(DOWN, buff=0.22).shift(DOWN * 0.45)
        
        self.play(FadeIn(card_c1), run_time=0.8)
        self.wait(4.0)
        self.play(FadeIn(card_c2), run_time=0.8)
        self.wait(4.5)
        self.play(FadeIn(card_c3), run_time=0.8)
        self.wait(6.0)  # Voiceover: Explaining the 3 possible outcomes of linear systems revealed by echelon form
        
        self.play(FadeOut(header), FadeOut(rank_banner), FadeOut(cards_cases), run_time=0.8)


class Scene6_SummaryAndCredits(Scene):
    def construct(self):
        # 1. Three Core Takeaways
        t_header = Text("Core Takeaways & Recap", font=FONT_FAMILY, font_size=30, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.6)
        self.play(Write(t_header))
        
        tk_w, tk_h = 10.5, 1.2
        takeaway1_box = RoundedRectangle(corner_radius=0.15, width=tk_w, height=tk_h, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.75)
        t1_title = Text("1. Augmented Matrix Representation", font=FONT_FAMILY, font_size=18, color=COLOR_TITLE, weight=BOLD)
        t1_desc = Text("Removes algebraic variable clutter and stores clean numerical coefficients [A | b].", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT)
        t1_vg = VGroup(t1_title, t1_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(takeaway1_box.get_center())
        card1 = VGroup(takeaway1_box, t1_vg)
        
        takeaway2_box = RoundedRectangle(corner_radius=0.15, width=tk_w, height=tk_h, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.75)
        t2_title = Text("2. Systematic Elimination via Pivots", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        t2_desc = Text("Elementary row operations create zeros below each pivot, forming the upper triangular REF.", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT)
        t2_vg = VGroup(t2_title, t2_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(takeaway2_box.get_center())
        card2 = VGroup(takeaway2_box, t2_vg)
        
        takeaway3_box = RoundedRectangle(corner_radius=0.15, width=tk_w, height=tk_h, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.75)
        t3_title = Text("3. Seamless Back-Substitution", font=FONT_FAMILY, font_size=18, color=COLOR_SUCCESS, weight=BOLD)
        t3_desc = Text("Once decoupled into echelon form, bottom-up substitution yields the unique solution rapidly.", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT)
        t3_vg = VGroup(t3_title, t3_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(takeaway3_box.get_center())
        card3 = VGroup(takeaway3_box, t3_vg)
        
        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.25).shift(DOWN * 0.45)
        
        self.play(FadeIn(card1), run_time=0.8)
        self.wait(5.0)
        self.play(FadeIn(card2), run_time=0.8)
        self.wait(5.0)
        self.play(FadeIn(card3), run_time=0.8)
        self.wait(7.0)  # Voiceover: Summarizing the 3 key pillars of Gaussian Elimination
        
        self.play(FadeOut(t_header), FadeOut(cards), run_time=0.8)
        
        # Extension Insight: REF vs RREF (Gauss-Jordan Elimination)
        rref_header = Text("Algorithmic Horizon: REF vs. Reduced Row Echelon Form (RREF)", font=FONT_FAMILY, font_size=20, color=COLOR_ACCENT, weight=BOLD).to_edge(UP, buff=0.6)
        self.play(Write(rref_header))
        
        rref_box = RoundedRectangle(corner_radius=0.15, width=10.5, height=3.3, color="#38BDF8", fill_color=COLOR_BOX_BG, fill_opacity=0.85)
        
        rref_p1 = Text("• Gaussian Elimination stops at REF (Upper Triangular) + Back-Substitution.", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        rref_p2 = Text("• Gauss-Jordan Elimination continues upwards, eliminating entries ABOVE pivots.", font=FONT_FAMILY, font_size=15, color=COLOR_TITLE)
        rref_p3 = Text("• The augmented matrix transforms into [ I | x ], revealing the exact solution directly!", font=FONT_FAMILY, font_size=15, color=COLOR_SUCCESS, weight=BOLD)
        rref_p4 = Text("• Computational Efficiency: Gaussian elimination takes ~2/3 n^3 operations (faster),\n  making it the preferred industry standard for large numerical systems.", font=FONT_FAMILY, font_size=13, color=COLOR_SUBTEXT, line_spacing=0.8)
        
        rref_vg = VGroup(rref_p1, rref_p2, rref_p3, rref_p4).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(rref_box.get_center())
        rref_group = VGroup(rref_box, rref_vg).shift(DOWN * 0.4)
        
        self.play(FadeIn(rref_group), run_time=1.0)
        self.wait(15.0)  # Slide stays on screen while concluding narration plays
        self.play(FadeOut(rref_header), FadeOut(rref_group), run_time=1.0)


class FullVideo(Scene):
    """
    Master Scene chaining all 6 scenes seamlessly into a single 5-minute video.
    """
    def construct(self):
        s1 = Scene1_HookAndContext()
        s1.construct = lambda: None  # avoid double
        Scene1_HookAndContext.construct(self)
        
        Scene2_AugmentedMatrixAndEROs.construct(self)
        Scene3_RowEchelonFormAndPivots.construct(self)
        Scene4_WorkedExample.construct(self)
        Scene5_BackSubstitution.construct(self)
        Scene6_SummaryAndCredits.construct(self)
