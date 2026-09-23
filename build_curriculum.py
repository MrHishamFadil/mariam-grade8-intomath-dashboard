import json

data = {
    "studentProfile": {
        "name": "Mariam Hisham AbdelFadil",
        "grade": "Grade 8",
        "program": "HMH Into Math",
        "unit": "Unit 1: Transformational Geometry",
        "targetStandard": "Common Core State Standards (CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.2, 8.G.A.3, 8.G.A.4)"
    },
    "modules": [
        {
            "id": "module-1",
            "number": 1,
            "title": "Transformations and Congruence",
            "subtitle": "Rigid Motions, Mapping Rules, and Congruence Proofs",
            "badge": "Module 1",
            "themeColor": "#4F46E5",
            "lessons": [
                {
                    "id": "lesson-1.1",
                    "number": "1.1",
                    "title": "Investigate Transformations",
                    "canDoStatement": "I can describe what happens to the side lengths, angle measures, and parallelism of a figure when it undergoes a transformation.",
                    "learningObjective": "Explore and observe the properties of rigid motions (translations, reflections, rotations) on geometric figures.",
                    "keyVocabulary": [
                        {
                            "term": "Transformation",
                            "definition": "An operation that maps an original geometric figure (preimage) onto a new figure (image) in a coordinate plane or space.",
                            "example": "Translating a triangle 4 units right and 2 units up is a geometric transformation."
                        },
                        {
                            "term": "Rigid Motion (Isometry)",
                            "definition": "A transformation that preserves both side lengths and angle measures. The shape and size remain unchanged.",
                            "example": "Translations, reflections, and rotations are rigid motions; dilations are not."
                        },
                        {
                            "term": "Preimage & Image",
                            "definition": "The preimage is the original geometric figure before transformation. The image is the new figure produced after transformation.",
                            "example": "Triangle ABC is the preimage; Triangle A'B'C' is the resulting image."
                        },
                        {
                            "term": "Orientation",
                            "definition": "The order or arrangement of vertices (clockwise vs. counterclockwise) and the direction a figure faces.",
                            "example": "Translations and rotations preserve orientation; reflections reverse orientation (flip clockwise to counterclockwise)."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Rigid Motion Invariance",
                            "formula": "Length(A'B') = Length(AB), m∠A' = m∠A",
                            "description": "Distances, angle measures, and parallel relationships are strictly preserved under all rigid motions."
                        }
                    ],
                    "keyTakeaways": [
                        "Rigid motions include translations, reflections, and rotations.",
                        "Rigid motions preserve side lengths, angle measures, betweenness of points, and parallelism of lines.",
                        "Orientation (vertex order) is preserved by translations and rotations, but reversed by reflections.",
                        "Figures that can be mapped to one another via rigid motions are congruent."
                    ],
                    "interactivePrompts": [
                        "Compare the perimeter and area of a polygon before and after a translation or rotation. Why must they stay identical?",
                        "Trace the vertices of Triangle ABC in clockwise order. When reflected across a line, what order do A', B', and C' follow?"
                    ]
                },
                {
                    "id": "lesson-1.2",
                    "number": "1.2",
                    "title": "Explore Translations",
                    "canDoStatement": "I can translate figures on the coordinate plane, describe translations using words and mapping notation, and determine an algebraic rule.",
                    "learningObjective": "Translate figures along vectors and represent shifts algebraically using coordinate mapping rules.",
                    "keyVocabulary": [
                        {
                            "term": "Translation",
                            "definition": "A rigid transformation that slides every point of a figure the exact same distance in the exact same direction along a straight line.",
                            "example": "Sliding a rectangle 5 units to the right and 3 units down."
                        },
                        {
                            "term": "Mapping Notation",
                            "definition": "A symbolic mathematical rule showing how coordinates change: (x, y) → (x + a, y + b).",
                            "example": "(x, y) → (x + 3, y - 5) slides points 3 units right and 5 units down."
                        },
                        {
                            "term": "Prime Notation",
                            "definition": "The use of the prime symbol (') on letter labels to denote the image of corresponding original vertices.",
                            "example": "Point A(1, 2) maps to A'(4, 7)."
                        },
                        {
                            "term": "Vector / Translation Component",
                            "definition": "The horizontal shift (a) and vertical shift (b) applied to every coordinate.",
                            "example": "Positive a shifts right, negative a shifts left; positive b shifts up, negative b shifts down."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Translation Rule",
                            "formula": "(x, y) → (x + a, y + b)",
                            "description": "a > 0 shifts right, a < 0 shifts left; b > 0 shifts up, b < 0 shifts down."
                        }
                    ],
                    "keyTakeaways": [
                        "Translations preserve size, shape, side lengths, angle measures, and orientation.",
                        "Every segment connecting a preimage point to its image point is parallel and equal in length.",
                        "To find the image coordinates, add the horizontal shift to x and the vertical shift to y."
                    ],
                    "interactivePrompts": [
                        "If a point starts at (-4, 2) and ends at (1, -3), what algebraic mapping rule was applied?",
                        "Does applying a translation ever change the slope of a line segment? Why or why not?"
                    ]
                },
                {
                    "id": "lesson-1.3",
                    "number": "1.3",
                    "title": "Explore Reflections",
                    "canDoStatement": "I can reflect a figure over either axis or a vertical/horizontal line in the coordinate plane and describe the reflection algebraically.",
                    "learningObjective": "Identify and perform reflections across lines of reflection, applying coordinate rules and observing orientation reversal.",
                    "keyVocabulary": [
                        {
                            "term": "Reflection",
                            "definition": "A rigid transformation that flips a figure across a line called the line of reflection, creating a mirror image.",
                            "example": "Flipping a polygon across the x-axis or y-axis."
                        },
                        {
                            "term": "Line of Reflection",
                            "definition": "The perpendicular bisector of the segment connecting each preimage point to its corresponding image point.",
                            "example": "If A is at (2, 3) and A' is at (2, -3), the line of reflection is the x-axis (y = 0)."
                        },
                        {
                            "term": "Orientation Reversal",
                            "definition": "The reversal of vertex winding order from clockwise to counterclockwise (or vice versa) caused by flipping.",
                            "example": "Looking at an ambulance sign or a mirror reflection."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Reflection across x-axis",
                            "formula": "(x, y) → (x, -y)",
                            "description": "The x-coordinate stays unchanged; the y-coordinate changes sign."
                        },
                        {
                            "name": "Reflection across y-axis",
                            "formula": "(x, y) → (-x, y)",
                            "description": "The x-coordinate changes sign; the y-coordinate stays unchanged."
                        },
                        {
                            "name": "Reflection across vertical line x = k",
                            "formula": "(x, y) → (2k - x, y)",
                            "description": "Distance to x = k is preserved on the opposite side."
                        },
                        {
                            "name": "Reflection across horizontal line y = k",
                            "formula": "(x, y) → (x, 2k - y)",
                            "description": "Distance to y = k is preserved on the opposite side."
                        }
                    ],
                    "keyTakeaways": [
                        "Points on the line of reflection remain invariant: they map onto themselves.",
                        "The distance from any point in the preimage to the line of reflection equals the distance from its image point to the line of reflection.",
                        "Reflections preserve lengths, angle measures, and parallelism, but reverse orientation."
                    ],
                    "interactivePrompts": [
                        "What happens to vertex B(-3, -5) when reflected across the line y-axis? What if reflected across the x-axis?",
                        "Why does the line of reflection always form a perpendicular bisector to segment PP'?"
                    ]
                },
                {
                    "id": "lesson-1.4",
                    "number": "1.4",
                    "title": "Explore Rotations",
                    "canDoStatement": "I can identify and perform rotations about the origin, describe rotations algebraically, and determine image coordinates.",
                    "learningObjective": "Rotate figures clockwise and counterclockwise about the origin (0,0) by 90°, 180°, and 270° using algebraic coordinate rules.",
                    "keyVocabulary": [
                        {
                            "term": "Rotation",
                            "definition": "A rigid transformation that turns every point of a figure by a specified angle and direction about a fixed point.",
                            "example": "Rotating a pinwheel or clock hand."
                        },
                        {
                            "term": "Center of Rotation",
                            "definition": "The fixed point about which a figure rotates. In Grade 8 Into Math, this is predominantly the origin (0, 0).",
                            "example": "Point (0, 0) does not move during a rotation centered at the origin."
                        },
                        {
                            "term": "Angle of Rotation & Direction",
                            "definition": "The measure of rotation in degrees and the direction: Clockwise (CW, with clock hands) or Counterclockwise (CCW, against clock hands).",
                            "example": "A 90° clockwise rotation is equivalent to a 270° counterclockwise rotation."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "90° Clockwise / 270° Counterclockwise",
                            "formula": "(x, y) → (y, -x)",
                            "description": "Swap coordinates and negate the new second coordinate."
                        },
                        {
                            "name": "180° Rotation (CW or CCW)",
                            "formula": "(x, y) → (-x, -y)",
                            "description": "Negate both x and y coordinates. Direction (CW vs CCW) produces identical results."
                        },
                        {
                            "name": "270° Clockwise / 90° Counterclockwise",
                            "formula": "(x, y) → (-y, x)",
                            "description": "Swap coordinates and negate the new first coordinate."
                        }
                    ],
                    "keyTakeaways": [
                        "Rotations preserve lengths, angles, parallelism, and orientation.",
                        "A 180° rotation is identical whether performed clockwise or counterclockwise.",
                        "Each 90° turn moves points to an adjacent quadrant.",
                        "Circular distance to the center of rotation remains constant for all points."
                    ],
                    "interactivePrompts": [
                        "If point P(3, -4) is rotated 90° counterclockwise about the origin, where does P' land? Walk through the coordinate swap and sign change.",
                        "Why is rotating 180° clockwise equivalent to reflecting across the origin?"
                    ]
                },
                {
                    "id": "lesson-1.5",
                    "number": "1.5",
                    "title": "Understand and Recognize Congruent Figures",
                    "canDoStatement": "I can determine congruence by performing or describing a sequence of rigid transformations that maps one figure onto another.",
                    "learningObjective": "Prove two figures are congruent by identifying a sequence of translations, reflections, and rotations mapping one directly onto the other.",
                    "keyVocabulary": [
                        {
                            "term": "Congruent Figures (≅)",
                            "definition": "Two figures are congruent if and only if there exists a sequence of rigid transformations that maps one figure exactly onto the other.",
                            "example": "Triangle ABC ≅ Triangle DEF means AB=DE, BC=EF, AC=DF, and all corresponding angles are equal."
                        },
                        {
                            "term": "Sequence of Transformations",
                            "definition": "Performing two or more transformations in succession. Order can sometimes affect the final position.",
                            "example": "First translate (x+2, y), then reflect across the x-axis."
                        },
                        {
                            "term": "Corresponding Parts",
                            "definition": "The sides and angles that occupy identical relative positions in two congruent or similar geometric figures.",
                            "example": "In △ABC ≅ △XYZ, side AB corresponds to side XY, and ∠B corresponds to ∠Y."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Congruence Definition",
                            "formula": "Figure A ≅ Figure B ⟺ Sequence of Rigid Motions(A) = B",
                            "description": "Preservation of all side lengths, perimeters, angle measures, and areas."
                        }
                    ],
                    "keyTakeaways": [
                        "If two figures have different side lengths or angle measures, they cannot be congruent.",
                        "A single reflection or an odd number of reflections reverses orientation; translations and rotations keep orientation unchanged.",
                        "Always write congruence statements in matching vertex correspondence: △ABC ≅ △DEF implies vertex A maps to D, B to E, and C to F."
                    ],
                    "interactivePrompts": [
                        "Figure 1 has clockwise vertex ordering and Figure 2 has counterclockwise vertex ordering. Must the sequence of transformations contain a reflection? Explain.",
                        "If △ABC ≅ △DEF and m∠A = 42°, m∠B = 68°, what is m∠F?"
                    ]
                },
                {
                    "id": "module-1-review",
                    "number": "1.R",
                    "title": "Module 1 Review & Performance Assessment",
                    "canDoStatement": "I can synthesize translations, reflections, and rotations to solve multi-step coordinate geometry challenges and justify congruence.",
                    "learningObjective": "Master all Unit 1 Module 1 standards, verify rigid motion properties, and execute composite transformations.",
                    "keyVocabulary": [
                        {
                            "term": "Composite Transformation",
                            "definition": "Combining multiple transformations consecutively where the image of the first transformation becomes the preimage for the second.",
                            "example": "(x, y) → (x-4, y+1) followed by (x, y) → (x, -y)."
                        },
                        {
                            "term": "Rigid Invariance Proof",
                            "definition": "Using distance and angle conservation to formally demonstrate congruence.",
                            "example": "Because distance and angles are preserved under translations and rotations, the figures are congruent."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Transformation Summary Matrix",
                            "formula": "Translation: (x+a, y+b) | Reflection x-axis: (x,-y) | Reflection y-axis: (-x,y) | Rotation 180°: (-x,-y)",
                            "description": "All Module 1 coordinate mapping rules."
                        }
                    ],
                    "keyTakeaways": [
                        "Always apply multi-step transformations in strict sequential order.",
                        "Check vertex labels carefully to match corresponding sides and angles.",
                        "All Module 1 transformations maintain 100% scale (scale factor = 1)."
                    ],
                    "interactivePrompts": [
                        "Given triangle RST with R(1, 2), S(4, 2), T(1, 6), apply a 90° CW rotation about (0,0) followed by a translation of (x-2, y+3). List intermediate and final coordinates."
                    ]
                }
            ]
        },
        {
            "id": "module-2",
            "number": 2,
            "title": "Transformations and Similarity",
            "subtitle": "Dilations, Scale Factors, Proportions, and Similarity Statements",
            "badge": "Module 2",
            "themeColor": "#059669",
            "lessons": [
                {
                    "id": "lesson-2.1",
                    "number": "2.1",
                    "title": "Investigate Reductions and Enlargements",
                    "canDoStatement": "I can identify and perform enlargements and reductions, find scale factors, and explain why figures are not congruent.",
                    "learningObjective": "Differentiate between reductions and enlargements using scale factors, observing that angles remain congruent while sides scale proportionally.",
                    "keyVocabulary": [
                        {
                            "term": "Enlargement",
                            "definition": "A proportional increase in size where the image is larger than the preimage, occurring when scale factor k > 1.",
                            "example": "A photo magnified with scale factor k = 3."
                        },
                        {
                            "term": "Reduction",
                            "definition": "A proportional decrease in size where the image is smaller than the preimage, occurring when 0 < scale factor k < 1.",
                            "example": "A blueprint or map with scale factor k = 1/50."
                        },
                        {
                            "term": "Scale Factor (k)",
                            "definition": "The constant ratio of any side length in the image to the corresponding side length in the preimage: k = (Image length) / (Preimage length).",
                            "example": "If image side is 12 and preimage side is 4, k = 12/4 = 3."
                        },
                        {
                            "term": "Non-Congruence",
                            "definition": "When k ≠ 1, side lengths change, so the image is not congruent to the preimage despite having equal corresponding angles.",
                            "example": "An enlargement preserves shape but alters size, making it similar but not congruent."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Scale Factor Formula",
                            "formula": "k = (Image Length) / (Preimage Length)",
                            "description": "k > 1 produces an enlargement; 0 < k < 1 produces a reduction; k = 1 produces a congruent figure."
                        }
                    ],
                    "keyTakeaways": [
                        "Enlargements expand figures (k > 1); reductions shrink figures (0 < k < 1).",
                        "Corresponding angle measures NEVER change during an enlargement or reduction.",
                        "Corresponding sides change by a common multiplier k.",
                        "Orientation remains identical in a standard dilation/resizing."
                    ],
                    "interactivePrompts": [
                        "A rectangular patio is 8 ft by 12 ft. An architect draws a reduction with width 2 ft. What is the scale factor k and the drawn length?",
                        "If a triangle's side lengths are multiplied by 0.75, what happens to the perimeter? What happens to the interior angles?"
                    ]
                },
                {
                    "id": "lesson-2.2",
                    "number": "2.2",
                    "title": "Explore Dilations",
                    "canDoStatement": "I can identify and perform dilations given a scale factor and center of dilation at the origin, identify the algebraic rule, and calculate perimeter and area effects.",
                    "learningObjective": "Dilation of figures on a coordinate plane with center at the origin, writing algebraic rules (x,y) → (kx, ky), and analyzing effects on perimeter and area.",
                    "keyVocabulary": [
                        {
                            "term": "Dilation",
                            "definition": "A non-rigid transformation that expands or contracts a figure by a scale factor k relative to a fixed point called the center of dilation.",
                            "example": "Multiplying coordinates by k=2 expands the figure away from the origin."
                        },
                        {
                            "term": "Center of Dilation",
                            "definition": "The reference point from which all points are expanded or contracted. When the center is (0, 0), each coordinate is multiplied by k.",
                            "example": "A point at (2, 4) dilated by k = 0.5 from origin moves to (1, 2)."
                        },
                        {
                            "term": "Perimeter Effect of Dilation",
                            "definition": "The perimeter of the image equals the perimeter of the preimage multiplied by the scale factor k: Perimeter' = k · Perimeter.",
                            "example": "If k = 3, the perimeter triples."
                        },
                        {
                            "term": "Area Effect of Dilation",
                            "definition": "The area of the image equals the area of the preimage multiplied by the square of the scale factor: Area' = k² · Area.",
                            "example": "If k = 3, the area becomes 3² = 9 times as large."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Dilation Mapping Rule (Center at Origin)",
                            "formula": "(x, y) → (kx, ky)",
                            "description": "Multiply both x and y by scale factor k."
                        },
                        {
                            "name": "Perimeter Scaling",
                            "formula": "P_{image} = k · P_{preimage}",
                            "description": "Linear dimensions scale directly by k."
                        },
                        {
                            "name": "Area Scaling",
                            "formula": "A_{image} = k^2 · A_{preimage}",
                            "description": "Two-dimensional surface areas scale by k squared."
                        }
                    ],
                    "keyTakeaways": [
                        "Dilation is NOT a rigid motion because side lengths are not preserved (unless k=1).",
                        "Dilations map lines to parallel lines (or lines through the center map to themselves).",
                        "Lines connecting corresponding preimage and image points all intersect at the center of dilation.",
                        "Perimeter scales by k; Area scales by k²."
                    ],
                    "interactivePrompts": [
                        "If a triangle has an area of 14 sq units and is dilated by a scale factor of 4, what is the area of the image triangle?",
                        "A polygon has vertex at (6, -9). After a dilation centered at (0,0), the image vertex is at (2, -3). What is the scale factor k?"
                    ]
                },
                {
                    "id": "lesson-2.3",
                    "number": "2.3",
                    "title": "Understand and Recognize Similar Figures",
                    "canDoStatement": "I can describe a sequence of transformations (rigid motions + dilation) that exhibits similarity between two figures and write similarity statements.",
                    "learningObjective": "Demonstrate that two figures are similar if there exists a sequence of rigid motions and dilations that maps one onto the other.",
                    "keyVocabulary": [
                        {
                            "term": "Similar Figures (~)",
                            "definition": "Two figures are similar if one can be mapped onto the other through a sequence of one or more rigid motions and a dilation.",
                            "example": "Triangle ABC ~ Triangle DEF implies corresponding angles are equal and corresponding sides are proportional."
                        },
                        {
                            "term": "Proportionality Statement",
                            "definition": "An equation showing that ratios of corresponding side lengths are all equal to the scale factor k.",
                            "example": "AB / DE = BC / EF = AC / DF = k."
                        },
                        {
                            "term": "Similarity Statement",
                            "definition": "A formal statement using the ~ symbol, written with corresponding vertices in matching sequential order.",
                            "example": "△JKL ~ △PQR indicates J corresponds to P, K to Q, and L to R."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Similarity Definition",
                            "formula": "Figure A ~ Figure B ⟺ (Dilation ∘ Rigid Motions)(A) = B",
                            "description": "All corresponding angles congruent, all corresponding sides proportional."
                        },
                        {
                            "name": "Side Proportionality",
                            "formula": "s_1'/s_1 = s_2'/s_2 = s_3'/s_3 = k",
                            "description": "Equal side ratios define geometric similarity."
                        }
                    ],
                    "keyTakeaways": [
                        "All congruent figures are similar (with k=1), but not all similar figures are congruent.",
                        "Similarity requires TWO conditions: (1) All corresponding angles are congruent, and (2) All corresponding side lengths are proportional.",
                        "A dilation combined with translations, reflections, or rotations establishes similarity.",
                        "If two triangles share two pairs of congruent angles (AA criterion), they are guaranteed to be similar."
                    ],
                    "interactivePrompts": [
                        "Triangle ABC has sides 6, 8, 10. Triangle DEF has sides 9, 12, 15. Are they similar? If so, what is the scale factor from ABC to DEF?",
                        "Can two rectangles have congruent angles but NOT be similar? Explain why using side length ratios."
                    ]
                },
                {
                    "id": "module-2-review",
                    "number": "2.R",
                    "title": "Module 2 Review & Performance Assessment",
                    "canDoStatement": "I can synthesize dilations, scale factors, and rigid motions to verify similarity and solve real-world scale model problems.",
                    "learningObjective": "Review, apply, and assess all concepts from Module 2 (Reductions, Enlargements, Dilations, Similar Figures).",
                    "keyVocabulary": [
                        {
                            "term": "Scale Factor of Similarity",
                            "definition": "The constant ratio k between any corresponding linear measurements of two similar figures.",
                            "example": "k = Perimeter(Image) / Perimeter(Preimage)."
                        },
                        {
                            "term": "Composite Similarity Sequence",
                            "definition": "A sequence containing a dilation and at least one rigid transformation mapping preimage to image.",
                            "example": "Dilation by k=0.5 followed by 90° CCW rotation."
                        }
                    ],
                    "coreFormulas": [
                        {
                            "name": "Comprehensive Similarity Checklist",
                            "formula": "∠A ≅ ∠A', ∠B ≅ ∠B', ∠C ≅ ∠C' AND A'B'/AB = B'C'/BC = A'C'/AC = k",
                            "description": "The two mathematical requirements for similarity."
                        }
                    ],
                    "keyTakeaways": [
                        "Check both angle congruence and side ratio equality when evaluating similarity.",
                        "Remember to square the scale factor when computing image area.",
                        "Always identify whether the transformation is an enlargement (k>1) or a reduction (k<1)."
                    ],
                    "interactivePrompts": [
                        "A map has a scale factor of 1:25,000. If two towns are 4 cm apart on the map, what is the actual distance in meters and kilometers?"
                    ]
                }
            ]
        }
    ],
    "formulaSheet": {
        "title": "Grade 8 Transformational Geometry Reference Sheet",
        "description": "Essential coordinate mapping rules, algebraic formulas, geometric properties, and theorems for Into Math Unit 1.",
        "categories": [
            {
                "categoryName": "Translations",
                "rules": [
                    {
                        "transformation": "Translation (Horizontal & Vertical)",
                        "rule": "(x, y) → (x + a, y + b)",
                        "effect": "Slides figure 'a' units horizontally (right if a>0, left if a<0) and 'b' units vertically (up if b>0, down if b<0).",
                        "preserves": "Side lengths, angle measures, orientation, parallelism, area, perimeter"
                    }
                ]
            },
            {
                "categoryName": "Reflections",
                "rules": [
                    {
                        "transformation": "Reflection across x-axis",
                        "rule": "(x, y) → (x, -y)",
                        "effect": "Flips figure vertically across the x-axis. y changes sign, x stays same.",
                        "preserves": "Side lengths, angle measures, parallelism. REVERSES orientation."
                    },
                    {
                        "transformation": "Reflection across y-axis",
                        "rule": "(x, y) → (-x, y)",
                        "effect": "Flips figure horizontally across the y-axis. x changes sign, y stays same.",
                        "preserves": "Side lengths, angle measures, parallelism. REVERSES orientation."
                    },
                    {
                        "transformation": "Reflection across vertical line x = k",
                        "rule": "(x, y) → (2k - x, y)",
                        "effect": "Flips horizontally across the vertical line x = k.",
                        "preserves": "Side lengths, angle measures. Distance from line x=k is invariant."
                    },
                    {
                        "transformation": "Reflection across horizontal line y = k",
                        "rule": "(x, y) → (x, 2k - y)",
                        "effect": "Flips vertically across the horizontal line y = k.",
                        "preserves": "Side lengths, angle measures. Distance from line y=k is invariant."
                    }
                ]
            },
            {
                "categoryName": "Rotations (Center at Origin 0,0)",
                "rules": [
                    {
                        "transformation": "90° Clockwise / 270° Counterclockwise",
                        "rule": "(x, y) → (y, -x)",
                        "effect": "Quarter turn clockwise. Swap coordinates and negate the new y.",
                        "preserves": "Side lengths, angle measures, orientation, parallelism."
                    },
                    {
                        "transformation": "180° Rotation (CW or CCW)",
                        "rule": "(x, y) → (-x, -y)",
                        "effect": "Half turn. Negate both coordinates. Direction does not matter.",
                        "preserves": "Side lengths, angle measures, orientation, parallelism."
                    },
                    {
                        "transformation": "270° Clockwise / 90° Counterclockwise",
                        "rule": "(x, y) → (-y, x)",
                        "effect": "Quarter turn counterclockwise. Swap coordinates and negate the new x.",
                        "preserves": "Side lengths, angle measures, orientation, parallelism."
                    },
                    {
                        "transformation": "360° Full Rotation",
                        "rule": "(x, y) → (x, y)",
                        "effect": "Full turn back to original starting position (identity transformation).",
                        "preserves": "All properties identical."
                    }
                ]
            },
            {
                "categoryName": "Dilations & Scaling (Center at Origin 0,0)",
                "rules": [
                    {
                        "transformation": "Dilation with scale factor k",
                        "rule": "(x, y) → (kx, ky)",
                        "effect": "Multiplies distance from origin by k. Enlargement if k > 1; Reduction if 0 < k < 1.",
                        "preserves": "Angle measures, shape, parallelism. Side lengths change by factor k."
                    },
                    {
                        "transformation": "Perimeter Scaling",
                        "rule": "P_{image} = k · P_{preimage}",
                        "effect": "The perimeter of the image scales linearly with scale factor k.",
                        "preserves": "Constant ratio of perimeters."
                    },
                    {
                        "transformation": "Area Scaling",
                        "rule": "A_{image} = k^2 · A_{preimage}",
                        "effect": "The area of the image scales with the square of the scale factor k².",
                        "preserves": "Proportional area relationship."
                    }
                ]
            },
            {
                "categoryName": "Theorems & Definitions",
                "rules": [
                    {
                        "transformation": "Congruence (≅)",
                        "rule": "△ABC ≅ △DEF ⟺ Sequence of Rigid Motions maps △ABC to △DEF",
                        "effect": "All corresponding sides are congruent (AB=DE, BC=EF, AC=DF) and all corresponding angles are congruent (∠A=∠D, ∠B=∠E, ∠C=∠F).",
                        "preserves": "Complete metric and geometric equivalence."
                    },
                    {
                        "transformation": "Similarity (~)",
                        "rule": "△ABC ~ △DEF ⟺ Sequence of Rigid Motions + Dilation maps △ABC to △DEF",
                        "effect": "All corresponding angles are congruent; corresponding sides are in constant proportion: AB/DE = BC/EF = AC/DF = k.",
                        "preserves": "Shape, angle measures, and side ratios."
                    }
                ]
            }
        ]
    },
    "quizBank": [
        # Lesson 1.1 Questions
        {
            "id": "q1_1_01",
            "module": 1,
            "lessonId": "lesson-1.1",
            "title": "Rigid Motion Angle Preservation",
            "type": "multiple-choice",
            "question": "Triangle ABC is translated 5 units left and 3 units down to form Triangle A'B'C'. If m∠A = 54° and m∠B = 68°, what is m∠A'?",
            "prompt": "Recall the fundamental properties of rigid motions regarding angle measures.",
            "visualConfig": {
                "type": "translation",
                "preimage": [{"x": 2, "y": 2, "label": "A"}, {"x": 5, "y": 2, "label": "B"}, {"x": 3, "y": 6, "label": "C"}],
                "image": [{"x": -3, "y": -1, "label": "A'"}, {"x": 0, "y": -1, "label": "B'"}, {"x": -2, "y": 3, "label": "C'"}],
                "transformationVector": {"dx": -5, "dy": -3}
            },
            "options": [
                "27° because sliding cuts the angle in half",
                "54° because translations preserve angle measures",
                "58° because the third angle changes the others",
                "108° because moving left doubles horizontal angles"
            ],
            "correctAnswer": "54° because translations preserve angle measures",
            "explanation": "A translation is a rigid motion (isometry). Rigid motions strictly preserve both side lengths and angle measures. Therefore, corresponding angles are congruent: m∠A' = m∠A = 54°.",
            "hint": "Does sliding a triangle across a paper change how sharp or wide its corners are?",
            "points": 10
        },
        {
            "id": "q1_1_02",
            "module": 1,
            "lessonId": "lesson-1.1",
            "title": "Orientation Changes in Transformations",
            "type": "multiple-choice",
            "question": "Which of the following transformations REVERSES the orientation of a geometric figure?",
            "prompt": "Think about reading vertices in clockwise order before and after the transformation.",
            "visualConfig": {
                "type": "reflection",
                "preimage": [{"x": 1, "y": 1, "label": "A"}, {"x": 4, "y": 1, "label": "B"}, {"x": 2, "y": 4, "label": "C"}],
                "image": [{"x": -1, "y": 1, "label": "A'"}, {"x": -4, "y": 1, "label": "B'"}, {"x": -2, "y": 4, "label": "C'"}],
                "lineOfReflection": "y-axis (x = 0)"
            },
            "options": [
                "Translation 4 units up",
                "Rotation 90° clockwise about the origin",
                "Reflection across the y-axis",
                "Rotation 180° counterclockwise about the origin"
            ],
            "correctAnswer": "Reflection across the y-axis",
            "explanation": "Reflections flip the figure across a line, which reverses the clockwise/counterclockwise order of the vertices. Translations and rotations keep the orientation preserved.",
            "hint": "When you look into a mirror, your right hand appears as a left hand. Which transformation behaves like a mirror?",
            "points": 10
        },
        {
            "id": "q1_1_03",
            "module": 1,
            "lessonId": "lesson-1.1",
            "title": "Parallelism Under Rigid Motions",
            "type": "true-false",
            "question": "True or False: If line segment AB is parallel to line segment CD, then after any rigid motion (translation, reflection, or rotation), segment A'B' will remain parallel to segment C'D'.",
            "prompt": "Determine whether parallelism is an invariant property of rigid transformations.",
            "visualConfig": {
                "type": "rotation",
                "preimage": [
                    {"x": 1, "y": 1, "label": "A"}, {"x": 4, "y": 1, "label": "B"},
                    {"x": 1, "y": 3, "label": "C"}, {"x": 4, "y": 3, "label": "D"}
                ],
                "image": [
                    {"x": -1, "y": 1, "label": "A'"}, {"x": -1, "y": 4, "label": "B'"},
                    {"x": -3, "y": 1, "label": "C'"}, {"x": -3, "y": 4, "label": "D'"}
                ],
                "rotationAngle": "90 deg CCW"
            },
            "options": ["True", "False"],
            "correctAnswer": "True",
            "explanation": "Rigid motions preserve line parallelism. If two lines or segments are parallel in the preimage (AB || CD), their images are guaranteed to be parallel (A'B' || C'D').",
            "hint": "Rigid motions preserve the relative geometric relationships between all parts of a figure.",
            "points": 10
        },

        # Lesson 1.2 Questions
        {
            "id": "q1_2_01",
            "module": 1,
            "lessonId": "lesson-1.2",
            "title": "Finding Image Coordinates from Mapping Rule",
            "type": "coordinate-input",
            "question": "Point P has coordinates (-3, 5). Find the coordinates of image point P' after applying the translation rule: (x, y) → (x + 6, y - 4).",
            "prompt": "Enter the coordinates in the standard format (x, y).",
            "visualConfig": {
                "type": "translation",
                "preimage": [{"x": -3, "y": 5, "label": "P"}],
                "image": [{"x": 3, "y": 1, "label": "P'"}],
                "transformationVector": {"dx": 6, "dy": -4}
            },
            "options": ["(3, 1)", "(-9, 9)", "(3, 9)", "(-9, 1)"],
            "correctAnswer": "(3, 1)",
            "explanation": "Apply the rule to each coordinate:\nx' = x + 6 = -3 + 6 = 3\ny' = y - 4 = 5 - 4 = 1\nThus, P' = (3, 1).",
            "hint": "Add 6 to the x-coordinate (-3) and subtract 4 from the y-coordinate (5).",
            "points": 10
        },
        {
            "id": "q1_2_02",
            "module": 1,
            "lessonId": "lesson-1.2",
            "title": "Determining the Algebraic Translation Rule",
            "type": "multiple-choice",
            "question": "Triangle JKL has vertex J(2, -1). After a translation, the image vertex is J'(-3, 4). Which algebraic mapping rule describes this translation?",
            "prompt": "Calculate the change in x (Δx = x' - x) and the change in y (Δy = y' - y).",
            "visualConfig": {
                "type": "translation",
                "preimage": [{"x": 2, "y": -1, "label": "J"}, {"x": 5, "y": -1, "label": "K"}, {"x": 3, "y": 2, "label": "L"}],
                "image": [{"x": -3, "y": 4, "label": "J'"}, {"x": 0, "y": 4, "label": "K'"}, {"x": -2, "y": 7, "label": "L'"}],
                "transformationVector": {"dx": -5, "dy": 5}
            },
            "options": [
                "(x, y) → (x + 5, y - 5)",
                "(x, y) → (x - 5, y + 5)",
                "(x, y) → (x - 1, y + 3)",
                "(x, y) → (-x, -y)"
            ],
            "correctAnswer": "(x, y) → (x - 5, y + 5)",
            "explanation": "Compute the shifts:\nHorizontal shift a = x' - x = -3 - 2 = -5 (5 units left)\nVertical shift b = y' - y = 4 - (-1) = 5 (5 units up)\nTherefore, the rule is (x, y) → (x - 5, y + 5).",
            "hint": "From x = 2 to x = -3, did you move left (-) or right (+)? From y = -1 to y = 4, did you move up (+) or down (-)?",
            "points": 10
        },
        {
            "id": "q1_2_03",
            "module": 1,
            "lessonId": "lesson-1.2",
            "title": "Translation Vector Length and Direction",
            "type": "multiple-choice",
            "question": "In a translation, the line segments connecting each preimage point to its corresponding image point (e.g., segment AA', BB', CC') are always:",
            "prompt": "Think about how every vertex travels during a slide.",
            "visualConfig": {
                "type": "translation",
                "preimage": [{"x": -2, "y": 1, "label": "A"}, {"x": 1, "y": 1, "label": "B"}, {"x": -1, "y": 4, "label": "C"}],
                "image": [{"x": 2, "y": -2, "label": "A'"}, {"x": 5, "y": -2, "label": "B'"}, {"x": 3, "y": 1, "label": "C'"}],
                "transformationVector": {"dx": 4, "dy": -3}
            },
            "options": [
                "Perpendicular to each other and of varying lengths",
                "Parallel to each other and equal in length",
                "Intersecting at the origin (0, 0)",
                "Intersecting at the center of the figure"
            ],
            "correctAnswer": "Parallel to each other and equal in length",
            "explanation": "Every point in the preimage travels along the same straight line trajectory by the exact same distance. Therefore, all segments connecting corresponding points (AA', BB', CC') are parallel and equal in length.",
            "hint": "If every person in a marching band takes 4 steps forward and 3 steps right, do their paths cross or run parallel?",
            "points": 10
        },

        # Lesson 1.3 Questions
        {
            "id": "q1_3_01",
            "module": 1,
            "lessonId": "lesson-1.3",
            "title": "Reflection Across the X-Axis",
            "type": "coordinate-input",
            "question": "Point M is located at (4, -7). What are the coordinates of M' after reflecting across the x-axis?",
            "prompt": "Apply the algebraic reflection rule for the x-axis: (x, y) → (x, -y).",
            "visualConfig": {
                "type": "reflection",
                "preimage": [{"x": 4, "y": -7, "label": "M"}],
                "image": [{"x": 4, "y": 7, "label": "M'"}],
                "lineOfReflection": "x-axis (y = 0)"
            },
            "options": ["(4, 7)", "(-4, -7)", "(-4, 7)", "(-7, 4)"],
            "correctAnswer": "(4, 7)",
            "explanation": "When reflecting across the x-axis, the x-coordinate remains unchanged, while the y-coordinate is negated: (x, y) → (x, -y).\nSo (4, -7) becomes (4, -(-7)) = (4, 7).",
            "hint": "Flipping over the horizontal x-axis changes the vertical position from below the axis to above it.",
            "points": 10
        },
        {
            "id": "q1_3_02",
            "module": 1,
            "lessonId": "lesson-1.3",
            "title": "Reflection Across the Y-Axis",
            "type": "coordinate-input",
            "question": "Vertex K of a parallelogram is at (-6, 2). What are the coordinates of K' after a reflection across the y-axis?",
            "prompt": "Apply the algebraic reflection rule for the y-axis: (x, y) → (-x, y).",
            "visualConfig": {
                "type": "reflection",
                "preimage": [{"x": -6, "y": 2, "label": "K"}],
                "image": [{"x": 6, "y": 2, "label": "K'"}],
                "lineOfReflection": "y-axis (x = 0)"
            },
            "options": ["(6, 2)", "(-6, -2)", "(6, -2)", "(2, -6)"],
            "correctAnswer": "(6, 2)",
            "explanation": "Reflecting across the y-axis negates the x-coordinate while leaving the y-coordinate unchanged: (x, y) → (-x, y).\nThus, (-6, 2) → (-(-6), 2) = (6, 2).",
            "hint": "Flipping across the vertical y-axis moves a point from Quadrant II to Quadrant I.",
            "points": 10
        },
        {
            "id": "q1_3_03",
            "module": 1,
            "lessonId": "lesson-1.3",
            "title": "Reflection Across a Line x = k",
            "type": "multiple-choice",
            "question": "Point Q is at (1, 4). If point Q is reflected across the vertical line x = 3, what are the coordinates of Q'?",
            "prompt": "Measure the distance from (1, 4) to the line x = 3, then count that same distance on the other side.",
            "visualConfig": {
                "type": "reflection",
                "preimage": [{"x": 1, "y": 4, "label": "Q"}],
                "image": [{"x": 5, "y": 4, "label": "Q'"}],
                "lineOfReflection": "vertical line x = 3"
            },
            "options": [
                "(5, 4)",
                "(3, 4)",
                "(1, 2)",
                "(-1, 4)"
            ],
            "correctAnswer": "(5, 4)",
            "explanation": "The distance from Q(1, 4) to the line x = 3 is 3 - 1 = 2 units to the left. The image Q' must be 2 units to the right of x = 3, at x = 3 + 2 = 5. The y-coordinate does not change, so Q' = (5, 4). Algebraically: (2k - x, y) = (2(3) - 1, 4) = (5, 4).",
            "hint": "How far is x = 1 from x = 3? Go that same distance past 3.",
            "points": 10
        },

        # Lesson 1.4 Questions
        {
            "id": "q1_4_01",
            "module": 1,
            "lessonId": "lesson-1.4",
            "title": "90° Clockwise Rotation About the Origin",
            "type": "coordinate-input",
            "question": "Point A is at (2, 5). What are its coordinates after a 90° clockwise rotation about the origin (0, 0)?",
            "prompt": "Recall the rule for 90° CW rotation: (x, y) → (y, -x).",
            "visualConfig": {
                "type": "rotation",
                "preimage": [{"x": 2, "y": 5, "label": "A"}],
                "image": [{"x": 5, "y": -2, "label": "A'"}],
                "rotationCenter": {"x": 0, "y": 0},
                "rotationAngle": "90 deg CW"
            },
            "options": ["(5, -2)", "(-5, 2)", "(-2, -5)", "(-2, 5)"],
            "correctAnswer": "(5, -2)",
            "explanation": "The coordinate rule for a 90° clockwise rotation about (0,0) is (x, y) → (y, -x).\nGiven A(2, 5):\nx' = y = 5\ny' = -x = -2\nSo A' = (5, -2).",
            "hint": "Swap the two numbers, and make the new second number negative.",
            "points": 10
        },
        {
            "id": "q1_4_02",
            "module": 1,
            "lessonId": "lesson-1.4",
            "title": "180° Rotation About the Origin",
            "type": "coordinate-input",
            "question": "Point B(-4, 3) is rotated 180° about the origin. What are the coordinates of B'?",
            "prompt": "Apply the rule for a 180° rotation: (x, y) → (-x, -y).",
            "visualConfig": {
                "type": "rotation",
                "preimage": [{"x": -4, "y": 3, "label": "B"}],
                "image": [{"x": 4, "y": -3, "label": "B'"}],
                "rotationCenter": {"x": 0, "y": 0},
                "rotationAngle": "180 deg"
            },
            "options": ["(4, -3)", "(-3, 4)", "(3, -4)", "(4, 3)"],
            "correctAnswer": "(4, -3)",
            "explanation": "A 180° rotation (clockwise or counterclockwise) negates both coordinates: (x, y) → (-x, -y).\nGiven B(-4, 3):\nB' = (-(-4), -(3)) = (4, -3).",
            "hint": "Change the sign of both coordinates: negative becomes positive, positive becomes negative.",
            "points": 10
        },
        {
            "id": "q1_4_03",
            "module": 1,
            "lessonId": "lesson-1.4",
            "title": "Equivalence of Rotations",
            "type": "multiple-choice",
            "question": "Which of the following rotations produces the EXACT same image as a 270° clockwise rotation about the origin?",
            "prompt": "Consider full circles of 360° and opposite directions.",
            "visualConfig": {
                "type": "rotation",
                "preimage": [{"x": 3, "y": 1, "label": "P"}],
                "image": [{"x": -1, "y": 3, "label": "P'"}],
                "rotationCenter": {"x": 0, "y": 0},
                "rotationAngle": "270 deg CW / 90 deg CCW"
            },
            "options": [
                "90° counterclockwise rotation",
                "90° clockwise rotation",
                "180° rotation",
                "360° counterclockwise rotation"
            ],
            "correctAnswer": "90° counterclockwise rotation",
            "explanation": "Since a full circular revolution is 360°, rotating 270° in the clockwise direction leaves 360° - 270° = 90° in the counterclockwise direction. Both share the mapping rule (x, y) → (-y, x).",
            "hint": "360 minus 270 equals 90.",
            "points": 10
        },

        # Lesson 1.5 Questions
        {
            "id": "q1_5_01",
            "module": 1,
            "lessonId": "lesson-1.5",
            "title": "Congruence Through Transformation Sequences",
            "type": "sequence",
            "question": "Triangle ABC with vertices A(1, 1), B(4, 1), C(1, 3) is transformed to Triangle DEF with vertices D(-1, -1), E(-4, -1), F(-1, -3). Which single transformation or sequence proves that △ABC ≅ △DEF?",
            "prompt": "Compare coordinates of corresponding vertices: (1, 1) to (-1, -1), (4, 1) to (-4, -1), (1, 3) to (-1, -3).",
            "visualConfig": {
                "type": "congruence_sequence",
                "preimage": [{"x": 1, "y": 1, "label": "A"}, {"x": 4, "y": 1, "label": "B"}, {"x": 1, "y": 3, "label": "C"}],
                "image": [{"x": -1, "y": -1, "label": "D"}, {"x": -4, "y": -1, "label": "E"}, {"x": -1, "y": -3, "label": "F"}],
                "sequence": ["180° rotation about the origin (0, 0)"]
            },
            "options": [
                "A 180° rotation about the origin (0, 0)",
                "A reflection across the line y = -x",
                "A translation of 2 units left and 2 units down",
                "A 90° counterclockwise rotation about the origin"
            ],
            "correctAnswer": "A 180° rotation about the origin (0, 0)",
            "explanation": "Notice that every coordinate (x, y) maps directly to (-x, -y):\nA(1, 1) → D(-1, -1)\nB(4, 1) → E(-4, -1)\nC(1, 3) → F(-1, -3)\nThis matches the algebraic rule for a 180° rotation about the origin, proving △ABC ≅ △DEF.",
            "hint": "Both the x-coordinate and the y-coordinate have their signs flipped.",
            "points": 10
        },
        {
            "id": "q1_5_02",
            "module": 1,
            "lessonId": "lesson-1.5",
            "title": "Matching Corresponding Parts in Congruence Statements",
            "type": "multiple-choice",
            "question": "Given that Quadrilateral ABCD ≅ Quadrilateral WXYZ, which of the following statements MUST be true?",
            "prompt": "Letter order in congruence statements indicates exact vertex correspondence.",
            "visualConfig": {
                "type": "congruence_statement",
                "preimage": [{"x": 1, "y": 1, "label": "A"}, {"x": 5, "y": 1, "label": "B"}, {"x": 4, "y": 4, "label": "C"}, {"x": 1, "y": 4, "label": "D"}],
                "image": [{"x": -1, "y": 1, "label": "W"}, {"x": -5, "y": 1, "label": "X"}, {"x": -4, "y": 4, "label": "Y"}, {"x": -1, "y": 4, "label": "Z"}]
            },
            "options": [
                "Side BC ≅ Side WX and ∠A ≅ ∠Z",
                "Side CD ≅ Side YZ and ∠B ≅ ∠X",
                "Side AB ≅ Side YZ and ∠C ≅ ∠W",
                "Side AD ≅ Side XY and ∠D ≅ ∠X"
            ],
            "correctAnswer": "Side CD ≅ Side YZ and ∠B ≅ ∠X",
            "explanation": "In congruence statements, corresponding positions match:\nA ↔ W, B ↔ X, C ↔ Y, D ↔ Z.\nTherefore, side CD corresponds to side YZ (positions 3 & 4), and angle B corresponds to angle X (position 2).",
            "hint": "Write down the two names: A-B-C-D and W-X-Y-Z and align their positions 1, 2, 3, 4.",
            "points": 10
        },
        {
            "id": "q1_5_03",
            "module": 1,
            "lessonId": "lesson-1.5",
            "title": "Multi-Step Congruence Sequence Identification",
            "type": "sequence",
            "question": "Triangle T is reflected across the x-axis and then translated 4 units right to land directly on Triangle T''. Which statement correctly describes the relationship between T and T''?",
            "prompt": "Analyze the effect of a composite series of rigid motions.",
            "visualConfig": {
                "type": "composite_rigid",
                "preimage": [{"x": -3, "y": 2, "label": "P1"}, {"x": -1, "y": 2, "label": "P2"}, {"x": -2, "y": 5, "label": "P3"}],
                "image": [{"x": 1, "y": -2, "label": "P1''"}, {"x": 3, "y": -2, "label": "P2''"}, {"x": 2, "y": -5, "label": "P3''"}],
                "sequence": ["Reflect across x-axis: (x, -y)", "Translate right 4: (x + 4, y)"]
            },
            "options": [
                "Triangle T is congruent to Triangle T'' because both transformations are rigid motions.",
                "Triangle T is similar but NOT congruent to Triangle T'' because reflection changes size.",
                "Triangle T is not congruent because translations change angles.",
                "Triangle T is congruent only if the order is reversed."
            ],
            "correctAnswer": "Triangle T is congruent to Triangle T'' because both transformations are rigid motions.",
            "explanation": "Both reflection and translation are rigid motions (isometries). A composition of any number of rigid motions preserves side lengths and angle measures, ensuring the final image is always congruent to the original preimage.",
            "hint": "Do reflections or translations change the length of any side?",
            "points": 10
        },

        # Module 1 Review Test Questions
        {
            "id": "q1_r_01",
            "module": 1,
            "lessonId": "module-1-review",
            "title": "Composite Transformation Final Coordinate",
            "type": "coordinate-input",
            "question": "Point Z(3, 4) is rotated 90° counterclockwise about the origin, and then the resulting image is translated by (x, y) → (x - 2, y + 5). What are the final coordinates of Z''?",
            "prompt": "Step 1: Perform 90° CCW rotation: (x, y) → (-y, x). Step 2: Apply translation rule to the intermediate point.",
            "visualConfig": {
                "type": "composite_transformation",
                "preimage": [{"x": 3, "y": 4, "label": "Z"}],
                "intermediate": [{"x": -4, "y": 3, "label": "Z'"}],
                "image": [{"x": -6, "y": 8, "label": "Z''"}]
            },
            "options": ["(-6, 8)", "(2, 1)", "(-2, 9)", "(1, 8)"],
            "correctAnswer": "(-6, 8)",
            "explanation": "Step 1 (90° CCW rotation): (x, y) → (-y, x), so Z(3, 4) becomes Z'(-4, 3).\nStep 2 (Translation): (x - 2, y + 5), so x'' = -4 - 2 = -6, and y'' = 3 + 5 = 8.\nFinal coordinates: Z'' = (-6, 8).",
            "hint": "Don't do both at once. Find Z' first, then apply the translation to Z'.",
            "points": 15
        },
        {
            "id": "q1_r_02",
            "module": 1,
            "lessonId": "module-1-review",
            "title": "Identifying Transformations from Given Figures",
            "type": "multiple-choice",
            "question": "Figure 1 has vertices at (1, 2), (3, 2), and (3, 5). Figure 2 has vertices at (-2, 1), (-2, 3), and (-5, 3). Which transformation maps Figure 1 onto Figure 2?",
            "prompt": "Test mapping rules: observe what happens to (x, y) values.",
            "visualConfig": {
                "type": "rotation",
                "preimage": [{"x": 1, "y": 2, "label": "A"}, {"x": 3, "y": 2, "label": "B"}, {"x": 3, "y": 5, "label": "C"}],
                "image": [{"x": -2, "y": 1, "label": "A'"}, {"x": -2, "y": 3, "label": "B'"}, {"x": -5, "y": 3, "label": "C'"}]
            },
            "options": [
                "Rotation 90° counterclockwise about the origin: (x, y) → (-y, x)",
                "Rotation 90° clockwise about the origin: (x, y) → (y, -x)",
                "Reflection across the line y = x",
                "Translation 3 units left and 1 unit down"
            ],
            "correctAnswer": "Rotation 90° counterclockwise about the origin: (x, y) → (-y, x)",
            "explanation": "Check the points:\n(1, 2) → (-2, 1)\n(3, 2) → (-2, 3)\n(3, 5) → (-5, 3)\nIn each case, (x, y) maps to (-y, x), which is the precise rule for a 90° counterclockwise rotation about (0,0).",
            "hint": "Notice that the original y-value became the opposite of the new x-value.",
            "points": 15
        },

        # Lesson 2.1 Questions
        {
            "id": "q2_1_01",
            "module": 2,
            "lessonId": "lesson-2.1",
            "title": "Identifying Scale Factor of Enlargement",
            "type": "multiple-choice",
            "question": "A photo with width 4 inches and length 6 inches is enlarged to a poster with width 16 inches and length 24 inches. What is the scale factor k of this enlargement?",
            "prompt": "Scale factor k = (Image dimension) / (Preimage dimension).",
            "visualConfig": {
                "type": "enlargement",
                "preimage": [{"x": 0, "y": 0}, {"x": 4, "y": 0}, {"x": 4, "y": 6}, {"x": 0, "y": 6}],
                "image": [{"x": 0, "y": 0}, {"x": 16, "y": 0}, {"x": 16, "y": 24}, {"x": 0, "y": 24}],
                "scaleFactor": 4
            },
            "options": ["k = 4", "k = 1/4", "k = 12", "k = 20"],
            "correctAnswer": "k = 4",
            "explanation": "Compute the ratio of corresponding side lengths:\nk = (New Width) / (Original Width) = 16 / 4 = 4.\nCheck length: 24 / 6 = 4. Since k > 1, this is an enlargement with scale factor 4.",
            "hint": "Divide the poster's width by the original photo's width.",
            "points": 10
        },
        {
            "id": "q2_1_02",
            "module": 2,
            "lessonId": "lesson-2.1",
            "title": "Reduction Scale Factor Range",
            "type": "multiple-choice",
            "question": "An architect makes a scale drawing of a 40-foot building. If the drawing is a reduction of the building, which of the following could be the scale factor k?",
            "prompt": "Recall the defining condition for a transformation to be a reduction.",
            "visualConfig": {
                "type": "reduction",
                "preimage": [{"x": 0, "y": 0}, {"x": 40, "y": 0}, {"x": 40, "y": 30}, {"x": 0, "y": 30}],
                "image": [{"x": 0, "y": 0}, {"x": 2, "y": 0}, {"x": 2, "y": 1.5}, {"x": 0, "y": 1.5}],
                "scaleFactor": 0.05
            },
            "options": [
                "k = 1/20 (or 0.05)",
                "k = 1.0",
                "k = 2.5",
                "k = -4"
            ],
            "correctAnswer": "k = 1/20 (or 0.05)",
            "explanation": "For any reduction, the image is strictly smaller than the preimage, meaning 0 < k < 1. The value k = 1/20 = 0.05 satisfies this condition.",
            "hint": "Reductions shrink a figure, so the scale factor must be between 0 and 1.",
            "points": 10
        },
        {
            "id": "q2_1_03",
            "module": 2,
            "lessonId": "lesson-2.1",
            "title": "Angle Measures in Scaled Drawings",
            "type": "multiple-choice",
            "question": "Triangle ABC has angles measuring 35°, 65°, and 80°. If Triangle ABC is enlarged by a scale factor of k = 3 to form Triangle A'B'C', what are the angle measures of Triangle A'B'C'?",
            "prompt": "Do scale factors alter interior angles of polygons?",
            "visualConfig": {
                "type": "enlargement",
                "preimage": [{"x": 0, "y": 0, "label": "A"}, {"x": 4, "y": 0, "label": "B"}, {"x": 1, "y": 3, "label": "C"}],
                "image": [{"x": 0, "y": 0, "label": "A'"}, {"x": 12, "y": 0, "label": "B'"}, {"x": 3, "y": 9, "label": "C'"}],
                "scaleFactor": 3
            },
            "options": [
                "105°, 195°, and 240° (each angle multiplied by 3)",
                "35°, 65°, and 80° (angles remain congruent)",
                "11.67°, 21.67°, and 26.67° (each angle divided by 3)",
                "60°, 60°, and 60° (it turns into an equilateral triangle)"
            ],
            "correctAnswer": "35°, 65°, and 80° (angles remain congruent)",
            "explanation": "In enlargements and reductions, only side lengths are multiplied by the scale factor. The angle measures NEVER change; corresponding angles remain exactly congruent.",
            "hint": "The sum of angles in any triangle must always be 180°. If you multiplied angles by 3, the sum would be 540°, which is impossible!",
            "points": 10
        },

        # Lesson 2.2 Questions
        {
            "id": "q2_2_01",
            "module": 2,
            "lessonId": "lesson-2.2",
            "title": "Dilation of Coordinates with Center at Origin",
            "type": "coordinate-input",
            "question": "Point D has coordinates (-4, 6). What are the coordinates of D' after a dilation centered at the origin (0, 0) with a scale factor of k = 0.5?",
            "prompt": "Use the dilation algebraic rule: (x, y) → (kx, ky).",
            "visualConfig": {
                "type": "dilation",
                "center": {"x": 0, "y": 0},
                "scaleFactor": 0.5,
                "preimage": [{"x": -4, "y": 6, "label": "D"}],
                "image": [{"x": -2, "y": 3, "label": "D'"}]
            },
            "options": ["(-2, 3)", "(-8, 12)", "(-3.5, 5.5)", "(-2, 6)"],
            "correctAnswer": "(-2, 3)",
            "explanation": "Multiply each coordinate by k = 0.5:\nx' = 0.5 · (-4) = -2\ny' = 0.5 · (6) = 3\nThus, D' = (-2, 3).",
            "hint": "Take half of -4 and half of 6.",
            "points": 10
        },
        {
            "id": "q2_2_02",
            "module": 2,
            "lessonId": "lesson-2.2",
            "title": "Effect of Dilation on Perimeter",
            "type": "multiple-choice",
            "question": "A rectangle has a perimeter of 28 cm. If it undergoes a dilation centered at the origin with a scale factor of k = 3, what is the perimeter of the dilated image?",
            "prompt": "How does scale factor k affect 1-dimensional measurements like perimeter?",
            "visualConfig": {
                "type": "dilation",
                "center": {"x": 0, "y": 0},
                "scaleFactor": 3,
                "preimagePerimeter": 28,
                "imagePerimeter": 84
            },
            "options": [
                "84 cm",
                "252 cm",
                "31 cm",
                "56 cm"
            ],
            "correctAnswer": "84 cm",
            "explanation": "Perimeter is a one-dimensional linear measure. The perimeter of the image equals the perimeter of the preimage multiplied by k:\nPerimeter' = k · Perimeter = 3 · 28 = 84 cm.",
            "hint": "Perimeter scales directly by k.",
            "points": 10
        },
        {
            "id": "q2_2_03",
            "module": 2,
            "lessonId": "lesson-2.2",
            "title": "Effect of Dilation on Area",
            "type": "multiple-choice",
            "question": "A right triangle has an area of 12 square inches. After a dilation with scale factor k = 4, what is the area of the image triangle?",
            "prompt": "Recall that area is a 2-dimensional measurement that scales by k².",
            "visualConfig": {
                "type": "dilation",
                "center": {"x": 0, "y": 0},
                "scaleFactor": 4,
                "preimageArea": 12,
                "imageArea": 192
            },
            "options": [
                "192 square inches",
                "48 square inches",
                "144 square inches",
                "96 square inches"
            ],
            "correctAnswer": "192 square inches",
            "explanation": "Area is a two-dimensional measure. When side lengths scale by k, area scales by k²:\nArea' = k² · Area = (4²) · 12 = 16 · 12 = 192 square inches.",
            "hint": "Multiply the original area by 4 squared (which is 16), not just 4.",
            "points": 10
        },
        {
            "id": "q2_2_04",
            "module": 2,
            "lessonId": "lesson-2.2",
            "title": "Finding Scale Factor from Preimage and Image Points",
            "type": "multiple-choice",
            "question": "Preimage point G(6, -9) is dilated with center at (0, 0) to produce image point G'(2, -3). What is the scale factor of this dilation?",
            "prompt": "Divide the image coordinate by the preimage coordinate: k = x' / x.",
            "visualConfig": {
                "type": "dilation",
                "center": {"x": 0, "y": 0},
                "preimage": [{"x": 6, "y": -9, "label": "G"}],
                "image": [{"x": 2, "y": -3, "label": "G'"}]
            },
            "options": [
                "k = 1/3",
                "k = 3",
                "k = -1/3",
                "k = 2/3"
            ],
            "correctAnswer": "k = 1/3",
            "explanation": "k = x' / x = 2 / 6 = 1/3. Also checking y: k = y' / y = -3 / (-9) = 1/3. Since 0 < k < 1, this is a reduction with scale factor 1/3.",
            "hint": "What do you multiply 6 by to get 2?",
            "points": 10
        },

        # Lesson 2.3 Questions
        {
            "id": "q2_3_01",
            "module": 2,
            "lessonId": "lesson-2.3",
            "title": "Conditions for Geometric Similarity",
            "type": "multiple-choice",
            "question": "Two geometric figures are mathematically SIMILAR if and only if:",
            "prompt": "Identify the two necessary conditions regarding angles and side lengths.",
            "visualConfig": {
                "type": "similarity",
                "preimage": [{"x": 1, "y": 1}, {"x": 4, "y": 1}, {"x": 1, "y": 5}],
                "image": [{"x": -2, "y": 2}, {"x": -8, "y": 2}, {"x": -2, "y": 10}]
            },
            "options": [
                "All corresponding angles are congruent and all corresponding sides are proportional",
                "All corresponding side lengths are equal and all corresponding angles are equal",
                "They have the exact same perimeter and area",
                "One figure can be mapped to the other using ONLY translations"
            ],
            "correctAnswer": "All corresponding angles are congruent and all corresponding sides are proportional",
            "explanation": "By definition, two figures are similar (~) if their corresponding angles are congruent and their corresponding side lengths are proportional. This is achieved via a sequence of rigid motions and a dilation.",
            "hint": "Similar figures have the exact same shape (equal angles) but can have different sizes (proportional sides).",
            "points": 10
        },
        {
            "id": "q2_3_02",
            "module": 2,
            "lessonId": "lesson-2.3",
            "title": "Verifying Triangle Similarity by Side Ratios",
            "type": "multiple-choice",
            "question": "Triangle ABC has side lengths 6, 8, and 10. Triangle DEF has corresponding side lengths 9, 12, and 15. Are these two triangles similar?",
            "prompt": "Calculate the ratio of each pair of corresponding sides: 9/6, 12/8, 15/10.",
            "visualConfig": {
                "type": "similarity_check",
                "triangle1": {"sides": [6, 8, 10], "label": "△ABC"},
                "triangle2": {"sides": [9, 12, 15], "label": "△DEF"}
            },
            "options": [
                "Yes, because all corresponding side ratios equal 1.5 (k = 1.5)",
                "No, because the sides do not have the same lengths",
                "No, because 15 - 10 ≠ 12 - 8",
                "Yes, but only if they are in the same quadrant"
            ],
            "correctAnswer": "Yes, because all corresponding side ratios equal 1.5 (k = 1.5)",
            "explanation": "Compute the ratios of corresponding sides:\n9 / 6 = 1.5\n12 / 8 = 1.5\n15 / 10 = 1.5\nSince all three ratios are equal, the sides are in constant proportion with scale factor k = 1.5, confirming △ABC ~ △DEF.",
            "hint": "Check whether 9/6, 12/8, and 15/10 all simplify to the same decimal or fraction.",
            "points": 10
        },
        {
            "id": "q2_3_03",
            "module": 2,
            "lessonId": "lesson-2.3",
            "title": "Describing Similarity Transformations",
            "type": "sequence",
            "question": "Figure A is dilated by a scale factor of 2 centered at the origin, and then rotated 90° clockwise about the origin to produce Figure B. Which statement is completely accurate?",
            "prompt": "Evaluate the relationship between Figure A and Figure B.",
            "visualConfig": {
                "type": "similarity_sequence",
                "preimage": [{"x": 1, "y": 2, "label": "P1"}, {"x": 3, "y": 2, "label": "P2"}, {"x": 1, "y": 4, "label": "P3"}],
                "image": [{"x": 4, "y": -2, "label": "P1''"}, {"x": 4, "y": -6, "label": "P2''"}, {"x": 8, "y": -2, "label": "P3''"}],
                "sequence": ["Dilation by k=2: (x, y) → (2x, 2y)", "90° CW rotation: (x, y) → (y, -x)"]
            },
            "options": [
                "Figure A is similar to Figure B (Figure A ~ Figure B), but they are NOT congruent.",
                "Figure A is congruent to Figure B because rotations preserve size.",
                "Figure A is neither similar nor congruent to Figure B.",
                "Figure A is congruent to Figure B only if translated back."
            ],
            "correctAnswer": "Figure A is similar to Figure B (Figure A ~ Figure B), but they are NOT congruent.",
            "explanation": "Because the sequence includes a dilation with scale factor k = 2 (k ≠ 1), side lengths are doubled. Thus the figures are not congruent. However, because dilations and rotations preserve angle measures and side proportionality, Figure A is mathematically similar to Figure B.",
            "hint": "Did the dilation change the size? If size changes, can they be congruent?",
            "points": 10
        },

        # Module 2 Review Test Questions
        {
            "id": "q2_r_01",
            "module": 2,
            "lessonId": "module-2-review",
            "title": "Composite Similarity Sequence Coordinate Calculation",
            "type": "coordinate-input",
            "question": "Point M(4, -8) is dilated with center at (0, 0) by a scale factor of k = 0.5, and then reflected across the y-axis. What are the final coordinates of M''?",
            "prompt": "Step 1: Dilate (x, y) → (0.5x, 0.5y). Step 2: Reflect across y-axis (x, y) → (-x, y).",
            "visualConfig": {
                "type": "composite_similarity",
                "preimage": [{"x": 4, "y": -8, "label": "M"}],
                "intermediate": [{"x": 2, "y": -4, "label": "M'"}],
                "image": [{"x": -2, "y": -4, "label": "M''"}]
            },
            "options": ["(-2, -4)", "(2, 4)", "(-2, 4)", "(2, -4)"],
            "correctAnswer": "(-2, -4)",
            "explanation": "Step 1: Dilation by k = 0.5:\nM'(0.5 · 4, 0.5 · (-8)) = (2, -4).\nStep 2: Reflection across the y-axis negates x:\nM''(-2, -4).\nFinal answer: (-2, -4).",
            "hint": "Half of 4 is 2; flip the sign of x across the y-axis to get -2.",
            "points": 15
        },
        {
            "id": "q2_r_02",
            "module": 2,
            "lessonId": "module-2-review",
            "title": "Comparing Perimeter and Area Multipliers",
            "type": "multiple-choice",
            "question": "Polygon X is dilated to produce Polygon Y using scale factor k = 5. By what factor does the perimeter increase, and by what factor does the area increase?",
            "prompt": "Perimeter multiplier is k; Area multiplier is k².",
            "visualConfig": {
                "type": "scaling_comparison",
                "scaleFactor": 5,
                "perimeterMultiplier": 5,
                "areaMultiplier": 25
            },
            "options": [
                "Perimeter increases by a factor of 5; Area increases by a factor of 25",
                "Perimeter increases by a factor of 5; Area increases by a factor of 5",
                "Perimeter increases by a factor of 10; Area increases by a factor of 25",
                "Perimeter increases by a factor of 25; Area increases by a factor of 125"
            ],
            "correctAnswer": "Perimeter increases by a factor of 5; Area increases by a factor of 25",
            "explanation": "For any dilation with scale factor k:\nPerimeter scales linearly: k = 5.\nArea scales quadratically: k² = 5² = 25.\nTherefore, the perimeter increases by 5, and the area increases by 25.",
            "hint": "Perimeter is 1D (power 1: 5¹), while Area is 2D (power 2: 5²).",
            "points": 15
        },
        {
            "id": "q2_r_03",
            "module": 2,
            "lessonId": "module-2-review",
            "title": "Similarity Statement Correspondence",
            "type": "multiple-choice",
            "question": "If △RST ~ △UVW, RS = 12, ST = 15, and UV = 4, what is the length of side VW?",
            "prompt": "Set up a proportion using corresponding sides: RS / UV = ST / VW.",
            "visualConfig": {
                "type": "proportion_solving",
                "preimage": {"name": "△RST", "RS": 12, "ST": 15},
                "image": {"name": "△UVW", "UV": 4, "VW": "?"}
            },
            "options": [
                "5",
                "3",
                "7.5",
                "10"
            ],
            "correctAnswer": "5",
            "explanation": "Since △RST ~ △UVW, corresponding sides are proportional:\nRS / UV = ST / VW\n12 / 4 = 15 / VW\n3 = 15 / VW\nVW = 15 / 3 = 5.",
            "hint": "The ratio 12 to 4 means the larger triangle is 3 times bigger. Divide 15 by 3.",
            "points": 15
        }
    ]
}

# Write out JavaScript file
js_content = f"// HMH Into Math Grade 8 - Unit 1: Transformational Geometry\n// Complete Curriculum Data for Mariam Hisham AbdelFadil\n\nwindow.CURRICULUM_DATA = {json.dumps(data, indent=2)};\n"

output_path = "/Users/hishammohamedabdelfadil/.gemini/antigravity/scratch/mariam-math-dashboard/curriculum-data.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote curriculum data to {output_path}")
print(f"Total modules: {len(data['modules'])}")
print(f"Total quiz questions: {len(data['quizBank'])}")
