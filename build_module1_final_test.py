# -*- coding: utf-8 -*-
"""
build_module1_final_test.py
Module 1 Final Mastery Test / Exam Questions Generator
HMH Into Math Grade 8 Teacher Edition - Module 1: Transformations and Congruence
Extracted and synthesized from Module 1 Review, Form A Test, and Form B Test (pages 82-88).

Structure:
- Exactly 5 questions representing Lesson 1.1 (Rigid motions, invariance, orientation)
- Exactly 5 questions representing Lesson 1.2 (Translations, vector shifts, coordinate rules)
- Exactly 5 questions representing Lesson 1.3 (Reflections, coordinate rules, lines of reflection)
- Exactly 5 questions representing Lesson 1.4 (Rotations 90°, 180°, 270°, rotational symmetry)
- Exactly 5 questions representing Lesson 1.5 (Sequences of rigid motions, congruence proofs, corresponding parts)
Total: 25 High-Quality Multiple Choice Questions.
"""

MODULE_1_FINAL_TEST_QUESTIONS = [
    # =========================================================================
    # LESSON 1.1: Rigid Motions, Invariance, and Orientation (Questions 1 to 5)
    # =========================================================================
    {
        "id": "mod1-test-q1",
        "lesson": "1.1",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1.b",
        "dok": 1,
        "q": "Roberto slides a rectangular picture frame $5\\text{ ft}$ to the right across a wall, and Dionne slides an isosceles triangular flag with base angles measuring $70^\\circ$ up a $9\\text{-meter}$ flagpole. Which statement correctly identifies the geometric properties preserved by these movements?",
        "opts": [
            "The picture frame still has $4$ right angles ($90^\\circ$) and the flag still has $2$ congruent base angles ($70^\\circ$) because translations are rigid motions that preserve angle measures.",
            "The picture frame's angles increase due to horizontal displacement, while the flag's base angles decrease as it ascends.",
            "The picture frame preserves its right angles, but the flag's base angles change because vertical translations distort acute angles.",
            "The angle measures of both figures change in direct proportion to the distance each figure was translated."
        ],
        "correct": 0,
        "hint": "Recall that a translation is a rigid motion (isometry). Does sliding a physical object change the angles between its edges?",
        "explanation": "Step 1: Identify the transformation type: Sliding an object horizontally or vertically without turning or resizing is a pure translation.\nStep 2: Apply properties of rigid motions (isometries): Under CCSS 8.G.A.1.b, rigid motions (translations, reflections, and rotations) strictly preserve angle measures. Therefore, every angle in the image is congruent to its corresponding angle in the preimage.\nStep 3: Analyze each figure: Roberto's rectangular frame began with 4 right angles ($90^\\circ$) and retains all 4 right angles ($90^\\circ$). Dionne's isosceles triangular flag began with base angles of $70^\\circ$ each and retains both $70^\\circ$ angles.\nWhy other choices are incorrect: Choices B, C, and D violate the fundamental angle invariance principle of rigid motions by claiming angles change when an object is shifted."
    },
    {
        "id": "mod1-test-q2",
        "lesson": "1.1",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1.c",
        "dok": 2,
        "q": "Parallelogram $RSTU$ has opposite sides $\\overline{RS} \\parallel \\overline{UT}$ and $\\overline{RU} \\parallel \\overline{ST}$. Parallelogram $RSTU$ is rotated $180^\\circ$ clockwise about vertex $R$ to form image $R'S'T'U'$. How many pairs of parallel sides does the rotated image have, and why?",
        "opts": [
            "$0$ pairs, because rotating a polygon reverses slope directions and breaks all parallelism.",
            "$1$ pair, because only horizontal side pairs maintain parallelism after a half-turn rotation.",
            "$2$ pairs, because a rotation is a rigid motion that maps parallel lines to parallel lines.",
            "$4$ pairs, because rotating around a vertex doubles each pair of parallel segments."
        ],
        "correct": 2,
        "hint": "Look at CCSS 8.G.A.1.c: what happens to parallel lines when a figure undergoes a rigid motion such as a rotation?",
        "explanation": "Step 1: Identify the initial figure properties: Parallelogram $RSTU$ has 2 pairs of parallel opposite sides: $\\overline{RS} \\parallel \\overline{UT}$ and $\\overline{RU} \\parallel \\overline{ST}$.\nStep 2: Apply the invariance of parallelism: Under CCSS 8.G.A.1.c, rigid motions (including rotations of any degree about any center) always map parallel lines to parallel lines. If line $L_1 \\parallel L_2$, then their image lines satisfy $L_1' \\parallel L_2'$.\nStep 3: Evaluate the image figure: The image $R'S'T'U'$ remains a parallelogram with exactly 2 pairs of parallel sides: $\\overline{R'S'} \\parallel \\overline{U'T'}$ and $\\overline{R'U'} \\parallel \\overline{S'T'}$.\nWhy other choices are incorrect: Choice A is false because rotations preserve parallelism. Choice B is false because both pairs are preserved, not just one. Choice D is false because a quadrilateral always has at most 2 pairs of opposite parallel sides."
    },
    {
        "id": "mod1-test-q3",
        "lesson": "1.1",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1",
        "dok": 2,
        "q": "A student analyzes four transformations applied to a geometric figure on a coordinate plane:\nI. A slide $6\\text{ units}$ left and $2\\text{ units}$ down\nII. A reflection across the line $x = 3$\nIII. A rotation of $90^\\circ$ counterclockwise about the origin\nIV. A dilation centered at the origin with scale factor $k = 1.5$\nWhich of the following correctly classifies these transformations as rigid motions (isometries) and describes their effect on vertex orientation?",
        "opts": [
            "I, II, and III are rigid motions because they preserve distances and angles; I and III preserve orientation, whereas II reverses orientation.",
            "All four transformations are rigid motions because geometric shape is preserved in all four cases.",
            "Only I and III are rigid motions; reflections and dilations are non-rigid transformations that alter side lengths.",
            "Only II and IV reverse orientation, while I, II, and III all alter side lengths."
        ],
        "correct": 0,
        "hint": "Think about which transformations keep the exact size (side lengths) of the figure unchanged, and which flip the figure like a mirror.",
        "explanation": "Step 1: Classify rigid vs. non-rigid motions: Rigid motions (isometries) preserve Euclidean distances (side lengths) and angle measures. Translations (I), reflections (II), and rotations (III) preserve distances and angles. Dilations (IV) with scale factor $k \\neq 1$ multiply all lengths by $k$ (here $1.5$), so IV is non-rigid.\nStep 2: Analyze vertex orientation: Translations (I) and rotations (III) are direct isometries (they preserve clockwise/counterclockwise vertex ordering). Reflections (II) are opposite isometries (they flip the figure across a reflection axis, reversing clockwise ordering to counterclockwise).\nWhy other choices are incorrect: Choice B is wrong because a dilation changes size and is non-rigid. Choice C is wrong because reflections strictly preserve side lengths and are rigid motions. Choice D incorrectly asserts that rigid motions alter side lengths."
    },
    {
        "id": "mod1-test-q4",
        "lesson": "1.1",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1.a",
        "dok": 1,
        "q": "Halley cuts a square piece of plywood with a side length of $7\\text{ inches}$. She rotates the piece $90^\\circ$ counterclockwise. Next, Amelia has a rectangular table that measures $4\\text{ ft}$ wide and $5\\text{ ft}$ long, which she rotates $90^\\circ$ clockwise. What is the side length of Halley's plywood square and the perimeter of Amelia's table after their rotations?",
        "opts": [
            "Halley's square has side length $9.9\\text{ inches}$; Amelia's table has perimeter $20\\text{ ft}$.",
            "Halley's square has side length $7\\text{ inches}$; Amelia's table has perimeter $18\\text{ ft}$.",
            "Halley's square has side length $3.5\\text{ inches}$; Amelia's table has perimeter $9\\text{ ft}$.",
            "Halley's square has side length $7\\text{ inches}$; Amelia's table has perimeter $14\\text{ ft}$."
        ],
        "correct": 1,
        "hint": "Do rotations change the length of sides or the total perimeter around an object?",
        "explanation": "Step 1: Understand the effect of a rotation on segment lengths: Under CCSS 8.G.A.1.a, rotations map line segments to line segments of the exact same length.\nStep 2: Evaluate Halley's square: Preimage side length = $7\\text{ in.}$ Since rotation is an isometry, each image side length remains exactly $7\\text{ in.}$\nStep 3: Evaluate Amelia's table: Preimage dimensions are width $= 4\\text{ ft}$ and length $= 5\\text{ ft}$. The perimeter of a rectangle is $P = 2(\\text{length} + \\text{width}) = 2(5 + 4) = 18\\text{ ft}$. Because all side lengths are invariant under rotation, the perimeter remains $18\\text{ ft}$.\nWhy other choices are incorrect: Choice A confuses side length with the diagonal $(\\approx 7\\sqrt{2} \\approx 9.9)$ or area. Choice C halves the dimensions. Choice D incorrectly computes $2 \\times 5 + 4 = 14$ instead of $2(5 + 4) = 18$."
    },
    {
        "id": "mod1-test-q5",
        "lesson": "1.1",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1.a",
        "dok": 2,
        "q": "On line segment $\\overline{AB}$, point $C$ lies between $A$ and $B$ such that $AC = 3\\text{ cm}$ and $CB = 5\\text{ cm}$, giving a total length $AB = 8\\text{ cm}$. The segment is mapped to $\\overline{A'B'}$ by a rigid motion (isometry), with $C'$ being the image of point $C$. Which statement MUST be true?",
        "opts": [
            "Point $C'$ can be displaced off line segment $\\overline{A'B'}$, forming a triangle with vertices $A', B', C'$.",
            "The total length $A'B' = 8\\text{ cm}$, but the position of $C'$ shifts such that $A'C' = C'B' = 4\\text{ cm}$.",
            "Point $C'$ lies on segment $\\overline{A'B'}$ between $A'$ and $B'$, with $A'C' = 3\\text{ cm}$, $C'B' = 5\\text{ cm}$, and $A'B' = 8\\text{ cm}$.",
            "The length $A'B'$ depends on whether the transformation was a reflection or a rotation."
        ],
        "correct": 2,
        "hint": "Rigid motions preserve collinearity (points on a line stay on a line) and betweenness (the order of points is maintained).",
        "explanation": "Step 1: Understand collinearity and betweenness invariance: Rigid motions preserve lines, line segments, distances, and point order. If points $A$, $C$, and $B$ are collinear with $C$ between $A$ and $B$, then their images $A'$, $C'$, and $B'$ are collinear with $C'$ between $A'$ and $B'$.\nStep 2: Verify distances: By distance preservation (CCSS 8.G.A.1.a), $d(A', C') = d(A, C) = 3\\text{ cm}$ and $d(C', B') = d(C, B) = 5\\text{ cm}$. Therefore, $A'B' = A'C' + C'B' = 3 + 5 = 8\\text{ cm}$.\nWhy other choices are incorrect: Choice A is false because rigid motions preserve lines (collinearity). Choice B is false because individual segment lengths are invariant, so $C'$ cannot become a midpoint. Choice D is false because all rigid motions (translations, reflections, rotations) preserve lengths identically."
    },

    # =========================================================================
    # LESSON 1.2: Translations, Vector Shifts, Coordinate Rules (Questions 6 to 10)
    # =========================================================================
    {
        "id": "mod1-test-q6",
        "lesson": "1.2",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "Triangle $ABC$ has vertices $A(-2, 3)$, $B(5, 4)$, and $C(-1, -1)$. The triangle is translated using the coordinate rule $(x, y) \\to (x - 3, y + 4)$. What are the coordinates of the image vertices $A'$, $B'$, and $C'$?",
        "opts": [
            "$A'(-5, 7)$, $B'(2, 8)$, and $C'(-4, 3)$",
            "$A'(1, -1)$, $B'(8, 0)$, and $C'(2, -5)$",
            "$A'(-5, -1)$, $B'(2, 0)$, and $C'(-4, -5)$",
            "$A'(-6, 12)$, $B'(15, 16)$, and $C'(-3, -4)$"
        ],
        "correct": 0,
        "hint": "Subtract $3$ from each $x$-coordinate ($x - 3$) and add $4$ to each $y$-coordinate ($y + 4$).",
        "explanation": "Step 1: Apply the translation rule $(x, y) \\to (x - 3, y + 4)$ to each vertex individually.\nStep 2: Compute $A'$: $A(-2, 3) \\to (-2 - 3, 3 + 4) = (-5, 7)$.\nStep 3: Compute $B'$: $B(5, 4) \\to (5 - 3, 4 + 4) = (2, 8)$.\nStep 4: Compute $C'$: $C(-1, -1) \\to (-1 - 3, -1 + 4) = (-4, 3)$.\nThus, the image vertices are $A'(-5, 7)$, $B'(2, 8)$, and $C'(-4, 3)$.\nWhy other choices are incorrect: Choice B accidentally added $3$ and subtracted $4$ ($(x+3, y-4)$). Choice C subtracted $4$ from $y$. Choice D multiplied the coordinates instead of adding/subtracting."
    },
    {
        "id": "mod1-test-q7",
        "lesson": "1.2",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "A triangle with vertices $D(-1, 1)$, $E(2, -1)$, and $F(3, 0)$ is translated $2\\text{ units}$ right and $6\\text{ units}$ down. Which coordinate rule and set of image vertices represent this translation?",
        "opts": [
            "Rule: $(x, y) \\to (x - 2, y + 6)$; Vertices: $D'(-3, 7)$, $E'(0, 5)$, $F'(1, 6)$",
            "Rule: $(x, y) \\to (x + 2, y + 6)$; Vertices: $D'(1, 7)$, $E'(4, 5)$, $F'(5, 6)$",
            "Rule: $(x, y) \\to (x - 6, y + 2)$; Vertices: $D'(-7, 3)$, $E'(-4, 1)$, $F'(-3, 2)$",
            "Rule: $(x, y) \\to (x + 2, y - 6)$; Vertices: $D'(1, -5)$, $E'(4, -7)$, $F'(5, -6)$"
        ],
        "correct": 3,
        "hint": "Moving 'right' adds to $x$, while moving 'down' subtracts from $y$.",
        "explanation": "Step 1: Write the algebraic translation rule: Moving $2\\text{ units}$ right means $x \\to x + 2$. Moving $6\\text{ units}$ down means $y \\to y - 6$. So the rule is $(x, y) \\to (x + 2, y - 6)$.\nStep 2: Calculate image of $D(-1, 1)$: $D'(-1 + 2, 1 - 6) = D'(1, -5)$.\nStep 3: Calculate image of $E(2, -1)$: $E'(2 + 2, -1 - 6) = E'(4, -7)$.\nStep 4: Calculate image of $F(3, 0)$: $F'(3 + 2, 0 - 6) = F'(5, -6)$.\nWhy other choices are incorrect: Choice A uses $(x - 2, y + 6)$ (left and up). Choice B uses $(x + 2, y + 6)$ (right and up). Choice C swaps the $x$ and $y$ translation amounts."
    },
    {
        "id": "mod1-test-q8",
        "lesson": "1.2",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "Triangle $PQR$ has vertices $P(2, -4)$, $Q(4, -5)$, and $R(7, -2)$. After a translation, the image vertex $P'$ is located at $(-4, -1)$. What is the coordinate rule for this translation, and what are the coordinates of image vertex $Q'$?",
        "opts": [
            "Rule: $(x, y) \\to (x + 6, y - 3)$; $Q'(10, -8)$",
            "Rule: $(x, y) \\to (x - 6, y + 3)$; $Q'(-2, -2)$",
            "Rule: $(x, y) \\to (x - 2, y + 5)$; $Q'(2, 0)$",
            "Rule: $(x, y) \\to (x - 6, y - 3)$; $Q'(-2, -8)$"
        ],
        "correct": 1,
        "hint": "Find the change in $x$ ($\\Delta x = x' - x$) and change in $y$ ($\\Delta y = y' - y$) from $P$ to $P'$.",
        "explanation": "Step 1: Determine the horizontal shift: $\\Delta x = x_{P'} - x_P = -4 - 2 = -6$.\nStep 2: Determine the vertical shift: $\\Delta y = y_{P'} - y_P = -1 - (-4) = -1 + 4 = +3$.\nStep 3: Formulate the coordinate rule: $(x, y) \\to (x - 6, y + 3)$.\nStep 4: Apply the rule to find $Q'$: Given $Q(4, -5)$, $Q'(4 - 6, -5 + 3) = Q'(-2, -2)$.\nWhy other choices are incorrect: Choice A reverses the signs of the shifts. Choice C calculates incorrect differences. Choice D subtracts $3$ instead of adding $3$ to $y$."
    },
    {
        "id": "mod1-test-q9",
        "lesson": "1.2",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "Quadrilateral $WXYZ$ is first translated $5\\text{ units}$ right and $2\\text{ units}$ down. It is then translated an additional $3\\text{ units}$ left and $7\\text{ units}$ up. Which single translation rule maps quadrilateral $WXYZ$ directly to its final image position?",
        "opts": [
            "$(x, y) \\to (x + 8, y + 9)$",
            "$(x, y) \\to (x + 2, y + 5)$",
            "$(x, y) \\to (x - 2, y - 5)$",
            "$(x, y) \\to (x + 2, y - 9)$"
        ],
        "correct": 1,
        "hint": "Combine the horizontal changes ($+5$ and $-3$) and the vertical changes ($-2$ and $+7$).",
        "explanation": "Step 1: Write the algebraic expression for the first translation $T_1$: $(x, y) \\to (x + 5, y - 2)$.\nStep 2: Apply the second translation $T_2$ to the result: $(x', y') \\to (x' - 3, y' + 7)$.\nStep 3: Substitute $x' = x + 5$ and $y' = y - 2$ into $T_2$:\n$x'' = (x + 5) - 3 = x + 2$\n$y'' = (y - 2) + 7 = y + 5$\nTherefore, the combined translation rule is $(x, y) \\to (x + 2, y + 5)$.\nWhy other choices are incorrect: Choice A adds the magnitudes without respecting direction ($5+3=8$ and $2+7=9$). Choice C reverses the net signs. Choice D subtracts $7$ instead of adding $7$."
    },
    {
        "id": "mod1-test-q10",
        "lesson": "1.2",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "A game graphic on a coordinate grid is translated using the rule $(x, y) \\to (x - 8, y + 5)$. If the translated image of a key vertex is located at $S'(3, -2)$, what were the coordinates of the original preimage vertex $S$?",
        "opts": [
            "$S(-5, 3)$",
            "$S(-5, -7)$",
            "$S(11, -7)$",
            "$S(11, 3)$"
        ],
        "correct": 2,
        "hint": "You are given the image $(x', y') = (3, -2)$. Work backwards to find the original $(x, y)$.",
        "explanation": "Step 1: Set up the equations from the coordinate rule $(x', y') = (x - 8, y + 5)$:\n$x - 8 = 3$\n$y + 5 = -2$\nStep 2: Solve for the preimage coordinates $x$ and $y$:\n$x = 3 + 8 = 11$\n$y = -2 - 5 = -7$\nStep 3: Check by applying the rule forward to $S(11, -7)$:\n$11 - 8 = 3$ and $-7 + 5 = -2$, which matches $S'(3, -2)$.\nWhy other choices are incorrect: Choice A mistakenly applied the translation rule forward to the image point ($3 - 8 = -5, -2 + 5 = 3$). Choices B and D contain sign errors when solving the linear equations."
    },

    # =========================================================================
    # LESSON 1.3: Reflections, Coordinate Rules, Lines of Reflection (Questions 11 to 15)
    # =========================================================================
    {
        "id": "mod1-test-q11",
        "lesson": "1.3",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 1,
        "q": "Point $M(2, -4)$ is reflected across the $x$-axis to produce $M'$, and point $N(-3, 1)$ is reflected across the $y$-axis to produce $N'$. What are the coordinates of $M'$ and $N'$?",
        "opts": [
            "$M'(2, 4)$ and $N'(3, 1)$",
            "$M'(-2, -4)$ and $N'(-3, -1)$",
            "$M'(-2, 4)$ and $N'(3, -1)$",
            "$M'(-4, 2)$ and $N'(1, -3)$"
        ],
        "correct": 0,
        "hint": "Reflection across the $x$-axis negates $y$: $(x, -y)$. Reflection across the $y$-axis negates $x$: $(-x, y)$.",
        "explanation": "Step 1: Apply the $x$-axis reflection rule $(x, y) \\to (x, -y)$ to point $M(2, -4)$:\n$x' = 2$, $y' = -(-4) = 4 \\implies M'(2, 4)$.\nStep 2: Apply the $y$-axis reflection rule $(x, y) \\to (-x, y)$ to point $N(-3, 1)$:\n$x' = -(-3) = 3$, $y' = 1 \\implies N'(3, 1)$.\nWhy other choices are incorrect: Choice B swaps the rules (negating $x$ for the $x$-axis and negating $y$ for the $y$-axis). Choice C negates both coordinates (which is a $180^\\circ$ rotation). Choice D swaps the $x$ and $y$ values."
    },
    {
        "id": "mod1-test-q12",
        "lesson": "1.3",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1",
        "dok": 2,
        "q": "In a coordinate plane, the vertices of $\\triangle ABC$ are $A(1, 2)$, $B(4, 2)$, and $C(2, 5)$. The vertices of its reflected image $\\triangle A'B'C'$ are $A'(-5, 2)$, $B'(-8, 2)$, and $C'(-6, 5)$. What is the equation of the line of reflection?",
        "opts": [
            "$y = 2$",
            "$x = -2$",
            "$x = -1$",
            "$y = -2$"
        ],
        "correct": 1,
        "hint": "The line of reflection is the perpendicular bisector of the segment connecting any preimage point and its image point. Find the midpoint of $\\overline{AA'}$.",
        "explanation": "Step 1: Understand the geometric definition of a reflection line: The line of reflection is the perpendicular bisector of every segment connecting a preimage point to its corresponding image point.\nStep 2: Compare corresponding points $A(1, 2)$ and $A'(-5, 2)$:\nThe $y$-coordinates are identical ($y = 2$), while the $x$-coordinates change from $1$ to $-5$. The segment $\\overline{AA'}$ is horizontal, so the line of reflection must be vertical (perpendicular to horizontal).\nStep 3: Find the midpoint of $\\overline{AA'}$:\n$x_{\\text{mid}} = \\frac{1 + (-5)}{2} = \\frac{-4}{2} = -2$.\nCheck with $B(4, 2)$ and $B'(-8, 2)$: $\\frac{4 + (-8)}{2} = -2$.\nCheck with $C(2, 5)$ and $C'(-6, 5)$: $\\frac{2 + (-6)}{2} = -2$.\nTherefore, the line of reflection is the vertical line $x = -2$.\nWhy other choices are incorrect: Choice A ($y = 2$) is a horizontal line passing through the vertices, not a perpendicular bisector. Choice C miscalculates the midpoint. Choice D is horizontal instead of vertical."
    },
    {
        "id": "mod1-test-q13",
        "lesson": "1.3",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "Which coordinate rule represents a reflection across the line $y = x$, and what is the image of point $K(-4, 7)$ under this reflection?",
        "opts": [
            "Rule: $(x, y) \\to (-y, -x)$; Image: $K'(-7, 4)$",
            "Rule: $(x, y) \\to (-x, -y)$; Image: $K'(4, -7)$",
            "Rule: $(x, y) \\to (x, -y)$; Image: $K'(-4, -7)$",
            "Rule: $(x, y) \\to (y, x)$; Image: $K'(7, -4)$"
        ],
        "correct": 3,
        "hint": "Reflecting across the diagonal line $y = x$ interchanges the roles of $x$ and $y$.",
        "explanation": "Step 1: Recall the coordinate rule for reflection across the line $y = x$: Every point $(x, y)$ swaps its coordinates: $(x, y) \\to (y, x)$.\nStep 2: Apply the rule to point $K(-4, 7)$:\n$x' = y = 7$\n$y' = x = -4$\nThus, $K'(7, -4)$.\nWhy other choices are incorrect: Choice A, $(x, y) \\to (-y, -x)$, represents a reflection across the line $y = -x$. Choice B, $(x, y) \\to (-x, -y)$, represents a $180^\\circ$ rotation about the origin. Choice C, $(x, y) \\to (x, -y)$, represents a reflection across the $x$-axis."
    },
    {
        "id": "mod1-test-q14",
        "lesson": "1.3",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1.a",
        "dok": 2,
        "q": "Point $P(5, 3)$ is reflected across the horizontal line $y = -1$ to produce image point $P'$. What are the coordinates of $P'$, and what is the total distance between $P$ and $P'$?",
        "opts": [
            "Coordinates: $P'(5, -3)$; Total distance: $6\\text{ units}$",
            "Coordinates: $P'(-7, 3)$; Total distance: $12\\text{ units}$",
            "Coordinates: $P'(5, -5)$; Total distance: $8\\text{ units}$",
            "Coordinates: $P'(5, -1)$; Total distance: $4\\text{ units}$"
        ],
        "correct": 2,
        "hint": "Find the vertical distance from $P$ to the line $y = -1$, then move that same distance past the line.",
        "explanation": "Step 1: Determine the distance from $P(5, 3)$ to the line $y = -1$:\nThe point has $y = 3$. The vertical distance to $y = -1$ is $d = 3 - (-1) = 4\\text{ units}$.\nStep 2: Find the coordinates of $P'$:\nUnder reflection across a horizontal line, the $x$-coordinate remains unchanged ($x' = 5$). The $y$-coordinate is $4\\text{ units}$ below the reflection line: $y' = -1 - 4 = -5$. Thus, $P'(5, -5)$.\nStep 3: Calculate the total distance between $P$ and $P'$:\nDistance $= 2 \\times d = 2 \\times 4 = 8\\text{ units}$ (or $|3 - (-5)| = 8\\text{ units}$).\nWhy other choices are incorrect: Choice A reflects across the $x$-axis ($y = 0$). Choice B reflects horizontally instead of vertically. Choice D places the point directly on the line of reflection."
    },
    {
        "id": "mod1-test-q15",
        "lesson": "1.3",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1",
        "dok": 2,
        "q": "Right triangle $XYZ$ has vertices listed in clockwise order: $X(1, 1)$, $Y(1, 4)$, and $Z(5, 1)$. Triangle $XYZ$ is reflected across the $y$-axis to produce $\\triangle X'Y'Z'$. Which statement correctly describes the side lengths and vertex orientation of $\\triangle X'Y'Z'$?",
        "opts": [
            "Side lengths are preserved, and the vertex order $X' \\to Y' \\to Z'$ remains clockwise because all rigid motions preserve orientation.",
            "Side lengths are preserved ($X'Y' = 3$, $X'Z' = 4$, $Y'Z' = 5$), but the vertex order $X' \\to Y' \\to Z'$ is now counterclockwise because reflection reverses orientation.",
            "Side lengths are negated ($X'Y' = -3$, $X'Z' = -4$), and the vertex order remains clockwise.",
            "The hypotenuse length decreases because the figure was flipped across the vertical axis."
        ],
        "correct": 1,
        "hint": "Reflections are 'mirror images' (opposite isometries). What does a mirror do to left and right?",
        "explanation": "Step 1: Compute side lengths of preimage $\\triangle XYZ$:\n$XY = |4 - 1| = 3$\n$XZ = |5 - 1| = 4$\n$YZ = \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5$.\nStep 2: Apply reflection across the $y$-axis: $(x, y) \\to (-x, y)$:\n$X'(-1, 1)$, $Y'(-1, 4)$, $Z'(-5, 1)$.\nDistances are strictly preserved: $X'Y' = 3$, $X'Z' = 4$, $Y'Z' = 5$.\nStep 3: Analyze orientation:\nIn $\\triangle XYZ$, tracing $X(1, 1) \\to Y(1, 4) \\to Z(5, 1) \\to X(1, 1)$ proceeds in a clockwise direction. In $\\triangle X'Y'Z'$, tracing $X'(-1, 1) \\to Y'(-1, 4) \\to Z'(-5, 1) \\to X'(-1, 1)$ proceeds in a counterclockwise direction.\nThus, reflection reverses orientation.\nWhy other choices are incorrect: Choice A fails to recognize that reflection reverses orientation. Choice C mentions negative lengths, which cannot exist. Choice D violates distance invariance (CCSS 8.G.A.1.a)."
    },

    # =========================================================================
    # LESSON 1.4: Rotations (90°, 180°, 270°), Rotational Symmetry (Questions 16 to 20)
    # =========================================================================
    {
        "id": "mod1-test-q16",
        "lesson": "1.4",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 1,
        "q": "The coordinates of a figure are transformed using the algebraic rule $(x, y) \\to (-y, x)$. Which transformation is represented by this rule?",
        "opts": [
            "A $90^\\circ$ counterclockwise rotation about the origin",
            "A $90^\\circ$ clockwise rotation about the origin",
            "A $180^\\circ$ rotation about the origin",
            "A reflection across the line $y = -x$"
        ],
        "correct": 0,
        "hint": "Test a point like $(1, 0)$: under $(x, y) \\to (-y, x)$, where does it go?",
        "explanation": "Step 1: Test with the standard unit point $(1, 0)$ on the positive $x$-axis:\nApplying $(x, y) \\to (-y, x)$: $(1, 0) \\to (0, 1)$.\nMoving from $(1, 0)$ to $(0, 1)$ is a turn of $90^\\circ$ counterclockwise (or $270^\\circ$ clockwise).\nStep 2: Confirm with $(0, 1)$ on the positive $y$-axis:\n$(0, 1) \\to (-1, 0)$, which continues the $90^\\circ$ counterclockwise rotation.\nStep 3: Verify the standard rotation rules about the origin:\n- $90^\\circ$ counterclockwise (or $270^\\circ$ clockwise): $(x, y) \\to (-y, x)$\n- $180^\\circ$ rotation: $(x, y) \\to (-x, -y)$\n- $90^\\circ$ clockwise (or $270^\\circ$ counterclockwise): $(x, y) \\to (y, -x)$\nWhy other choices are incorrect: Choice B is $(y, -x)$. Choice C is $(-x, -y)$. Choice D is $(-y, -x)$."
    },
    {
        "id": "mod1-test-q17",
        "lesson": "1.4",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "Parallelogram $ABCD$ has a vertex at $A(3, -5)$. The parallelogram is rotated $90^\\circ$ clockwise about the origin. What are the coordinates of the image vertex $A'$?",
        "opts": [
            "$A'(5, 3)$",
            "$A'(-3, 5)$",
            "$A'(-5, -3)$",
            "$A'(5, -3)$"
        ],
        "correct": 2,
        "hint": "The coordinate rule for a $90^\\circ$ clockwise rotation about the origin is $(x, y) \\to (y, -x)$.",
        "explanation": "Step 1: Identify the rotation rule: A $90^\\circ$ clockwise rotation about the origin maps each point $(x, y)$ to $(y, -x)$.\nStep 2: Substitute the coordinates of $A(3, -5)$ into the rule:\nHere, $x = 3$ and $y = -5$.\n$x' = y = -5$\n$y' = -x = -(3) = -3$\nStep 3: Write the resulting coordinate pair: $A'(-5, -3)$.\nWhy other choices are incorrect: Choice A is $(-y, x)$, which is a $90^\\circ$ counterclockwise rotation ($(-(-5), 3) = (5, 3)$). Choice B is $(-x, -y)$, which is a $180^\\circ$ rotation. Choice D has an incorrect sign on the new $x$-coordinate."
    },
    {
        "id": "mod1-test-q18",
        "lesson": "1.4",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "Triangle $RST$ has vertices $R(-4, 2)$, $S(-1, 5)$, and $T(-2, 1)$. The triangle is rotated $180^\\circ$ about the origin. What are the coordinates of the image vertices, and how does a $180^\\circ$ clockwise rotation compare to a $180^\\circ$ counterclockwise rotation?",
        "opts": [
            "Image vertices: $R'(-2, 4)$, $S'(-5, 1)$, $T'(-1, 2)$; clockwise and counterclockwise produce perpendicular images.",
            "Image vertices: $R'(4, 2)$, $S'(1, 5)$, $T'(2, 1)$; clockwise rotates right, counterclockwise rotates left.",
            "Image vertices: $R'(-4, -2)$, $S'(-1, -5)$, $T'(-2, -1)$; only counterclockwise negates the $y$-coordinate.",
            "Image vertices: $R'(4, -2)$, $S'(1, -5)$, $T'(2, -1)$; both directions yield the identical image."
        ],
        "correct": 3,
        "hint": "Rotating a full half-circle ($180^\\circ$) lands on the exact same opposite ray whether you turn clockwise or counterclockwise: $(x, y) \\to (-x, -y)$.",
        "explanation": "Step 1: Identify the coordinate rule for a $180^\\circ$ rotation: A half-turn ($180^\\circ$) about the origin negates both coordinates: $(x, y) \\to (-x, -y)$.\nStep 2: Compute each vertex:\n$R(-4, 2) \\to (-(-4), -(2)) = (4, -2)$\n$S(-1, 5) \\to (-(-1), -(5)) = (1, -5)$\n$T(-2, 1) \\to (-(-2), -(1)) = (2, -1)$\nStep 3: Compare rotational directions: Because $180^\\circ + 180^\\circ = 360^\\circ$ (a full circle), rotating $180^\\circ$ clockwise lands in the exact same position as rotating $180^\\circ$ counterclockwise.\nWhy other choices are incorrect: Choice A swaps and negates coordinates. Choice B only negates the $x$-coordinate. Choice C only negates the $y$-coordinate."
    },
    {
        "id": "mod1-test-q19",
        "lesson": "1.4",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1",
        "dok": 2,
        "q": "A regular hexagon is centered at the origin of a coordinate plane. What is the smallest positive angle of rotation about its center that maps the hexagon onto itself, and what is its total order of rotational symmetry?",
        "opts": [
            "Smallest angle: $60^\\circ$; Order of rotational symmetry: $6$",
            "Smallest angle: $90^\\circ$; Order of rotational symmetry: $4$",
            "Smallest angle: $120^\\circ$; Order of rotational symmetry: $3$",
            "Smallest angle: $45^\\circ$; Order of rotational symmetry: $8$"
        ],
        "correct": 0,
        "hint": "A regular polygon with $n$ sides has $n$ equal central angles. Divide $360^\\circ$ by the number of sides $n$.",
        "explanation": "Step 1: Identify the number of sides: A regular hexagon has $n = 6$ congruent sides and $6$ congruent central angles.\nStep 2: Calculate the fundamental angle of rotational symmetry:\nAngle $= \\frac{360^\\circ}{n} = \\frac{360^\\circ}{6} = 60^\\circ$.\nStep 3: Determine the order of rotational symmetry: The figure maps onto itself at rotations of $60^\\circ, 120^\\circ, 180^\\circ, 240^\\circ, 300^\\circ,$ and $360^\\circ$ (or $0^\\circ$). That is a total of $6$ rotational alignments within one complete turn, so its order of rotational symmetry is $6$.\nWhy other choices are incorrect: Choice B corresponds to a square ($n=4$). Choice C uses $120^\\circ$ (which maps the hexagon onto itself, but is not the *smallest* positive angle). Choice D corresponds to a regular octagon ($n=8$)."
    },
    {
        "id": "mod1-test-q20",
        "lesson": "1.4",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "Rectangle $PQRS$ is rotated $270^\\circ$ counterclockwise about the origin. Vertex $P$ has coordinates $(-6, 2)$. Which coordinate rule represents a $270^\\circ$ counterclockwise rotation, and what are the coordinates of $P'$?",
        "opts": [
            "Rule: $(x, y) \\to (-y, x)$; Coordinates: $P'(-2, -6)$",
            "Rule: $(x, y) \\to (y, -x)$; Coordinates: $P'(2, 6)$",
            "Rule: $(x, y) \\to (-x, -y)$; Coordinates: $P'(6, -2)$",
            "Rule: $(x, y) \\to (-y, -x)$; Coordinates: $P'(-2, 6)$"
        ],
        "correct": 1,
        "hint": "Notice that $270^\\circ$ counterclockwise is the exact same rotational motion as $90^\\circ$ clockwise: $(x, y) \\to (y, -x)$.",
        "explanation": "Step 1: Connect angles of rotation: Turning $270^\\circ$ counterclockwise leaves $360^\\circ - 270^\\circ = 90^\\circ$ clockwise. Hence, a $270^\\circ$ counterclockwise rotation is mathematically equivalent to a $90^\\circ$ clockwise rotation.\nStep 2: Recall the coordinate rule: $(x, y) \\to (y, -x)$.\nStep 3: Evaluate point $P(-6, 2)$ where $x = -6$ and $y = 2$:\n$x' = y = 2$\n$y' = -x = -(-6) = 6$\nSo $P'(2, 6)$.\nWhy other choices are incorrect: Choice A is the rule for $90^\\circ$ counterclockwise ($270^\\circ$ clockwise). Choice C is the rule for $180^\\circ$ rotation. Choice D is a reflection across the line $y = -x$."
    },

    # =========================================================================
    # LESSON 1.5: Sequences of Rigid Motions, Congruence Proofs (Questions 21 to 25)
    # =========================================================================
    {
        "id": "mod1-test-q21",
        "lesson": "1.5",
        "standard": "CCSS.MATH.CONTENT.8.G.A.3",
        "dok": 2,
        "q": "The point $(a, b)$ is reflected across the $x$-axis and then translated $4\\text{ units}$ to the right and $2\\text{ units}$ down. Which expression gives the coordinates of the final image point?",
        "opts": [
            "$(-a + 4, b - 2)$",
            "$(a + 4, -b + 2)$",
            "$(a - 4, -b - 2)$",
            "$(a + 4, -b - 2)$"
        ],
        "correct": 3,
        "hint": "Apply each transformation step-by-step: first reflect across the $x$-axis ($(x, y) \\to (x, -y)$), then apply the translation to the new coordinates.",
        "explanation": "Step 1: Perform the reflection across the $x$-axis: The rule is $(x, y) \\to (x, -y)$. Applying this to $(a, b)$ yields the intermediate point $(a, -b)$.\nStep 2: Apply the translation: Translating $4\\text{ units}$ to the right adds $4$ to the $x$-coordinate: $x' = a + 4$. Translating $2\\text{ units}$ down subtracts $2$ from the current $y$-coordinate: $y' = -b - 2$.\nStep 3: Combine into the final coordinate pair: $(a + 4, -b - 2)$.\nWhy other choices are incorrect: Choice A incorrectly negates $a$ (as if reflected across the $y$-axis). Choice B adds $2$ instead of subtracting $2$. Choice C subtracts $4$ from $a$ (translating left instead of right)."
    },
    {
        "id": "mod1-test-q22",
        "lesson": "1.5",
        "standard": "CCSS.MATH.CONTENT.8.G.A.2",
        "dok": 3,
        "q": "Consider the point $T(3, 2)$ subjected to two different sequences of transformations:\nSequence 1: Translate $3\\text{ units}$ up, then reflect across the $x$-axis.\nSequence 2: Reflect across the $x$-axis, then translate $3\\text{ units}$ up.\nWhat are the resulting coordinates for Sequence 1 and Sequence 2, respectively, and what does this demonstrate?",
        "opts": [
            "Sequence 1 produces $(3, 5)$; Sequence 2 produces $(3, 5)$; this demonstrates that transformations always commute.",
            "Sequence 1 produces $(-3, -5)$; Sequence 2 produces $(3, -1)$; this demonstrates that reflections always reverse the $x$-coordinate.",
            "Sequence 1 produces $(3, -5)$; Sequence 2 produces $(3, 1)$; this demonstrates that the order of transformations matters (transformations do not generally commute).",
            "Sequence 1 produces $(3, -1)$; Sequence 2 produces $(3, -5)$; this demonstrates that translating up is equivalent to subtracting from $y$."
        ],
        "correct": 2,
        "hint": "Work through each sequence step-by-step from left to right. Does the order in which you perform operations affect the final answer?",
        "explanation": "Step 1: Calculate Sequence 1 for $T(3, 2)$:\n- First translate $3$ up: $(3, 2) \\to (3, 2 + 3) = (3, 5)$.\n- Then reflect across the $x$-axis: $(3, 5) \\to (3, -5)$.\nStep 2: Calculate Sequence 2 for $T(3, 2)$:\n- First reflect across the $x$-axis: $(3, 2) \\to (3, -2)$.\n- Then translate $3$ up: $(3, -2) \\to (3, -2 + 3) = (3, 1)$.\nStep 3: Compare results: Since $(3, -5) \\neq (3, 1)$, reversing the order of the reflection and translation produces different final locations. In mathematics, this means transformations are generally non-commutative ($T \\circ R \\neq R \\circ T$).\nWhy other choices are incorrect: Choice A falsely claims both sequences yield $(3, 5)$. Choice B introduces erroneous sign flips on the $x$-coordinate. Choice D swaps the results of the two sequences."
    },
    {
        "id": "mod1-test-q23",
        "lesson": "1.5",
        "standard": "CCSS.MATH.CONTENT.8.G.A.2",
        "dok": 2,
        "q": "Trapezoid $WXYZ$ has angles $\\angle W = 100^\\circ$ and $\\angle X = 80^\\circ$, with side lengths $WX = 5\\text{ cm}$ and $ZW = 7\\text{ cm}$. Trapezoid $WXYZ$ is rotated $90^\\circ$ clockwise about its center and then translated $6\\text{ units}$ down and $4\\text{ units}$ right to produce trapezoid $HJKL$, where vertices $W, X, Y, Z$ correspond to $H, J, K, L$. What are the measure of $\\angle J$ and the length of side $\\overline{LH}$?",
        "opts": [
            "$m\\angle J = 100^\\circ$ and $LH = 5\\text{ cm}$",
            "$m\\angle J = 80^\\circ$ and $LH = 7\\text{ cm}$",
            "$m\\angle J = 170^\\circ$ and $LH = 13\\text{ cm}$",
            "$m\\angle J = 80^\\circ$ and $LH = 11\\text{ cm}$"
        ],
        "correct": 1,
        "hint": "Identify corresponding parts between the preimage $WXYZ$ and image $HJKL$. Which vertex corresponds to $J$? Which side corresponds to $\\overline{LH}$?",
        "explanation": "Step 1: Identify congruence of figures: Because the sequence consists entirely of rigid motions (a rotation followed by a translation), $\\text{Trapezoid } WXYZ \\cong \\text{Trapezoid } HJKL$ by CCSS 8.G.A.2.\nStep 2: Map corresponding vertices and angles: The correspondence is $W \\mapsto H$, $X \\mapsto J$, $Y \\mapsto K$, and $Z \\mapsto L$. Therefore, $\\angle J$ corresponds to $\\angle X$. Since rigid motions preserve angle measures, $m\\angle J = m\\angle X = 80^\\circ$.\nStep 3: Map corresponding sides: Segment $\\overline{LH}$ connects the 4th and 1st vertices, corresponding to $\\overline{ZW}$. Since rigid motions preserve distances, $LH = ZW = 7\\text{ cm}$.\nWhy other choices are incorrect: Choice A swaps the corresponding angle and side with $W$ and $WX$. Choice C adds the translation amounts to the angle and side length (a common misconception). Choice D adds the translation horizontal shift ($4$) to side length ($7+4=11$)."
    },
    {
        "id": "mod1-test-q24",
        "lesson": "1.5",
        "standard": "CCSS.MATH.CONTENT.8.G.A.2",
        "dok": 3,
        "q": "Triangle $J$ has vertices at $(1, 1)$, $(4, 1)$, and $(1, 3)$. Triangle $P$ has vertices at $(-1, -1)$, $(-1, -4)$, and $(-3, -1)$. Which sequence of transformations proves that Triangle $J$ is congruent to Triangle $P$?",
        "opts": [
            "A reflection across the $y$-axis followed by a $90^\\circ$ counterclockwise rotation about the origin",
            "A translation $2\\text{ units}$ left and $2\\text{ units}$ down followed by a dilation of scale factor $1$",
            "A reflection across the $x$-axis followed by a reflection across the line $y = x$",
            "A $180^\\circ$ rotation about the origin followed by a reflection across the horizontal line $y = 0$"
        ],
        "correct": 0,
        "hint": "Trace what happens to the right-angle vertex $(1, 1)$ and long leg $(4, 1)$ under each sequence of transformations.",
        "explanation": "Step 1: Test Choice A step-by-step:\n- Step 1a: Reflect across the $y$-axis: $(x, y) \\to (-x, y)$:\n  $(1, 1) \\to (-1, 1)$\n  $(4, 1) \\to (-4, 1)$\n  $(1, 3) \\to (-1, 3)$\n- Step 1b: Rotate $90^\\circ$ counterclockwise about the origin: $(x', y') \\to (-y', x')$:\n  $(-1, 1) \\to (-1, -1)$\n  $(-4, 1) \\to (-1, -4)$\n  $(-1, 3) \\to (-3, -1)$\nNotice that the resulting set of vertices is $\{(-1, -1), (-1, -4), (-3, -1)\}$, which matches Triangle $P$ exactly!\nStep 2: Conclusion on congruence: Since Triangle $P$ is obtained from Triangle $J$ through a sequence of rigid motions (a reflection followed by a rotation), Triangle $J \\cong \\text{Triangle } P$ by CCSS 8.G.A.2.\nWhy other choices are incorrect: Choice B only translates $(1, 1) \\to (-1, -1)$ but leaves $(4, 1) \\to (2, -1) \\neq (-1, -4)$. Choice C maps $(x, y) \\to (x, -y) \\to (-y, x)$ which is a pure rotation, but Triangle $J$ and Triangle $P$ have opposite orientations so a single reflection must be involved. Choice D does not map $(4, 1)$ to $(-1, -4)$."
    },
    {
        "id": "mod1-test-q25",
        "lesson": "1.5",
        "standard": "CCSS.MATH.CONTENT.8.G.A.2",
        "dok": 2,
        "q": "Pentagon $PQRST$ undergoes a sequence of rigid motions consisting of a reflection across a vertical line followed by a translation $2\\text{ units}$ left and $5\\text{ units}$ up to produce pentagon $ABCDE$, with vertex correspondence $P \\mapsto A$, $Q \\mapsto B$, $R \\mapsto C$, $S \\mapsto D$, and $T \\mapsto E$. Which statement about the two pentagons is FALSE?",
        "opts": [
            "Pentagon $ABCDE$ is congruent to Pentagon $PQRST$ ($\text{Pentagon } ABCDE \\cong \\text{Pentagon } PQRST$).",
            "Side length $DC$ is equal to side length $SR$ ($DC = SR$).",
            "The angle measure of $\\angle E$ equals the angle measure of $\\angle T$ ($m\\angle E = m\\angle T$).",
            "The clockwise vertex orientation of Pentagon $ABCDE$ is identical to the clockwise vertex orientation of Pentagon $PQRST$."
        ],
        "correct": 3,
        "hint": "Recall the effect of reflections on orientation: an odd number of reflections reverses the clockwise order of vertices.",
        "explanation": "Step 1: Recall congruence and rigid motion properties (CCSS 8.G.A.2): Any figure produced by a sequence of rigid motions (reflections and translations) is congruent to the original figure. Thus, Pentagon $ABCDE \\cong \\text{Pentagon } PQRST$ (Choice A is TRUE).\nStep 2: Check corresponding parts of congruent figures: Corresponding side lengths are equal, so $DC = SR$ (Choice B is TRUE). Corresponding angle measures are equal, so $m\\angle E = m\\angle T$ (Choice C is TRUE).\nStep 3: Analyze orientation: A reflection reverses the orientation of a figure (flips clockwise to counterclockwise). A translation preserves orientation. Therefore, a sequence consisting of one reflection and one translation results in a reversed orientation. Tracing vertices $A \\to B \\to C \\to D \\to E$ proceeds in the opposite rotational sense compared to $P \\to Q \\to R \\to S \\to T$.\nTherefore, the statement claiming orientation is identical is FALSE and is the correct answer.\nWhy other choices are incorrect: Choices A, B, and C are all true statements about congruent polygons resulting from rigid motions."
    }
]

def get_module1_final_test():
    """Returns the list of 25 Module 1 Final Mastery Test questions."""
    return MODULE_1_FINAL_TEST_QUESTIONS

if __name__ == "__main__":
    print(f"Total Module 1 Final Test Questions: {len(MODULE_1_FINAL_TEST_QUESTIONS)}")
    lesson_counts = {}
    for q in MODULE_1_FINAL_TEST_QUESTIONS:
        les = q["lesson"]
        lesson_counts[les] = lesson_counts.get(les, 0) + 1
    print("Lesson Distribution:", lesson_counts)
