# -*- coding: utf-8 -*-
import json
import sys

# We will build each lesson dictionary and then assemble them.
lessons = {}

# ==============================================================================
# LESSON 1.1: Investigate Transformations
# ==============================================================================
lessons["1.1"] = {
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
            "coreDefinition": "A transformation is a mathematical operation that maps every point of an original geometric figure, called the preimage, to a corresponding location on a new figure, called the image. When a transformation preserves both the size and the shape of the figure—leaving all side lengths, angle measures, and parallel relationships unchanged—it is called a rigid motion (or isometry).",
            "keyProperties": [
                "Preservation of Distance: The length of each segment in the image is equal to the length of the corresponding segment in the preimage (A'B' = AB).",
                "Preservation of Angle Measure: Each angle in the image has the exact same degree measure as its corresponding preimage angle (m∠A' = m∠A).",
                "Preservation of Collinearity and Betweenness: Points that lie on a straight line in the preimage remain on a straight line in the image.",
                "Preservation of Parallelism: Lines that are parallel in the preimage remain strictly parallel in the image.",
                "Orientation vs. Invariance: Translations and rotations preserve orientation (the clockwise order of vertices). Reflections reverse orientation (mirror flip)."
            ],
            "coordinateNotationRule": "General transformation rule: (x, y) → (x', y'). Under rigid motions, distances d(P, Q) = d(P', Q') for all points P and Q.",
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
                "definition": "A one-to-one mapping that changes the position, orientation, or size of a shape on a coordinate plane.",
                "example": "Translating triangle ABC 5 units right and 3 units up is a geometric transformation."
            },
            {
                "term": "Preimage",
                "definition": "The original geometric figure before any transformation is applied.",
                "example": "In ΔABC → ΔA'B'C', ΔABC is the preimage."
            },
            {
                "term": "Image",
                "definition": "The new figure that results from applying a transformation to a preimage.",
                "example": "In ΔABC → ΔA'B'C', ΔA'B'C' is the image, labeled with prime symbols."
            },
            {
                "term": "Rigid Motion (Isometry)",
                "definition": "A transformation that preserves distance (segment lengths) and angle measures, ensuring the image is congruent to the preimage.",
                "example": "Translations, reflections, and rotations are rigid motions."
            },
            {
                "term": "Non-Rigid Motion",
                "definition": "A transformation that changes the size of a figure (such as a dilation or stretch), altering side lengths.",
                "example": "Enlarging a photograph by multiplying coordinates by 2 is a non-rigid transformation."
            },
            {
                "term": "Orientation",
                "definition": "The order or arrangement of vertices (e.g., clockwise vs. counterclockwise) and the facing direction of a figure.",
                "example": "Translations keep vertex order clockwise; reflections flip clockwise vertices into counterclockwise order."
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

print("Lesson 1.1 built successfully")
