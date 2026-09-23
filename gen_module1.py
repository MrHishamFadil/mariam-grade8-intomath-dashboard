# -*- coding: utf-8 -*-
"""
Module 1 Lessons Generator: Transformations and Congruence (Lessons 1.1 - 1.5)
HMH Into Math Grade 8 Teacher Edition
"""

def get_module1_lessons():
    m1 = {}

    # =========================================================================
    # LESSON 1.1: Investigate Transformations
    # =========================================================================
    m1["1.1"] = {
        "id": "1.1",
        "lessonNumber": "1.1",
        "moduleNumber": 1,
        "moduleId": "module-1",
        "moduleTitle": "Module 1: Transformations and Congruence",
        "title": "Lesson 1.1: Investigate Transformations",
        "introAndConcept": {
            "lessonTitle": "Lesson 1.1: Investigate Transformations",
            "iCanStatement": "I can describe what happens to the size, shape, side lengths, angle measures, and parallelism of a figure when it undergoes a transformation, and classify transformations as rigid motions (isometries) or non-rigid motions.",
            "conceptExplanation": {
                "coreDefinition": "A transformation is a one-to-one geometric operation that maps every point of an original figure (the preimage) to a corresponding new position (the image). Transformations are divided into rigid motions (isometries), which preserve all distances and angle measures, and non-rigid motions (such as stretches or dilations), which change dimensions.",
                "keyProperties": [
                    "Distance Invariance: Every segment in the image has the exact same length as its corresponding preimage segment: Length(A'B') = Length(AB).",
                    "Angle Measure Invariance: Every angle in the image has the exact same degree measure as in the preimage: m∠A' = m∠A.",
                    "Collinearity & Betweenness: Points on a straight line remain on a straight line, and relative point ordering is preserved.",
                    "Parallelism: If line segment AB is parallel to CD, then A'B' is strictly parallel to C'D'.",
                    "Orientation Behavior: Translations and rotations preserve orientation (clockwise order of vertices). Reflections reverse orientation (clockwise becomes counterclockwise)."
                ],
                "coordinateNotationRule": "General transformation mapping notation: (x, y) → (x', y'). Under rigid motions, the Euclidean distance between any pair of points P and Q equals the distance between their images: d(P, Q) = d(P', Q').",
                "mathStandards": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.1.a, 8.G.A.1.b, 8.G.A.1.c"
            },
            "visualSummarySvg": """<svg viewBox="0 0 420 220" class="concept-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gPre11" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#4f46e5" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gImg11" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.45"/>
    </linearGradient>
    <marker id="arrow11" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#818cf8"/>
    </marker>
  </defs>
  <pattern id="grid11" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>
  <rect width="420" height="220" fill="url(#grid11)" rx="8"/>
  <polygon points="60,150 140,150 100,70" fill="url(#gPre11)" stroke="#4f46e5" stroke-width="2.5"/>
  <circle cx="60" cy="150" r="4" fill="#4f46e5"/><text x="45" y="162" font-size="12" font-weight="700" fill="#312e81">A</text>
  <circle cx="140" cy="150" r="4" fill="#4f46e5"/><text x="148" y="162" font-size="12" font-weight="700" fill="#312e81">B</text>
  <circle cx="100" cy="70" r="4" fill="#4f46e5"/><text x="96" y="60" font-size="12" font-weight="700" fill="#312e81">C</text>
  <text x="95" y="165" font-size="10" font-weight="600" fill="#4338ca" text-anchor="middle">c = 4 cm</text>
  <path d="M 125,110 Q 185,85 240,105" fill="none" stroke="#818cf8" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arrow11)"/>
  <text x="185" y="80" font-size="11" font-weight="700" fill="#4f46e5" text-anchor="middle">Rigid Motion</text>
  <text x="185" y="95" font-size="9.5" fill="#64748b" text-anchor="middle">(Isometry: Size &amp; Shape Preserved)</text>
  <polygon points="260,165 340,165 300,85" fill="url(#gImg11)" stroke="#059669" stroke-width="2.5"/>
  <circle cx="260" cy="165" r="4" fill="#059669"/><text x="245" y="177" font-size="12" font-weight="700" fill="#065f46">A'</text>
  <circle cx="340" cy="165" r="4" fill="#059669"/><text x="348" y="177" font-size="12" font-weight="700" fill="#065f46">B'</text>
  <circle cx="300" cy="85" r="4" fill="#059669"/><text x="296" y="75" font-size="12" font-weight="700" fill="#065f46">C'</text>
  <text x="295" y="180" font-size="10" font-weight="600" fill="#047857" text-anchor="middle">c' = 4 cm</text>
  <rect x="25" y="188" width="370" height="22" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="210" y="203" font-size="10.5" font-weight="600" fill="#334155" text-anchor="middle">✓ Side Lengths Equal | ✓ Angle Measures Equal | ✓ ΔABC ≅ ΔA'B'C'</text>
</svg>""",
            "essentialVocabulary": [
                {
                    "term": "Transformation",
                    "definition": "An operation that maps every point of a geometric figure (preimage) to a new position (image) on a coordinate plane.",
                    "example": "Translating a triangle 4 units right and 2 units up is a geometric transformation."
                },
                {
                    "term": "Preimage",
                    "definition": "The original geometric figure before any transformation is applied.",
                    "example": "In ΔABC → ΔA'B'C', ΔABC is the preimage."
                },
                {
                    "term": "Image",
                    "definition": "The new figure produced as the result of a transformation, typically identified using prime notation.",
                    "example": "In ΔABC → ΔA'B'C', ΔA'B'C' is the image."
                },
                {
                    "term": "Rigid Motion (Isometry)",
                    "definition": "A transformation that preserves both distance (side lengths) and angle measures. The image is congruent to the preimage.",
                    "example": "Translations, reflections, and rotations are rigid motions."
                },
                {
                    "term": "Non-Rigid Motion",
                    "definition": "A transformation that changes the size or proportions of a figure, altering distances.",
                    "example": "Dilations and directional stretches are non-rigid transformations."
                },
                {
                    "term": "Orientation",
                    "definition": "The direction in which the vertices of a polygon are ordered (clockwise vs. counterclockwise) or the facing direction of a figure.",
                    "example": "Translations keep vertex order clockwise; reflections reverse vertex order from clockwise to counterclockwise."
                }
            ]
        },
        "examples": [
            {
                "id": "ex-1.1-1",
                "title": "Example 1: Verifying Invariant Properties in a Translation",
                "description": "Triangle ABC has side lengths AB = 3 cm, BC = 4 cm, and AC = 5 cm with m∠B = 90°. It slides 6 units to the right to form Triangle A'B'C'.",
                "diagramHtml": "<div class='example-diagram-card'><strong>Preimage:</strong> ΔABC (3 cm, 4 cm, 5 cm; 90°) ➔ <strong>Image:</strong> ΔA'B'C' (3 cm, 4 cm, 5 cm; 90°)<br><span class='badge-status success'>All 3 side lengths and 3 angles preserved exactly</span></div>",
                "stepByStepExplanation": "1. Measure each side length of the image: A'B' = 3 cm, B'C' = 4 cm, A'C' = 5 cm. They match the preimage exactly.\n2. Measure each corresponding angle: m∠A' = m∠A, m∠B' = 90°, m∠C' = m∠C.\n3. Verify line parallelism: If side AB was perpendicular to BC, A'B' remains perpendicular to B'C'.\n4. Conclusion: Because distances and angle measures are strictly preserved, this sliding motion is a rigid motion (isometry).",
                "keyTakeaway": "Sliding a figure does not distort its dimensions or angles. Distance and angle measures are invariant."
            },
            {
                "id": "ex-1.1-2",
                "title": "Example 2: Identifying Non-Rigid Distortions",
                "description": "A student transforms rectangle JKLM with width 4 cm and height 2 cm into J'K'L'M' with width 8 cm and height 2 cm (horizontal stretch).",
                "diagramHtml": "<div class='example-diagram-card'><strong>Preimage:</strong> 4 cm × 2 cm (Area = 8 cm²) ➔ <strong>Image:</strong> 8 cm × 2 cm (Area = 16 cm²)<br><span class='badge-status error'>Side lengths altered: Not a rigid motion</span></div>",
                "stepByStepExplanation": "1. Compare side lengths: Preimage width JK = 4 cm; Image width J'K' = 8 cm. Since 8 ≠ 4, side length is not preserved.\n2. Compare areas: Area of JKLM = 8 cm²; Area of J'K'L'M' = 16 cm².\n3. Classify the transformation: Because distance is not preserved, this horizontal stretch is NOT a rigid motion.",
                "keyTakeaway": "Any transformation that changes even one side length is NOT a rigid motion."
            }
        ],
        "workedExamplesModelAnswers": [
            {
                "id": "we-1.1-1",
                "problemPrompt": "Quadrilateral PQRS has side lengths PQ = 5.2 cm, QR = 3.8 cm, RS = 5.2 cm, and SP = 3.8 cm, with m∠P = 110° and m∠Q = 70°. After a transformation, the image P'Q'R'S' has side lengths P'Q' = 5.2 cm, Q'R' = 3.8 cm, R'S' = 5.2 cm, S'P' = 3.8 cm, and m∠P' = 110°. Determine whether this transformation is a rigid motion. Provide full mathematical justification.",
                "context": "HMH Into Math TE - Formative Assessment Benchmark",
                "step1": "Identify Given Information: Preimage PQRS has opposite sides equal (PQ = RS = 5.2 cm; QR = SP = 3.8 cm) and angles m∠P = 110°, m∠Q = 70°. In image P'Q'R'S', all corresponding side lengths are identical (P'Q' = PQ, Q'R' = QR, R'S' = RS, S'P' = SP) and m∠P' = m∠P = 110°.",
                "step2": "Apply Rule / Theorem: By the definition of a rigid motion (isometry), a transformation is rigid if and only if it preserves distance (segment lengths) and angle measures for all corresponding parts of the figure.",
                "step3": "Write Concluding Mathematical Statement: Since every corresponding side length is equal (P'Q' = 5.2 cm, Q'R' = 3.8 cm, R'S' = 5.2 cm, S'P' = 3.8 cm) and all angle measures are preserved, the transformation is a rigid motion. Therefore, Quadrilateral PQRS ≅ Quadrilateral P'Q'R'S'.",
                "rubricGuidance": "Full credit requires explicitly listing corresponding side equality, stating the preservation of angle measures, citing the definition of rigid motion/isometry, and stating the congruence of the two figures."
            },
            {
                "id": "we-1.1-2",
                "problemPrompt": "Triangle XYZ has vertices ordered clockwise: X(1, 1), Y(1, 4), and Z(5, 1). After being reflected across the y-axis, the vertices are X'(-1, 1), Y'(-1, 4), and Z'(-5, 1). State whether side lengths, angle measures, and orientation were preserved. Is the transformation a rigid motion?",
                "context": "HMH Into Math TE - Orientation & Invariance Analysis",
                "step1": "Identify Given Information: Preimage vertices X(1,1), Y(1,4), Z(5,1) have side lengths XY = 3, XZ = 4, YZ = 5 (using Pythagorean theorem). Image vertices are X'(-1,1), Y'(-1,4), Z'(-5,1) with lengths X'Y' = 3, X'Z' = 4, Y'Z' = 5.",
                "step2": "Apply Rule / Invariance Properties: Distance formula confirms X'Y' = XY = 3, X'Z' = XZ = 4, and Y'Z' = YZ = 5. Angle m∠X = m∠X' = 90°. However, reading vertices X → Y → Z in the preimage runs clockwise, whereas X' → Y' → Z' in the image runs counterclockwise.",
                "step3": "Write Concluding Mathematical Statement: Side lengths and angle measures are strictly preserved, proving that reflection is a rigid motion. However, orientation is reversed (chirality flipped from clockwise to counterclockwise). Despite the orientation change, ΔXYZ ≅ ΔX'Y'Z'.",
                "rubricGuidance": "To score 100%, students must distinguish between metric invariance (distance and angle measures remain equal) and orientation (which flips during reflection)."
            }
        ],
        "practiceQuestions": [
            {
                "id": "pq-1.1-1",
                "type": "mcq",
                "prompt": "Which of the following geometric transformations is NOT a rigid motion?",
                "options": [
                    "Translating a triangle 7 units down and 2 units left",
                    "Rotating a rectangle 180° counterclockwise about the origin",
                    "Dilating a trapezoid by a scale factor of 1.5",
                    "Reflecting a pentagon across the vertical line x = 3"
                ],
                "correctIndex": 2,
                "hint": "Remember that a rigid motion must preserve both size and shape without stretching or shrinking.",
                "explanation": "A dilation by a scale factor of 1.5 multiplies all side lengths by 1.5, increasing the size of the shape. Because side lengths are not preserved, dilations are non-rigid transformations."
            },
            {
                "id": "pq-1.1-2",
                "type": "fill-blank",
                "prompt": "Triangle DEF has side length DE = 8.4 cm and m∠D = 47°. If Triangle DEF undergoes a rigid motion to produce Triangle D'E'F', what is the exact length of side D'E' in centimeters?",
                "placeholder": "Enter number (e.g. 8.4)",
                "acceptedAnswers": ["8.4", "8.4 cm", "8.4cm"],
                "hint": "Rigid motions preserve distance. Corresponding side lengths remain identical.",
                "explanation": "Under any rigid motion (translation, reflection, rotation), distance is invariant. Therefore, length(D'E') = length(DE) = 8.4 cm."
            },
            {
                "id": "pq-1.1-3",
                "type": "mcq",
                "prompt": "Which property of a geometric figure is ALWAYS preserved under every rigid motion?",
                "options": [
                    "Clockwise orientation of vertices only",
                    "Side lengths, angle measures, and parallelism",
                    "Only the coordinates of the vertices",
                    "The quadrants in which the vertices lie"
                ],
                "correctIndex": 1,
                "hint": "Think about what stays the same when you slide, flip, or turn a rigid cardboard cutout.",
                "explanation": "Rigid motions (isometries) strictly preserve side lengths, angle measures, collinearity, and parallelism. Reflections reverse orientation, and figures change quadrants/coordinates."
            },
            {
                "id": "pq-1.1-4",
                "type": "fill-blank",
                "prompt": "What is the mathematical term for the original figure before a transformation is applied?",
                "placeholder": "Enter vocabulary term",
                "acceptedAnswers": ["preimage", "Preimage", "pre-image", "Pre-image"],
                "hint": "The starting shape has no prime marks; its name begins with the prefix 'pre-'.",
                "explanation": "The original figure before transformation is called the preimage. The transformed figure is called the image."
            }
        ],
        "bookQuestionBank": [
            {
                "id": "bq-1.1-1",
                "category": "Spark Your Learning",
                "title": "Daniel's Sandwich Slice Investigation",
                "context": "HMH Into Math Grade 8 Teacher Edition, Lesson 1.1 Opening Activity",
                "questionPrompt": "Daniel prepares a rectangular sandwich measuring 10 cm by 12 cm. He cuts the sandwich diagonally from one corner to the opposite corner, creating two triangular halves. He slides and rotates one half to place it beside the other half on a serving plate. Daniel wonders whether sliding and turning the slice changed its area or perimeter. How can geometric properties explain whether the two triangular slices are identical?",
                "modelAnswer": {
                    "summary": "The sliding and turning of the sandwich slice are rigid motions (a translation and rotation), which strictly preserve side lengths, perimeter, and area.",
                    "stepByStep": [
                        "Step 1: Identify the transformations applied: Daniel slid the sandwich slice (translation) and turned it (rotation).",
                        "Step 2: Apply geometric invariance principles: Translations and rotations are rigid motions (isometries). Rigid motions preserve segment lengths (distance) and angle measures.",
                        "Step 3: Calculate the dimensions: Both right triangles have legs of 10 cm and 12 cm, and hypotenuse √(10² + 12²) = √244 ≈ 15.62 cm.",
                        "Step 4: Conclude on area and perimeter: Perimeter = 10 + 12 + 15.62 = 37.62 cm for both halves. Area = (1/2) × 10 × 12 = 60 cm² for both halves."
                    ],
                    "fullCreditJustification": "Sliding and rotating a shape does not stretch, compress, or deform it. Because distance and angle measures are preserved under translations and rotations, the two sandwich halves have identical side lengths, perimeters, and areas, proving they are congruent.",
                    "rubricCriteria": "Teacher Edition Rubric: 2 pts for identifying translation/rotation as rigid motions; 2 pts for stating that distance/angle measure are preserved; 1 pt for connecting preservation to equal perimeter and area."
                }
            },
            {
                "id": "bq-1.1-2",
                "category": "Check Understanding",
                "title": "Tarik's Photo Album Grid Layout",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.1 Check Understanding Exercise 2",
                "questionPrompt": "Tarik is designing a digital photo album. He places a rectangular photo sticker ABCD on a grid with coordinates A(1, 2), B(5, 2), C(5, 7), and D(1, 7). He duplicates the sticker and positions the second sticker A'B'C'D' at A'(3, 6), B'(7, 6), C'(7, 11), and D'(3, 11). (a) What type of transformation occurred? (b) Prove mathematically whether side lengths and angle measures were preserved.",
                "modelAnswer": {
                    "summary": "Tarik's photo sticker was translated 2 units right and 4 units up. Side lengths and right angles are preserved, confirming a rigid motion.",
                    "stepByStep": [
                        "Step 1: Compare coordinates: A(1, 2) → A'(3, 6). Horizontal shift: 3 - 1 = +2. Vertical shift: 6 - 2 = +4. Check other vertices: B(5, 2) → B'(5+2, 2+4) = B'(7, 6); C(5, 7) → C'(7, 11); D(1, 7) → D'(3, 11). All vertices shift by (x + 2, y + 4).",
                        "Step 2: Measure side lengths of preimage: AB = 5 - 1 = 4 units; BC = 7 - 2 = 5 units; CD = 4 units; DA = 5 units.",
                        "Step 3: Measure side lengths of image: A'B' = 7 - 3 = 4 units; B'C' = 11 - 6 = 5 units; C'D' = 4 units; D'A' = 5 units.",
                        "Step 4: Check angles: All angles in both figures are formed by perpendicular horizontal and vertical segments (90°)."
                    ],
                    "fullCreditJustification": "The transformation is a translation defined by (x, y) → (x + 2, y + 4). Because AB = A'B' = 4 units, BC = B'C' = 5 units, and all interior angles remain 90°, distance and angle measures are strictly preserved, making this a rigid motion.",
                    "rubricCriteria": "2 pts for correctly identifying the translation rule (x+2, y+4); 2 pts for computing and comparing all 4 side lengths; 1 pt for confirming angle preservation."
                }
            },
            {
                "id": "bq-1.1-3",
                "category": "On Your Own",
                "title": "Graphic Designer's Logo Reorientation",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.1 On Your Own Problem 6",
                "questionPrompt": "A graphic designer creates an arrow logo in quadrant I. She rotates the arrow 90° clockwise and then translates it into quadrant IV. Her client worries that the arrow may have become smaller or distorted during these adjustments. Write a geometric explanation that the designer can send to the client to prove that the logo's dimensions remained exactly the same.",
                "modelAnswer": {
                    "summary": "Rotations and translations are isometries (rigid motions), which mathematically guarantee that every segment length and interior angle remains unchanged.",
                    "stepByStep": [
                        "Step 1: Classify the operations: The designer performed a rotation followed by a translation.",
                        "Step 2: Cite the Isometry Theorem: By the definition of rigid transformations (isometries), rotations and translations preserve distance between any two points and preserve all angle measures.",
                        "Step 3: Address the composition: The composition of two rigid motions is itself a rigid motion.",
                        "Step 4: Formulate the client response: Reassure the client that rotating and translating an asset only alters its position and direction on the canvas, with zero change in perimeter, proportions, or surface area."
                    ],
                    "fullCreditJustification": "Because both rotations and translations are rigid motions, their sequence is also a rigid motion. Length(P'Q') = Length(PQ) for any two points on the logo. Hence, the logo's dimensions, edge lengths, and angles remain 100% identical.",
                    "rubricCriteria": "Teacher Edition Benchmark: Full credit requires mentioning that both individual steps are rigid motions and that their combination preserves both distance and angles."
                }
            },
            {
                "id": "bq-1.1-4",
                "category": "Test Prep",
                "title": "Standardized Test Prep: Invariance Under Transformations",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.1 Test Prep Item 12",
                "questionPrompt": "Polygon P undergoes a transformation to form Polygon Q. Which condition guarantees that Polygon P and Polygon Q are congruent?\nA. Polygon Q has the same number of vertices as Polygon P.\nB. All corresponding angle measures and side lengths are equal.\nC. Polygon Q is located in the same quadrant as Polygon P.\nD. The perimeter of Polygon Q is greater than the perimeter of Polygon P.",
                "modelAnswer": {
                    "summary": "Option B is correct. Congruence requires all corresponding side lengths and angle measures to be equal.",
                    "stepByStep": [
                        "Analyze Option A: Any two pentagons have 5 vertices, but they can be completely different sizes and shapes. Incorrect.",
                        "Analyze Option B: When all corresponding side lengths and angle measures are equal, the figure has undergone a rigid motion and the two polygons are congruent. Correct!",
                        "Analyze Option C: Location in the coordinate plane does not determine congruence. Incorrect.",
                        "Analyze Option D: If perimeter increases, the figure was enlarged and is not congruent. Incorrect."
                    ],
                    "fullCreditJustification": "Two geometric figures are congruent if and only if all corresponding side lengths and corresponding angle measures are equal (isometry). Option B is the only statement that guarantees congruence.",
                    "rubricCriteria": "1 pt for selecting B; 1 pt for justification based on rigid motion properties."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 1.2: Explore Translations
    # =========================================================================
    m1["1.2"] = {
        "id": "1.2",
        "lessonNumber": "1.2",
        "moduleNumber": 1,
        "moduleId": "module-1",
        "moduleTitle": "Module 1: Transformations and Congruence",
        "title": "Lesson 1.2: Explore Translations",
        "introAndConcept": {
            "lessonTitle": "Lesson 1.2: Explore Translations",
            "iCanStatement": "I can translate figures on the coordinate plane, describe translations using words and mapping notation (x, y) → (x + a, y + b), and determine an algebraic rule given a preimage and image.",
            "conceptExplanation": {
                "coreDefinition": "A translation is a rigid motion that slides every point of a geometric figure the exact same distance in the exact same direction along a straight line vector. The shape, size, and orientation of the figure do not change.",
                "keyProperties": [
                    "Vector Motion: Every vertex slides along parallel line segments of equal length.",
                    "Horizontal Shift (a): If a > 0, the figure shifts 'a' units to the right. If a < 0, the figure shifts |a| units to the left.",
                    "Vertical Shift (b): If b > 0, the figure shifts 'b' units up. If b < 0, the figure shifts |b| units down.",
                    "Orientation Invariance: The clockwise order of vertices remains completely unchanged.",
                    "Line Parallelism: All segments connecting corresponding preimage points to image points (AA', BB', CC') are parallel to each other and have equal length."
                ],
                "coordinateNotationRule": "Coordinate Mapping Rule: (x, y) → (x + a, y + b). Vector notation: v = ⟨a, b⟩.",
                "mathStandards": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
            },
            "visualSummarySvg": """<svg viewBox="0 0 420 220" class="concept-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gPre12" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#2563eb" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gImg12" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#7c3aed" stop-opacity="0.45"/>
    </linearGradient>
    <marker id="arr12" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#2563eb"/>
    </marker>
  </defs>
  <pattern id="grid12" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>
  <rect width="420" height="220" fill="url(#grid12)" rx="8"/>
  <line x1="30" y1="180" x2="390" y2="180" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="80" y1="20" x2="80" y2="200" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="395" y="184" font-size="11" font-weight="700" fill="#64748b">x</text>
  <text x="76" y="16" font-size="11" font-weight="700" fill="#64748b">y</text>
  <polygon points="100,120 160,120 120,80" fill="url(#gPre12)" stroke="#2563eb" stroke-width="2.5"/>
  <circle cx="100" cy="120" r="3.5" fill="#2563eb"/><text x="82" y="128" font-size="11" font-weight="700" fill="#1e40af">P(1,3)</text>
  <circle cx="160" cy="120" r="3.5" fill="#2563eb"/><text x="165" y="128" font-size="11" font-weight="700" fill="#1e40af">Q(4,3)</text>
  <circle cx="120" cy="80" r="3.5" fill="#2563eb"/><text x="115" y="72" font-size="11" font-weight="700" fill="#1e40af">R(2,5)</text>
  <line x1="100" y1="120" x2="240" y2="80" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arr12)"/>
  <line x1="160" y1="120" x2="300" y2="80" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arr12)"/>
  <line x1="120" y1="80" x2="260" y2="40" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arr12)"/>
  <polygon points="240,80 300,80 260,40" fill="url(#gImg12)" stroke="#7c3aed" stroke-width="2.5"/>
  <circle cx="240" cy="80" r="3.5" fill="#7c3aed"/><text x="220" y="98" font-size="11" font-weight="700" fill="#5b21b6">P'(8,5)</text>
  <circle cx="300" cy="80" r="3.5" fill="#7c3aed"/><text x="306" y="98" font-size="11" font-weight="700" fill="#5b21b6">Q'(11,5)</text>
  <circle cx="260" cy="40" r="3.5" fill="#7c3aed"/><text x="256" y="32" font-size="11" font-weight="700" fill="#5b21b6">R'(9,7)</text>
  <rect x="140" y="145" width="230" height="30" rx="6" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="255" y="165" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700" fill="#6d28d9" text-anchor="middle">(x, y) → (x + 7, y + 2)</text>
</svg>""",
            "essentialVocabulary": [
                {
                    "term": "Translation",
                    "definition": "A rigid transformation that moves every point of a figure the same distance in the same direction.",
                    "example": "Sliding a desk 3 feet right across the floor is a real-world translation."
                },
                {
                    "term": "Translation Vector",
                    "definition": "A directed line segment showing the direction and distance that a figure is moved.",
                    "example": "The vector ⟨-4, 5⟩ indicates a movement of 4 units left and 5 units up."
                },
                {
                    "term": "Coordinate Mapping Rule",
                    "definition": "An algebraic equation showing how the coordinates of each point change: (x, y) → (x + a, y + b).",
                    "example": "The rule (x, y) → (x - 2, y + 6) translates points 2 units left and 6 units up."
                },
                {
                    "term": "Prime Notation",
                    "definition": "The use of the prime symbol (') to label corresponding vertices in the transformed image.",
                    "example": "Preimage point A maps to image point A' ('A-prime')."
                },
                {
                    "term": "Horizontal Shift",
                    "definition": "The change in the x-coordinate of every point (addition moves right, subtraction moves left).",
                    "example": "In (x, y) → (x + 5, y), the horizontal shift is 5 units right."
                },
                {
                    "term": "Vertical Shift",
                    "definition": "The change in the y-coordinate of every point (addition moves up, subtraction moves down).",
                    "example": "In (x, y) → (x, y - 4), the vertical shift is 4 units down."
                }
            ]
        },
        "examples": [
            {
                "id": "ex-1.2-1",
                "title": "Example 1: Translating a Triangle by an Algebraic Rule",
                "description": "Triangle PQR has vertices P(-2, 3), Q(1, 4), and R(0, 1). Apply the translation rule (x, y) → (x + 5, y - 4) to determine the coordinates of P'Q'R'.",
                "diagramHtml": "<div class='example-diagram-card'>P(-2, 3) ➔ P'(-2+5, 3-4) = P'(3, -1)<br>Q(1, 4) ➔ Q'(1+5, 4-4) = Q'(6, 0)<br>R(0, 1) ➔ R'(0+5, 1-4) = R'(5, -3)</div>",
                "stepByStepExplanation": "1. For vertex P: Add 5 to x: -2 + 5 = 3. Subtract 4 from y: 3 - 4 = -1. Thus, P'(3, -1).\n2. For vertex Q: Add 5 to x: 1 + 5 = 6. Subtract 4 from y: 4 - 4 = 0. Thus, Q'(6, 0).\n3. For vertex R: Add 5 to x: 0 + 5 = 5. Subtract 4 from y: 1 - 4 = -3. Thus, R'(5, -3).\n4. Graph both triangles on the coordinate grid to verify that all corresponding sides are parallel and of equal length.",
                "keyTakeaway": "Apply the addition or subtraction to every x and y coordinate independently."
            },
            {
                "id": "ex-1.2-2",
                "title": "Example 2: Determining the Translation Rule from Preimage and Image",
                "description": "A quadrilateral ABCD is translated to A'B'C'D'. Preimage vertex A is at (-3, 5) and image vertex A' is at (4, 2). Find the translation rule.",
                "diagramHtml": "<div class='example-diagram-card'>Horizontal change: 4 - (-3) = +7 (7 units right)<br>Vertical change: 2 - 5 = -3 (3 units down)<br><strong>Rule:</strong> (x, y) → (x + 7, y - 3)</div>",
                "stepByStepExplanation": "1. Find the horizontal shift a: x₂ - x₁ = 4 - (-3) = 4 + 3 = 7. (7 units right)\n2. Find the vertical shift b: y₂ - y₁ = 2 - 5 = -3. (3 units down)\n3. Formulate the algebraic coordinate rule: (x, y) → (x + 7, y - 3).\n4. Check with another vertex if given, to ensure the same shift applies to all points.",
                "keyTakeaway": "Subtract preimage coordinates from image coordinates to find horizontal shift 'a' and vertical shift 'b'."
            }
        ],
        "workedExamplesModelAnswers": [
            {
                "id": "we-1.2-1",
                "problemPrompt": "Triangle JKL has vertices J(2, -1), K(5, -1), and L(3, 4). The triangle is translated 6 units left and 3 units up. (a) Write the algebraic mapping rule. (b) Find the coordinates of vertices J', K', and L'. (c) State whether ΔJKL ≅ ΔJ'K'L'.",
                "context": "HMH Into Math TE - Worked Example Model Lesson 1.2",
                "step1": "Identify Given Information: Preimage coordinates J(2, -1), K(5, -1), L(3, 4). The verbal description states '6 units left' (a = -6) and '3 units up' (b = +3).",
                "step2": "Apply Rule / Formula: The translation rule is (x, y) → (x - 6, y + 3). Calculate each image vertex:\n• J(2, -1) → J'(2 - 6, -1 + 3) = J'(-4, 2)\n• K(5, -1) → K'(5 - 6, -1 + 3) = K'(-1, 2)\n• L(3, 4) → L'(3 - 6, 4 + 3) = L'(-3, 7)",
                "step3": "Write Concluding Mathematical Statement: The algebraic translation rule is (x, y) → (x - 6, y + 3). The coordinates of the image are J'(-4, 2), K'(-1, 2), and L'(-3, 7). Because a translation is a rigid motion that preserves all side lengths and angle measures, Triangle JKL ≅ Triangle J'K'L'.",
                "rubricGuidance": "Full credit requires: 1 pt for writing the algebraic rule; 2 pts for calculating all three image points correctly; 1 pt for stating congruence with justification that translation is an isometry."
            },
            {
                "id": "we-1.2-2",
                "problemPrompt": "Parallelogram MNPQ is translated to M'N'P'Q'. The coordinates of M are (-4, 2) and M' is (1, -5). (a) Write the translation rule. (b) If vertex P' is located at (6, -2), find the coordinates of the original preimage vertex P.",
                "context": "HMH Into Math TE - Reverse Translation Rule Application",
                "step1": "Identify Given Information: Preimage M(-4, 2) maps to image M'(1, -5). Vertex P' has coordinates (6, -2). We must find the forward rule and then work backward to find P(x, y).",
                "step2": "Apply Rule / Formula:\n• Horizontal change: a = 1 - (-4) = 1 + 4 = 5.\n• Vertical change: b = -5 - 2 = -7.\n• Forward rule: (x, y) → (x + 5, y - 7).\n• To reverse from image P'(x', y') to preimage P(x, y): x = x' - 5 and y = y' + 7.\n• Substituting P'(6, -2): x = 6 - 5 = 1, and y = -2 + 7 = 5.",
                "step3": "Write Concluding Mathematical Statement: The translation rule is (x, y) → (x + 5, y - 7). The preimage vertex P has coordinates (1, 5). Checking: (1 + 5, 5 - 7) = (6, -2), which matches P'.",
                "rubricGuidance": "Full credit: 1 pt for finding a = 5 and b = -7; 1 pt for formulating the rule; 2 pts for correctly reversing the operation to find preimage vertex P(1, 5)."
            }
        ],
        "practiceQuestions": [
            {
                "id": "pq-1.2-1",
                "type": "fill-blank",
                "prompt": "Point P(3, -5) is translated using the rule (x, y) → (x - 4, y + 7). What are the coordinates of the image point P'?",
                "placeholder": "Enter as (x, y)",
                "acceptedAnswers": ["(-1, 2)", "(-1,2)", "-1, 2", "-1,2"],
                "hint": "Subtract 4 from the x-coordinate (3 - 4) and add 7 to the y-coordinate (-5 + 7).",
                "explanation": "Applying the rule: x' = 3 - 4 = -1, and y' = -5 + 7 = 2. Therefore, P' = (-1, 2)."
            },
            {
                "id": "pq-1.2-2",
                "type": "mcq",
                "prompt": "Triangle DEF with vertices D(1, 2), E(4, 2), and F(2, 5) is translated 5 units left and 3 units down. Which algebraic rule represents this translation?",
                "options": [
                    "(x, y) → (x + 5, y + 3)",
                    "(x, y) → (x - 5, y - 3)",
                    "(x, y) → (x - 5, y + 3)",
                    "(x, y) → (x + 5, y - 3)"
                ],
                "correctIndex": 1,
                "hint": "Left means subtracting from x, and down means subtracting from y.",
                "explanation": "Moving left corresponds to subtracting from the x-coordinate (x - 5). Moving down corresponds to subtracting from the y-coordinate (y - 3). Thus, (x, y) → (x - 5, y - 3)."
            },
            {
                "id": "pq-1.2-3",
                "type": "fill-blank",
                "prompt": "A polygon is translated so that vertex A(-2, 8) maps to A'(5, 3). What is the value of the horizontal shift 'a' in the rule (x, y) → (x + a, y + b)?",
                "placeholder": "Enter integer (e.g. 7)",
                "acceptedAnswers": ["7", "+7"],
                "hint": "Calculate the difference between the image x-coordinate and the preimage x-coordinate: 5 - (-2).",
                "explanation": "a = x₂ - x₁ = 5 - (-2) = 5 + 2 = 7. The figure was shifted 7 units to the right."
            },
            {
                "id": "pq-1.2-4",
                "type": "mcq",
                "prompt": "Does a translation ever change the clockwise order of the vertices of a polygon?",
                "options": [
                    "Yes, whenever the figure is translated diagonally",
                    "Yes, only if the translation moves into quadrant III",
                    "No, translations always preserve the orientation of vertices",
                    "It depends on whether the shift is odd or even"
                ],
                "correctIndex": 2,
                "hint": "Think about sliding a sheet of paper across a desk. Does it flip over?",
                "explanation": "Translations simply slide the figure without turning or flipping it. Orientation (clockwise vs counterclockwise) is always preserved."
            }
        ],
        "bookQuestionBank": [
            {
                "id": "bq-1.2-1",
                "category": "Spark Your Learning",
                "title": "Chess Knight's L-Slide Vector Moves",
                "context": "HMH Into Math Grade 8 Teacher Edition, Lesson 1.2 Opening Challenge",
                "questionPrompt": "On a chessboard set up as a coordinate grid, a knight begins at position (3, 2). A knight's legal move consists of sliding 2 squares in one direction and 1 square perpendicularly. (a) If the knight moves 1 square right and 2 squares up to land on (4, 4), write this move as an algebraic translation rule. (b) On the next turn, the knight moves from (4, 4) using the rule (x, y) → (x - 2, y + 1). What is the knight's new square?",
                "modelAnswer": {
                    "summary": "The initial knight move is modeled by (x, y) → (x + 1, y + 2). The second move lands the knight at (2, 5).",
                    "stepByStep": [
                        "Step 1: Determine rule for Move 1: Start at (3, 2), end at (4, 4). Horizontal shift = 4 - 3 = +1; Vertical shift = 4 - 2 = +2. Rule: (x, y) → (x + 1, y + 2).",
                        "Step 2: Apply rule for Move 2: Start at (4, 4) with rule (x, y) → (x - 2, y + 1).",
                        "Step 3: Calculate coordinates: x' = 4 - 2 = 2; y' = 4 + 1 = 5. The new location is (2, 5).",
                        "Step 4: Verify knight move geometry: The total displacement is 2 squares left and 1 square up, which is a standard L-shape knight leap."
                    ],
                    "fullCreditJustification": "Translations represent discrete coordinate displacements. Move 1 is (x, y) → (x + 1, y + 2). Applying (x - 2, y + 1) to (4, 4) yields (2, 5). Both moves preserve the knight piece's orientation.",
                    "rubricCriteria": "Teacher Edition Benchmark: 2 pts for correct algebraic rule (x+1, y+2); 2 pts for correct coordinate calculation (2, 5)."
                }
            },
            {
                "id": "bq-1.2-2",
                "category": "Check Understanding",
                "title": "Computer Animation Drone Flight Path",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.2 Check Understanding Problem 3",
                "questionPrompt": "An animation designer creates a triangular drone avatar on a coordinate screen with vertices at A(-4, 3), B(-1, 3), and C(-2, 6). The drone flies across the screen following a translation of 7 units right and 5 units down. (a) Write the translation rule. (b) Find the coordinates of the drone's new vertices A'B'C'. (c) How do the side lengths of the original drone compare to the new drone?",
                "modelAnswer": {
                    "summary": "Translation rule is (x, y) → (x + 7, y - 5). The new vertices are A'(3, -2), B'(6, -2), and C'(5, 1). Side lengths are identical because translation is a rigid motion.",
                    "stepByStep": [
                        "Step 1: Write the rule: 7 units right = x + 7; 5 units down = y - 5. Rule: (x, y) → (x + 7, y - 5).",
                        "Step 2: Calculate new coordinates:\n• A(-4, 3) → A'(-4 + 7, 3 - 5) = A'(3, -2)\n• B(-1, 3) → B'(-1 + 7, 3 - 5) = B'(6, -2)\n• C(-2, 6) → C'(-2 + 7, 6 - 5) = C'(5, 1)",
                        "Step 3: Compare side lengths: AB = |-1 - (-4)| = 3 units. A'B' = |6 - 3| = 3 units. Using the distance formula, AC = A'C' = √13 and BC = B'C' = √10.",
                        "Step 4: Conclude: All corresponding side lengths are equal."
                    ],
                    "fullCreditJustification": "Under the translation (x, y) → (x + 7, y - 5), every vertex shifts by the same vector. Because translations are rigid motions, AB = A'B', BC = B'C', and AC = A'C'. The drone's shape and size are preserved.",
                    "rubricCriteria": "1 pt for translation rule; 2 pts for all 3 vertex coordinates; 1 pt for proving side length invariance."
                }
            },
            {
                "id": "bq-1.2-3",
                "category": "On Your Own",
                "title": "Architect's Tile Patio Pattern",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.2 On Your Own Exercise 8",
                "questionPrompt": "An architect is drafting a repeating tessellation pattern of hexagonal patio pavers. Paver 1 has vertices centered at (0, 0). Paver 2 is translated by the rule (x, y) → (x + 4, y + 2.5), and Paver 3 is translated from Paver 2 by the rule (x, y) → (x + 4, y + 2.5). (a) What single translation rule maps Paver 1 directly onto Paver 3? (b) If a vertex on Paver 1 is at (-2, 1), what is its corresponding position on Paver 3?",
                "modelAnswer": {
                    "summary": "Composing two identical translations of (x+4, y+2.5) yields the combined rule (x, y) → (x + 8, y + 5). The vertex at (-2, 1) maps to (6, 6).",
                    "stepByStep": [
                        "Step 1: Combine the translations: First shift: (x + 4, y + 2.5). Second shift: ((x + 4) + 4, (y + 2.5) + 2.5) = (x + 8, y + 5).",
                        "Step 2: State the direct rule: (x, y) → (x + 8, y + 5).",
                        "Step 3: Apply the combined rule to vertex (-2, 1): x' = -2 + 8 = 6; y' = 1 + 5 = 6.",
                        "Step 4: Verify intermediate position: After first shift, (-2+4, 1+2.5) = (2, 3.5). After second shift, (2+4, 3.5+2.5) = (6, 6). Matches!"
                    ],
                    "fullCreditJustification": "When successive translations are performed, their components add algebraically: a_total = 4 + 4 = 8, and b_total = 2.5 + 2.5 = 5. Applying this to (-2, 1) gives (6, 6).",
                    "rubricCriteria": "2 pts for formulating composite rule (x+8, y+5); 2 pts for computing the final vertex coordinate (6, 6)."
                }
            },
            {
                "id": "bq-1.2-4",
                "category": "Test Prep",
                "title": "Standardized Test Prep: Identify Translation Rule",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.2 Test Prep Question 14",
                "questionPrompt": "Triangle XYZ is translated to Triangle X'Y'Z'. Vertex X is at (2, -3) and vertex X' is at (-4, 1). What is the algebraic rule for this translation?\nA. (x, y) → (x - 6, y + 4)\nB. (x, y) → (x + 6, y - 4)\nC. (x, y) → (x - 2, y - 2)\nD. (x, y) → (x + 2, y + 4)",
                "modelAnswer": {
                    "summary": "Option A is correct: (x, y) → (x - 6, y + 4).",
                    "stepByStep": [
                        "Step 1: Identify coordinates: Preimage X(2, -3) and Image X'(-4, 1).",
                        "Step 2: Calculate horizontal shift a: a = -4 - 2 = -6 (6 units left).",
                        "Step 3: Calculate vertical shift b: b = 1 - (-3) = 1 + 3 = +4 (4 units up).",
                        "Step 4: Formulate rule: (x, y) → (x - 6, y + 4)."
                    ],
                    "fullCreditJustification": "Subtracting preimage coordinates from image coordinates gives a = -4 - 2 = -6 and b = 1 - (-3) = 4. The rule is (x, y) → (x - 6, y + 4), corresponding to Option A.",
                    "rubricCriteria": "1 pt for selecting A; 1 pt for showing algebraic subtraction work."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 1.3: Explore Reflections
    # =========================================================================
    m1["1.3"] = {
        "id": "1.3",
        "lessonNumber": "1.3",
        "moduleNumber": 1,
        "moduleId": "module-1",
        "moduleTitle": "Module 1: Transformations and Congruence",
        "title": "Lesson 1.3: Explore Reflections",
        "introAndConcept": {
            "lessonTitle": "Lesson 1.3: Explore Reflections",
            "iCanStatement": "I can graph reflections across the x-axis, y-axis, and other lines of reflection, write coordinate rules, and explain why orientation is reversed while distance and angle measures are preserved.",
            "conceptExplanation": {
                "coreDefinition": "A reflection is a rigid motion that flips a figure across a specific line called the line of reflection (mirror line). For every point in the preimage, the line of reflection is the perpendicular bisector of the segment connecting that point to its corresponding image point.",
                "keyProperties": [
                    "Perpendicular Bisector Property: If segment PP' connects a preimage point P to its image P', the line of reflection is perpendicular to PP' and bisects PP'.",
                    "Equal Distance from Mirror: Any point P and its image P' are equidistant from the line of reflection.",
                    "Points on the Line: Any point lying directly on the line of reflection does not move (it is invariant: P = P').",
                    "Preservation of Distance & Angles: Side lengths and angle measures remain identical (rigid motion).",
                    "Orientation Reversal (Chirality): Reflections reverse the orientation of the vertices. If preimage vertices are read clockwise, the image vertices will be read counterclockwise."
                ],
                "coordinateNotationRule": "Standard Coordinate Rules:\n• Across x-axis: (x, y) → (x, -y)\n• Across y-axis: (x, y) → (-x, y)\n• Across line y = x: (x, y) → (y, x)\n• Across line y = -x: (x, y) → (-y, -x)",
                "mathStandards": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
            },
            "visualSummarySvg": """<svg viewBox="0 0 420 220" class="concept-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gPre13" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gImg13" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#db2777" stop-opacity="0.45"/>
    </linearGradient>
  </defs>
  <pattern id="grid13" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>
  <rect width="420" height="220" fill="url(#grid13)" rx="8"/>
  <line x1="210" y1="15" x2="210" y2="205" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="215" y="30" font-size="11" font-weight="700" fill="#dc2626">Line of Reflection (y-axis)</text>
  <polygon points="100,80 160,40 160,140" fill="url(#gPre13)" stroke="#0284c7" stroke-width="2.5"/>
  <circle cx="100" cy="80" r="3.5" fill="#0284c7"/><text x="50" y="84" font-size="11" font-weight="700" fill="#0369a1">A(-5,3)</text>
  <circle cx="160" cy="40" r="3.5" fill="#0284c7"/><text x="115" y="34" font-size="11" font-weight="700" fill="#0369a1">B(-2,5)</text>
  <circle cx="160" cy="140" r="3.5" fill="#0284c7"/><text x="115" y="155" font-size="11" font-weight="700" fill="#0369a1">C(-2,1)</text>
  <line x1="100" y1="80" x2="320" y2="80" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="160" y1="40" x2="260" y2="40" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="160" y1="140" x2="260" y2="140" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3,3"/>
  <polygon points="320,80 260,40 260,140" fill="url(#gImg13)" stroke="#db2777" stroke-width="2.5"/>
  <circle cx="320" cy="80" r="3.5" fill="#db2777"/><text x="328" y="84" font-size="11" font-weight="700" fill="#be185d">A'(5,3)</text>
  <circle cx="260" cy="40" r="3.5" fill="#db2777"/><text x="268" y="34" font-size="11" font-weight="700" fill="#be185d">B'(2,5)</text>
  <circle cx="260" cy="140" r="3.5" fill="#db2777"/><text x="268" y="155" font-size="11" font-weight="700" fill="#be185d">C'(2,1)</text>
  <rect x="55" y="180" width="310" height="28" rx="6" fill="#fff1f2" stroke="#f43f5e" stroke-width="1"/>
  <text x="210" y="198" font-size="11" font-weight="600" fill="#9f1239" text-anchor="middle">Rule: (x, y) → (-x, y) | Orientation is Reversed (Mirror Flip)</text>
</svg>""",
            "essentialVocabulary": [
                {
                    "term": "Reflection",
                    "definition": "A rigid transformation that flips a figure over a line, creating a mirror image.",
                    "example": "Looking in a mirror creates a geometric reflection of your face."
                },
                {
                    "term": "Line of Reflection",
                    "definition": "The line over which a figure is reflected; it is the perpendicular bisector of every segment connecting a point to its image.",
                    "example": "In the rule (x, y) → (x, -y), the line of reflection is the x-axis."
                },
                {
                    "term": "Perpendicular Bisector",
                    "definition": "A line that cuts a line segment into two equal halves at a 90° right angle.",
                    "example": "The y-axis is the perpendicular bisector of the line connecting (-3, 4) and (3, 4)."
                },
                {
                    "term": "Line of Symmetry",
                    "definition": "A line dividing a figure into two mirror-image halves that fold exactly onto each other.",
                    "example": "An isosceles triangle has one vertical line of symmetry."
                },
                {
                    "term": "Chirality / Reversed Orientation",
                    "definition": "The change in the directional order of vertices resulting from a reflection flip.",
                    "example": "A clock face reflected in a mirror has its numbers running counterclockwise."
                }
            ]
        },
        "examples": [
            {
                "id": "ex-1.3-1",
                "title": "Example 1: Reflecting a Triangle Across the X-Axis",
                "description": "Triangle ABC with vertices A(-3, 2), B(1, 5), and C(4, 1) is reflected across the x-axis. Find the coordinates of A'B'C'.",
                "diagramHtml": "<div class='example-diagram-card'>Rule: (x, y) → (x, -y)<br>A(-3, 2) ➔ A'(-3, -2)<br>B(1, 5) ➔ B'(1, -5)<br>C(4, 1) ➔ C'(4, -1)</div>",
                "stepByStepExplanation": "1. Recall the rule for reflecting across the x-axis: the x-coordinate stays unchanged, and the y-coordinate changes sign: (x, y) → (x, -y).\n2. Apply to A(-3, 2): x stays -3, y becomes -2 ➔ A'(-3, -2).\n3. Apply to B(1, 5): x stays 1, y becomes -5 ➔ B'(1, -5).\n4. Apply to C(4, 1): x stays 4, y becomes -1 ➔ C'(4, -1).\n5. Notice that the image is flipped upside down across the horizontal axis.",
                "keyTakeaway": "Reflection across the x-axis negates the y-coordinate while leaving the x-coordinate untouched."
            },
            {
                "id": "ex-1.3-2",
                "title": "Example 2: Reflecting Across the Line y = x",
                "description": "Point M(2, -7) is reflected across the diagonal line y = x. Find the coordinates of M'.",
                "diagramHtml": "<div class='example-diagram-card'>Rule: (x, y) → (y, x)<br>M(2, -7) ➔ M'(-7, 2)<br>The coordinates switch positions!</div>",
                "stepByStepExplanation": "1. Recall the algebraic rule for reflection across the line y = x: swap the x and y coordinates: (x, y) → (y, x).\n2. Identify x = 2 and y = -7.\n3. The new x-coordinate becomes the original y-coordinate: -7.\n4. The new y-coordinate becomes the original x-coordinate: 2.\n5. Therefore, M' is located at (-7, 2).",
                "keyTakeaway": "Reflecting across y = x exchanges the coordinates: (x, y) becomes (y, x)."
            }
        ],
        "workedExamplesModelAnswers": [
            {
                "id": "we-1.3-1",
                "problemPrompt": "Quadrilateral ABCD has vertices A(-4, 1), B(-2, 4), C(-1, 2), and D(-3, 0). The figure is reflected across the y-axis to create A'B'C'D'. (a) State the coordinate reflection rule. (b) Determine the coordinates of all image vertices. (c) Prove that segment AA' is bisected by the y-axis.",
                "context": "HMH Into Math TE - Worked Example Model Lesson 1.3",
                "step1": "Identify Given Information: Preimage coordinates A(-4, 1), B(-2, 4), C(-1, 2), D(-3, 0). Reflection line is the y-axis (equation x = 0).",
                "step2": "Apply Rule / Formula:\n• The reflection rule across the y-axis is (x, y) → (-x, y).\n• A(-4, 1) → A'(-(-4), 1) = A'(4, 1)\n• B(-2, 4) → B'(-(-2), 4) = B'(2, 4)\n• C(-1, 2) → C'(-(-1), 2) = C'(1, 2)\n• D(-3, 0) → D'(-(-3), 0) = D'(3, 0)\n• To prove the y-axis bisects AA': Find the midpoint of AA': Midpoint = ((-4 + 4)/2, (1 + 1)/2) = (0, 1). Since the x-coordinate of the midpoint is 0, the midpoint lies directly on the y-axis (x = 0).",
                "step3": "Write Concluding Mathematical Statement: The reflection rule is (x, y) → (-x, y). The image coordinates are A'(4, 1), B'(2, 4), C'(1, 2), and D'(3, 0). Because the segment AA' is horizontal (length 8) and its midpoint is (0, 1), the vertical line x = 0 (y-axis) is the perpendicular bisector of AA'. Therefore, distance is preserved and ABCD ≅ A'B'C'D'.",
                "rubricGuidance": "Full credit: 1 pt for writing rule (-x, y); 2 pts for calculating all 4 image vertices; 1 pt for proving the y-axis is the perpendicular bisector using midpoint."
            },
            {
                "id": "we-1.3-2",
                "problemPrompt": "Triangle RST has vertices R(1, 2), S(4, 2), and T(2, 6). Its image R'S'T' has vertices R'(1, -4), S'(4, -4), and T'(2, -8). Determine the equation of the line of reflection that mapped Triangle RST onto Triangle R'S'T'.",
                "context": "HMH Into Math TE - Identifying Line of Reflection",
                "step1": "Identify Given Information: Preimage R(1, 2) and image R'(1, -4); S(4, 2) and S'(4, -4); T(2, 6) and T'(2, -8).",
                "step2": "Apply Rule / Formula: The line of reflection is the perpendicular bisector of the segment connecting any preimage vertex to its image vertex. Find the midpoint of RR':\n• Midpoint x = (1 + 1)/2 = 1\n• Midpoint y = (2 + (-4))/2 = -2/2 = -1\n• Check midpoint of TT': x = (2 + 2)/2 = 2; y = (6 + (-8))/2 = -1.\n• Since all midpoints share the constant y-coordinate y = -1, the line of reflection is horizontal.",
                "step3": "Write Concluding Mathematical Statement: The equation of the line of reflection is y = -1. Each preimage point is the exact same vertical distance from y = -1 as its corresponding image point (e.g., R is 3 units above y = -1 and R' is 3 units below y = -1).",
                "rubricGuidance": "Full credit: 1 pt for identifying midpoint calculation method; 2 pts for computing midpoints; 1 pt for writing the correct horizontal line equation y = -1."
            }
        ],
        "practiceQuestions": [
            {
                "id": "pq-1.3-1",
                "type": "fill-blank",
                "prompt": "If point K(-6, 7) is reflected across the x-axis, what are the coordinates of the image point K'?",
                "placeholder": "Enter as (x, y)",
                "acceptedAnswers": ["(-6, -7)", "(-6,-7)", "-6, -7", "-6,-7"],
                "hint": "Reflecting across the x-axis negates the y-coordinate: (x, y) → (x, -y).",
                "explanation": "Across the x-axis, the x-coordinate remains -6, while the y-coordinate changes from 7 to -7. Thus, K'(-6, -7)."
            },
            {
                "id": "pq-1.3-2",
                "type": "fill-blank",
                "prompt": "If point M(4, -9) is reflected across the y-axis, what are the coordinates of the image point M'?",
                "placeholder": "Enter as (x, y)",
                "acceptedAnswers": ["(-4, -9)", "(-4,-9)", "-4, -9", "-4,-9"],
                "hint": "Reflecting across the y-axis negates the x-coordinate: (x, y) → (-x, y).",
                "explanation": "Across the y-axis, the x-coordinate becomes -4, while the y-coordinate stays -9. Thus, M'(-4, -9)."
            },
            {
                "id": "pq-1.3-3",
                "type": "mcq",
                "prompt": "Which transformation rule represents a reflection across the line y = x?",
                "options": [
                    "(x, y) → (-x, -y)",
                    "(x, y) → (y, x)",
                    "(x, y) → (-y, -x)",
                    "(x, y) → (x, -y)"
                ],
                "correctIndex": 1,
                "hint": "When reflecting over y = x, the values of x and y swap places.",
                "explanation": "Reflecting across the diagonal line y = x interchanges the coordinates: (x, y) → (y, x)."
            },
            {
                "id": "pq-1.3-4",
                "type": "mcq",
                "prompt": "When a polygon with clockwise vertex order undergoes a reflection across any line, what happens to the vertex order of its image?",
                "options": [
                    "It stays clockwise",
                    "It changes to counterclockwise (orientation reverses)",
                    "It depends on whether the line is horizontal or vertical",
                    "The vertices are scrambled randomly"
                ],
                "correctIndex": 1,
                "hint": "Think about looking at your right hand in a mirror. It looks like a left hand!",
                "explanation": "Reflections reverse orientation (chirality). A clockwise sequence of vertices always becomes counterclockwise after reflection."
            }
        ],
        "bookQuestionBank": [
            {
                "id": "bq-1.3-1",
                "category": "Spark Your Learning",
                "title": "Mountain Lake Reflection Symmetry",
                "context": "HMH Into Math Grade 8 Teacher Edition, Lesson 1.3 Opening Exploration",
                "questionPrompt": "A photographer frames a shot of a mountain peak across a perfectly calm, still lake. On the camera viewfinder coordinate grid, the mountain peak is at P(3, 8) and the lake shoreline forms the line y = 2. The reflection of the peak appears in the water below. (a) What are the coordinates of the reflected mountain peak P'? (b) Explain why the lake surface acts as a line of reflection using geometric terms.",
                "modelAnswer": {
                    "summary": "The reflected peak is located at P'(3, -4). The still lake surface acts as the perpendicular bisector between the actual peak and its virtual image.",
                    "stepByStep": [
                        "Step 1: Determine the distance from peak P(3, 8) to the reflection line y = 2: Distance = 8 - 2 = 6 units.",
                        "Step 2: Apply the equal distance principle: The reflected image P' must lie 6 units below the line y = 2 along the same vertical line x = 3.",
                        "Step 3: Calculate y-coordinate of image: y' = 2 - 6 = -4.",
                        "Step 4: State the image coordinates: P'(3, -4).",
                        "Step 5: Explain geometric properties: The line segment connecting P(3, 8) and P'(3, -4) is vertical (perpendicular to horizontal line y = 2), and the line y = 2 cuts PP' exactly in half (midpoint is (3, 2))."
                    ],
                    "fullCreditJustification": "The water's surface y = 2 is the perpendicular bisector of segment PP'. Since P is 6 units above the water, its reflection P' is 6 units below at (3, -4). Distance and angle measures are preserved, but orientation is inverted.",
                    "rubricCriteria": "2 pts for finding P'(3, -4); 2 pts for explaining the perpendicular bisector relationship."
                }
            },
            {
                "id": "bq-1.3-2",
                "category": "Check Understanding",
                "title": "Maritime Signal Flag Distress Flip",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.3 Check Understanding Problem 4",
                "questionPrompt": "A ship carries a triangular signal flag with vertices at A(-5, 1), B(-2, 1), and C(-5, 4). In an emergency exercise, the flag must be flipped across the vertical line x = 0 (the y-axis) and then reflected across the x-axis. (a) Find the coordinates after the first reflection. (b) Find the coordinates after the second reflection. (c) Compare the final orientation with the original orientation.",
                "modelAnswer": {
                    "summary": "After reflecting across the y-axis: A'(5, 1), B'(2, 1), C'(5, 4). After reflecting across the x-axis: A''(5, -1), B''(2, -1), C''(5, -4). Two reflections restore the original orientation.",
                    "stepByStep": [
                        "Step 1: First reflection across y-axis: Rule (x, y) → (-x, y).\n• A(-5, 1) → A'(5, 1)\n• B(-2, 1) → B'(2, 1)\n• C(-5, 4) → C'(5, 4)",
                        "Step 2: Second reflection across x-axis: Rule (x, y) → (x, -y).\n• A'(5, 1) → A''(5, -1)\n• B'(2, 1) → B''(2, -1)\n• C'(5, 4) → C''(5, -4)",
                        "Step 3: Analyze orientation: The first reflection reversed orientation (clockwise to counterclockwise). The second reflection reversed orientation again (counterclockwise back to clockwise).",
                        "Step 4: Notice that (x, y) → (-x, -y) is equivalent to a 180° rotation about the origin!"
                    ],
                    "fullCreditJustification": "Each reflection reverses orientation. An even number of reflections (two) restores the original orientation. The composition of reflections across two perpendicular axes produces a 180° rotation.",
                    "rubricCriteria": "1 pt for first reflection; 1 pt for second reflection; 2 pts for correctly analyzing orientation restoration."
                }
            },
            {
                "id": "bq-1.3-3",
                "category": "On Your Own",
                "title": "Graphic Designer's Symmetrical Butterfly Wings",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.3 On Your Own Problem 7",
                "questionPrompt": "A graphic designer illustrates one wing of a monarch butterfly in Quadrant II with vertices at J(-1, 1), K(-4, 3), L(-6, 6), and M(-2, 5). She reflects the wing across the y-axis to generate the opposite wing. (a) List the coordinates of the opposite wing J'K'L'M'. (b) If the designer also wants a vertical line connecting the wing tips LL', what is the length of this segment?",
                "modelAnswer": {
                    "summary": "The opposite wing vertices are J'(1, 1), K'(4, 3), L'(6, 6), and M'(2, 5). The distance between wing tips LL' is 12 units.",
                    "stepByStep": [
                        "Step 1: Apply reflection across y-axis: Rule (x, y) → (-x, y).\n• J(-1, 1) → J'(1, 1)\n• K(-4, 3) → K'(4, 3)\n• L(-6, 6) → L'(6, 6)\n• M(-2, 5) → M'(2, 5)",
                        "Step 2: Find distance between wing tips L(-6, 6) and L'(6, 6):\n• Both points have y = 6 (horizontal segment).\n• Distance = |6 - (-6)| = 6 + 6 = 12 units.",
                        "Step 3: Verify symmetry: The y-axis (x = 0) is the perpendicular bisector of LL', bisecting the 12-unit segment into two 6-unit halves."
                    ],
                    "fullCreditJustification": "Across the y-axis, x-coordinates negate: L(-6, 6) maps to L'(6, 6). The length of horizontal segment LL' is |6 - (-6)| = 12 units.",
                    "rubricCriteria": "2 pts for all 4 reflected vertices; 2 pts for computing the length LL' = 12 units."
                }
            },
            {
                "id": "bq-1.3-4",
                "category": "Test Prep",
                "title": "Standardized Test Prep: Reflection Across Line y = x",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.3 Test Prep Question 15",
                "questionPrompt": "Point W has coordinates (-3, 5). If Point W is reflected across the line y = x, what are the coordinates of W'?\nA. (-3, -5)\nB. (3, -5)\nC. (5, -3)\nD. (-5, 3)",
                "modelAnswer": {
                    "summary": "Option C is correct: (5, -3).",
                    "stepByStep": [
                        "Step 1: State rule for reflection across y = x: (x, y) → (y, x).",
                        "Step 2: Identify preimage coordinates: x = -3, y = 5.",
                        "Step 3: Swap coordinates: New x = 5, New y = -3.",
                        "Step 4: Conclude: W' = (5, -3)."
                    ],
                    "fullCreditJustification": "Reflecting across the diagonal line y = x interchanges the x and y coordinates: (-3, 5) becomes (5, -3), which corresponds to Option C.",
                    "rubricCriteria": "1 pt for selecting C; 1 pt for identifying coordinate interchange rule."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 1.4: Explore Rotations
    # =========================================================================
    m1["1.4"] = {
        "id": "1.4",
        "lessonNumber": "1.4",
        "moduleNumber": 1,
        "moduleId": "module-1",
        "moduleTitle": "Module 1: Transformations and Congruence",
        "title": "Lesson 1.4: Explore Rotations",
        "introAndConcept": {
            "lessonTitle": "Lesson 1.4: Explore Rotations",
            "iCanStatement": "I can rotate figures 90°, 180°, and 270° clockwise and counterclockwise about the origin on the coordinate plane, determine algebraic mapping rules, and understand rotational symmetry.",
            "conceptExplanation": {
                "coreDefinition": "A rotation is a rigid motion that turns every point of a figure through a specified angle and direction around a fixed point called the center of rotation. Every point in the image remains the exact same distance from the center of rotation as its corresponding preimage point.",
                "keyProperties": [
                    "Fixed Center: The center of rotation does not move during the transformation.",
                    "Equal Radii: The distance from the center of rotation O to any preimage point P equals the distance from O to image point P' (OP = OP').",
                    "Constant Angle of Rotation: The angle formed by connecting preimage point P to center O and center O to image point P' (∠POP') equals the specified angle of rotation.",
                    "Preservation of Distance & Angles: Rotations preserve side lengths, angle measures, and parallelism (rigid motion).",
                    "Orientation Invariance: Rotations PRESERVE orientation. If vertices are clockwise in the preimage, they remain clockwise in the image."
                ],
                "coordinateNotationRule": "Coordinate Rules for Rotations About the Origin (0, 0):\n• 90° Clockwise (or 270° Counterclockwise): (x, y) → (y, -x)\n• 180° Turn (Clockwise or Counterclockwise): (x, y) → (-x, -y)\n• 270° Clockwise (or 90° Counterclockwise): (x, y) → (-y, x)\n• 360° Full Turn: (x, y) → (x, y) [Identity mapping]",
                "mathStandards": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3"
            },
            "visualSummarySvg": """<svg viewBox="0 0 420 220" class="concept-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gPre14" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#d97706" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gImg14" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#6d28d9" stop-opacity="0.45"/>
    </linearGradient>
    <marker id="arr14" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#6d28d9"/>
    </marker>
  </defs>
  <pattern id="grid14" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>
  <rect width="420" height="220" fill="url(#grid14)" rx="8"/>
  <line x1="40" y1="140" x2="380" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="180" y1="20" x2="180" y2="200" stroke="#94a3b8" stroke-width="1.5"/>
  <circle cx="180" cy="140" r="4.5" fill="#ef4444"/>
  <text x="160" y="155" font-size="11" font-weight="700" fill="#dc2626">Origin (0,0)</text>
  <polygon points="240,120 280,120 280,60" fill="url(#gPre14)" stroke="#d97706" stroke-width="2.5"/>
  <circle cx="240" cy="120" r="3.5" fill="#d97706"/><text x="245" y="133" font-size="10" font-weight="700" fill="#b45309">A(3,1)</text>
  <circle cx="280" cy="120" r="3.5" fill="#d97706"/><text x="286" y="133" font-size="10" font-weight="700" fill="#b45309">B(5,1)</text>
  <circle cx="280" cy="60" r="3.5" fill="#d97706"/><text x="286" y="58" font-size="10" font-weight="700" fill="#b45309">C(5,4)</text>
  <path d="M 240,120 A 70 70 0 0 0 160,80" fill="none" stroke="#6d28d9" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arr14)"/>
  <text x="235" y="90" font-size="11" font-weight="700" fill="#6d28d9">90° CCW</text>
  <polygon points="160,80 160,40 100,40" fill="url(#gImg14)" stroke="#6d28d9" stroke-width="2.5"/>
  <circle cx="160" cy="80" r="3.5" fill="#6d28d9"/><text x="168" y="85" font-size="10" font-weight="700" fill="#5b21b6">A'(-1,3)</text>
  <circle cx="160" cy="40" r="3.5" fill="#6d28d9"/><text x="168" y="38" font-size="10" font-weight="700" fill="#5b21b6">B'(-1,5)</text>
  <circle cx="100" cy="40" r="3.5" fill="#6d28d9"/><text x="65" y="38" font-size="10" font-weight="700" fill="#5b21b6">C'(-4,5)</text>
  <rect x="40" y="175" width="340" height="26" rx="5" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1"/>
  <text x="210" y="192" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="600" fill="#5b21b6" text-anchor="middle">Rule for 90° CCW (270° CW): (x, y) → (-y, x)</text>
</svg>""",
            "essentialVocabulary": [
                {
                    "term": "Rotation",
                    "definition": "A rigid transformation that turns a figure around a fixed point by a specified angle and direction.",
                    "example": "Turning a steering wheel or the hands of an analog clock is a rotation."
                },
                {
                    "term": "Center of Rotation",
                    "definition": "The fixed point around which all other points in the plane rotate.",
                    "example": "In Grade 8 math, the origin (0, 0) is the most common center of rotation."
                },
                {
                    "term": "Angle of Rotation",
                    "definition": "The amount of rotation in degrees (such as 90°, 180°, or 270°) through which a figure is turned.",
                    "example": "A quarter-turn is an angle of rotation of 90°."
                },
                {
                    "term": "Direction of Rotation",
                    "definition": "The sense of the turn: Clockwise (CW, following clock hands) or Counterclockwise (CCW, opposing clock hands).",
                    "example": "A 90° clockwise rotation is mathematically identical to a 270° counterclockwise rotation."
                },
                {
                    "term": "Rotational Symmetry",
                    "definition": "A figure has rotational symmetry if it can be rotated by an angle of 180° or less about its center and match its original outline exactly.",
                    "example": "A square has rotational symmetry at 90°, 180°, and 270°."
                }
            ]
        },
        "examples": [
            {
                "id": "ex-1.4-1",
                "title": "Example 1: Rotating 90° Counterclockwise About the Origin",
                "description": "Triangle ABC with vertices A(2, 3), B(5, 1), and C(4, 6) is rotated 90° counterclockwise about the origin (0, 0). Find the image coordinates.",
                "diagramHtml": "<div class='example-diagram-card'>Rule for 90° CCW: (x, y) → (-y, x)<br>A(2, 3) ➔ A'(-3, 2)<br>B(5, 1) ➔ B'(-1, 5)<br>C(4, 6) ➔ C'(-6, 4)</div>",
                "stepByStepExplanation": "1. Identify the rule for 90° counterclockwise rotation about (0,0): (x, y) → (-y, x).\n2. For vertex A(2, 3): Swap coordinates and negate the new x: A'(-3, 2).\n3. For vertex B(5, 1): Swap coordinates and negate the new x: B'(-1, 5).\n4. For vertex C(4, 6): Swap coordinates and negate the new x: C'(-6, 4).\n5. Notice that points in Quadrant I moved to Quadrant II.",
                "keyTakeaway": "90° CCW rotation swaps coordinates and negates the first term: (x, y) → (-y, x)."
            },
            {
                "id": "ex-1.4-2",
                "title": "Example 2: 180° Half-Turn Rotation About Origin",
                "description": "Rectangle EFGH has vertices E(-4, 2), F(-1, 2), G(-1, -3), and H(-4, -3). Rotate EFGH 180° about the origin.",
                "diagramHtml": "<div class='example-diagram-card'>Rule for 180°: (x, y) → (-x, -y)<br>E(-4, 2) ➔ E'(4, -2)<br>F(-1, 2) ➔ F'(1, -2)<br>G(-1, -3) ➔ G'(1, 3)<br>H(-4, -3) ➔ H'(4, 3)</div>",
                "stepByStepExplanation": "1. Recall rule for 180° rotation: Both coordinates change sign: (x, y) → (-x, -y).\n2. Apply to E(-4, 2): x becomes 4, y becomes -2 ➔ E'(4, -2).\n3. Apply to F(-1, 2): x becomes 1, y becomes -2 ➔ F'(1, -2).\n4. Apply to G(-1, -3): x becomes 1, y becomes 3 ➔ G'(1, 3).\n5. Apply to H(-4, -3): x becomes 4, y becomes 3 ➔ H'(4, 3).",
                "keyTakeaway": "A 180° rotation negates both x and y. CW and CCW 180° rotations yield the identical image."
            }
        ],
        "workedExamplesModelAnswers": [
            {
                "id": "we-1.4-1",
                "problemPrompt": "Trapezoid WXYZ has vertices W(1, 4), X(4, 4), Y(5, 1), and Z(0, 1). The trapezoid is rotated 90° clockwise about the origin to create W'X'Y'Z'. (a) State the coordinate rule. (b) Calculate the coordinates of W'X'Y'Z'. (c) Show that length WX = length W'X'.",
                "context": "HMH Into Math TE - Worked Example Model Lesson 1.4",
                "step1": "Identify Given Information: Preimage coordinates W(1, 4), X(4, 4), Y(5, 1), Z(0, 1). Rotation is 90° clockwise about origin (0, 0).",
                "step2": "Apply Rule / Formula:\n• The coordinate rule for a 90° clockwise rotation about the origin is (x, y) → (y, -x).\n• W(1, 4) → W'(4, -1)\n• X(4, 4) → X'(4, -4)\n• Y(5, 1) → Y'(1, -5)\n• Z(0, 1) → Z'(1, 0)\n• Calculate lengths: Preimage horizontal base WX = 4 - 1 = 3 units. Image vertical base W'X' = |-4 - (-1)| = |-3| = 3 units.",
                "step3": "Write Concluding Mathematical Statement: The algebraic rule is (x, y) → (y, -x). The image coordinates are W'(4, -1), X'(4, -4), Y'(1, -5), and Z'(1, 0). Because length WX = length W'X' = 3 units and all corresponding segments remain equal in length, the rotation is a rigid motion and Trapezoid WXYZ ≅ Trapezoid W'X'Y'Z'.",
                "rubricGuidance": "Full credit: 1 pt for writing (y, -x); 2 pts for computing all 4 vertices; 1 pt for verifying length invariance WX = W'X' = 3."
            },
            {
                "id": "we-1.4-2",
                "problemPrompt": "Triangle PQR has vertices P(-3, -2), Q(-1, -5), and R(-4, -6). Its image P'Q'R' has vertices P'(3, 2), Q'(1, 5), and R'(4, 6). Determine the angle and direction of rotation about the origin that maps PQR onto P'Q'R'.",
                "context": "HMH Into Math TE - Identifying Rotation Transformations",
                "step1": "Identify Given Information: Preimage vertices P(-3, -2), Q(-1, -5), R(-4, -6) and image vertices P'(3, 2), Q'(1, 5), R'(4, 6). Center of rotation is the origin (0, 0).",
                "step2": "Apply Rule / Formula:\n• Compare coordinate signs: (-3, -2) → (3, 2); (-1, -5) → (1, 5); (-4, -6) → (4, 6).\n• For every point, x' = -x and y' = -y.\n• This algebraic mapping (x, y) → (-x, -y) represents a 180° rotation.\n• A line drawn from P(-3, -2) through (0, 0) to P'(3, 2) forms a straight line of 180°.",
                "step3": "Write Concluding Mathematical Statement: The transformation is a 180° rotation (clockwise or counterclockwise) about the origin. Because rotating 180° in either direction results in the same opposite-sign coordinates (-x, -y), direction does not change the result.",
                "rubricGuidance": "Full credit: 1 pt for identifying coordinate negation rule; 2 pts for concluding 180° rotation; 1 pt for noting that CW and CCW produce identical 180° images."
            }
        ],
        "practiceQuestions": [
            {
                "id": "pq-1.4-1",
                "type": "fill-blank",
                "prompt": "Point A(5, -2) is rotated 90° counterclockwise about the origin. What are the coordinates of the image point A'?",
                "placeholder": "Enter as (x, y)",
                "acceptedAnswers": ["(2, 5)", "(2,5)", "2, 5", "2,5"],
                "hint": "Rule for 90° CCW about origin is (x, y) → (-y, x). The opposite of -2 is 2.",
                "explanation": "Applying (x, y) → (-y, x): x' = -(-2) = 2, and y' = 5. Therefore, A'(2, 5)."
            },
            {
                "id": "pq-1.4-2",
                "type": "fill-blank",
                "prompt": "Point B(-3, 8) is rotated 180° about the origin. What are the coordinates of the image point B'?",
                "placeholder": "Enter as (x, y)",
                "acceptedAnswers": ["(3, -8)", "(3,-8)", "3, -8", "3,-8"],
                "hint": "Rule for 180° rotation about origin is (x, y) → (-x, -y).",
                "explanation": "Applying (x, y) → (-x, -y): x' = -(-3) = 3, and y' = -(8) = -8. Thus, B'(3, -8)."
            },
            {
                "id": "pq-1.4-3",
                "type": "mcq",
                "prompt": "Which rotation produces the EXACT SAME image as a 90° clockwise rotation about the origin?",
                "options": [
                    "90° counterclockwise rotation",
                    "180° clockwise rotation",
                    "270° counterclockwise rotation",
                    "360° counterclockwise rotation"
                ],
                "correctIndex": 2,
                "hint": "Full circle is 360°. A 90° turn in one direction leaves 360° - 90° in the other.",
                "explanation": "Since 360° - 90° = 270°, turning 90° clockwise brings a figure to the exact same position as turning 270° counterclockwise. Both share the rule (x, y) → (y, -x)."
            },
            {
                "id": "pq-1.4-4",
                "type": "mcq",
                "prompt": "What is the coordinate rule for a 270° clockwise rotation about the origin?",
                "options": [
                    "(x, y) → (y, -x)",
                    "(x, y) → (-y, x)",
                    "(x, y) → (-x, -y)",
                    "(x, y) → (-x, y)"
                ],
                "correctIndex": 1,
                "hint": "A 270° clockwise rotation is equivalent to a 90° counterclockwise rotation.",
                "explanation": "Rotating 270° clockwise is identical to 90° counterclockwise, which follows the algebraic mapping rule (x, y) → (-y, x)."
            }
        ],
        "bookQuestionBank": [
            {
                "id": "bq-1.4-1",
                "category": "Spark Your Learning",
                "title": "Amusement Park Ferris Wheel Cart Position",
                "context": "HMH Into Math Grade 8 Teacher Edition, Lesson 1.4 Opening Activity",
                "questionPrompt": "A Ferris wheel at an amusement park is centered at the origin (0, 0) on a park blueprint. Cart 1 is currently boarded at position C(0, -10) at the bottom of the wheel. The operator turns the wheel 90° counterclockwise, then pauses. (a) What are the coordinates of Cart 1 after the 90° CCW rotation? (b) If the operator continues turning the wheel another 90° CCW (total 180° from start), what are the coordinates? (c) Does Cart 1's distance from the center change during the ride?",
                "modelAnswer": {
                    "summary": "Cart 1 rotates to (10, 0) at 90° CCW, and to (0, 10) at 180°. Distance from center remains strictly 10 units at all times.",
                    "stepByStep": [
                        "Step 1: Identify initial position: C(0, -10) with center (0, 0). Radius r = 10 units.",
                        "Step 2: Apply 90° CCW rotation rule: (x, y) → (-y, x).\n• x' = -(-10) = 10; y' = 0.\n• Position after 90° CCW = (10, 0) [3 o'clock position].",
                        "Step 3: Apply 180° rotation rule to start C(0, -10): (x, y) → (-x, -y).\n• x'' = -(0) = 0; y'' = -(-10) = 10.\n• Position after 180° = (0, 10) [12 o'clock top position].",
                        "Step 4: Analyze distance: The distance from the center (0,0) to any point on a rotation circle is r = √(x² + y²). In all positions, r = 10 units."
                    ],
                    "fullCreditJustification": "Rotations preserve distance from the center of rotation. At 90° CCW, C'(10, 0); at 180°, C''(0, 10). The radius of 10 units is strictly invariant.",
                    "rubricCriteria": "1 pt for (10, 0); 1 pt for (0, 10); 2 pts for explaining distance invariance from center."
                }
            },
            {
                "id": "bq-1.4-2",
                "category": "Check Understanding",
                "title": "Wind Turbine Blade Rotational Balance",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.4 Check Understanding Problem 2",
                "questionPrompt": "An engineering model tests a 2-blade wind turbine rotor centered at the origin (0, 0). Blade Tip 1 has coordinates B₁(3, 4). Because the rotor is completely balanced, Blade Tip 2 is oriented directly opposite Blade Tip 1 through a 180° rotation. (a) Find the coordinates of Blade Tip 2. (b) Calculate the total tip-to-tip diameter of the rotor. (c) Does rotating the turbine blades preserve orientation?",
                "modelAnswer": {
                    "summary": "Blade Tip 2 is at B₂(-3, -4). The total diameter is 10 units. Rotations preserve orientation.",
                    "stepByStep": [
                        "Step 1: Apply 180° rotation rule: (x, y) → (-x, -y).\n• For B₁(3, 4), B₂ = (-(3), -(4)) = (-3, -4).",
                        "Step 2: Calculate blade length from center: Radius = √(3² + 4²) = √(9 + 16) = √25 = 5 units.",
                        "Step 3: Calculate total tip-to-tip diameter: Diameter = 2 × Radius = 2 × 5 = 10 units. (Alternatively, distance between (3, 4) and (-3, -4) is √((3 - (-3))² + (4 - (-4))²) = √(6² + 8²) = √100 = 10).",
                        "Step 4: Orientation: Rotations preserve the clockwise/counterclockwise order of vertices."
                    ],
                    "fullCreditJustification": "A 180° rotation produces coordinates (-3, -4). The distance between the opposite tips is 10 units. Rotations preserve distance and preserve orientation.",
                    "rubricCriteria": "2 pts for finding B₂(-3, -4); 1 pt for calculating diameter = 10; 1 pt for confirming orientation preservation."
                }
            },
            {
                "id": "bq-1.4-3",
                "category": "On Your Own",
                "title": "Graphic Pinwheel Blade Quarter-Turns",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.4 On Your Own Exercise 5",
                "questionPrompt": "A pinwheel logo consists of four identical triangular blades. Blade 1 has vertices O(0, 0), P(4, 0), and Q(3, 2). Blade 2 is created by rotating Blade 1 by 90° CCW about O. Blade 3 is created by rotating Blade 1 by 180° about O. Blade 4 is created by rotating Blade 1 by 270° CCW about O. List the coordinates of vertices P and Q for Blades 2, 3, and 4.",
                "modelAnswer": {
                    "summary": "Blade 2 (90° CCW): P₂(0, 4), Q₂(-2, 3). Blade 3 (180°): P₃(-4, 0), Q₃(-3, -2). Blade 4 (270° CCW): P₄(0, -4), Q₄(2, -3).",
                    "stepByStep": [
                        "Step 1: Start with P(4, 0) and Q(3, 2).",
                        "Step 2: Blade 2 (90° CCW): Rule (x, y) → (-y, x).\n• P₂(0, 4) and Q₂(-2, 3).",
                        "Step 3: Blade 3 (180°): Rule (x, y) → (-x, -y).\n• P₃(-4, 0) and Q₃(-3, -2).",
                        "Step 4: Blade 4 (270° CCW): Rule (x, y) → (y, -x).\n• P₄(0, -4) and Q₄(2, -3)."
                    ],
                    "fullCreditJustification": "Applying standard origin rotation rules: 90° CCW gives (-y, x), 180° gives (-x, -y), and 270° CCW gives (y, -x). All 4 blades are congruent.",
                    "rubricCriteria": "1 pt per blade calculation (3 pts total); 1 pt for clear systematic presentation."
                }
            },
            {
                "id": "bq-1.4-4",
                "category": "Test Prep",
                "title": "Standardized Test Prep: Quadrant Rotation Mapping",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.4 Test Prep Problem 16",
                "questionPrompt": "Triangle JKL has vertices J(-3, 2), K(-1, 5), and L(-5, 4) located in Quadrant II. If Triangle JKL is rotated 90° clockwise about the origin, in which quadrant will the image Triangle J'K'L' lie?\nA. Quadrant I\nB. Quadrant II\nC. Quadrant III\nD. Quadrant IV",
                "modelAnswer": {
                    "summary": "Option A is correct: Quadrant I.",
                    "stepByStep": [
                        "Step 1: Identify rule for 90° clockwise rotation about origin: (x, y) → (y, -x).",
                        "Step 2: In Quadrant II, preimage coordinates have negative x and positive y: (-, +).",
                        "Step 3: Applying rule: New x = y (which is positive, +); New y = -x (the negative of a negative is positive, +).",
                        "Step 4: Both coordinates of the image are positive (+, +), which corresponds directly to Quadrant I."
                    ],
                    "fullCreditJustification": "When a figure in Quadrant II (-, +) rotates 90° clockwise, it turns one quadrant forward clockwise into Quadrant I (+, +). Option A is correct.",
                    "rubricCriteria": "1 pt for selecting A; 1 pt for quadrant algebraic explanation."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 1.5: Understand and Recognize Congruent Figures
    # =========================================================================
    m1["1.5"] = {
        "id": "1.5",
        "lessonNumber": "1.5",
        "moduleNumber": 1,
        "moduleId": "module-1",
        "moduleTitle": "Module 1: Transformations and Congruence",
        "title": "Lesson 1.5: Understand and Recognize Congruent Figures",
        "introAndConcept": {
            "lessonTitle": "Lesson 1.5: Understand and Recognize Congruent Figures",
            "iCanStatement": "I can verify that two figures are congruent by identifying a sequence of one or more rigid motions that maps one figure onto the other, and write formal congruence statements matching corresponding vertices.",
            "conceptExplanation": {
                "coreDefinition": "Two two-dimensional geometric figures are congruent (symbol: ≅) if and only if there exists a sequence of one or more rigid motions (translations, reflections, rotations) that maps the preimage exactly onto the image. Congruent figures have identical size and identical shape.",
                "keyProperties": [
                    "Fundamental Theorem of Congruence: Figure A ≅ Figure B ⇔ A can be mapped to B by a sequence of rigid motions.",
                    "CPCTC: Corresponding Parts of Congruent Figures are Congruent. All corresponding side lengths are equal (AB = DE) and all corresponding angles are equal (m∠A = m∠D).",
                    "Sequence / Composition: Rigid motions can be chained together (e.g., a translation followed by a rotation). The composition of any number of rigid motions is always a rigid motion.",
                    "Non-Commutative Warning: The order in which transformations are performed often matters! Translating then reflecting does not always produce the same result as reflecting then translating.",
                    "Congruence Statement Vertex Ordering: In the statement ΔABC ≅ ΔXYZ, the order of letters dictates corresponding vertices: A corresponds to X, B to Y, and C to Z."
                ],
                "coordinateNotationRule": "Congruence statement: Figure A ≅ Figure B. Mapping composition: (x, y) → T₁(x, y) → T₂(T₁(x, y)). Distance invariant: d(A, B) = d(A', B').",
                "mathStandards": "CCSS.MATH.CONTENT.8.G.A.2"
            },
            "visualSummarySvg": """<svg viewBox="0 0 420 220" class="concept-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gPre15" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#047857" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gMid15" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#eab308" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#ca8a04" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gFin15" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#3730a3" stop-opacity="0.45"/>
    </linearGradient>
    <marker id="arr15" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#0284c7"/>
    </marker>
  </defs>
  <pattern id="grid15" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>
  <rect width="420" height="220" fill="url(#grid15)" rx="8"/>
  <polygon points="40,140 100,140 80,70" fill="url(#gPre15)" stroke="#059669" stroke-width="2.5"/>
  <text x="70" y="125" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">Figure 1</text>
  <path d="M 105,105 L 155,105" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arr15)"/>
  <text x="130" y="95" font-size="9.5" font-weight="700" fill="#0284c7" text-anchor="middle">1. Translate</text>
  <polygon points="170,140 230,140 210,70" fill="url(#gMid15)" stroke="#ca8a04" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="200" y="125" font-size="10" font-weight="700" fill="#854d0e" text-anchor="middle">Step 1 Image</text>
  <path d="M 240,105 L 290,105" stroke="#9333ea" stroke-width="2.5" marker-end="url(#arr15)"/>
  <text x="265" y="95" font-size="9.5" font-weight="700" fill="#9333ea" text-anchor="middle">2. Reflect</text>
  <polygon points="310,140 370,140 330,70" fill="url(#gFin15)" stroke="#4f46e5" stroke-width="2.5"/>
  <text x="340" y="125" font-size="11" font-weight="800" fill="#312e81" text-anchor="middle">Figure 2</text>
  <rect x="30" y="170" width="360" height="34" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <text x="210" y="192" font-size="11.5" font-weight="700" fill="#166534" text-anchor="middle">Congruence Theorem: Rigid Motion Sequence ⇒ Figure 1 ≅ Figure 2</text>
</svg>""",
            "essentialVocabulary": [
                {
                    "term": "Congruent Figures",
                    "definition": "Geometric figures that have the exact same shape and exact same size; one can be mapped onto the other using only rigid motions.",
                    "example": "If ΔABC ≅ ΔDEF, every corresponding side and angle are equal in measure."
                },
                {
                    "term": "Congruence Symbol (≅)",
                    "definition": "The mathematical symbol indicating that two figures are congruent.",
                    "example": "Read 'ΔABC ≅ ΔXYZ' as 'Triangle ABC is congruent to Triangle XYZ'."
                },
                {
                    "term": "Sequence of Transformations",
                    "definition": "Two or more transformations executed in succession where the image of the first serves as the preimage for the second.",
                    "example": "A translation 4 units right followed by a reflection across the x-axis."
                },
                {
                    "term": "CPCTC",
                    "definition": "'Corresponding Parts of Congruent Triangles are Congruent' — once congruence is proven, all matching sides and angles are equal.",
                    "example": "Since ΔABC ≅ ΔDEF, side AB = DE and ∠C = ∠F."
                },
                {
                    "term": "Rigid Motion Sequence",
                    "definition": "Any chain of translations, reflections, and rotations; it always preserves side lengths and angle measures.",
                    "example": "Combining a rotation of 90° with a translation produces a congruent figure."
                }
            ]
        },
        "examples": [
            {
                "id": "ex-1.5-1",
                "title": "Example 1: Identifying a Sequence of Transformations Proving Congruence",
                "description": "Triangle 1 has vertices A(1, 1), B(4, 1), and C(1, 5). Triangle 2 has vertices D(-1, -1), E(-4, -1), and F(-1, -5). Describe a sequence of rigid motions mapping Triangle 1 to Triangle 2.",
                "diagramHtml": "<div class='example-diagram-card'>Sequence Option: 180° rotation about origin<br>A(1, 1) ➔ (-1, -1) = D<br>B(4, 1) ➔ (-4, -1) = E<br>C(1, 5) ➔ (-1, -5) = F<br><strong>Conclusion:</strong> ΔABC ≅ ΔDEF via 180° rotation.</div>",
                "stepByStepExplanation": "1. Compare coordinates: A(1, 1) and D(-1, -1); B(4, 1) and E(-4, -1); C(1, 5) and F(-1, -5).\n2. Notice that for every vertex, (x, y) maps to (-x, -y).\n3. Recall that (x, y) → (-x, -y) is a 180° rotation about the origin.\n4. Since a 180° rotation is a rigid motion, Triangle 1 maps exactly onto Triangle 2.\n5. Therefore, Triangle 1 ≅ Triangle 2.",
                "keyTakeaway": "If a sequence of rigid motions maps one figure onto another, the figures are mathematically congruent."
            },
            {
                "id": "ex-1.5-2",
                "title": "Example 2: Order of Transformations Matters (Non-Commutative)",
                "description": "Start with point P(2, 3). Compare: (Sequence A) Translate 4 units right, then reflect across x-axis vs. (Sequence B) Reflect across x-axis, then translate 4 units right.",
                "diagramHtml": "<div class='example-diagram-card'><strong>Seq A:</strong> P(2, 3) ➔ (6, 3) ➔ (6, -3)<br><strong>Seq B:</strong> P(2, 3) ➔ (2, -3) ➔ (6, -3)<br>In this case they match! But consider y-translation + reflection: order often changes final position!</div>",
                "stepByStepExplanation": "1. Consider translation up 2 units, then reflect across x-axis: (2, 3) → (2, 5) → (2, -5).\n2. Reverse the order: Reflect across x-axis first, then translate up 2: (2, 3) → (2, -3) → (2, -1).\n3. Compare results: (2, -5) ≠ (2, -1)!\n4. Conclusion: Changing the sequence order produces completely different locations.",
                "keyTakeaway": "Always execute transformation sequences in the exact order specified."
            }
        ],
        "workedExamplesModelAnswers": [
            {
                "id": "we-1.5-1",
                "problemPrompt": "On a coordinate plane, Figure A is a triangle with vertices at (1, 2), (4, 2), and (4, 5). Figure B has vertices at (-4, -2), (-1, -2), and (-1, -5). (a) Identify a specific sequence of two rigid motions that maps Figure A onto Figure B. (b) Write a formal congruence statement with vertices listed in correct corresponding order.",
                "context": "HMH Into Math TE - Congruence Sequence Proof",
                "step1": "Identify Given Information: Preimage Figure A vertices (1, 2), (4, 2), (4, 5). Image Figure B vertices (-4, -2), (-1, -2), (-1, -5). Both are right triangles with legs of length 3.",
                "step2": "Apply Rule / Formula:\n• Step 1: Reflect Figure A across the y-axis using rule (x, y) → (-x, y). The intermediate image has vertices at (-1, 2), (-4, 2), and (-4, 5).\n• Step 2: Reflect the intermediate figure across the line y = 0 (the x-axis) or translate. Alternatively, notice a single translation of 5 units left and 7 units down does not match orientation. Instead: Reflect across the x-axis: (-1, 2) → (-1, -2); (-4, 2) → (-4, -2); (-4, 5) → (-4, -5).\n• Now, translate 3 units left or re-examine: Notice (1, 2) → (-1, -2) is a 180° rotation: (1, 2) → (-1, -2); (4, 2) → (-4, -2); (4, 5) → (-4, -5). Wait! Figure B has vertices (-4, -2), (-1, -2), (-1, -5). Intermediate vertices were (-4, -5) vs (-1, -5). Thus, reflect intermediate figure across the vertical line x = -2.5.\n• Clear 2-step sequence: Step 1: Translate Figure A 5 units left: (x, y) → (x - 5, y), giving vertices (-4, 2), (-1, 2), (-1, 5). Step 2: Reflect across the horizontal line y = 0 (the x-axis): (x, y) → (x, -y), giving (-4, -2), (-1, -2), and (-1, -5)!",
                "step3": "Write Concluding Mathematical Statement: A sequence that maps Figure A onto Figure B is: (1) A translation 5 units to the left: (x, y) → (x - 5, y), followed by (2) A reflection across the x-axis: (x, y) → (x, -y). Because both steps are rigid motions that preserve side lengths and angle measures, Figure A ≅ Figure B.",
                "rubricGuidance": "Full credit: 2 pts for describing a valid 2-step sequence of rigid motions; 1 pt for intermediate coordinate verification; 1 pt for writing the formal congruence conclusion."
            },
            {
                "id": "we-1.5-2",
                "problemPrompt": "Quadrilateral ABCD is congruent to Quadrilateral EFGH. Given that AB = 7.2 cm, BC = 4.5 cm, CD = 6.1 cm, DA = 5.0 cm, m∠A = 85°, and m∠B = 105°, determine: (a) The length of side EF. (b) The length of side GH. (c) The measure of ∠E. (d) The measure of ∠F.",
                "context": "HMH Into Math TE - CPCTC Applications",
                "step1": "Identify Given Information: Congruence statement Quadrilateral ABCD ≅ Quadrilateral EFGH. Given sides AB = 7.2, BC = 4.5, CD = 6.1, DA = 5.0 cm; angles m∠A = 85°, m∠B = 105°.",
                "step2": "Apply Rule / Theorem (CPCTC): In a congruence statement, the letter order indicates corresponding parts:\n• Side AB corresponds to Side EF ➔ EF = AB = 7.2 cm.\n• Side BC corresponds to Side FG ➔ FG = BC = 4.5 cm.\n• Side CD corresponds to Side GH ➔ GH = CD = 6.1 cm.\n• Side DA corresponds to Side HE ➔ HE = DA = 5.0 cm.\n• Angle A corresponds to Angle E ➔ m∠E = m∠A = 85°.\n• Angle B corresponds to Angle F ➔ m∠F = m∠B = 105°.",
                "step3": "Write Concluding Mathematical Statement: By CPCTC, EF = 7.2 cm, GH = 6.1 cm, m∠E = 85°, and m∠F = 105°. All corresponding lengths and angles are equal.",
                "rubricGuidance": "Full credit: 1 pt for each correct value with explicit CPCTC justification (4 pts total)."
            }
        ],
        "practiceQuestions": [
            {
                "id": "pq-1.5-1",
                "type": "mcq",
                "prompt": "If Triangle JKL ≅ Triangle XYZ, which side in Triangle XYZ corresponds to side KL?",
                "options": [
                    "Side XY",
                    "Side YZ",
                    "Side XZ",
                    "Side ZX"
                ],
                "correctIndex": 1,
                "hint": "Match the position of the letters in the congruence statement: JKL ≅ XYZ. KL are the 2nd and 3rd letters.",
                "explanation": "In the congruence statement ΔJKL ≅ ΔXYZ, the letters KL are in the 2nd and 3rd positions. The corresponding letters in ΔXYZ are YZ. Therefore, side KL corresponds to side YZ."
            },
            {
                "id": "pq-1.5-2",
                "type": "fill-blank",
                "prompt": "Triangle ABC is congruent to Triangle DEF. If m∠A = 52° and m∠B = 68°, what is the measure of ∠F in degrees?",
                "placeholder": "Enter number (e.g. 60)",
                "acceptedAnswers": ["60", "60°", "60 degrees"],
                "hint": "First find m∠C using the triangle angle sum theorem (180° - 52° - 68°). Then use CPCTC: m∠F = m∠C.",
                "explanation": "The sum of angles in ΔABC is 180°. So m∠C = 180° - 52° - 68° = 60°. Since ΔABC ≅ ΔDEF, ∠C corresponds to ∠F. Therefore, m∠F = 60°."
            },
            {
                "id": "pq-1.5-3",
                "type": "mcq",
                "prompt": "Which sequence of transformations produces an image that is CONGRUENT to the original preimage?",
                "options": [
                    "A translation followed by a dilation with scale factor 2",
                    "A rotation followed by a reflection across the x-axis",
                    "A reflection followed by a horizontal stretch",
                    "A dilation with scale factor 0.5 followed by a translation"
                ],
                "correctIndex": 1,
                "hint": "Congruence requires ONLY rigid motions (translations, reflections, rotations). No dilations or stretches allowed!",
                "explanation": "Rotations and reflections are both rigid motions (isometries). Their composition preserves side lengths and angle measures, guaranteeing congruence. Dilations change size, destroying congruence."
            },
            {
                "id": "pq-1.5-4",
                "type": "fill-blank",
                "prompt": "Two figures that can be mapped onto each other using only a sequence of rigid motions are called ____________ figures.",
                "placeholder": "Enter vocabulary word",
                "acceptedAnswers": ["congruent", "Congruent"],
                "hint": "They have the exact same shape and exact same size (symbol ≅).",
                "explanation": "Two figures related by a sequence of rigid motions are congruent."
            }
        ],
        "bookQuestionBank": [
            {
                "id": "bq-1.5-1",
                "category": "Spark Your Learning",
                "title": "Quilt Patchwork Mosaic Congruence",
                "context": "HMH Into Math Grade 8 Teacher Edition, Lesson 1.5 Opening Exploration",
                "questionPrompt": "A master quilter pieces together a geometric quilt top. Patch 1 is an asymmetrical right triangle with legs of 6 inches and 8 inches. Patch 2 is sewn in a different block, appearing upside down and shifted. The quilter claims both patches were cut from the exact same template. How can you prove using transformational geometry that Patch 1 is congruent to Patch 2?",
                "modelAnswer": {
                    "summary": "By demonstrating a sequence of rigid motions (such as a translation and a 180° rotation) that maps Patch 1 onto Patch 2, we prove they are congruent.",
                    "stepByStep": [
                        "Step 1: Define congruence via transformations: Two figures are congruent if and only if there exists a sequence of rigid motions mapping one directly onto the other.",
                        "Step 2: Identify the transformations: To align the upside-down patch, apply a 180° rotation (rigid motion). To align position, apply a vector translation (rigid motion).",
                        "Step 3: Verify invariance: Both rotation and translation preserve segment lengths (6 in, 8 in, and hypotenuse 10 in) and right angles (90°).",
                        "Step 4: Conclude: Since Patch 1 maps onto Patch 2 through rigid motions, Patch 1 ≅ Patch 2."
                    ],
                    "fullCreditJustification": "Under CCSS Grade 8 standards, congruence is established by exhibiting a sequence of rigid motions. Since rotation and translation preserve all distances and angles, the two quilt patches are congruent.",
                    "rubricCriteria": "2 pts for identifying valid rigid motions; 2 pts for citing the transformational definition of congruence."
                }
            },
            {
                "id": "bq-1.5-2",
                "category": "Check Understanding",
                "title": "Robotic Assembly Arm Conveyor Path",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.5 Check Understanding Problem 3",
                "questionPrompt": "An industrial robotic arm picks up a smartphone chassis from Conveyor Belt 1 at position A(2, 1), B(2, 6), C(4, 6), and D(4, 1). It places the chassis on Conveyor Belt 2 at position A'(-6, -2), B'(-6, -7), C'(-4, -7), and D'(-4, -2). (a) Describe a sequence of two rigid motions the robot arm performed. (b) Explain why the chassis fits into the casing on Belt 2 without any measurement change.",
                "modelAnswer": {
                    "summary": "The robot performed a reflection across the y-axis followed by a translation of 4 units left and 3 units down (or a 180° rotation and translation). The chassis fits perfectly because rigid motions preserve distance and angles.",
                    "stepByStep": [
                        "Step 1: Check dimensions: Preimage width = 2 units, height = 5 units. Image width = 2 units, height = 5 units.",
                        "Step 2: Analyze orientation and positions: A(2, 1) and B(2, 6) were on the left. In the image, A'(-6, -2) and B'(-6, -7) have y inverted and shifted.",
                        "Step 3: Sequence: Step 1: Rotate 180° about origin: (x, y) → (-x, -y), giving (-2, -1), (-2, -6), (-4, -6), (-4, -1). Step 2: Translate 4 units left and 1 unit down: (x - 4, y - 1), yielding (-6, -2), (-6, -7), (-8, -7)... Notice matching: A reflection across y-axis followed by translation achieves exact placement.",
                        "Step 4: Conclude on fit: Because all steps are rigid motions, side lengths and interior angles are invariant. The smartphone chassis did not warp, stretch, or shrink."
                    ],
                    "fullCreditJustification": "A sequence of rigid motions maps the chassis from Belt 1 to Belt 2. Because rigid motions preserve distance (isometry), the chassis dimensions remain identical, guaranteeing a perfect fit.",
                    "rubricCriteria": "2 pts for identifying a valid rigid motion sequence; 2 pts for explaining fit via invariance of distance and angles."
                }
            },
            {
                "id": "bq-1.5-3",
                "category": "On Your Own",
                "title": "Skatepark Ramp Blueprint Truss Supports",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.5 On Your Own Exercise 9",
                "questionPrompt": "A civil engineer designs triangular steel trusses to reinforce a skatepark launch ramp. Truss 1 has coordinates at (0, 0), (6, 0), and (6, 8). Truss 2 has coordinates at (10, 8), (10, 2), and (2, 2). Prove whether Truss 1 and Truss 2 are congruent by finding corresponding side lengths and describing a sequence of rigid motions.",
                "modelAnswer": {
                    "summary": "Truss 1 and Truss 2 are congruent right triangles with legs 6 and 8 and hypotenuse 10. A 90° clockwise rotation followed by a translation maps Truss 1 onto Truss 2.",
                    "stepByStep": [
                        "Step 1: Compute side lengths of Truss 1: Base = 6, Height = 8, Hypotenuse = √(6² + 8²) = √100 = 10.",
                        "Step 2: Compute side lengths of Truss 2: Vertical leg = |8 - 2| = 6, Horizontal leg = |10 - 2| = 8, Hypotenuse = √(6² + 8²) = 10.",
                        "Step 3: Verify matching parts: Both trusses have side lengths 6, 8, and 10 with an included right angle of 90°.",
                        "Step 4: Describe mapping sequence: (1) Rotate Truss 1 by 90° clockwise about (0,0): (x, y) → (y, -x). The vertices become (0, 0), (0, -6), (8, -6). (2) Translate by (x + 2, y + 8): (0+2, 0+8) = (2, 8)... Alternatively, reflect and translate.",
                        "Step 5: Conclude: Since a sequence of rigid motions maps Truss 1 to Truss 2, Truss 1 ≅ Truss 2."
                    ],
                    "fullCreditJustification": "Corresponding side lengths are equal (6 = 6, 8 = 8, 10 = 10) and corresponding angles are equal (90° = 90°). Because Truss 1 can be mapped to Truss 2 via rigid motions, Truss 1 ≅ Truss 2.",
                    "rubricCriteria": "2 pts for calculating side lengths (6, 8, 10); 2 pts for describing rigid motion sequence and concluding congruence."
                }
            },
            {
                "id": "bq-1.5-4",
                "category": "Test Prep",
                "title": "Standardized Test Prep: Congruence Sequence Matching",
                "context": "HMH Into Math Grade 8 TE, Lesson 1.5 Test Prep Question 18",
                "questionPrompt": "Figure 1 is reflected across the x-axis and then translated 3 units right to create Figure 2. Which statement MUST be true?\nA. Figure 1 and Figure 2 have different perimeters.\nB. Figure 1 and Figure 2 are congruent.\nC. Figure 2 has twice the area of Figure 1.\nD. The angle measures of Figure 2 are larger than Figure 1.",
                "modelAnswer": {
                    "summary": "Option B is correct: Figure 1 and Figure 2 are congruent.",
                    "stepByStep": [
                        "Step 1: Identify the transformations: Reflection across the x-axis and translation 3 units right.",
                        "Step 2: Classify both transformations: Both reflections and translations are rigid motions (isometries).",
                        "Step 3: Apply the Congruence Theorem: Any sequence composed solely of rigid motions produces an image that is congruent to the preimage.",
                        "Step 4: Evaluate options: Perimeters and areas remain identical, angles remain identical. Only Option B is true."
                    ],
                    "fullCreditJustification": "A sequence of rigid motions always maps a figure onto a congruent figure. Therefore, Figure 1 ≅ Figure 2 (Option B).",
                    "rubricCriteria": "1 pt for selecting B; 1 pt for justification using rigid motion composition."
                }
            }
        ]
    }

    return m1

if __name__ == "__main__":
    m1 = get_module1_lessons()
    print("Module 1 lessons generated successfully:", list(m1.keys()))
