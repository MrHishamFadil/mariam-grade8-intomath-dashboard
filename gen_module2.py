# -*- coding: utf-8 -*-
"""
Module 2 Lessons Generator: Transformations and Similarity (Lessons 2.1 - 2.3)
HMH Into Math Grade 8 Teacher Edition
"""

def get_module2_lessons():
    m2 = {}

    # =========================================================================
    # LESSON 2.1: Investigate Reductions and Enlargements
    # =========================================================================
    m2["2.1"] = {
        "id": "2.1",
        "lessonNumber": "2.1",
        "moduleNumber": 2,
        "moduleId": "module-2",
        "moduleTitle": "Module 2: Transformations and Similarity",
        "title": "Lesson 2.1: Investigate Reductions and Enlargements",
        "introAndConcept": {
            "lessonTitle": "Lesson 2.1: Investigate Reductions and Enlargements",
            "iCanStatement": "I can determine whether a transformation produces an enlargement, a reduction, or a congruent figure, and calculate the scale factor k comparing side lengths.",
            "conceptExplanation": {
                "coreDefinition": "Scaling changes the size of a geometric figure proportionally without altering its shape. The scale factor, denoted by k, is the constant ratio of any side length in the image to its corresponding side length in the preimage: k = (Image Side Length) / (Preimage Side Length).",
                "keyProperties": [
                    "Classification by Scale Factor k:\n  • If k > 1, the image is an Enlargement (larger than the preimage).\n  • If 0 < k < 1, the image is a Reduction (smaller than the preimage).\n  • If k = 1, the image is Congruent (identical size, rigid motion).",
                    "Angle Invariance: Under any proportional scaling, all corresponding angle measures remain strictly congruent (m∠A' = m∠A).",
                    "Perimeter Ratio: The ratio of the perimeters equals the scale factor k: Perimeter(Image) = k × Perimeter(Preimage).",
                    "Area Ratio (k² Effect): The ratio of the areas equals the SQUARE of the scale factor: Area(Image) = k² × Area(Preimage)."
                ],
                "coordinateNotationRule": "Proportional scaling with center at the origin: (x, y) → (kx, ky). Scale factor formula: k = (image dimension) / (preimage dimension).",
                "mathStandards": "CCSS.MATH.CONTENT.8.G.A.3, 8.G.A.4"
            },
            "visualSummarySvg": """<svg viewBox="0 0 420 220" class="concept-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gPre21" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gRed21" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#d97706" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gEnl21" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.45"/>
    </linearGradient>
  </defs>
  <pattern id="grid21" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>
  <rect width="420" height="220" fill="url(#grid21)" rx="8"/>
  <rect x="30" y="90" width="40" height="50" fill="url(#gRed21)" stroke="#d97706" stroke-width="2"/>
  <text x="50" y="80" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">Reduction</text>
  <text x="50" y="118" font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">k = 0.5</text>
  <text x="50" y="155" font-size="9" fill="#64748b" text-anchor="middle">2 cm × 2.5 cm</text>
  <rect x="140" y="65" width="80" height="100" fill="url(#gPre21)" stroke="#0284c7" stroke-width="2.5"/>
  <text x="180" y="55" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">Preimage (Original)</text>
  <text x="180" y="120" font-size="12" font-weight="800" fill="#0c4a6e" text-anchor="middle">k = 1.0</text>
  <text x="180" y="180" font-size="9.5" fill="#64748b" text-anchor="middle">4 cm × 5 cm (Base)</text>
  <rect x="270" y="40" width="120" height="150" fill="url(#gEnl21)" stroke="#059669" stroke-width="2.5"/>
  <text x="330" y="30" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">Enlargement</text>
  <text x="330" y="120" font-size="12" font-weight="800" fill="#064e3b" text-anchor="middle">k = 1.5</text>
  <text x="330" y="205" font-size="9.5" fill="#64748b" text-anchor="middle">6 cm × 7.5 cm</text>
</svg>""",
            "essentialVocabulary": [
                {
                    "term": "Scale Factor (k)",
                    "definition": "The constant ratio comparing any linear measurement of an image to the corresponding measurement of its preimage: k = Image / Preimage.",
                    "example": "If an original 4-inch photo is resized to 12 inches, the scale factor is k = 12/4 = 3."
                },
                {
                    "term": "Enlargement",
                    "definition": "A proportional scaling transformation that produces an image larger than the original preimage (scale factor k > 1).",
                    "example": "Dilating a shape by k = 2.5 is an enlargement."
                },
                {
                    "term": "Reduction",
                    "definition": "A proportional scaling transformation that produces an image smaller than the original preimage (scale factor 0 < k < 1).",
                    "example": "Scaling a blueprint by k = 1/4 is a reduction."
                },
                {
                    "term": "Proportionality",
                    "definition": "The property that corresponding side lengths have equal ratios across the entire geometric figure.",
                    "example": "In similar triangles, side1'/side1 = side2'/side2 = side3'/side3 = k."
                },
                {
                    "term": "Area Multiplier (k²)",
                    "definition": "The mathematical principle stating that when all 1D linear dimensions are scaled by k, the 2D surface area scales by k².",
                    "example": "If a rectangle's dimensions are doubled (k = 2), its area becomes 2² = 4 times as large."
                }
            ]
        },
        "examples": [
            {
                "id": "ex-2.1-1",
                "title": "Example 1: Calculating Scale Factor from Dimensions",
                "description": "An original photograph has dimensions 4 inches by 6 inches. An enlarged poster has dimensions 16 inches by 24 inches. Determine the scale factor k and verify whether the enlargement is proportional.",
                "diagramHtml": "<div class='example-diagram-card'>Preimage: 4 in × 6 in<br>Image: 16 in × 24 in<br>Width ratio: 16 / 4 = 4<br>Height ratio: 24 / 6 = 4<br><strong>Scale Factor k = 4 (Enlargement)</strong></div>",
                "stepByStepExplanation": "1. Find width ratio: k_width = 16 in / 4 in = 4.\n2. Find height ratio: k_height = 24 in / 6 in = 4.\n3. Compare ratios: Both ratios equal 4, proving the enlargement is strictly proportional.\n4. Classify: Since k = 4 > 1, this transformation is an enlargement.",
                "keyTakeaway": "Always compute Image / Preimage. If k > 1, the transformation is an enlargement."
            },
            {
                "id": "ex-2.1-2",
                "title": "Example 2: Determining Area and Perimeter Changes",
                "description": "A square garden plot has side length 5 meters (Perimeter = 20 m, Area = 25 m²). It is enlarged with a scale factor of k = 3. Find the new perimeter and area.",
                "diagramHtml": "<div class='example-diagram-card'>Scale factor k = 3<br>New Side = 5 × 3 = 15 m<br>New Perimeter = 20 × 3 = 60 m (k × P)<br>New Area = 25 × 3² = 25 × 9 = 225 m² (k² × A)</div>",
                "stepByStepExplanation": "1. Calculate new side length: s' = k × s = 3 × 5 m = 15 m.\n2. Calculate new perimeter: P' = 4 × 15 m = 60 m. Notice 60 / 20 = 3 = k.\n3. Calculate new area: A' = (15 m)² = 225 m². Notice 225 / 25 = 9 = 3² = k².\n4. Conclusion: Perimeter scales by k (3×), while area scales by k² (9×).",
                "keyTakeaway": "1D measurements (sides, perimeters) scale by k; 2D measurements (areas) scale by k²."
            }
        ],
        "workedExamplesModelAnswers": [
            {
                "id": "we-2.1-1",
                "problemPrompt": "A graphic artist scales down a company logo. The original triangle has side lengths of 15 cm, 20 cm, and 25 cm. The scaled logo has corresponding side lengths of 6 cm, 8 cm, and 10 cm. (a) Calculate the scale factor k as a simplified fraction and as a decimal. (b) Classify the transformation as an enlargement, reduction, or congruence. (c) If the original logo has an area of 150 cm², calculate the area of the scaled logo.",
                "context": "HMH Into Math TE - Worked Example Model Lesson 2.1",
                "step1": "Identify Given Information: Preimage side lengths = 15 cm, 20 cm, 25 cm. Preimage area = 150 cm². Image side lengths = 6 cm, 8 cm, 10 cm.",
                "step2": "Apply Rule / Formula:\n• Scale factor k = (Image side) / (Preimage side) = 6/15 = 8/20 = 10/25.\n• Simplify fraction: 6/15 = 2/5.\n• Decimal value: 2/5 = 0.4.\n• Classification: Since 0 < k < 1 (0.4 < 1), this transformation is a reduction.\n• Area calculation: Area(Image) = k² × Area(Preimage) = (2/5)² × 150 = (4/25) × 150 = 4 × 6 = 24 cm².",
                "step3": "Write Concluding Mathematical Statement: The scale factor is k = 2/5 (or 0.4). Because 0 < 0.4 < 1, the transformation is a reduction. The area of the scaled logo is 24 cm², which is exactly (2/5)² = 4/25 of the original 150 cm² area.",
                "rubricGuidance": "Full credit: 1 pt for computing k = 2/5 (or 0.4); 1 pt for classifying as reduction; 2 pts for applying k² = 4/25 to find area = 24 cm²."
            },
            {
                "id": "we-2.1-2",
                "problemPrompt": "A rectangular billboard model is created from a blueprint measuring 12 cm by 18 cm. The actual billboard measures 4 meters (400 cm) by 6 meters (600 cm). (a) Determine the scale factor k from the blueprint to the actual billboard. (b) How many times larger is the surface area of the billboard compared to the blueprint?",
                "context": "HMH Into Math TE - Scale Factor Unit Conversion & Area Ratio",
                "step1": "Identify Given Information: Blueprint dimensions: 12 cm by 18 cm. Billboard dimensions: 4 m = 400 cm by 6 m = 600 cm. Convert all measurements to the same units (centimeters).",
                "step2": "Apply Rule / Formula:\n• Width ratio: k = 400 cm / 12 cm = 100/3 ≈ 33.33.\n• Height ratio: k = 600 cm / 18 cm = 100/3 ≈ 33.33.\n• Since both ratios are equal, the scale factor is k = 100/3 (an enlargement).\n• Area ratio = k² = (100/3)² = 10,000 / 9 ≈ 1,111.11 times larger.",
                "step3": "Write Concluding Mathematical Statement: The scale factor is k = 100/3 (or approximately 33.33). The surface area of the actual billboard is (100/3)² = 10,000/9 (approximately 1,111.11 times) greater than the blueprint area.",
                "rubricGuidance": "Full credit: 1 pt for unit conversion to cm; 1 pt for calculating k = 100/3; 2 pts for calculating area ratio k² = 10,000/9."
            }
        ],
        "practiceQuestions": [
            {
                "id": "pq-2.1-1",
                "type": "fill-blank",
                "prompt": "An original photograph has a width of 5 inches. It is enlarged proportionally so the new width is 20 inches. What is the scale factor k?",
                "placeholder": "Enter number (e.g. 4)",
                "acceptedAnswers": ["4", "k=4", "k = 4"],
                "hint": "Scale factor k = (Image width) / (Preimage width) = 20 / 5.",
                "explanation": "k = 20 in / 5 in = 4. The image is 4 times as large as the original, making k = 4."
            },
            {
                "id": "pq-2.1-2",
                "type": "fill-blank",
                "prompt": "A blueprint has a segment length of 18 cm. The reduced copy has a corresponding segment length of 6 cm. What is the scale factor k as a simplified fraction?",
                "placeholder": "Enter fraction (e.g. 1/3)",
                "acceptedAnswers": ["1/3", "1 / 3", "0.33", "0.333"],
                "hint": "k = Image / Preimage = 6 / 18. Simplify by dividing numerator and denominator by 6.",
                "explanation": "k = 6 / 18 = 1/3. Since k < 1, this represents a reduction by a scale factor of 1/3."
            },
            {
                "id": "pq-2.1-3",
                "type": "mcq",
                "prompt": "If a polygon is enlarged by a scale factor of k = 3, by what factor does its surface area increase?",
                "options": [
                    "3 times",
                    "6 times",
                    "9 times",
                    "27 times"
                ],
                "correctIndex": 2,
                "hint": "Remember that area scales by the square of the scale factor: Area Multiplier = k².",
                "explanation": "When all 1D dimensions are multiplied by k = 3, the 2D area is multiplied by k² = 3² = 9. The area becomes 9 times as large."
            },
            {
                "id": "pq-2.1-4",
                "type": "mcq",
                "prompt": "Which of the following scale factors results in a REDUCTION?",
                "options": [
                    "k = 5/4",
                    "k = 1.0",
                    "k = 0.75",
                    "k = 2.5"
                ],
                "correctIndex": 2,
                "hint": "A reduction occurs when the scale factor is strictly between 0 and 1 (0 < k < 1).",
                "explanation": "A reduction requires 0 < k < 1. Here, 0.75 is less than 1. k = 5/4 and 2.5 are enlargements, and k = 1 produces a congruent figure."
            }
        ],
        "bookQuestionBank": [
            {
                "id": "bq-2.1-1",
                "category": "Spark Your Learning",
                "title": "Microscope Amoeba Specimen Magnification",
                "context": "HMH Into Math Grade 8 Teacher Edition, Lesson 2.1 Opening Activity",
                "questionPrompt": "In a biology lab, Mariam views an amoeba under a light microscope. The actual amoeba has a length of 0.25 millimeters. On the digital screen attached to the microscope, the projected image of the amoeba measures 10 millimeters long. (a) Calculate the scale factor k of the microscope projection. (b) Is this transformation an enlargement or a reduction? (c) If the projected image displays a cell nucleus with a diameter of 2.4 mm, what is the actual diameter of the nucleus in the real specimen?",
                "modelAnswer": {
                    "summary": "The microscope magnification scale factor is k = 40 (an enlargement). The actual nucleus diameter is 0.06 mm.",
                    "stepByStep": [
                        "Step 1: Calculate the scale factor: k = (Image dimension) / (Preimage dimension) = 10 mm / 0.25 mm = 40.",
                        "Step 2: Classify the transformation: Since k = 40 > 1, the transformation is an enlargement (40× magnification).",
                        "Step 3: Solve for actual nucleus size: Image = k × Preimage ➔ Preimage = Image / k = 2.4 mm / 40 = 0.06 mm.",
                        "Step 4: Check: 0.06 mm × 40 = 2.4 mm. Proportions hold."
                    ],
                    "fullCreditJustification": "k = 10 / 0.25 = 40. Because k > 1, it is an enlargement. Dividing the 2.4 mm image by 40 yields the true specimen diameter of 0.06 mm.",
                    "rubricCriteria": "1 pt for calculating k = 40; 1 pt for classifying as enlargement; 2 pts for computing the actual nucleus diameter (0.06 mm)."
                }
            },
            {
                "id": "bq-2.1-2",
                "category": "Check Understanding",
                "title": "Smartphone App Icon Billboard Expansion",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.1 Check Understanding Exercise 2",
                "questionPrompt": "A software developer creates an app icon that is a square measuring 2 cm on each side. The marketing team prints an enlarged square banner for a tech expo measuring 150 cm on each side. (a) What is the scale factor k? (b) What is the perimeter of the icon and the banner? Verify the perimeter ratio. (c) By what factor did the area increase?",
                "modelAnswer": {
                    "summary": "The scale factor is k = 75. Icon perimeter = 8 cm, banner perimeter = 600 cm (ratio = 75). Area increased by 75² = 5,625 times.",
                    "stepByStep": [
                        "Step 1: Calculate scale factor: k = 150 cm / 2 cm = 75.",
                        "Step 2: Calculate perimeters: Icon perimeter P = 4 × 2 cm = 8 cm. Banner perimeter P' = 4 × 150 cm = 600 cm. Ratio P'/P = 600 / 8 = 75 = k.",
                        "Step 3: Calculate areas: Icon area A = 2² = 4 cm². Banner area A' = 150² = 22,500 cm².",
                        "Step 4: Area multiplier: A'/A = 22,500 / 4 = 5,625. Verify with k²: 75² = 5,625. Exactly matches!"
                    ],
                    "fullCreditJustification": "k = 75. Perimeter ratio P'/P = 75 = k. Area ratio A'/A = 75² = 5,625 = k². All 1D lengths scale by k, while 2D areas scale by k².",
                    "rubricCriteria": "1 pt for k = 75; 1 pt for perimeters and verification; 2 pts for area ratio 5,625."
                }
            },
            {
                "id": "bq-2.1-3",
                "category": "On Your Own",
                "title": "Architectural Miniature Skyscraper Model",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.1 On Your Own Problem 5",
                "questionPrompt": "An architect builds a scale model of a planned 240-meter skyscraper. The model has a height of 1.2 meters. (a) What is the scale factor k from the actual building to the model? (b) Is this an enlargement or a reduction? (c) If a rectangular observation deck on the actual building has an area of 500 m², what is the area of the observation deck on the model in square centimeters? (Hint: 1 m² = 10,000 cm²)",
                "modelAnswer": {
                    "summary": "The scale factor from building to model is k = 1/200 (a reduction). The model observation deck has an area of 125 cm².",
                    "stepByStep": [
                        "Step 1: Calculate scale factor: k = (Model height) / (Actual height) = 1.2 m / 240 m = 1/200 = 0.005.",
                        "Step 2: Classify: Since 0 < k < 1, this transformation is a reduction.",
                        "Step 3: Calculate model area in m²: Area_model = k² × Area_actual = (1/200)² × 500 m² = (1/40,000) × 500 = 500 / 40,000 = 0.0125 m².",
                        "Step 4: Convert m² to cm²: 0.0125 m² × 10,000 cm²/m² = 125 cm²."
                    ],
                    "fullCreditJustification": "k = 1.2 / 240 = 1/200 (0.005), which is a reduction. The area scales by k² = 1/40,000. 500 m² × (1/40,000) = 0.0125 m² = 125 cm².",
                    "rubricCriteria": "1 pt for k = 1/200; 1 pt for reduction classification; 2 pts for correctly calculating 125 cm²."
                }
            },
            {
                "id": "bq-2.1-4",
                "category": "Test Prep",
                "title": "Standardized Test Prep: Scale Factor from Polygon Table",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.1 Test Prep Problem 11",
                "questionPrompt": "The table below lists corresponding side lengths of two similar pentagons:\nPreimage Side: [4 cm, 6 cm, 8 cm, 10 cm, 12 cm]\nImage Side:    [10 cm, 15 cm, 20 cm, 25 cm, 30 cm]\nWhat is the scale factor of the enlargement?\nA. k = 0.4\nB. k = 2.0\nC. k = 2.5\nD. k = 6.0",
                "modelAnswer": {
                    "summary": "Option C is correct: k = 2.5.",
                    "stepByStep": [
                        "Step 1: Select any pair of corresponding sides: Image = 10 cm, Preimage = 4 cm.",
                        "Step 2: Compute k: k = 10 / 4 = 2.5.",
                        "Step 3: Check remaining pairs:\n• 15 / 6 = 2.5\n• 20 / 8 = 2.5\n• 25 / 10 = 2.5\n• 30 / 12 = 2.5",
                        "Step 4: Conclude: The constant scale factor is k = 2.5 (Option C)."
                    ],
                    "fullCreditJustification": "Scale factor is the constant ratio of image length to preimage length: 10/4 = 15/6 = 2.5. Option C is the correct answer.",
                    "rubricCriteria": "1 pt for selecting C; 1 pt for showing ratio calculation."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 2.2: Explore Dilations
    # =========================================================================
    m2["2.2"] = {
        "id": "2.2",
        "lessonNumber": "2.2",
        "moduleNumber": 2,
        "moduleId": "module-2",
        "moduleTitle": "Module 2: Transformations and Similarity",
        "title": "Lesson 2.2: Explore Dilations",
        "introAndConcept": {
            "lessonTitle": "Lesson 2.2: Explore Dilations",
            "iCanStatement": "I can perform and describe dilations of figures on the coordinate plane using a given center of dilation and scale factor, and write coordinate mapping rules (x, y) → (kx, ky).",
            "conceptExplanation": {
                "coreDefinition": "A dilation is a transformation that changes the size of a geometric figure by a scale factor k relative to a fixed center point called the center of dilation. Rays drawn from the center of dilation through each preimage point pass through the corresponding image points.",
                "keyProperties": [
                    "Ray Collinearity: The center of dilation C, preimage point P, and image point P' all lie on the exact same straight line ray.",
                    "Distance from Center: The distance from the center of dilation to the image point is k times the distance from the center to the preimage point: CP' = k × CP.",
                    "Angle Invariance: Under dilations, all corresponding angles remain strictly congruent (m∠A' = m∠A).",
                    "Parallelism Preserved: Line segments connecting points in the image are parallel to their corresponding segments in the preimage (A'B' || AB), provided the line does not pass through the center of dilation.",
                    "Orientation Preserved: Dilations preserve the clockwise/counterclockwise order of vertices."
                ],
                "coordinateNotationRule": "Coordinate Rule for Dilation Centered at the Origin (0, 0): (x, y) → (kx, ky). For center (a, b): (x, y) → (a + k(x - a), b + k(y - b)).",
                "mathStandards": "CCSS.MATH.CONTENT.8.G.A.3"
            },
            "visualSummarySvg": """<svg viewBox="0 0 420 220" class="concept-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gPre22" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#4338ca" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gImg22" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0891b2" stop-opacity="0.45"/>
    </linearGradient>
  </defs>
  <pattern id="grid22" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>
  <rect width="420" height="220" fill="url(#grid22)" rx="8"/>
  <circle cx="50" cy="180" r="5" fill="#ef4444"/>
  <text x="50" y="200" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">Center C(0,0)</text>
  <line x1="50" y1="180" x2="360" y2="40" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="50" y1="180" x2="380" y2="140" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="50" y1="180" x2="280" y2="180" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <polygon points="120,140 180,140 150,100" fill="url(#gPre22)" stroke="#4f46e5" stroke-width="2"/>
  <circle cx="120" cy="140" r="3" fill="#4f46e5"/><text x="110" y="135" font-size="10" font-weight="700" fill="#312e81">A(2,1)</text>
  <circle cx="180" cy="140" r="3" fill="#4f46e5"/><text x="185" y="145" font-size="10" font-weight="700" fill="#312e81">B(4,1)</text>
  <circle cx="150" cy="100" r="3" fill="#4f46e5"/><text x="145" y="90" font-size="10" font-weight="700" fill="#312e81">C(3,3)</text>
  <polygon points="240,100 360,100 300,20" fill="url(#gImg22)" stroke="#0891b2" stroke-width="2.5"/>
  <circle cx="240" cy="100" r="4" fill="#0891b2"/><text x="230" y="92" font-size="11" font-weight="700" fill="#164e63">A'(4,2)</text>
  <circle cx="360" cy="100" r="4" fill="#0891b2"/><text x="365" y="105" font-size="11" font-weight="700" fill="#164e63">B'(8,2)</text>
  <circle cx="300" cy="20" r="4" fill="#0891b2"/><text x="305" y="15" font-size="11" font-weight="700" fill="#164e63">C'(6,6)</text>
  <rect x="180" y="175" width="220" height="28" rx="5" fill="#ecfeff" stroke="#a5f3fc" stroke-width="1"/>
  <text x="290" y="194" font-size="11" font-family="'JetBrains Mono', monospace" font-weight="700" fill="#0e7490" text-anchor="middle">(x, y) → (2x, 2y) [Scale Factor k = 2]</text>
</svg>""",
            "essentialVocabulary": [
                {
                    "term": "Dilation",
                    "definition": "A transformation that expands or contracts a figure by a scale factor k with respect to a fixed center of dilation.",
                    "example": "Dilating a triangle by k = 3 with center at (0, 0) triples its coordinates: (x, y) → (3x, 3y)."
                },
                {
                    "term": "Center of Dilation",
                    "definition": "The stationary fixed point from which all points are expanded or contracted along projection rays.",
                    "example": "When dilating on a coordinate grid in Grade 8, the center of dilation is almost always the origin (0, 0)."
                },
                {
                    "term": "Projection Rays",
                    "definition": "Lines drawn from the center of dilation passing through preimage points to locate corresponding image points.",
                    "example": "A ray from (0, 0) through (2, 3) passes directly through (6, 9) when k = 3."
                },
                {
                    "term": "Similarity Transformation",
                    "definition": "A transformation or sequence combining rigid motions and dilations; it preserves shape and angles while changing size.",
                    "example": "A dilation followed by a rotation is a similarity transformation."
                },
                {
                    "term": "Non-Rigid Transformation",
                    "definition": "Any transformation that changes distances (segment lengths); dilations are non-rigid transformations.",
                    "example": "A dilation by k = 0.5 halves all side lengths."
                }
            ]
        },
        "examples": [
            {
                "id": "ex-2.2-1",
                "title": "Example 1: Dilating a Triangle Centered at the Origin (k = 2)",
                "description": "Triangle ABC has vertices A(1, 2), B(3, 1), and C(2, 4). Dilate Triangle ABC by a scale factor of k = 2 with center of dilation at the origin (0, 0).",
                "diagramHtml": "<div class='example-diagram-card'>Rule: (x, y) → (2x, 2y)<br>A(1, 2) ➔ A'(2·1, 2·2) = A'(2, 4)<br>B(3, 1) ➔ B'(2·3, 2·1) = B'(6, 2)<br>C(2, 4) ➔ C'(2·2, 2·4) = C'(4, 8)</div>",
                "stepByStepExplanation": "1. Write the algebraic rule for dilation centered at origin: (x, y) → (kx, ky) = (2x, 2y).\n2. Multiply coordinates of A(1, 2) by 2: A'(2, 4).\n3. Multiply coordinates of B(3, 1) by 2: B'(6, 2).\n4. Multiply coordinates of C(2, 4) by 2: C'(4, 8).\n5. Notice that every side length of A'B'C' is exactly 2 times the length of the corresponding side in ABC.",
                "keyTakeaway": "Multiply both x and y by scale factor k when the origin is the center."
            },
            {
                "id": "ex-2.2-2",
                "title": "Example 2: Dilating with a Fractional Scale Factor (k = 0.5)",
                "description": "Rectangle EFGH has vertices E(-6, 4), F(2, 4), G(2, -2), and H(-6, -2). Apply a dilation with scale factor k = 0.5 centered at the origin.",
                "diagramHtml": "<div class='example-diagram-card'>Rule: (x, y) → (0.5x, 0.5y)<br>E(-6, 4) ➔ E'(-3, 2)<br>F(2, 4) ➔ F'(1, 2)<br>G(2, -2) ➔ G'(1, -1)<br>H(-6, -2) ➔ H'(-3, -1)</div>",
                "stepByStepExplanation": "1. Apply rule: (x, y) → (0.5x, 0.5y).\n2. E(-6, 4) ➔ E'(-6 × 0.5, 4 × 0.5) = E'(-3, 2).\n3. F(2, 4) ➔ F'(2 × 0.5, 4 × 0.5) = F'(1, 2).\n4. G(2, -2) ➔ G'(2 × 0.5, -2 × 0.5) = G'(1, -1).\n5. H(-6, -2) ➔ H'(-6 × 0.5, -2 × 0.5) = H'(-3, -1).\n6. The image moves closer to the center of dilation and is half as wide and half as tall.",
                "keyTakeaway": "When 0 < k < 1, all points move closer to the center of dilation."
            }
        ],
        "workedExamplesModelAnswers": [
            {
                "id": "we-2.2-1",
                "problemPrompt": "Trapezoid ABCD has vertices A(1, 1), B(4, 1), C(3, 3), and D(2, 3). It undergoes a dilation centered at the origin with scale factor k = 3. (a) State the coordinate dilation rule. (b) Find the coordinates of A'B'C'D'. (c) Prove that base AB is parallel to base A'B'.",
                "context": "HMH Into Math TE - Worked Example Model Lesson 2.2",
                "step1": "Identify Given Information: Preimage vertices A(1, 1), B(4, 1), C(3, 3), D(2, 3). Dilation center is (0, 0) and scale factor k = 3.",
                "step2": "Apply Rule / Formula:\n• Coordinate rule: (x, y) → (3x, 3y).\n• A(1, 1) → A'(3·1, 3·1) = A'(3, 3)\n• B(4, 1) → B'(3·4, 3·1) = B'(12, 3)\n• C(3, 3) → C'(3·3, 3·3) = C'(9, 9)\n• D(2, 3) → D'(3·2, 3·3) = D'(6, 9)\n• Calculate slopes: Slope(AB) = (1 - 1)/(4 - 1) = 0/3 = 0 (horizontal line).\n• Slope(A'B') = (3 - 3)/(12 - 3) = 0/9 = 0 (horizontal line).",
                "step3": "Write Concluding Mathematical Statement: The coordinate dilation rule is (x, y) → (3x, 3y). The image coordinates are A'(3, 3), B'(12, 3), C'(9, 9), and D'(6, 9). Because both segment AB and segment A'B' have a slope of 0, AB is parallel to A'B' (AB || A'B'). Dilations preserve parallelism.",
                "rubricGuidance": "Full credit: 1 pt for coordinate rule; 2 pts for computing all 4 vertices; 1 pt for slope proof of parallelism."
            },
            {
                "id": "we-2.2-2",
                "problemPrompt": "Triangle PQR is dilated to Triangle P'Q'R'. Preimage vertex P is located at (2, -4) and image vertex P' is located at (5, -10). The center of dilation is the origin (0, 0). (a) Determine the scale factor k. (b) If vertex Q' has coordinates (-7.5, 15), find the coordinates of preimage vertex Q.",
                "context": "HMH Into Math TE - Determining Scale Factor & Inverse Coordinates",
                "step1": "Identify Given Information: Preimage P(2, -4) and Image P'(5, -10). Image Q'(-7.5, 15). Center of dilation is (0, 0).",
                "step2": "Apply Rule / Formula:\n• Find k using x-coordinates: k = x' / x = 5 / 2 = 2.5.\n• Verify using y-coordinates: k = y' / y = -10 / -4 = 2.5. Consistent!\n• General rule: (x, y) → (2.5x, 2.5y).\n• To find preimage vertex Q(x, y) from image Q'(-7.5, 15):\n  x = x' / k = -7.5 / 2.5 = -3.\n  y = y' / k = 15 / 2.5 = 6.",
                "step3": "Write Concluding Mathematical Statement: The scale factor is k = 2.5 (an enlargement). Preimage vertex Q is located at (-3, 6). Check: (-3 × 2.5, 6 × 2.5) = (-7.5, 15), which matches Q'.",
                "rubricGuidance": "Full credit: 2 pts for calculating k = 2.5; 2 pts for finding preimage Q(-3, 6)."
            }
        ],
        "practiceQuestions": [
            {
                "id": "pq-2.2-1",
                "type": "fill-blank",
                "prompt": "Point P(6, -8) undergoes a dilation centered at the origin with scale factor k = 0.5. What are the coordinates of image point P'?",
                "placeholder": "Enter as (x, y)",
                "acceptedAnswers": ["(3, -4)", "(3,-4)", "3, -4", "3,-4"],
                "hint": "Multiply both the x-coordinate (6) and the y-coordinate (-8) by 0.5.",
                "explanation": "Applying (x, y) → (0.5x, 0.5y): x' = 6 × 0.5 = 3; y' = -8 × 0.5 = -4. Thus, P'(3, -4)."
            },
            {
                "id": "pq-2.2-2",
                "type": "fill-blank",
                "prompt": "A dilation centered at the origin maps vertex R(-2, 5) to R'(-8, 20). What is the scale factor k?",
                "placeholder": "Enter number (e.g. 4)",
                "acceptedAnswers": ["4", "k=4", "k = 4"],
                "hint": "Divide the image coordinate by the preimage coordinate: k = -8 / -2 = 20 / 5.",
                "explanation": "k = -8 / (-2) = 4 (and 20 / 5 = 4). The scale factor is k = 4."
            },
            {
                "id": "pq-2.2-3",
                "type": "mcq",
                "prompt": "Triangle XYZ with m∠X = 45° is dilated by a scale factor of k = 1.5. What is the measure of angle X' in the dilated triangle?",
                "options": [
                    "30°",
                    "45°",
                    "67.5°",
                    "90°"
                ],
                "correctIndex": 1,
                "hint": "Dilations change side lengths, but what happens to angle measures?",
                "explanation": "Dilations preserve angle measures. Even though side lengths grow by 1.5×, the angles remain exactly equal: m∠X' = m∠X = 45°."
            },
            {
                "id": "pq-2.2-4",
                "type": "mcq",
                "prompt": "Which statement about dilations on the coordinate plane is FALSE?",
                "options": [
                    "Dilations preserve parallelism of lines",
                    "Dilations preserve orientation of vertices",
                    "Dilations preserve distances between points",
                    "Dilations preserve angle measures"
                ],
                "correctIndex": 2,
                "hint": "Think about what 'rigid motion' means compared to dilations.",
                "explanation": "Dilations do NOT preserve distances between points—they multiply distances by the scale factor k. That is why dilations are non-rigid transformations."
            }
        ],
        "bookQuestionBank": [
            {
                "id": "bq-2.2-1",
                "category": "Spark Your Learning",
                "title": "Flashlight Shadow Puppet Dilation",
                "context": "HMH Into Math Grade 8 Teacher Edition, Lesson 2.2 Opening Investigation",
                "questionPrompt": "A student holds a cardboard triangle cutout 20 cm in front of a point flashlight bulb (acting as the center of dilation at the origin). The triangle is 6 cm tall. The shadow of the triangle is cast onto a wall located 80 cm from the flashlight bulb. (a) What is the scale factor k of the shadow dilation? (b) How tall is the shadow on the wall? (c) Why do the edges of the shadow remain straight lines?",
                "modelAnswer": {
                    "summary": "The scale factor is k = 4. The shadow is 24 cm tall. Dilations preserve collinearity and straight lines.",
                    "stepByStep": [
                        "Step 1: Calculate scale factor from distance ratios: Center to shadow wall = 80 cm; Center to cardboard cutout = 20 cm. Scale factor k = 80 cm / 20 cm = 4.",
                        "Step 2: Calculate shadow height: Height_shadow = k × Height_cutout = 4 × 6 cm = 24 cm.",
                        "Step 3: Explain straight edge invariance: Light travels in straight projection rays radiating from the point source. Dilations preserve collinearity of points, ensuring straight edges in the preimage remain straight in the image."
                    ],
                    "fullCreditJustification": "Distance ratio k = 80/20 = 4. Shadow height = 4 × 6 cm = 24 cm. Dilations preserve angle measures and collinearity, so all edges remain straight.",
                    "rubricCriteria": "1 pt for k = 4; 2 pts for calculating 24 cm; 1 pt for explaining collinearity preservation."
                }
            },
            {
                "id": "bq-2.2-2",
                "category": "Check Understanding",
                "title": "Video Game Minimap Radar Zoom",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.2 Check Understanding Problem 3",
                "questionPrompt": "In an aerial video game, a player's drone is at the origin (0, 0). The heads-up display radar detects three enemy bases forming a triangle at E₁(2, 3), E₂(5, 1), and E₃(4, 7). The player toggles the 2.5× zoom feature, which dilates the map view with center at (0, 0) by k = 2.5. (a) What are the new radar display coordinates of the three bases? (b) If the distance between E₁ and E₂ was originally √13 units, what is the new distance on the zoomed display?",
                "modelAnswer": {
                    "summary": "The zoomed coordinates are E₁'(5, 7.5), E₂'(12.5, 2.5), and E₃'(10, 17.5). The new distance is 2.5√13 units.",
                    "stepByStep": [
                        "Step 1: Apply dilation rule (x, y) → (2.5x, 2.5y):\n• E₁(2, 3) ➔ E₁'(2 × 2.5, 3 × 2.5) = E₁'(5, 7.5)\n• E₂(5, 1) ➔ E₂'(5 × 2.5, 1 × 2.5) = E₂'(12.5, 2.5)\n• E₃(4, 7) ➔ E₃'(4 × 2.5, 7 × 2.5) = E₃'(10, 17.5)",
                        "Step 2: Calculate distance scaling: All lengths scale directly by k = 2.5.\n• New distance E₁'E₂' = k × E₁E₂ = 2.5 × √13 ≈ 9.01 units."
                    ],
                    "fullCreditJustification": "Multiplying coordinates by k = 2.5 yields E₁'(5, 7.5), E₂'(12.5, 2.5), and E₃'(10, 17.5). Segment lengths multiply by k, so the new distance is 2.5√13.",
                    "rubricCriteria": "2 pts for all 3 correct zoomed coordinates; 2 pts for distance scaling 2.5√13."
                }
            },
            {
                "id": "bq-2.2-3",
                "category": "On Your Own",
                "title": "Artist Canvas Stretcher Grid Projection",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.2 On Your Own Problem 8",
                "questionPrompt": "An artist sketches a miniature cartoon character on a coordinate grid with vertices at (1, 1), (3, 1), (3, 4), and (1, 3). She projects the character onto an oil painting canvas using a dilation centered at (0, 0). On the canvas, the vertex originally at (3, 1) appears at (15, 5). (a) What is the scale factor k? (b) Find the canvas coordinates for the remaining three vertices. (c) What is the ratio of the area of the canvas painting to the sketch?",
                "modelAnswer": {
                    "summary": "Scale factor is k = 5. Remaining canvas coordinates are (5, 5), (15, 20), and (5, 15). The painting area is 25 times the sketch area.",
                    "stepByStep": [
                        "Step 1: Find scale factor: k = 15 / 3 = 5 / 1 = 5 (verified: 5 / 1 = 5).",
                        "Step 2: Apply rule (x, y) → (5x, 5y) to all vertices:\n• (1, 1) ➔ (5, 5)\n• (3, 4) ➔ (15, 20)\n• (1, 3) ➔ (5, 15)",
                        "Step 3: Calculate area ratio: Area ratio = k² = 5² = 25.",
                        "Step 4: Conclude: The canvas character is 5 times as tall and wide, and has 25 times the area."
                    ],
                    "fullCreditJustification": "k = 15/3 = 5. Dilating coordinates by 5 yields (5, 5), (15, 20), and (5, 15). The area scales by k² = 25.",
                    "rubricCriteria": "1 pt for k = 5; 2 pts for 3 coordinates; 1 pt for area ratio 25."
                }
            },
            {
                "id": "bq-2.2-4",
                "category": "Test Prep",
                "title": "Standardized Test Prep: Dilation Image Coordinates",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.2 Test Prep Question 14",
                "questionPrompt": "Trapezoid MNOP has coordinates M(-4, 6), N(2, 6), O(4, -2), and P(-2, -2). What are the coordinates of vertex M' after a dilation centered at the origin with a scale factor of k = 3/2?\nA. (-6, 9)\nB. (-8/3, 4)\nC. (-6, 6)\nD. (-4.5, 9)",
                "modelAnswer": {
                    "summary": "Option A is correct: M'(-6, 9).",
                    "stepByStep": [
                        "Step 1: Identify coordinates of M: x = -4, y = 6. Scale factor k = 3/2 = 1.5.",
                        "Step 2: Multiply x-coordinate: x' = -4 × (3/2) = -12/2 = -6.",
                        "Step 3: Multiply y-coordinate: y' = 6 × (3/2) = 18/2 = 9.",
                        "Step 4: Image point M' = (-6, 9), matching Option A."
                    ],
                    "fullCreditJustification": "Applying (x, y) → ((3/2)x, (3/2)y) to M(-4, 6) gives x' = -6 and y' = 9. Option A is the correct answer.",
                    "rubricCriteria": "1 pt for selecting A; 1 pt for showing algebraic multiplication."
                }
            }
        ]
    }

    # =========================================================================
    # LESSON 2.3: Understand and Recognize Similar Figures
    # =========================================================================
    m2["2.3"] = {
        "id": "2.3",
        "lessonNumber": "2.3",
        "moduleNumber": 2,
        "moduleId": "module-2",
        "moduleTitle": "Module 2: Transformations and Similarity",
        "title": "Lesson 2.3: Understand and Recognize Similar Figures",
        "introAndConcept": {
            "lessonTitle": "Lesson 2.3: Understand and Recognize Similar Figures",
            "iCanStatement": "I can determine whether two figures are similar by finding a sequence of transformations (rigid motions plus a dilation) that maps one onto the other, and write similarity statements.",
            "conceptExplanation": {
                "coreDefinition": "Two two-dimensional figures are similar (symbol: ~) if and only if there exists a sequence of transformations comprising rigid motions (translations, reflections, rotations) AND a dilation that maps the preimage exactly onto the image. Similar figures have the exact same shape, but may have different sizes.",
                "keyProperties": [
                    "Fundamental Theorem of Similarity: Figure A ~ Figure B ⇔ A can be mapped to B by a sequence of rigid motions and a dilation.",
                    "Congruent Angles: All corresponding interior angles are strictly equal: m∠A = m∠A', m∠B = m∠B', m∠C = m∠C'.",
                    "Proportional Sides: All corresponding side lengths share the exact same constant ratio k: A'B'/AB = B'C'/BC = C'A'/CA = k.",
                    "Perimeter Ratio: The ratio of perimeters equals the scale factor k: Perimeter(Image) / Perimeter(Preimage) = k.",
                    "Area Ratio: The ratio of areas equals the square of the scale factor k²: Area(Image) / Area(Preimage) = k².",
                    "All Congruent Figures are Similar: Congruence is a special case of similarity where the dilation scale factor is k = 1."
                ],
                "coordinateNotationRule": "Similarity statement: Figure A ~ Figure B (vertex order MUST match corresponding points). Proportionality equation: a'/a = b'/b = c'/c = k. Area ratio: Area' = k² × Area.",
                "mathStandards": "CCSS.MATH.CONTENT.8.G.A.4"
            },
            "visualSummarySvg": """<svg viewBox="0 0 420 220" class="concept-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gPre23" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#6d28d9" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="gSim23" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14b8a6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0f766e" stop-opacity="0.45"/>
    </linearGradient>
  </defs>
  <pattern id="grid23" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>
  <rect width="420" height="220" fill="url(#grid23)" rx="8"/>
  <polygon points="50,160 130,160 130,80" fill="url(#gPre23)" stroke="#7c3aed" stroke-width="2.5"/>
  <text x="90" y="175" font-size="10" font-weight="700" fill="#5b21b6" text-anchor="middle">base = 4</text>
  <text x="145" y="125" font-size="10" font-weight="700" fill="#5b21b6">height = 4</text>
  <text x="75" y="115" font-size="10" font-weight="700" fill="#5b21b6">hyp = 5.66</text>
  <text x="90" y="140" font-size="12" font-weight="800" fill="#4c1d95" text-anchor="middle">ΔABC</text>
  <polygon points="240,170 360,170 360,50" fill="url(#gSim23)" stroke="#0f766e" stroke-width="2.5"/>
  <text x="300" y="186" font-size="10" font-weight="700" fill="#115e59" text-anchor="middle">base = 6 (×1.5)</text>
  <text x="375" y="115" font-size="10" font-weight="700" fill="#115e59">height = 6 (×1.5)</text>
  <text x="280" y="100" font-size="10" font-weight="700" fill="#115e59">hyp = 8.49 (×1.5)</text>
  <text x="320" y="140" font-size="12" font-weight="800" fill="#134e4a" text-anchor="middle">ΔDEF</text>
  <path d="M 70,160 A 20 20 0 0 0 65,145" fill="none" stroke="#dc2626" stroke-width="2"/>
  <text x="75" y="152" font-size="9" font-weight="700" fill="#dc2626">45°</text>
  <path d="M 270,170 A 30 30 0 0 0 262,148" fill="none" stroke="#dc2626" stroke-width="2"/>
  <text x="275" y="158" font-size="9" font-weight="700" fill="#dc2626">45°</text>
  <rect x="40" y="10" width="340" height="28" rx="6" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.2"/>
  <text x="210" y="28" font-size="11" font-weight="700" fill="#115e59" text-anchor="middle">ΔABC ~ ΔDEF : Angles ≅ (Equal) | Sides Proportional (k = 1.5)</text>
</svg>""",
            "essentialVocabulary": [
                {
                    "term": "Similar Figures",
                    "definition": "Figures that have identical angle measures and proportional corresponding side lengths; they have the same shape but may differ in size.",
                    "example": "All circles are similar to one another; all squares are similar to one another."
                },
                {
                    "term": "Similarity Symbol (~)",
                    "definition": "The tilde symbol used to express that two geometric figures are similar.",
                    "example": "ΔABC ~ ΔDEF means Triangle ABC is similar to Triangle DEF."
                },
                {
                    "term": "Similarity Transformation",
                    "definition": "A composite sequence of transformations including at least one dilation and any number of rigid motions.",
                    "example": "A dilation followed by a translation is a similarity transformation."
                },
                {
                    "term": "Indirect Measurement",
                    "definition": "A technique that uses proportional reasoning with similar figures to find distances or heights that are difficult to measure directly.",
                    "example": "Using shadow lengths and similar triangles to find the height of a tall flagpole."
                },
                {
                    "term": "Corresponding Angles & Sides",
                    "definition": "Angles and sides in the same relative position in two similar polygons; angles are equal, and sides have equal ratios.",
                    "example": "If ΔABC ~ ΔXYZ, then ∠A ≅ ∠X and AB/XY = BC/YZ."
                }
            ]
        },
        "examples": [
            {
                "id": "ex-2.3-1",
                "title": "Example 1: Verifying Similarity Using Angle Measures and Side Ratios",
                "description": "Triangle ABC has side lengths 6, 8, 10 and angles 37°, 53°, 90°. Triangle DEF has side lengths 9, 12, 15 and angles 37°, 53°, 90°. Determine whether ΔABC is similar to ΔDEF.",
                "diagramHtml": "<div class='example-diagram-card'>Angles: 37°=37°, 53°=53°, 90°=90° (Congruent)<br>Side ratios: 9/6 = 1.5, 12/8 = 1.5, 15/10 = 1.5<br><strong>Conclusion: ΔABC ~ ΔDEF (Scale factor k = 1.5)</strong></div>",
                "stepByStepExplanation": "1. Check corresponding angles: All 3 pairs of corresponding angles are congruent: 37° = 37°, 53° = 53°, 90° = 90°.\n2. Check side length ratios: DE/AB = 9/6 = 1.5; EF/BC = 12/8 = 1.5; DF/AC = 15/10 = 1.5.\n3. Compare ratios: All side ratios are equal to the common scale factor k = 1.5.\n4. Conclude: Because corresponding angles are congruent and corresponding side lengths are proportional, ΔABC ~ ΔDEF.",
                "keyTakeaway": "Similarity requires two conditions: (1) Corresponding angles are congruent, and (2) Corresponding sides are proportional."
            },
            {
                "id": "ex-2.3-2",
                "title": "Example 2: Solving for Missing Side Lengths in Similar Polygons",
                "description": "Quadrilateral ABCD is similar to Quadrilateral EFGH. Side AB = 8 cm, BC = 12 cm. In EFGH, side EF = 20 cm. Find the length of corresponding side FG.",
                "diagramHtml": "<div class='example-diagram-card'>Proportion: AB / EF = BC / FG<br>8 / 20 = 12 / FG<br>Cross multiply: 8 × FG = 20 × 12 = 240<br><strong>FG = 240 / 8 = 30 cm</strong></div>",
                "stepByStepExplanation": "1. Write the similarity proportion comparing matching sides: AB / EF = BC / FG.\n2. Substitute known values: 8 / 20 = 12 / FG.\n3. Cross-multiply: 8 × FG = 20 × 12 = 240.\n4. Divide by 8: FG = 240 / 8 = 30 cm.\n5. Alternative scale factor method: k = 20 / 8 = 2.5. FG = 12 × 2.5 = 30 cm.",
                "keyTakeaway": "Use cross-multiplication or multiply by scale factor k to solve for unknown sides."
            }
        ],
        "workedExamplesModelAnswers": [
            {
                "id": "we-2.3-1",
                "problemPrompt": "On a coordinate grid, Triangle 1 has vertices at (1, 1), (3, 1), and (1, 4). Triangle 2 has vertices at (-2, -2), (-6, -2), and (-2, -8). (a) Identify a sequence of transformations that maps Triangle 1 onto Triangle 2. (b) State whether Triangle 1 is similar to Triangle 2. (c) Write a formal similarity statement.",
                "context": "HMH Into Math TE - Worked Example Model Lesson 2.3",
                "step1": "Identify Given Information: Triangle 1 vertices A(1, 1), B(3, 1), C(1, 4). Triangle 2 vertices D(-2, -2), E(-6, -2), F(-2, -8). Both are right triangles.",
                "step2": "Apply Rule / Formula:\n• Compare dimensions: Triangle 1 base AB = 2, height AC = 3. Triangle 2 base DE = 4, height DF = 6.\n• Scale factor k = 4/2 = 6/3 = 2.\n• Dilation step: Dilate Triangle 1 by k = 2 with center at origin: (x, y) → (2x, 2y), giving A'(2, 2), B'(6, 2), and C'(2, 8).\n• Rotation step: Notice all coordinates in Triangle 2 have opposite signs: (-2, -2), (-6, -2), (-2, -8). Apply a 180° rotation about the origin: (x, y) → (-x, -y).",
                "step3": "Write Concluding Mathematical Statement: A sequence of transformations that maps Triangle 1 onto Triangle 2 is: (1) A dilation centered at the origin with scale factor k = 2, followed by (2) A 180° rotation about the origin. Because Triangle 2 can be obtained from Triangle 1 through a similarity transformation (dilation and rigid motion), Triangle 1 is similar to Triangle 2: ΔABC ~ ΔDEF.",
                "rubricGuidance": "Full credit: 2 pts for describing valid 2-step sequence (dilation k=2 + 180° rotation); 1 pt for calculating scale factor k = 2; 1 pt for formal similarity statement."
            },
            {
                "id": "we-2.3-2",
                "problemPrompt": "Mariam stands next to a tall palm tree on a sunny afternoon to measure its height indirectly. Mariam is 1.5 meters tall and casts a shadow that is 2.0 meters long. At the exact same moment, the palm tree casts a shadow that is 14.0 meters long. (a) Explain why the triangle formed by Mariam and her shadow is similar to the triangle formed by the palm tree and its shadow. (b) Calculate the height of the palm tree.",
                "context": "HMH Into Math TE - Real-World Indirect Measurement",
                "step1": "Identify Given Information: Mariam's height h₁ = 1.5 m, shadow s₁ = 2.0 m. Palm tree height h₂ = ?, shadow s₂ = 14.0 m.",
                "step2": "Apply Rule / Theorem (Angle-Angle Similarity):\n• Both Mariam and the palm tree stand perpendicular to the ground, forming 90° right angles with their shadows.\n• The sun's rays hit the ground at the exact same angle of elevation at the same time and location, making the angle of the sun identical in both triangles.\n• By Angle-Angle (AA) criterion, the two right triangles are similar.\n• Set up proportion: h₂ / h₁ = s₂ / s₁ ➔ h₂ / 1.5 = 14.0 / 2.0.\n• Simplify right side: 14.0 / 2.0 = 7.0.\n• Solve for h₂: h₂ = 1.5 × 7.0 = 10.5 meters.",
                "step3": "Write Concluding Mathematical Statement: The triangles are similar by AA similarity because they share a 90° angle and congruent sun elevation angles. The scale factor from Mariam to the tree is k = 14.0 / 2.0 = 7.0. Therefore, the palm tree is 1.5 × 7 = 10.5 meters tall.",
                "rubricGuidance": "Full credit: 1 pt for explaining AA similarity (right angle + sun angle); 2 pts for setting up proportion; 1 pt for computing height = 10.5 m."
            }
        ],
        "practiceQuestions": [
            {
                "id": "pq-2.3-1",
                "type": "fill-blank",
                "prompt": "Triangle ABC is similar to Triangle DEF (ΔABC ~ ΔDEF). If AB = 6 cm, BC = 8 cm, and corresponding side DE = 15 cm, what is the length of side EF in centimeters?",
                "placeholder": "Enter number (e.g. 20)",
                "acceptedAnswers": ["20", "20 cm", "20cm"],
                "hint": "Set up the proportion: AB / DE = BC / EF. So 6 / 15 = 8 / EF.",
                "explanation": "6 / 15 = 8 / EF. Cross multiply: 6 × EF = 15 × 8 = 120. EF = 120 / 6 = 20 cm."
            },
            {
                "id": "pq-2.3-2",
                "type": "mcq",
                "prompt": "If two geometric figures are SIMILAR, which statement must ALWAYS be true?",
                "options": [
                    "Corresponding angles are congruent and corresponding sides are proportional",
                    "Corresponding side lengths and corresponding angles are all equal",
                    "The two figures have the exact same perimeter and area",
                    "The figures can only be mapped using translations and reflections"
                ],
                "correctIndex": 0,
                "hint": "Similar means same shape, but possibly different size. Angles stay equal, sides scale proportionally.",
                "explanation": "By definition, similar figures have strictly congruent corresponding angles and proportional corresponding side lengths."
            },
            {
                "id": "pq-2.3-3",
                "type": "fill-blank",
                "prompt": "Polygon P has an area of 12 cm². It is dilated by a scale factor of k = 3 to create similar Polygon Q. What is the area of Polygon Q in cm²?",
                "placeholder": "Enter number (e.g. 108)",
                "acceptedAnswers": ["108", "108 cm^2", "108 sq cm", "108cm2"],
                "hint": "Remember that Area(Image) = k² × Area(Preimage). Here k² = 3² = 9.",
                "explanation": "Area(Q) = k² × Area(P) = 3² × 12 = 9 × 12 = 108 cm²."
            },
            {
                "id": "pq-2.3-4",
                "type": "mcq",
                "prompt": "Is every pair of congruent figures also considered similar?",
                "options": [
                    "Yes, they are similar with a scale factor of k = 1",
                    "No, congruent figures cannot be similar",
                    "Only if they are equilateral triangles",
                    "Only if they are located in the same quadrant"
                ],
                "correctIndex": 0,
                "hint": "Congruence preserves angles and has equal side lengths (ratio 1:1).",
                "explanation": "Congruence is a special case of similarity where the scale factor is exactly k = 1. Corresponding angles are congruent and side ratios are 1."
            }
        ],
        "bookQuestionBank": [
            {
                "id": "bq-2.3-1",
                "category": "Spark Your Learning",
                "title": "Thales' Great Pyramid Shadow Calculation",
                "context": "HMH Into Math Grade 8 Teacher Edition, Lesson 2.3 Opening Historical Problem",
                "questionPrompt": "The ancient Greek mathematician Thales measured the height of the Great Pyramid of Giza by placing his walking staff vertically in the sand. Thales' staff was 2 meters tall and cast a shadow of 3 meters. At that exact moment, the shadow of the Great Pyramid (measured from its center apex point to the tip of its shadow) measured 219 meters. (a) Explain how similar triangles allow this indirect measurement. (b) Calculate the height of the Great Pyramid.",
                "modelAnswer": {
                    "summary": "Using AA similarity, the ratio of height to shadow is constant. The Great Pyramid is 146 meters tall.",
                    "stepByStep": [
                        "Step 1: Justify similarity: Both the staff and the pyramid form right angles (90°) with the ground. The sun rays strike both objects at identical angles of elevation. By AA similarity, the two triangles are similar.",
                        "Step 2: Set up proportion comparing height to shadow length: Height_pyramid / Shadow_pyramid = Height_staff / Shadow_staff.",
                        "Step 3: Substitute values: H / 219 = 2 / 3.",
                        "Step 4: Solve for H: H = (2/3) × 219 = 2 × 73 = 146 meters.",
                        "Step 5: Verify: 146 / 219 = 2 / 3. Proportions are strictly equal."
                    ],
                    "fullCreditJustification": "By AA similarity, the triangles formed by the staff and pyramid are similar. Height / Shadow = 2 / 3. Solving H / 219 = 2 / 3 yields H = 146 meters.",
                    "rubricCriteria": "2 pts for geometric justification of AA similarity; 2 pts for setting up and solving proportion to find 146 m."
                }
            },
            {
                "id": "bq-2.3-2",
                "category": "Check Understanding",
                "title": "Satellite Aerial Survey vs. Topographic Map",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.3 Check Understanding Problem 4",
                "questionPrompt": "A cartographer compares a satellite aerial photo of an island reservoir to an official topographic map. On the satellite photo, the triangular reservoir has vertices at (2, 4), (8, 4), and (8, 12). On the map, the reservoir vertices are at (1, 2), (4, 2), and (4, 6). (a) Describe the transformation that maps the map image to the satellite photo. (b) Are the two representations similar? Provide side length proofs.",
                "modelAnswer": {
                    "summary": "The satellite photo is a dilation of the map with scale factor k = 2 centered at the origin. They are similar because corresponding side lengths have ratio 2:1 and angles are equal.",
                    "stepByStep": [
                        "Step 1: Compare coordinates from map to satellite:\n• (1, 2) ➔ (2, 4) [× 2]\n• (4, 2) ➔ (8, 4) [× 2]\n• (4, 6) ➔ (8, 12) [× 2]\n• The transformation is a dilation: (x, y) → (2x, 2y) with center (0, 0) and k = 2.",
                        "Step 2: Measure side lengths of map triangle: Base = 4 - 1 = 3 units; Height = 6 - 2 = 4 units; Hypotenuse = √(3² + 4²) = 5 units.",
                        "Step 3: Measure side lengths of satellite triangle: Base = 8 - 2 = 6 units; Height = 12 - 4 = 8 units; Hypotenuse = √(6² + 8²) = 10 units.",
                        "Step 4: Check ratios: 6/3 = 8/4 = 10/5 = 2. Ratios are constant (k = 2) and both have a right angle at vertex (4, 2) / (8, 4)."
                    ],
                    "fullCreditJustification": "The transformation is a dilation with k = 2. Side lengths are in proportion (6:3, 8:4, 10:5 = 2), and corresponding right angles are equal. Therefore, the two representations are similar.",
                    "rubricCriteria": "2 pts for identifying dilation rule (2x, 2y); 2 pts for calculating side lengths (3, 4, 5 vs 6, 8, 10) and proving similarity."
                }
            },
            {
                "id": "bq-2.3-3",
                "category": "On Your Own",
                "title": "Aspect Ratio Photo Resizing vs Distortion",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.3 On Your Own Problem 7",
                "questionPrompt": "A photographer takes a rectangular photo with dimensions 8 inches by 12 inches (aspect ratio 2:3). She prepares two sample prints for a magazine:\n• Print A: 12 inches by 18 inches\n• Print B: 12 inches by 16 inches\nDetermine which print is similar to the original photo and which print distorted the image. Explain using scale factor and ratio proofs.",
                "modelAnswer": {
                    "summary": "Print A is similar (scale factor k = 1.5). Print B is distorted because its width and height were scaled by different factors.",
                    "stepByStep": [
                        "Step 1: Test Print A (12 in × 18 in):\n• Width ratio: 12 / 8 = 1.5\n• Height ratio: 18 / 12 = 1.5\n• Since both ratios equal 1.5, Print A is similar to the original with k = 1.5. Aspect ratio 2:3 is preserved.",
                        "Step 2: Test Print B (12 in × 16 in):\n• Width ratio: 12 / 8 = 1.5\n• Height ratio: 16 / 12 = 1.33...\n• Since 1.5 ≠ 1.33, the dimensions are not proportional.",
                        "Step 3: Conclude: Print A preserved similarity and looks crisp and undistorted. Print B stretched width more than height, resulting in image distortion."
                    ],
                    "fullCreditJustification": "Similar figures require all corresponding dimensions to scale by the same factor k. For Print A, 12/8 = 18/12 = 1.5 (similar). For Print B, 12/8 ≠ 16/12 (not similar, distorted).",
                    "rubricCriteria": "2 pts for testing Print A and finding k = 1.5; 2 pts for testing Print B and showing unequal ratios."
                }
            },
            {
                "id": "bq-2.3-4",
                "category": "Test Prep",
                "title": "Standardized Test Prep: Coordinate Similarity Verification",
                "context": "HMH Into Math Grade 8 TE, Lesson 2.3 Test Prep Problem 15",
                "questionPrompt": "Which sequence of transformations proves that Triangle PQR is similar to Triangle P''Q''R'' on a coordinate grid?\nA. A reflection across the y-axis followed by a translation 4 units down\nB. A rotation of 90° clockwise followed by a dilation with scale factor 0.5\nC. A horizontal stretch of factor 2 followed by a translation\nD. A vertical shear followed by a reflection across the line y = x",
                "modelAnswer": {
                    "summary": "Option B is correct: A rotation of 90° clockwise followed by a dilation with scale factor 0.5.",
                    "stepByStep": [
                        "Step 1: Recall the definition of similarity: Two figures are similar if and only if they can be related by a sequence of rigid motions (translations, reflections, rotations) AND dilations.",
                        "Step 2: Evaluate Option A: Contains only rigid motions; this proves congruence, not a general similarity with size change.",
                        "Step 3: Evaluate Option B: A rotation (rigid motion) combined with a dilation is the textbook definition of a similarity transformation! Correct.",
                        "Step 4: Evaluate Options C and D: Stretches and shears distort angles and are non-similarity transformations."
                    ],
                    "fullCreditJustification": "A similarity transformation requires rigid motions combined with a dilation. Option B describes a rotation and a dilation, which preserves shape and angle measures while scaling size. Option B is correct.",
                    "rubricCriteria": "1 pt for selecting B; 1 pt for justification based on similarity transformation definition."
                }
            }
        ]
    }

    return m2

if __name__ == "__main__":
    m2 = get_module2_lessons()
    print("Module 2 lessons generated successfully:", list(m2.keys()))
