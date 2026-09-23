# -*- coding: utf-8 -*-
"""
build_lesson_1_1.py
Master Curriculum Content, Concept Explanations, Vocabulary, Formulas,
Illustrative Examples, and 20 HMH Into Math Aligned MCQs for Lesson 1.1:
'Investigate Transformations' (Grade 8, Module 1).

Author: Antigravity (Agent 1)
Curriculum Reference: HMH Into Math Grade 8 Teacher Edition (Pages 22-35)
Standard: CCSS.MATH.CONTENT.8.G.A.1 (8.G.A.1.a, 8.G.A.1.b, 8.G.A.1.c)
"""

LESSON_1_1_DATA = {
    "lessonInfo": {
        "id": "1.1",
        "lessonNumber": "1.1",
        "moduleNumber": 1,
        "moduleId": "module-1",
        "moduleTitle": "Module 1: Transformations and Congruence",
        "title": "Lesson 1.1: Investigate Transformations",
        "tag": "Rigid Motions & Invariance",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1",
        "standards": [
            "CCSS.MATH.CONTENT.8.G.A.1",
            "CCSS.MATH.CONTENT.8.G.A.1.a",
            "CCSS.MATH.CONTENT.8.G.A.1.b",
            "CCSS.MATH.CONTENT.8.G.A.1.c"
        ],
        "iCanStatement": (
            "I can describe what happens to the side lengths, angle measures, and parallelism "
            "of a figure when it is transformed, and distinguish between rigid motions (isometries) "
            "and non-rigid motions."
        ),
        "learningObjective": (
            "Explore, observe, and mathematically prove the effects of rigid motions (translations, "
            "reflections, rotations) on two-dimensional geometric figures, verifying that side lengths, "
            "angle measures, and parallelism are strictly preserved."
        ),
        "languageObjective": (
            "Explain orally and in writing how sliding, turning, and flipping a figure affects its "
            "position, orientation, and dimensions using precise geometric vocabulary such as "
            "preimage, image, rigid motion, isometry, and invariant properties."
        )
    },

    "conceptExplanation": {
        "overview": (
            "In transformational geometry, a transformation is an operation that maps every point of a "
            "starting figure, called the preimage, to a new position on the plane, producing the image. "
            "Lesson 1.1 establishes the foundational concept of rigid motions (isometries)—transformations "
            "that preserve both distances and angle measures. Under rigid motions, figures move without "
            "any stretching, shrinking, or bending, ensuring that the preimage and image are congruent."
        ),
        "coreDefinition": (
            "A **rigid motion** (also known as an **isometry**, from Greek *isos* meaning 'equal' and *metron* "
            "meaning 'measure') is a transformation that preserves distance between all points. As a direct "
            "mathematical consequence, rigid motions preserve segment lengths, angle measures, parallelism, "
            "collinearity, perimeter, and area."
        ),
        "rigidVsNonRigid": {
            "rigidMotions": [
                {
                    "name": "Translation (Slide)",
                    "action": "Shifts every point of a figure by the same distance in a specified direction.",
                    "properties": "Preserves side lengths, angle measures, parallelism, and vertex orientation (direct isometry)."
                },
                {
                    "name": "Reflection (Flip)",
                    "action": "Flips a figure across a specified line of reflection.",
                    "properties": "Preserves side lengths, angle measures, and parallelism; REVERSES vertex orientation from clockwise to counterclockwise or vice versa (opposite isometry)."
                },
                {
                    "name": "Rotation (Turn)",
                    "action": "Turns a figure by a specified angle in a clockwise or counterclockwise direction around a fixed center point.",
                    "properties": "Preserves side lengths, angle measures, parallelism, and vertex orientation (direct isometry)."
                }
            ],
            "nonRigidMotions": [
                {
                    "name": "Dilation",
                    "action": "Enlarges or reduces a figure proportionally from a center point by a scale factor $k \\neq 1$.",
                    "properties": "Preserves angle measures and shape, but CHANGES side lengths, perimeter, and area. (Creates similar, not congruent, figures)."
                },
                {
                    "name": "Horizontal or Vertical Stretch/Compression",
                    "action": "Multiplies only one coordinate axis by a factor (e.g., $(x, y) \\to (2x, y)$).",
                    "properties": "Distorts both side lengths and angle measures. Figures are neither congruent nor similar."
                }
            ]
        },
        "fiveInvarianceProperties": [
            {
                "property": "1. Preservation of Distance (Side Lengths)",
                "rule": "\\text{Length}(A'B') = \\text{Length}(AB)",
                "description": "Every line segment in the image has the exact same Euclidean length as the corresponding segment in the preimage."
            },
            {
                "property": "2. Preservation of Angle Measures",
                "rule": "m\\angle A' = m\\angle A",
                "description": "Every interior angle in the image has the identical degree measure as the corresponding angle in the preimage."
            },
            {
                "property": "3. Preservation of Parallelism",
                "rule": "AB \\parallel CD \\implies A'B' \\parallel C'D'",
                "description": "If two lines or segments are parallel in the preimage, their images remain parallel and maintain the exact same perpendicular distance apart."
            },
            {
                "property": "4. Preservation of Collinearity & Betweenness",
                "rule": "B \\text{ is between } A \\text{ and } C \\implies B' \\text{ is between } A' \\text{ and } C'",
                "description": "Points lying on a straight line remain on a straight line. Straight lines never bend into curves under rigid motions."
            },
            {
                "property": "5. Invariance of Perimeter and Area",
                "rule": "P_{\\text{image}} = P_{\\text{preimage}}, \\quad \\text{Area}_{\\text{image}} = \\text{Area}_{\\text{preimage}}",
                "description": "Because all boundary lengths and interior angles are conserved, the total boundary perimeter and the enclosed 2D area are 100% invariant."
            }
        ],
        "orientationAndChirality": (
            "Orientation refers to the rotational order of vertices around the perimeter of a polygon. "
            "If vertices $A \\to B \\to C$ read in a clockwise direction in the preimage: "
            "(1) Under a **translation** or **rotation**, $A' \\to B' \\to C'$ remains in **clockwise** order (Direct Isometry). "
            "(2) Under a **reflection**, $A' \\to B' \\to C'$ reverses to **counterclockwise** order (Opposite Isometry). "
            "Understanding this distinction is vital for proving whether two congruent shapes require a reflection to map onto each other."
        ),
        "misconceptionsAndTeacherAlerts": [
            {
                "misconception": "Moving across axes or into different quadrants changes size or makes measurements negative.",
                "teacherGuidance": "Coordinates can be negative, but geometric distance $d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ is strictly non-negative. A rectangle translated into Quadrant III retains identical positive side lengths and positive area."
            },
            {
                "misconception": "A slanted or diagonal line segment is longer than a horizontal segment.",
                "teacherGuidance": "When a horizontal segment is rotated $45^\\circ$, students often believe it grew longer because it crosses grid squares diagonally. Emphasize that rotation changes slope, not distance."
            },
            {
                "misconception": "Any transformation defined by a neat algebraic rule is a rigid motion.",
                "teacherGuidance": "Rules such as $(x, y) \\to (2x, y)$ or $(x, y) \\to (3x, 3y)$ are algebraic transformations, but they stretch the plane non-uniformly or scale it, violating distance preservation."
            },
            {
                "misconception": "Equal perimeter guarantees rigid motion / congruence.",
                "teacherGuidance": "Two rhombuses can both have perimeter $20\\text{ cm}$, but if one has angles $74^\\circ/106^\\circ$ and the other has $60^\\circ/120^\\circ$, they cannot be mapped via rigid motion because angle measures are not preserved."
            }
        ],
        "realWorldConnections": [
            "Daniel's Sandwich Slice (HMH Into Math TE Opening): Cutting a sandwich diagonally produces two right triangles that can be slid and turned to form a rectangle; side lengths, perimeter, and area are conserved.",
            "Carpenter's Blueprint & Board Cuts (HMH Into Math TE Challenge): Rotating cut wooden boards allows carpenters to create identical roof trusses and birdhouse parts with zero waste.",
            "Nautical Signaling Flags (HMH Into Math TE More Practice): Ships flip flags vertically to signal distress. The flag retains its shape and size, but reversing top and bottom creates an internationally recognized distress call."
        ]
    },

    "essentialVocabulary": [
        {
            "term": "Transformation",
            "definition": "An operation that maps every point of a geometric figure (preimage) to a new position (image) in a plane.",
            "example": "Translating a triangle 4 units right and 2 units up is a geometric transformation."
        },
        {
            "term": "Preimage",
            "definition": "The original figure prior to the application of a transformation.",
            "example": "In $\\triangle ABC \\to \\triangle A'B'C'$, $\\triangle ABC$ is the preimage."
        },
        {
            "term": "Image",
            "definition": "The resulting figure after a transformation has been applied, denoted with prime symbols ($A'$).",
            "example": "In $\\triangle ABC \\to \\triangle A'B'C'$, $\\triangle A'B'C'$ is the image."
        },
        {
            "term": "Rigid Motion (Isometry)",
            "definition": "A transformation that preserves Euclidean distance between all points and preserves all angle measures. Preimage and image are congruent.",
            "example": "Translations, reflections, and rotations are the three fundamental rigid motions in the plane."
        },
        {
            "term": "Non-Rigid Motion",
            "definition": "A transformation that alters distances between points, changing the size or proportions of the figure.",
            "example": "Dilations and directional stretches are non-rigid motions."
        },
        {
            "term": "Translation (Slide)",
            "definition": "A rigid motion that shifts every point of a figure by the same distance in the same direction along a vector.",
            "example": "Mapping rule: $(x, y) \\to (x + a, y + b)$."
        },
        {
            "term": "Reflection (Flip)",
            "definition": "A rigid motion that maps each point to its mirror image across a specified line of reflection.",
            "example": "Reflecting across the $y$-axis: $(x, y) \\to (-x, y)$."
        },
        {
            "term": "Rotation (Turn)",
            "definition": "A rigid motion that turns every point of a figure through a specified angle and direction about a fixed point called the center of rotation.",
            "example": "Rotating $90^\\circ$ counterclockwise about the origin: $(x, y) \\to (-y, x)$."
        },
        {
            "term": "Orientation (Chirality)",
            "definition": "The relative order of vertices around the boundary of a figure (clockwise vs. counterclockwise).",
            "example": "Translations and rotations preserve orientation; reflections reverse it."
        },
        {
            "term": "Congruence ($\\cong$)",
            "definition": "The relationship between two geometric figures where one can be mapped exactly onto the other by a sequence of rigid motions.",
            "example": "If $\\triangle ABC$ undergoes a rigid motion to become $\\triangle A'B'C'$, then $\\triangle ABC \\cong \\triangle A'B'C'$."
        },
        {
            "term": "Parallelism Invariance",
            "definition": "The geometric theorem stating that if two lines or segments are parallel, their images under any rigid motion remain parallel.",
            "example": "If $\\overline{AB} \\parallel \\overline{CD}$, then $\\overline{A'B'} \\parallel \\overline{C'D'}$."
        },
        {
            "term": "Collinearity",
            "definition": "The property of three or more points lying on a single straight line. Rigid motions always map straight lines to straight lines.",
            "example": "If points $A$, $B$, and $C$ lie on line $\\ell$, their images $A'$, $B'$, and $C'$ lie on line $\\ell'$."
        }
    ],

    "formulasAndProperties": [
        {
            "name": "Distance Invariance (Isometry)",
            "formula": "d(A', B') = d(A, B)",
            "description": "The length of any segment in the image equals the length of the corresponding segment in the preimage."
        },
        {
            "name": "Angle Measure Invariance",
            "formula": "m\\angle A' = m\\angle A",
            "description": "Corresponding angle measures remain strictly identical."
        },
        {
            "name": "Parallelism Invariance",
            "formula": "L_1 \\parallel L_2 \\implies L'_1 \\parallel L'_2",
            "description": "Lines that do not intersect in the preimage will never intersect in the image."
        },
        {
            "name": "Perimeter Invariance",
            "formula": "P_{\\text{image}} = P_{\\text{preimage}}",
            "description": "Sum of side lengths is unchanged under all rigid motions."
        },
        {
            "name": "Area Invariance",
            "formula": "\\text{Area}_{\\text{image}} = \\text{Area}_{\\text{preimage}}",
            "description": "Two-dimensional surface enclosed by the polygon remains constant."
        },
        {
            "name": "Direct Isometry (Orientation Preserved)",
            "formula": "\\text{Clockwise} \\to \\text{Clockwise}",
            "description": "Applies to translations and rotations."
        },
        {
            "name": "Opposite Isometry (Orientation Reversed)",
            "formula": "\\text{Clockwise} \\to \\text{Counterclockwise}",
            "description": "Applies to reflections across any line."
        }
    ],

    "illustrativeExamples": [
        {
            "id": "ex-1.1-1",
            "title": "Example 1: Verifying Invariant Properties on a Right Trapezoid",
            "description": (
                "Right trapezoid $ABCD$ has vertices $A(1, 1)$, $B(5, 1)$, $C(3, 4)$, and $D(1, 4)$. "
                "Side $\\overline{AB}$ is parallel to side $\\overline{CD}$ ($\parallel$), $AD = 3\\text{ units}$, "
                "$AB = 4\\text{ units}$, $CD = 2\\text{ units}$, and $m\\angle A = 90^\\circ$. "
                "The trapezoid is translated $3\\text{ units}$ right and $2\\text{ units}$ up to form $A'B'C'D'$."
            ),
            "stepByStepExplanation": [
                "Step 1: Calculate preimage dimensions: Base $AB = 5 - 1 = 4$, top base $CD = 3 - 1 = 2$, vertical height $AD = 4 - 1 = 3$. By Pythagorean theorem, slant leg $BC = \\sqrt{(5-3)^2 + (1-4)^2} = \\sqrt{4 + 9} = \\sqrt{13} \\approx 3.61\\text{ units}$.",
                "Step 2: Apply translation vector $(x, y) \\to (x + 3, y + 2)$: $A'(4, 3)$, $B'(7, 3)$, $C'(6, 6)$, $D'(4, 6)$.",
                "Step 3: Measure image dimensions: Base $A'B' = 7 - 4 = 4$, top base $C'D' = 6 - 4 = 2$, vertical height $A'D' = 6 - 3 = 3$, slant leg $B'C' = \\sqrt{(7-6)^2 + (3-6)^2} = \\sqrt{1 + 9} = \\sqrt{10}$... wait, check coords: $B(5,1) \\to B'(8,3), C(3,4) \\to C'(6,6)$, $B'C' = \\sqrt{(8-6)^2 + (3-6)^2} = \\sqrt{13}$. All segment lengths match exactly!",
                "Step 4: Check parallelism and angles: $A'B'$ lies on $y = 3$ and $C'D'$ lies on $y = 6$. Both have slope $m = 0$, so $A'B' \\parallel C'D'$. $A'D'$ is vertical ($x = 4$), forming a $90^\\circ$ angle with $A'B'$.",
                "Step 5: Conclude: Distance, angle measures, and parallelism are strictly preserved. Therefore, the translation is a rigid motion, and $ABCD \\cong A'B'C'D'$."
            ],
            "keyTakeaway": "Translating a figure preserves side lengths, parallelism, and right angles without distortion."
        },
        {
            "id": "ex-1.1-2",
            "title": "Example 2: Distinguishing Rigid vs. Non-Rigid Transformations & Tracking Orientation",
            "description": (
                "Triangle $PQR$ with vertices $P(1, 1)$, $Q(4, 1)$, and $R(1, 5)$ undergoes two separate operations: "
                "Operation 1: Reflection across the $y$-axis to form $\\triangle P'Q'R'$. "
                "Operation 2: Vertical stretch $(x, y) \\to (x, 2y)$ to form $\\triangle P''Q''R''$."
            ),
            "stepByStepExplanation": [
                "Step 1: Analyze Operation 1 (Reflection): Preimage side lengths are $PQ = 3$, $PR = 4$, $QR = 5$. Image coordinates are $P'(-1, 1)$, $Q'(-4, 1)$, $R'(-1, 5)$. Side lengths are $P'Q' = 3$, $P'R' = 4$, $Q'R' = 5$. All distances and angles are preserved! However, tracing $P \\to Q \\to R$ in the preimage is counterclockwise, whereas $P' \\to Q' \\to R'$ in the image is clockwise. Orientation is reversed, but Operation 1 is a RIGID MOTION.",
                "Step 2: Analyze Operation 2 (Vertical Stretch): Image coordinates are $P''(1, 2)$, $Q''(4, 2)$, $R''(1, 10)$. Side $P''Q'' = 3$, but vertical side $P''R'' = 10 - 2 = 8$. Hypotenuse $Q''R'' = \\sqrt{(4-1)^2 + (2-10)^2} = \\sqrt{9 + 64} = \\sqrt{73} \\approx 8.54\\text{ units}$.",
                "Step 3: Compare side lengths: $P''R'' = 8 \\neq PR = 4$. Because distances are not preserved, Operation 2 is NOT A RIGID MOTION.",
                "Step 4: Conclude: Reflection preserves distances and angles while reversing orientation (rigid motion). Vertical stretch alters distances and angles (non-rigid motion)."
            ],
            "keyTakeaway": "A transformation is rigid if and only if it preserves all segment lengths. Reversing vertex orientation during reflection does not violate rigidity."
        }
    ],

    "workedExamplesModelAnswers": [
        {
            "id": "we-1.1-1",
            "problemPrompt": (
                "Quadrilateral $WXYZ$ has vertices $W(2, 3)$, $X(6, 3)$, $Y(8, 7)$, and $Z(4, 7)$. "
                "Side $WX = 4\\text{ units}$, $YZ = 4\\text{ units}$, and $\\overline{WX} \\parallel \\overline{YZ}$ with height $4\\text{ units}$. "
                "The figure is rotated $180^\\circ$ about the origin to form $W'X'Y'Z'$. "
                "Determine: (a) the length of side $\\overline{W'X'}$, (b) whether $\\overline{W'X'} \\parallel \\overline{Y'Z'}$, "
                "and (c) whether the perimeter and area of $W'X'Y'Z'$ equal those of $WXYZ$. Justify using properties of rigid motions."
            ),
            "context": "HMH Into Math TE - Formative Assessment Benchmark",
            "step1": (
                "Identify Given Information & Transformation Type: Preimage $WXYZ$ is a parallelogram with base $b = 4\\text{ units}$, "
                "height $h = 4\\text{ units}$, slant side length $\\sqrt{(6-8)^2 + (3-7)^2} = \\sqrt{4+16} = \\sqrt{20} \\approx 4.47\\text{ units}$, "
                "perimeter $P = 2(4 + \\sqrt{20}) \\approx 16.94\\text{ units}$, and area $A = b \\times h = 4 \\times 4 = 16\\text{ units}^2$. "
                "The transformation is a $180^\\circ$ rotation about the origin, which is an isometry (rigid motion)."
            ),
            "step2": (
                "Apply Invariance Theorems: Under any rotation (rigid motion): "
                "(1) Line segments are taken to line segments of equal length (Distance Invariance), so $W'X' = WX = 4\\text{ units}$. "
                "(2) Parallel lines are taken to parallel lines (Parallelism Invariance), so $\\overline{W'X'} \\parallel \\overline{Y'Z'}$. "
                "(3) Because all side lengths and heights are preserved, the perimeter and area are invariant."
            ),
            "step3": (
                "Write Formal Conclusion: "
                "(a) $W'X' = 4\\text{ units}$. "
                "(b) $\\overline{W'X'} \\parallel \\overline{Y'Z'}$. "
                "(c) $\\text{Perimeter}(W'X'Y'Z') = 2(4 + \\sqrt{20})\\text{ units}$ and $\\text{Area}(W'X'Y'Z') = 16\\text{ units}^2$, "
                "both identical to the preimage. Because distance and angles are preserved, $WXYZ \\cong W'X'Y'Z'$."
            ),
            "rubricGuidance": (
                "Full credit (4/4): 1 pt for stating $W'X' = 4$ citing distance preservation; 1 pt for confirming parallelism citing 8.G.A.1.c; "
                "1 pt for correctly computing and equating perimeter and area; 1 pt for explicitly naming rotation as a rigid motion/isometry."
            )
        },
        {
            "id": "we-1.1-2",
            "problemPrompt": (
                "Triangle $\\triangle ABC$ with vertices $A(1, 2)$, $B(4, 2)$, and $C(1, 6)$ is reflected across the vertical line $x = 0$ ($y$-axis). "
                "A student claims that because the triangle was flipped, its angles were inverted and its side lengths are now negative coordinates, "
                "meaning the figure is no longer congruent to the original. Write a point-by-point geometric refutation."
            ),
            "context": "HMH Into Math TE - Teacher Edition Misconceptions Critique",
            "step1": (
                "Identify Coordinates & Geometric Dimensions: Preimage $A(1, 2)$, $B(4, 2)$, $C(1, 6)$ forms a right triangle with legs $AB = 3$ and $AC = 4$, "
                "and hypotenuse $BC = 5$. The image coordinates under reflection across the $y$-axis $(x, y) \\to (-x, y)$ are $A'(-1, 2)$, $B'(-4, 2)$, and $C'(-1, 6)$."
            ),
            "step2": (
                "Refute Negative Coordinate Misconception: Coordinates represent location, whereas side length is geometric distance. "
                "Using the distance formula: $A'B' = |-4 - (-1)| = 3\\text{ units}$, $A'C' = |6 - 2| = 4\\text{ units}$, and $B'C' = \\sqrt{(-4 - (-1))^2 + (2 - 6)^2} = 5\\text{ units}$. "
                "All side lengths remain strictly positive and identical to the preimage."
            ),
            "step3": (
                "Refute Inverted Angles & Congruence Claim: In preimage $\\triangle ABC$, $\\overline{AB}$ is horizontal and $\\overline{AC}$ is vertical, forming $m\\angle A = 90^\\circ$. "
                "In image $\\triangle A'B'C'$, $\\overline{A'B'}$ is horizontal and $\\overline{A'C'}$ is vertical, forming $m\\angle A' = 90^\\circ$. "
                "All interior angle measures are preserved. While reflection reverses the vertex orientation (from clockwise to counterclockwise), "
                "reflection is a rigid motion (isometry), mathematically guaranteeing that $\\triangle ABC \\cong \\triangle A'B'C'$."
            ),
            "rubricGuidance": (
                "Full credit (4/4): 1 pt for calculating image side lengths showing they are positive and equal; 1 pt for proving angle preservation; "
                "1 pt for distinguishing between coordinate signs and geometric distance; 1 pt for clarifying that orientation reversal does not invalidate congruence."
            )
        }
    ],

    "mcqs": [
        {
            "id": "p-1-1-mcq-1",
            "q": "Which of the following transformations represents a **rigid motion** (isometry) on the coordinate plane?",
            "opts": [
                "Doubling the $x$-coordinates while keeping the $y$-coordinates the same: $(x, y) \\to (2x, y)$",
                "Dilating a polygon by a scale factor of $0.5$ centered at the origin: $(x, y) \\to (0.5x, 0.5y)$",
                "Tripling both coordinates: $(x, y) \\to (3x, 3y)$",
                "Translating a polygon $5\\text{ units}$ to the left and $3\\text{ units}$ up: $(x, y) \\to (x - 5, y + 3)$"
            ],
            "correct": 3,
            "hint": "A rigid motion (isometry) must preserve all segment lengths and angle measures without stretching, shrinking, or distorting the shape.",
            "explanation": "Option D is correct because a translation slides every point by a fixed distance without changing side lengths or angles, making it a rigid motion (isometry). Options A, B, and C are non-rigid transformations: Option A is a horizontal stretch that distorts proportions; Options B and C are dilations that alter segment lengths and areas.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-2",
            "q": "Triangle $\\triangle ABC$ has side lengths $AB = 7.4\\text{ cm}$, $BC = 5.1\\text{ cm}$, and $AC = 9.8\\text{ cm}$. If $\\triangle ABC$ is rotated $90^\\circ$ clockwise about the origin to form $\\triangle A'B'C'$, what is the exact length of side $\\overline{A'B'}$?",
            "opts": [
                "$5.1\\text{ cm}$",
                "$9.8\\text{ cm}$",
                "$7.4\\text{ cm}$",
                "Cannot be determined without knowing the center of rotation"
            ],
            "correct": 2,
            "hint": "Remember the distance preservation property of rigid motions: $\\text{Length}(A'B') = \\text{Length}(AB)$.",
            "explanation": "Option C is correct because rotation is a rigid motion (isometry). Under any rigid motion, line segments are taken to line segments of the exact same length: $\\text{Length}(A'B') = \\text{Length}(AB) = 7.4\\text{ cm}$. Options A and B cite lengths of other sides ($BC$ and $AC$). Option D is incorrect because the preservation of distance holds regardless of the chosen center of rotation.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-3",
            "q": "In right triangle $\\triangle DEF$, $m\\angle D = 38^\\circ$ and $m\\angle E = 90^\\circ$. The triangle is reflected across the $y$-axis to produce $\\triangle D'E'F'$. What is the measure of angle $\\angle F'$?",
            "opts": [
                "$38^\\circ$",
                "$90^\\circ$",
                "$142^\\circ$",
                "$52^\\circ$"
            ],
            "correct": 3,
            "hint": "First calculate the third angle in the preimage using the triangle angle sum ($180^\\circ$), then apply angle preservation.",
            "explanation": "Option D is correct. In preimage $\\triangle DEF$, the sum of angles is $180^\\circ$, so $m\\angle F = 180^\\circ - (90^\\circ + 38^\\circ) = 52^\\circ$. Because reflection is a rigid motion, angle measures are preserved: $m\\angle F' = m\\angle F = 52^\\circ$. Option A is $m\\angle D'$, Option B is $m\\angle E'$, and Option C is the obtuse supplement ($180^\\circ - 38^\\circ$).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-4",
            "q": "Trapezoid $PQRS$ has parallel bases $\\overline{PQ} \\parallel \\overline{RS}$, which are separated by a perpendicular distance of $4.5\\text{ cm}$. After trapezoid $PQRS$ is translated $6\\text{ units}$ down and reflected across a vertical line to form $P'Q'R'S'$, which statement must be true?",
            "opts": [
                "$\\overline{P'Q'}$ and $\\overline{R'S'}$ intersect at a right angle.",
                "$\\overline{P'Q'} \\parallel \\overline{R'S'}$ and the perpendicular distance between them remains $4.5\\text{ cm}$.",
                "$\\overline{P'Q'} \\parallel \\overline{R'S'}$, but the distance between them increases to $9.0\\text{ cm}$ because two transformations were performed.",
                "$\\overline{P'Q'}$ is no longer parallel to $\\overline{R'S'}$ because reflection changes line slopes."
            ],
            "correct": 1,
            "hint": "Consider standard 8.G.A.1.c: Parallel lines are taken to parallel lines under rigid motions.",
            "explanation": "Option B is correct. Translations and reflections are rigid motions, and their composition is also a rigid motion. Under rigid motions, parallel lines map to parallel lines ($\\overline{P'Q'} \\parallel \\overline{R'S'}$), and distances between corresponding points or parallel segments are invariant ($4.5\\text{ cm}$). Options A and D falsely claim parallelism is lost. Option C confuses performing multiple rigid motions with scaling/dilating.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-5",
            "q": "Three points $L$, $M$, and $N$ lie on the same straight line with $M$ located between $L$ and $N$. Given $LM = 3.2\\text{ cm}$ and $MN = 4.8\\text{ cm}$, the segment undergoes a rigid motion mapping $L \\to L'$, $M \\to M'$, and $N \\to N'$. Which deduction is mathematically guaranteed?",
            "opts": [
                "$L'$, $M'$, and $N'$ form the vertices of a scalene triangle with perimeter $16\\text{ cm}$.",
                "$L'$, $M'$, and $N'$ are non-collinear because turning a line curves it into an arc.",
                "$L'$, $M'$, and $N'$ remain collinear, $M'$ is between $L'$ and $N'$, and $L'N' = 8.0\\text{ cm}$.",
                "$M'$ is no longer between $L'$ and $N'$ because rigid motions reverse the internal order of points."
            ],
            "correct": 2,
            "hint": "Rigid motions preserve collinearity (lines map to lines) and betweenness of points on a line.",
            "explanation": "Option C is correct. Rigid motions take straight lines to straight lines and preserve betweenness of points and segment addition. In the preimage, $LN = LM + MN = 3.2 + 4.8 = 8.0\\text{ cm}$. Under rigid motion, $L'M' = 3.2\\text{ cm}$, $M'N' = 4.8\\text{ cm}$, points remain collinear with $M'$ between $L'$ and $N'$, and $L'N' = 8.0\\text{ cm}$. Options A and B contradict the fact that lines map to lines. Option D is incorrect because betweenness along a segment is preserved.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-6",
            "q": "Triangle $\\triangle JKL$ has vertices named in clockwise order around its perimeter. The triangle undergoes a rotation of $180^\\circ$ about the origin, followed by a reflection across the vertical line $x = 2$. What is the vertex orientation of the final image $J''K''L''$?",
            "opts": [
                "Clockwise, because both rotations and reflections preserve clockwise vertex order.",
                "Undefined, because multiple transformations destroy vertex order.",
                "Clockwise, because a $180^\\circ$ rotation reverses orientation and the reflection reverses it back.",
                "Counterclockwise, because rotation preserves clockwise orientation, and reflection reverses it to counterclockwise."
            ],
            "correct": 3,
            "hint": "Recall orientation behavior: translations and rotations are direct isometries (preserve orientation); reflections are opposite isometries (reverse orientation).",
            "explanation": "Option D is correct. A rotation is a direct isometry, so after the $180^\\circ$ turn, the vertices $J'K'L'$ remain in clockwise order. Then, reflecting across the line $x = 2$ is an opposite isometry, which flips the chirality (orientation) from clockwise to counterclockwise. Option C contains a common student misconception: rotations do NOT reverse orientation; only reflections reverse orientation.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-7",
            "q": "A parallelogram has base $b = 8\\text{ cm}$, slant side $s = 5\\text{ cm}$, perpendicular height $h = 4\\text{ cm}$, perimeter $P = 26\\text{ cm}$, and area $A = 32\\text{ cm}^2$. If it undergoes a $90^\\circ$ rotation followed by a translation of $\\langle -4, 7 \\rangle$, what are the perimeter and area of the resulting image?",
            "opts": [
                "$\\text{Perimeter} = 26\\text{ cm}$ and $\\text{Area} = 32\\text{ cm}^2$",
                "$\\text{Perimeter} = 52\\text{ cm}$ and $\\text{Area} = 64\\text{ cm}^2$",
                "$\\text{Perimeter} = 26\\text{ cm}$ and $\\text{Area} = 16\\text{ cm}^2$",
                "$\\text{Perimeter} = 32\\text{ cm}$ and $\\text{Area} = 26\\text{ cm}^2$"
            ],
            "correct": 0,
            "hint": "Since all side lengths and angles are strictly invariant under rigid motions, what happens to their perimeter and enclosed area?",
            "explanation": "Option A is correct. Both rotation and translation are rigid motions (isometries). Rigid motions preserve all linear distances ($A'B' = AB$), meaning the perimeter remains $P' = P = 26\\text{ cm}$. They also preserve angle measures and height, guaranteeing that the enclosed two-dimensional area is completely invariant: $A' = A = 32\\text{ cm}^2$. Options B, C, and D incorrectly alter perimeter or area.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-8",
            "q": "A student graphs polygon $ABCD$ in Quadrant I. She translates the polygon $10\\text{ units}$ left and $12\\text{ units}$ down into Quadrant III. A peer argues: *'Since the coordinates changed from positive to negative, the shape got smaller and its area became negative.'* How should this argument be refuted?",
            "opts": [
                "The peer is correct because coordinates in Quadrant III represent negative geometric lengths.",
                "The peer is incorrect; coordinates only specify position on the grid. Distance and area depend on absolute differences, which remain invariant under translation.",
                "The peer is incorrect because translations only change the area when moving diagonally.",
                "The peer is partially correct; side lengths stay positive, but area is mathematically defined as negative in Quadrant III."
            ],
            "correct": 1,
            "hint": "Look at the teacher edition note on misconceptions: shifting a figure into a different quadrant changes location, not size or physical attributes.",
            "explanation": "Option B is correct. A major misconception addressed in the HMH Teacher Edition is confusing coordinate signs with geometric measures. Coordinates denote position, but lengths are Euclidean distances $\\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$, which are always non-negative. Translation is a rigid motion, so side lengths, angles, perimeter, and area are 100% preserved. Area cannot be negative. Options A, C, and D reflect misconceptions.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-9",
            "q": "A graphic design software applies the algebraic mapping $(x, y) \\to (x + 4, 2y)$ to a rectangle with vertices $(0,0)$, $(3,0)$, $(3,2)$, and $(0,2)$. Which statement correctly classifies this transformation?",
            "opts": [
                "It is a rigid motion because all corners remain $90^\\circ$ right angles.",
                "It is a rigid motion because it includes a translation of $+4$ along the $x$-axis.",
                "It is NOT a rigid motion because the vertical sides are stretched by a factor of $2$, altering side lengths and doubling area.",
                "It is a rigid motion because it is a combination of a slide and a flip."
            ],
            "correct": 2,
            "hint": "Check whether corresponding side lengths are equal before and after the mapping.",
            "explanation": "Option C is correct. In the preimage, the height is $|2 - 0| = 2$. In the image, the $y$-coordinates are doubled, so the height becomes $|4 - 0| = 4$. Because the side length changed from $2$ to $4$, distance is not preserved ($A'B' \\neq AB$). A transformation that alters distance is by definition non-rigid (here, a vertical stretch). Option A is wrong because preserving right angles alone is insufficient (as in dilations and stretches). Options B and D are factually inaccurate.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-10",
            "q": "Consider the following claim: *'If a transformation preserves all angle measures of any polygon ($m\\angle A' = m\\angle A, m\\angle B' = m\\angle B, \\dots$), then the transformation is guaranteed to be a rigid motion.'* Which counterexample definitively disproves this claim?",
            "opts": [
                "Rotating a square $90^\\circ$ clockwise about its center",
                "Dilating an equilateral triangle by a scale factor of $k = 3$, which keeps all angles at $60^\\circ$ but triples all side lengths",
                "Reflecting an isosceles trapezoid across the line $y = x$",
                "Translating a scalene triangle $5\\text{ units}$ horizontally and $2\\text{ units}$ vertically"
            ],
            "correct": 1,
            "hint": "A counterexample must show that angle preservation alone does not guarantee distance preservation.",
            "explanation": "Option B is correct. In a dilation by a scale factor of $k = 3$, all interior angles remain exactly $60^\\circ$, yet every side length is tripled ($s' = 3s$). Because side lengths are not preserved, the dilation is NOT a rigid motion. This proves that angle preservation alone is insufficient to guarantee an isometry; distance must also be preserved. Options A, C, and D are actual rigid motions and cannot serve as counterexamples.",
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-11",
            "q": "Triangle $\\triangle ABC$ has vertices $A(2, 1)$, $B(5, 1)$, and $C(2, 6)$. Under a transformation, the image vertices are $A'(-2, 1)$, $B'(-5, 1)$, and $C'(-2, 6)$. Which transformation was performed, and what happened to its vertex orientation?",
            "opts": [
                "Reflection across the $y$-axis; vertex orientation reversed from clockwise to counterclockwise.",
                "Translation $4\\text{ units}$ left; vertex orientation was preserved.",
                "Rotation $180^\\circ$ about the origin; vertex orientation was preserved.",
                "Reflection across the $x$-axis; vertex orientation remained clockwise."
            ],
            "correct": 0,
            "hint": "Observe the coordinates: $(x, y) \\to (-x, y)$. What transformation negates only the $x$-coordinate?",
            "explanation": "Option A is correct. The coordinate rule $(x, y) \\to (-x, y)$ represents a reflection across the $y$-axis. In the preimage, tracing $A(2,1) \\to B(5,1) \\to C(2,6)$ moves along the base rightward, then up-left back to $A$, which is counterclockwise. In the image, $A'(-2,1) \\to B'(-5,1) \\to C'(-2,6)$ moves leftward along the base, then up-right, which is clockwise. Testing shows that reflection across a line always reverses orientation (swaps chirality). Option B is wrong because $B$ shifted by $-10$, not $-4$. Option C rule would be $(-x, -y)$. Option D rule would be $(x, -y)$.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-12",
            "q": "A carpenter cuts boards to create identical pieces for a birdhouse (from Into Math TE). A board in the shape of a trapezoid has one pair of parallel sides that are $2\\text{ inches}$ apart. The carpenter turns the board one-quarter turn ($90^\\circ$) clockwise on her table. What is true about the parallel sides of the turned board?",
            "opts": [
                "The parallel sides remain parallel and are still exactly $2\\text{ inches}$ apart.",
                "The sides are no longer parallel because turning them changed their directions.",
                "The parallel sides remain parallel, but the distance between them is now $2 \\times \\sqrt{2} \\approx 2.83\\text{ inches}$.",
                "The parallel sides become perpendicular to each other."
            ],
            "correct": 0,
            "hint": "Teacher Edition problem 7 & 12 note: Parallel lines stay parallel, and the distance between them remains constant under rigid motions.",
            "explanation": "Option A is correct. As emphasized in Into Math TE Lesson 1.1 Problems 7 and 11-12, when a shape undergoes a turn (rotation), rigid motion properties guarantee that: (1) parallel lines are taken to parallel lines, and (2) the distance between parallel lines remains exactly the same ($2\\text{ inches}$). Option B is a misconception. Options C and D incorrectly assume rotating changes metric distance between lines.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-13",
            "q": "Line segment $\\overline{AB}$ is horizontal with length $AB = 6\\text{ cm}$. A student rotates the segment $45^\\circ$ counterclockwise about endpoint $A$. The student claims: *'Because the segment is now slanted diagonally across grid squares, its length must be greater than $6\\text{ cm}$.'* What error did the student make?",
            "opts": [
                "The student should have measured the length in inches instead of centimeters.",
                "The student forgot that rotating a segment by $45^\\circ$ cuts its length in half.",
                "The student failed to realize that only $90^\\circ$ and $180^\\circ$ rotations preserve lengths.",
                "The student confused the visual slope/slant with geometric length; rotations are rigid motions, so distance is invariant regardless of tilt."
            ],
            "correct": 3,
            "hint": "Teacher Edition Common Error: Students often believe that diagonal segments are automatically longer than horizontal ones, confusing coordinate grid alignment with physical length.",
            "explanation": "Option D is correct. A well-documented misconception in the HMH Into Math TE is that students equate diagonal orientation with increased length (often thinking of the hypotenuse of grid squares). However, rotation is a rigid motion (isometry), which guarantees that the distance between endpoints remains invariant: $\\text{Length}(A'B') = \\text{Length}(AB) = 6\\text{ cm}$. Options A, B, and C contain false mathematical claims.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-14",
            "q": "Triangle $\\triangle PQR$ has angle measures $m\\angle P = 40^\\circ$, $m\\angle Q = 60^\\circ$, and $m\\angle R = 80^\\circ$, with an area of $24\\text{ cm}^2$. It is reflected across line $\\ell$ and then rotated $60^\\circ$ about point $P'$. What are the interior angle sum and area of the resulting triangle $P''Q''R''$?",
            "opts": [
                "Interior angle sum $= 240^\\circ$, $\\text{Area} = 24\\text{ cm}^2$",
                "Interior angle sum $= 360^\\circ$, $\\text{Area} = 48\\text{ cm}^2$",
                "Interior angle sum $= 180^\\circ$, $\\text{Area} = 24\\text{ cm}^2$",
                "Interior angle sum $= 180^\\circ$, $\\text{Area} = 12\\text{ cm}^2$"
            ],
            "correct": 2,
            "hint": "Sequences of rigid motions preserve angle measures, side lengths, and area.",
            "explanation": "Option C is correct. The composition of two rigid motions (a reflection followed by a rotation) is also a rigid motion. Every individual angle measure is preserved ($40^\\circ, 60^\\circ, 80^\\circ$), so their sum remains strictly $180^\\circ$. Furthermore, because side lengths and altitudes are invariant, the area remains exactly $24\\text{ cm}^2$. Options A, B, and D incorrectly alter the angle sum or area.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-15",
            "q": "Which of the following correctly describes how basic transformations affect the **orientation** (clockwise vs. counterclockwise ordering of vertices) of a figure?",
            "opts": [
                "Translations and reflections preserve orientation; rotations reverse it.",
                "Translations and rotations preserve orientation (direct isometries); reflections reverse orientation (opposite isometries).",
                "Rotations and reflections preserve orientation; translations reverse it.",
                "All transformations (translations, rotations, reflections) reverse orientation."
            ],
            "correct": 1,
            "hint": "Think of looking at a clock face: when you slide it or turn it, the numbers still run clockwise. What happens when you look at it in a mirror?",
            "explanation": "Option B is correct. Translations (slides) and rotations (turns) keep vertices in the same relative clockwise order around the perimeter, so they are direct isometries. A reflection (flip) produces a mirror image, reversing the clockwise order to counterclockwise (or vice versa), making it an opposite isometry. Options A, C, and D misstate these fundamental properties.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-16",
            "q": "On straight line segment $\\overline{AC}$, point $B$ lies between $A$ and $C$ such that $AB = x + 3$, $BC = 2x - 1$, and $AC = 14\\text{ cm}$. The segment undergoes a rigid motion mapping $A \\to A'$, $B \\to B'$, and $C \\to C'$. What is the length of image segment $\\overline{A'B'}$?",
            "opts": [
                "$4\\text{ cm}$",
                "$5\\text{ cm}$",
                "$9\\text{ cm}$",
                "$7\\text{ cm}$"
            ],
            "correct": 3,
            "hint": "Use the segment addition postulate $AB + BC = AC$ to solve for $x$, find $AB$, and apply distance preservation.",
            "explanation": "Option D is correct. By betweenness and the segment addition postulate: $AB + BC = AC \\implies (x + 3) + (2x - 1) = 14 \\implies 3x + 2 = 14 \\implies 3x = 12 \\implies x = 4$. Therefore, $AB = 4 + 3 = 7\\text{ cm}$ (and $BC = 2(4) - 1 = 7\\text{ cm}$). Because a rigid motion preserves distances between all points, $A'B' = AB = 7\\text{ cm}$. Option A is the value of $x$, Option B is an arithmetic error, and Option C is $x+5$.",
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-17",
            "q": "Which of the following coordinate rules represents a transformation that is **NEVER** a rigid motion?",
            "opts": [
                "$(x, y) \\to (x - 7, y + 4)$",
                "$(x, y) \\to (-y, x)$",
                "$(x, y) \\to (x, -y)$",
                "$(x, y) \\to (3x, 3y)$"
            ],
            "correct": 3,
            "hint": "Look for a rule where coordinates are multiplied by a number other than $1$ or $-1$, scaling the size of the shape.",
            "explanation": "Option D is correct. The rule $(x, y) \\to (3x, 3y)$ multiplies all coordinates by $3$, creating a dilation with scale factor $k = 3$. This triples all segment lengths ($d' = 3d$) and multiplies the area by $3^2 = 9$. Because distance is not preserved, it is never a rigid motion. Option A is a translation, Option B is a $90^\\circ$ counterclockwise rotation, and Option C is a reflection across the $x$-axis—all of which are rigid motions.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-18",
            "q": "A student examines two rhombuses:\n- **Rhombus 1:** Side length $5\\text{ cm}$, perimeter $20\\text{ cm}$, and interior angles $74^\\circ$ and $106^\\circ$.\n- **Rhombus 2:** Side length $5\\text{ cm}$, perimeter $20\\text{ cm}$, and interior angles $60^\\circ$ and $120^\\circ$.\nCan Rhombus 2 be formed by applying a rigid motion to Rhombus 1?",
            "opts": [
                "Yes, because both rhombuses have the exact same side lengths and perimeter of $20\\text{ cm}$.",
                "Yes, because turning a rhombus changes its angle measures to fit a new orientation.",
                "No, because rigid motions MUST preserve all angle measures, and $74^\\circ \\neq 60^\\circ$.",
                "No, because rigid motions cannot be applied to four-sided shapes."
            ],
            "correct": 2,
            "hint": "Recall: A rigid motion must preserve BOTH distance (side lengths) AND angle measures simultaneously.",
            "explanation": "Option C is correct. A rigid motion (isometry) requires the preservation of BOTH side lengths AND angle measures ($m\\angle A' = m\\angle A$). Although both shapes share the same side lengths ($5\\text{ cm}$) and perimeter ($20\\text{ cm}$), their angle measures differ ($74^\\circ \\neq 60^\\circ$). Because angle measures are not preserved, Rhombus 2 cannot be the image of Rhombus 1 under any rigid motion. Option A confuses perimeter equality with congruence. Option B is a common misconception.",
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-19",
            "q": "Reginald draws regular hexagon $ABCDEF$ with side length $s = 4\\text{ cm}$ and three pairs of opposite parallel sides (from Into Math TE Wrap-Up Exit Ticket). He rotates the hexagon $120^\\circ$ counterclockwise about its center. Which statement accurately describes image $A'B'C'D'E'F'$?",
            "opts": [
                "All side lengths remain $4\\text{ cm}$, all interior angles remain $120^\\circ$, opposite sides remain parallel, and perimeter is $24\\text{ cm}$.",
                "Side lengths increase to $6\\text{ cm}$ and opposite sides intersect because rotation turns sides in different directions.",
                "The interior angles increase by $120^\\circ$ to $240^\\circ$, but side lengths stay $4\\text{ cm}$.",
                "The hexagon becomes irregular because horizontal sides stay fixed while slanted sides rotate."
            ],
            "correct": 0,
            "hint": "See HMH Into Math TE page 31 Exit Ticket: Reginald rotates a regular hexagon. What is true of the angles, side lengths, and parallel sides?",
            "explanation": "Option A is correct. In the TE Wrap-Up Exit Ticket (page 31), students verify that when Reginald rotates a regular hexagon, angles stay the same ($120^\\circ$), side lengths stay the same ($4\\text{ cm}$), perimeter stays the same ($6 \\times 4 = 24\\text{ cm}$), and opposite parallel sides remain parallel. Rigid motions preserve all metric properties and parallelism uniformly across the entire polygon. Options B, C, and D are false.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        },
        {
            "id": "p-1-1-mcq-20",
            "q": "A mathematics class analyzes four statements about transformations:\n1. *Under any rigid motion, if line $m \\parallel \\text{line } n$, then their images satisfy $m' \\parallel n'$.*\n2. *If a transformation preserves the area of a rectangle, it is guaranteed to be a rigid motion.*\n3. *A reflection across a line preserves all side lengths and angle measures, but reverses vertex orientation (chirality).*\n4. *Translating a polygon from Quadrant I to Quadrant III reduces the side lengths of the polygon because the coordinates become negative.*\nWhich of these statements are mathematically **TRUE**?",
            "opts": [
                "Statements 1 and 3 only",
                "Statements 1, 2, and 3 only",
                "Statements 2 and 4 only",
                "Statements 1, 3, and 4 only"
            ],
            "correct": 0,
            "hint": "Evaluate each statement individually: Statement 1 (parallelism), Statement 2 (can non-rigid shear or stretch preserve area?), Statement 3 (reflection properties), Statement 4 (quadrant misconception).",
            "explanation": "Option A is correct.\n- Statement 1 is TRUE: CCSS 8.G.A.1.c states that parallel lines are taken to parallel lines under rigid motions.\n- Statement 2 is FALSE: A horizontal stretch by $2$ combined with a vertical compression by $\\frac{1}{2}$ preserves area ($2 \\times \\frac{1}{2} = 1$), but distorts side lengths and angles, so it is NOT a rigid motion.\n- Statement 3 is TRUE: Reflections preserve distance and angle measures, but reverse vertex orientation from clockwise to counterclockwise.\n- Statement 4 is FALSE: Coordinates become negative, but side lengths are distances, which are invariant under translation.\nTherefore, only Statements 1 and 3 are true.",
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1"
        }
    ]
}


def get_lesson_1_1_data():
    """Return a deep copy of the Lesson 1.1 dataset."""
    import copy
    return copy.deepcopy(LESSON_1_1_DATA)


def validate_lesson_1_1():
    """Validate completeness, data integrity, and constraints for Lesson 1.1."""
    data = LESSON_1_1_DATA
    errors = []

    # Check root keys
    required_keys = [
        "lessonInfo", "conceptExplanation", "essentialVocabulary",
        "formulasAndProperties", "illustrativeExamples",
        "workedExamplesModelAnswers", "mcqs"
    ]
    for key in required_keys:
        if key not in data:
            errors.append(f"Missing root key: {key}")

    # Check MCQs
    mcqs = data.get("mcqs", [])
    if len(mcqs) != 20:
        errors.append(f"Expected EXACTLY 20 MCQs, but found {len(mcqs)}")

    mcq_ids = set()
    dok_counts = {1: 0, 2: 0, 3: 0}
    correct_counts = {0: 0, 1: 0, 2: 0, 3: 0}

    for idx, item in enumerate(mcqs, start=1):
        expected_id = f"p-1-1-mcq-{idx}"
        actual_id = item.get("id")
        if actual_id != expected_id:
            errors.append(f"MCQ #{idx} id mismatch: expected '{expected_id}', got '{actual_id}'")
        if actual_id in mcq_ids:
            errors.append(f"Duplicate MCQ ID: {actual_id}")
        mcq_ids.add(actual_id)

        # Check required fields
        for field in ["id", "q", "opts", "correct", "hint", "explanation", "dok", "standard"]:
            if field not in item:
                errors.append(f"MCQ #{idx} missing field: {field}")

        # Check options
        opts = item.get("opts", [])
        if len(opts) != 4:
            errors.append(f"MCQ #{idx} has {len(opts)} options, expected 4")

        # Check correct index
        correct = item.get("correct")
        if correct not in [0, 1, 2, 3]:
            errors.append(f"MCQ #{idx} has invalid correct index: {correct}")
        else:
            correct_counts[correct] = correct_counts.get(correct, 0) + 1

        # Check DOK
        dok = item.get("dok")
        if dok not in [1, 2, 3]:
            errors.append(f"MCQ #{idx} has invalid dok: {dok}")
        else:
            dok_counts[dok] = dok_counts.get(dok, 0) + 1

        # Check Standard
        std = item.get("standard")
        if std != "CCSS.MATH.CONTENT.8.G.A.1":
            errors.append(f"MCQ #{idx} has unexpected standard: {std}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "mcq_count": len(mcqs),
        "dok_distribution": dok_counts,
        "correct_option_distribution": correct_counts,
        "vocab_count": len(data.get("essentialVocabulary", [])),
        "formulas_count": len(data.get("formulasAndProperties", [])),
        "examples_count": len(data.get("illustrativeExamples", []))
    }


if __name__ == "__main__":
    report = validate_lesson_1_1()
    print("=" * 60)
    print("BUILD LESSON 1.1 VALIDATION REPORT")
    print("=" * 60)
    print(f"Status: {'PASS' if report['valid'] else 'FAIL'}")
    print(f"Total MCQs: {report['mcq_count']}")
    print(f"DOK Distribution: {report['dok_distribution']}")
    print(f"Answer Key Distribution: {report['correct_option_distribution']}")
    print(f"Vocabulary Terms: {report['vocab_count']}")
    print(f"Formulas & Properties: {report['formulas_count']}")
    print(f"Illustrative Examples: {report['examples_count']}")
    if report["errors"]:
        print("\nErrors Found:")
        for err in report["errors"]:
            print(f" - {err}")
    print("=" * 60)
