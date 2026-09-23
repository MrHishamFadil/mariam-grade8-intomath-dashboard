# -*- coding: utf-8 -*-
"""
module2_mcqs.py
Master Curriculum Practice Question Bank: 20 MCQs each for Lessons 2.1, 2.2, and 2.3.
HMH Into Math Grade 8 Teacher Edition - Module 2: Transformations and Similarity
"""

MODULE_2_MCQS = {
    "2.1": [
        {
            "id": "p-2-1-mcq-1",
            "q": "Which scale factor \\(k\\) produces an **enlargement** of a geometric figure?",
            "opts": [
                "\\(k = \\frac{3}{4}\\)",
                "\\(k = 0.85\\)",
                "\\(k = 1.0\\)",
                "\\(k = \\frac{5}{3}\\)"
            ],
            "correct": 3,
            "hint": "An enlargement occurs when the scale factor is strictly greater than 1 (\\(k > 1\\)).",
            "explanation": "Step 1: Recall the classification rule for scale factors: if \\(k > 1\\), the transformation is an enlargement; if \\(0 < k < 1\\), it is a reduction; if \\(k = 1\\), the figure remains congruent.\nStep 2: Evaluate the choices: \\(\\frac{3}{4} = 0.75 < 1\\) (reduction), \\(0.85 < 1\\) (reduction), \\(1.0\\) (congruent), and \\(\\frac{5}{3} \\approx 1.67 > 1\\) (enlargement).\nConclusion: Only \\(k = \\frac{5}{3}\\) represents an enlargement.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-1-mcq-2",
            "q": "An original photograph has a width of \\(4\\text{ inches}\\). It is enlarged proportionally so the new width is \\(14\\text{ inches}\\). What is the scale factor \\(k\\)?",
            "opts": [
                "\\(k = 0.28\\)",
                "\\(k = 2.5\\)",
                "\\(k = 3.5\\)",
                "\\(k = 10\\)"
            ],
            "correct": 2,
            "hint": "Use the formula: \\(k = \\frac{\\text{Image Dimension}}{\\text{Preimage Dimension}}\\).",
            "explanation": "Step 1: Identify dimensions: Preimage width = \\(4\\text{ in}\\), Image width = \\(14\\text{ in}\\).\nStep 2: Calculate scale factor: \\(k = \\frac{14}{4} = \\frac{7}{2} = 3.5\\).\nStep 3: Check classification: Since \\(3.5 > 1\\), it is an enlargement by a factor of 3.5.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-1-mcq-3",
            "q": "A blueprint architectural drawing uses a scale factor of \\(k = \\frac{1}{50}\\) compared to actual room dimensions. If a wall in the real room is \\(600\\text{ cm}\\) long, what is its length on the blueprint?",
            "opts": [
                "\\(6\\text{ cm}\\)",
                "\\(12\\text{ cm}\\)",
                "\\(50\\text{ cm}\\)",
                "\\(300\\text{ cm}\\)"
            ],
            "correct": 1,
            "hint": "Multiply the real dimension by the scale factor \\(k\\).",
            "explanation": "Step 1: Apply the scaling formula: \\(\\text{Image Length} = k \\times \\text{Preimage Length}\\).\nStep 2: Substitute values: \\(\\text{Blueprint Length} = \\frac{1}{50} \\times 600 = \\frac{600}{50} = 12\\text{ cm}\\).\nConclusion: The blueprint drawing represents the wall with a segment of \\(12\\text{ cm}\\).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-4",
            "q": "If a square with side length \\(6\\text{ cm}\\) is dilated by a scale factor of \\(k = 2.5\\), what is the perimeter of the dilated square?",
            "opts": [
                "\\(15\\text{ cm}\\)",
                "\\(24\\text{ cm}\\)",
                "\\(60\\text{ cm}\\)",
                "\\(150\\text{ cm}\\)"
            ],
            "correct": 2,
            "hint": "The perimeter scales directly by \\(k\\): \\(P_{\\text{image}} = k \\times P_{\\text{preimage}}\\).",
            "explanation": "Step 1: Calculate the original perimeter: A square with side \\(s = 6\\text{ cm}\\) has perimeter \\(P = 4s = 4(6) = 24\\text{ cm}\\).\nStep 2: Apply the perimeter scaling theorem: \\(P_{\\text{image}} = k \\times P_{\\text{preimage}} = 2.5 \\times 24 = 60\\text{ cm}\\).\nAlternatively, new side length = \\(2.5 \\times 6 = 15\\text{ cm}\\), so new perimeter = \\(4 \\times 15 = 60\\text{ cm}\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-5",
            "q": "A triangle with an area of \\(18\\text{ cm}^2\\) is dilated by a scale factor of \\(k = 3\\). What is the area of the resulting dilated triangle?",
            "opts": [
                "\\(54\\text{ cm}^2\\)",
                "\\(108\\text{ cm}^2\\)",
                "\\(162\\text{ cm}^2\\)",
                "\\(324\\text{ cm}^2\\)"
            ],
            "correct": 2,
            "hint": "Recall the Area Multiplier rule: \\(\\text{Area}_{\\text{image}} = k^2 \\times \\text{Area}_{\\text{preimage}}\\).",
            "explanation": "Step 1: Remember that when linear dimensions scale by \\(k\\), two-dimensional surface area scales by \\(k^2\\).\nStep 2: Compute the area multiplier: \\(k^2 = 3^2 = 9\\).\nStep 3: Calculate the new area: \\(\\text{Area}_{\\text{image}} = 9 \\times 18 = 162\\text{ cm}^2\\).\nWhy not 54? 54 is \\(3 \\times 18\\), which incorrectly applies linear scaling to area.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-6",
            "q": "Under any dilation with scale factor \\(k > 0\\), what happens to the measures of corresponding angles?",
            "opts": [
                "They are multiplied by \\(k\\)",
                "They remain exactly equal (preserved: \\(m\\angle A' = m\\angle A\\))",
                "They increase if \\(k > 1\\) and decrease if \\(k < 1\\)",
                "They are multiplied by \\(k^2\\)"
            ],
            "correct": 1,
            "hint": "Dilations preserve the shape of figures. Does resizing a photograph stretch the corners into different angles?",
            "explanation": "Step 1: A dilation preserves shape, collinearity, betweenness, and angle measures.\nStep 2: Under all dilations, corresponding angles are strictly congruent: \\(m\\angle A' = m\\angle A\\).\nStep 3: Only linear segment lengths change by factor \\(k\\), while angles never scale by \\(k\\).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-1-mcq-7",
            "q": "A microscope magnifies an insect specimen from an actual length of \\(0.8\\text{ mm}\\) to an image length of \\(28\\text{ mm}\\). What is the magnification scale factor?",
            "opts": [
                "\\(k = 22.4\\)",
                "\\(k = 28\\)",
                "\\(k = 35\\)",
                "\\(k = 350\\)"
            ],
            "correct": 2,
            "hint": "Divide the image length by the actual specimen length: \\(k = \\frac{28}{0.8}\\).",
            "explanation": "Step 1: Set up the ratio: \\(k = \\frac{\\text{Image}}{\\text{Preimage}} = \\frac{28\\text{ mm}}{0.8\\text{ mm}}\\).\nStep 2: Divide: \\(\\frac{28}{0.8} = \\frac{280}{8} = 35\\).\nConclusion: The microscope provides a \\(35\\times\\) magnification enlargement.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-1-mcq-8",
            "q": "If the perimeter of an image is \\(45\\text{ cm}\\) and the perimeter of the preimage was \\(60\\text{ cm}\\), what was the scale factor \\(k\\) of the dilation?",
            "opts": [
                "\\(k = \\frac{3}{4}\\)",
                "\\(k = \\frac{4}{3}\\)",
                "\\(k = 15\\)",
                "\\(k = \\frac{9}{16}\\)"
            ],
            "correct": 0,
            "hint": "Use \\(k = \\frac{P_{\\text{image}}}{P_{\\text{preimage}}}\\).",
            "explanation": "Step 1: The perimeter ratio equals the scale factor: \\(k = \\frac{P_{\\text{image}}}{P_{\\text{preimage}}}\\).\nStep 2: Substitute values: \\(k = \\frac{45}{60}\\).\nStep 3: Simplify by dividing top and bottom by 15: \\(k = \\frac{3}{4} = 0.75\\).\nConclusion: Since \\(k = 0.75 < 1\\), this is a reduction.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-9",
            "q": "A graphic designer scales a rectangle from \\(8\\text{ cm} \\times 12\\text{ cm}\\) to a smaller icon measuring \\(2\\text{ cm} \\times 3\\text{ cm}\\). Which statement is true?",
            "opts": [
                "This is a reduction with scale factor \\(k = \\frac{1}{4}\\)",
                "This is an enlargement with scale factor \\(k = 4\\)",
                "This is a reduction with scale factor \\(k = \\frac{1}{6}\\)",
                "The transformation is non-proportional because dimensions differ"
            ],
            "correct": 0,
            "hint": "Check width ratio: \\(\\frac{2}{8}\\) and length ratio: \\(\\frac{3}{12}\\).",
            "explanation": "Step 1: Check proportionality: \\(\\frac{2}{8} = \\frac{1}{4}\\) and \\(\\frac{3}{12} = \\frac{1}{4}\\). Since both dimensions have the same ratio \\(k = \\frac{1}{4}\\), the scaling is proportional.\nStep 2: Classify: Because \\(0 < k = \\frac{1}{4} < 1\\), this transformation is a reduction.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-1-mcq-10",
            "q": "If a circular rug with radius \\(3\\text{ ft}\\) is replaced with a similar rug dilated by \\(k = 4\\), how does the floor area covered by the new rug compare to the original rug?",
            "opts": [
                "It is \\(4\\) times as large",
                "It is \\(8\\) times as large",
                "It is \\(12\\) times as large",
                "It is \\(16\\) times as large"
            ],
            "correct": 3,
            "hint": "Area scales by \\(k^2\\).",
            "explanation": "Step 1: Linear dimensions (such as radius) are multiplied by \\(k = 4\\).\nStep 2: Area scales by the square of the scale factor: \\(k^2 = 4^2 = 16\\).\nConclusion: The new rug covers \\(16\\) times as much floor area as the original rug.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-11",
            "q": "Which of the following values of \\(k\\) represents a dilation that preserves the congruence of a figure (an isometry)?",
            "opts": [
                "\\(k = 0\\)",
                "\\(k = 0.5\\)",
                "\\(k = 1\\)",
                "\\(k = 2\\)"
            ],
            "correct": 2,
            "hint": "When does the size of a figure remain completely unchanged?",
            "explanation": "Step 1: If \\(k = 1\\), every length is multiplied by 1: \\(L' = 1 \\cdot L = L\\).\nStep 2: All segment lengths and angle measures are unchanged, so the preimage and image are congruent (\\(\\cong\\)).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-1-mcq-12",
            "q": "A photo has dimensions \\(5\\text{ in} \\times 7\\text{ in}\\). A printer resizes it to \\(15\\text{ in} \\times 20\\text{ in}\\). Did the printer perform a proportional enlargement?",
            "opts": [
                "Yes, because both dimensions increased.",
                "No, because \\(\\frac{15}{5} = 3\\) but \\(\\frac{20}{7} \\approx 2.86\\), so ratios are not equal.",
                "Yes, because the scale factor is \\(k = 3\\).",
                "No, because the area did not increase."
            ],
            "correct": 1,
            "hint": "For a dilation to be valid, all corresponding side ratios must be equal to the same constant \\(k\\).",
            "explanation": "Step 1: Calculate the width ratio: \\(\\frac{15}{5} = 3.0\\).\nStep 2: Calculate the length ratio: \\(\\frac{20}{7} \\approx 2.857\\).\nStep 3: Compare ratios: Since \\(3.0 \\neq 2.857\\), the dimensions did not scale by the same factor. This distorts the image and is not a proportional dilation.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-1-mcq-13",
            "q": "An equilateral triangle has perimeter \\(36\\text{ cm}\\). It undergoes a reduction with scale factor \\(k = \\frac{2}{3}\\). What is the side length of the reduced triangle?",
            "opts": [
                "\\(6\\text{ cm}\\)",
                "\\(8\\text{ cm}\\)",
                "\\(12\\text{ cm}\\)",
                "\\(24\\text{ cm}\\)"
            ],
            "correct": 1,
            "hint": "First find the original side length, then multiply by \\(k = \\frac{2}{3}\\).",
            "explanation": "Step 1: Original side length = \\(\\frac{36}{3} = 12\\text{ cm}\\).\nStep 2: Apply scale factor: \\(s' = k \\times s = \\frac{2}{3} \\times 12 = 8\\text{ cm}\\).\nCheck: New perimeter = \\(3 \\times 8 = 24\\text{ cm}\\), which equals \\(\\frac{2}{3} \\times 36 = 24\\text{ cm}\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-14",
            "q": "If quadrilateral \\(ABCD\\) is dilated to form quadrilateral \\(A'B'C'D'\\) with \\(k = 0.4\\), what is the ratio of \\(\\text{Area}(A'B'C'D')\\) to \\(\\text{Area}(ABCD)\\)?",
            "opts": [
                "\\(0.16\\)",
                "\\(0.4\\)",
                "\\(0.8\\)",
                "\\(1.6\\)"
            ],
            "correct": 0,
            "hint": "The area ratio is \\(k^2\\). Compute \\(0.4^2\\).",
            "explanation": "Step 1: Area scaling rule: \\(\\frac{\\text{Area}_{\\text{image}}}{\\text{Area}_{\\text{preimage}}} = k^2\\).\nStep 2: Compute \\(k^2 = (0.4)^2 = 0.16\\).\nConclusion: The area of the image is \\(0.16\\) (or \\(16\\%\\)) of the original area.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-15",
            "q": "A map has a scale of \\(1\\text{ cm} = 25\\text{ km}\\). Two towns are \\(4.8\\text{ cm}\\) apart on the map. What is the actual distance between them?",
            "opts": [
                "\\(5.2\\text{ km}\\)",
                "\\(100\\text{ km}\\)",
                "\\(120\\text{ km}\\)",
                "\\(250\\text{ km}\\)"
            ],
            "correct": 2,
            "hint": "Multiply the map distance in cm by 25 km/cm.",
            "explanation": "Step 1: Set up the proportion: \\(\\text{Actual Distance} = 4.8\\text{ cm} \\times 25\\text{ km/cm}\\).\nStep 2: Calculate: \\(4.8 \\times 25 = 4.8 \\times \\frac{100}{4} = 1.2 \\times 100 = 120\\text{ km}\\).\nConclusion: The towns are \\(120\\text{ km}\\) apart.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-16",
            "q": "Which transformation does NOT preserve segment length?",
            "opts": [
                "Translation 5 units left",
                "Reflection across the x-axis",
                "Rotation 180° about the origin",
                "Dilation by scale factor \\(k = 1.2\\)"
            ],
            "correct": 3,
            "hint": "Rigid motions preserve distance; dilations (with \\(k \\neq 1\\)) change distance.",
            "explanation": "Translations, reflections, and rotations are rigid motions (isometries) that preserve segment lengths. A dilation with \\(k = 1.2\\) increases lengths by \\(20\\%\\), so it does not preserve distance.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-2-1-mcq-17",
            "q": "If two polygons are similar with a scale factor of \\(k = \\frac{5}{2}\\), what is the ratio of their perimeters?",
            "opts": [
                "\\(\\frac{2}{5}\\)",
                "\\(\\frac{5}{2}\\)",
                "\\(\\frac{25}{4}\\)",
                "\\(\\frac{125}{8}\\)"
            ],
            "correct": 1,
            "hint": "Perimeter is a one-dimensional measure, so its ratio equals \\(k\\).",
            "explanation": "Step 1: Perimeter is the sum of side lengths (1D measurement).\nStep 2: Under dilation, every side length scales by \\(k\\), so the sum of side lengths also scales by \\(k\\).\nConclusion: The ratio of perimeters is exactly \\(k = \\frac{5}{2}\\).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-18",
            "q": "A right triangle has legs of length \\(3\\text{ cm}\\) and \\(4\\text{ cm}\\), with hypotenuse \\(5\\text{ cm}\\). After an enlargement, the hypotenuse is \\(15\\text{ cm}\\). What are the lengths of the two legs in the image?",
            "opts": [
                "\\(6\\text{ cm}\\) and \\(8\\text{ cm}\\)",
                "\\(9\\text{ cm}\\) and \\(12\\text{ cm}\\)",
                "\\(10\\text{ cm}\\) and \\(12\\text{ cm}\\)",
                "\\(15\\text{ cm}\\) and \\(20\\text{ cm}\\)"
            ],
            "correct": 1,
            "hint": "Find \\(k = \\frac{15}{5} = 3\\), then multiply each leg by 3.",
            "explanation": "Step 1: Find scale factor: \\(k = \\frac{\\text{Image Hypotenuse}}{\\text{Preimage Hypotenuse}} = \\frac{15}{5} = 3\\).\nStep 2: Multiply each leg by \\(k = 3\\): Leg 1 = \\(3 \\times 3 = 9\\text{ cm}\\); Leg 2 = \\(4 \\times 3 = 12\\text{ cm}\\).\nCheck: \\(\\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15\\text{ cm}\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-1-mcq-19",
            "q": "A scale factor of \\(k = 0.05\\) is applied to an original drawing. How does the size of the image compare to the original?",
            "opts": [
                "The image is \\(5\\text{ times}\\) larger than the original.",
                "The image is \\(20\\text{ times}\\) larger than the original.",
                "The image is \\(\\frac{1}{20}\\) of the original size (a reduction).",
                "The image is identical in size to the original."
            ],
            "correct": 2,
            "hint": "Express \\(0.05\\) as a fraction: \\(0.05 = \\frac{5}{100} = \\frac{1}{20}\\).",
            "explanation": "Step 1: Convert decimal to fraction: \\(k = 0.05 = \\frac{5}{100} = \\frac{1}{20}\\).\nStep 2: Since \\(0 < k < 1\\), it is a reduction.\nStep 3: The image lengths are \\(\\frac{1}{20}\\) (or \\(5\\%\\)) of the original dimensions.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-1-mcq-20",
            "q": "If the area of an image triangle is \\(100\\text{ ft}^2\\) and the area of the original preimage was \\(4\\text{ ft}^2\\), what was the scale factor \\(k\\) of the dilation?",
            "opts": [
                "\\(k = 5\\)",
                "\\(k = 10\\)",
                "\\(k = 25\\)",
                "\\(k = 50\\)"
            ],
            "correct": 0,
            "hint": "Recall \\(\\frac{\\text{Area}_{\\text{image}}}{\\text{Area}_{\\text{preimage}}} = k^2\\). Solve for \\(k = \\sqrt{\\frac{100}{4}}\\).",
            "explanation": "Step 1: Area ratio formula: \\(k^2 = \\frac{\\text{Area}_{\\text{image}}}{\\text{Area}_{\\text{preimage}}} = \\frac{100}{4} = 25\\).\nStep 2: Solve for linear scale factor: \\(k = \\sqrt{25} = 5\\).\nConclusion: The linear scale factor was \\(k = 5\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        }
    ],

    "2.2": [
        {
            "id": "p-2-2-mcq-1",
            "q": "What is the coordinate rule for a dilation centered at the origin \\((0, 0)\\) with scale factor \\(k\\)?",
            "opts": [
                "\\((x, y) \\to (x + k, y + k)\\)",
                "\\((x, y) \\to (kx, ky)\\)",
                "\\((x, y) \\to (\\frac{x}{k}, \\frac{y}{k})\\)",
                "\\((x, y) \\to (kx + a, ky + b)\\)"
            ],
            "correct": 1,
            "hint": "Each coordinate of every point is multiplied directly by the scale factor \\(k\\).",
            "explanation": "The standard algebraic mapping rule for a dilation centered at the origin with scale factor \\(k\\) is \\((x, y) \\to (kx, ky)\\). Both coordinates are scaled by \\(k\\).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-2",
            "q": "Point \\(P(4, -6)\\) is dilated with center at the origin and scale factor \\(k = 2.5\\). What are the coordinates of \\(P'\\)?",
            "opts": [
                "\\((6.5, -3.5)\\)",
                "\\((8, -12)\\)",
                "\\((10, -15)\\)",
                "\\((16, -24)\\)"
            ],
            "correct": 2,
            "hint": "Multiply both the x- and y-coordinates by 2.5: \\(x' = 2.5 \\times 4\\), \\(y' = 2.5 \\times (-6)\\).",
            "explanation": "Step 1: Apply the rule \\((x, y) \\to (kx, ky)\\) with \\(k = 2.5\\).\nStep 2: Calculate \\(x' = 2.5 \\times 4 = 10\\).\nStep 3: Calculate \\(y' = 2.5 \\times (-6) = -15\\).\nConclusion: The image coordinates are \\(P'(10, -15)\\).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-3",
            "q": "Point \\(A(-8, 12)\\) maps to \\(A'(-2, 3)\\) under a dilation centered at the origin. What is the scale factor \\(k\\)?",
            "opts": [
                "\\(k = -4\\)",
                "\\(k = \\frac{1}{4}\\)",
                "\\(k = 4\\)",
                "\\(k = -\\frac{1}{4}\\)"
            ],
            "correct": 1,
            "hint": "Divide the image coordinate by the preimage coordinate: \\(k = \\frac{-2}{-8}\\).",
            "explanation": "Step 1: Use \\(k = \\frac{x'}{x} = \\frac{-2}{-8} = \\frac{1}{4}\\).\nStep 2: Verify with y-coordinates: \\(k = \\frac{y'}{y} = \\frac{3}{12} = \\frac{1}{4}\\).\nStep 3: Since both ratios equal \\(\\frac{1}{4}\\), the scale factor is \\(k = \\frac{1}{4}\\) (a reduction). Scale factors are always positive.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-4",
            "q": "Under a dilation centered at the origin, a point, its image, and the origin always lie on:",
            "opts": [
                "A circle centered at the origin",
                "The same straight ray extending from the origin",
                "Perpendicular lines",
                "Opposite quadrants"
            ],
            "correct": 1,
            "hint": "A dilation expands or contracts figures along rays originating from the center of dilation.",
            "explanation": "By geometric definition of dilation, for any point \\(P\\) and center \\(O\\), the image \\(P'\\) lies on ray \\(OP\\) such that \\(OP' = k \\cdot OP\\). Therefore, \\(O\\), \\(P\\), and \\(P'\\) are collinear.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-5",
            "q": "Triangle \\(ABC\\) has vertices \\(A(0, 0)\\), \\(B(3, 0)\\), and \\(C(0, 4)\\). If it is dilated by scale factor \\(k = 3\\) centered at the origin, what is the length of the image hypotenuse \\(B'C'\\)?",
            "opts": [
                "\\(5\\text{ units}\\)",
                "\\(12\\text{ units}\\)",
                "\\(15\\text{ units}\\)",
                "\\(25\\text{ units}\\)"
            ],
            "correct": 2,
            "hint": "Original hypotenuse \\(BC = \\sqrt{3^2 + 4^2} = 5\\). Multiply by \\(k = 3\\).",
            "explanation": "Step 1: Find original hypotenuse: \\(BC = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = 5\\).\nStep 2: Dilating with \\(k = 3\\) multiplies all side lengths by 3.\nStep 3: Length \\(B'C' = k \\times BC = 3 \\times 5 = 15\\text{ units}\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-6",
            "q": "If the center of dilation is at the origin \\((0, 0)\\), what happens to the origin itself under any scale factor \\(k\\)?",
            "opts": [
                "It moves to \\((k, k)\\)",
                "It is undefined",
                "It remains invariant at \\((0, 0)\\)",
                "It is reflected to \\((-k, -k)\\)"
            ],
            "correct": 2,
            "hint": "Multiply \\((0, 0)\\) by \\(k\\): \\((k \\cdot 0, k \\cdot 0)\\).",
            "explanation": "Under the mapping \\((x, y) \\to (kx, ky)\\), the origin maps to \\((k \\cdot 0, k \\cdot 0) = (0, 0)\\). The center of dilation is the only fixed point invariant under the dilation.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-7",
            "q": "The image of point \\(M\\) after a dilation with \\(k = \\frac{1}{3}\\) centered at the origin is \\(M'(-5, 2)\\). What were the original coordinates of preimage \\(M\\)?",
            "opts": [
                "\\((-\\frac{5}{3}, \\frac{2}{3})\\)",
                "\\((-15, 6)\\)",
                "\\((-8, 5)\\)",
                "\\((15, -6)\\)"
            ],
            "correct": 1,
            "hint": "To reverse the dilation, divide by \\(k\\) (or multiply by 3): \\(x = \\frac{x'}{k}\\).",
            "explanation": "Step 1: If \\(x' = kx\\), then \\(x = \\frac{x'}{k} = \\frac{-5}{1/3} = -5 \\times 3 = -15\\).\nStep 2: Similarly, \\(y = \\frac{y'}{k} = \\frac{2}{1/3} = 2 \\times 3 = 6\\).\nConclusion: The preimage coordinates were \\(M(-15, 6)\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-8",
            "q": "Which of the following points is \\(6\\text{ units}\\) from the origin after undergoing a dilation with \\(k = 2\\) from an original point \\(P(0, 3)\\)?",
            "opts": [
                "\\(P'(0, 5)\\)",
                "\\(P'(0, 6)\\)",
                "\\(P'(2, 6)\\)",
                "\\(P'(0, 9)\\)"
            ],
            "correct": 1,
            "hint": "Apply \\((x, y) \\to (2x, 2y)\\) to \\(P(0, 3)\\).",
            "explanation": "Step 1: Apply the rule: \\(P'(2 \\cdot 0, 2 \\cdot 3) = P'(0, 6)\\).\nStep 2: Distance from origin = \\(\\sqrt{0^2 + 6^2} = 6\\text{ units}\\).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-9",
            "q": "A line segment has endpoints \\(A(2, 1)\\) and \\(B(6, 1)\\). It is dilated with center at the origin and \\(k = 3\\). What is the slope of \\(A'B'\\) compared to \\(AB\\)?",
            "opts": [
                "The slope of \\(A'B'\\) is 3 times steeper",
                "The slope of \\(A'B'\\) is identical (both slopes are 0)",
                "The slope of \\(A'B'\\) is undefined",
                "The slope becomes negative"
            ],
            "correct": 1,
            "hint": "Dilations map lines to parallel lines. What is true about the slopes of parallel lines?",
            "explanation": "Step 1: Original segment \\(AB\\) is horizontal: slope \\(m = \\frac{1 - 1}{6 - 2} = 0\\).\nStep 2: Dilated points are \\(A'(6, 3)\\) and \\(B'(18, 3)\\): slope \\(m' = \\frac{3 - 3}{18 - 6} = 0\\).\nConclusion: Dilations preserve parallelism and slope.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-10",
            "q": "Rectangle \\(EFGH\\) has vertices \\(E(1, 1)\\), \\(F(5, 1)\\), \\(G(5, 3)\\), and \\(H(1, 3)\\). After a dilation centered at the origin, the image vertex \\(E'\\) is at \\((4, 4)\\). What are the coordinates of \\(G'\\)?",
            "opts": [
                "\\((8, 6)\\)",
                "\\((9, 7)\\)",
                "\\((20, 12)\\)",
                "\\((20, 16)\\)"
            ],
            "correct": 2,
            "hint": "Find \\(k\\) from \\(E(1, 1) \\to E'(4, 4)\\): \\(k = 4\\). Then multiply \\(G(5, 3)\\) by 4.",
            "explanation": "Step 1: Find scale factor: \\(k = \\frac{4}{1} = 4\\).\nStep 2: Apply \\(k = 4\\) to point \\(G(5, 3)\\): \\(G'(4 \\cdot 5, 4 \\cdot 3) = G'(20, 12)\\).\nConclusion: \\(G' = (20, 12)\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-11",
            "q": "Point \\(Q(-9, -15)\\) is dilated by \\(k = \\frac{2}{3}\\) centered at the origin. What are the image coordinates \\(Q'\\)?",
            "opts": [
                "\\((-6, -10)\\)",
                "\\((-12, -20)\\)",
                "\\((-3, -5)\\)",
                "\\((6, 10)\\)"
            ],
            "correct": 0,
            "hint": "Multiply both -9 and -15 by 2/3.",
            "explanation": "Step 1: Calculate \\(x' = \\frac{2}{3} \\times (-9) = 2 \\times (-3) = -6\\).\nStep 2: Calculate \\(y' = \\frac{2}{3} \\times (-15) = 2 \\times (-5) = -10\\).\nConclusion: The image coordinates are \\(Q'(-6, -10)\\).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-12",
            "q": "In which quadrant does the image of point \\(W(-4, 7)\\) lie after a dilation centered at the origin with scale factor \\(k = 1.8\\)?",
            "opts": [
                "Quadrant I",
                "Quadrant II",
                "Quadrant III",
                "Quadrant IV"
            ],
            "correct": 1,
            "hint": "Multiplying by a positive scale factor does not change the signs of the coordinates.",
            "explanation": "Step 1: Point \\(W(-4, 7)\\) has a negative x and positive y, located in Quadrant II.\nStep 2: Since \\(k = 1.8 > 0\\), \\(x' = 1.8(-4) = -7.2 < 0\\) and \\(y' = 1.8(7) = 12.6 > 0\\).\nConclusion: The image remains in Quadrant II.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-13",
            "q": "A dilation maps \\(\\triangle ABC\\) to \\(\\triangle A'B'C'\\). If side \\(AB\\) lies on the line \\(y = 2x + 1\\) and does not pass through the center of dilation, the image line containing \\(A'B'\\) will be:",
            "opts": [
                "Perpendicular to \\(y = 2x + 1\\)",
                "Parallel to \\(y = 2x + 1\\) with the same slope \\(m = 2\\)",
                "Horizontal with slope \\(m = 0\\)",
                "A curve with variable slope"
            ],
            "correct": 1,
            "hint": "Dilations map any line not passing through the center to a parallel line.",
            "explanation": "Under CCSS 8.G.A.3, a dilation takes a line not passing through the center of dilation to a parallel line. Since parallel lines have identical slopes, the image line has slope \\(m = 2\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-14",
            "q": "If a line passes directly through the center of dilation, what is the effect of the dilation on that line?",
            "opts": [
                "The line is rotated by 90°",
                "The line maps onto itself (the exact same line)",
                "The line shifts outward away from the center",
                "The line becomes a ray"
            ],
            "correct": 1,
            "hint": "All points on the line are scaled along the line itself.",
            "explanation": "A line passing through the center of dilation is mapped directly onto itself because every point on the line scales along rays that lie entirely within that line.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-15",
            "q": "Segment \\(CD\\) has endpoints \\(C(1, 2)\\) and \\(D(4, 6)\\). What is the length of image segment \\(C'D'\\) after a dilation with \\(k = 4\\) centered at the origin?",
            "opts": [
                "\\(5\\text{ units}\\)",
                "\\(15\\text{ units}\\)",
                "\\(20\\text{ units}\\)",
                "\\(80\\text{ units}\\)"
            ],
            "correct": 2,
            "hint": "Find the original distance \\(CD = \\sqrt{(4-1)^2 + (6-2)^2}\\), then multiply by 4.",
            "explanation": "Step 1: Calculate preimage length: \\(CD = \\sqrt{(4 - 1)^2 + (6 - 2)^2} = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = 5\\).\nStep 2: Multiply by \\(k = 4\\): \\(C'D' = k \\times CD = 4 \\times 5 = 20\\text{ units}\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-16",
            "q": "A dilation is performed on polygon \\(P\\) with scale factor \\(k = 0.5\\). If the perimeter of the dilated image is \\(14\\text{ units}\\), what was the perimeter of the original polygon?",
            "opts": [
                "\\(7\\text{ units}\\)",
                "\\(14\\text{ units}\\)",
                "\\(28\\text{ units}\\)",
                "\\(56\\text{ units}\\)"
            ],
            "correct": 2,
            "hint": "Since \\(P' = k \\times P\\), divide the image perimeter by \\(k = 0.5\\).",
            "explanation": "Step 1: Use the relation \\(P_{\\text{image}} = k \\times P_{\\text{preimage}}\\).\nStep 2: Substitute values: \\(14 = 0.5 \\times P_{\\text{preimage}}\\).\nStep 3: Solve: \\(P_{\\text{preimage}} = \\frac{14}{0.5} = 28\\text{ units}\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-17",
            "q": "Which transformation sequence produces an image that is SIMILAR but NOT congruent to the preimage?",
            "opts": [
                "Translate right 4 units, then reflect across the y-axis",
                "Rotate 90° clockwise, then translate up 3 units",
                "Reflect across the x-axis, then rotate 180°",
                "Translate down 2 units, then dilate by scale factor \\(k = 2.5\\)"
            ],
            "correct": 3,
            "hint": "Look for the sequence that includes a dilation with \\(k \\neq 1\\).",
            "explanation": "Choices A, B, and C consist solely of rigid motions (translations, reflections, rotations), which produce congruent images (\\(k = 1\\)). Choice D includes a dilation with \\(k = 2.5\\), which changes size while preserving shape, producing similar but non-congruent figures.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-2-mcq-18",
            "q": "Triangle \\(JKL\\) has vertices \\(J(-2, 4)\\), \\(K(6, 4)\\), and \\(L(2, 10)\\). What are the coordinates of image vertex \\(K'\\) after a dilation with \\(k = \\frac{1}{2}\\) centered at the origin?",
            "opts": [
                "\\((-1, 2)\\)",
                "\\((3, 2)\\)",
                "\\((1, 5)\\)",
                "\\((12, 8)\\)"
            ],
            "correct": 1,
            "hint": "Multiply the coordinates of \\(K(6, 4)\\) by 1/2.",
            "explanation": "Step 1: Identify vertex \\(K(6, 4)\\).\nStep 2: Apply the rule \\((x, y) \\to (0.5x, 0.5y)\\): \\(K'(0.5 \\times 6, 0.5 \\times 4) = K'(3, 2)\\).\nConclusion: \\(K' = (3, 2)\\).",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-19",
            "q": "If a triangle has an interior angle of \\(43^\\circ\\), what is the measure of the corresponding angle after a dilation with \\(k = 6\\)?",
            "opts": [
                "\\(7.17^\\circ\\)",
                "\\(43^\\circ\\)",
                "\\(180^\\circ\\)",
                "\\(258^\\circ\\)"
            ],
            "correct": 1,
            "hint": "Dilations preserve angle measures.",
            "explanation": "Even though linear dimensions are multiplied by 6, angles are strictly invariant under all dilations: \\(m\\angle A' = m\\angle A = 43^\\circ\\). Angle measures NEVER multiply by the scale factor.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        },
        {
            "id": "p-2-2-mcq-20",
            "q": "Point \\(T(a, b)\\) is dilated centered at the origin by scale factor \\(k = 5\\) to point \\(T'(35, -20)\\). What are the values of \\(a\\) and \\(b\\)?",
            "opts": [
                "\\(a = 7, b = -4\\)",
                "\\(a = 30, b = -25\\)",
                "\\(a = 175, b = -100\\)",
                "\\(a = -7, b = 4\\)"
            ],
            "correct": 0,
            "hint": "Set up equations: \\(5a = 35\\) and \\(5b = -20\\).",
            "explanation": "Step 1: Since \\(x' = ka\\), \\(35 = 5a \\implies a = \\frac{35}{5} = 7\\).\nStep 2: Since \\(y' = kb\\), \\(-20 = 5b \\implies b = \\frac{-20}{5} = -4\\).\nConclusion: \\(a = 7\\) and \\(b = -4\\), so \\(T(7, -4)\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.3"
        }
    ],

    "2.3": [
        {
            "id": "p-2-3-mcq-1",
            "q": "Two geometric figures are defined as **similar** (\\(\\sim\\)) if and only if:",
            "opts": [
                "They have the exact same perimeter and area",
                "One figure can be mapped onto the other through a sequence of rigid motions and dilations",
                "All side lengths are equal in measure",
                "They lie in the same quadrant of the coordinate plane"
            ],
            "correct": 1,
            "hint": "Similarity combines rigid motions (which preserve size & shape) with dilations (which resize proportionally).",
            "explanation": "According to CCSS.MATH.CONTENT.8.G.A.4, two figures are similar if there is a sequence of transformations (translations, reflections, rotations, and dilations) that maps one figure onto the other. Similar figures have congruent corresponding angles and proportional corresponding side lengths.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-2",
            "q": "Triangle \\(ABC\\) is similar to Triangle \\(DEF\\) (\\(\\triangle ABC \\sim \\triangle DEF\\)). If \\(AB = 6\\), \\(BC = 8\\), \\(AC = 10\\), and the shortest side of \\(\\triangle DEF\\) is \\(15\\), what is the length of side \\(DF\\)?",
            "opts": [
                "\\(18\\)",
                "\\(20\\)",
                "\\(25\\)",
                "\\(30\\)"
            ],
            "correct": 2,
            "hint": "Find the scale factor \\(k\\) comparing the shortest sides: \\(k = \\frac{15}{6}\\). Then multiply \\(AC = 10\\) by \\(k\\).",
            "explanation": "Step 1: The shortest side in \\(\\triangle ABC\\) is \\(AB = 6\\). Its corresponding shortest side in \\(\\triangle DEF\\) is \\(DE = 15\\).\nStep 2: Find scale factor: \\(k = \\frac{DE}{AB} = \\frac{15}{6} = 2.5\\).\nStep 3: Side \\(DF\\) corresponds to hypotenuse \\(AC = 10\\): \\(DF = k \\times AC = 2.5 \\times 10 = 25\\).\nConclusion: \\(DF = 25\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-3",
            "q": "In \\(\\triangle PQR\\), \\(m\\angle P = 55^\\circ\\) and \\(m\\angle Q = 65^\\circ\\). In \\(\\triangle STU\\), \\(m\\angle S = 55^\\circ\\) and \\(m\\angle U = 60^\\circ\\). Are the two triangles similar?",
            "opts": [
                "No, because the angle measures do not match.",
                "Yes, by Angle-Angle (AA) similarity, because both triangles have angles of 55°, 65°, and 60°.",
                "Only if their perimeters are equal.",
                "Cannot be determined without side lengths."
            ],
            "correct": 1,
            "hint": "Calculate the third angle of each triangle: \\(180^\\circ - (\\text{sum of other two})\\).",
            "explanation": "Step 1: In \\(\\triangle PQR\\), the third angle \\(m\\angle R = 180^\\circ - (55^\\circ + 65^\\circ) = 180^\\circ - 120^\\circ = 60^\\circ\\).\nStep 2: In \\(\\triangle STU\\), the third angle \\(m\\angle T = 180^\\circ - (55^\\circ + 60^\\circ) = 180^\\circ - 115^\\circ = 65^\\circ\\).\nStep 3: Both triangles have identical angle sets: \\(\\{55^\\circ, 60^\\circ, 65^\\circ\\}\\). By the AA Similarity Criterion, \\(\\triangle PQR \\sim \\triangle STU\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-4",
            "q": "A \\(6\\text{-foot}\\) tall teacher casts a \\(4\\text{-foot}\\) shadow at the same time a nearby flagpole casts a \\(28\\text{-foot}\\) shadow. How tall is the flagpole?",
            "opts": [
                "\\(18.6\\text{ ft}\\)",
                "\\(32\\text{ ft}\\)",
                "\\(42\\text{ ft}\\)",
                "\\(56\\text{ ft}\\)"
            ],
            "correct": 2,
            "hint": "Set up a proportion: \\(\\frac{\\text{Height}}{\\text{Shadow}} = \\frac{6}{4} = \\frac{h}{28}\\).",
            "explanation": "Step 1: The sun's rays create similar right triangles with objects and their shadows.\nStep 2: Set up proportion: \\(\\frac{\\text{Height of Flagpole}}{\\text{Flagpole Shadow}} = \\frac{\\text{Teacher Height}}{\\text{Teacher Shadow}}\\).\nStep 3: \\(\\frac{h}{28} = \\frac{6}{4} = 1.5\\).\nStep 4: Solve for \\(h\\): \\(h = 1.5 \\times 28 = 42\\text{ ft}\\).\nConclusion: The flagpole is \\(42\\text{ feet}\\) tall.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-5",
            "q": "Which statement correctly distinguishes between **congruent figures** (\\(\\cong\\)) and **similar figures** (\\(\\sim\\))?",
            "opts": [
                "Congruent figures have the same shape and size (\\(k = 1\\)); similar figures have the same shape, but may differ in size (\\(k > 0\\)).",
                "Similar figures must have equal side lengths, while congruent figures have proportional sides.",
                "Congruent figures are created by dilations, while similar figures are created by reflections.",
                "All similar figures are congruent, but not all congruent figures are similar."
            ],
            "correct": 0,
            "hint": "Congruence requires identical dimensions (isometry), while similarity allows uniform scaling.",
            "explanation": "Congruent figures can be mapped via rigid motions alone (scale factor strictly \\(k = 1\\)), preserving both size and shape. Similar figures allow dilations (any scale factor \\(k > 0\\)), preserving angle measures and proportional side lengths. Therefore, all congruent figures are similar, but not all similar figures are congruent.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2"
        },
        {
            "id": "p-2-3-mcq-6",
            "q": "Triangle \\(XYZ\\) is mapped to Triangle \\(X'Y'Z'\\) by the sequence: a reflection across line \\(x = 2\\), followed by a dilation centered at the origin with scale factor \\(k = 3\\). Are \\(\\triangle XYZ\\) and \\(\\triangle X'Y'Z'\\) similar?",
            "opts": [
                "No, because reflections reverse orientation, destroying similarity.",
                "Yes, because reflections are rigid motions and dilations preserve shape.",
                "No, because reflections cannot be combined with dilations.",
                "Only if the scale factor \\(k\\) is an integer."
            ],
            "correct": 1,
            "hint": "Any sequence composed of rigid motions (translations, reflections, rotations) and dilations establishes similarity.",
            "explanation": "By definition (CCSS 8.G.A.4), two figures are similar if one can be obtained from the other by a sequence of rigid motions and dilations. A reflection preserves side lengths and angles, and a dilation scales lengths proportionally while preserving angles. Thus, \\(\\triangle XYZ \\sim \\triangle X'Y'Z'\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-7",
            "q": "If \\(\\triangle ABC \\sim \\triangle LMN\\), which of the following ratios is NOT necessarily equal to the scale factor \\(k\\)?",
            "opts": [
                "\\(\\frac{LM}{AB}\\)",
                "\\(\\frac{MN}{BC}\\)",
                "\\(\\frac{m\\angle L}{m\\angle A}\\)",
                "\\(\\frac{\\text{Perimeter}(\\triangle LMN)}{\\text{Perimeter}(\\triangle ABC)}\\)"
            ],
            "correct": 2,
            "hint": "Angles do not scale by \\(k\\); corresponding angles are equal, so their ratio is always 1.",
            "explanation": "Corresponding side lengths and perimeters scale by \\(k\\), so \\(\\frac{LM}{AB} = \\frac{MN}{BC} = \\frac{\\text{Perimeter}}{\\text{Perimeter}} = k\\). However, angle measures are congruent: \\(m\\angle L = m\\angle A\\), meaning their ratio is \\(\\frac{m\\angle L}{m\\angle A} = 1\\), not \\(k\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-8",
            "q": "Are all equilateral triangles similar to each other? Why or why not?",
            "opts": [
                "No, because equilateral triangles can have different side lengths.",
                "Yes, because all equilateral triangles have three \\(60^\\circ\\) interior angles, satisfying Angle-Angle (AA) similarity.",
                "No, because similarity requires identical areas.",
                "Only if they are oriented in the same direction."
            ],
            "correct": 1,
            "hint": "What are the interior angles of any equilateral triangle?",
            "explanation": "Every equilateral triangle has interior angles measuring exactly \\(60^\\circ, 60^\\circ, 60^\\circ\\). By the AA Similarity Criterion, any two triangles with two congruent angles are similar. Therefore, ALL equilateral triangles in geometry are similar to one another.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-9",
            "q": "A rectangular billboard is \\(12\\text{ ft}\\) wide by \\(20\\text{ ft}\\) tall. A flyer for the billboard is \\(6\\text{ in}\\) wide by \\(10\\text{ in}\\) tall. Are the flyer and the billboard similar rectangles?",
            "opts": [
                "No, because feet and inches cannot be similar.",
                "Yes, because both ratios \\(\\frac{12\\text{ ft}}{6\\text{ in}}\\) and \\(\\frac{20\\text{ ft}}{10\\text{ in}}\\) simplify to the same scale ratio of \\(24 : 1\\).",
                "No, because the billboard's area is much larger.",
                "Only if the flyer is enlarged first."
            ],
            "correct": 1,
            "hint": "Convert dimensions to the same units (inches): 12 ft = 144 in, 20 ft = 240 in.",
            "explanation": "Step 1: Convert billboard dimensions to inches: \\(12\\text{ ft} = 144\\text{ in}\\), \\(20\\text{ ft} = 240\\text{ in}\\).\nStep 2: Compute width ratio: \\(\\frac{144}{6} = 24\\).\nStep 3: Compute height ratio: \\(\\frac{240}{10} = 24\\).\nConclusion: Since both ratios equal \\(24\\) and all angles are right angles (\\(90^\\circ\\)), the rectangles are similar.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-10",
            "q": "If \\(\\triangle ABC \\sim \\triangle DEF\\) with scale factor \\(k = 4\\), how does the area of \\(\\triangle DEF\\) compare to the area of \\(\\triangle ABC\\)?",
            "opts": [
                "It is \\(4\\) times as large",
                "It is \\(8\\) times as large",
                "It is \\(16\\) times as large",
                "It is \\(64\\) times as large"
            ],
            "correct": 2,
            "hint": "Remember the area ratio theorem: \\(\\frac{\\text{Area}_{2}}{\\text{Area}_{1}} = k^2\\).",
            "explanation": "The ratio of the areas of two similar figures equals the square of the scale factor: \\(\\text{Area Multiplier} = k^2 = 4^2 = 16\\). The area of \\(\\triangle DEF\\) is \\(16\\text{ times}\\) greater.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-11",
            "q": "In two similar triangles, corresponding sides measure \\(8\\text{ cm}\\) and \\(12\\text{ cm}\\). If the area of the smaller triangle is \\(32\\text{ cm}^2\\), what is the area of the larger triangle?",
            "opts": [
                "\\(48\\text{ cm}^2\\)",
                "\\(72\\text{ cm}^2\\)",
                "\\(96\\text{ cm}^2\\)",
                "\\(144\\text{ cm}^2\\)"
            ],
            "correct": 1,
            "hint": "Find \\(k = \\frac{12}{8} = 1.5\\). Then \\(\\text{Area} = 1.5^2 \\times 32 = 2.25 \\times 32\\).",
            "explanation": "Step 1: Linear scale factor \\(k = \\frac{12}{8} = \\frac{3}{2} = 1.5\\).\nStep 2: Area multiplier \\(k^2 = (\\frac{3}{2})^2 = \\frac{9}{4} = 2.25\\).\nStep 3: Area of larger triangle = \\(\\frac{9}{4} \\times 32 = 9 \\times 8 = 72\\text{ cm}^2\\).\nConclusion: The area is \\(72\\text{ cm}^2\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-12",
            "q": "Which single transformation can be combined with a translation to prove that two non-congruent similar polygons are related?",
            "opts": [
                "A reflection",
                "A rotation",
                "A dilation with \\(k \\neq 1\\)",
                "A shear"
            ],
            "correct": 2,
            "hint": "What transformation changes size proportionally without altering shape?",
            "explanation": "By definition, rigid motions preserve size. To relate two figures that have the same shape but different sizes, a dilation with \\(k \\neq 1\\) must be included in the transformation sequence.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-13",
            "q": "Two regular pentagons are given. Pentagon A has side length \\(5\\text{ cm}\\) and Pentagon B has side length \\(15\\text{ cm}\\). Are the two pentagons similar?",
            "opts": [
                "Yes, all regular polygons with the same number of sides are similar.",
                "No, because their areas differ by a factor of 9.",
                "Only if their centers coincide at the origin.",
                "No, because only triangles can be similar."
            ],
            "correct": 0,
            "hint": "All regular polygons of the same type have equal interior angles (for pentagons, all angles are 108°) and equal side ratios.",
            "explanation": "Every regular pentagon has five interior angles of \\(108^\\circ\\) and all sides equal. Therefore, the angle measures are congruent and all side ratios are equal to \\(\\frac{15}{5} = 3\\). All regular pentagons are mathematically similar.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-14",
            "q": "On a coordinate plane, \\(\\triangle ABC\\) has vertices \\(A(1, 1)\\), \\(B(3, 1)\\), and \\(C(1, 4)\\). \\(\\triangle DEF\\) has vertices \\(D(2, 2)\\), \\(E(8, 2)\\), and \\(F(2, 11)\\). What sequence of transformations proves that \\(\\triangle ABC \\sim \\triangle DEF\\)?",
            "opts": [
                "A translation right 1, up 1 followed by a rotation 90°",
                "A dilation centered at the origin with scale factor \\(k = 3\\), followed by a translation left 1, down 1",
                "A reflection across the line \\(y = x\\)",
                "A dilation centered at \\((0,0)\\) with scale factor \\(k = 2\\)"
            ],
            "correct": 1,
            "hint": "Side \\(AB = 2\\) and side \\(DE = 6\\), so \\(k = \\frac{6}{2} = 3\\). Dilating \\(A(1, 1)\\) by 3 gives \\((3, 3)\\). How do you get to \\(D(2, 2)\\)?",
            "explanation": "Step 1: Check lengths: \\(AB = 3 - 1 = 2\\), \\(DE = 8 - 2 = 6\\). Scale factor \\(k = \\frac{6}{2} = 3\\).\nStep 2: Check vertical lengths: \\(AC = 4 - 1 = 3\\), \\(DF = 11 - 2 = 9\\). Ratio \\(\\frac{9}{3} = 3\\).\nStep 3: Dilating \\(\\triangle ABC\\) by \\(k = 3\\) yields \\(A''(3, 3)\\), \\(B''(9, 3)\\), \\(C''(3, 12)\\).\nStep 4: Translating by vector \\(\\langle -1, -1 \\rangle\\) maps \\((3, 3) \\to (2, 2) = D\\), \\((9, 3) \\to (8, 2) = E\\), and \\((3, 12) \\to (2, 11) = F\\).\nConclusion: A dilation with \\(k = 3\\) followed by a translation proves similarity.",
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-15",
            "q": "A student claims that all rectangles are similar because all rectangles have four right angles (\\(90^\\circ\\)). Is the student's reasoning correct?",
            "opts": [
                "Yes, because having all congruent angles guarantees similarity in all polygons.",
                "No, because similarity also requires corresponding side lengths to be proportional, which is not true for all rectangles (e.g. 2×3 vs 2×8).",
                "Yes, because rectangles are quadrilaterals.",
                "No, because rectangles have parallel sides."
            ],
            "correct": 1,
            "hint": "Consider a 1 by 10 rectangle versus a 5 by 5 square. Are their side ratios proportional?",
            "explanation": "While all rectangles share four \\(90^\\circ\\) angles, similarity requires BOTH congruent angles AND proportional corresponding side lengths. A \\(2 \\times 3\\) rectangle (ratio \\(1.5\\)) is not similar to a \\(2 \\times 8\\) rectangle (ratio \\(4.0\\)). The student's claim is false.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-16",
            "q": "If \\(\\triangle ABC \\sim \\triangle DEF\\) and \\(\\triangle DEF \\cong \\triangle GHI\\), what is the relationship between \\(\\triangle ABC\\) and \\(\\triangle GHI\\)?",
            "opts": [
                "\\(\\triangle ABC \\cong \\triangle GHI\\)",
                "\\(\\triangle ABC \\sim \\triangle GHI\\)",
                "They have no geometric relationship",
                "Their perimeters must be identical"
            ],
            "correct": 1,
            "hint": "Congruence is a special case of similarity (where \\(k = 1\\)). Similarity is transitive.",
            "explanation": "Since congruence is a subset of similarity with \\(k = 1\\), \\(\\triangle DEF \\sim \\triangle GHI\\). By the transitive property of similarity, if \\(\\triangle ABC \\sim \\triangle DEF\\) and \\(\\triangle DEF \\sim \\triangle GHI\\), then \\(\\triangle ABC \\sim \\triangle GHI\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-17",
            "q": "A \\(15\\text{-meter}\\) building casts a shadow of \\(9\\text{ meters}\\). A nearby statue casts a shadow of \\(3\\text{ meters}\\). What is the height of the statue?",
            "opts": [
                "\\(3\\text{ m}\\)",
                "\\(5\\text{ m}\\)",
                "\\(6\\text{ m}\\)",
                "\\(10\\text{ m}\\)"
            ],
            "correct": 1,
            "hint": "Set up a proportion: \\(\\frac{\\text{Height}}{\\text{Shadow}} = \\frac{15}{9} = \\frac{h}{3}\\).",
            "explanation": "Step 1: Set up the proportion: \\(\\frac{h}{3} = \\frac{15}{9}\\).\nStep 2: Simplify \\(\\frac{15}{9} = \\frac{5}{3}\\).\nStep 3: Solve for \\(h\\): \\(h = \\frac{5}{3} \\times 3 = 5\\text{ meters}\\).\nConclusion: The statue is \\(5\\text{ meters}\\) tall.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-18",
            "q": "Two similar triangles have perimeters in the ratio \\(3 : 7\\). What is the ratio of their areas?",
            "opts": [
                "\\(3 : 7\\)",
                "\\(6 : 14\\)",
                "\\(9 : 49\\)",
                "\\(27 : 343\\)"
            ],
            "correct": 2,
            "hint": "Square the linear ratio \\(\\frac{3}{7}\\).",
            "explanation": "Step 1: The perimeter ratio equals the linear scale factor: \\(k = \\frac{3}{7}\\).\nStep 2: The area ratio equals the square of the linear scale factor: \\(k^2 = (\\frac{3}{7})^2 = \\frac{9}{49}\\).\nConclusion: The ratio of their areas is \\(9 : 49\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-19",
            "q": "Which symbol is used in mathematics to state that two geometric figures are **similar**?",
            "opts": [
                "\\(=\\)",
                "\\(\\cong\\)",
                "\\(\\sim\\)",
                "\\(\\approx\\)"
            ],
            "correct": 2,
            "hint": "The tilde symbol represents similarity, while an equal sign with a tilde on top represents congruence.",
            "explanation": "In standard geometry notation, \\(\\sim\\) denotes similarity (e.g. \\(\\triangle ABC \\sim \\triangle DEF\\)), whereas \\(\\cong\\) denotes congruence.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        },
        {
            "id": "p-2-3-mcq-20",
            "q": "Trapezoid \\(ABCD\\) has bases of length \\(8\\text{ cm}\\) and \\(14\\text{ cm}\\), and height \\(6\\text{ cm}\\). Similar trapezoid \\(A'B'C'D'\\) has a shorter base of length \\(20\\text{ cm}\\). What is the height of \\(A'B'C'D'\\)?",
            "opts": [
                "\\(12\\text{ cm}\\)",
                "\\(15\\text{ cm}\\)",
                "\\(18\\text{ cm}\\)",
                "\\(24\\text{ cm}\\)"
            ],
            "correct": 1,
            "hint": "Find \\(k = \\frac{20}{8} = 2.5\\). Then multiply the original height 6 cm by 2.5.",
            "explanation": "Step 1: Find scale factor using corresponding shorter bases: \\(k = \\frac{20}{8} = 2.5\\).\nStep 2: Apply \\(k\\) to the height: \\(h' = k \\times h = 2.5 \\times 6 = 15\\text{ cm}\\).\nConclusion: The height of the similar trapezoid is \\(15\\text{ cm}\\).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.4"
        }
    ]
}
