"""
Gaussian Elimination - Animation Video Script (Modern Minimal Light Theme)
Linear Algebra and Calculus (M3) • Internal Assessment
Student: Dheeraj (ID: E25B070814)

Render with:
/opt/homebrew/bin/manim -r 1920,1080 --fps 30 gaussian_elimination.py SceneName
or run render_1080p.sh
"""

from manim import *
import numpy as np

# -------------------------------------------------------------
# GLOBAL THEME CONFIGURATION (Modern Minimal Light Palette)
# -------------------------------------------------------------
config.background_color = "#F8FAFC"   # Clean light slate/off-white (Tailwind Slate 50)
FONT_FAMILY = "Helvetica"

# Minimal Modern Color Palette
COLOR_TITLE       = "#1E3A8A"   # Deep Navy Blue (Headers & Focus)
COLOR_TEXT        = "#0F172A"   # Deep Charcoal Slate 900 (High contrast readability)
COLOR_SUBTEXT     = "#475569"   # Muted Slate 600 (Secondary explanations)
COLOR_MUTED       = "#64748B"   # Light Slate 500 (Labels, ticks, axes)

COLOR_PRIMARY     = "#2563EB"   # Electric Royal Blue (Vectors, active lines)
COLOR_SECONDARY   = "#4F46E5"   # Indigo 600 (Brackets, partitions)
COLOR_ACCENT      = "#D97706"   # Warm Amber (Pivots, leading entries)
COLOR_SUCCESS     = "#059669"   # Emerald Green (Created zeros, solutions, REF success)
COLOR_TARGET      = "#DC2626"   # Crimson Red (Elimination targets, cancellations)
COLOR_PURPLE      = "#7C3AED"   # Violet 600 (Plane 3, 3D accents)
COLOR_CYAN        = "#0284C7"   # Sky Blue 600 (Plane 1, matrix headers)

COLOR_CARD_BG     = "#FFFFFF"   # Pure White Card
COLOR_CARD_BORDER = "#CBD5E1"   # Clean Light Slate Border
COLOR_CARD_SHADOW = "#E2E8F0"   # Soft drop-shadow color


def create_card(width, height, border_color=COLOR_CARD_BORDER, fill_color=COLOR_CARD_BG, corner_radius=0.18, stroke_width=1.8, accent_bar_color=None):
    """
    Creates an Apple-style minimal white card with a clean border, soft drop-shadow,
    and optional top accent bar. Outlines are crisp and well-defined.
    """
    shadow = RoundedRectangle(
        corner_radius=corner_radius,
        width=width,
        height=height,
        color=COLOR_CARD_SHADOW,
        stroke_width=3.5,
        fill_color=COLOR_CARD_SHADOW,
        fill_opacity=0.45
    ).shift(DOWN * 0.05 + RIGHT * 0.03)
    
    card = RoundedRectangle(
        corner_radius=corner_radius,
        width=width,
        height=height,
        color=border_color,
        stroke_width=stroke_width,
        fill_color=fill_color,
        fill_opacity=1.0
    )
    group = VGroup(shadow, card)
    if accent_bar_color:
        bar = RoundedRectangle(
            corner_radius=0.08,
            width=width - 0.08,
            height=0.08,
            color=accent_bar_color,
            fill_color=accent_bar_color,
            fill_opacity=1.0,
            stroke_width=0
        ).move_to(card.get_top() + DOWN * 0.05)
        group.add(bar)
    return group, card


def create_matrix_mobject(data, font_size=24):
    """
    Creates an augmented 3x4 matrix in the light theme with crisp brackets and separator.
    Row positions are calibrated to give ample headroom for 'Pivot = 1' labels.
    """
    rows = []
    for r in data:
        row_cells = []
        for c_idx, val in enumerate(r):
            txt = Text(str(val), font=FONT_FAMILY, font_size=font_size, color=COLOR_TEXT, weight=BOLD)
            row_cells.append(txt)
        rows.append(row_cells)
    
    num_rows = len(data)
    num_cols = len(data[0])
    
    col_x = [-1.85, -0.75, 0.35, 1.65]  # x positions for cols 1, 2, 3 and augment col
    row_y = [0.65, -0.05, -0.75]        # calibrated y positions with ample top headroom
    
    all_elements = VGroup()
    for r in range(num_rows):
        for c in range(num_cols):
            rows[r][c].move_to(np.array([col_x[c], row_y[r], 0]))
            all_elements.add(rows[r][c])
            
    # Vertical separator line between col 2 (z) and col 3 (constants)
    sep_line = Line(
        start=np.array([1.0, 1.40, 0]),
        end=np.array([1.0, -1.35, 0]),
        color=COLOR_CARD_BORDER,
        stroke_width=2.5
    )
    
    # Crisp Light Brackets with 1.45 unit height for clearance
    top_left = np.array([-2.35, 1.45, 0])
    bottom_left = np.array([-2.35, -1.35, 0])
    l_bracket = VGroup(
        Line(top_left + RIGHT * 0.25, top_left, color=COLOR_SUBTEXT, stroke_width=2.5),
        Line(top_left, bottom_left, color=COLOR_SUBTEXT, stroke_width=2.5),
        Line(bottom_left, bottom_left + RIGHT * 0.25, color=COLOR_SUBTEXT, stroke_width=2.5)
    )
    
    top_right = np.array([2.35, 1.45, 0])
    bottom_right = np.array([2.35, -1.35, 0])
    r_bracket = VGroup(
        Line(top_right + LEFT * 0.25, top_right, color=COLOR_SUBTEXT, stroke_width=2.5),
        Line(top_right, bottom_right, color=COLOR_SUBTEXT, stroke_width=2.5),
        Line(bottom_right, bottom_right + LEFT * 0.25, color=COLOR_SUBTEXT, stroke_width=2.5)
    )
    
    # Row labels on the left
    r_labels = VGroup(
        Text("R1", font=FONT_FAMILY, font_size=18, color=COLOR_MUTED, weight=BOLD).next_to(l_bracket, LEFT, buff=0.25).set_y(row_y[0]),
        Text("R2", font=FONT_FAMILY, font_size=18, color=COLOR_MUTED, weight=BOLD).next_to(l_bracket, LEFT, buff=0.25).set_y(row_y[1]),
        Text("R3", font=FONT_FAMILY, font_size=18, color=COLOR_MUTED, weight=BOLD).next_to(l_bracket, LEFT, buff=0.25).set_y(row_y[2])
    )
    
    # White card backdrop for matrix with crisp outline
    mat_card_g, _ = create_card(width=5.5, height=3.5, border_color=COLOR_CARD_BORDER)
    
    mat_group = VGroup(mat_card_g, all_elements, sep_line, l_bracket, r_bracket, r_labels)
    return mat_group, rows, sep_line, r_labels


def iso_project(x, y, z, origin=ORIGIN, scale=0.55):
    """
    Isometric 3D projection:
    x-axis at 210 deg, y-axis at 330 deg, z-axis straight up (90 deg).
    """
    vx = np.array([-np.cos(np.pi / 6), -np.sin(np.pi / 6), 0]) * scale
    vy = np.array([np.cos(np.pi / 6), -np.sin(np.pi / 6), 0]) * scale
    vz = np.array([0, 1.0, 0]) * scale
    return origin + x * vx + y * vy + z * vz


def create_3d_planes_graphic(origin=ORIGIN, scale=0.55):
    """
    Builds a high-fidelity 3D coordinate system with 3 intersecting planes meeting at (1, 4, -1),
    complete with planar grid textures, coordinate axes, and solution vector.
    """
    def iso(x, y, z):
        return iso_project(x, y, z, origin, scale)

    # 3D Coordinate Axes
    ax_x = Arrow(iso(0,0,0), iso(3.5, 0, 0), color="#64748B", stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.14)
    ax_y = Arrow(iso(0,0,0), iso(0, 5.0, 0), color="#64748B", stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.14)
    ax_z = Arrow(iso(0,0,0), iso(0, 0, 3.2), color="#64748B", stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.14)
    
    lbl_x = Text("X", font=FONT_FAMILY, font_size=14, color="#64748B", weight=BOLD).next_to(ax_x.get_end(), DL, buff=0.1)
    lbl_y = Text("Y", font=FONT_FAMILY, font_size=14, color="#64748B", weight=BOLD).next_to(ax_y.get_end(), DR, buff=0.1)
    lbl_z = Text("Z", font=FONT_FAMILY, font_size=14, color="#64748B", weight=BOLD).next_to(ax_z.get_end(), UP, buff=0.1)
    axes_group = VGroup(ax_x, ax_y, ax_z, lbl_x, lbl_y, lbl_z)

    # Three 3D Intersecting Planes with realistic planar surfaces
    # Plane 1: x + 2y + z = 8 (Sky Blue)
    pl1_pts = [iso(-1, 4.5, 0), iso(3, 2.5, 0), iso(3, 1, 3), iso(-1, 3, 3)]
    plane1 = Polygon(*pl1_pts, fill_color=COLOR_CYAN, fill_opacity=0.38, stroke_color=COLOR_CYAN, stroke_width=2.0)
    # Surface grid texture line for Plane 1
    pl1_grid = DashedLine(iso(1, 3.5, 0), iso(1, 2, 3), color=COLOR_CYAN, stroke_width=1.2)
    lbl_p1 = Text("Plane 1: x + 2y + z = 8", font=FONT_FAMILY, font_size=11.5, color=COLOR_CYAN, weight=BOLD).next_to(plane1, LEFT, buff=0.1).shift(UP * 0.4)
    p1_full = VGroup(plane1, pl1_grid, lbl_p1)

    # Plane 2: 2x + 5y + 3z = 19 (Royal Blue)
    pl2_pts = [iso(0, 3.8, 0), iso(2.2, 3, 0), iso(2.2, 4.2, -2), iso(0, 5, -2)]
    plane2 = Polygon(*pl2_pts, fill_color=COLOR_PRIMARY, fill_opacity=0.38, stroke_color=COLOR_PRIMARY, stroke_width=2.0)
    pl2_grid = DashedLine(iso(1.1, 3.4, 0), iso(1.1, 4.6, -2), color=COLOR_PRIMARY, stroke_width=1.2)
    lbl_p2 = Text("Plane 2: 2x + 5y + 3z = 19", font=FONT_FAMILY, font_size=11.5, color=COLOR_PRIMARY, weight=BOLD).next_to(plane2, DOWN, buff=0.12).shift(RIGHT * 0.2)
    p2_full = VGroup(plane2, pl2_grid, lbl_p2)

    # Plane 3: 3x + 8y + 6z = 29 (Violet)
    pl3_pts = [iso(-0.5, 4.2, -1.8), iso(2.5, 3.5, -1.8), iso(2.5, 4.2, 0.5), iso(-0.5, 4.9, 0.5)]
    plane3 = Polygon(*pl3_pts, fill_color=COLOR_PURPLE, fill_opacity=0.38, stroke_color=COLOR_PURPLE, stroke_width=2.0)
    pl3_grid = DashedLine(iso(1.0, 3.85, -1.8), iso(1.0, 4.55, 0.5), color=COLOR_PURPLE, stroke_width=1.2)
    lbl_p3 = Text("Plane 3: 3x + 8y + 6z = 29", font=FONT_FAMILY, font_size=11.5, color=COLOR_PURPLE, weight=BOLD).next_to(plane3, LEFT, buff=0.1).shift(DOWN * 0.15)
    p3_full = VGroup(plane3, pl3_grid, lbl_p3)

    # Unique Solution Intersection Point (1, 4, -1)
    sol_pt = iso(1, 4, -1)
    sol_dot = Dot(sol_pt, color=COLOR_SUCCESS, radius=0.15)
    sol_ring = Circle(radius=0.28, color=COLOR_SUCCESS, stroke_width=2.8).move_to(sol_pt)
    
    # Coordinate Projection Lines to Axes (z -> y -> x)
    drop_xy = iso(1, 4, 0)
    line_z = DashedLine(sol_pt, drop_xy, color="#94A3B8", stroke_width=1.8)
    line_x = DashedLine(drop_xy, iso(1, 0, 0), color="#94A3B8", stroke_width=1.8)
    line_y = DashedLine(drop_xy, iso(0, 4, 0), color="#94A3B8", stroke_width=1.8)
    proj_lines = VGroup(line_z, line_x, line_y)

    # Floating 3D Coordinate Pill Tag placed safely in open space
    pill_bg = RoundedRectangle(corner_radius=0.08, width=1.9, height=0.40, color=COLOR_SUCCESS, fill_color="#ECFDF5", fill_opacity=1.0, stroke_width=1.5)
    pill_txt = Text("(1, 4, -1)", font=FONT_FAMILY, font_size=12, color=COLOR_SUCCESS, weight=BOLD).move_to(pill_bg)
    pt_tag = VGroup(pill_bg, pill_txt).next_to(sol_dot, UL, buff=0.15)
    
    # 3D Solution Vector from Origin (0,0,0) to (1,4,-1)
    vec_sol = Arrow(iso(0,0,0), sol_pt, color=COLOR_SUCCESS, stroke_width=3.5, buff=0, max_tip_length_to_length_ratio=0.16)

    planes_list = [p1_full, p2_full, p3_full]
    graph_group = VGroup(axes_group, p1_full, p2_full, p3_full, proj_lines, vec_sol, sol_ring, sol_dot, pt_tag)
    return graph_group, axes_group, planes_list, VGroup(sol_dot, sol_ring, vec_sol, proj_lines, pt_tag)


# =============================================================================
# SCENE 1: HOOK & 3D INTERSECTING PLANES ANIMATION (~51s)
# =============================================================================
class Scene1_HookAndContext(Scene):
    def construct(self):
        # 1. Opening Title Card (00:00 – 00:13)
        badge_g, badge = create_card(width=10.6, height=5.5, border_color="#3B82F6", accent_bar_color=COLOR_PRIMARY)
        
        course_tag = Text("LINEAR ALGEBRA & CALCULUS (M3)", font=FONT_FAMILY, font_size=22, color=COLOR_PRIMARY, weight=BOLD)
        project_tag = Text("INTERNAL ASSESSMENT • PROJECT OPTION 1: ANIMATION VIDEO", font=FONT_FAMILY, font_size=14.5, color=COLOR_SUBTEXT)
        
        main_title = Text("Gaussian Elimination & Row Echelon Form", font=FONT_FAMILY, font_size=36, color=COLOR_TITLE, weight=BOLD)
        subtitle = Text("A Visual & Geometric Journey into Linear Systems", font=FONT_FAMILY, font_size=19, color=COLOR_SUBTEXT)
        
        div_line = Line(LEFT * 4.0, RIGHT * 4.0, color=COLOR_CARD_BORDER, stroke_width=1.5)
        
        student_name = Text("Presenter: Dheeraj", font=FONT_FAMILY, font_size=22, color=COLOR_ACCENT, weight=BOLD)
        student_id = Text("Student ID: E25B070814", font=FONT_FAMILY, font_size=18, color=COLOR_TEXT)
        
        title_group = VGroup(
            course_tag,
            project_tag,
            main_title,
            subtitle,
            div_line,
            student_name,
            student_id
        ).arrange(DOWN, buff=0.22).move_to(badge.get_center())
        
        full_title_group = VGroup(badge_g, title_group)
        self.play(FadeIn(full_title_group), run_time=1.4)
        self.wait(10.5)  # Voiceover: Intro & Opening details (Dheeraj, ID: E25B070814)
        
        self.play(FadeOut(full_title_group), run_time=0.9)
        
        # 2. The Hook: Real-World 3D Planes Graph (00:13 – 00:30)
        hook_header = Text("The Real-World Problem: 3 Equations in 3D Space", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.55)
        self.play(Write(hook_header))
        
        # Left side: Clean card with equations and generous padding
        eq_card_g, eq_card = create_card(width=5.2, height=3.6, border_color="#38BDF8", accent_bar_color=COLOR_CYAN)
        eq_title = Text("System of 3 Planes in R^3", font=FONT_FAMILY, font_size=16, color=COLOR_PRIMARY, weight=BOLD)
        eq1 = Text("  x  +  2y  +   z  =   8", font=FONT_FAMILY, font_size=21, color=COLOR_CYAN, weight=BOLD)
        eq2 = Text(" 2x  +  5y  +  3z  =  19", font=FONT_FAMILY, font_size=21, color=COLOR_PRIMARY, weight=BOLD)
        eq3 = Text(" 3x  +  8y  +  6z  =  29", font=FONT_FAMILY, font_size=21, color=COLOR_PURPLE, weight=BOLD)
        eq_vg = VGroup(eq_title, eq1, eq2, eq3).arrange(DOWN, buff=0.3).move_to(eq_card.get_center())
        left_group = VGroup(eq_card_g, eq_vg).shift(LEFT * 3.4 + DOWN * 0.25)
        
        # Right side: Dynamic 3D Geometric Representation with Step-by-Step Plane Animations!
        graph_g, axes_g, planes_list, sol_g = create_3d_planes_graphic(origin=RIGHT * 2.7 + DOWN * 0.2, scale=0.48)
        
        self.play(FadeIn(left_group), Create(axes_g), run_time=1.0)
        self.wait(1.0)
        # Sequential drawing of the 3 3D planes
        self.play(FadeIn(planes_list[0]), run_time=0.8)
        self.play(FadeIn(planes_list[1]), run_time=0.8)
        self.play(FadeIn(planes_list[2]), run_time=0.8)
        # Animate the unique intersection point and solution vector
        self.play(Create(sol_g), run_time=1.2)
        
        # Concentric radar beacon ripple on intersection point
        sol_pt = iso_project(1, 4, -1, origin=RIGHT * 2.7 + DOWN * 0.2, scale=0.48)
        ripple1 = Circle(radius=0.15, color=COLOR_SUCCESS, stroke_width=3).move_to(sol_pt)
        self.play(ripple1.animate.scale(2.8).set_stroke(opacity=0), run_time=0.9)
        self.remove(ripple1)
        self.wait(4.5)  # Voiceover: Here is a 3x3 system of linear equations in 3D space
        
        self.play(FadeOut(left_group), FadeOut(graph_g), run_time=0.8)
        
        # 3. Curiosity Questions (00:30 – 00:51) - Generous box widths and comfortable text margins
        q_card1_g, q_c1 = create_card(width=10.4, height=1.1, border_color="#EF4444", accent_bar_color="#EF4444")
        q1_txt = Text("Can we solve this by simple substitution?", font=FONT_FAMILY, font_size=17.5, color=COLOR_TARGET, weight=BOLD)
        q1_vg = VGroup(q_card1_g, q1_txt.move_to(q_c1.get_center()))
        
        q_card2_g, q_c2 = create_card(width=10.4, height=1.1, border_color="#F59E0B", accent_bar_color="#F59E0B")
        q2_txt = Text("With 3 equations it's messy. In robotics & graphics with 100 equations: impossible!", font=FONT_FAMILY, font_size=15.0, color=COLOR_SUBTEXT, weight=BOLD)
        q2_vg = VGroup(q_card2_g, q2_txt.move_to(q_c2.get_center()))
        
        q_card3_g, q_c3 = create_card(width=10.4, height=1.1, border_color="#10B981", accent_bar_color="#10B981")
        q3_txt = Text("Solution: An organized, foolproof matrix algorithm — Gaussian Elimination.", font=FONT_FAMILY, font_size=17.0, color=COLOR_SUCCESS, weight=BOLD)
        q3_vg = VGroup(q_card3_g, q3_txt.move_to(q_c3.get_center()))
        
        q_cards = VGroup(q1_vg, q2_vg, q3_vg).arrange(DOWN, buff=0.28).shift(DOWN * 0.3)
        
        self.play(FadeIn(q1_vg), run_time=0.7)
        self.wait(5.0)
        self.play(FadeIn(q2_vg), run_time=0.7)
        self.wait(6.5)
        self.play(FadeIn(q3_vg), run_time=0.7)
        self.wait(8.5)
        
        self.play(FadeOut(hook_header), FadeOut(q_cards), run_time=0.8)


# =============================================================================
# SCENE 2: THE AUGMENTED MATRIX & DYNAMIC EROs (~51s)
# =============================================================================
class Scene2_AugmentedMatrixAndEROs(Scene):
    def construct(self):
        header = Text("Scene 2: The Augmented Matrix & Rules", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.55)
        self.play(Write(header))
        
        intro_txt = Text("Step 1: Strip away variable names (x, y, z) into an Augmented Matrix [A | b]", font=FONT_FAMILY, font_size=18, color=COLOR_SUBTEXT)
        intro_txt.next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(intro_txt))
        
        # Left: Equations in Card with generous padding
        eq_box_g, eq_box = create_card(width=4.8, height=3.0, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        eq1 = Text("1x + 2y + 1z =  8", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT)
        eq2 = Text("2x + 5y + 3z = 19", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT)
        eq3 = Text("3x + 8y + 6z = 29", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT)
        eq_vg = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.32).move_to(eq_box.get_center())
        left_side = VGroup(eq_box_g, eq_vg).shift(LEFT * 3.4 + DOWN * 0.2)
        
        arrow = Arrow(LEFT * 0.7, RIGHT * 0.7, color=COLOR_PRIMARY, stroke_width=3.5).shift(DOWN * 0.2)
        
        # Right: Augmented Matrix [A | b]
        data = [
            ["1", "2", "1", " 8"],
            ["2", "5", "3", "19"],
            ["3", "8", "6", "29"]
        ]
        mat_mob, _, _, _ = create_matrix_mobject(data, font_size=24)
        mat_mob.shift(RIGHT * 3.2 + DOWN * 0.2)
        
        col_headers = VGroup(
            Text("x", font=FONT_FAMILY, font_size=16, color=COLOR_PRIMARY, weight=BOLD).next_to(mat_mob[1][0], UP, buff=0.45),
            Text("y", font=FONT_FAMILY, font_size=16, color=COLOR_PRIMARY, weight=BOLD).next_to(mat_mob[1][1], UP, buff=0.45),
            Text("z", font=FONT_FAMILY, font_size=16, color=COLOR_PRIMARY, weight=BOLD).next_to(mat_mob[1][2], UP, buff=0.45),
            Text("b", font=FONT_FAMILY, font_size=16, color=COLOR_ACCENT, weight=BOLD).next_to(mat_mob[1][3], UP, buff=0.45)
        )
        
        self.play(FadeIn(left_side), run_time=0.9)
        self.wait(3.5)
        self.play(GrowArrow(arrow), FadeIn(mat_mob), FadeIn(col_headers), run_time=1.2)
        self.wait(13.0)  # Voiceover: Coefficients on the left, constants on the right
        
        self.play(FadeOut(left_side), FadeOut(arrow), FadeOut(mat_mob), FadeOut(col_headers), FadeOut(intro_txt), run_time=0.8)
        
        # Step 2: The Three Elementary Row Operations (EROs) with Motion Graphics
        ero_title = Text("The 3 Legal Elementary Row Operations (EROs)", font=FONT_FAMILY, font_size=24, color=COLOR_TITLE, weight=BOLD)
        ero_title.next_to(header, DOWN, buff=0.35)
        self.play(Write(ero_title))
        
        card_w, card_h = 10.6, 1.35
        
        # Card 1: Row Swap with Curved Swap Arrows
        c1_g, c1 = create_card(width=card_w, height=card_h, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        ero1_top = VGroup(
            Text("1. Row Swap:", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD),
            Text("Ri  <--->  Rj", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        ).arrange(RIGHT, buff=0.3)
        ero1_desc = Text("Reordering equations does not alter the geometric intersection point.", font=FONT_FAMILY, font_size=14.5, color=COLOR_SUBTEXT)
        c1_text = VGroup(ero1_top, ero1_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(c1.get_center()).shift(LEFT * 0.9)
        
        # Visual icon: dynamic swap arrows
        swap_up = CurvedArrow(RIGHT * 3.8 + DOWN * 0.15, RIGHT * 3.8 + UP * 0.25, angle=-TAU/4, color=COLOR_PRIMARY, stroke_width=2.5)
        swap_dn = CurvedArrow(RIGHT * 4.3 + UP * 0.25, RIGHT * 4.3 + DOWN * 0.15, angle=-TAU/4, color=COLOR_ACCENT, stroke_width=2.5)
        ero1_icon = VGroup(swap_up, swap_dn).move_to(c1.get_center()).shift(RIGHT * 3.9)
        ero1_full = VGroup(c1_g, c1_text, ero1_icon)
        
        # Card 2: Scalar Scale with Scaling Badge
        c2_g, c2 = create_card(width=card_w, height=card_h, border_color="#F59E0B", accent_bar_color=COLOR_ACCENT)
        ero2_top = VGroup(
            Text("2. Scalar Scale:", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD),
            Text("k · Ri  --->  Ri  (k != 0)", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        ).arrange(RIGHT, buff=0.3)
        ero2_desc = Text("Multiplying both sides by a non-zero constant preserves balance.", font=FONT_FAMILY, font_size=14.5, color=COLOR_SUBTEXT)
        c2_text = VGroup(ero2_top, ero2_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(c2.get_center()).shift(LEFT * 0.9)
        
        scale_badge = RoundedRectangle(corner_radius=0.1, width=1.4, height=0.6, color=COLOR_ACCENT, fill_color="#FEF3C7", fill_opacity=1.0)
        scale_txt = Text("× k", font=FONT_FAMILY, font_size=16, color=COLOR_ACCENT, weight=BOLD).move_to(scale_badge.get_center())
        ero2_icon = VGroup(scale_badge, scale_txt).move_to(c2.get_center()).shift(RIGHT * 3.9)
        ero2_full = VGroup(c2_g, c2_text, ero2_icon)
        
        # Card 3: Row Addition with Target Elimination Badge
        c3_g, c3 = create_card(width=card_w, height=card_h, border_color="#10B981", accent_bar_color=COLOR_SUCCESS)
        ero3_top = VGroup(
            Text("3. Row Addition:", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD),
            Text("Ri + k · Rj  --->  Ri", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        ).arrange(RIGHT, buff=0.3)
        ero3_desc = Text("Adding a multiple of one row to another systematically eliminates target variables!", font=FONT_FAMILY, font_size=14.0, color=COLOR_SUBTEXT)
        c3_text = VGroup(ero3_top, ero3_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(c3.get_center()).shift(LEFT * 0.9)
        
        add_badge = RoundedRectangle(corner_radius=0.1, width=1.4, height=0.6, color=COLOR_SUCCESS, fill_color="#D1FAE5", fill_opacity=1.0)
        add_txt = Text("-> 0", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD).move_to(add_badge.get_center())
        ero3_icon = VGroup(add_badge, add_txt).move_to(c3.get_center()).shift(RIGHT * 3.9)
        ero3_full = VGroup(c3_g, c3_text, ero3_icon)
        
        cards = VGroup(ero1_full, ero2_full, ero3_full).arrange(DOWN, buff=0.25).shift(DOWN * 0.45)
        
        self.play(FadeIn(ero1_full), run_time=0.8)
        self.wait(6.0)
        self.play(FadeIn(ero2_full), run_time=0.8)
        self.wait(6.0)
        self.play(FadeIn(ero3_full), run_time=0.8)
        self.wait(9.0)  # Voiceover: Explaining why row operations keep the exact same solution
        
        self.play(FadeOut(header), FadeOut(ero_title), FadeOut(cards), run_time=0.8)


# =============================================================================
# SCENE 3: ROW ECHELON FORM & PARTIAL PIVOTING (~60s)
# =============================================================================
class Scene3_RowEchelonFormAndPivots(Scene):
    def construct(self):
        header = Text("Scene 3: The Target — Row Echelon Form (REF)", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.55)
        self.play(Write(header))
        
        sub = Text("Our Destination: An Upper Triangular Staircase Architecture", font=FONT_FAMILY, font_size=18, color=COLOR_SUBTEXT)
        sub.next_to(header, DOWN, buff=0.25)
        self.play(FadeIn(sub))
        
        # Display target echelon structure
        target_data = [
            ["P1", " *", " *", " d1"],
            [" 0", "P2", " *", " d2"],
            [" 0", " 0", "P3", " d3"]
        ]
        
        t_mob, t_cells, _, _ = create_matrix_mobject(target_data, font_size=28)
        t_mob.shift(LEFT * 2.3 + DOWN * 0.45)
        
        # Dynamic Staircase line
        p1 = t_cells[0][0].get_corner(DL) + LEFT * 0.25 + DOWN * 0.08
        p2 = t_cells[0][0].get_corner(DR) + RIGHT * 0.25 + DOWN * 0.08
        p3 = t_cells[1][1].get_corner(DL) + LEFT * 0.25 + DOWN * 0.08
        p4 = t_cells[1][1].get_corner(DR) + RIGHT * 0.25 + DOWN * 0.08
        p5 = t_cells[2][2].get_corner(DL) + LEFT * 0.25 + DOWN * 0.08
        p6 = t_cells[2][2].get_corner(DR) + RIGHT * 0.25 + DOWN * 0.08
        
        staircase = VMobject(color=COLOR_SUCCESS, stroke_width=4.5)
        staircase.set_points_as_corners([
            p1,
            np.array([p2[0], p1[1], 0]),
            np.array([p2[0], p3[1], 0]),
            np.array([p4[0], p3[1], 0]),
            np.array([p4[0], p5[1], 0]),
            np.array([p6[0], p5[1], 0])
        ])
        
        # Right Explanation Card with generous margins
        info_box_g, info_box = create_card(width=5.6, height=3.6, border_color="#3B82F6", accent_bar_color=COLOR_PRIMARY)
        info_title = Text("Row Echelon Criteria", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD)
        r1 = Text("• Pivot: The first non-zero\n  entry from left in each row.", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        r2 = Text("• Staircase: Each pivot is\n  strictly to the right of\n  the pivot above it.", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        r3 = Text("• Zeros Below: All entries\n  below every pivot MUST be 0.", font=FONT_FAMILY, font_size=15, color=COLOR_SUCCESS, weight=BOLD)
        info_body = VGroup(info_title, r1, r2, r3).arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to(info_box.get_center())
        info_card = VGroup(info_box_g, info_body).shift(RIGHT * 3.4 + DOWN * 0.45)
        
        self.play(FadeIn(t_mob), run_time=0.9)
        self.wait(2.0)
        self.play(Create(staircase), run_time=1.2)
        self.wait(2.0)
        self.play(FadeIn(info_card), run_time=1.0)
        self.wait(3.5)
        
        # Highlight pivots P1, P2, P3
        p1_box = SurroundingRectangle(t_cells[0][0], color=COLOR_ACCENT, buff=0.1, stroke_width=2.8)
        p2_box = SurroundingRectangle(t_cells[1][1], color=COLOR_ACCENT, buff=0.1, stroke_width=2.8)
        p3_box = SurroundingRectangle(t_cells[2][2], color=COLOR_ACCENT, buff=0.1, stroke_width=2.8)
        
        self.play(Create(p1_box), Create(p2_box), Create(p3_box), run_time=1.0)
        self.wait(9.0)  # Voiceover: Highlighting pivots and why upper triangular structure decouples variables
        
        # Highlight zeros
        z1_box = SurroundingRectangle(t_cells[1][0], color=COLOR_SUCCESS, buff=0.1, stroke_width=2.8)
        z2_box = SurroundingRectangle(t_cells[2][0], color=COLOR_SUCCESS, buff=0.1, stroke_width=2.8)
        z3_box = SurroundingRectangle(t_cells[2][1], color=COLOR_SUCCESS, buff=0.1, stroke_width=2.8)
        
        self.play(Create(z1_box), Create(z2_box), Create(z3_box), run_time=1.0)
        self.wait(9.5)  # Voiceover: Once these 3 zeros are created, back-substitution is trivial
        
        # Transition to Crucial Insight: Partial Pivoting
        self.play(
            FadeOut(t_mob), FadeOut(staircase), FadeOut(info_card),
            FadeOut(p1_box), FadeOut(p2_box), FadeOut(p3_box),
            FadeOut(z1_box), FadeOut(z2_box), FadeOut(z3_box),
            FadeOut(sub),
            run_time=0.8
        )
        
        sub_pivot = Text("Crucial Insight: What if a Pivot is Zero? (Partial Pivoting & Stability)", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD)
        sub_pivot.next_to(header, DOWN, buff=0.25)
        self.play(Write(sub_pivot))
        
        # Partial pivoting visual & card with comfortable line wrapping
        piv_card_g, piv_card = create_card(width=10.6, height=3.6, border_color="#F59E0B", accent_bar_color=COLOR_ACCENT)
        
        piv_t1 = Text("Problem: If the pivot entry is 0, we cannot divide by 0 to eliminate numbers below!", font=FONT_FAMILY, font_size=15.5, color=COLOR_TARGET, weight=BOLD)
        piv_t2 = Text("Mathematical Remedy: Swap rows (Ri <---> Rj) with a non-zero row underneath.", font=FONT_FAMILY, font_size=15.0, color=COLOR_TEXT)
        piv_t3 = Text("Engineering Gold Standard — Partial Pivoting:", font=FONT_FAMILY, font_size=15.5, color=COLOR_TITLE, weight=BOLD)
        piv_t4 = Text("In scientific computing (NumPy, SciPy, LAPACK), algorithms scan the column and swap\nto select the LARGEST magnitude pivot. This eliminates round-off errors and prevents division by tiny numbers!", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUBTEXT, line_spacing=0.85)
        
        piv_content = VGroup(piv_t1, piv_t2, piv_t3, piv_t4).arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to(piv_card.get_center())
        piv_group = VGroup(piv_card_g, piv_content).shift(DOWN * 0.4)
        
        self.play(FadeIn(piv_group), run_time=1.0)
        self.wait(16.0)  # Voiceover: Explaining row swap when pivot is 0 and partial pivoting
        
        self.play(FadeOut(header), FadeOut(sub_pivot), FadeOut(piv_group), run_time=0.8)


# =============================================================================
# SCENE 4: STEP-BY-STEP FORWARD ELIMINATION WITH GRAPHICAL ARITHMETIC (~86s)
# =============================================================================
class Scene4_WorkedExample(Scene):
    def construct(self):
        header = Text("Scene 4: Step-by-Step Forward Elimination", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(header))
        
        current_data = [
            ["1", "2", "1", " 8"],
            ["2", "5", "3", "19"],
            ["3", "8", "6", "29"]
        ]
        
        mat_mob, cells, sep, r_lbls = create_matrix_mobject(current_data, font_size=24)
        mat_mob.shift(LEFT * 3.4 + DOWN * 0.2)
        
        self.play(FadeIn(mat_mob), run_time=1.0)
        self.wait(3.0)
        
        # ---------------------------------------------------------
        # STEP 1: PIVOT 1 (Row 1, Col 1) -> Eliminate (2,1)
        # ---------------------------------------------------------
        step_banner = Text("Step 1: Use Pivot 1 to eliminate Row 2, Column 1", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD)
        step_banner.next_to(header, DOWN, buff=0.25)
        self.play(Write(step_banner))
        
        # Amber Pivot Box and Label with clean clearance from top bracket
        pivot1_rect = SurroundingRectangle(cells[0][0], color=COLOR_ACCENT, buff=0.08, stroke_width=2.8)
        p1_text = Text("Pivot = 1", font=FONT_FAMILY, font_size=13, color=COLOR_ACCENT, weight=BOLD).next_to(pivot1_rect, UP, buff=0.12)
        target1_rect = SurroundingRectangle(cells[1][0], color=COLOR_TARGET, buff=0.08, stroke_width=2.8)
        
        self.play(Create(pivot1_rect), Write(p1_text), Create(target1_rect), run_time=1.0)
        self.wait(4.0)  # Voiceover: Pivot is 1. Target below it is 2.
        
        # Scratchpad Card 1 (Calibrated width 6.4, positioned safely inside right screen margin)
        scratch_box_g, scratch_box = create_card(width=6.4, height=3.7, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        
        tag1 = RoundedRectangle(corner_radius=0.08, width=2.1, height=0.38, color=COLOR_PRIMARY, fill_color="#EFF6FF", fill_opacity=1.0, stroke_width=1.4)
        tag1_lbl = Text("Row Operation", font=FONT_FAMILY, font_size=12, color=COLOR_PRIMARY, weight=BOLD).move_to(tag1.get_center())
        op1_txt = Text("R2  --->  R2 - 2·R1", font=FONT_FAMILY, font_size=17, color=COLOR_TITLE, weight=BOLD)
        head1 = VGroup(VGroup(tag1, tag1_lbl), op1_txt).arrange(RIGHT, buff=0.22)
        
        calc_line1 = Text("      R2 : [  2,   5,   3  |  19 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_TEXT)
        calc_line2 = Text(" - 2·R1 : [ -2,  -4,  -2  | -16 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_TARGET, weight=BOLD)
        calc_div   = Line(LEFT * 2.7, RIGHT * 2.7, color=COLOR_CARD_BORDER, stroke_width=1.8)
        calc_line3 = Text(" New R2 : [  0,   1,   1  |   3 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_SUCCESS, weight=BOLD)
        
        scratch_group = VGroup(head1, calc_line1, calc_line2, calc_div, calc_line3).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(scratch_box.get_center())
        card1 = VGroup(scratch_box_g, scratch_group).shift(RIGHT * 2.85 + DOWN * 0.2)
        
        self.play(FadeIn(card1), run_time=1.0)
        self.wait(9.0)  # Voiceover: Explaining R2 - 2R1 gives [0, 1, 1 | 3]
        
        # Update Matrix Row 2 with green ripple
        new_r2_vals = ["0", "1", "1", " 3"]
        anim_list = []
        for c in range(4):
            new_txt = Text(new_r2_vals[c], font=FONT_FAMILY, font_size=24, color=COLOR_SUCCESS if c==0 else COLOR_TEXT, weight=BOLD)
            new_txt.move_to(cells[1][c].get_center())
            anim_list.append(Transform(cells[1][c], new_txt))
            
        ripple1 = Circle(radius=0.15, color=COLOR_SUCCESS, stroke_width=3).move_to(cells[1][0].get_center())
        self.play(*anim_list, FadeOut(target1_rect), ripple1.animate.scale(2.5).set_stroke(opacity=0), run_time=1.0)
        self.remove(ripple1)
        self.wait(3.5)
        
        # ---------------------------------------------------------
        # STEP 2: PIVOT 1 (Row 1, Col 1) -> Eliminate (3,1)
        # ---------------------------------------------------------
        step2_banner = Text("Step 2: Use Pivot 1 to eliminate Row 3, Column 1", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD)
        step2_banner.next_to(header, DOWN, buff=0.25)
        self.play(Transform(step_banner, step2_banner))
        
        target2_rect = SurroundingRectangle(cells[2][0], color=COLOR_TARGET, buff=0.08, stroke_width=2.8)
        self.play(Create(target2_rect), FadeOut(card1), run_time=0.8)
        self.wait(4.0)  # Voiceover: Now eliminate the 3 in Row 3
        
        # Scratchpad Card 2
        scratch_box_g2, scratch_box2 = create_card(width=6.4, height=3.7, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        tag2 = RoundedRectangle(corner_radius=0.08, width=2.1, height=0.38, color=COLOR_PRIMARY, fill_color="#EFF6FF", fill_opacity=1.0, stroke_width=1.4)
        tag2_lbl = Text("Row Operation", font=FONT_FAMILY, font_size=12, color=COLOR_PRIMARY, weight=BOLD).move_to(tag2.get_center())
        op2_txt = Text("R3  --->  R3 - 3·R1", font=FONT_FAMILY, font_size=17, color=COLOR_TITLE, weight=BOLD)
        head2 = VGroup(VGroup(tag2, tag2_lbl), op2_txt).arrange(RIGHT, buff=0.22)
        
        calc2_line1 = Text("      R3 : [  3,   8,   6  |  29 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_TEXT)
        calc2_line2 = Text(" - 3·R1 : [ -3,  -6,  -3  | -24 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_TARGET, weight=BOLD)
        calc2_div   = Line(LEFT * 2.7, RIGHT * 2.7, color=COLOR_CARD_BORDER, stroke_width=1.8)
        calc2_line3 = Text(" New R3 : [  0,   2,   3  |   5 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_SUCCESS, weight=BOLD)
        
        scratch2_group = VGroup(head2, calc2_line1, calc2_line2, calc2_div, calc2_line3).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(scratch_box2.get_center())
        card2 = VGroup(scratch_box_g2, scratch2_group).shift(RIGHT * 2.85 + DOWN * 0.2)
        
        self.play(FadeIn(card2), run_time=1.0)
        self.wait(9.0)  # Voiceover: Explaining R3 - 3R1 gives [0, 2, 3 | 5]
        
        # Update Matrix Row 3 with green ripple
        new_r3_vals = ["0", "2", "3", " 5"]
        anim_list2 = []
        for c in range(4):
            new_txt = Text(new_r3_vals[c], font=FONT_FAMILY, font_size=24, color=COLOR_SUCCESS if c==0 else COLOR_TEXT, weight=BOLD)
            new_txt.move_to(cells[2][c].get_center())
            anim_list2.append(Transform(cells[2][c], new_txt))
            
        ripple2 = Circle(radius=0.15, color=COLOR_SUCCESS, stroke_width=3).move_to(cells[2][0].get_center())
        self.play(*anim_list2, FadeOut(target2_rect), ripple2.animate.scale(2.5).set_stroke(opacity=0), run_time=1.0)
        self.remove(ripple2)
        self.wait(3.5)
        
        col1_cleared = Text("✓ Column 1 below Pivot 1 fully cleared to 0!", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD)
        col1_cleared.next_to(mat_mob, DOWN, buff=0.35)
        self.play(FadeIn(col1_cleared))
        self.wait(4.5)
        
        self.play(FadeOut(pivot1_rect), FadeOut(p1_text), FadeOut(col1_cleared), FadeOut(card2), run_time=0.8)
        
        # ---------------------------------------------------------
        # STEP 3: PIVOT 2 (Row 2, Col 2) -> Eliminate (3,2)
        # ---------------------------------------------------------
        step3_banner = Text("Step 3: Move to Pivot 2 (Row 2, Col 2) to eliminate Row 3, Col 2", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD)
        step3_banner.next_to(header, DOWN, buff=0.25)
        self.play(Transform(step_banner, step3_banner))
        
        pivot2_rect = SurroundingRectangle(cells[1][1], color=COLOR_ACCENT, buff=0.08, stroke_width=2.8)
        p2_text = Text("Pivot = 1", font=FONT_FAMILY, font_size=13, color=COLOR_ACCENT, weight=BOLD).next_to(pivot2_rect, UP, buff=0.12)
        target3_rect = SurroundingRectangle(cells[2][1], color=COLOR_TARGET, buff=0.08, stroke_width=2.8)
        
        self.play(Create(pivot2_rect), Write(p2_text), Create(target3_rect), run_time=1.0)
        self.wait(4.0)  # Voiceover: Pivot 2 is 1. We must eliminate the 2 underneath it!
        
        # Scratchpad Card 3
        scratch_box_g3, scratch_box3 = create_card(width=6.4, height=3.7, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        tag3 = RoundedRectangle(corner_radius=0.08, width=2.1, height=0.38, color=COLOR_PRIMARY, fill_color="#EFF6FF", fill_opacity=1.0, stroke_width=1.4)
        tag3_lbl = Text("Row Operation", font=FONT_FAMILY, font_size=12, color=COLOR_PRIMARY, weight=BOLD).move_to(tag3.get_center())
        op3_txt = Text("R3  --->  R3 - 2·R2", font=FONT_FAMILY, font_size=17, color=COLOR_TITLE, weight=BOLD)
        head3 = VGroup(VGroup(tag3, tag3_lbl), op3_txt).arrange(RIGHT, buff=0.22)
        
        calc3_line1 = Text("      R3 : [  0,   2,   3  |   5 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_TEXT)
        calc3_line2 = Text(" - 2·R2 : [  0,  -2,  -2  |  -6 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_TARGET, weight=BOLD)
        calc3_div   = Line(LEFT * 2.7, RIGHT * 2.7, color=COLOR_CARD_BORDER, stroke_width=1.8)
        calc3_line3 = Text(" New R3 : [  0,   0,   1  |  -1 ]", font=FONT_FAMILY, font_size=15.5, color=COLOR_SUCCESS, weight=BOLD)
        
        scratch3_group = VGroup(head3, calc3_line1, calc3_line2, calc3_div, calc3_line3).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(scratch_box3.get_center())
        card3 = VGroup(scratch_box_g3, scratch3_group).shift(RIGHT * 2.85 + DOWN * 0.2)
        
        self.play(FadeIn(card3), run_time=1.0)
        self.wait(9.0)  # Voiceover: Explaining R3 - 2R2 gives [0, 0, 1 | -1]
        
        # Update Matrix Row 3 with ripple
        final_r3_vals = ["0", "0", "1", "-1"]
        anim_list3 = []
        for c in range(4):
            new_txt = Text(final_r3_vals[c], font=FONT_FAMILY, font_size=24, color=COLOR_SUCCESS if c in (0,1) else COLOR_TEXT, weight=BOLD)
            new_txt.move_to(cells[2][c].get_center())
            anim_list3.append(Transform(cells[2][c], new_txt))
            
        ripple3 = Circle(radius=0.15, color=COLOR_SUCCESS, stroke_width=3).move_to(cells[2][1].get_center())
        self.play(*anim_list3, FadeOut(target3_rect), ripple3.animate.scale(2.5).set_stroke(opacity=0), run_time=1.0)
        self.remove(ripple3)
        self.wait(3.5)
        
        self.play(FadeOut(pivot2_rect), FadeOut(p2_text), FadeOut(card3), run_time=0.8)
        
        # Final Echelon Celebration
        success_banner = Text("★ Success: Matrix is in Row Echelon Form (REF)!", font=FONT_FAMILY, font_size=20, color=COLOR_SUCCESS, weight=BOLD)
        success_banner.next_to(header, DOWN, buff=0.25)
        self.play(Transform(step_banner, success_banner))
        
        box_p1 = SurroundingRectangle(cells[0][0], color=COLOR_ACCENT, buff=0.08, stroke_width=3)
        box_p2 = SurroundingRectangle(cells[1][1], color=COLOR_ACCENT, buff=0.08, stroke_width=3)
        box_p3 = SurroundingRectangle(cells[2][2], color=COLOR_ACCENT, buff=0.08, stroke_width=3)
        
        self.play(Create(box_p1), Create(box_p2), Create(box_p3), run_time=1.2)
        self.wait(7.0)  # Voiceover: All 3 pivots (1, 1, 1) and zeros below. Ready for back-substitution!
        
        self.play(
            FadeOut(header), FadeOut(step_banner), FadeOut(mat_mob),
            FadeOut(box_p1), FadeOut(box_p2), FadeOut(box_p3),
            run_time=0.8
        )


# =============================================================================
# SCENE 5: BACK-SUBSTITUTION & 3D GEOMETRIC SOLUTION GRAPH (~49s)
# =============================================================================
class Scene5_BackSubstitution(Scene):
    def construct(self):
        header = Text("Scene 5: Back-Substitution & Geometric Meaning", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(header))
        
        sub = Text("Reading the uncoupled system from bottom to top", font=FONT_FAMILY, font_size=18, color=COLOR_SUBTEXT)
        sub.next_to(header, DOWN, buff=0.22)
        self.play(FadeIn(sub))
        
        # Left: Echelon Matrix in card
        ref_data = [
            ["1", "2", "1", " 8"],
            ["0", "1", "1", " 3"],
            ["0", "0", "1", "-1"]
        ]
        mat_mob, cells, sep, r_lbls = create_matrix_mobject(ref_data, font_size=24)
        mat_mob.shift(LEFT * 3.4 + DOWN * 0.4)
        
        self.play(FadeIn(mat_mob), run_time=0.8)
        self.wait(1.5)
        
        # Right: Solving Step by Step with widened cards and generous padding
        # 1. Row 3 -> z = -1
        r3_box_g, r3_box = create_card(width=6.2, height=1.1, border_color="#10B981", accent_bar_color=COLOR_SUCCESS)
        r3_txt1 = Text("From Row 3:   0x + 0y + 1z = -1", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        r3_ans  = Text("===>   z = -1", font=FONT_FAMILY, font_size=18, color=COLOR_SUCCESS, weight=BOLD)
        r3_group = VGroup(r3_txt1, r3_ans).arrange(RIGHT, buff=0.35).move_to(r3_box.get_center())
        card_r3 = VGroup(r3_box_g, r3_group).shift(RIGHT * 3.1 + UP * 1.0)
        
        hl_r3 = SurroundingRectangle(cells[2][2], color=COLOR_ACCENT, buff=0.08, stroke_width=3)
        self.play(Create(hl_r3), FadeIn(card_r3), run_time=1.0)
        self.wait(6.0)  # Voiceover: Row 3 tells us z = -1 immediately
        
        # 2. Row 2 -> y + z = 3 -> y = 4
        r2_box_g, r2_box = create_card(width=6.2, height=1.1, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        r2_txt1 = Text("From Row 2:   1y + 1(-1) = 3", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        r2_ans  = Text("===>   y = 4", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD)
        r2_group = VGroup(r2_txt1, r2_ans).arrange(RIGHT, buff=0.35).move_to(r2_box.get_center())
        card_r2 = VGroup(r2_box_g, r2_group).shift(RIGHT * 3.1 + DOWN * 0.2)
        
        hl_r2 = SurroundingRectangle(cells[1][1], color=COLOR_PRIMARY, buff=0.08, stroke_width=3)
        self.play(Create(hl_r2), FadeIn(card_r2), run_time=1.0)
        self.wait(6.5)  # Voiceover: Substitute z = -1 into row 2 to get y = 4
        
        # 3. Row 1 -> x + 2(4) + 1(-1) = 8 -> x = 1
        r1_box_g, r1_box = create_card(width=6.2, height=1.1, border_color="#F59E0B", accent_bar_color=COLOR_ACCENT)
        r1_txt1 = Text("From Row 1:   x + 2(4) + (-1) = 8", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT)
        r1_ans  = Text("===>   x = 1", font=FONT_FAMILY, font_size=18, color=COLOR_ACCENT, weight=BOLD)
        r1_group = VGroup(r1_txt1, r1_ans).arrange(RIGHT, buff=0.35).move_to(r1_box.get_center())
        card_r1 = VGroup(r1_box_g, r1_group).shift(RIGHT * 3.1 + DOWN * 1.4)
        
        hl_r1 = SurroundingRectangle(cells[0][0], color=COLOR_ACCENT, buff=0.08, stroke_width=3)
        self.play(Create(hl_r1), FadeIn(card_r1), run_time=1.0)
        self.wait(7.0)  # Voiceover: Substitute both into row 1 to get x = 1
        
        self.play(
            FadeOut(mat_mob), FadeOut(card_r3), FadeOut(card_r2), FadeOut(card_r1),
            FadeOut(hl_r3), FadeOut(hl_r2), FadeOut(hl_r1),
            run_time=0.8
        )
        
        # -------------------------------------------------------------
        # PROPER 3D GEOMETRIC REPRESENTATION WITH ANIMATED INTERSECTION
        # -------------------------------------------------------------
        sol_graph_g, ax_g, planes_list, sol_elements = create_3d_planes_graphic(origin=LEFT * 3.4 + DOWN * 0.2, scale=0.48)
        
        # Right Explanation Card with generous padding and clean outline
        sol_box_g, sol_box = create_card(width=6.0, height=3.6, border_color="#10B981", accent_bar_color=COLOR_SUCCESS)
        sol_title = Text("Unique Solution in 3D Space", font=FONT_FAMILY, font_size=18, color=COLOR_SUCCESS, weight=BOLD)
        sol_vec = Text("( x ,  y ,  z )  =  ( 1 ,  4 ,  -1 )", font=FONT_FAMILY, font_size=23, color=COLOR_PRIMARY, weight=BOLD)
        geo_desc = Text("Geometric Reality:\nEach original equation defines a 2D plane in R^3.\nThe unique solution represents the EXACT single point\nwhere all three planes intersect simultaneously!", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUBTEXT, line_spacing=0.82)
        
        sol_content = VGroup(sol_title, sol_vec, geo_desc).arrange(DOWN, buff=0.25).move_to(sol_box.get_center())
        sol_right_group = VGroup(sol_box_g, sol_content).shift(RIGHT * 3.3 + DOWN * 0.2)
        
        # Animate the 3D geometry step-by-step
        self.play(Create(ax_g), FadeIn(planes_list[0]), FadeIn(planes_list[1]), FadeIn(planes_list[2]), FadeIn(sol_right_group), run_time=1.2)
        # Solution vector draws dynamically from the origin to the intersection
        self.play(GrowArrow(sol_elements[2]), FadeIn(sol_elements[0]), Create(sol_elements[1]), run_time=1.0)
        # Projection lines drop to axes, showing the (1, 4, -1) coordinates
        self.play(Create(sol_elements[3]), FadeIn(sol_elements[4]), run_time=1.0)
        
        # Concentric beacon pulse at the 3D intersection point
        sol_pt = iso_project(1, 4, -1, origin=LEFT * 3.4 + DOWN * 0.2, scale=0.48)
        beacon = Circle(radius=0.15, color=COLOR_SUCCESS, stroke_width=3).move_to(sol_pt)
        self.play(beacon.animate.scale(2.8).set_stroke(opacity=0), run_time=1.0)
        self.remove(beacon)
        self.wait(3.8)  # Voiceover: Explaining unique 3D plane intersection
        
        self.play(FadeOut(sol_graph_g), FadeOut(sol_right_group), FadeOut(sub), run_time=0.8)
        
        # Theoretical Depth: The 3 System Outcomes / Rank Analysis (All text comfortable inside 10.6 card)
        rank_banner = Text("Theoretical Depth: What Echelon Form Reveals About Any System", font=FONT_FAMILY, font_size=18, color=COLOR_PRIMARY, weight=BOLD)
        rank_banner.next_to(header, DOWN, buff=0.25)
        self.play(Write(rank_banner))
        
        c_w, c_h = 10.6, 1.35
        
        c1_g, c1 = create_card(width=c_w, height=c_h, border_color="#10B981", accent_bar_color=COLOR_SUCCESS)
        c1_title = Text("1. Unique Solution (Our Case):", font=FONT_FAMILY, font_size=16, color=COLOR_SUCCESS, weight=BOLD)
        c1_desc  = Text("Pivots in all 3 columns (Rank = 3). The 3 planes intersect at exactly ONE single point: (1, 4, -1).", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUBTEXT)
        c1_vg = VGroup(c1_title, c1_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(c1.get_center()).shift(LEFT * 0.5)
        card_c1 = VGroup(c1_g, c1_vg)
        
        c2_g, c2 = create_card(width=c_w, height=c_h, border_color="#EF4444", accent_bar_color="#EF4444")
        c2_title = Text("2. Inconsistent System (No Solution):", font=FONT_FAMILY, font_size=16, color=COLOR_TARGET, weight=BOLD)
        c2_desc  = Text("A row like [ 0  0  0 | 5 ] implies 0 = 5 (contradiction!). The planes are parallel and never intersect.", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUBTEXT)
        c2_vg = VGroup(c2_title, c2_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(c2.get_center()).shift(LEFT * 0.5)
        card_c2 = VGroup(c2_g, c2_vg)
        
        c3_g, c3 = create_card(width=c_w, height=c_h, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        c3_title = Text("3. Infinite Solutions (Underdetermined / Dependent):", font=FONT_FAMILY, font_size=16, color=COLOR_PRIMARY, weight=BOLD)
        c3_desc  = Text("A zero row [ 0  0  0 | 0 ] leaves free variables. The planes intersect along an entire shared line or plane.", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUBTEXT)
        c3_vg = VGroup(c3_title, c3_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(c3.get_center()).shift(LEFT * 0.5)
        card_c3 = VGroup(c3_g, c3_vg)
        
        cards_cases = VGroup(card_c1, card_c2, card_c3).arrange(DOWN, buff=0.22).shift(DOWN * 0.45)
        
        self.play(FadeIn(card_c1), run_time=0.8)
        self.wait(3.5)
        self.play(FadeIn(card_c2), run_time=0.8)
        self.wait(4.0)
        self.play(FadeIn(card_c3), run_time=0.8)
        self.wait(5.5)  # Voiceover: Explaining the 3 possible outcomes of linear systems
        
        self.play(FadeOut(header), FadeOut(rank_banner), FadeOut(cards_cases), run_time=0.8)


# =============================================================================
# SCENE 6: SUMMARY, ALGORITHMIC EFFICIENCY GRAPH & CLEAN OUTRO (~34s)
# =============================================================================
class Scene6_SummaryAndCredits(Scene):
    def construct(self):
        # 1. Three Core Takeaways (04:57 – 05:14)
        t_header = Text("Core Takeaways & Recap", font=FONT_FAMILY, font_size=28, color=COLOR_TITLE, weight=BOLD).to_edge(UP, buff=0.55)
        self.play(Write(t_header))
        
        tk_w, tk_h = 10.6, 1.25
        
        c1_g, c1 = create_card(width=tk_w, height=tk_h, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        t1_title = Text("1. Augmented Matrix Representation", font=FONT_FAMILY, font_size=17, color=COLOR_PRIMARY, weight=BOLD)
        t1_desc = Text("Removes algebraic variable clutter and stores clean numerical coefficients [A | b].", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUBTEXT)
        t1_vg = VGroup(t1_title, t1_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(c1.get_center()).shift(LEFT * 0.5)
        card1 = VGroup(c1_g, t1_vg)
        
        c2_g, c2 = create_card(width=tk_w, height=tk_h, border_color="#F59E0B", accent_bar_color=COLOR_ACCENT)
        t2_title = Text("2. Systematic Elimination via Pivots", font=FONT_FAMILY, font_size=17, color=COLOR_ACCENT, weight=BOLD)
        t2_desc = Text("Elementary row operations create zeros below each pivot, forming the upper triangular REF.", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUBTEXT)
        t2_vg = VGroup(t2_title, t2_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(c2.get_center()).shift(LEFT * 0.5)
        card2 = VGroup(c2_g, t2_vg)
        
        c3_g, c3 = create_card(width=tk_w, height=tk_h, border_color="#10B981", accent_bar_color=COLOR_SUCCESS)
        t3_title = Text("3. Seamless Back-Substitution", font=FONT_FAMILY, font_size=17, color=COLOR_SUCCESS, weight=BOLD)
        t3_desc = Text("Once decoupled into echelon form, bottom-up substitution yields the unique solution rapidly.", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUBTEXT)
        t3_vg = VGroup(t3_title, t3_desc).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(c3.get_center()).shift(LEFT * 0.5)
        card3 = VGroup(c3_g, t3_vg)
        
        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.24).shift(DOWN * 0.45)
        
        self.play(FadeIn(card1), run_time=0.8)
        self.wait(4.5)
        self.play(FadeIn(card2), run_time=0.8)
        self.wait(4.5)
        self.play(FadeIn(card3), run_time=0.8)
        self.wait(6.5)  # Voiceover: Summarizing the 3 key pillars
        
        self.play(FadeOut(t_header), FadeOut(cards), run_time=0.8)
        
        # 2. Algorithmic Horizon: REF vs RREF + Animated Computational Complexity Bar Graph!
        rref_header = Text("Algorithmic Horizon: REF vs. Reduced Row Echelon Form (RREF)", font=FONT_FAMILY, font_size=20, color=COLOR_PRIMARY, weight=BOLD).to_edge(UP, buff=0.55)
        self.play(Write(rref_header))
        
        # Left: Clean Information Card with calibrated text wrapping and zero overflow
        rref_box_g, rref_box = create_card(width=7.2, height=4.1, border_color="#38BDF8", accent_bar_color=COLOR_PRIMARY)
        
        rref_p1 = Text("• Gaussian Elimination stops at Row Echelon Form (Upper Triangular)\n  followed by efficient bottom-up Back-Substitution.", font=FONT_FAMILY, font_size=13.5, color=COLOR_TEXT, line_spacing=0.85)
        rref_p2 = Text("• Gauss-Jordan Elimination continues upwards to RREF,\n  eliminating all entries ABOVE every pivot as well.", font=FONT_FAMILY, font_size=13.5, color=COLOR_PRIMARY, weight=BOLD, line_spacing=0.85)
        rref_p3 = Text("• The augmented matrix transforms directly into [ I | x ],\n  revealing the exact solution vector without back-substitution!", font=FONT_FAMILY, font_size=13.5, color=COLOR_SUCCESS, weight=BOLD, line_spacing=0.85)
        rref_p4 = Text("• Computational Gold Standard: Gaussian Elimination requires\n  ~50% FEWER operations, making it standard in scientific solvers.", font=FONT_FAMILY, font_size=12.5, color=COLOR_SUBTEXT, line_spacing=0.85)
        
        rref_vg = VGroup(rref_p1, rref_p2, rref_p3, rref_p4).arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to(rref_box.get_center())
        left_info = VGroup(rref_box_g, rref_vg).shift(LEFT * 3.1 + DOWN * 0.35)
        
        # Right: Animated Computational Complexity Bar Chart!
        chart_box_g, chart_box = create_card(width=4.1, height=4.1, border_color="#CBD5E1", accent_bar_color=COLOR_ACCENT)
        chart_title = Text("Operation Count\n(Computational FLOPs)", font=FONT_FAMILY, font_size=12.5, color=COLOR_TITLE, weight=BOLD, line_spacing=0.8).move_to(chart_box.get_top() + DOWN * 0.38)
        
        # Axis base line
        base_line = Line(chart_box.get_bottom() + UP * 0.75 + LEFT * 1.5, chart_box.get_bottom() + UP * 0.75 + RIGHT * 1.5, color="#94A3B8", stroke_width=2)
        
        # Bar 1: Gaussian Elimination (~ 2/3 n^3)
        bar1 = Rectangle(width=0.92, height=1.1, color=COLOR_PRIMARY, fill_color=COLOR_PRIMARY, fill_opacity=0.85)
        bar1.next_to(base_line, UP, buff=0).shift(LEFT * 0.7)
        lbl_b1_top = Text("~ 2/3 n^3", font=FONT_FAMILY, font_size=12, color=COLOR_PRIMARY, weight=BOLD).next_to(bar1, UP, buff=0.08)
        lbl_b1_bot = Text("Gaussian\n(REF)", font=FONT_FAMILY, font_size=11, color=COLOR_TEXT, weight=BOLD, line_spacing=0.8).next_to(bar1, DOWN, buff=0.1)
        
        # Bar 2: Gauss-Jordan (~ n^3, 50% taller)
        bar2 = Rectangle(width=0.92, height=1.65, color=COLOR_ACCENT, fill_color=COLOR_ACCENT, fill_opacity=0.85)
        bar2.next_to(base_line, UP, buff=0).shift(RIGHT * 0.7)
        lbl_b2_top = Text("~ n^3", font=FONT_FAMILY, font_size=12, color=COLOR_ACCENT, weight=BOLD).next_to(bar2, UP, buff=0.08)
        lbl_b2_bot = Text("Gauss-Jordan\n(RREF)", font=FONT_FAMILY, font_size=11, color=COLOR_TEXT, weight=BOLD, line_spacing=0.8).next_to(bar2, DOWN, buff=0.1)
        
        # +50% operations badge
        diff_badge = RoundedRectangle(corner_radius=0.08, width=1.9, height=0.36, color="#DC2626", fill_color="#FEE2E2", fill_opacity=1.0, stroke_width=1.4)
        diff_txt = Text("+50% FLOPs", font=FONT_FAMILY, font_size=11, color="#DC2626", weight=BOLD).move_to(diff_badge.get_center())
        diff_callout = VGroup(diff_badge, diff_txt).next_to(lbl_b2_top, UP, buff=0.18)
        
        chart_group = VGroup(chart_box_g, chart_title, base_line, bar1, lbl_b1_top, lbl_b1_bot, bar2, lbl_b2_top, lbl_b2_bot, diff_callout).shift(RIGHT * 4.1 + DOWN * 0.35)
        
        self.play(FadeIn(left_info), FadeIn(chart_box_g), Write(chart_title), Create(base_line), run_time=1.0)
        self.play(GrowFromEdge(bar1, DOWN), Write(lbl_b1_top), Write(lbl_b1_bot), run_time=0.8)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl_b2_top), Write(lbl_b2_bot), FadeIn(diff_callout), run_time=0.8)
        
        # Stays on screen till concluding narration finishes!
        self.wait(14.0)
        self.play(FadeOut(rref_header), FadeOut(left_info), FadeOut(chart_group), run_time=1.2)
