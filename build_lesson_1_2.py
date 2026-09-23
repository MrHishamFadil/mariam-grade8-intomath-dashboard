# -*- coding: utf-8 -*-
"""
build_lesson_1_2.py
Curriculum Content & 20 High-Yield MCQs for Lesson 1.2: Explore Translations
Based on HMH Into Math Grade 8 Teacher Edition (pages 36-47 in extracted_module1_raw.json)

Standards Covered:
  - CCSS.MATH.CONTENT.8.G.A.1: Verify experimentally the properties of rotations, reflections, and translations.
  - CCSS.MATH.CONTENT.8.G.A.1.a: Lines are taken to lines, and line segments to line segments of the same length.
  - CCSS.MATH.CONTENT.8.G.A.1.b: Angles are taken to angles of the same measure.
  - CCSS.MATH.CONTENT.8.G.A.1.c: Parallel lines are taken to parallel lines.
  - CCSS.MATH.CONTENT.8.G.A.3: Describe the effect of dilations, translations, rotations, and reflections on
    two-dimensional figures using coordinates.

Topics Covered Thoroughly:
  1. Translation vectors and vector notation <a, b>.
  2. Algebraic mapping rule notation: (x, y) -> (x + a, y + b).
  3. Horizontal translations: (x, y) -> (x + a, y) where a > 0 is right, a < 0 is left.
  4. Vertical translations: (x, y) -> (x, y + b) where b > 0 is up, b < 0 is down.
  5. Combined translations shifting figures across quadrants (e.g. Quadrant II to Quadrant IV).
  6. Finding image coordinates given preimage coordinates and rule.
  7. Finding translation rule given preimage and image coordinates.
  8. Finding preimage coordinates given image coordinates and translation rule (working backward).
  9. Invariance under translation: side lengths, angle measures, slope of segments, and orientation.
  10. Distance traveled by points: using Pythagorean theorem sqrt(a^2 + b^2).
  11. Successive translations (compositions of translations): (x + a1 + a2, y + b1 + b2).
  12. Real-world contextual problems from the book (drone navigation, game piece movement, architecture).
"""

import collections.abc

MCQS = [
    {
        "id": "p-1-2-mcq-1",
        "q": "A translation slides a geometric figure $6\\text{ units left}$ and $8\\text{ units up}$ on a coordinate plane. Which vector represents this transformation in component vector notation?",
        "opts": [
            "$\\langle 6, -8 \\rangle$",
            "$\\langle -6, 8 \\rangle$",
            "$\\langle 8, -6 \\rangle$",
            "$\\langle -8, 6 \\rangle$"
        ],
        "correct": 1,
        "hint": "In vector notation $\\langle a, b \\rangle$, the first value $a$ represents horizontal change (negative for left, positive for right), and the second value $b$ represents vertical change (positive for up, negative for down).",
        "explanation": "A horizontal shift of 6 units to the left is represented by $a = -6$, and a vertical shift of 8 units up is represented by $b = +8$. Thus, the vector in component notation is $\\langle -6, 8 \\rangle$. Choice A reverses the positive and negative directions. Choices C and D swap the horizontal and vertical components.",
        "dok": 1,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-2",
        "q": "Which algebraic mapping rule correctly represents translating a polygon $4\\text{ units right}$ and $7\\text{ units down}$ on a Cartesian coordinate plane?",
        "opts": [
            "$(x, y) \\to (x + 4, y - 7)$",
            "$(x, y) \\to (x - 4, y + 7)$",
            "$(x, y) \\to (x + 7, y - 4)$",
            "$(x, y) \\to (4x, -7y)$"
        ],
        "correct": 0,
        "hint": "Moving right increases the $x$-coordinate, while moving down decreases the $y$-coordinate.",
        "explanation": "Moving 4 units right adds 4 to each $x$-coordinate ($x \\to x + 4$). Moving 7 units down subtracts 7 from each $y$-coordinate ($y \\to y - 7$). Combining these gives $(x, y) \\to (x + 4, y - 7)$. Choice B incorrectly subtracts for right and adds for down. Choice C swaps the $x$ and $y$ shifts. Choice D uses multiplication, which describes a dilation rather than a translation.",
        "dok": 1,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-3",
        "q": "Point $W(-5, 9)$ undergoes the pure horizontal translation $(x, y) \\to (x + 8, y)$. What are the coordinates of the image point $W'$?",
        "opts": [
            "$(-13, 9)$",
            "$(-5, 17)$",
            "$(3, 9)$",
            "$(3, 17)$"
        ],
        "correct": 2,
        "hint": "Only the $x$-coordinate is modified by adding 8; the $y$-coordinate remains completely unchanged.",
        "explanation": "Applying the rule $(x, y) \\to (x + 8, y)$ to $W(-5, 9)$: $x' = -5 + 8 = 3$, and $y' = 9$. Thus, $W' = (3, 9)$. Choice A mistakenly subtracts 8 ($-5 - 8 = -13$). Choice B mistakenly adds 8 to the $y$-coordinate. Choice D erroneously adds 8 to both coordinates.",
        "dok": 1,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-4",
        "q": "A line segment on a blueprint with endpoint $P(4, -3)$ is translated vertically such that its image is $P'(4, -11)$. Which translation rule was applied to the segment?",
        "opts": [
            "$(x, y) \\to (x, y - 8)$",
            "$(x, y) \\to (x, y + 8)$",
            "$(x, y) \\to (x - 8, y)$",
            "$(x, y) \\to (x, y - 14)$"
        ],
        "correct": 0,
        "hint": "Calculate the vertical change: $b = y_{\\text{image}} - y_{\\text{preimage}} = -11 - (-3)$.",
        "explanation": "The $x$-coordinate does not change ($4 \\to 4$), so there is zero horizontal displacement. The vertical displacement is $b = y' - y = -11 - (-3) = -11 + 3 = -8$, meaning the segment moved 8 units down. The mapping rule is $(x, y) \\to (x, y - 8)$. Choice B incorrectly adds 8 instead of subtracting. Choice C applies the shift horizontally. Choice D adds $-11$ and $-3$ to get $-14$.",
        "dok": 1,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-5",
        "q": "Triangle $DEF$ has vertices $D(-3, 4)$, $E(1, 6)$, and $F(2, -1)$. The triangle is translated according to the rule $(x, y) \\to (x + 5, y - 6)$. What are the coordinates of vertex $D'$?",
        "opts": [
            "$(-8, 10)$",
            "$(2, 10)$",
            "$(-8, -2)$",
            "$(2, -2)$"
        ],
        "correct": 3,
        "hint": "Substitute $x = -3$ and $y = 4$ directly into the algebraic rule: $x' = -3 + 5$ and $y' = 4 - 6$.",
        "explanation": "Substituting $D(-3, 4)$ into $(x + 5, y - 6)$ yields $x' = -3 + 5 = 2$ and $y' = 4 - 6 = -2$. Therefore, $D' = (2, -2)$. Choice A subtracts 5 and adds 6 ($(-8, 10)$). Choice B mistakenly adds 6 to $y$ ($4 + 6 = 10$). Choice C subtracts 5 from $x$ ($-3 - 5 = -8$).",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-6",
        "q": "In a computer graphic animation, polygon vertex $K(7, -3)$ maps to image vertex $K'(-1, 5)$ under a translation. Which algebraic rule describes this translation?",
        "opts": [
            "$(x, y) \\to (x + 8, y - 8)$",
            "$(x, y) \\to (x - 8, y + 8)$",
            "$(x, y) \\to (x - 6, y + 2)$",
            "$(x, y) \\to (x + 6, y - 2)$"
        ],
        "correct": 1,
        "hint": "Always subtract the preimage coordinates from the image coordinates: $a = x' - x$ and $b = y' - y$.",
        "explanation": "Calculate the horizontal displacement: $a = x' - x = -1 - 7 = -8$. Calculate the vertical displacement: $b = y' - y = 5 - (-3) = 5 + 3 = 8$. Thus, the rule is $(x, y) \\to (x - 8, y + 8)$. Choice A subtracts image from preimage ($7 - (-1) = 8$), which reverses the direction vector. Choices C and D add coordinates instead of computing differences.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-7",
        "q": "After a translation using the rule $(x, y) \\to (x - 6, y + 9)$, the image of point $M$ is $M'(2, -4)$. What were the coordinates of the original preimage point $M$?",
        "opts": [
            "$(8, -13)$",
            "$(-4, 5)$",
            "$(8, 5)$",
            "$(-4, -13)$"
        ],
        "correct": 0,
        "hint": "Work backward from the image coordinates by applying inverse operations: solve $x - 6 = 2$ and $y + 9 = -4$.",
        "explanation": "To recover the preimage from the image, apply the inverse operations: $x = x' + 6 = 2 + 6 = 8$, and $y = y' - 9 = -4 - 9 = -13$. Thus, $M = (8, -13)$. Verifying forward: $(8 - 6, -13 + 9) = (2, -4) = M'$. Choice B erroneously applies the forward rule to $M'$ ($2 - 6 = -4, -4 + 9 = 5$). Choice C adds 9 to $y$ instead of subtracting. Choice D subtracts 6 from $x$.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-8",
        "q": "Triangle $ABC$ lies in **Quadrant II** with vertex $A(-4, 5)$. The triangle is translated by the rule $(x, y) \\to (x + 9, y - 8)$. In which quadrant of the coordinate plane does the image vertex $A'$ lie?",
        "opts": [
            "Quadrant I",
            "Quadrant II",
            "Quadrant III",
            "Quadrant IV"
        ],
        "correct": 3,
        "hint": "Calculate the image coordinates $A'(x', y')$ and inspect their signs: $(+, +)$ is Quadrant I, $(-, +)$ is Quadrant II, $(-, -)$ is Quadrant III, and $(+, -)$ is Quadrant IV.",
        "explanation": "Applying the translation rule to $A(-4, 5)$: $x' = -4 + 9 = 5$ (positive) and $y' = 5 - 8 = -3$ (negative). An ordered pair with a positive $x$-value and negative $y$-value $(5, -3)$ lies in **Quadrant IV**. Choice A represents Quadrant I ($x > 0, y > 0$). Choice B represents Quadrant II ($x < 0, y > 0$). Choice C represents Quadrant III ($x < 0, y < 0$).",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-9",
        "q": "Rectangle $PQRS$ has side lengths $PQ = 8\\text{ cm}$ and $QR = 5\\text{ cm}$, with $m\\angle P = 90^\\circ$. If $PQRS$ is translated $12\\text{ units left}$ and $15\\text{ units down}$ to form rectangle $P'Q'R'S'$, which statement is **NOT** true?",
        "opts": [
            "The perimeter of $P'Q'R'S'$ is greater than the perimeter of $PQRS$ because the figure was translated by a large distance.",
            "The length of segment $P'Q'$ is equal to $8\\text{ cm}$.",
            "$m\\angle P' = 90^\\circ$.",
            "Segment $P'Q'$ is parallel to segment $PQ$."
        ],
        "correct": 0,
        "hint": "A translation is a rigid motion (isometry). Does sliding a shape across a flat plane change its perimeter or dimensions?",
        "explanation": "Translations are rigid motions that preserve side lengths, angle measures, perimeter, area, and parallelism. Sliding a figure never stretches or shrinks it, so the perimeter remains exactly $2(8 + 5) = 26\\text{ cm}$. Therefore, statement A is false (making it the correct answer to the question). Choices B, C, and D are all fundamental invariant properties preserved under translation.",
        "dok": 1,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-10",
        "q": "On a coordinate grid, line segment $\\overline{AB}$ connects $A(1, 2)$ to $B(4, 8)$, giving it a slope of $m = \\frac{8 - 2}{4 - 1} = 2$. Segment $\\overline{AB}$ is translated by $(x, y) \\to (x - 5, y + 3)$ to create image segment $\\overline{A'B'}$. What is the slope of $\\overline{A'B'}$?",
        "opts": [
            "$-2$",
            "$\\frac{1}{2}$",
            "$2$",
            "$-\\frac{3}{5}$"
        ],
        "correct": 2,
        "hint": "Under a translation, line segments map to parallel line segments. What do you know about the slopes of parallel lines?",
        "explanation": "Translations preserve the orientation and steepness of lines; every translated segment is parallel to its preimage segment. Since parallel lines have identical slopes, the slope of $\\overline{A'B'}$ is equal to the slope of $\\overline{AB}$, which is $2$. Calculating directly: $A'(-4, 5)$ and $B'(-1, 11)$; slope $= \\frac{11 - 5}{-1 - (-4)} = \\frac{6}{3} = 2$. Choice A is the negative slope. Choice B is the reciprocal slope. Choice D confuses the slope with the ratio of translation vector components.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-11",
        "q": "A polygon is translated on a coordinate grid according to the vector $\\langle 6, -8 \\rangle$. What is the straight-line distance that each vertex of the polygon travels during this translation?",
        "opts": [
            "$14\\text{ units}$",
            "$10\\text{ units}$",
            "$2\\text{ units}$",
            "$\\sqrt{28}\\text{ units}$"
        ],
        "correct": 1,
        "hint": "Use the Pythagorean theorem $d = \\sqrt{a^2 + b^2}$ to find the length (magnitude) of the translation vector.",
        "explanation": "The straight-line Euclidean distance traveled by any point under vector $\\langle a, b \\rangle$ is given by $d = \\sqrt{a^2 + b^2}$. Here, $d = \\sqrt{6^2 + (-8)^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10\\text{ units}$. Choice A simply adds the absolute shifts $6 + 8 = 14$ (taxicab distance, not straight-line distance). Choice C subtracts the components ($8 - 6 = 2$). Choice D subtracts the squares ($\\sqrt{64 - 36} = \\sqrt{28}$).",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-12",
        "q": "Triangle $XYZ$ is translated along vector $\\langle -5, 12 \\rangle$ to form Triangle $X'Y'Z'$. Vertex $X$ travels a straight-line distance of $13\\text{ units}$ to $X'$. How far does vertex $Z$ travel to reach its image $Z'$?",
        "opts": [
            "Exactly $13\\text{ units}$",
            "More than $13\\text{ units}$ if $Z$ is farther from the origin than $X$",
            "Less than $13\\text{ units}$ because $Z$ is at the opposite end of the triangle",
            "It cannot be determined without knowing the exact initial coordinates of $Z$"
        ],
        "correct": 0,
        "hint": "By definition, does a translation move every point by the same distance, or do different points travel different distances?",
        "explanation": "By definition, a translation slides EVERY point of a figure by the exact same distance and in the exact same direction along parallel paths. Because the vector is $\\langle -5, 12 \\rangle$, every point in the triangle travels $d = \\sqrt{(-5)^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13\\text{ units}$. Choices B, C, and D are misconceptions; distance traveled during a translation is constant across all points and does not depend on position relative to the origin.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-13",
        "q": "A geometric figure is first translated by $T_1: (x, y) \\to (x + 4, y - 3)$, and then its image is translated by $T_2: (x, y) \\to (x - 9, y + 8)$. Which single algebraic rule represents the composition of these two successive translations?",
        "opts": [
            "$(x, y) \\to (x + 13, y - 11)$",
            "$(x, y) \\to (x + 5, y - 5)$",
            "$(x, y) \\to (x - 5, y + 5)$",
            "$(x, y) \\to (x - 36, y - 24)$"
        ],
        "correct": 2,
        "hint": "Add the corresponding horizontal displacements together ($a_1 + a_2$) and the vertical displacements together ($b_1 + b_2$).",
        "explanation": "To combine successive translations, sum their respective components: $a_{\\text{net}} = 4 + (-9) = -5$, and $b_{\\text{net}} = -3 + 8 = 5$. Thus, the single equivalent mapping rule is $(x, y) \\to (x - 5, y + 5)$. Choice A subtracts the shifts ($4 - (-9) = 13, -3 - 8 = -11$). Choice B reverses the signs of the net shifts. Choice D multiplies the shifts.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-14",
        "q": "In HMH Into Math Lesson 1.2 *Turn and Talk*, students explore moving a chess piece $1\\text{ space right and } 2\\text{ spaces up}$ versus moving it $2\\text{ spaces up and } 1\\text{ space right}$. What mathematical property explains why both sequences result in the exact same final position?",
        "opts": [
            "The distributive property of multiplication over addition",
            "The commutative property of addition for real numbers ($x + a_1 + a_2 = x + a_2 + a_1$)",
            "The reflexive property of geometric congruence",
            "The inverse property of coordinate reflections"
        ],
        "correct": 1,
        "hint": "Translations are represented by adding constants to coordinate values. Does the order in which you add two real numbers change their sum?",
        "explanation": "Translations modify coordinates by adding constants: $x \\to x + a_1 + a_2$ and $y \\to y + b_1 + b_2$. Because addition of real numbers is commutative ($a_1 + a_2 = a_2 + a_1$ and $b_1 + b_2 = b_2 + b_1$), changing the sequence of the translations results in the identical final coordinates. Translations commute with each other. Choices A, C, and D cite unrelated properties.",
        "dok": 3,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-15",
        "q": "An agricultural inspection drone hovers over a crop field at coordinate $(15, 28)$, where coordinates are measured in meters. The flight computer executes a translation along vector $\\langle -32, -45 \\rangle$ to inspect an irrigation valve. What are the new coordinates of the drone?",
        "opts": [
            "$(-17, -17)$",
            "$(47, 73)$",
            "$(-17, 73)$",
            "$(47, -17)$"
        ],
        "correct": 0,
        "hint": "Add the vector components directly to the drone's initial coordinates: $x' = 15 + (-32)$ and $y' = 28 + (-45)$.",
        "explanation": "Applying the translation vector $\\langle -32, -45 \\rangle$: $x' = 15 + (-32) = -17\\text{ m}$, and $y' = 28 + (-45) = -17\\text{ m}$. Thus, the drone's new position is $(-17, -17)$. Choice B incorrectly subtracts negative values ($15 - (-32) = 47, 28 - (-45) = 73$). Choice C computes $x$ correctly but adds for $y$. Choice D adds for $x$ but subtracts for $y$.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-16",
        "q": "On a chessboard modeled as a coordinate grid (HMH TE p. 38), a knight begins at position $(3, 2)$. A player makes two consecutive legal moves: first sliding 1 unit right and 2 units up, and then sliding 2 units left and 1 unit up. What is the knight's final coordinate position?",
        "opts": [
            "$(4, 4)$",
            "$(0, 5)$",
            "$(2, 3)$",
            "$(2, 5)$"
        ],
        "correct": 3,
        "hint": "Calculate the intermediate position after the first move, then apply the second move to that result.",
        "explanation": "Move 1 (1 right, 2 up): $(x, y) \\to (x + 1, y + 2)$, landing the knight at $(3 + 1, 2 + 2) = (4, 4)$. Move 2 (2 left, 1 up): $(x, y) \\to (x - 2, y + 1)$, moving the knight from $(4, 4)$ to $(4 - 2, 4 + 1) = (2, 5)$. Choice A is the intermediate coordinate after only move 1. Choice B subtracts 2 from the initial $x$ without adding 1. Choice C subtracts 1 from $y$ on the second move instead of adding 1.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-17",
        "q": "An architect places Building $A$ on a city planning grid with vertices at $(1, 1)$, $(3, 1)$, $(3, 3)$, and $(1, 3)$ (a $2 \\times 2$ square; HMH TE p. 42-43). A developer proposes four new building footprints. Which proposal represents a **valid translation** of Building $A$?",
        "opts": [
            "Building $B'$ with vertices at $(1, 1)$, $(4, 1)$, $(4, 4)$, and $(1, 4)$",
            "Building $C'$ with vertices at $(-1, 1)$, $(-3, 1)$, $(-3, 3)$, and $(-1, 3)$",
            "Building $A'$ with vertices at $(5, -4)$, $(7, -4)$, $(7, -2)$, and $(5, -2)$",
            "Building $D'$ with vertices at $(2, 2)$, $(6, 2)$, $(6, 6)$, and $(2, 6)$"
        ],
        "correct": 2,
        "hint": "In a true translation, every vertex shifts by the exact same $a$ and $b$, and the dimensions ($2 \\times 2$) and orientation remain unchanged.",
        "explanation": "In Building $A'$, every single vertex is shifted by the identical rule $(x, y) \\to (x + 4, y - 5)$: $(1+4, 1-5)=(5, -4)$, $(3+4, 1-5)=(7, -4)$, $(3+4, 3-5)=(7, -2)$, and $(1+4, 3-5)=(5, -2)$. The size ($2 \\times 2$) and orientation are perfectly preserved. Choice A has dimensions $3 \\times 3$ (dilation). Choice B has vertices with opposite $x$-coordinates, representing a reflection across the $y$-axis. Choice D has dimensions $4 \\times 4$ (dilation by factor 2).",
        "dok": 3,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-18",
        "q": "Parallelogram $ABCD$ is translated on a coordinate plane. Vertex $A(-2, 3)$ maps to $A'(4, -1)$. If vertex $C$ is located at $(1, -4)$, what are the coordinates of image vertex $C'$?",
        "opts": [
            "$(-5, 0)$",
            "$(7, -8)$",
            "$(7, 0)$",
            "$(-5, -8)$"
        ],
        "correct": 1,
        "hint": "Find the translation vector from $A$ to $A'$: $a = 4 - (-2)$ and $b = -1 - 3$. Then apply this exact same vector to vertex $C$.",
        "explanation": "Determine the translation rule from $A(-2, 3) \\to A'(4, -1)$: $a = 4 - (-2) = 6$ and $b = -1 - 3 = -4$. The rule is $(x, y) \\to (x + 6, y - 4)$. Because translations shift all vertices equally, apply this rule to $C(1, -4)$: $x' = 1 + 6 = 7$, and $y' = -4 - 4 = -8$. Therefore, $C' = (7, -8)$. Choice A applies the inverse rule ($1 - 6 = -5, -4 + 4 = 0$). Choice C adds 4 to $y$ instead of subtracting 4. Choice D subtracts 6 from $x$.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-19",
        "q": "In HMH Into Math Lesson 1.2 Task 1D, students are asked: *“What translation must be performed on the image so that it returns to the exact location of the preimage?”* If a figure was translated by $(x, y) \\to (x - 7, y + 4)$, which rule will return the image back to its original preimage?",
        "opts": [
            "$(x, y) \\to (x - 7, y + 4)$",
            "$(x, y) \\to (x + 7, y + 4)$",
            "$(x, y) \\to (x - 4, y + 7)$",
            "$(x, y) \\to (x + 7, y - 4)$"
        ],
        "correct": 3,
        "hint": "The inverse translation reverses both directions: the opposite of moving left 7 is moving right 7, and the opposite of moving up 4 is moving down 4.",
        "explanation": "To undo a translation and return an image to its starting position, apply the inverse translation by negating both displacements. The opposite of shifting 7 units left ($-7$) is shifting 7 units right ($+7$), and the opposite of shifting 4 units up ($+4$) is shifting 4 units down ($-4$). Thus, the returning rule is $(x, y) \\to (x + 7, y - 4)$. Choice A repeats the forward translation. Choice B fails to reverse the vertical shift. Choice C swaps the horizontal and vertical numbers.",
        "dok": 2,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    },
    {
        "id": "p-1-2-mcq-20",
        "q": "A homeowner wants to slide a rectangular sofa from the center of a living room flush against a wall (HMH TE p. 39 DOK 3). The sofa has dimensions $84\\text{ inches long}$ by $36\\text{ inches deep}$. The available wall space between two doorways measures $90\\text{ inches wide}$. Why does the homeowner know with mathematical certainty that the sofa will fit against the wall after being pushed along a straight-line path without rotating?",
        "opts": [
            "Because sliding a shape across a floor slightly compresses its length along the direction of motion.",
            "Because translations alter the angle measures of a quadrilateral to adapt to boundary constraints.",
            "Because translations preserve side lengths, angle measures, and parallelism, the sofa's dimensions remain exactly $84\\text{ in.} \\times 36\\text{ in.}$, which is less than the $90\\text{ in.}$ space.",
            "Because the translation vector's magnitude reduces the perimeter of any translated object by a factor of $\\sqrt{a^2 + b^2}$."
        ],
        "correct": 2,
        "hint": "Translations are rigid motions. What happens to the side lengths, perimeter, and rectangular angles of an object when it slides?",
        "explanation": "Translations are rigid motions (isometries) that preserve side lengths, angle measures, collinearity, perimeter, and area. Because the sofa does not rotate, stretch, compress, or deform during the translation, its length remains exactly 84 inches. Since $84\\text{ in.} < 90\\text{ in.}$, the sofa is guaranteed to fit flush against the wall. Choice A falsely assumes physical deformation occurs during a geometric translation. Choices B and D contradict the fundamental property that translations preserve all angles, side lengths, and perimeter.",
        "dok": 3,
        "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
    }
]


class LessonData(list):
    """
    Hybrid data structure for Lesson 1.2:
    Acts both as a standard list of 20 MCQs (for iteration, indexing, len())
    and as a dictionary-like container with metadata keys.
    """
    def __init__(self, mcqs, **kwargs):
        super().__init__(mcqs)
        self.metadata = kwargs
        self.id = kwargs.get("id", "1.2")
        self.lessonId = kwargs.get("lessonId", "1.2")
        self.title = kwargs.get("title", "Lesson 1.2: Explore Translations")
        self.module = kwargs.get("module", 1)
        self.grade = kwargs.get("grade", "Grade 8")
        self.pages = kwargs.get("pages", "36-47")
        self.standards = kwargs.get("standards", "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3")
        self.mcqs = self
        self.practiceQuestions = self

    def __getitem__(self, key):
        if isinstance(key, str):
            if key in ("mcqs", "questions", "practiceQuestions"):
                return list(self)
            return self.metadata.get(key)
        return super().__getitem__(key)

    def get(self, key, default=None):
        if key in ("mcqs", "questions", "practiceQuestions"):
            return list(self)
        return self.metadata.get(key, default)

    def __contains__(self, item):
        if isinstance(item, str):
            return item in self.metadata or item in ("mcqs", "questions", "practiceQuestions")
        return super().__contains__(item)

    def keys(self):
        return list(self.metadata.keys()) + ["mcqs", "questions", "practiceQuestions"]

    def items(self):
        res = list(self.metadata.items())
        res.append(("mcqs", list(self)))
        return res

    def values(self):
        res = list(self.metadata.values())
        res.append(list(self))
        return res


# Register LessonData with collections.abc.Mapping
collections.abc.Mapping.register(LessonData)

# Instantiate LESSON_1_2_DATA
LESSON_1_2_DATA = LessonData(
    MCQS,
    id="1.2",
    lessonId="1.2",
    title="Lesson 1.2: Explore Translations",
    module=1,
    grade="Grade 8",
    curriculum="HMH Into Math Grade 8 Teacher Edition",
    pages="36-47",
    standard="CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
    standards=["CCSS.MATH.CONTENT.8.G.A.1", "CCSS.MATH.CONTENT.8.G.A.3"]
)

# Also export dictionary and list aliases for maximum compatibility
LESSON_1_2_MCQS = MCQS
LESSON_1_2_DICT = {
    "id": "1.2",
    "lessonId": "1.2",
    "title": "Lesson 1.2: Explore Translations",
    "module": 1,
    "grade": "Grade 8",
    "curriculum": "HMH Into Math Grade 8 Teacher Edition",
    "pages": "36-47",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
    "standards": ["CCSS.MATH.CONTENT.8.G.A.1", "CCSS.MATH.CONTENT.8.G.A.3"],
    "mcqs": MCQS,
    "practiceQuestions": MCQS
}


def validate_mcqs():
    """Validates the structure and mathematical integrity of the 20 MCQs."""
    assert len(MCQS) == 20, f"Expected exactly 20 MCQs, got {len(MCQS)}"
    expected_ids = [f"p-1-2-mcq-{i}" for i in range(1, 21)]

    for i, mcq in enumerate(MCQS):
        assert mcq["id"] == expected_ids[i], f"Mismatch at index {i}: {mcq['id']} != {expected_ids[i]}"
        assert "q" in mcq and len(mcq["q"]) > 10, f"Invalid question stem at index {i}"
        assert "$" in mcq["q"], f"Question stem at index {i} missing KaTeX formatting: {mcq['q']}"
        assert "opts" in mcq and len(mcq["opts"]) == 4, f"Invalid options length at index {i}"
        assert len(set(mcq["opts"])) == 4, f"Duplicate options found at index {i}"
        assert mcq["correct"] in [0, 1, 2, 3], f"Invalid correct index at index {i}: {mcq['correct']}"
        assert "hint" in mcq and len(mcq["hint"]) > 10, f"Missing or brief hint at index {i}"
        assert "explanation" in mcq and len(mcq["explanation"]) > 20, f"Missing explanation at index {i}"
        assert mcq["dok"] in [1, 2, 3], f"Invalid DOK at index {i}: {mcq['dok']}"
        assert mcq["standard"] == "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3", f"Invalid standard at index {i}"

    print(f"Validation SUCCESS: All {len(MCQS)} MCQs strictly conform to schema and requirements.")


if __name__ == "__main__":
    validate_mcqs()
    print("LESSON_1_2_DATA length:", len(LESSON_1_2_DATA))
    print("LESSON_1_2_DATA['title']:", LESSON_1_2_DATA["title"])
    print("LESSON_1_2_DATA.id:", LESSON_1_2_DATA.id)
    print("Sample Question 1:", LESSON_1_2_DATA[0]["q"])
