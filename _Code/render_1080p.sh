#!/usr/bin/env bash
set -e

echo "=================================================="
echo "Rendering Gaussian Elimination Video at 1080p HD"
echo "Student: Dheeraj | Student ID: E25B070814"
echo "=================================================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$SCRIPT_DIR"

MANIM_BIN="/opt/homebrew/bin/manim"
FFMPEG_BIN="/opt/homebrew/bin/ffmpeg"

echo ">>> Rendering Scene 1: Hook and Context..."
$MANIM_BIN -r 1920,1080 --fps 30 gaussian_elimination.py Scene1_HookAndContext

echo ">>> Rendering Scene 2: Augmented Matrix & EROs..."
$MANIM_BIN -r 1920,1080 --fps 30 gaussian_elimination.py Scene2_AugmentedMatrixAndEROs

echo ">>> Rendering Scene 3: Row Echelon Form & Pivots..."
$MANIM_BIN -r 1920,1080 --fps 30 gaussian_elimination.py Scene3_RowEchelonFormAndPivots

echo ">>> Rendering Scene 4: Worked Example Step-by-Step..."
$MANIM_BIN -r 1920,1080 --fps 30 gaussian_elimination.py Scene4_WorkedExample

echo ">>> Rendering Scene 5: Back-Substitution..."
$MANIM_BIN -r 1920,1080 --fps 30 gaussian_elimination.py Scene5_BackSubstitution

echo ">>> Rendering Scene 6: Summary and Credits..."
$MANIM_BIN -r 1920,1080 --fps 30 gaussian_elimination.py Scene6_SummaryAndCredits

VIDEO_DIR="$SCRIPT_DIR/media/videos/gaussian_elimination/1080p30"

cat << EOF > "$VIDEO_DIR/concat_list.txt"
file 'Scene1_HookAndContext.mp4'
file 'Scene2_AugmentedMatrixAndEROs.mp4'
file 'Scene3_RowEchelonFormAndPivots.mp4'
file 'Scene4_WorkedExample.mp4'
file 'Scene5_BackSubstitution.mp4'
file 'Scene6_SummaryAndCredits.mp4'
EOF

echo ">>> Concatenating into final 1080p MP4..."
$FFMPEG_BIN -y -f concat -safe 0 -i "$VIDEO_DIR/concat_list.txt" -c copy "$ROOT_DIR/_Video.mp4"

echo "=================================================="
echo "SUCCESS! Render complete: $ROOT_DIR/_Video.mp4"
echo "=================================================="
