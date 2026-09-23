# -*- coding: utf-8 -*-
"""
build_lesson_1_4.py
===================
Lesson 1.4: Explore Rotations
Extracted and generated from HMH Into Math Grade 8 Teacher Edition (Pages 60-71 in extracted_module1_raw.json).

Covers:
1. Definition of rotation: center of rotation, angle of rotation, and direction (clockwise vs counterclockwise; positive = CCW).
2. 90° counterclockwise rotation about origin: (x, y) → (-y, x).
3. 180° rotation about origin: (x, y) → (-x, -y).
4. 270° counterclockwise rotation (or 90° clockwise) about origin: (x, y) → (y, -x).
5. 270° clockwise rotation (equivalent to 90° counterclockwise): (x, y) → (-y, x).
6. 360° rotation: (x, y) → (x, y) (full turn).
7. Center of rotation is a fixed point: (0,0) → (0,0) or vertex P → P.
8. Preservation of distance, angle measures, parallelism, and vertex orientation (clockwise stays clockwise).
9. Effect on slope: 90° rotation makes lines perpendicular (slopes are negative reciprocals m' = -1/m); 180° rotation preserves slope (m' = m).
10. Rotational symmetry: minimum angle of rotation mapping a regular polygon onto itself (360° / n).
11. Finding the angle and direction of rotation given preimage and image coordinates.
12. Common errors: confusing clockwise and counterclockwise, forgetting to swap coordinates for 90°/270°, sign errors.
"""

LESSON_1_4_DATA = {
    "id": "1.4",
    "lessonNumber": "1.4",
    "title": "Lesson 1.4: Explore Rotations",
    "module": 1,
    "moduleTitle": "Transformations and Congruence",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
    "canDo": "I can identify and perform rotations, and describe a rotation on a coordinate plane algebraically.",
    "sourcePages": "HMH Into Math Grade 8 Teacher Edition, Pages 60-71",
    "topicsCovered": [
        "Definition of rotation: center of rotation, angle of rotation, and direction (clockwise vs counterclockwise; positive = CCW)",
        "90° counterclockwise rotation about origin: (x, y) → (-y, x)",
        "180° rotation about origin: (x, y) → (-x, -y)",
        "270° counterclockwise rotation (or 90° clockwise) about origin: (x, y) → (y, -x)",
        "270° clockwise rotation (equivalent to 90° counterclockwise): (x, y) → (-y, x)",
        "360° rotation: (x, y) → (x, y) (full turn)",
        "Center of rotation is a fixed point: (0,0) → (0,0) or vertex P → P",
        "Preservation of distance, angle measures, parallelism, and vertex orientation (clockwise stays clockwise)",
        "Effect on slope: 90° rotation makes lines perpendicular (m' = -1/m); 180° rotation preserves slope (m' = m)",
        "Rotational symmetry: minimum angle of rotation mapping a regular polygon onto itself (360° / n)",
        "Finding the angle and direction of rotation given preimage and image coordinates",
        "Common errors: confusing clockwise and counterclockwise, forgetting to swap coordinates for 90°/270°, sign errors"
    ],
    "mcqs": [
        {
            "id": "p-1-4-mcq-1",
            "q": "In transformational geometry, a rotation by an angle $\\theta > 0^\\circ$ is defined by a center of rotation, an angle of rotation, and a direction. According to standard mathematical convention, which direction corresponds to a positive angle of rotation (such as $+90^\\circ$) on the coordinate plane?",
            "opts": [
                "Clockwise",
                "Counterclockwise",
                "In the positive $x$-direction (to the right)",
                "In the positive $y$-direction (upward)"
            ],
            "correct": 1,
            "hint": "Think about how angles are measured in standard position on the coordinate plane starting from the positive $x$-axis.",
            "explanation": "In standard mathematics and geometry, a positive angle of rotation turns in the counterclockwise direction (for example, $+90^\\circ$ indicates a $90^\\circ$ counterclockwise turn). A clockwise rotation corresponds to a negative angle. Choices C and D describe translations (linear shifts along axes), not rotational directions.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-2",
            "q": "Triangle $ABC$ is rotated $90^\\circ$ counterclockwise about the origin $(0, 0)$. What happens to the coordinates of the origin itself during this transformation?",
            "opts": [
                "The origin shifts to $(0, 1)$ because of the $90^\\circ$ counterclockwise turn.",
                "The origin is undefined after a rotation because a pivot cannot move.",
                "The origin remains at $(0, 0)$ because the center of rotation is a fixed point that maps onto itself.",
                "The origin moves to $(-1, 0)$ following the rule $(x, y) \\to (-y, x)$."
            ],
            "correct": 2,
            "hint": "Consider what happens to the point where the tip of your pencil rests when turning tracing paper (Into Math TE p. 62-63).",
            "explanation": "The center of rotation is a fixed point (invariant point) under any rotation. Under the coordinate mapping rule $(x, y) \\to (-y, x)$, substituting $(0, 0)$ yields $(-0, 0) = (0, 0)$. Choices A and D incorrectly assign non-zero coordinates to the center of rotation, while Choice B incorrectly claims the point is undefined.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-3",
            "q": "Point $A(3, 7)$ is rotated $90^\\circ$ counterclockwise about the origin. What are the coordinates of the image point $A'$?",
            "opts": [
                "$A'(7, -3)$",
                "$A'(-7, 3)$",
                "$A'(-3, -7)$",
                "$A'(-7, -3)$"
            ],
            "correct": 1,
            "hint": "Apply the algebraic mapping rule for a $90^\\circ$ counterclockwise rotation: $(x, y) \\to (-y, x)$.",
            "explanation": "For a $90^\\circ$ counterclockwise rotation about the origin, the mapping rule is $(x, y) \\to (-y, x)$. Given $A(3, 7)$, we have $x = 3$ and $y = 7$. Substituting these values gives $A'(-7, 3)$. Choice A $(7, -3)$ is the result of a $90^\\circ$ clockwise rotation $(y, -x)$. Choice C $(-3, -7)$ is a $180^\\circ$ rotation $(-x, -y)$. Choice D $(-7, -3)$ incorrectly negates both coordinates after swapping.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-4",
            "q": "Point $B(-4, -6)$ in Quadrant III is rotated $90^\\circ$ counterclockwise about the origin. What are the coordinates of the image point $B'$?",
            "opts": [
                "$B'(-6, 4)$",
                "$B'(4, -6)$",
                "$B'(-6, -4)$",
                "$B'(6, -4)$"
            ],
            "correct": 3,
            "hint": "Be careful with signs: $-y$ means the opposite of $y$. If $y = -6$, what is $-y$?",
            "explanation": "The algebraic rule for a $90^\\circ$ counterclockwise rotation about the origin is $(x, y) \\to (-y, x)$. For $B(-4, -6)$, the new $x$-coordinate is $-y = -(-6) = 6$, and the new $y$-coordinate is $x = -4$. Thus $B'(6, -4)$ lies in Quadrant IV. Choice A $(-6, 4)$ forgets that $-(-6) = +6$. Choice B $(4, -6)$ negates $x$ and leaves $y$ unchanged (a reflection across the $y$-axis). Choice C $(-6, -4)$ swaps coordinates without applying the required negation.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-5",
            "q": "In HMH Into Math Lesson 1.4, a figure with vertex $J(-3, 4)$ is rotated $180^\\circ$ about the origin. What are the coordinates of the image vertex $J'$?",
            "opts": [
                "$J'(3, -4)$",
                "$J'(-4, -3)$",
                "$J'(4, 3)$",
                "$J'(-3, -4)$"
            ],
            "correct": 0,
            "hint": "A $180^\\circ$ rotation takes every point $(x, y)$ to $(-x, -y)$, whether turned clockwise or counterclockwise.",
            "explanation": "The rule for a $180^\\circ$ rotation about the origin is $(x, y) \\to (-x, -y)$. Applying this to $J(-3, 4)$ gives $x' = -(-3) = 3$ and $y' = -(4) = -4$, resulting in $J'(3, -4)$. Note that turning $180^\\circ$ clockwise or $180^\\circ$ counterclockwise yields the identical image. Choice B $(-4, -3)$ mistakenly swaps the coordinates. Choice C $(4, 3)$ applies a $90^\\circ$ clockwise rule with sign errors. Choice D $(-3, -4)$ only negates the $y$-coordinate.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-6",
            "q": "In the textbook activity (TE p. 64), the letter 'N' has vertex $A(2, 1)$ and is rotated $90^\\circ$ clockwise about the origin to create the letter 'Z'. What are the coordinates of image vertex $A'$?",
            "opts": [
                "$A'(-1, 2)$",
                "$A'(1, -2)$",
                "$A'(-2, 1)$",
                "$A'(-2, -1)$"
            ],
            "correct": 1,
            "hint": "A $90^\\circ$ clockwise rotation follows the algebraic rule $(x, y) \\to (y, -x)$.",
            "explanation": "Rotating $90^\\circ$ clockwise about the origin follows the mapping rule $(x, y) \\to (y, -x)$. With preimage $A(2, 1)$, we swap coordinates and negate the new second component: $x' = y = 1$ and $y' = -x = -2$. Therefore, $A'(1, -2)$. Choice A $(-1, 2)$ is the result of a $90^\\circ$ counterclockwise rotation $(-y, x)$. Choice C $(-2, 1)$ is a reflection across the $y$-axis. Choice D $(-2, -1)$ is a $180^\\circ$ rotation.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-7",
            "q": "Which algebraic mapping rule represents both a $270^\\circ$ counterclockwise rotation and a $90^\\circ$ clockwise rotation about the origin?",
            "opts": [
                "$(x, y) \\to (-y, x)$",
                "$(x, y) \\to (-x, -y)$",
                "$(x, y) \\to (y, -x)$",
                "$(x, y) \\to (-y, -x)$"
            ],
            "correct": 2,
            "hint": "A full circle is $360^\\circ$. Turning $90^\\circ$ clockwise brings a figure to the same position as turning $360^\\circ - 90^\\circ = 270^\\circ$ counterclockwise.",
            "explanation": "Because a full rotation is $360^\\circ$, moving $90^\\circ$ clockwise places a figure in the exact same position as moving $360^\\circ - 90^\\circ = 270^\\circ$ counterclockwise. Both rotations share the coordinate rule $(x, y) \\to (y, -x)$. Choice A $(-y, x)$ represents a $90^\\circ$ counterclockwise (or $270^\\circ$ clockwise) rotation. Choice B $(-x, -y)$ represents a $180^\\circ$ rotation. Choice D $(-y, -x)$ is a reflection across the line $y = -x$.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-8",
            "q": "Point $P(5, -2)$ undergoes a $270^\\circ$ clockwise rotation about the origin. What are the coordinates of image point $P'$?",
            "opts": [
                "$P'(2, 5)$",
                "$P'(-2, -5)$",
                "$P'(-5, 2)$",
                "$P'(5, 2)$"
            ],
            "correct": 0,
            "hint": "Convert the $270^\\circ$ clockwise rotation to its equivalent counterclockwise turn: $360^\\circ - 270^\\circ = 90^\\circ$ counterclockwise.",
            "explanation": "Rotating $270^\\circ$ clockwise is equivalent to rotating $360^\\circ - 270^\\circ = 90^\\circ$ counterclockwise about the origin. The rule for $90^\\circ$ counterclockwise is $(x, y) \\to (-y, x)$. For $P(5, -2)$, $x' = -(-2) = 2$ and $y' = x = 5$, giving $P'(2, 5)$. Choice B $(-2, -5)$ uses the $90^\\circ$ clockwise rule $(y, -x)$. Choice C $(-5, 2)$ is a $180^\\circ$ rotation $(-x, -y)$. Choice D $(5, 2)$ reflects across the $x$-axis.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-9",
            "q": "A quadrilateral in the coordinate plane is rotated $360^\\circ$ about the origin. Which statement correctly describes the relationship between the preimage and its image?",
            "opts": [
                "The image is inverted into the opposite quadrant according to $(x, y) \\to (-x, -y)$.",
                "The coordinates swap axes according to $(x, y) \\to (y, x)$.",
                "The image is identical to the preimage and occupies the exact same position because a $360^\\circ$ rotation is a full turn: $(x, y) \\to (x, y)$.",
                "The coordinates are multiplied by 2 because $360^\\circ$ is twice $180^\\circ$."
            ],
            "correct": 2,
            "hint": "How many degrees are in one complete circle or full turn?",
            "explanation": "A $360^\\circ$ rotation represents one complete revolution around the center of rotation. Every point completes a full circular path and returns to its initial location, described by the identity rule $(x, y) \\to (x, y)$. Choice A describes a $180^\\circ$ rotation. Choice B is a reflection across the line $y = x$. Choice D confuses rotation with a dilation of scale factor 2.",
            "dok": 1,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-10",
            "q": "Triangle $ABC$ has vertices named in clockwise order: $A(1, 2)$, $B(4, 2)$, and $C(1, 6)$. Which transformation will result in an image triangle whose corresponding vertices $A' \\to B' \\to C'$ remain in clockwise order?",
            "opts": [
                "A reflection across the $x$-axis",
                "A reflection across the $y$-axis",
                "A reflection across the line $y = x$",
                "A rotation of $90^\\circ$ counterclockwise about the origin"
            ],
            "correct": 3,
            "hint": "Which rigid motions preserve orientation (clockwise remains clockwise), and which rigid motion reverses orientation?",
            "explanation": "Rotations and translations preserve vertex orientation: if the vertices of the preimage read in clockwise order, the vertices of the image also read in clockwise order. In contrast, reflections reverse orientation (turning clockwise order into counterclockwise order). Therefore, only the rotation in Choice D preserves the clockwise order. Choices A, B, and C are all reflections, each of which reverses vertex orientation.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-11",
            "q": "In HMH Into Math Lesson 1.4 (p. 67 Problem 8), $\\triangle JKL$ has an area of $3.25\\text{ square units}$ and a perimeter of $8.5\\text{ units}$. What happens to its area and perimeter when it is rotated $180^\\circ$ about vertex $J$?",
            "opts": [
                "Both area and perimeter remain unchanged: $\\text{Area} = 3.25\\text{ square units}$ and $\\text{Perimeter} = 8.5\\text{ units}$.",
                "The perimeter doubles to $17.0\\text{ units}$, but the area remains $3.25\\text{ square units}$.",
                "The area becomes negative ($-3.25\\text{ square units}$) because the figure is inverted.",
                "The area becomes $0$ because the center of rotation is located at vertex $J$."
            ],
            "correct": 0,
            "hint": "Remember that a rotation is a rigid motion (isometry). What properties are preserved by all rigid motions?",
            "explanation": "Rotations are rigid motions (isometries), which preserve all distances (segment lengths) and angle measures regardless of the chosen center of rotation. Because all side lengths are preserved, the perimeter remains $8.5\\text{ units}$. Because side lengths and angle measures are preserved, the area remains strictly $3.25\\text{ square units}$. Area cannot be negative (Choice C), does not collapse to zero (Choice D), and perimeter does not change (Choice B).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-12",
            "q": "Line segment $AB$ has endpoints $A(1, 2)$ and $B(3, 8)$, giving it a slope of $m = \\frac{8 - 2}{3 - 1} = 3$. If segment $AB$ is rotated $90^\\circ$ counterclockwise about the origin to form segment $A'B'$, what is the slope $m'$ of the image segment?",
            "opts": [
                "$m' = 3$",
                "$m' = -3$",
                "$m' = -\\frac{1}{3}$",
                "$m' = \\frac{1}{3}$"
            ],
            "correct": 2,
            "hint": "A $90^\\circ$ rotation turns a line so that it is perpendicular to the original line. What is the relationship between the slopes of two perpendicular lines?",
            "explanation": "Rotating a line segment by $90^\\circ$ turns the segment perpendicular to its original orientation. Two non-vertical perpendicular lines have slopes that are negative reciprocals ($m' = -\\frac{1}{m}$). Since the original slope is $m = 3$, the new slope is $m' = -\\frac{1}{3}$. We can verify with coordinates: $A'(-2, 1)$ and $B'(-8, 3)$ using $(x, y) \\to (-y, x)$. Slope $m' = \\frac{3 - 1}{-8 - (-2)} = \\frac{2}{-6} = -\\frac{1}{3}$. Choice A assumes slope is invariant (true for $180^\\circ$ or translations, not $90^\\circ$). Choice B only negates the slope without taking the reciprocal. Choice D takes the reciprocal without negating.",
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-13",
            "q": "Line segment $CD$ has a slope of $m = -\\frac{4}{7}$. After undergoing a $180^\\circ$ rotation about the origin, what is the slope of the resulting image segment $C'D'$?",
            "opts": [
                "$m' = \\frac{7}{4}$",
                "$m' = -\\frac{4}{7}$",
                "$m' = \\frac{4}{7}$",
                "$m' = -\\frac{7}{4}$"
            ],
            "correct": 1,
            "hint": "A $180^\\circ$ rotation turns a segment in the opposite direction along a parallel line. What is true about the slopes of parallel lines?",
            "explanation": "Under a $180^\\circ$ rotation about the origin, every point $(x, y)$ maps to $(-x, -y)$. The slope formula between image points is $m' = \\frac{-y_2 - (-y_1)}{-x_2 - (-x_1)} = \\frac{-(y_2 - y_1)}{-(x_2 - x_1)} = \\frac{y_2 - y_1}{x_2 - x_1} = m$. A $180^\\circ$ rotation preserves the slope ($m' = m$) because the image line is parallel to (or lies on the same line as) the preimage line. Thus, the slope remains $-\\frac{4}{7}$. Choice A is the perpendicular negative reciprocal (for $90^\\circ$). Choice C erroneously flips the sign. Choice D is the reciprocal without preserving the sign.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-14",
            "q": "In Lesson 1.4 Spark Your Learning (TE p. 61-62), students investigate rotational symmetry. What is the minimum positive angle of rotation about its center that will map a regular hexagon ($6$ equal sides) onto itself?",
            "opts": [
                "$90^\\circ$",
                "$120^\\circ$",
                "$45^\\circ$",
                "$60^\\circ$"
            ],
            "correct": 3,
            "hint": "The minimum angle of rotational symmetry for a regular $n$-sided polygon is $\\frac{360^\\circ}{n}$.",
            "explanation": "A regular polygon with $n$ sides has $n$-fold rotational symmetry. The minimum positive angle of rotation that maps the figure onto itself is $\\frac{360^\\circ}{n}$. For a regular hexagon ($n = 6$), the minimum angle is $\\frac{360^\\circ}{6} = 60^\\circ$. Choice A ($90^\\circ$) is for a square ($n = 4$). Choice B ($120^\\circ$) is a multiple of $60^\\circ$ and the minimum angle for an equilateral triangle ($n = 3$), but not the minimum for a hexagon. Choice C ($45^\\circ$) is for a regular octagon ($n = 8$).",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-15",
            "q": "In HMH Into Math Lesson 1.4 Step It Out (TE p. 64), students identify uppercase letters that look identical after a $180^\\circ$ rotation about their center point. Which group consists ENTIRELY of letters with $180^\\circ$ rotational symmetry?",
            "opts": [
                "$\\text{A, M, T, V}$",
                "$\\text{B, C, D, E}$",
                "$\\text{H, N, O, Z}$",
                "$\\text{F, G, J, L}$"
            ],
            "correct": 2,
            "hint": "Imagine turning the letters upside down ($180^\\circ$). Which group contains letters that still look exactly the same?",
            "explanation": "As highlighted in the Teacher Edition (p. 64 Turn and Talk), the uppercase letters possessing $180^\\circ$ rotational symmetry are H, I, N, O, S, X, and Z. Turning any of these letters upside down results in the exact same letter. Choice A contains letters with vertical reflection symmetry (turning upside down reverses 'M' into 'W' and inverts 'A'). Choice B contains letters with horizontal reflection symmetry. Choice D contains asymmetric letters with neither reflectional nor rotational symmetry.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-16",
            "q": "In Lesson 1.4 On Your Own (TE p. 67 Problem 9), a triangle has vertices at $(-2, 1)$, $(-5, 2)$, and $(-3, 6)$. After a rotation about the origin, the image has vertices at $(1, 2)$, $(2, 5)$, and $(6, 3)$. Which rotation was performed?",
            "opts": [
                "$90^\\circ$ counterclockwise rotation about the origin",
                "$180^\\circ$ rotation about the origin",
                "$360^\\circ$ rotation about the origin",
                "$90^\\circ$ clockwise rotation about the origin"
            ],
            "correct": 3,
            "hint": "Compare $(x, y) = (-2, 1)$ with its image $(x', y') = (1, 2)$. How do the positions and signs of $x$ and $y$ relate?",
            "explanation": "Testing preimage point $(-2, 1)$ against image $(1, 2)$: The original $y$-value ($1$) becomes the new $x'$-value, and the opposite of the original $x$-value ($-(-2) = 2$) becomes the new $y'$-value. This matches the algebraic rule $(x, y) \\to (y, -x)$. Checking the other vertices confirms this rule: $(-5, 2) \\to (2, -(-5)) = (2, 5)$ and $(-3, 6) \\to (6, -(-3)) = (6, 3)$. The rule $(x, y) \\to (y, -x)$ represents a $90^\\circ$ clockwise rotation about the origin (or $270^\\circ$ counterclockwise). Choice A is $90^\\circ$ counterclockwise, which follows $(-y, x)$ and would yield $(-1, -2)$. Choice B is $180^\\circ$, which follows $(-x, -y)$ and would yield $(2, -1)$. Choice C is $360^\\circ$, which leaves coordinates unchanged.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-17",
            "q": "In Lesson 1.4 (TE p. 67 Problem 10), a shape is first rotated by the rule $(x, y) \\to (y, -x)$, and then the resulting image is rotated by the rule $(x, y) \\to (-x, -y)$. Which single transformation maps the original preimage directly to the final image?",
            "opts": [
                "A $90^\\circ$ counterclockwise rotation about the origin: $(x, y) \\to (-y, x)$",
                "A $90^\\circ$ clockwise rotation about the origin: $(x, y) \\to (y, -x)$",
                "A $180^\\circ$ rotation about the origin: $(x, y) \\to (-x, -y)$",
                "A $360^\\circ$ rotation about the origin: $(x, y) \\to (x, y)$"
            ],
            "correct": 0,
            "hint": "Track what happens to the coordinates step-by-step: first $(x, y) \\to (y, -x)$, then apply the second rule $(-x, -y)$ to the intermediate coordinates $(y, -x)$.",
            "explanation": "Let us compose the two rules step-by-step: Step 1 applies $(x, y) \\to (y, -x)$ (a $90^\\circ$ clockwise rotation). Step 2 applies $(-x, -y)$ (a $180^\\circ$ rotation), which negates both components of the intermediate pair: $(y, -x) \\to (-y, -(-x)) = (-y, x)$. The resulting composite rule is $(x, y) \\to (-y, x)$, which is a $90^\\circ$ counterclockwise rotation about the origin. Geometrically, rotating $90^\\circ$ clockwise ($-90^\\circ$) followed by $180^\\circ$ yields $-90^\\circ + 180^\\circ = +90^\\circ$ (or $90^\\circ$ counterclockwise). Choices B, C, and D do not match the composite mapping rule.",
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-18",
            "q": "In HMH Into Math Lesson 1.4 Check Understanding (TE p. 65 Problem 1), Antoine and Bobby each rotated a pentagon about Point $P$, but got different results. Bobby's transformed pentagon has the exact same orientation (sides remain parallel to the original directions and it points upward like the preimage). Antoine's transformed pentagon turned so that its top vertex now points to the right. Which student performed a correct rotation?",
            "opts": [
                "Bobby, because rigid motions must keep all corresponding sides parallel to their preimages.",
                "Antoine, because rotating around a point turns the figure and changes the direction it faces; Bobby performed a translation.",
                "Both students performed valid rotations of different angles about Point $P$.",
                "Neither student is correct, because Point $P$ must be the origin $(0, 0)$."
            ],
            "correct": 1,
            "hint": "What is the key visual difference between sliding a figure (translation) and turning a figure around a pivot point (rotation)?",
            "explanation": "As stated in the Into Math Teacher Edition (p. 65 Check Understanding 1): 'Antoine’s rotation is correct. Bobby appears to have performed a translation.' In a rotation, all points travel along circular arcs around the center of rotation, which alters the direction the figure faces. Bobby merely slid the figure without turning it, which is the definition of a translation. Choice A is incorrect because rotations do not keep sides parallel to their preimages (except for $180^\\circ$ rotations). Choice D is incorrect because any point in the plane can serve as a center of rotation.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-19",
            "q": "A student attempts to rotate the point $M(4, -3)$ by $90^\\circ$ counterclockwise about the origin, but writes the image coordinates as $M'(-4, -3)$. What error did the student commit?",
            "opts": [
                "The student correctly applied the $90^\\circ$ counterclockwise rotation rule.",
                "The student performed a $180^\\circ$ rotation about the origin.",
                "The student performed a $90^\\circ$ clockwise rotation instead of counterclockwise.",
                "The student only negated the $x$-coordinate, producing a reflection across the $y$-axis instead of swapping the coordinates and negating $y$ via $(x, y) \\to (-y, x)$."
            ],
            "correct": 3,
            "hint": "Recall the $90^\\circ$ counterclockwise rule: $(x, y) \\to (-y, x)$. Did the student swap the $x$ and $y$ values?",
            "explanation": "The correct rule for a $90^\\circ$ counterclockwise rotation is $(x, y) \\to (-y, x)$. For $M(4, -3)$, the correct image is $M'(-(-3), 4) = M'(3, 4)$. The student wrote $(-4, -3)$, which kept the coordinates in their original positions and only negated $x$: $(x, y) \\to (-x, y)$. This is a reflection across the $y$-axis, not a rotation. The student forgot to swap the coordinates. Choice B ($180^\\circ$ rotation) would result in $(-4, 3)$. Choice C ($90^\\circ$ clockwise rotation) would result in $(-3, -4)$.",
            "dok": 2,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        },
        {
            "id": "p-1-4-mcq-20",
            "q": "In Lesson 1.4 Test Prep (TE p. 69 Problem 6), triangle $MNP$ is rotated about vertex $P$ to produce triangle $PQR$. Which of the following geometric properties MUST be true regarding vertex $P$ and the transformation?",
            "opts": [
                "Vertex $P$ must move according to the coordinate origin rule $(x, y) \\to (-y, x)$.",
                "The area of $\\triangle PQR$ is cut in half because one vertex is pinned at the center.",
                "Vertex $P$ remains at its exact location ($P' = P$) because it is the center of rotation, and side lengths and angle measures are preserved.",
                "The orientation of the vertices reverses from clockwise to counterclockwise."
            ],
            "correct": 2,
            "hint": "The center of rotation does not move during a rotation, and rotations are rigid motions.",
            "explanation": "When a figure is rotated about one of its own vertices (Point $P$), that vertex serves as the center of rotation and is a fixed point: its image coincides with itself ($P' = P$). Furthermore, because rotation is a rigid motion, all side lengths, angle measures, and areas are strictly preserved ($\\text{Area}(\\triangle PQR) = \\text{Area}(\\triangle MNP)$), and vertex orientation is preserved. Choice A incorrectly applies an origin-centered rule to a vertex-centered rotation. Choice B falsely claims area changes. Choice D confuses rotations with reflections (which reverse orientation).",
            "dok": 3,
            "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
        }
    ]
}

# Aliases for convenience and backward compatibility
LESSON_1_4_DATA["practice"] = {"mcqs": LESSON_1_4_DATA["mcqs"]}
LESSON_1_4_DATA["practiceQuestions"] = LESSON_1_4_DATA["mcqs"]
MCQS = LESSON_1_4_DATA["mcqs"]

if __name__ == "__main__":
    print(f"Loaded Lesson 1.4: '{LESSON_1_4_DATA['title']}'")
    print(f"Total MCQs: {len(LESSON_1_4_DATA['mcqs'])}")
    for i, q in enumerate(LESSON_1_4_DATA["mcqs"], 1):
        print(f"Q{i:02d} ({q['id']}): DOK {q['dok']} | Ans: {chr(65 + q['correct'])} | {q['q'][:65]}...")
