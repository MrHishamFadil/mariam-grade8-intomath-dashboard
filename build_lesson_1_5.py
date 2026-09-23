# -*- coding: utf-8 -*-
"""
build_lesson_1_5.py
HMH Into Math Grade 8 - Lesson 1.5: Understand and Recognize Congruent Figures
Curriculum Question Bank: EXACTLY 20 high-quality Multiple Choice Questions (MCQs)
Based on HMH Into Math Grade 8 Teacher Edition (pages 72-83)

Covers:
1. Definition of congruence (Rigid motions / isometries)
2. Congruence statements & vertex correspondence
3. Corresponding parts of congruent figures (CPCTC)
4. Sequences of rigid motions & non-commutativity
5. Glide reflection (definition & coordinate applications)
6. Non-congruent figures (angle/side differences, dilations k != 1)
7. Explaining congruence using transformation arguments & critiquing reasoning
8. Area and perimeter equality under rigid motions
9. Quilt patterns, tiling, and coordinate plane congruence proofs
10. Open-ended multi-step sequences mapping figures
"""

LESSON_1_5_DATA = {
    "lessonId": "1.5",
    "lessonNumber": "1.5",
    "moduleNumber": 1,
    "moduleId": "module-1",
    "moduleTitle": "Module 1: Transformations and Congruence",
    "title": "Lesson 1.5: Understand and Recognize Congruent Figures",
    "standards": [
        "CCSS.MATH.CONTENT.8.G.A.2",
        "CCSS.MATH.CONTENT.8.G.A.3"
    ],
    "description": (
        "Comprehensive collection of 20 authentic, pedagogical MCQs covering "
        "rigid motion definitions of congruence, vertex ordering in congruence statements, "
        "corresponding parts (CPCTC), composition of transformations, glide reflections, "
        "distinguishing non-congruent shapes, invariant perimeter/area, and quilt/coordinate proofs."
    ),
    "mcqs": [
        # -------------------------------------------------------------------------
        # TOPIC 1: Definition of Congruence (Rigid Motions / Isometries)
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-1",
            "q": (
                "According to the geometric definition of congruence based on transformations, "
                "two two-dimensional figures are congruent ($\\cong$) if and only if:"
            ),
            "opts": [
                "There is a sequence of one or more rigid motions (translations, reflections, rotations) that maps one figure onto the other.",
                "One figure can be mapped onto the other using a dilation with a scale factor $k > 1$.",
                "Both figures have the exact same number of sides, regardless of side lengths or interior angle measures.",
                "The figures have the same perimeter even if their corresponding angle measures are different."
            ],
            "correct": 0,
            "hint": "Recall from Into Math Lesson 1.5 that rigid motions preserve both side lengths and angle measures without stretching, shrinking, or distorting.",
            "explanation": (
                "By the Common Core and HMH Into Math definition (8.G.A.2), two figures are congruent ($\\cong$) "
                "if and only if there is a sequence of rigid motions (translations, reflections, and rotations) that maps "
                "one figure exactly onto the other. Rigid motions preserve distance and angle measure.\n"
                "• Distractor B describes an enlargement dilation, which changes size ($k \\neq 1$) and produces similar, not congruent, figures.\n"
                "• Distractor C is incorrect because having the same number of sides (e.g., any two arbitrary triangles) does not guarantee identical shape or size.\n"
                "• Distractor D is incorrect because equal perimeter does not guarantee congruent shapes (e.g., a $3 \\times 5$ rectangle and a $4 \\times 4$ square both have perimeter 16, but different shapes)."
            ),
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-2",
            "q": (
                "Polygon $P$ undergoes a transformation on the Cartesian coordinate plane. "
                "Which resulting polygon is **guaranteed** to be congruent to Polygon $P$ ($P \\cong \\text{Image}$)? "
            ),
            "opts": [
                "Polygon $Q$ formed by multiplying all coordinates by $1.5$: $(x, y) \\to (1.5x, 1.5y)$",
                "Polygon $R$ formed by a horizontal stretch: $(x, y) \\to (3x, y)$",
                "Polygon $S$ formed by a $90^\\circ$ counterclockwise rotation followed by a translation 6 units left: $(x, y) \\to (-y - 6, x)$",
                "Polygon $T$ formed by adding 4 to $x$ while multiplying $y$ by $0.5$: $(x, y) \\to (x + 4, 0.5y)$"
            ],
            "correct": 2,
            "hint": "Identify which operation is a composition composed purely of rigid motions (isometries) that preserve distances between all pairs of points.",
            "explanation": (
                "Rotations and translations are rigid motions. Any sequence consisting solely of rigid motions "
                "preserves all distances and angle measures, guaranteeing that the image is congruent to the preimage ($P \\cong S$). "
                "A $90^\\circ$ rotation counterclockwise maps $(x, y) \\to (-y, x)$, and a translation 6 units left maps that to $(-y - 6, x)$.\n"
                "• Distractor A is a dilation by scale factor $1.5$, which increases side lengths by $50\\%$.\n"
                "• Distractor B triples the horizontal dimension, distorting the shape.\n"
                "• Distractor D compresses the vertical dimension by half ($0.5y$), destroying congruence."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 2: Congruence Statements & Vertex Correspondence
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-3",
            "q": (
                "Given the formal congruence statement $\\triangle MNP \\cong \\triangle STW$, "
                "which pair of corresponding parts **must** be congruent?"
            ),
            "opts": [
                "Side $MN \\cong \\text{side } TW$ and $\\angle P \\cong \\angle S$",
                "Side $NP \\cong \\text{side } TW$ and $\\angle M \\cong \\angle S$",
                "Side $MP \\cong \\text{side } ST$ and $\\angle N \\cong \\angle W$",
                "Side $MN \\cong \\text{side } SW$ and $\\angle P \\cong \\angle T$"
            ],
            "correct": 1,
            "hint": "In a congruence statement, vertices are written in exact matching order: 1st to 1st ($M \\leftrightarrow S$), 2nd to 2nd ($N \\leftrightarrow T$), and 3rd to 3rd ($P \\leftrightarrow W$).",
            "explanation": (
                "The order of vertices in a congruence statement defines the one-to-one correspondence:\n"
                "• 1st vertex: $M \\leftrightarrow S$\n"
                "• 2nd vertex: $N \\leftrightarrow T$\n"
                "• 3rd vertex: $P \\leftrightarrow W$\n"
                "Therefore, side $NP$ (vertices 2 and 3) corresponds to side $TW$ (vertices 2 and 3), "
                "and $\\angle M$ (vertex 1) corresponds to $\\angle S$ (vertex 1). Hence, side $NP \\cong \\text{side } TW$ and $\\angle M \\cong \\angle S$.\n"
                "• Distractor A mismatches side $MN$ (1-2) with $TW$ (2-3) and $\\angle P$ (3) with $\\angle S$ (1).\n"
                "• Distractor C mismatches side $MP$ (1-3) with $ST$ (1-2) and $\\angle N$ (2) with $\\angle W$ (3).\n"
                "• Distractor D mismatches side $MN$ (1-2) with $SW$ (1-3) and $\\angle P$ (3) with $\\angle T$ (2)."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-4",
            "q": (
                "Triangle $\\triangle ABC$ has vertices $A(1, 2)$, $B(4, 2)$, and $C(1, 6)$. "
                "It is reflected across the $y$-axis to produce an image with vertices $X(-1, 2)$, $Y(-4, 2)$, and $Z(-1, 6)$, "
                "where $A$ maps to $X$, $B$ maps to $Y$, and $C$ maps to $Z$. "
                "Which congruence statement correctly expresses this relationship?"
            ),
            "opts": [
                "$\\triangle ABC \\cong \\triangle YXZ$",
                "$\\triangle ABC \\cong \\triangle ZYX$",
                "$\\triangle ABC \\cong \\triangle YZX$",
                "$\\triangle ABC \\cong \\triangle XYZ$"
            ],
            "correct": 3,
            "hint": "Match each letter in the preimage to its specific reflection image: $A(1, 2) \\to X(-1, 2)$, $B(4, 2) \\to Y(-4, 2)$, $C(1, 6) \\to Z(-1, 6)$.",
            "explanation": (
                "Under reflection across the $y$-axis, $(x, y) \\to (-x, y)$:\n"
                "• $A(1, 2) \\to X(-1, 2)$, so $A \\leftrightarrow X$\n"
                "• $B(4, 2) \\to Y(-4, 2)$, so $B \\leftrightarrow Y$\n"
                "• $C(1, 6) \\to Z(-1, 6)$, so $C \\leftrightarrow Z$\n"
                "A congruence statement must write matching vertices in the exact same positional sequence. "
                "Therefore, $\\triangle ABC \\cong \\triangle XYZ$ is the only correctly ordered statement.\n"
                "• Distractors A, B, and C place the vertices out of correspondence."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 3: Corresponding Parts of Congruent Figures (CPCTC)
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-5",
            "q": (
                "If $\\triangle DEF \\cong \\triangle JKL$, with $m\\angle D = 43^\\circ$, $m\\angle E = 79^\\circ$, "
                "side $DE = 6.8\\text{ cm}$, and side $EF = 9.2\\text{ cm}$, "
                "what are the measure of $\\angle L$ and the length of side $JK$?"
            ),
            "opts": [
                "$m\\angle L = 58^\\circ$ and $JK = 6.8\\text{ cm}$",
                "$m\\angle L = 43^\\circ$ and $JK = 9.2\\text{ cm}$",
                "$m\\angle L = 79^\\circ$ and $JK = 6.8\\text{ cm}$",
                "$m\\angle L = 58^\\circ$ and $JK = 9.2\\text{ cm}$"
            ],
            "correct": 0,
            "hint": "Use the triangle angle sum ($180^\\circ$) to calculate $m\\angle F$ first. Then use CPCTC: $\\angle L \\cong \\angle F$ and side $JK \\cong \\text{side } DE$.",
            "explanation": (
                "Step 1: Find the missing angle measure in $\\triangle DEF$ using the Triangle Angle Sum Theorem:\n"
                "$$m\\angle F = 180^\\circ - (43^\\circ + 79^\\circ) = 180^\\circ - 122^\\circ = 58^\\circ$$\n"
                "Step 2: By CPCTC (Corresponding Parts of Congruent Triangles are Congruent):\n"
                "• Vertex $F$ corresponds to vertex $L$, so $m\\angle L = m\\angle F = 58^\\circ$.\n"
                "• Side $DE$ (vertices 1-2) corresponds to side $JK$ (vertices 1-2), so $JK = DE = 6.8\\text{ cm}$.\n"
                "• Distractor B incorrectly equates $\\angle L$ with $\\angle D$ and $JK$ with $EF$.\n"
                "• Distractor C incorrectly equates $\\angle L$ with $\\angle E$.\n"
                "• Distractor D gets the angle right ($58^\\circ$) but mistakenly pairs $JK$ with $EF$ ($9.2\\text{ cm}$)."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-6",
            "q": (
                "Quadrilaterals $ABCD$ and $EFGH$ are congruent ($ABCD \\cong EFGH$). "
                "If side $BC = 4x - 7$ and corresponding side $FG = 2x + 9$, "
                "what is the actual numerical length of side $FG$?"
            ),
            "opts": [
                "$x = 8$, so $FG = 17$",
                "$x = 1$, so $FG = 11$",
                "$x = 8$, so $FG = 25$",
                "$x = 16$, so $FG = 41$"
            ],
            "correct": 2,
            "hint": "Corresponding sides of congruent figures have equal lengths. Set $4x - 7 = 2x + 9$ to solve for $x$, then substitute $x$ into $2x + 9$.",
            "explanation": (
                "Step 1: Set the lengths of corresponding sides equal because $ABCD \\cong EFGH$ implies $BC = FG$:\n"
                "$$4x - 7 = 2x + 9$$\n"
                "Step 2: Solve the linear equation for $x$:\n"
                "$$4x - 2x = 9 + 7 \\implies 2x = 16 \\implies x = 8$$\n"
                "Step 3: Substitute $x = 8$ back into the expression for $FG$:\n"
                "$$FG = 2(8) + 9 = 16 + 9 = 25$$\n"
                "(Check: $BC = 4(8) - 7 = 32 - 7 = 25$, confirming $BC = FG$).\n"
                "• Distractor A solves $x = 8$ correctly but subtracts 8 from 25 or miscalculates $2(8) + 1$.\n"
                "• Distractor B makes a sign error when moving terms ($4x - 2x = 9 - 7 \\implies 2x = 2 \\implies x = 1$).\n"
                "• Distractor D forgets to divide 16 by 2 when solving $2x = 16$."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 4: Sequences of Rigid Motions & Non-Commutativity
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-7",
            "q": (
                "A polygon vertex located at $P(-3, 5)$ undergoes a two-step sequence of rigid motions:\n"
                "• **Step 1:** Reflection across the $x$-axis.\n"
                "• **Step 2:** Translation by the vector rule $(x, y) \\to (x + 7, y - 2)$.\n"
                "What are the coordinates of the final image point $P''$?"
            ),
            "opts": [
                "$(4, 3)$",
                "$(4, -7)$",
                "$(-10, -7)$",
                "$(4, -3)$"
            ],
            "correct": 1,
            "hint": "Apply the transformations in order: first reflect across the $x$-axis: $(x, y) \\to (x, -y)$, then apply the translation to the resulting coordinates.",
            "explanation": (
                "Step 1 (Reflection across $x$-axis): The rule is $(x, y) \\to (x, -y)$.\n"
                "$$P(-3, 5) \\to P'(-3, -5)$$\n"
                "Step 2 (Translation $(x + 7, y - 2)$):\n"
                "$$P'(-3, -5) \\to P''(-3 + 7, -5 - 2) = P''(4, -7)$$\n"
                "• Distractor A translates the original point $P(-3, 5)$ directly without reflecting: $(-3 + 7, 5 - 2) = (4, 3)$.\n"
                "• Distractor C subtracts 7 from $x$ instead of adding: $(-3 - 7, -5 - 2) = (-10, -7)$.\n"
                "• Distractor D reflects across the $y$-axis first instead of the $x$-axis: $(3, 5) \\to (3 + 7, 5 - 2) = (10, 3)$ or miscalculates $-5 - 2$."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-8",
            "q": (
                "In HMH Into Math Lesson 1.5 Task 3, students investigate whether the order of transformations matters. "
                "Starting with the point $A(2, 5)$:\n"
                "• **Order 1:** Reflect across the $y$-axis, then translate 3 units right.\n"
                "• **Order 2:** Translate 3 units right, then reflect across the $y$-axis.\n"
                "What are the resulting coordinates for Order 1 and Order 2, and what key geometric principle does this prove?"
            ),
            "opts": [
                "Order 1 produces $(1, 5)$; Order 2 produces $(1, 5)$. This proves that the order of transformations never matters.",
                "Order 1 produces $(-5, 5)$; Order 2 produces $(5, 5)$. This proves that reflecting across an axis doubles distance.",
                "Order 1 produces $(-1, 5)$; Order 2 produces $(-5, 5)$. This proves that the figures cease to be congruent.",
                "Order 1 produces $(1, 5)$; Order 2 produces $(-5, 5)$. This proves that transformation composition is non-commutative (order matters)."
            ],
            "correct": 3,
            "hint": "Calculate the coordinates for each order separately. For Order 1: reflect across $y$-axis first, then add 3 to $x$. For Order 2: add 3 to $x$ first, then reflect across $y$-axis.",
            "explanation": (
                "Order 1:\n"
                "1. Reflect $A(2, 5)$ across the $y$-axis: $(x, y) \\to (-x, y) \\implies A'(-2, 5)$.\n"
                "2. Translate 3 units right: $(-2 + 3, 5) = (1, 5)$.\n"
                "Order 2:\n"
                "1. Translate $A(2, 5)$ 3 units right: $(2 + 3, 5) = (5, 5)$.\n"
                "2. Reflect $(5, 5)$ across the $y$-axis: $(x, y) \\to (-x, y) \\implies (-5, 5)$.\n"
                "Because $(1, 5) \\neq (-5, 5)$, the order in which transformations are performed affects the final position. "
                "This demonstrates that transformation composition is generally non-commutative ($T_2 \\circ T_1 \\neq T_1 \\circ T_2$).\n"
                "• Distractor A incorrectly claims that order never matters.\n"
                "• Distractor B has incorrect coordinates for Order 1.\n"
                "• Distractor C incorrectly claims the figures are no longer congruent; rigid motions always preserve congruence even when landing at different locations."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 5: Glide Reflection
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-9",
            "q": (
                "In transformational geometry, what is the precise definition of a **glide reflection** "
                "mapping a geometric figure $F$ onto its congruent image $F'$ ($F \\cong F'$)? "
            ),
            "opts": [
                "A sequence consisting of a translation along a line followed by a reflection across that same line (or a line parallel to the translation direction).",
                "A reflection across a line followed by a rotation of $180^\\circ$ about a point on that line.",
                "A translation followed by an enlargement dilation with scale factor $k = 1.5$.",
                "Two consecutive reflections across two perpendicular coordinate axes that produce a half-turn."
            ],
            "correct": 0,
            "hint": "Think of footprints left by walking in wet sand: one foot steps forward (translation) and reflects across the centerline.",
            "explanation": (
                "A **glide reflection** is defined as the composition of a translation (the glide) and a reflection "
                "across a line that is parallel to the direction of translation (or along the line of translation itself). "
                "Because both translations and reflections are isometries, a glide reflection is an isometry that reverses orientation.\n"
                "• Distractor B describes a reflection combined with a rotation, not a glide reflection.\n"
                "• Distractor C includes a dilation, which alters size and is non-rigid.\n"
                "• Distractor D describes reflections across intersecting perpendicular lines, which is equivalent to a $180^\\circ$ rotation, not a glide reflection."
            ),
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-10",
            "q": (
                "Triangle $\\triangle ABC$ has vertices $A(1, 2)$, $B(4, 2)$, and $C(1, 5)$. "
                "It undergoes a glide reflection composed of:\n"
                "1. A translation by the rule $(x, y) \\to (x + 3, y)$\n"
                "2. A reflection across the $x$-axis ($y = 0$).\n"
                "What are the vertices of the image triangle $\\triangle A''B''C''$?"
            ),
            "opts": [
                "$A''(4, 2), B''(7, 2), C''(4, 5)$",
                "$A''(-4, -2), B''(-7, -2), C''(-4, -5)$",
                "$A''(4, -2), B''(7, -2), C''(4, -5)$",
                "$A''(1, -5), B''(4, -5), C''(1, -8)$"
            ],
            "correct": 2,
            "hint": "First add 3 to each $x$-coordinate: $(x + 3, y)$. Then reflect across the $x$-axis by negating each $y$-coordinate: $(x, -y)$.",
            "explanation": (
                "Step 1: Translate $(x, y) \\to (x + 3, y)$:\n"
                "• $A(1, 2) \\to A'(1 + 3, 2) = (4, 2)$\n"
                "• $B(4, 2) \\to B'(4 + 3, 2) = (7, 2)$\n"
                "• $C(1, 5) \\to C'(1 + 3, 5) = (4, 5)$\n"
                "Step 2: Reflect across the $x$-axis: $(x, y) \\to (x, -y)$:\n"
                "• $A'(4, 2) \\to A''(4, -2)$\n"
                "• $B'(7, 2) \\to B''(7, -2)$\n"
                "• $C'(4, 5) \\to C''(4, -5)$\n"
                "• Distractor A performs only the translation and forgets the reflection.\n"
                "• Distractor B incorrectly negates the $x$-coordinates as well.\n"
                "• Distractor D applies the translation to $y$ instead of $x$."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 6: Non-Congruent Figures (Angle/Side Differences & Dilations)
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-11",
            "q": (
                "In HMH Into Math Lesson 1.5 On Your Own Problem 3, students are asked: "
                "\"Can a square with side length $s_1$ ever be congruent to a regular pentagon with side length $s_2$? Explain.\"\n"
                "Which response provides the mathematically correct explanation?"
            ),
            "opts": [
                "Yes, as long as both polygons are scaled so that their perimeters are equal.",
                "No, because congruent figures must have the exact same size and shape. A square has 4 sides and four $90^\\circ$ angles, while a regular pentagon has 5 sides and five $108^\\circ$ angles; no sequence of rigid motions can change the number of sides or angle measures.",
                "Yes, because a square can be transformed into a pentagon by a sequence of a reflection followed by a dilation with scale factor $k = \\frac{5}{4}$.",
                "No, because squares are two-dimensional planar figures while pentagons are three-dimensional polyhedra."
            ],
            "correct": 1,
            "hint": "Consider the invariance properties of rigid motions: rigid motions preserve the number of vertices, side lengths, and angle measures.",
            "explanation": (
                "Congruent figures must have identical shape and size. A square has 4 vertices, 4 sides, and interior angles of $90^\\circ$. "
                "A regular pentagon has 5 vertices, 5 sides, and interior angles of $108^\\circ$. "
                "Because rigid motions preserve the number of sides and the measures of all angles, no sequence of translations, "
                "reflections, and rotations can map a 4-sided polygon onto a 5-sided polygon.\n"
                "• Distractor A is false; having equal perimeters does not make different shapes congruent.\n"
                "• Distractor C is false; dilations are not rigid motions, and dilating a square cannot add a fifth side.\n"
                "• Distractor D is false; both squares and pentagons are two-dimensional polygons."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-12",
            "q": (
                "Figure 1 is a rectangle with dimensions $4\\text{ cm} \\times 9\\text{ cm}$ (area $= 36\\text{ cm}^2$). "
                "Figure 2 is a square with dimensions $6\\text{ cm} \\times 6\\text{ cm}$ (area $= 36\\text{ cm}^2$). "
                "Are Figure 1 and Figure 2 congruent?"
            ),
            "opts": [
                "Yes, because both figures have the exact same area of $36\\text{ cm}^2$.",
                "Yes, because both figures have four $90^\\circ$ interior angles.",
                "No, because rigid motions cannot be performed on figures that have right angles.",
                "No, because their corresponding side lengths are not equal ($4 \\neq 6$ and $9 \\neq 6$), and rigid motions strictly preserve distance; equal area alone does not establish congruence."
            ],
            "correct": 3,
            "hint": "Check whether rigid motions preserve side lengths. Can you translate, reflect, or rotate a side of length 4 cm so that it covers a side of length 6 cm without stretching?",
            "explanation": (
                "While both figures have the same area ($36\\text{ cm}^2$) and both have four right angles, "
                "their side lengths are different ($4$ and $9$ vs. $6$ and $6$). "
                "Because rigid motions preserve distance (segment length), any image of Figure 1 must have side lengths "
                "of $4\\text{ cm}$ and $9\\text{ cm}$. It is impossible to map a side of length $4\\text{ cm}$ onto a side of length $6\\text{ cm}$ "
                "using rigid motions. Thus, Figure 1 is not congruent to Figure 2.\n"
                "• Distractor A is a common student trap: equal area is necessary for congruence, but not sufficient.\n"
                "• Distractor B is incorrect because having equal angles only implies similarity (for certain shapes), not congruence.\n"
                "• Distractor C is mathematically absurd; rigid motions apply to all geometric figures."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 7: Explaining Congruence Using Transformation Arguments & Critiquing
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-13",
            "q": (
                "On a math critique task (HMH Into Math Problem 8), Nathan claims: "
                "\"Figure $B$ is congruent to Figure $A$ because both figures have the exact same orientation on the grid.\" "
                "How should Nathan's mathematical reasoning be evaluated?"
            ),
            "opts": [
                "Nathan is incorrect. Having the same orientation is neither necessary nor sufficient for congruence; two figures are congruent if and only if there is a sequence of rigid motions mapping one onto the other, which preserves all side lengths and angle measures.",
                "Nathan is correct because having the same orientation is the definition of congruence in the coordinate plane.",
                "Nathan is correct because reflections reverse orientation, meaning reflected figures can never be congruent.",
                "Nathan is incorrect because congruent figures must always have opposite orientations."
            ],
            "correct": 0,
            "hint": "Can two figures face the same direction but have completely different sizes? Can two congruent figures face opposite directions?",
            "explanation": (
                "Nathan's reasoning is mathematically flawed on two levels:\n"
                "1. Having the same orientation is not sufficient: a dilated triangle can have the exact same orientation as its preimage, but have double the size (not congruent).\n"
                "2. Having the same orientation is not necessary: a figure reflected across a line has reversed orientation, yet it remains completely congruent to its preimage.\n"
                "Two figures are congruent if and only if a sequence of rigid motions maps one onto the other.\n"
                "• Distractors B, C, and D reflect common student misconceptions regarding orientation and congruence."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-14",
            "q": (
                "In HMH Into Math Lesson 1.5 Problem 14, Henrietta claims that Figure $B$ can be transformed into Figure $A$ "
                "by translating it 2 units right and then rotating it $90^\\circ$ clockwise about the origin. "
                "However, following Henrietta's instructions places the image in the wrong quadrant. "
                "How should Henrietta's sequence be corrected?"
            ),
            "opts": [
                "She must replace the rotation with a dilation of scale factor $k = 1$.",
                "She must perform the transformations in the reverse order: rotate $90^\\circ$ clockwise about the origin first, and then translate the resulting figure.",
                "She must reflect the figure across the diagonal line $y = x$ instead of rotating.",
                "She must translate the figure 4 units down before doing anything else."
            ],
            "correct": 1,
            "hint": "Check Into Math TE Page 79 Problem 14: 'The transformations must be done in the other order.' Rotating after translating swings the translation displacement around the origin!",
            "explanation": (
                "When a figure is translated first and then rotated about the origin, the rotation affects both the figure's "
                "shape orientation and its entire position vector relative to the origin. "
                "In Into Math Lesson 1.5 Problem 14, the TE explicitly notes: 'The transformations must be done in the other order.' "
                "Rotating $90^\\circ$ clockwise about the origin first, followed by the translation, places the figure in the exact location of Figure $A$.\n"
                "• Distractor A is incorrect because dilating by $k = 1$ is an identity transformation that does not change position.\n"
                "• Distractors C and D suggest incorrect transformation families or wrong translation vectors."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 8: Area and Perimeter Equality of Congruent Figures
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-15",
            "q": (
                "Right triangle $\\triangle ABC$ has legs of length $5\\text{ units}$ and $12\\text{ units}$. "
                "It undergoes a multi-step sequence of rigid motions: a rotation of $90^\\circ$ clockwise about the origin, "
                "followed by a translation of $(x - 4, y + 6)$, and finally a reflection across the line $y = 3$. "
                "What are the perimeter and area of the final image triangle $\\triangle A'''B'''C'''$?"
            ),
            "opts": [
                "$\\text{Perimeter} = 17\\text{ units}$ and $\\text{Area} = 30\\text{ sq units}$",
                "$\\text{Perimeter} = 30\\text{ units}$ and $\\text{Area} = 60\\text{ sq units}$",
                "$\\text{Perimeter} = 30\\text{ units}$ and $\\text{Area} = 30\\text{ sq units}$",
                "$\\text{Perimeter} = 60\\text{ units}$ and $\\text{Area} = 30\\text{ sq units}$"
            ],
            "correct": 2,
            "hint": "Find the hypotenuse using the Pythagorean theorem: $c = \\sqrt{5^2 + 12^2}$. Then recall that rigid motions preserve both perimeter and area.",
            "explanation": (
                "Step 1: Compute the hypotenuse and measurements of the preimage $\\triangle ABC$:\n"
                "$$c = \\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13\\text{ units}$$\n"
                "$$\\text{Perimeter} = 5 + 12 + 13 = 30\\text{ units}$$\n"
                "$$\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2}(5)(12) = 30\\text{ sq units}$$\n"
                "Step 2: Because rotations, translations, and reflections are all rigid motions (isometries), "
                "distances and enclosed areas are strictly invariant.\n"
                "Therefore, $\\text{Perimeter}(\\triangle A'''B'''C''') = 30\\text{ units}$ and $\\text{Area}(\\triangle A'''B'''C''') = 30\\text{ sq units}$.\n"
                "• Distractor A fails to include the hypotenuse in the perimeter ($5 + 12 = 17$).\n"
                "• Distractor B forgets the $\\frac{1}{2}$ in the triangle area formula ($5 \\times 12 = 60$).\n"
                "• Distractor D mistakenly doubles the perimeter."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-16",
            "q": (
                "Polygon $G$ has a perimeter of $34\\text{ cm}$ and an area of $60\\text{ cm}^2$. "
                "Polygon $H$ is the result of applying a transformation to Polygon $G$. "
                "Which condition **proves definitively** that Polygon $H$ is **NOT** congruent to Polygon $G$?"
            ),
            "opts": [
                "Polygon $H$ has its vertices labeled in counterclockwise order while Polygon $G$ has vertices in clockwise order.",
                "Polygon $H$ lies entirely in Quadrant IV while Polygon $G$ lies in Quadrant II.",
                "Polygon $H$ is rotated $180^\\circ$ relative to Polygon $G$.",
                "Polygon $H$ has a perimeter of $38\\text{ cm}$."
            ],
            "correct": 3,
            "hint": "Rigid motions preserve distances, so the perimeter of a transformed figure must remain strictly unchanged if the figures are congruent.",
            "explanation": (
                "A sequence of rigid motions preserves all segment lengths, which means the sum of side lengths (perimeter) "
                "must remain exactly the same. If Polygon $H$ has a perimeter of $38\\text{ cm}$ while Polygon $G$ has a perimeter "
                "of $34\\text{ cm}$, the side lengths have changed ($38 \\neq 34$). Therefore, no sequence of rigid motions can map $G$ to $H$, "
                "proving definitively that $G \\not\\cong H$.\n"
                "• Distractor A occurs whenever a reflection is performed; reflected shapes are still congruent.\n"
                "• Distractor B occurs when shapes are translated or rotated across quadrants; location does not affect congruence.\n"
                "• Distractor C is a rigid rotation, which preserves congruence."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 9: Quilt Patterns, Tiling, and Coordinate Plane Congruence Proofs
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-17",
            "q": (
                "In HMH Into Math Lesson 1.5 Spark Your Learning (quilt pattern), "
                "Maribel creates quilt blocks using congruent fabric triangles. "
                "One fabric triangle in Quadrant II has vertices at $(-5, 1)$, $(-2, 1)$, and $(-2, 5)$. "
                "Maribel rotates this triangle $180^\\circ$ about the center of the quilt $(0, 0)$ to place a congruent "
                "piece in Quadrant IV. What are the coordinates of the rotated quilt piece?"
            ),
            "opts": [
                "$(5, -1)$, $(2, -1)$, and $(2, -5)$",
                "$(-5, -1)$, $(-2, -1)$, and $(-2, -5)$",
                "$(1, 5)$, $(1, 2)$, and $(5, 2)$",
                "$(-1, -5)$, $(-1, -2)$, and $(-5, -2)$"
            ],
            "correct": 0,
            "hint": "The coordinate rule for a $180^\\circ$ rotation about the origin is $(x, y) \\to (-x, -y)$.",
            "explanation": (
                "Applying the coordinate rule for a $180^\\circ$ rotation about the origin, $(x, y) \\to (-x, -y)$:\n"
                "• $(-5, 1) \\to (-(-5), -(1)) = (5, -1)$\n"
                "• $(-2, 1) \\to (-(-2), -(1)) = (2, -1)$\n"
                "• $(-2, 5) \\to (-(-2), -(5)) = (2, -5)$\n"
                "All coordinates are in Quadrant IV $(+, -)$. Because a rotation is a rigid motion, "
                "the rotated quilt block is guaranteed to be congruent to the original template.\n"
                "• Distractor B reflects across the $x$-axis only: $(x, -y)$.\n"
                "• Distractor C rotates $90^\\circ$ clockwise: $(y, -x)$ or swaps coordinates.\n"
                "• Distractor D rotates $90^\\circ$ counterclockwise: $(-y, x)$."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-18",
            "q": (
                "In HMH Into Math Lesson 1.5 Step It Out Task 2, five congruent triangles are positioned on a fabric grid. "
                "Triangle $B$ has vertices $(2, -1), (5, -1),$ and $(2, -4)$. "
                "Triangle $D$ has vertices $(8, 1), (11, 1),$ and $(8, 4)$. "
                "Which sequence of transformations maps Triangle $B$ onto Triangle $D$, proving $\\triangle B \\cong \\triangle D$?"
            ),
            "opts": [
                "A translation 6 units right and 2 units up",
                "A $180^\\circ$ rotation about the origin",
                "A reflection across the $x$-axis followed by a translation 6 units right",
                "A reflection across the $y$-axis followed by a translation 10 units right"
            ],
            "correct": 2,
            "hint": "Notice that Triangle $B$ points down in the negative $y$-direction, while Triangle $D$ points up in the positive $y$-direction. This requires a reflection across a horizontal line!",
            "explanation": (
                "Let's trace the vertices through the sequence in Choice C:\n"
                "1. Reflection across the $x$-axis: $(x, y) \\to (x, -y)$:\n"
                "• $(2, -1) \\to (2, 1)$\n"
                "• $(5, -1) \\to (5, 1)$\n"
                "• $(2, -4) \\to (2, 4)$\n"
                "2. Translation 6 units right: $(x, y) \\to (x + 6, y)$:\n"
                "• $(2, 1) \\to (2 + 6, 1) = (8, 1)$\n"
                "• $(5, 1) \\to (5 + 6, 1) = (11, 1)$\n"
                "• $(2, 4) \\to (2 + 6, 4) = (8, 4)$\n"
                "These match the vertices of Triangle $D$ exactly! Since reflections and translations are rigid motions, $\\triangle B \\cong \\triangle D$.\n"
                "• Distractor A fails because a pure translation cannot change the vertical orientation from pointing down to pointing up.\n"
                "• Distractor B maps $(2, -1) \\to (-2, 1)$, placing the shape on the negative $x$-axis.\n"
                "• Distractor D reflects horizontally, leaving the shape still pointing downward."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },

        # -------------------------------------------------------------------------
        # TOPIC 10: Open-Ended Multi-Step Sequences to Map Figures
        # -------------------------------------------------------------------------
        {
            "id": "p-1-5-mcq-19",
            "q": (
                "Triangle 1 has vertices $A(1, 1), B(4, 1),$ and $C(1, 3)$. "
                "Triangle 2 has vertices $D(-1, 2), E(-1, -1),$ and $F(1, 2)$. "
                "Which sequence of transformations maps Triangle 1 directly onto Triangle 2, "
                "proving that $\\triangle 1 \\cong \\triangle 2$?"
            ),
            "opts": [
                "Translate 2 units left and 1 unit up, then reflect across the $x$-axis.",
                "Rotate $90^\\circ$ clockwise about the origin, then translate 2 units left and 3 units up.",
                "Reflect across the $y$-axis, then translate 3 units down and 1 unit right.",
                "Rotate $180^\\circ$ about the origin, then translate 1 unit right and 2 units up."
            ],
            "correct": 1,
            "hint": "Analyze the side orientation: In Triangle 1, the 3-unit leg $AB$ is horizontal. In Triangle 2, the 3-unit leg $DE$ is vertical. This rotation of $90^\\circ$ indicates a $90^\\circ$ turn!",
            "explanation": (
                "Step 1: Rotate $90^\\circ$ clockwise about the origin using $(x, y) \\to (y, -x)$:\n"
                "• $A(1, 1) \\to A'(1, -1)$\n"
                "• $B(4, 1) \\to B'(1, -4)$\n"
                "• $C(1, 3) \\to C'(3, -1)$\n"
                "Step 2: Translate 2 units left and 3 units up: $(x, y) \\to (x - 2, y + 3)$:\n"
                "• $A'(1, -1) \\to (1 - 2, -1 + 3) = (-1, 2) = D$\n"
                "• $B'(1, -4) \\to (1 - 2, -4 + 3) = (-1, -1) = E$\n"
                "• $C'(3, -1) \\to (3 - 2, -1 + 3) = (1, 2) = F$\n"
                "This maps Triangle 1 precisely onto Triangle 2. Because both transformations are rigid motions, $\\triangle 1 \\cong \\triangle 2$.\n"
                "• Distractors A, C, and D do not produce the correct orientation or vertex coordinates."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        },
        {
            "id": "p-1-5-mcq-20",
            "q": (
                "Triangle $\\triangle JKL$ with vertices $J(-5, 2), K(-2, 2),$ and $L(-2, 6)$ "
                "is transformed into $\\triangle PQR$ with vertices $P(5, -2), Q(2, -2),$ and $R(2, 2)$. "
                "Which sequence of rigid motions proves that $\\triangle JKL \\cong \\triangle PQR$?"
            ),
            "opts": [
                "A reflection across the $y$-axis: $(x, y) \\to (-x, y)$, followed by a translation 4 units down: $(x, y) \\to (x, y - 4)$",
                "A translation 7 units right followed by a reflection across the line $y = x$",
                "A $90^\\circ$ counterclockwise rotation about the origin followed by a translation 2 units right",
                "A reflection across the $x$-axis followed by a translation 3 units left"
            ],
            "correct": 0,
            "hint": "Check the $x$-coordinates: $J(-5, 2) \\to P(5, -2)$ has $x$ negated from $-5$ to $5$, suggesting a reflection across the $y$-axis first.",
            "explanation": (
                "Step 1: Reflect across the $y$-axis: $(x, y) \\to (-x, y)$:\n"
                "• $J(-5, 2) \\to J'(5, 2)$\n"
                "• $K(-2, 2) \\to K'(2, 2)$\n"
                "• $L(-2, 6) \\to L'(2, 6)$\n"
                "Step 2: Translate 4 units down: $(x, y) \\to (x, y - 4)$:\n"
                "• $J'(5, 2) \\to (5, 2 - 4) = (5, -2) = P$\n"
                "• $K'(2, 2) \\to (2, 2 - 4) = (2, -2) = Q$\n"
                "• $L'(2, 6) \\to (2, 6 - 4) = (2, 2) = R$\n"
                "The image matches $\\triangle PQR$ in every coordinate. Because reflection and translation are rigid motions, "
                "this proves that $\\triangle JKL \\cong \\triangle PQR$.\n"
                "• Distractor B gives $(x + 7, y) \\to (y, x + 7)$, which does not match $\\triangle PQR$.\n"
                "• Distractor C rotates $90^\\circ$ counterclockwise, which turns horizontal sides vertical, whereas side $JK$ and side $PQ$ are both horizontal.\n"
                "• Distractor D reflects across the $x$-axis first, giving negative $x$ coordinates."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3"
        }
    ]
}


if __name__ == "__main__":
    print(f"Loaded Lesson 1.5 data successfully:")
    print(f"Title: {LESSON_1_5_DATA['title']}")
    print(f"Number of MCQs: {len(LESSON_1_5_DATA['mcqs'])}")
    for i, mcq in enumerate(LESSON_1_5_DATA['mcqs'], 1):
        print(f"  {i}. [{mcq['id']}] (DOK {mcq['dok']}, ans={mcq['correct']}): {mcq['q'][:65]}...")
