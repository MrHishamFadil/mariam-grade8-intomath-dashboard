# -*- coding: utf-8 -*-
"""
build_lesson_1_3.py
Master Curriculum Content, Concept Explanations, Vocabulary, Formulas,
Illustrative Examples, and 20 HMH Into Math Aligned MCQs for Lesson 1.3:
'Explore Reflections' (Grade 8, Module 1).

Author: Antigravity (Agent 3)
Curriculum Reference: HMH Into Math Grade 8 Teacher Edition (Pages 48-59, extracted_module1_raw.json)
Standards: CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3
"""

LESSON_1_3_DATA = {
    "lessonInfo": {
        "id": "1.3",
        "lessonNumber": "1.3",
        "moduleNumber": 1,
        "moduleId": "module-1",
        "moduleTitle": "Module 1: Transformations and Congruence",
        "title": "Lesson 1.3: Explore Reflections",
        "tag": "Reflections, Coordinate Rules & Symmetry",
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
        "standards": [
            "CCSS.MATH.CONTENT.8.G.A.1",
            "CCSS.MATH.CONTENT.8.G.A.1.a",
            "CCSS.MATH.CONTENT.8.G.A.1.b",
            "CCSS.MATH.CONTENT.8.G.A.1.c",
            "CCSS.MATH.CONTENT.8.G.A.3"
        ],
        "iCanStatement": (
            "I can reflect a figure across the x-axis, y-axis, lines x = c, y = c, and diagonal lines "
            "y = x and y = -x in the coordinate plane, describe the reflections algebraically, and explain "
            "why reflections preserve distance and angle measures while reversing vertex orientation."
        ),
        "learningObjective": (
            "Explore and observe the geometric and algebraic effects of reflections on two-dimensional figures; "
            "apply mapping rules across horizontal, vertical, and diagonal lines; prove that the line of reflection "
            "is the perpendicular bisector of every segment connecting a preimage point to its image point; and "
            "investigate double reflections and reflectional line symmetry."
        ),
        "languageObjective": (
            "Explain orally and in writing how flipping a figure across a line of reflection affects its vertex "
            "coordinates, line slopes, and vertex orientation (chirality) using precise geometric vocabulary such as "
            "line of reflection, perpendicular bisector, invariant point, direct vs. opposite isometry, and line of symmetry."
        )
    },

    "conceptExplanation": {
        "overview": (
            "A reflection is a rigid transformation (isometry) that flips a geometric figure across a specific "
            "line called the line of reflection (mirror line). Like translations and rotations, reflections preserve "
            "side lengths, interior angle measures, parallelism, and area. However, reflections are unique among rigid "
            "motions because they reverse the orientation (chirality) of the figure—transforming clockwise vertex "
            "order into counterclockwise vertex order."
        ),
        "coreDefinition": (
            "A **reflection** across a line $\\ell$ is a transformation that maps every point $P$ in the plane to a "
            "point $P'$ such that:\n"
            "1. If $P$ does not lie on $\\ell$, then $\\ell$ is the perpendicular bisector of segment $\\overline{PP'}$.\n"
            "2. If $P$ lies directly on $\\ell$, then $P' = P$ (the point is invariant or fixed)."
        ),
        "keyProperties": [
            {
                "property": "1. Perpendicular Bisector Property",
                "detail": (
                    "The line of reflection $\\ell$ is perpendicular to segment $\\overline{PP'}$ and bisects $\\overline{PP'}$ "
                    "at its midpoint: $\\text{Midpoint}(P, P') \\in \\ell$ and $\\overline{PP'} \\perp \\ell$."
                )
            },
            {
                "property": "2. Equidistance from the Mirror Line",
                "detail": (
                    "Every point $P$ and its corresponding image point $P'$ lie at the exact same perpendicular distance "
                    "from the line of reflection: $d(P, \\ell) = d(P', \\ell)$."
                )
            },
            {
                "property": "3. Invariant (Fixed) Points",
                "detail": (
                    "Any point lying directly on the line of reflection is mapped to itself: $P \\in \\ell \\iff P' = P$."
                )
            },
            {
                "property": "4. Distance and Angle Preservation (Rigid Motion)",
                "detail": (
                    "Reflections preserve segment lengths ($A'B' = AB$), angle measures ($m\\angle A' = m\\angle A$), "
                    "parallelism ($L_1 \\parallel L_2 \\implies L'_1 \\parallel L'_2$), and area."
                )
            },
            {
                "property": "5. Orientation Reversal (Opposite Isometry / Chirality)",
                "detail": (
                    "Reflecting a polygon flips its vertex ordering. A clockwise sequence of vertices $A \\to B \\to C$ "
                    "becomes counterclockwise $A' \\to B' \\to C'$."
                )
            },
            {
                "property": "6. Effect of Reflection on Slope",
                "detail": (
                    "Reflecting a non-vertical, non-horizontal line segment across either coordinate axis (or any horizontal/vertical line) "
                    "negates its slope: $m' = -m$."
                )
            },
            {
                "property": "7. Composition of Two Reflections",
                "detail": (
                    "• Two reflections across parallel lines separated by distance $d$ equal a translation by $2d$ perpendicular to the lines.\n"
                    "• Two reflections across perpendicular lines (intersecting at $90^\\circ$, such as the $x$-axis followed by the $y$-axis) "
                    "equal a $180^\\circ$ rotation about the point of intersection."
                )
            }
        ],
        "coordinateRulesTable": [
            {"reflectionLine": "x-axis (y = 0)", "coordinateRule": "(x, y) \\to (x, -y)", "effect": "x remains unchanged; y changes sign"},
            {"reflectionLine": "y-axis (x = 0)", "coordinateRule": "(x, y) \\to (-x, y)", "effect": "x changes sign; y remains unchanged"},
            {"reflectionLine": "Diagonal line y = x", "coordinateRule": "(x, y) \\to (y, x)", "effect": "x and y swap positions"},
            {"reflectionLine": "Diagonal line y = -x", "coordinateRule": "(x, y) \\to (-y, -x)", "effect": "x and y swap positions and negate"},
            {"reflectionLine": "Vertical line x = c", "coordinateRule": "(x, y) \\to (2c - x, y)", "effect": "Horizontal distance to x=c is reflected"},
            {"reflectionLine": "Horizontal line y = c", "coordinateRule": "(x, y) \\to (x, 2c - y)", "effect": "Vertical distance to y=c is reflected"}
        ]
    },

    "essentialVocabulary": [
        {
            "term": "Reflection",
            "definition": "A rigid transformation that flips a figure across a line, producing a congruent mirror image with reversed orientation.",
            "example": "Flipping $\\triangle ABC$ across the $y$-axis creates congruent $\\triangle A'B'C'$."
        },
        {
            "term": "Line of Reflection",
            "definition": "The line over which a figure is reflected; it acts as the perpendicular bisector of every segment connecting a preimage point to its image point.",
            "example": "In the reflection $(x, y) \\to (x, -y)$, the line of reflection is the $x$-axis ($y = 0$)."
        },
        {
            "term": "Perpendicular Bisector",
            "definition": "A line that divides a line segment into two congruent halves at a right angle ($90^\\circ$).",
            "example": "The $y$-axis is the perpendicular bisector of the segment connecting $(-4, 3)$ and $(4, 3)$."
        },
        {
            "term": "Invariant (Fixed) Point",
            "definition": "A point that maps directly onto itself during a geometric transformation ($P = P'$).",
            "example": "Any point with coordinates $(0, y)$ remains unchanged when reflected across the $y$-axis."
        },
        {
            "term": "Orientation / Chirality",
            "definition": "The rotational order (clockwise vs. counterclockwise) in which the vertices of a polygon are read. Reflections reverse orientation.",
            "example": "Looking at the word 'AMBULANCE' in a mirror reverses the order and appearance of the letters from left to right."
        },
        {
            "term": "Line Symmetry (Reflectional Symmetry)",
            "definition": "A geometric property of a figure that can be divided into two congruent halves by a line such that each half is the reflection of the other.",
            "example": "A regular hexagon has 6 lines of reflectional symmetry."
        },
        {
            "term": "Double Reflection Theorem",
            "definition": "A theorem stating that reflecting across two parallel lines separated by distance $d$ yields a translation of $2d$, while reflecting across two perpendicular lines yields a $180^\\circ$ rotation.",
            "example": "Reflecting across $x = 1$ then $x = 4$ translates a figure $2(4 - 1) = 6$ units to the right."
        }
    ],

    "formulasAndProperties": [
        {
            "name": "Reflection across the x-axis",
            "formula": "r_{x\\text{-axis}}(x, y) = (x, -y)",
            "description": "Negates the y-coordinate while keeping the x-coordinate constant."
        },
        {
            "name": "Reflection across the y-axis",
            "formula": "r_{y\\text{-axis}}(x, y) = (-x, y)",
            "description": "Negates the x-coordinate while keeping the y-coordinate constant."
        },
        {
            "name": "Reflection across the line y = x",
            "formula": "r_{y=x}(x, y) = (y, x)",
            "description": "Swaps the x- and y-coordinates."
        },
        {
            "name": "Reflection across the line y = -x",
            "formula": "r_{y=-x}(x, y) = (-y, -x)",
            "description": "Swaps and negates both coordinates."
        },
        {
            "name": "Reflection across vertical line x = c",
            "formula": "r_{x=c}(x, y) = (2c - x, y)",
            "description": "The x-coordinate reflects across c; the y-coordinate remains unchanged."
        },
        {
            "name": "Reflection across horizontal line y = c",
            "formula": "r_{y=c}(x, y) = (x, 2c - y)",
            "description": "The y-coordinate reflects across c; the x-coordinate remains unchanged."
        },
        {
            "name": "Perpendicular Bisector Midpoint Condition",
            "formula": "M = \\left(\\frac{x + x'}{2}, \\frac{y + y'}{2}\\right) \\in \\text{Line of Reflection}",
            "description": "The midpoint of segment PP' must lie on the line of reflection."
        },
        {
            "name": "Slope Transformation under Axis Reflection",
            "formula": "m' = -m",
            "description": "The slope of a reflected non-vertical, non-horizontal segment is the negative of the original slope."
        },
        {
            "name": "Composition of Reflections across Parallel Lines",
            "formula": "r_{x = b} \\circ r_{x = a}(x, y) = (x + 2(b - a), y)",
            "description": "Produces a pure translation by twice the directed distance between the parallel lines."
        },
        {
            "name": "Composition of Reflections across Perpendicular Axes",
            "formula": "r_{y\\text{-axis}} \\circ r_{x\\text{-axis}}(x, y) = (-x, -y) = R_{(0,0), 180^\\circ}(x, y)",
            "description": "Two perpendicular reflections produce a 180° rotation about the intersection point."
        }
    ],

    "illustrativeExamples": [
        {
            "id": "ex-1.3-1",
            "title": "Example 1: Reflecting an L-Shaped Polygon Across Coordinate Axes (HMH Into Math TE p. 52)",
            "description": (
                "An L-shaped figure with key points $A(3, 2)$, $B(3, 8)$, $C(3, 12)$, $D(9, 12)$, and $E(9, 8)$ "
                "is reflected across the $x$-axis to produce $A'B'C'D'E'$, and across the $y$-axis to produce $A''B''C''D''E''$."
            ),
            "stepByStepExplanation": [
                "Step 1: Apply reflection across x-axis rule $(x, y) \\to (x, -y)$: The x-coordinates stay the same, while y-coordinates are negated: "
                "$A'(3, -2)$, $B'(3, -8)$, $C'(3, -12)$, $D'(9, -12)$, and $E'(9, -8)$.",
                "Step 2: Verify distance preservation: Segment $AC$ has length $|12 - 2| = 10\\text{ units}$. Segment $A'C'$ has length $|-12 - (-2)| = 10\\text{ units}$. Segment length is invariant.",
                "Step 3: Analyze orientation across x-axis: The original upright figure is turned upside down. Tracing vertices around the figure reverses from clockwise to counterclockwise.",
                "Step 4: Apply reflection across y-axis rule $(x, y) \\to (-x, y)$: $A''(-3, 2)$, $B''(-3, 8)$, $C''(-3, 12)$, $D''(-9, 12)$, and $E''(-9, 8)$.",
                "Step 5: Analyze orientation across y-axis: The figure faces left instead of right. Both reflections preserve all side lengths and right angles, confirming they are rigid motions."
            ],
            "keyTakeaway": "Reflecting across axes preserves segment lengths and angle measures, but flips the direction the figure faces and inverts vertex orientation."
        },
        {
            "id": "ex-1.3-2",
            "title": "Example 2: Determining the Line of Reflection and Testing Perpendicular Bisector Property (HMH Into Math TE p. 54)",
            "description": (
                "A triangle has preimage vertex $P(-4, 3)$ and image vertex $P'(2, 3)$ after a single reflection. "
                "Identify the line of reflection, write its equation, and verify the perpendicular bisector property."
            ),
            "stepByStepExplanation": [
                "Step 1: Examine segment $\\overline{PP'}$: The endpoints are $(-4, 3)$ and $(2, 3)$. Since the y-coordinates are equal, $\\overline{PP'}$ is a horizontal segment lying along the line $y = 3$.",
                "Step 2: Find the midpoint of $\\overline{PP'}$: $M = \\left(\\frac{-4 + 2}{2}, \\frac{3 + 3}{2}\\right) = \\left(\\frac{-2}{2}, 3\\right) = (-1, 3)$.",
                "Step 3: Determine the line perpendicular to $\\overline{PP'}$: A line perpendicular to a horizontal segment must be vertical. Since it passes through midpoint $(-1, 3)$, its equation is $x = -1$.",
                "Step 4: Verify equidistance: The distance from $P(-4, 3)$ to $x = -1$ is $|-1 - (-4)| = 3\\text{ units}$. The distance from $P'(2, 3)$ to $x = -1$ is $|2 - (-1)| = 3\\text{ units}$. Both points are 3 units from the mirror line.",
                "Step 5: Conclude: The line of reflection is $x = -1$, and it serves as the perpendicular bisector of segment $\\overline{PP'}$."
            ],
            "keyTakeaway": "The line of reflection is uniquely determined as the perpendicular bisector of any segment connecting a preimage point to its image point."
        }
    ],

    "mcqs": [
        {
            "id": "p-1-3-mcq-1",
            "q": "Point $A(-4, 7)$ is reflected across the $x$-axis. What are the coordinates of the image point $A'$?",
            "opts": [
                "$(-4, -7)$",
                "$(4, 7)$",
                "$(4, -7)$",
                "$(7, -4)$"
            ],
            "correct": 0,
            "hint": "Reflecting across the $x$-axis preserves the horizontal position ($x$) and inverts the vertical position ($y$): $(x, y) \\to (x, -y)$.",
            "explanation": (
                "Option A is correct. The coordinate rule for reflection across the $x$-axis is $(x, y) \\to (x, -y)$. "
                "The $x$-coordinate remains $-4$, while the $y$-coordinate is negated from $7$ to $-7$, giving $A'(-4, -7)$. "
                "Option B $(4, 7)$ negates the $x$-coordinate instead (reflection across the $y$-axis). "
                "Option C $(4, -7)$ negates both coordinates (equivalent to a $180^\\circ$ rotation about the origin). "
                "Option D $(7, -4)$ swaps the coordinates (reflection across the diagonal line $y = x$)."
            ),
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-2",
            "q": "Triangle $\\triangle JKL$ with vertex $K(5, -8)$ is reflected across the $y$-axis to produce $\\triangle J'K'L'$. Which coordinate pair represents the location of $K'$?",
            "opts": [
                "$(5, 8)$",
                "$(-5, -8)$",
                "$(-5, 8)$",
                "$(-8, 5)$"
            ],
            "correct": 1,
            "hint": "Reflecting across the $y$-axis keeps the vertical height ($y$) identical and reflects the horizontal position ($x$): $(x, y) \\to (-x, y)$.",
            "explanation": (
                "Option B is correct. Under a reflection across the $y$-axis, the algebraic mapping rule is $(x, y) \\to (-x, y)$. "
                "The $x$-coordinate $5$ becomes $-5$, while the $y$-coordinate remains $-8$. Therefore, $K'(-5, -8)$. "
                "Option A $(5, 8)$ reflects across the $x$-axis by negating $y$. "
                "Option C $(-5, 8)$ negates both coordinates, which is a $180^\\circ$ rotation. "
                "Option D $(-8, 5)$ incorrectly interchanges the $x$- and $y$-coordinates."
            ),
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-3",
            "q": "A polygon vertex located at $P(-3, 8)$ is reflected across the diagonal line $y = x$. What are the coordinates of the reflected image $P'$?",
            "opts": [
                "$(3, -8)$",
                "$(-8, 3)$",
                "$(8, -3)$",
                "$(-3, -8)$"
            ],
            "correct": 2,
            "hint": "On the line $y = x$, every point has equal coordinates. Reflecting across this line simply interchanges the roles of $x$ and $y$: $(x, y) \\to (y, x)$.",
            "explanation": (
                "Option C is correct. The algebraic mapping rule for reflection across the line $y = x$ is $(x, y) \\to (y, x)$. "
                "The coordinates swap positions without altering their signs: the new $x$-value is the old $y$-value ($8$), "
                "and the new $y$-value is the old $x$-value ($-3$). Thus, $P' = (8, -3)$. "
                "Option A $(3, -8)$ negates both coordinates without swapping. "
                "Option B $(-8, 3)$ swaps and negates both coordinates, which is the rule for reflecting across $y = -x$. "
                "Option D $(-3, -8)$ reflects across the $x$-axis."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-4",
            "q": "Line segment $\\overline{CD}$ has endpoint $D(4, -6)$. If $\\overline{CD}$ is reflected across the diagonal line $y = -x$, which coordinates identify $D'$?",
            "opts": [
                "$(-6, 4)$",
                "$(-4, 6)$",
                "$(4, 6)$",
                "$(6, -4)$"
            ],
            "correct": 3,
            "hint": "Reflecting across the line $y = -x$ requires both swapping the coordinates and changing their signs: $(x, y) \\to (-y, -x)$.",
            "explanation": (
                "Option D is correct. The coordinate rule for a reflection across the line $y = -x$ is $(x, y) \\to (-y, -x)$. "
                "Starting with $D(4, -6)$: the new $x$-coordinate is $-y = -(-6) = 6$, and the new $y$-coordinate is $-x = -(4) = -4$. "
                "Hence, $D' = (6, -4)$. "
                "Option A $(-6, 4)$ swapped coordinates without changing signs (reflection across $y = x$). "
                "Option B $(-4, 6)$ negated both coordinates without swapping (a $180^\\circ$ rotation). "
                "Option C $(4, 6)$ negated only the $y$-coordinate (reflection across the $x$-axis)."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-5",
            "q": "Point $M(1, 5)$ is reflected across the vertical line $x = 4$. What are the coordinates of the reflected image $M'$?",
            "opts": [
                "$(7, 5)$",
                "$(-2, 5)$",
                "$(4, 5)$",
                "$(7, -5)$"
            ],
            "correct": 0,
            "hint": "The line $x = 4$ is vertical, so the $y$-coordinate does not change. Find how far $1$ is from $4$, and move that same distance to the other side of $4$.",
            "explanation": (
                "Option A is correct. In a reflection across a vertical line $x = c$, the $y$-coordinate remains invariant ($y' = 5$). "
                "The horizontal distance from $M(1, 5)$ to $x = 4$ is $4 - 1 = 3$ units to the left. The reflected image $M'$ must be "
                "$3$ units to the right of $x = 4$: $x' = 4 + 3 = 7$. Alternatively, using the algebraic formula: $x' = 2c - x = 2(4) - 1 = 7$. "
                "Thus, $M' = (7, 5)$. "
                "Option B $(-2, 5)$ incorrectly subtracted $3$ from $1$ instead of adding to $4$. "
                "Option C $(4, 5)$ is the midpoint on the line of reflection itself. "
                "Option D $(7, -5)$ incorrectly negated the $y$-coordinate."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-6",
            "q": "Vertex $V(-3, -2)$ is reflected across the horizontal line $y = 3$. What are the coordinates of the reflected image $V'$?",
            "opts": [
                "$(-3, 5)$",
                "$(-3, 1)$",
                "$(3, -2)$",
                "$(-3, 8)$"
            ],
            "correct": 3,
            "hint": "A reflection across a horizontal line keeps the $x$-coordinate constant. Calculate the vertical distance from $-2$ to $3$, then add that distance above $y = 3$.",
            "explanation": (
                "Option D is correct. Across the horizontal line $y = c$, the $x$-coordinate is unaffected ($x' = -3$). "
                "The vertical distance from $V(-3, -2)$ to the mirror line $y = 3$ is $3 - (-2) = 5$ units. "
                "The image $V'$ must lie $5$ units above the mirror line: $y' = 3 + 5 = 8$. "
                "Using the formula: $y' = 2c - y = 2(3) - (-2) = 6 + 2 = 8$. Thus, $V' = (-3, 8)$. "
                "Option A $(-3, 5)$ merely added the distance $5$ to $0$ or forgot to double the offset. "
                "Option B $(-3, 1)$ added $3$ to $-2$ instead of reflecting across $y = 3$. "
                "Option C $(3, -2)$ reflected horizontally across the $y$-axis."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-7",
            "q": "Point $P(2, 6)$ is reflected across line $\\ell$ to produce $P'(8, 6)$. Which mathematical statement accurately describes line $\\ell$ and its geometric relationship to segment $\\overline{PP'}$?",
            "opts": [
                "Line $\\ell$ has equation $y = 6$ and is parallel to segment $\\overline{PP'}$.",
                "Line $\\ell$ has equation $x = 5$ and is the perpendicular bisector of segment $\\overline{PP'}$.",
                "Line $\\ell$ has equation $x = 6$ and intersects $\\overline{PP'}$ at a $45^\\circ$ angle.",
                "Line $\\ell$ has equation $y = 5$ and bisects $\\overline{PP'}$ obliquely."
            ],
            "correct": 1,
            "hint": "Recall the fundamental geometric definition: The line of reflection is always the perpendicular bisector of every segment connecting a preimage point to its image point.",
            "explanation": (
                "Option B is correct. Segment $\\overline{PP'}$ connects $(2, 6)$ and $(8, 6)$, which is a horizontal segment on the line $y = 6$ "
                "of length $|8 - 2| = 6$ units. The midpoint of $\\overline{PP'}$ is $\\left(\\frac{2+8}{2}, \\frac{6+6}{2}\\right) = (5, 6)$. "
                "The line of reflection must pass through this midpoint and be perpendicular to the horizontal segment. "
                "A line perpendicular to a horizontal line is vertical, giving the equation $x = 5$. "
                "Option A ($y = 6$) is the line containing the segment itself, not its perpendicular bisector. "
                "Option C ($x = 6$) does not pass through the midpoint. "
                "Option D ($y = 5$) is horizontal and cannot be perpendicular to another horizontal segment."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-8",
            "q": "Triangle $\\triangle ABC$ has vertices listed in clockwise order: $A(1, 2)$, $B(4, 2)$, and $C(1, 6)$. After reflecting $\\triangle ABC$ across the $y$-axis to form $\\triangle A'B'C'$, which statement regarding the congruence and vertex orientation of $\\triangle A'B'C'$ is true?",
            "opts": [
                "$\\triangle A'B'C' \\cong \\triangle ABC$, and its vertices $A' \\to B' \\to C'$ remain in clockwise order.",
                "$\\triangle A'B'C'$ is not congruent to $\\triangle ABC$ because reflections distort vertex order.",
                "$\\triangle A'B'C' \\cong \\triangle ABC$, but its vertices $A' \\to B' \\to C'$ are now ordered counterclockwise (orientation is reversed).",
                "The vertex orientation is unchanged because all rigid motions preserve clockwise order."
            ],
            "correct": 2,
            "hint": "Reflections are rigid motions (isometries) that preserve side lengths and angles, but they flip the plane like looking into a mirror, reversing chirality.",
            "explanation": (
                "Option C is correct. Because reflection is a rigid motion (isometry), side lengths and angle measures are strictly preserved, "
                "guaranteeing that $\\triangle A'B'C' \\cong \\triangle ABC$. However, reflections are opposite isometries (chirality-reversing): "
                "tracing $A(1,2) \\to B(4,2) \\to C(1,6)$ runs clockwise, but tracing their reflections $A'(-1,2) \\to B'(-4,2) \\to C'(-1,6)$ "
                "runs counterclockwise. "
                "Option A falsely asserts that orientation is preserved (translations and rotations preserve orientation, but reflections do not). "
                "Option B is false because orientation reversal does not alter congruence. "
                "Option D is incorrect because rigid motions include opposite isometries."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-9",
            "q": "A quadrilateral has vertices $Q(0, 4)$, $R(3, 0)$, $S(-2, 5)$, and $T(0, -6)$. If the quadrilateral is reflected across the $y$-axis, which vertex or vertices remain strictly fixed at their original coordinates ($P = P'$)?",
            "opts": [
                "Only $R(3, 0)$",
                "Only $S(-2, 5)$",
                "None of the vertices, because transformations always move every point",
                "Both $Q(0, 4)$ and $T(0, -6)$"
            ],
            "correct": 3,
            "hint": "Which points lie directly ON the line of reflection? Points on the line of reflection never move ($P = P'$).",
            "explanation": (
                "Option D is correct. The line of reflection is the $y$-axis, whose equation is $x = 0$. "
                "Any point lying directly on the line of reflection is an invariant (fixed) point: $(0, y) \\to (-0, y) = (0, y)$. "
                "Both $Q(0, 4)$ and $T(0, -6)$ have an $x$-coordinate of $0$, so $Q' = Q(0, 4)$ and $T' = T(0, -6)$. "
                "Option A $R(3, 0)$ lies on the $x$-axis, not the $y$-axis; its image is $R'(-3, 0) \\neq R$. "
                "Option B $S(-2, 5)$ has $x = -2$, so its image is $S'(2, 5)$. "
                "Option C is a common misconception; points on the reflection axis are always fixed."
            ),
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-10",
            "q": "A geometric figure is reflected across the line $y = x$. Which of the following points will map directly onto itself ($P = P'$)?",
            "opts": [
                "$(4, -4)$",
                "$(-7, -7)$",
                "$(0, 5)$",
                "$(3, -3)$"
            ],
            "correct": 1,
            "hint": "A point remains fixed under reflection if and only if it lies directly on the mirror line. Test which point satisfies $y = x$.",
            "explanation": (
                "Option B is correct. A point $(x, y)$ is invariant under reflection across $y = x$ if and only if it satisfies the equation of the line, "
                "meaning $x = y$. For point $(-7, -7)$, both coordinates are equal to $-7$. Applying the reflection rule $(x, y) \\to (y, x)$ "
                "gives $(-7, -7) \\to (-7, -7)$, so $P = P'$. "
                "Options A $(4, -4)$ and D $(3, -3)$ lie on the line $y = -x$, so reflecting across $y = x$ swaps them to $(-4, 4)$ and $(-3, 3)$. "
                "Option C $(0, 5)$ maps to $(5, 0) \\neq (0, 5)$."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-11",
            "q": "Segment $\\overline{AB}$ connects $A(1, 2)$ and $B(4, 8)$, giving it a slope of $m = \\frac{8 - 2}{4 - 1} = 2$. If $\\overline{AB}$ is reflected across the $x$-axis to produce segment $\\overline{A'B'}$, what is the slope of $\\overline{A'B'}$?",
            "opts": [
                "$2$",
                "$\\frac{1}{2}$",
                "$-2$",
                "$-\\frac{1}{2}$"
            ],
            "correct": 2,
            "hint": "Calculate the image coordinates $A'$ and $B'$ using $(x, y) \\to (x, -y)$, then compute the slope $m' = \\frac{y'_2 - y'_1}{x'_2 - x'_1}$.",
            "explanation": (
                "Option C is correct. Reflecting across the $x$-axis maps $A(1, 2) \\to A'(1, -2)$ and $B(4, 8) \\to B'(4, -8)$. "
                "The slope of $\\overline{A'B'}$ is $m' = \\frac{-8 - (-2)}{4 - 1} = \\frac{-6}{3} = -2$. "
                "In general, reflecting across any horizontal or vertical line negates the slope of a line segment: $m' = -m = -(2) = -2$. "
                "Option A ($2$) incorrectly assumes slope is invariant under reflection (slope is preserved under translations, not axis reflections). "
                "Option B ($\\frac{1}{2}$) took the reciprocal. "
                "Option D ($-\\frac{1}{2}$) took the negative reciprocal (perpendicular slope)."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-12",
            "q": "Line segment $\\overline{GH}$ has a slope of $-\\frac{3}{5}$. If $\\overline{GH}$ is reflected across the $y$-axis, what will be the slope of the reflected image $\\overline{G'H'}$?",
            "opts": [
                "$\\frac{3}{5}$",
                "$-\\frac{3}{5}$",
                "$\\frac{5}{3}$",
                "$-\\frac{5}{3}$"
            ],
            "correct": 0,
            "hint": "Reflecting across the $y$-axis negates the run ($\Delta x$), which changes the sign of the slope: $m' = \\frac{\\Delta y}{-\\Delta x} = -m$.",
            "explanation": (
                "Option A is correct. Under a reflection across the $y$-axis, the transformation is $(x, y) \\to (-x, y)$. "
                "For any two points with horizontal change $\Delta x = x_2 - x_1$ and vertical change $\Delta y = y_2 - y_1$, "
                "the reflected points have horizontal change $-\Delta x$ and vertical change $\Delta y$. "
                "Thus, the new slope is $m' = \\frac{\\Delta y}{-\\Delta x} = -m$. "
                "Given $m = -\\frac{3}{5}$, the reflected slope is $m' = -\\left(-\\frac{3}{5}\\right) = \\frac{3}{5}$. "
                "Option B ($-\\frac{3}{5}$) fails to negate the slope. "
                "Options C and D invert the ratio of vertical to horizontal change."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-13",
            "q": "A figure is reflected across the vertical line $x = 2$, and its image is immediately reflected across the parallel vertical line $x = 7$. What single transformation is equivalent to this composition of two reflections?",
            "opts": [
                "A translation $5\\text{ units}$ to the right",
                "A translation $10\\text{ units}$ to the right",
                "A rotation of $180^\\circ$ about the point $(4.5, 0)$",
                "A translation $10\\text{ units}$ to the left"
            ],
            "correct": 1,
            "hint": "According to the Double Reflection Theorem, reflecting across two parallel lines separated by distance $d$ produces a translation of $2d$ in the direction from the first line to the second.",
            "explanation": (
                "Option B is correct. By the Double Reflection Theorem across parallel lines, the composition of reflections across two parallel lines "
                "separated by distance $d$ is equivalent to a translation by $2d$ perpendicular to the lines. "
                "The lines $x = 2$ and $x = 7$ are parallel vertical lines separated by $d = 7 - 2 = 5$ units directed to the right. "
                "The composite motion is therefore a translation to the right by $2d = 2(5) = 10$ units: $(x, y) \\to (x + 10, y)$. "
                "For verification, test $x = 0$: reflect across $x = 2 \\implies 2(2) - 0 = 4$; reflect $4$ across $x = 7 \\implies 2(7) - 4 = 10$. Net change: $+10$. "
                "Option A forgets to multiply the distance by $2$. "
                "Option C confuses parallel reflection lines with intersecting reflection lines. "
                "Option D translates in the opposite direction."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-14",
            "q": "Figure $F$ is reflected across the horizontal line $y = -1$, and the resulting image is then reflected across the horizontal line $y = -5$. Which algebraic mapping rule describes this composite transformation?",
            "opts": [
                "$(x, y) \\to (x, y - 8)$",
                "$(x, y) \\to (x, y + 8)$",
                "$(x, y) \\to (x, y - 4)$",
                "$(x, y) \\to (-x, -y - 6)$"
            ],
            "correct": 0,
            "hint": "The lines are horizontal and parallel. The motion goes from $y = -1$ down to $y = -5$ (a downward shift). What is $2 \\times$ the distance between them?",
            "explanation": (
                "Option A is correct. Let us algebraically compose the two reflections: "
                "1. First reflection across $y = -1$: $y_1 = 2(-1) - y = -2 - y$. "
                "2. Second reflection across $y = -5$: $y_2 = 2(-5) - y_1 = -10 - (-2 - y) = -10 + 2 + y = y - 8$. "
                "The $x$-coordinate is unaffected because both lines are horizontal. "
                "Thus, the composition is the pure translation $(x, y) \\to (x, y - 8)$. "
                "This matches the theorem: the directed distance from $y = -1$ to $y = -5$ is $-4$, and doubling it gives a shift of $2(-4) = -8$. "
                "Option B $(x, y) \\to (x, y + 8)$ shifts upward instead of downward. "
                "Option C $(x, y) \\to (x, y - 4)$ forgot to double the distance. "
                "Option D confuses the translation with a point reflection."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-15",
            "q": "Triangle $\\triangle RST$ is reflected across the $x$-axis, and its image is then reflected across the $y$-axis. Which single transformation achieves the exact same image from the original $\\triangle RST$?",
            "opts": [
                "A translation $2\\text{ units}$ along the vector $\\langle -1, -1 \\rangle$",
                "A reflection across the diagonal line $y = -x$",
                "A rotation of $180^\\circ$ about the origin $(0, 0)$",
                "A reflection across the diagonal line $y = x$"
            ],
            "correct": 2,
            "hint": "Trace what happens to coordinates: first $(x, y) \\to (x, -y)$, then apply the second reflection. Which single transformation rule is $(-x, -y)$?",
            "explanation": (
                "Option C is correct. Track an arbitrary point $(x, y)$ under the two transformations: "
                "First, reflection across the $x$-axis maps $(x, y) \\to (x, -y)$. "
                "Next, reflection across the $y$-axis maps $(x, -y) \\to (-x, -y)$. "
                "The algebraic rule $(x, y) \\to (-x, -y)$ is precisely the rule for a $180^\\circ$ rotation (clockwise or counterclockwise) about the origin $(0, 0)$. "
                "Geometrically, when two reflection lines intersect at an angle $\\theta = 90^\\circ$, their composition is a rotation about their intersection point by $2\\theta = 2(90^\\circ) = 180^\\circ$. "
                "Option A is a translation. "
                "Option B is a reflection across $y = -x$, which has rule $(x, y) \\to (-y, -x)$. "
                "Option D is a reflection across $y = x$, which has rule $(x, y) \\to (y, x)$."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-16",
            "q": "A polygon has clockwise vertex ordering. It is reflected across the vertical line $x = 3$, and that image is subsequently reflected across the perpendicular horizontal line $y = -2$. What is the vertex orientation of the final image, and what geometric motion describes this combined transformation?",
            "opts": [
                "Counterclockwise; the transformation is equivalent to a single reflection across $y = -x + 1$.",
                "Counterclockwise; each reflection preserves orientation so the net result is unchanged.",
                "Clockwise; reflecting twice across perpendicular lines preserves orientation and is equivalent to a $180^\\circ$ rotation about $(3, -2)$.",
                "Undefined; intersecting reflections destroy polygon vertex ordering."
            ],
            "correct": 2,
            "hint": "A single reflection reverses orientation (clockwise $\\to$ counterclockwise). What does a second reflection do? Remember: two perpendicular reflections form a $180^\\circ$ rotation.",
            "explanation": (
                "Option C is correct. A single reflection is an opposite isometry, reversing orientation from clockwise to counterclockwise. "
                "A second reflection reverses orientation once again: counterclockwise $\\to$ clockwise. "
                "Because the two lines $x = 3$ and $y = -2$ are perpendicular (intersecting at $(3, -2)$ at $90^\\circ$), "
                "their composition is a $180^\\circ$ rotation about $(3, -2)$. Rotations are direct isometries that preserve clockwise orientation. "
                "Option A claims the composition of two reflections is a single reflection (two reflections can never equal an odd number of reflections). "
                "Option B falsely claims that individual reflections preserve orientation. "
                "Option D is mathematically meaningless because rigid motions always preserve geometric structure."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-17",
            "q": "Preimage point $W(-5, 3)$ is mapped to image point $W'(7, 3)$ by a single reflection. What is the equation of the line of reflection?",
            "opts": [
                "$x = 1$",
                "$y = 3$",
                "$x = 2$",
                "$y = 1$"
            ],
            "correct": 0,
            "hint": "The points share the same $y$-coordinate ($3$), so $\\overline{WW'}$ is horizontal. The line of reflection must be vertical ($x = c$) and pass through the midpoint of $\\overline{WW'}$.",
            "explanation": (
                "Option A is correct. Points $W(-5, 3)$ and $W'(7, 3)$ have identical $y$-coordinates, meaning segment $\\overline{WW'}$ is horizontal. "
                "The line of reflection is the perpendicular bisector of $\\overline{WW'}$. "
                "A line perpendicular to a horizontal line is a vertical line of the form $x = c$. "
                "The line must pass through the midpoint $x$-coordinate: $c = \\frac{-5 + 7}{2} = \\frac{2}{2} = 1$. "
                "Therefore, the line of reflection is $x = 1$. "
                "Option B ($y = 3$) is the horizontal line on which the points lie, not the perpendicular bisector. "
                "Option C ($x = 2$) results from an arithmetic error in calculating the average. "
                "Option D ($y = 1$) is a horizontal line."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-18",
            "q": "During a geometry lab, a student discovers that preimage vertex $E(2, -5)$ maps to image vertex $E'(-5, 2)$ after a single reflection. Across which line was the point reflected?",
            "opts": [
                "The $x$-axis ($y = 0$)",
                "The line $y = -x$",
                "The $y$-axis ($x = 0$)",
                "The line $y = x$"
            ],
            "correct": 3,
            "hint": "Compare the coordinates: $x = 2$ became $y' = 2$, and $y = -5$ became $x' = -5$. The coordinates swapped places without sign changes: $(x, y) \\to (y, x)$.",
            "explanation": (
                "Option D is correct. Comparing preimage $E(2, -5)$ and image $E'(-5, 2)$, the $x$- and $y$-coordinates have swapped values: $(x, y) \\to (y, x)$. "
                "This is the defining coordinate rule for reflection across the diagonal line $y = x$. "
                "We can also verify using the perpendicular bisector property: "
                "The midpoint is $\\left(\\frac{2 + (-5)}{2}, \\frac{-5 + 2}{2}\\right) = (-1.5, -1.5)$, which lies directly on $y = x$. "
                "The slope of $\\overline{EE'}$ is $\\frac{2 - (-5)}{-5 - 2} = \\frac{7}{-7} = -1$, which is perpendicular to the slope of $y = x$ ($+1$). "
                "Option A reflects $(2, -5)$ to $(2, 5)$. "
                "Option B ($y = -x$) reflects $(2, -5)$ to $(5, -2)$ by swapping and negating. "
                "Option C reflects $(2, -5)$ to $(-2, -5)$."
            ),
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-19",
            "q": "A regular octagon is centered at the origin on the coordinate plane. How many distinct lines of reflectional symmetry does this regular octagon possess?",
            "opts": [
                "$4$",
                "$8$",
                "$16$",
                "Infinitely many"
            ],
            "correct": 1,
            "hint": "In any regular polygon with $n$ sides, how many lines of symmetry connect opposite vertices or midpoints of opposite sides?",
            "explanation": (
                "Option B is correct. Any regular polygon with $n$ sides has exactly $n$ lines of reflectional symmetry. "
                "For a regular octagon ($n = 8$): "
                "• $4$ lines of symmetry pass through pairs of opposite vertices.\n"
                "• $4$ lines of symmetry pass through the midpoints of opposite sides.\n"
                "This gives a total of $4 + 4 = 8$ distinct lines of reflectional symmetry. "
                "Option A ($4$) counts only the vertex lines or only the side-bisector lines. "
                "Option C ($16$) double-counts the axes or confuses lines of symmetry with total symmetries (dihedral group order $D_8$). "
                "Option D applies only to a circle."
            ),
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-3-mcq-20",
            "q": "An isosceles trapezoid is positioned in the coordinate plane with vertices $A(-4, 1)$, $B(4, 1)$, $C(2, 5)$, and $D(-2, 5)$. Which equation represents the line of reflectional symmetry that maps this trapezoid onto itself?",
            "opts": [
                "$y = 0$ (the $x$-axis)",
                "$y = 3$",
                "$y = x$",
                "$x = 0$ (the $y$-axis)"
            ],
            "correct": 3,
            "hint": "A line of symmetry must reflect every vertex of the trapezoid onto another vertex of the same trapezoid. Test which axis reflects $A(-4, 1)$ to $B(4, 1)$ and $D(-2, 5)$ to $C(2, 5)$.",
            "explanation": (
                "Option D is correct. Reflecting across the line $x = 0$ (the $y$-axis) applies the rule $(x, y) \\to (-x, y)$: "
                "• $A(-4, 1) \\to (4, 1) = B$\n"
                "• $B(4, 1) \\to (-4, 1) = A$\n"
                "• $C(2, 5) \\to (-2, 5) = D$\n"
                "• $D(-2, 5) \\to (2, 5) = C$\n"
                "Every vertex maps directly onto a corresponding vertex of the figure, meaning the $y$-axis ($x = 0$) is the line of symmetry. "
                "Option A ($y = 0$) flips the trapezoid below the $x$-axis ($y < 0$), completely outside its original region. "
                "Option B ($y = 3$) is a horizontal midline; reflecting over it would swap base $AB$ (length $8$) with base $CD$ (length $4$), distorting the figure. "
                "Option C ($y = x$) tilts the figure obliquely."
            ),
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        }
    ]
}

# Alias for direct import of MCQs
LESSON_1_3_MCQS = LESSON_1_3_DATA["mcqs"]


def validate_lesson_1_3(data=None):
    """
    Validates that Lesson 1.3 data satisfies all architectural,
    pedagogical, and schema requirements.
    """
    if data is None:
        data = LESSON_1_3_DATA

    errors = []
    mcqs = data.get("mcqs", [])

    if len(mcqs) != 20:
        errors.append(f"Expected exactly 20 MCQs, found {len(mcqs)}")

    required_fields = ["id", "q", "opts", "correct", "hint", "explanation", "dok", "standard"]
    dok_counts = {1: 0, 2: 0, 3: 0}
    correct_counts = {0: 0, 1: 0, 2: 0, 3: 0}

    for idx, item in enumerate(mcqs, 1):
        expected_id = f"p-1-3-mcq-{idx}"
        if item.get("id") != expected_id:
            errors.append(f"MCQ #{idx} has id '{item.get('id')}', expected '{expected_id}'")

        for field in required_fields:
            if field not in item:
                errors.append(f"MCQ #{idx} missing field: {field}")

        opts = item.get("opts", [])
        if len(opts) != 4:
            errors.append(f"MCQ #{idx} has {len(opts)} options, expected 4")

        correct = item.get("correct")
        if correct not in [0, 1, 2, 3]:
            errors.append(f"MCQ #{idx} has invalid correct index: {correct}")
        else:
            correct_counts[correct] = correct_counts.get(correct, 0) + 1

        dok = item.get("dok")
        if dok not in [1, 2, 3]:
            errors.append(f"MCQ #{idx} has invalid dok: {dok}")
        else:
            dok_counts[dok] = dok_counts.get(dok, 0) + 1

        std = item.get("standard")
        if std != "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3":
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
    report = validate_lesson_1_3()
    print("=" * 60)
    print("BUILD LESSON 1.3 VALIDATION REPORT")
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
