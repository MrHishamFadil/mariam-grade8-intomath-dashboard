# -*- coding: utf-8 -*-
# lessons_db.py
# Complete, rich HMH Into Math Grade 8 Chapter 1 Curriculum for Mariam Hisham Mohamed AbdelFadil
# Auto-updated by merge_all_curriculum.py with 20 high-yield MCQs per lesson for Module 1.

LESSONS = [   {   'id': '1.1',
        'modId': 'mod1',
        'modNum': 1,
        'modTitle': 'Transformations and Congruence',
        'themeColor': '#4f46e5',
        'badge': 'Module 1 • Lesson 1.1',
        'num': '1.1',
        'title': 'Investigate Transformations',
        'tag': 'Rigid Motions & Invariance',
        'standard': 'CCSS.MATH.CONTENT.8.G.A.1',
        'canDo': 'I can determine whether a transformation is a rigid motion (isometry) and '
                 'explain its effects on side lengths, angle measures, parallelism, and vertex '
                 'orientation.',
        'conceptIntro': 'A <strong>geometric transformation</strong> is an operation that maps an '
                        'original figure, called the <strong>preimage</strong>, onto a new figure, '
                        'called the <strong>image</strong>. When a transformation preserves both '
                        'distance (side lengths) and angle measures, it is classified as a '
                        '<strong>rigid motion</strong> (or <strong>isometry</strong>). Rigid '
                        'motions never stretch or distort a shape; therefore, the preimage and '
                        'image are guaranteed to be <strong>congruent (\\(\\cong\\))</strong>.',
        'rules': [   {   'name': 'Distance Invariance',
                         'formula': "AB = A'B'",
                         'desc': 'The length of any segment in the image is strictly equal to the '
                                 'length in the preimage.'},
                     {   'name': 'Angle Invariance',
                         'formula': "m\\angle A = m\\angle A'",
                         'desc': 'All corresponding angle measures remain identical.'},
                     {   'name': 'Parallelism Invariance',
                         'formula': "AB \\parallel CD \\iff A'B' \\parallel C'D'",
                         'desc': 'Lines that were parallel in the preimage remain parallel in the '
                                 'image.'}],
        'vocab': [   {   'term': 'Transformation',
                         'def': 'A function that changes the position, orientation, or size of a '
                                'shape on a coordinate plane.',
                         'ex': 'Translations, reflections, rotations, and dilations.'},
                     {   'term': 'Rigid Motion (Isometry)',
                         'def': 'A transformation that preserves distances and angle measures, '
                                'keeping size and shape identical.',
                         'ex': 'Translations, reflections, and rotations.'},
                     {   'term': 'Preimage & Image',
                         'def': 'The preimage is the original starting shape; the image is the '
                                'resulting shape after the transformation.',
                         'ex': 'Preimage \\(\\triangle ABC\\) maps to image \\(\\triangle '
                               "A'B'C'\\)."},
                     {   'term': 'Orientation',
                         'def': 'The order of vertices (clockwise vs. counterclockwise) or '
                                'direction a figure faces.',
                         'ex': 'Translations and rotations preserve orientation; reflections '
                               'reverse it.'}],
        'invariance': [   {   'prop': 'Side Lengths (Distance)',
                              'status': '✓ Preserved',
                              'cls': 'yes'},
                          {'prop': 'Angle Measures', 'status': '✓ Preserved', 'cls': 'yes'},
                          {'prop': 'Parallelism of Lines', 'status': '✓ Preserved', 'cls': 'yes'},
                          {'prop': 'Collinearity of Points', 'status': '✓ Preserved', 'cls': 'yes'},
                          {   'prop': 'Perimeter & Area',
                              'status': "✓ Identical (P'=P, A'=A)",
                              'cls': 'yes'},
                          {   'prop': 'Orientation',
                              'status': 'Reversed ONLY by reflection',
                              'cls': 'warn'}],
        'illustrativeExamples': [   {   'title': 'Example 1: Testing for Distance Preservation',
                                        'desc': 'A quadrilateral with side lengths 5 cm, 8 cm, 5 '
                                                'cm, and 8 cm is transformed. The resulting '
                                                'quadrilateral has side lengths 10 cm, 16 cm, 10 '
                                                'cm, and 16 cm. Is this a rigid motion?',
                                        'analysis': 'No. The side lengths changed from 5 and 8 to '
                                                    '10 and 16 (each was multiplied by 2). Because '
                                                    'distance is not preserved, this '
                                                    'transformation is <strong>not a rigid '
                                                    'motion</strong> (it is an enlargement '
                                                    'dilation).'},
                                    {   'title': 'Example 2: Analyzing Vertex Orientation in '
                                                 'Reflections',
                                        'desc': 'Triangle \\(ABC\\) has vertices labeled '
                                                'clockwise: \\(A(1, 2)\\), \\(B(4, 2)\\), \\(C(1, '
                                                '6)\\). When reflected across the y-axis, the '
                                                "image vertices are \\(A'(-1, 2)\\), \\(B'(-4, "
                                                "2)\\), and \\(C'(-1, 6)\\).",
                                        'analysis': "Following the vertices \\(A' \\to B' \\to "
                                                    "C'\\) now runs <em>counterclockwise</em>. "
                                                    'While side lengths and angles are preserved, '
                                                    'the orientation has reversed. This reversal '
                                                    'is the hallmark of reflections.'}],
        'workedExample': {   'title': 'Worked Example: Proving Invariance Under Rigid Motion',
                             'problem': 'Right triangle \\(DEF\\) has vertices \\(D(2, 1)\\), '
                                        '\\(E(7, 1)\\), and \\(F(2, 5)\\). It undergoes a rigid '
                                        "motion to create \\(\\triangle D'E'F'\\). Determine the "
                                        "side length \\(D'E'\\), the angle measure \\(m\\angle "
                                        "D'\\), and explain whether \\(\\triangle DEF \\cong "
                                        "\\triangle D'E'F'\\).",
                             'step1': '<strong>Step 1: Calculate measurements in the '
                                      'preimage:</strong> Side \\(DE\\) is horizontal: \\(DE = |7 '
                                      '- 2| = 5\\) units. Side \\(DF\\) is vertical: \\(DF = |5 - '
                                      '1| = 4\\) units. Because horizontal and vertical lines meet '
                                      'at \\(90^\\circ\\), \\(m\\angle D = 90^\\circ\\).',
                             'step2': '<strong>Step 2: Apply the rigid motion property:</strong> '
                                      'By definition, any rigid motion preserves segment lengths '
                                      '(distance) and angle measures without distortion.',
                             'step3': '<strong>Step 3: State the image values and '
                                      "conclusion:</strong> Therefore, \\(D'E' = DE = 5\\) units, "
                                      "and \\(m\\angle D' = m\\angle D = 90^\\circ\\). Because all "
                                      'side lengths and angles are preserved, the figures are '
                                      "congruent: \\(\\triangle DEF \\cong \\triangle D'E'F'\\).",
                             'modelAnswer': '<strong>Student Model Answer:</strong> Side length '
                                            "\\(D'E' = 5\\) units and \\(m\\angle D' = "
                                            '90^\\circ\\). Because rigid motions preserve distance '
                                            'and angle measures, the preimage and image are '
                                            'congruent (\\(\\triangle DEF \\cong \\triangle '
                                            "D'E'F'\\))."},
        'practice': {   'mcqs': [   {   'id': 'p-1-1-mcq-1',
                                        'q': 'Which of the following transformations represents a '
                                             '**rigid motion** (isometry) on the coordinate plane?',
                                        'opts': [   'Doubling the $x$-coordinates while keeping '
                                                    'the $y$-coordinates the same: $(x, y) \\to '
                                                    '(2x, y)$',
                                                    'Dilating a polygon by a scale factor of $0.5$ '
                                                    'centered at the origin: $(x, y) \\to (0.5x, '
                                                    '0.5y)$',
                                                    'Tripling both coordinates: $(x, y) \\to (3x, '
                                                    '3y)$',
                                                    'Translating a polygon $5\\text{ units}$ to '
                                                    'the left and $3\\text{ units}$ up: $(x, y) '
                                                    '\\to (x - 5, y + 3)$'],
                                        'correct': 3,
                                        'hint': 'A rigid motion (isometry) must preserve all '
                                                'segment lengths and angle measures without '
                                                'stretching, shrinking, or distorting the shape.',
                                        'explanation': 'Option D is correct because a translation '
                                                       'slides every point by a fixed distance '
                                                       'without changing side lengths or angles, '
                                                       'making it a rigid motion (isometry). '
                                                       'Options A, B, and C are non-rigid '
                                                       'transformations: Option A is a horizontal '
                                                       'stretch that distorts proportions; Options '
                                                       'B and C are dilations that alter segment '
                                                       'lengths and areas.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-2',
                                        'q': 'Triangle $\\triangle ABC$ has side lengths $AB = '
                                             '7.4\\text{ cm}$, $BC = 5.1\\text{ cm}$, and $AC = '
                                             '9.8\\text{ cm}$. If $\\triangle ABC$ is rotated '
                                             '$90^\\circ$ clockwise about the origin to form '
                                             "$\\triangle A'B'C'$, what is the exact length of "
                                             "side $\\overline{A'B'}$?",
                                        'opts': [   '$5.1\\text{ cm}$',
                                                    '$9.8\\text{ cm}$',
                                                    '$7.4\\text{ cm}$',
                                                    'Cannot be determined without knowing the '
                                                    'center of rotation'],
                                        'correct': 2,
                                        'hint': 'Remember the distance preservation property of '
                                                "rigid motions: $\\text{Length}(A'B') = "
                                                '\\text{Length}(AB)$.',
                                        'explanation': 'Option C is correct because rotation is a '
                                                       'rigid motion (isometry). Under any rigid '
                                                       'motion, line segments are taken to line '
                                                       'segments of the exact same length: '
                                                       "$\\text{Length}(A'B') = \\text{Length}(AB) "
                                                       '= 7.4\\text{ cm}$. Options A and B cite '
                                                       'lengths of other sides ($BC$ and $AC$). '
                                                       'Option D is incorrect because the '
                                                       'preservation of distance holds regardless '
                                                       'of the chosen center of rotation.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-3',
                                        'q': 'In right triangle $\\triangle DEF$, $m\\angle D = '
                                             '38^\\circ$ and $m\\angle E = 90^\\circ$. The '
                                             'triangle is reflected across the $y$-axis to produce '
                                             "$\\triangle D'E'F'$. What is the measure of angle "
                                             "$\\angle F'$?",
                                        'opts': [   '$38^\\circ$',
                                                    '$90^\\circ$',
                                                    '$142^\\circ$',
                                                    '$52^\\circ$'],
                                        'correct': 3,
                                        'hint': 'First calculate the third angle in the preimage '
                                                'using the triangle angle sum ($180^\\circ$), then '
                                                'apply angle preservation.',
                                        'explanation': 'Option D is correct. In preimage '
                                                       '$\\triangle DEF$, the sum of angles is '
                                                       '$180^\\circ$, so $m\\angle F = 180^\\circ '
                                                       '- (90^\\circ + 38^\\circ) = 52^\\circ$. '
                                                       'Because reflection is a rigid motion, '
                                                       "angle measures are preserved: $m\\angle F' "
                                                       '= m\\angle F = 52^\\circ$. Option A is '
                                                       "$m\\angle D'$, Option B is $m\\angle E'$, "
                                                       'and Option C is the obtuse supplement '
                                                       '($180^\\circ - 38^\\circ$).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-4',
                                        'q': 'Trapezoid $PQRS$ has parallel bases $\\overline{PQ} '
                                             '\\parallel \\overline{RS}$, which are separated by a '
                                             'perpendicular distance of $4.5\\text{ cm}$. After '
                                             'trapezoid $PQRS$ is translated $6\\text{ units}$ '
                                             'down and reflected across a vertical line to form '
                                             "$P'Q'R'S'$, which statement must be true?",
                                        'opts': [   "$\\overline{P'Q'}$ and $\\overline{R'S'}$ "
                                                    'intersect at a right angle.',
                                                    "$\\overline{P'Q'} \\parallel "
                                                    "\\overline{R'S'}$ and the perpendicular "
                                                    'distance between them remains $4.5\\text{ '
                                                    'cm}$.',
                                                    "$\\overline{P'Q'} \\parallel "
                                                    "\\overline{R'S'}$, but the distance between "
                                                    'them increases to $9.0\\text{ cm}$ because '
                                                    'two transformations were performed.',
                                                    "$\\overline{P'Q'}$ is no longer parallel to "
                                                    "$\\overline{R'S'}$ because reflection changes "
                                                    'line slopes.'],
                                        'correct': 1,
                                        'hint': 'Consider standard 8.G.A.1.c: Parallel lines are '
                                                'taken to parallel lines under rigid motions.',
                                        'explanation': 'Option B is correct. Translations and '
                                                       'reflections are rigid motions, and their '
                                                       'composition is also a rigid motion. Under '
                                                       'rigid motions, parallel lines map to '
                                                       "parallel lines ($\\overline{P'Q'} "
                                                       "\\parallel \\overline{R'S'}$), and "
                                                       'distances between corresponding points or '
                                                       'parallel segments are invariant '
                                                       '($4.5\\text{ cm}$). Options A and D '
                                                       'falsely claim parallelism is lost. Option '
                                                       'C confuses performing multiple rigid '
                                                       'motions with scaling/dilating.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-5',
                                        'q': 'Three points $L$, $M$, and $N$ lie on the same '
                                             'straight line with $M$ located between $L$ and $N$. '
                                             'Given $LM = 3.2\\text{ cm}$ and $MN = 4.8\\text{ '
                                             'cm}$, the segment undergoes a rigid motion mapping '
                                             "$L \\to L'$, $M \\to M'$, and $N \\to N'$. Which "
                                             'deduction is mathematically guaranteed?',
                                        'opts': [   "$L'$, $M'$, and $N'$ form the vertices of a "
                                                    'scalene triangle with perimeter $16\\text{ '
                                                    'cm}$.',
                                                    "$L'$, $M'$, and $N'$ are non-collinear "
                                                    'because turning a line curves it into an arc.',
                                                    "$L'$, $M'$, and $N'$ remain collinear, $M'$ "
                                                    "is between $L'$ and $N'$, and $L'N' = "
                                                    '8.0\\text{ cm}$.',
                                                    "$M'$ is no longer between $L'$ and $N'$ "
                                                    'because rigid motions reverse the internal '
                                                    'order of points.'],
                                        'correct': 2,
                                        'hint': 'Rigid motions preserve collinearity (lines map to '
                                                'lines) and betweenness of points on a line.',
                                        'explanation': 'Option C is correct. Rigid motions take '
                                                       'straight lines to straight lines and '
                                                       'preserve betweenness of points and segment '
                                                       'addition. In the preimage, $LN = LM + MN = '
                                                       '3.2 + 4.8 = 8.0\\text{ cm}$. Under rigid '
                                                       "motion, $L'M' = 3.2\\text{ cm}$, $M'N' = "
                                                       '4.8\\text{ cm}$, points remain collinear '
                                                       "with $M'$ between $L'$ and $N'$, and $L'N' "
                                                       '= 8.0\\text{ cm}$. Options A and B '
                                                       'contradict the fact that lines map to '
                                                       'lines. Option D is incorrect because '
                                                       'betweenness along a segment is preserved.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-6',
                                        'q': 'Triangle $\\triangle JKL$ has vertices named in '
                                             'clockwise order around its perimeter. The triangle '
                                             'undergoes a rotation of $180^\\circ$ about the '
                                             'origin, followed by a reflection across the vertical '
                                             'line $x = 2$. What is the vertex orientation of the '
                                             "final image $J''K''L''$?",
                                        'opts': [   'Clockwise, because both rotations and '
                                                    'reflections preserve clockwise vertex order.',
                                                    'Undefined, because multiple transformations '
                                                    'destroy vertex order.',
                                                    'Clockwise, because a $180^\\circ$ rotation '
                                                    'reverses orientation and the reflection '
                                                    'reverses it back.',
                                                    'Counterclockwise, because rotation preserves '
                                                    'clockwise orientation, and reflection '
                                                    'reverses it to counterclockwise.'],
                                        'correct': 3,
                                        'hint': 'Recall orientation behavior: translations and '
                                                'rotations are direct isometries (preserve '
                                                'orientation); reflections are opposite isometries '
                                                '(reverse orientation).',
                                        'explanation': 'Option D is correct. A rotation is a '
                                                       'direct isometry, so after the $180^\\circ$ '
                                                       "turn, the vertices $J'K'L'$ remain in "
                                                       'clockwise order. Then, reflecting across '
                                                       'the line $x = 2$ is an opposite isometry, '
                                                       'which flips the chirality (orientation) '
                                                       'from clockwise to counterclockwise. Option '
                                                       'C contains a common student misconception: '
                                                       'rotations do NOT reverse orientation; only '
                                                       'reflections reverse orientation.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-7',
                                        'q': 'A parallelogram has base $b = 8\\text{ cm}$, slant '
                                             'side $s = 5\\text{ cm}$, perpendicular height $h = '
                                             '4\\text{ cm}$, perimeter $P = 26\\text{ cm}$, and '
                                             'area $A = 32\\text{ cm}^2$. If it undergoes a '
                                             '$90^\\circ$ rotation followed by a translation of '
                                             '$\\langle -4, 7 \\rangle$, what are the perimeter '
                                             'and area of the resulting image?',
                                        'opts': [   '$\\text{Perimeter} = 26\\text{ cm}$ and '
                                                    '$\\text{Area} = 32\\text{ cm}^2$',
                                                    '$\\text{Perimeter} = 52\\text{ cm}$ and '
                                                    '$\\text{Area} = 64\\text{ cm}^2$',
                                                    '$\\text{Perimeter} = 26\\text{ cm}$ and '
                                                    '$\\text{Area} = 16\\text{ cm}^2$',
                                                    '$\\text{Perimeter} = 32\\text{ cm}$ and '
                                                    '$\\text{Area} = 26\\text{ cm}^2$'],
                                        'correct': 0,
                                        'hint': 'Since all side lengths and angles are strictly '
                                                'invariant under rigid motions, what happens to '
                                                'their perimeter and enclosed area?',
                                        'explanation': 'Option A is correct. Both rotation and '
                                                       'translation are rigid motions '
                                                       '(isometries). Rigid motions preserve all '
                                                       "linear distances ($A'B' = AB$), meaning "
                                                       "the perimeter remains $P' = P = 26\\text{ "
                                                       'cm}$. They also preserve angle measures '
                                                       'and height, guaranteeing that the enclosed '
                                                       'two-dimensional area is completely '
                                                       "invariant: $A' = A = 32\\text{ cm}^2$. "
                                                       'Options B, C, and D incorrectly alter '
                                                       'perimeter or area.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-8',
                                        'q': 'A student graphs polygon $ABCD$ in Quadrant I. She '
                                             'translates the polygon $10\\text{ units}$ left and '
                                             '$12\\text{ units}$ down into Quadrant III. A peer '
                                             "argues: *'Since the coordinates changed from "
                                             'positive to negative, the shape got smaller and its '
                                             "area became negative.'* How should this argument be "
                                             'refuted?',
                                        'opts': [   'The peer is correct because coordinates in '
                                                    'Quadrant III represent negative geometric '
                                                    'lengths.',
                                                    'The peer is incorrect; coordinates only '
                                                    'specify position on the grid. Distance and '
                                                    'area depend on absolute differences, which '
                                                    'remain invariant under translation.',
                                                    'The peer is incorrect because translations '
                                                    'only change the area when moving diagonally.',
                                                    'The peer is partially correct; side lengths '
                                                    'stay positive, but area is mathematically '
                                                    'defined as negative in Quadrant III.'],
                                        'correct': 1,
                                        'hint': 'Look at the teacher edition note on '
                                                'misconceptions: shifting a figure into a '
                                                'different quadrant changes location, not size or '
                                                'physical attributes.',
                                        'explanation': 'Option B is correct. A major misconception '
                                                       'addressed in the HMH Teacher Edition is '
                                                       'confusing coordinate signs with geometric '
                                                       'measures. Coordinates denote position, but '
                                                       'lengths are Euclidean distances '
                                                       '$\\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$, which '
                                                       'are always non-negative. Translation is a '
                                                       'rigid motion, so side lengths, angles, '
                                                       'perimeter, and area are 100% preserved. '
                                                       'Area cannot be negative. Options A, C, and '
                                                       'D reflect misconceptions.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-9',
                                        'q': 'A graphic design software applies the algebraic '
                                             'mapping $(x, y) \\to (x + 4, 2y)$ to a rectangle '
                                             'with vertices $(0,0)$, $(3,0)$, $(3,2)$, and '
                                             '$(0,2)$. Which statement correctly classifies this '
                                             'transformation?',
                                        'opts': [   'It is a rigid motion because all corners '
                                                    'remain $90^\\circ$ right angles.',
                                                    'It is a rigid motion because it includes a '
                                                    'translation of $+4$ along the $x$-axis.',
                                                    'It is NOT a rigid motion because the vertical '
                                                    'sides are stretched by a factor of $2$, '
                                                    'altering side lengths and doubling area.',
                                                    'It is a rigid motion because it is a '
                                                    'combination of a slide and a flip.'],
                                        'correct': 2,
                                        'hint': 'Check whether corresponding side lengths are '
                                                'equal before and after the mapping.',
                                        'explanation': 'Option C is correct. In the preimage, the '
                                                       'height is $|2 - 0| = 2$. In the image, the '
                                                       '$y$-coordinates are doubled, so the height '
                                                       'becomes $|4 - 0| = 4$. Because the side '
                                                       'length changed from $2$ to $4$, distance '
                                                       "is not preserved ($A'B' \\neq AB$). A "
                                                       'transformation that alters distance is by '
                                                       'definition non-rigid (here, a vertical '
                                                       'stretch). Option A is wrong because '
                                                       'preserving right angles alone is '
                                                       'insufficient (as in dilations and '
                                                       'stretches). Options B and D are factually '
                                                       'inaccurate.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-10',
                                        'q': "Consider the following claim: *'If a transformation "
                                             'preserves all angle measures of any polygon '
                                             "($m\\angle A' = m\\angle A, m\\angle B' = m\\angle "
                                             'B, \\dots$), then the transformation is guaranteed '
                                             "to be a rigid motion.'* Which counterexample "
                                             'definitively disproves this claim?',
                                        'opts': [   'Rotating a square $90^\\circ$ clockwise about '
                                                    'its center',
                                                    'Dilating an equilateral triangle by a scale '
                                                    'factor of $k = 3$, which keeps all angles at '
                                                    '$60^\\circ$ but triples all side lengths',
                                                    'Reflecting an isosceles trapezoid across the '
                                                    'line $y = x$',
                                                    'Translating a scalene triangle $5\\text{ '
                                                    'units}$ horizontally and $2\\text{ units}$ '
                                                    'vertically'],
                                        'correct': 1,
                                        'hint': 'A counterexample must show that angle '
                                                'preservation alone does not guarantee distance '
                                                'preservation.',
                                        'explanation': 'Option B is correct. In a dilation by a '
                                                       'scale factor of $k = 3$, all interior '
                                                       'angles remain exactly $60^\\circ$, yet '
                                                       "every side length is tripled ($s' = 3s$). "
                                                       'Because side lengths are not preserved, '
                                                       'the dilation is NOT a rigid motion. This '
                                                       'proves that angle preservation alone is '
                                                       'insufficient to guarantee an isometry; '
                                                       'distance must also be preserved. Options '
                                                       'A, C, and D are actual rigid motions and '
                                                       'cannot serve as counterexamples.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-11',
                                        'q': 'Triangle $\\triangle ABC$ has vertices $A(2, 1)$, '
                                             '$B(5, 1)$, and $C(2, 6)$. Under a transformation, '
                                             "the image vertices are $A'(-2, 1)$, $B'(-5, 1)$, and "
                                             "$C'(-2, 6)$. Which transformation was performed, and "
                                             'what happened to its vertex orientation?',
                                        'opts': [   'Reflection across the $y$-axis; vertex '
                                                    'orientation reversed from clockwise to '
                                                    'counterclockwise.',
                                                    'Translation $4\\text{ units}$ left; vertex '
                                                    'orientation was preserved.',
                                                    'Rotation $180^\\circ$ about the origin; '
                                                    'vertex orientation was preserved.',
                                                    'Reflection across the $x$-axis; vertex '
                                                    'orientation remained clockwise.'],
                                        'correct': 0,
                                        'hint': 'Observe the coordinates: $(x, y) \\to (-x, y)$. '
                                                'What transformation negates only the '
                                                '$x$-coordinate?',
                                        'explanation': 'Option A is correct. The coordinate rule '
                                                       '$(x, y) \\to (-x, y)$ represents a '
                                                       'reflection across the $y$-axis. In the '
                                                       'preimage, tracing $A(2,1) \\to B(5,1) \\to '
                                                       'C(2,6)$ moves along the base rightward, '
                                                       'then up-left back to $A$, which is '
                                                       "counterclockwise. In the image, $A'(-2,1) "
                                                       "\\to B'(-5,1) \\to C'(-2,6)$ moves "
                                                       'leftward along the base, then up-right, '
                                                       'which is clockwise. Testing shows that '
                                                       'reflection across a line always reverses '
                                                       'orientation (swaps chirality). Option B is '
                                                       'wrong because $B$ shifted by $-10$, not '
                                                       '$-4$. Option C rule would be $(-x, -y)$. '
                                                       'Option D rule would be $(x, -y)$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-12',
                                        'q': 'A carpenter cuts boards to create identical pieces '
                                             'for a birdhouse (from Into Math TE). A board in the '
                                             'shape of a trapezoid has one pair of parallel sides '
                                             'that are $2\\text{ inches}$ apart. The carpenter '
                                             'turns the board one-quarter turn ($90^\\circ$) '
                                             'clockwise on her table. What is true about the '
                                             'parallel sides of the turned board?',
                                        'opts': [   'The parallel sides remain parallel and are '
                                                    'still exactly $2\\text{ inches}$ apart.',
                                                    'The sides are no longer parallel because '
                                                    'turning them changed their directions.',
                                                    'The parallel sides remain parallel, but the '
                                                    'distance between them is now $2 \\times '
                                                    '\\sqrt{2} \\approx 2.83\\text{ inches}$.',
                                                    'The parallel sides become perpendicular to '
                                                    'each other.'],
                                        'correct': 0,
                                        'hint': 'Teacher Edition problem 7 & 12 note: Parallel '
                                                'lines stay parallel, and the distance between '
                                                'them remains constant under rigid motions.',
                                        'explanation': 'Option A is correct. As emphasized in Into '
                                                       'Math TE Lesson 1.1 Problems 7 and 11-12, '
                                                       'when a shape undergoes a turn (rotation), '
                                                       'rigid motion properties guarantee that: '
                                                       '(1) parallel lines are taken to parallel '
                                                       'lines, and (2) the distance between '
                                                       'parallel lines remains exactly the same '
                                                       '($2\\text{ inches}$). Option B is a '
                                                       'misconception. Options C and D incorrectly '
                                                       'assume rotating changes metric distance '
                                                       'between lines.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-13',
                                        'q': 'Line segment $\\overline{AB}$ is horizontal with '
                                             'length $AB = 6\\text{ cm}$. A student rotates the '
                                             'segment $45^\\circ$ counterclockwise about endpoint '
                                             "$A$. The student claims: *'Because the segment is "
                                             'now slanted diagonally across grid squares, its '
                                             "length must be greater than $6\\text{ cm}$.'* What "
                                             'error did the student make?',
                                        'opts': [   'The student should have measured the length '
                                                    'in inches instead of centimeters.',
                                                    'The student forgot that rotating a segment by '
                                                    '$45^\\circ$ cuts its length in half.',
                                                    'The student failed to realize that only '
                                                    '$90^\\circ$ and $180^\\circ$ rotations '
                                                    'preserve lengths.',
                                                    'The student confused the visual slope/slant '
                                                    'with geometric length; rotations are rigid '
                                                    'motions, so distance is invariant regardless '
                                                    'of tilt.'],
                                        'correct': 3,
                                        'hint': 'Teacher Edition Common Error: Students often '
                                                'believe that diagonal segments are automatically '
                                                'longer than horizontal ones, confusing coordinate '
                                                'grid alignment with physical length.',
                                        'explanation': 'Option D is correct. A well-documented '
                                                       'misconception in the HMH Into Math TE is '
                                                       'that students equate diagonal orientation '
                                                       'with increased length (often thinking of '
                                                       'the hypotenuse of grid squares). However, '
                                                       'rotation is a rigid motion (isometry), '
                                                       'which guarantees that the distance between '
                                                       'endpoints remains invariant: '
                                                       "$\\text{Length}(A'B') = \\text{Length}(AB) "
                                                       '= 6\\text{ cm}$. Options A, B, and C '
                                                       'contain false mathematical claims.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-14',
                                        'q': 'Triangle $\\triangle PQR$ has angle measures '
                                             '$m\\angle P = 40^\\circ$, $m\\angle Q = 60^\\circ$, '
                                             'and $m\\angle R = 80^\\circ$, with an area of '
                                             '$24\\text{ cm}^2$. It is reflected across line '
                                             '$\\ell$ and then rotated $60^\\circ$ about point '
                                             "$P'$. What are the interior angle sum and area of "
                                             "the resulting triangle $P''Q''R''$?",
                                        'opts': [   'Interior angle sum $= 240^\\circ$, '
                                                    '$\\text{Area} = 24\\text{ cm}^2$',
                                                    'Interior angle sum $= 360^\\circ$, '
                                                    '$\\text{Area} = 48\\text{ cm}^2$',
                                                    'Interior angle sum $= 180^\\circ$, '
                                                    '$\\text{Area} = 24\\text{ cm}^2$',
                                                    'Interior angle sum $= 180^\\circ$, '
                                                    '$\\text{Area} = 12\\text{ cm}^2$'],
                                        'correct': 2,
                                        'hint': 'Sequences of rigid motions preserve angle '
                                                'measures, side lengths, and area.',
                                        'explanation': 'Option C is correct. The composition of '
                                                       'two rigid motions (a reflection followed '
                                                       'by a rotation) is also a rigid motion. '
                                                       'Every individual angle measure is '
                                                       'preserved ($40^\\circ, 60^\\circ, '
                                                       '80^\\circ$), so their sum remains strictly '
                                                       '$180^\\circ$. Furthermore, because side '
                                                       'lengths and altitudes are invariant, the '
                                                       'area remains exactly $24\\text{ cm}^2$. '
                                                       'Options A, B, and D incorrectly alter the '
                                                       'angle sum or area.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-15',
                                        'q': 'Which of the following correctly describes how basic '
                                             'transformations affect the **orientation** '
                                             '(clockwise vs. counterclockwise ordering of '
                                             'vertices) of a figure?',
                                        'opts': [   'Translations and reflections preserve '
                                                    'orientation; rotations reverse it.',
                                                    'Translations and rotations preserve '
                                                    'orientation (direct isometries); reflections '
                                                    'reverse orientation (opposite isometries).',
                                                    'Rotations and reflections preserve '
                                                    'orientation; translations reverse it.',
                                                    'All transformations (translations, rotations, '
                                                    'reflections) reverse orientation.'],
                                        'correct': 1,
                                        'hint': 'Think of looking at a clock face: when you slide '
                                                'it or turn it, the numbers still run clockwise. '
                                                'What happens when you look at it in a mirror?',
                                        'explanation': 'Option B is correct. Translations (slides) '
                                                       'and rotations (turns) keep vertices in the '
                                                       'same relative clockwise order around the '
                                                       'perimeter, so they are direct isometries. '
                                                       'A reflection (flip) produces a mirror '
                                                       'image, reversing the clockwise order to '
                                                       'counterclockwise (or vice versa), making '
                                                       'it an opposite isometry. Options A, C, and '
                                                       'D misstate these fundamental properties.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-16',
                                        'q': 'On straight line segment $\\overline{AC}$, point $B$ '
                                             'lies between $A$ and $C$ such that $AB = x + 3$, $BC '
                                             '= 2x - 1$, and $AC = 14\\text{ cm}$. The segment '
                                             "undergoes a rigid motion mapping $A \\to A'$, $B "
                                             "\\to B'$, and $C \\to C'$. What is the length of "
                                             "image segment $\\overline{A'B'}$?",
                                        'opts': [   '$4\\text{ cm}$',
                                                    '$5\\text{ cm}$',
                                                    '$9\\text{ cm}$',
                                                    '$7\\text{ cm}$'],
                                        'correct': 3,
                                        'hint': 'Use the segment addition postulate $AB + BC = AC$ '
                                                'to solve for $x$, find $AB$, and apply distance '
                                                'preservation.',
                                        'explanation': 'Option D is correct. By betweenness and '
                                                       'the segment addition postulate: $AB + BC = '
                                                       'AC \\implies (x + 3) + (2x - 1) = 14 '
                                                       '\\implies 3x + 2 = 14 \\implies 3x = 12 '
                                                       '\\implies x = 4$. Therefore, $AB = 4 + 3 = '
                                                       '7\\text{ cm}$ (and $BC = 2(4) - 1 = '
                                                       '7\\text{ cm}$). Because a rigid motion '
                                                       'preserves distances between all points, '
                                                       "$A'B' = AB = 7\\text{ cm}$. Option A is "
                                                       'the value of $x$, Option B is an '
                                                       'arithmetic error, and Option C is $x+5$.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-17',
                                        'q': 'Which of the following coordinate rules represents a '
                                             'transformation that is **NEVER** a rigid motion?',
                                        'opts': [   '$(x, y) \\to (x - 7, y + 4)$',
                                                    '$(x, y) \\to (-y, x)$',
                                                    '$(x, y) \\to (x, -y)$',
                                                    '$(x, y) \\to (3x, 3y)$'],
                                        'correct': 3,
                                        'hint': 'Look for a rule where coordinates are multiplied '
                                                'by a number other than $1$ or $-1$, scaling the '
                                                'size of the shape.',
                                        'explanation': 'Option D is correct. The rule $(x, y) \\to '
                                                       '(3x, 3y)$ multiplies all coordinates by '
                                                       '$3$, creating a dilation with scale factor '
                                                       '$k = 3$. This triples all segment lengths '
                                                       "($d' = 3d$) and multiplies the area by "
                                                       '$3^2 = 9$. Because distance is not '
                                                       'preserved, it is never a rigid motion. '
                                                       'Option A is a translation, Option B is a '
                                                       '$90^\\circ$ counterclockwise rotation, and '
                                                       'Option C is a reflection across the '
                                                       '$x$-axis—all of which are rigid motions.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-18',
                                        'q': 'A student examines two rhombuses:\n'
                                             '- **Rhombus 1:** Side length $5\\text{ cm}$, '
                                             'perimeter $20\\text{ cm}$, and interior angles '
                                             '$74^\\circ$ and $106^\\circ$.\n'
                                             '- **Rhombus 2:** Side length $5\\text{ cm}$, '
                                             'perimeter $20\\text{ cm}$, and interior angles '
                                             '$60^\\circ$ and $120^\\circ$.\n'
                                             'Can Rhombus 2 be formed by applying a rigid motion '
                                             'to Rhombus 1?',
                                        'opts': [   'Yes, because both rhombuses have the exact '
                                                    'same side lengths and perimeter of $20\\text{ '
                                                    'cm}$.',
                                                    'Yes, because turning a rhombus changes its '
                                                    'angle measures to fit a new orientation.',
                                                    'No, because rigid motions MUST preserve all '
                                                    'angle measures, and $74^\\circ \\neq '
                                                    '60^\\circ$.',
                                                    'No, because rigid motions cannot be applied '
                                                    'to four-sided shapes.'],
                                        'correct': 2,
                                        'hint': 'Recall: A rigid motion must preserve BOTH '
                                                'distance (side lengths) AND angle measures '
                                                'simultaneously.',
                                        'explanation': 'Option C is correct. A rigid motion '
                                                       '(isometry) requires the preservation of '
                                                       'BOTH side lengths AND angle measures '
                                                       "($m\\angle A' = m\\angle A$). Although "
                                                       'both shapes share the same side lengths '
                                                       '($5\\text{ cm}$) and perimeter ($20\\text{ '
                                                       'cm}$), their angle measures differ '
                                                       '($74^\\circ \\neq 60^\\circ$). Because '
                                                       'angle measures are not preserved, Rhombus '
                                                       '2 cannot be the image of Rhombus 1 under '
                                                       'any rigid motion. Option A confuses '
                                                       'perimeter equality with congruence. Option '
                                                       'B is a common misconception.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-19',
                                        'q': 'Reginald draws regular hexagon $ABCDEF$ with side '
                                             'length $s = 4\\text{ cm}$ and three pairs of '
                                             'opposite parallel sides (from Into Math TE Wrap-Up '
                                             'Exit Ticket). He rotates the hexagon $120^\\circ$ '
                                             'counterclockwise about its center. Which statement '
                                             "accurately describes image $A'B'C'D'E'F'$?",
                                        'opts': [   'All side lengths remain $4\\text{ cm}$, all '
                                                    'interior angles remain $120^\\circ$, opposite '
                                                    'sides remain parallel, and perimeter is '
                                                    '$24\\text{ cm}$.',
                                                    'Side lengths increase to $6\\text{ cm}$ and '
                                                    'opposite sides intersect because rotation '
                                                    'turns sides in different directions.',
                                                    'The interior angles increase by $120^\\circ$ '
                                                    'to $240^\\circ$, but side lengths stay '
                                                    '$4\\text{ cm}$.',
                                                    'The hexagon becomes irregular because '
                                                    'horizontal sides stay fixed while slanted '
                                                    'sides rotate.'],
                                        'correct': 0,
                                        'hint': 'See HMH Into Math TE page 31 Exit Ticket: '
                                                'Reginald rotates a regular hexagon. What is true '
                                                'of the angles, side lengths, and parallel sides?',
                                        'explanation': 'Option A is correct. In the TE Wrap-Up '
                                                       'Exit Ticket (page 31), students verify '
                                                       'that when Reginald rotates a regular '
                                                       'hexagon, angles stay the same '
                                                       '($120^\\circ$), side lengths stay the same '
                                                       '($4\\text{ cm}$), perimeter stays the same '
                                                       '($6 \\times 4 = 24\\text{ cm}$), and '
                                                       'opposite parallel sides remain parallel. '
                                                       'Rigid motions preserve all metric '
                                                       'properties and parallelism uniformly '
                                                       'across the entire polygon. Options B, C, '
                                                       'and D are false.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'},
                                    {   'id': 'p-1-1-mcq-20',
                                        'q': 'A mathematics class analyzes four statements about '
                                             'transformations:\n'
                                             '1. *Under any rigid motion, if line $m \\parallel '
                                             "\\text{line } n$, then their images satisfy $m' "
                                             "\\parallel n'$.*\n"
                                             '2. *If a transformation preserves the area of a '
                                             'rectangle, it is guaranteed to be a rigid motion.*\n'
                                             '3. *A reflection across a line preserves all side '
                                             'lengths and angle measures, but reverses vertex '
                                             'orientation (chirality).*\n'
                                             '4. *Translating a polygon from Quadrant I to '
                                             'Quadrant III reduces the side lengths of the polygon '
                                             'because the coordinates become negative.*\n'
                                             'Which of these statements are mathematically '
                                             '**TRUE**?',
                                        'opts': [   'Statements 1 and 3 only',
                                                    'Statements 1, 2, and 3 only',
                                                    'Statements 2 and 4 only',
                                                    'Statements 1, 3, and 4 only'],
                                        'correct': 0,
                                        'hint': 'Evaluate each statement individually: Statement 1 '
                                                '(parallelism), Statement 2 (can non-rigid shear '
                                                'or stretch preserve area?), Statement 3 '
                                                '(reflection properties), Statement 4 (quadrant '
                                                'misconception).',
                                        'explanation': 'Option A is correct.\n'
                                                       '- Statement 1 is TRUE: CCSS 8.G.A.1.c '
                                                       'states that parallel lines are taken to '
                                                       'parallel lines under rigid motions.\n'
                                                       '- Statement 2 is FALSE: A horizontal '
                                                       'stretch by $2$ combined with a vertical '
                                                       'compression by $\\frac{1}{2}$ preserves '
                                                       'area ($2 \\times \\frac{1}{2} = 1$), but '
                                                       'distorts side lengths and angles, so it is '
                                                       'NOT a rigid motion.\n'
                                                       '- Statement 3 is TRUE: Reflections '
                                                       'preserve distance and angle measures, but '
                                                       'reverse vertex orientation from clockwise '
                                                       'to counterclockwise.\n'
                                                       '- Statement 4 is FALSE: Coordinates become '
                                                       'negative, but side lengths are distances, '
                                                       'which are invariant under translation.\n'
                                                       'Therefore, only Statements 1 and 3 are '
                                                       'true.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1'}],
                        'fitb': [   {   'id': 'p-1-1-f1',
                                        'q': 'If \\(\\triangle ABC\\) has \\(m\\angle B = '
                                             "62^\\circ\\), what is \\(m\\angle B'\\) after "
                                             'undergoing a rotation? (Enter number)',
                                        'expected': '62',
                                        'hint': 'Rotations are rigid motions, which preserve all '
                                                'angle measures.'},
                                    {   'id': 'p-1-1-f2',
                                        'q': 'A transformation that preserves both distance and '
                                             'angle measures is called a(n) ________ (or '
                                             'isometry).',
                                        'expected': 'rigid motion',
                                        'altExpected': ['rigid motion', 'rigid transformation'],
                                        'hint': "Two words: starts with 'rigid'."}]},
        'bookQuestions': [   {   'num': 'HMH Into Math • Section 1.1 Question 3',
                                 'q': 'Triangle \\(XYZ\\) has perimeter \\(18.5\\text{ cm}\\). '
                                      'After a transformation, the perimeter of \\(\\triangle '
                                      "X'Y'Z'\\) is \\(18.5\\text{ cm}\\) and all angle measures "
                                      'are preserved. Can you conclude that the transformation is '
                                      'definitely a rigid motion? Explain.',
                                 'modelAnswer': '<strong>Model Answer:</strong> Yes. Because both '
                                                'the side lengths (which sum to the perimeter) and '
                                                'all corresponding angle measures are preserved, '
                                                'the transformation maintains identical shape and '
                                                'size, which satisfies the mathematical definition '
                                                'of a rigid motion (isometry).'},
                             {   'num': 'HMH Into Math • Section 1.1 Question 8',
                                 'q': 'Compare and contrast the effects of a translation and a '
                                      'reflection on vertex orientation. Give a specific '
                                      'coordinate example.',
                                 'modelAnswer': '<strong>Model Answer:</strong> A translation '
                                                'preserves orientation; if vertices are in '
                                                'clockwise order in the preimage, they remain '
                                                'clockwise in the image. In contrast, a reflection '
                                                'reverses orientation from clockwise to '
                                                'counterclockwise (or vice versa). For example, '
                                                'reflecting \\(A(1, 2), B(3, 2), C(1, 4)\\) across '
                                                'the y-axis flips the horizontal order of '
                                                'vertices.'}]},
    {   'id': '1.2',
        'modId': 'mod1',
        'modNum': 1,
        'modTitle': 'Transformations and Congruence',
        'themeColor': '#4f46e5',
        'badge': 'Module 1 • Lesson 1.2',
        'num': '1.2',
        'title': 'Explore Translations',
        'tag': 'Vectors & Mapping Rules',
        'standard': 'CCSS.MATH.CONTENT.8.G.A.1.a, 8.G.A.3',
        'canDo': 'I can translate figures on the coordinate plane, describe translations using '
                 'words and algebraic mapping notation \\((x, y) \\to (x + a, y + b)\\), and find '
                 'image or preimage coordinates.',
        'conceptIntro': 'A <strong>translation</strong> is a rigid motion that slides every point '
                        'of a figure the exact same distance and in the exact same direction along '
                        'a straight line vector \\(\\vec{v} = \\langle a, b \\rangle\\). In '
                        'coordinate notation: \\((x, y) \\to (x + a, y + b)\\). When \\(a > 0\\), '
                        'the figure shifts <strong>right</strong>; when \\(a < 0\\), it shifts '
                        '<strong>left</strong>. When \\(b > 0\\), the figure shifts '
                        '<strong>up</strong>; when \\(b < 0\\), it shifts <strong>down</strong>.',
        'rules': [   {   'name': 'Algebraic Translation Rule',
                         'formula': '(x, y) \\to (x + a, y + b)',
                         'desc': "Add horizontal shift 'a' to x; add vertical shift 'b' to y."},
                     {   'name': 'Parallel Segment Property',
                         'formula': "AA' \\parallel BB' \\parallel CC'",
                         'desc': 'Segments connecting corresponding preimage and image points are '
                                 "parallel and equal in length: \\(AA' = BB' = CC' = \\sqrt{a^2 + "
                                 'b^2}\\).'}],
        'vocab': [   {   'term': 'Translation',
                         'def': 'A transformation that slides every point of a figure by a '
                                'specified horizontal and vertical distance without turning or '
                                'flipping.',
                         'ex': 'Sliding a shape 4 units right and 3 units down.'},
                     {   'term': 'Vector \\(\\langle a, b \\rangle\\)',
                         'def': 'A quantity specifying both direction and distance of movement.',
                         'ex': '\\(\\langle -3, 5 \\rangle\\) means 3 units left and 5 units up.'},
                     {   'term': 'Prime Notation',
                         'def': "The symbol (') appended to letters denoting image vertices.",
                         'ex': "Point \\(A(2, 3)\\) translates to \\(A'(6, 1)\\)."}],
        'invariance': [   {   'prop': 'Side Lengths (Distance)',
                              'status': '✓ Preserved',
                              'cls': 'yes'},
                          {'prop': 'Angle Measures', 'status': '✓ Preserved', 'cls': 'yes'},
                          {   'prop': 'Orientation',
                              'status': '✓ Preserved (Same direction)',
                              'cls': 'yes'},
                          {   'prop': 'Slope of Segments',
                              'status': '✓ Preserved (Parallel lines)',
                              'cls': 'yes'},
                          {'prop': 'Area & Perimeter', 'status': '✓ Preserved', 'cls': 'yes'}],
        'illustrativeExamples': [   {   'title': 'Example 1: Translating a Single Point',
                                        'desc': 'Find the image of point \\(P(-4, 7)\\) under the '
                                                'translation rule \\((x, y) \\to (x + 6, y - '
                                                '9)\\).',
                                        'analysis': "Apply the rule to each coordinate: \\(x' = -4 "
                                                    "+ 6 = 2\\) and \\(y' = 7 - 9 = -2\\). "
                                                    "Therefore, \\(P' = (2, -2)\\)."},
                                    {   'title': 'Example 2: Determining the Translation Rule from '
                                                 'Coordinates',
                                        'desc': "Point \\(M(3, -1)\\) translates to \\(M'(-2, "
                                                '4)\\). Write the algebraic mapping rule.',
                                        'analysis': "Horizontal change: \\(a = x' - x = -2 - 3 = "
                                                    "-5\\). Vertical change: \\(b = y' - y = 4 - "
                                                    '(-1) = 5\\). Rule: \\((x, y) \\to (x - 5, y + '
                                                    '5)\\) (slide 5 units left and 5 units up).'}],
        'workedExample': {   'title': 'Worked Example: Translating a Polygon & Finding All Image '
                                      'Vertices',
                             'problem': 'Triangle \\(ABC\\) has vertices \\(A(-3, 2)\\), \\(B(1, '
                                        '4)\\), and \\(C(0, -1)\\). It is translated along the '
                                        'vector \\(\\langle 4, -3 \\rangle\\). (a) Write the '
                                        'algebraic mapping rule. (b) Determine the coordinates of '
                                        "\\(A'\\), \\(B'\\), and \\(C'\\). (c) Confirm whether "
                                        "\\(\\triangle ABC \\cong \\triangle A'B'C'\\).",
                             'step1': '<strong>Step 1: Formulate the algebraic rule:</strong> '
                                      'Vector \\(\\langle 4, -3 \\rangle\\) corresponds to '
                                      'horizontal shift \\(a = +4\\) and vertical shift \\(b = '
                                      '-3\\). Rule: \\((x, y) \\to (x + 4, y - 3)\\).',
                             'step2': '<strong>Step 2: Substitute each vertex into the '
                                      "rule:</strong><br>• \\(A(-3, 2) \\to A'(-3 + 4, 2 - 3) = "
                                      "A'(1, -1)\\)<br>• \\(B(1, 4) \\to B'(1 + 4, 4 - 3) = B'(5, "
                                      "1)\\)<br>• \\(C(0, -1) \\to C'(0 + 4, -1 - 3) = C'(4, "
                                      '-4)\\).',
                             'step3': '<strong>Step 3: Justify congruence:</strong> Because '
                                      'translations are rigid motions, distance, angle measures, '
                                      'and orientation are preserved. Therefore, \\(\\triangle ABC '
                                      "\\cong \\triangle A'B'C'\\).",
                             'modelAnswer': '<strong>Student Model Answer:</strong> Mapping rule: '
                                            '\\((x, y) \\to (x + 4, y - 3)\\). The image vertices '
                                            "are \\(A'(1, -1)\\), \\(B'(5, 1)\\), and \\(C'(4, "
                                            '-4)\\). Because a translation is a rigid motion, '
                                            "\\(\\triangle ABC \\cong \\triangle A'B'C'\\)."},
        'practice': {   'mcqs': [   {   'id': 'p-1-2-mcq-1',
                                        'q': 'A translation slides a geometric figure $6\\text{ '
                                             'units left}$ and $8\\text{ units up}$ on a '
                                             'coordinate plane. Which vector represents this '
                                             'transformation in component vector notation?',
                                        'opts': [   '$\\langle 6, -8 \\rangle$',
                                                    '$\\langle -6, 8 \\rangle$',
                                                    '$\\langle 8, -6 \\rangle$',
                                                    '$\\langle -8, 6 \\rangle$'],
                                        'correct': 1,
                                        'hint': 'In vector notation $\\langle a, b \\rangle$, the '
                                                'first value $a$ represents horizontal change '
                                                '(negative for left, positive for right), and the '
                                                'second value $b$ represents vertical change '
                                                '(positive for up, negative for down).',
                                        'explanation': 'A horizontal shift of 6 units to the left '
                                                       'is represented by $a = -6$, and a vertical '
                                                       'shift of 8 units up is represented by $b = '
                                                       '+8$. Thus, the vector in component '
                                                       'notation is $\\langle -6, 8 \\rangle$. '
                                                       'Choice A reverses the positive and '
                                                       'negative directions. Choices C and D swap '
                                                       'the horizontal and vertical components.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-2',
                                        'q': 'Which algebraic mapping rule correctly represents '
                                             'translating a polygon $4\\text{ units right}$ and '
                                             '$7\\text{ units down}$ on a Cartesian coordinate '
                                             'plane?',
                                        'opts': [   '$(x, y) \\to (x + 4, y - 7)$',
                                                    '$(x, y) \\to (x - 4, y + 7)$',
                                                    '$(x, y) \\to (x + 7, y - 4)$',
                                                    '$(x, y) \\to (4x, -7y)$'],
                                        'correct': 0,
                                        'hint': 'Moving right increases the $x$-coordinate, while '
                                                'moving down decreases the $y$-coordinate.',
                                        'explanation': 'Moving 4 units right adds 4 to each '
                                                       '$x$-coordinate ($x \\to x + 4$). Moving 7 '
                                                       'units down subtracts 7 from each '
                                                       '$y$-coordinate ($y \\to y - 7$). Combining '
                                                       'these gives $(x, y) \\to (x + 4, y - 7)$. '
                                                       'Choice B incorrectly subtracts for right '
                                                       'and adds for down. Choice C swaps the $x$ '
                                                       'and $y$ shifts. Choice D uses '
                                                       'multiplication, which describes a dilation '
                                                       'rather than a translation.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-3',
                                        'q': 'Point $W(-5, 9)$ undergoes the pure horizontal '
                                             'translation $(x, y) \\to (x + 8, y)$. What are the '
                                             "coordinates of the image point $W'$?",
                                        'opts': [   '$(-13, 9)$',
                                                    '$(-5, 17)$',
                                                    '$(3, 9)$',
                                                    '$(3, 17)$'],
                                        'correct': 2,
                                        'hint': 'Only the $x$-coordinate is modified by adding 8; '
                                                'the $y$-coordinate remains completely unchanged.',
                                        'explanation': 'Applying the rule $(x, y) \\to (x + 8, y)$ '
                                                       "to $W(-5, 9)$: $x' = -5 + 8 = 3$, and $y' "
                                                       "= 9$. Thus, $W' = (3, 9)$. Choice A "
                                                       'mistakenly subtracts 8 ($-5 - 8 = -13$). '
                                                       'Choice B mistakenly adds 8 to the '
                                                       '$y$-coordinate. Choice D erroneously adds '
                                                       '8 to both coordinates.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-4',
                                        'q': 'A line segment on a blueprint with endpoint $P(4, '
                                             '-3)$ is translated vertically such that its image is '
                                             "$P'(4, -11)$. Which translation rule was applied to "
                                             'the segment?',
                                        'opts': [   '$(x, y) \\to (x, y - 8)$',
                                                    '$(x, y) \\to (x, y + 8)$',
                                                    '$(x, y) \\to (x - 8, y)$',
                                                    '$(x, y) \\to (x, y - 14)$'],
                                        'correct': 0,
                                        'hint': 'Calculate the vertical change: $b = '
                                                'y_{\\text{image}} - y_{\\text{preimage}} = -11 - '
                                                '(-3)$.',
                                        'explanation': 'The $x$-coordinate does not change ($4 '
                                                       '\\to 4$), so there is zero horizontal '
                                                       'displacement. The vertical displacement is '
                                                       "$b = y' - y = -11 - (-3) = -11 + 3 = -8$, "
                                                       'meaning the segment moved 8 units down. '
                                                       'The mapping rule is $(x, y) \\to (x, y - '
                                                       '8)$. Choice B incorrectly adds 8 instead '
                                                       'of subtracting. Choice C applies the shift '
                                                       'horizontally. Choice D adds $-11$ and $-3$ '
                                                       'to get $-14$.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-5',
                                        'q': 'Triangle $DEF$ has vertices $D(-3, 4)$, $E(1, 6)$, '
                                             'and $F(2, -1)$. The triangle is translated according '
                                             'to the rule $(x, y) \\to (x + 5, y - 6)$. What are '
                                             "the coordinates of vertex $D'$?",
                                        'opts': [   '$(-8, 10)$',
                                                    '$(2, 10)$',
                                                    '$(-8, -2)$',
                                                    '$(2, -2)$'],
                                        'correct': 3,
                                        'hint': 'Substitute $x = -3$ and $y = 4$ directly into the '
                                                "algebraic rule: $x' = -3 + 5$ and $y' = 4 - 6$.",
                                        'explanation': 'Substituting $D(-3, 4)$ into $(x + 5, y - '
                                                       "6)$ yields $x' = -3 + 5 = 2$ and $y' = 4 - "
                                                       "6 = -2$. Therefore, $D' = (2, -2)$. Choice "
                                                       'A subtracts 5 and adds 6 ($(-8, 10)$). '
                                                       'Choice B mistakenly adds 6 to $y$ ($4 + 6 '
                                                       '= 10$). Choice C subtracts 5 from $x$ ($-3 '
                                                       '- 5 = -8$).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-6',
                                        'q': 'In a computer graphic animation, polygon vertex '
                                             "$K(7, -3)$ maps to image vertex $K'(-1, 5)$ under a "
                                             'translation. Which algebraic rule describes this '
                                             'translation?',
                                        'opts': [   '$(x, y) \\to (x + 8, y - 8)$',
                                                    '$(x, y) \\to (x - 8, y + 8)$',
                                                    '$(x, y) \\to (x - 6, y + 2)$',
                                                    '$(x, y) \\to (x + 6, y - 2)$'],
                                        'correct': 1,
                                        'hint': 'Always subtract the preimage coordinates from the '
                                                "image coordinates: $a = x' - x$ and $b = y' - y$.",
                                        'explanation': 'Calculate the horizontal displacement: $a '
                                                       "= x' - x = -1 - 7 = -8$. Calculate the "
                                                       "vertical displacement: $b = y' - y = 5 - "
                                                       '(-3) = 5 + 3 = 8$. Thus, the rule is $(x, '
                                                       'y) \\to (x - 8, y + 8)$. Choice A '
                                                       'subtracts image from preimage ($7 - (-1) = '
                                                       '8$), which reverses the direction vector. '
                                                       'Choices C and D add coordinates instead of '
                                                       'computing differences.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-7',
                                        'q': 'After a translation using the rule $(x, y) \\to (x - '
                                             "6, y + 9)$, the image of point $M$ is $M'(2, -4)$. "
                                             'What were the coordinates of the original preimage '
                                             'point $M$?',
                                        'opts': [   '$(8, -13)$',
                                                    '$(-4, 5)$',
                                                    '$(8, 5)$',
                                                    '$(-4, -13)$'],
                                        'correct': 0,
                                        'hint': 'Work backward from the image coordinates by '
                                                'applying inverse operations: solve $x - 6 = 2$ '
                                                'and $y + 9 = -4$.',
                                        'explanation': 'To recover the preimage from the image, '
                                                       "apply the inverse operations: $x = x' + 6 "
                                                       "= 2 + 6 = 8$, and $y = y' - 9 = -4 - 9 = "
                                                       '-13$. Thus, $M = (8, -13)$. Verifying '
                                                       'forward: $(8 - 6, -13 + 9) = (2, -4) = '
                                                       "M'$. Choice B erroneously applies the "
                                                       "forward rule to $M'$ ($2 - 6 = -4, -4 + 9 "
                                                       '= 5$). Choice C adds 9 to $y$ instead of '
                                                       'subtracting. Choice D subtracts 6 from '
                                                       '$x$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-8',
                                        'q': 'Triangle $ABC$ lies in **Quadrant II** with vertex '
                                             '$A(-4, 5)$. The triangle is translated by the rule '
                                             '$(x, y) \\to (x + 9, y - 8)$. In which quadrant of '
                                             "the coordinate plane does the image vertex $A'$ lie?",
                                        'opts': [   'Quadrant I',
                                                    'Quadrant II',
                                                    'Quadrant III',
                                                    'Quadrant IV'],
                                        'correct': 3,
                                        'hint': "Calculate the image coordinates $A'(x', y')$ and "
                                                'inspect their signs: $(+, +)$ is Quadrant I, $(-, '
                                                '+)$ is Quadrant II, $(-, -)$ is Quadrant III, and '
                                                '$(+, -)$ is Quadrant IV.',
                                        'explanation': 'Applying the translation rule to $A(-4, '
                                                       "5)$: $x' = -4 + 9 = 5$ (positive) and $y' "
                                                       '= 5 - 8 = -3$ (negative). An ordered pair '
                                                       'with a positive $x$-value and negative '
                                                       '$y$-value $(5, -3)$ lies in **Quadrant '
                                                       'IV**. Choice A represents Quadrant I ($x > '
                                                       '0, y > 0$). Choice B represents Quadrant '
                                                       'II ($x < 0, y > 0$). Choice C represents '
                                                       'Quadrant III ($x < 0, y < 0$).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-9',
                                        'q': 'Rectangle $PQRS$ has side lengths $PQ = 8\\text{ '
                                             'cm}$ and $QR = 5\\text{ cm}$, with $m\\angle P = '
                                             '90^\\circ$. If $PQRS$ is translated $12\\text{ units '
                                             'left}$ and $15\\text{ units down}$ to form rectangle '
                                             "$P'Q'R'S'$, which statement is **NOT** true?",
                                        'opts': [   "The perimeter of $P'Q'R'S'$ is greater than "
                                                    'the perimeter of $PQRS$ because the figure '
                                                    'was translated by a large distance.',
                                                    "The length of segment $P'Q'$ is equal to "
                                                    '$8\\text{ cm}$.',
                                                    "$m\\angle P' = 90^\\circ$.",
                                                    "Segment $P'Q'$ is parallel to segment $PQ$."],
                                        'correct': 0,
                                        'hint': 'A translation is a rigid motion (isometry). Does '
                                                'sliding a shape across a flat plane change its '
                                                'perimeter or dimensions?',
                                        'explanation': 'Translations are rigid motions that '
                                                       'preserve side lengths, angle measures, '
                                                       'perimeter, area, and parallelism. Sliding '
                                                       'a figure never stretches or shrinks it, so '
                                                       'the perimeter remains exactly $2(8 + 5) = '
                                                       '26\\text{ cm}$. Therefore, statement A is '
                                                       'false (making it the correct answer to the '
                                                       'question). Choices B, C, and D are all '
                                                       'fundamental invariant properties preserved '
                                                       'under translation.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-10',
                                        'q': 'On a coordinate grid, line segment $\\overline{AB}$ '
                                             'connects $A(1, 2)$ to $B(4, 8)$, giving it a slope '
                                             'of $m = \\frac{8 - 2}{4 - 1} = 2$. Segment '
                                             '$\\overline{AB}$ is translated by $(x, y) \\to (x - '
                                             '5, y + 3)$ to create image segment '
                                             "$\\overline{A'B'}$. What is the slope of "
                                             "$\\overline{A'B'}$?",
                                        'opts': [   '$-2$',
                                                    '$\\frac{1}{2}$',
                                                    '$2$',
                                                    '$-\\frac{3}{5}$'],
                                        'correct': 2,
                                        'hint': 'Under a translation, line segments map to '
                                                'parallel line segments. What do you know about '
                                                'the slopes of parallel lines?',
                                        'explanation': 'Translations preserve the orientation and '
                                                       'steepness of lines; every translated '
                                                       'segment is parallel to its preimage '
                                                       'segment. Since parallel lines have '
                                                       'identical slopes, the slope of '
                                                       "$\\overline{A'B'}$ is equal to the slope "
                                                       'of $\\overline{AB}$, which is $2$. '
                                                       "Calculating directly: $A'(-4, 5)$ and "
                                                       "$B'(-1, 11)$; slope $= \\frac{11 - 5}{-1 - "
                                                       '(-4)} = \\frac{6}{3} = 2$. Choice A is the '
                                                       'negative slope. Choice B is the reciprocal '
                                                       'slope. Choice D confuses the slope with '
                                                       'the ratio of translation vector '
                                                       'components.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-11',
                                        'q': 'A polygon is translated on a coordinate grid '
                                             'according to the vector $\\langle 6, -8 \\rangle$. '
                                             'What is the straight-line distance that each vertex '
                                             'of the polygon travels during this translation?',
                                        'opts': [   '$14\\text{ units}$',
                                                    '$10\\text{ units}$',
                                                    '$2\\text{ units}$',
                                                    '$\\sqrt{28}\\text{ units}$'],
                                        'correct': 1,
                                        'hint': 'Use the Pythagorean theorem $d = \\sqrt{a^2 + '
                                                'b^2}$ to find the length (magnitude) of the '
                                                'translation vector.',
                                        'explanation': 'The straight-line Euclidean distance '
                                                       'traveled by any point under vector '
                                                       '$\\langle a, b \\rangle$ is given by $d = '
                                                       '\\sqrt{a^2 + b^2}$. Here, $d = \\sqrt{6^2 '
                                                       '+ (-8)^2} = \\sqrt{36 + 64} = \\sqrt{100} '
                                                       '= 10\\text{ units}$. Choice A simply adds '
                                                       'the absolute shifts $6 + 8 = 14$ (taxicab '
                                                       'distance, not straight-line distance). '
                                                       'Choice C subtracts the components ($8 - 6 '
                                                       '= 2$). Choice D subtracts the squares '
                                                       '($\\sqrt{64 - 36} = \\sqrt{28}$).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-12',
                                        'q': 'Triangle $XYZ$ is translated along vector $\\langle '
                                             "-5, 12 \\rangle$ to form Triangle $X'Y'Z'$. Vertex "
                                             '$X$ travels a straight-line distance of $13\\text{ '
                                             "units}$ to $X'$. How far does vertex $Z$ travel to "
                                             "reach its image $Z'$?",
                                        'opts': [   'Exactly $13\\text{ units}$',
                                                    'More than $13\\text{ units}$ if $Z$ is '
                                                    'farther from the origin than $X$',
                                                    'Less than $13\\text{ units}$ because $Z$ is '
                                                    'at the opposite end of the triangle',
                                                    'It cannot be determined without knowing the '
                                                    'exact initial coordinates of $Z$'],
                                        'correct': 0,
                                        'hint': 'By definition, does a translation move every '
                                                'point by the same distance, or do different '
                                                'points travel different distances?',
                                        'explanation': 'By definition, a translation slides EVERY '
                                                       'point of a figure by the exact same '
                                                       'distance and in the exact same direction '
                                                       'along parallel paths. Because the vector '
                                                       'is $\\langle -5, 12 \\rangle$, every point '
                                                       'in the triangle travels $d = \\sqrt{(-5)^2 '
                                                       '+ 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = '
                                                       '13\\text{ units}$. Choices B, C, and D are '
                                                       'misconceptions; distance traveled during a '
                                                       'translation is constant across all points '
                                                       'and does not depend on position relative '
                                                       'to the origin.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-13',
                                        'q': 'A geometric figure is first translated by $T_1: (x, '
                                             'y) \\to (x + 4, y - 3)$, and then its image is '
                                             'translated by $T_2: (x, y) \\to (x - 9, y + 8)$. '
                                             'Which single algebraic rule represents the '
                                             'composition of these two successive translations?',
                                        'opts': [   '$(x, y) \\to (x + 13, y - 11)$',
                                                    '$(x, y) \\to (x + 5, y - 5)$',
                                                    '$(x, y) \\to (x - 5, y + 5)$',
                                                    '$(x, y) \\to (x - 36, y - 24)$'],
                                        'correct': 2,
                                        'hint': 'Add the corresponding horizontal displacements '
                                                'together ($a_1 + a_2$) and the vertical '
                                                'displacements together ($b_1 + b_2$).',
                                        'explanation': 'To combine successive translations, sum '
                                                       'their respective components: '
                                                       '$a_{\\text{net}} = 4 + (-9) = -5$, and '
                                                       '$b_{\\text{net}} = -3 + 8 = 5$. Thus, the '
                                                       'single equivalent mapping rule is $(x, y) '
                                                       '\\to (x - 5, y + 5)$. Choice A subtracts '
                                                       'the shifts ($4 - (-9) = 13, -3 - 8 = '
                                                       '-11$). Choice B reverses the signs of the '
                                                       'net shifts. Choice D multiplies the '
                                                       'shifts.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-14',
                                        'q': 'In HMH Into Math Lesson 1.2 *Turn and Talk*, '
                                             'students explore moving a chess piece $1\\text{ '
                                             'space right and } 2\\text{ spaces up}$ versus moving '
                                             'it $2\\text{ spaces up and } 1\\text{ space right}$. '
                                             'What mathematical property explains why both '
                                             'sequences result in the exact same final position?',
                                        'opts': [   'The distributive property of multiplication '
                                                    'over addition',
                                                    'The commutative property of addition for real '
                                                    'numbers ($x + a_1 + a_2 = x + a_2 + a_1$)',
                                                    'The reflexive property of geometric '
                                                    'congruence',
                                                    'The inverse property of coordinate '
                                                    'reflections'],
                                        'correct': 1,
                                        'hint': 'Translations are represented by adding constants '
                                                'to coordinate values. Does the order in which you '
                                                'add two real numbers change their sum?',
                                        'explanation': 'Translations modify coordinates by adding '
                                                       'constants: $x \\to x + a_1 + a_2$ and $y '
                                                       '\\to y + b_1 + b_2$. Because addition of '
                                                       'real numbers is commutative ($a_1 + a_2 = '
                                                       'a_2 + a_1$ and $b_1 + b_2 = b_2 + b_1$), '
                                                       'changing the sequence of the translations '
                                                       'results in the identical final '
                                                       'coordinates. Translations commute with '
                                                       'each other. Choices A, C, and D cite '
                                                       'unrelated properties.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-15',
                                        'q': 'An agricultural inspection drone hovers over a crop '
                                             'field at coordinate $(15, 28)$, where coordinates '
                                             'are measured in meters. The flight computer executes '
                                             'a translation along vector $\\langle -32, -45 '
                                             '\\rangle$ to inspect an irrigation valve. What are '
                                             'the new coordinates of the drone?',
                                        'opts': [   '$(-17, -17)$',
                                                    '$(47, 73)$',
                                                    '$(-17, 73)$',
                                                    '$(47, -17)$'],
                                        'correct': 0,
                                        'hint': "Add the vector components directly to the drone's "
                                                "initial coordinates: $x' = 15 + (-32)$ and $y' = "
                                                '28 + (-45)$.',
                                        'explanation': 'Applying the translation vector $\\langle '
                                                       "-32, -45 \\rangle$: $x' = 15 + (-32) = "
                                                       "-17\\text{ m}$, and $y' = 28 + (-45) = "
                                                       "-17\\text{ m}$. Thus, the drone's new "
                                                       'position is $(-17, -17)$. Choice B '
                                                       'incorrectly subtracts negative values ($15 '
                                                       '- (-32) = 47, 28 - (-45) = 73$). Choice C '
                                                       'computes $x$ correctly but adds for $y$. '
                                                       'Choice D adds for $x$ but subtracts for '
                                                       '$y$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-16',
                                        'q': 'On a chessboard modeled as a coordinate grid (HMH TE '
                                             'p. 38), a knight begins at position $(3, 2)$. A '
                                             'player makes two consecutive legal moves: first '
                                             'sliding 1 unit right and 2 units up, and then '
                                             'sliding 2 units left and 1 unit up. What is the '
                                             "knight's final coordinate position?",
                                        'opts': ['$(4, 4)$', '$(0, 5)$', '$(2, 3)$', '$(2, 5)$'],
                                        'correct': 3,
                                        'hint': 'Calculate the intermediate position after the '
                                                'first move, then apply the second move to that '
                                                'result.',
                                        'explanation': 'Move 1 (1 right, 2 up): $(x, y) \\to (x + '
                                                       '1, y + 2)$, landing the knight at $(3 + 1, '
                                                       '2 + 2) = (4, 4)$. Move 2 (2 left, 1 up): '
                                                       '$(x, y) \\to (x - 2, y + 1)$, moving the '
                                                       'knight from $(4, 4)$ to $(4 - 2, 4 + 1) = '
                                                       '(2, 5)$. Choice A is the intermediate '
                                                       'coordinate after only move 1. Choice B '
                                                       'subtracts 2 from the initial $x$ without '
                                                       'adding 1. Choice C subtracts 1 from $y$ on '
                                                       'the second move instead of adding 1.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-17',
                                        'q': 'An architect places Building $A$ on a city planning '
                                             'grid with vertices at $(1, 1)$, $(3, 1)$, $(3, 3)$, '
                                             'and $(1, 3)$ (a $2 \\times 2$ square; HMH TE p. '
                                             '42-43). A developer proposes four new building '
                                             'footprints. Which proposal represents a **valid '
                                             'translation** of Building $A$?',
                                        'opts': [   "Building $B'$ with vertices at $(1, 1)$, $(4, "
                                                    '1)$, $(4, 4)$, and $(1, 4)$',
                                                    "Building $C'$ with vertices at $(-1, 1)$, "
                                                    '$(-3, 1)$, $(-3, 3)$, and $(-1, 3)$',
                                                    "Building $A'$ with vertices at $(5, -4)$, "
                                                    '$(7, -4)$, $(7, -2)$, and $(5, -2)$',
                                                    "Building $D'$ with vertices at $(2, 2)$, $(6, "
                                                    '2)$, $(6, 6)$, and $(2, 6)$'],
                                        'correct': 2,
                                        'hint': 'In a true translation, every vertex shifts by the '
                                                'exact same $a$ and $b$, and the dimensions ($2 '
                                                '\\times 2$) and orientation remain unchanged.',
                                        'explanation': "In Building $A'$, every single vertex is "
                                                       'shifted by the identical rule $(x, y) \\to '
                                                       '(x + 4, y - 5)$: $(1+4, 1-5)=(5, -4)$, '
                                                       '$(3+4, 1-5)=(7, -4)$, $(3+4, 3-5)=(7, '
                                                       '-2)$, and $(1+4, 3-5)=(5, -2)$. The size '
                                                       '($2 \\times 2$) and orientation are '
                                                       'perfectly preserved. Choice A has '
                                                       'dimensions $3 \\times 3$ (dilation). '
                                                       'Choice B has vertices with opposite '
                                                       '$x$-coordinates, representing a reflection '
                                                       'across the $y$-axis. Choice D has '
                                                       'dimensions $4 \\times 4$ (dilation by '
                                                       'factor 2).',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-18',
                                        'q': 'Parallelogram $ABCD$ is translated on a coordinate '
                                             "plane. Vertex $A(-2, 3)$ maps to $A'(4, -1)$. If "
                                             'vertex $C$ is located at $(1, -4)$, what are the '
                                             "coordinates of image vertex $C'$?",
                                        'opts': [   '$(-5, 0)$',
                                                    '$(7, -8)$',
                                                    '$(7, 0)$',
                                                    '$(-5, -8)$'],
                                        'correct': 1,
                                        'hint': "Find the translation vector from $A$ to $A'$: $a "
                                                '= 4 - (-2)$ and $b = -1 - 3$. Then apply this '
                                                'exact same vector to vertex $C$.',
                                        'explanation': 'Determine the translation rule from $A(-2, '
                                                       "3) \\to A'(4, -1)$: $a = 4 - (-2) = 6$ and "
                                                       '$b = -1 - 3 = -4$. The rule is $(x, y) '
                                                       '\\to (x + 6, y - 4)$. Because translations '
                                                       'shift all vertices equally, apply this '
                                                       "rule to $C(1, -4)$: $x' = 1 + 6 = 7$, and "
                                                       "$y' = -4 - 4 = -8$. Therefore, $C' = (7, "
                                                       '-8)$. Choice A applies the inverse rule '
                                                       '($1 - 6 = -5, -4 + 4 = 0$). Choice C adds '
                                                       '4 to $y$ instead of subtracting 4. Choice '
                                                       'D subtracts 6 from $x$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-19',
                                        'q': 'In HMH Into Math Lesson 1.2 Task 1D, students are '
                                             'asked: *“What translation must be performed on the '
                                             'image so that it returns to the exact location of '
                                             'the preimage?”* If a figure was translated by $(x, '
                                             'y) \\to (x - 7, y + 4)$, which rule will return the '
                                             'image back to its original preimage?',
                                        'opts': [   '$(x, y) \\to (x - 7, y + 4)$',
                                                    '$(x, y) \\to (x + 7, y + 4)$',
                                                    '$(x, y) \\to (x - 4, y + 7)$',
                                                    '$(x, y) \\to (x + 7, y - 4)$'],
                                        'correct': 3,
                                        'hint': 'The inverse translation reverses both directions: '
                                                'the opposite of moving left 7 is moving right 7, '
                                                'and the opposite of moving up 4 is moving down 4.',
                                        'explanation': 'To undo a translation and return an image '
                                                       'to its starting position, apply the '
                                                       'inverse translation by negating both '
                                                       'displacements. The opposite of shifting 7 '
                                                       'units left ($-7$) is shifting 7 units '
                                                       'right ($+7$), and the opposite of shifting '
                                                       '4 units up ($+4$) is shifting 4 units down '
                                                       '($-4$). Thus, the returning rule is $(x, '
                                                       'y) \\to (x + 7, y - 4)$. Choice A repeats '
                                                       'the forward translation. Choice B fails to '
                                                       'reverse the vertical shift. Choice C swaps '
                                                       'the horizontal and vertical numbers.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-2-mcq-20',
                                        'q': 'A homeowner wants to slide a rectangular sofa from '
                                             'the center of a living room flush against a wall '
                                             '(HMH TE p. 39 DOK 3). The sofa has dimensions '
                                             '$84\\text{ inches long}$ by $36\\text{ inches '
                                             'deep}$. The available wall space between two '
                                             'doorways measures $90\\text{ inches wide}$. Why does '
                                             'the homeowner know with mathematical certainty that '
                                             'the sofa will fit against the wall after being '
                                             'pushed along a straight-line path without rotating?',
                                        'opts': [   'Because sliding a shape across a floor '
                                                    'slightly compresses its length along the '
                                                    'direction of motion.',
                                                    'Because translations alter the angle measures '
                                                    'of a quadrilateral to adapt to boundary '
                                                    'constraints.',
                                                    'Because translations preserve side lengths, '
                                                    "angle measures, and parallelism, the sofa's "
                                                    'dimensions remain exactly $84\\text{ in.} '
                                                    '\\times 36\\text{ in.}$, which is less than '
                                                    'the $90\\text{ in.}$ space.',
                                                    "Because the translation vector's magnitude "
                                                    'reduces the perimeter of any translated '
                                                    'object by a factor of $\\sqrt{a^2 + b^2}$.'],
                                        'correct': 2,
                                        'hint': 'Translations are rigid motions. What happens to '
                                                'the side lengths, perimeter, and rectangular '
                                                'angles of an object when it slides?',
                                        'explanation': 'Translations are rigid motions '
                                                       '(isometries) that preserve side lengths, '
                                                       'angle measures, collinearity, perimeter, '
                                                       'and area. Because the sofa does not '
                                                       'rotate, stretch, compress, or deform '
                                                       'during the translation, its length remains '
                                                       'exactly 84 inches. Since $84\\text{ in.} < '
                                                       '90\\text{ in.}$, the sofa is guaranteed to '
                                                       'fit flush against the wall. Choice A '
                                                       'falsely assumes physical deformation '
                                                       'occurs during a geometric translation. '
                                                       'Choices B and D contradict the fundamental '
                                                       'property that translations preserve all '
                                                       'angles, side lengths, and perimeter.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'}],
                        'fitb': [   {   'id': 'p-1-2-f1',
                                        'q': 'Point K(3, -2) is translated by (x, y) → (x - 4, y + '
                                             "6). Enter the image coordinates K' in the format (x, "
                                             'y):',
                                        'expected': '(-1, 4)',
                                        'altExpected': ['(-1,4)', '-1, 4', '-1,4'],
                                        'hint': 'Calculate 3 - 4 for x, and -2 + 6 for y.'},
                                    {   'id': 'p-1-2-f2',
                                        'q': 'If an image point is at (5, 8) under the rule (x, y) '
                                             '→ (x + 3, y - 2), what was the original x-coordinate '
                                             'of the preimage?',
                                        'expected': '2',
                                        'hint': 'Work backwards: x + 3 = 5, so x = 5 - 3.'}]},
        'bookQuestions': [   {   'num': 'HMH Into Math • Section 1.2 Exercise 7',
                                 'q': 'A graphic designer moves a digital logo from \\(A(-5, 3)\\) '
                                      "to \\(A'(2, -1)\\). (a) Write the translation rule. (b) If "
                                      'another vertex on the logo was at \\(B(-1, -4)\\), what are '
                                      "the coordinates of \\(B'\\)?",
                                 'modelAnswer': '<strong>Model Answer:</strong><br>(a) Horizontal '
                                                'shift: \\(a = 2 - (-5) = 7\\). Vertical shift: '
                                                '\\(b = -1 - 3 = -4\\). Rule: \\((x, y) \\to (x + '
                                                '7, y - 4)\\).<br>(b) Substitute \\(B(-1, -4)\\): '
                                                "\\(B'(-1 + 7, -4 - 4) = B'(6, -8)\\)."},
                             {   'num': 'HMH Into Math • Section 1.2 Exercise 12',
                                 'q': 'Explain why line segments connecting corresponding points '
                                      'of a preimage and image under a translation are always '
                                      'parallel and equal in length.',
                                 'modelAnswer': '<strong>Model Answer:</strong> In a translation, '
                                                'every single point moves along the exact same '
                                                'vector \\(\\langle a, b \\rangle\\). Since all '
                                                'points travel in the identical direction, the '
                                                "line segments connecting each \\(P\\) to \\(P'\\) "
                                                'have the same slope \\(\\frac{b}{a}\\) (making '
                                                'them parallel) and the same distance '
                                                '\\(\\sqrt{a^2 + b^2}\\) (making them equal in '
                                                'length).'}]},
    {   'id': '1.3',
        'modId': 'mod1',
        'modNum': 1,
        'modTitle': 'Transformations and Congruence',
        'themeColor': '#4f46e5',
        'badge': 'Module 1 • Lesson 1.3',
        'num': '1.3',
        'title': 'Explore Reflections',
        'tag': 'Lines of Symmetry & Orientation',
        'standard': 'CCSS.MATH.CONTENT.8.G.A.1.b, 8.G.A.3',
        'canDo': 'I can graph reflections across the x-axis, y-axis, and lines of symmetry, apply '
                 'algebraic rules, and explain why reflections reverse vertex orientation.',
        'conceptIntro': 'A <strong>reflection</strong> is a rigid motion that flips a figure '
                        'across a specific line called the <strong>line of reflection</strong>. '
                        'Each point and its image are the exact same distance from the line of '
                        'reflection, and the segment connecting them is perpendicular to that '
                        'line. The line of reflection acts as the <strong>perpendicular '
                        'bisector</strong> of every segment connecting a preimage point to its '
                        'image point.',
        'rules': [   {   'name': 'Across the x-axis',
                         'formula': '(x, y) \\to (x, -y)',
                         'desc': 'x stays the same; y changes sign (negates).'},
                     {   'name': 'Across the y-axis',
                         'formula': '(x, y) \\to (-x, y)',
                         'desc': 'x changes sign (negates); y stays the same.'},
                     {   'name': 'Across the line y = x',
                         'formula': '(x, y) \\to (y, x)',
                         'desc': 'Swap the x and y coordinates.'},
                     {   'name': 'Across vertical line x = k',
                         'formula': '(x, y) \\to (2k - x, y)',
                         'desc': 'Horizontal flip across vertical line x = k.'}],
        'vocab': [   {   'term': 'Reflection',
                         'def': 'A transformation that flips a figure across a line creating a '
                                'mirror image.',
                         'ex': 'Looking in a mirror or flipping over the x-axis.'},
                     {   'term': 'Line of Reflection',
                         'def': 'The line across which a figure is reflected. It is the '
                                'perpendicular bisector of every segment connecting corresponding '
                                'points.',
                         'ex': 'The x-axis (y = 0) or the line y = x.'},
                     {   'term': 'Reversed Orientation',
                         'def': 'The reversal of vertex order from clockwise to counterclockwise.',
                         'ex': 'Clockwise \\(\\triangle ABC\\) becomes counterclockwise '
                               "\\(\\triangle A'B'C'\\)."}],
        'invariance': [   {   'prop': 'Side Lengths & Angles',
                              'status': '✓ Preserved (Congruent)',
                              'cls': 'yes'},
                          {'prop': 'Parallelism of Lines', 'status': '✓ Preserved', 'cls': 'yes'},
                          {'prop': 'Perimeter & Area', 'status': '✓ Preserved', 'cls': 'yes'},
                          {   'prop': 'Vertex Orientation',
                              'status': '✕ Reversed (Mirror flip)',
                              'cls': 'no'}],
        'illustrativeExamples': [   {   'title': 'Example 1: Reflecting Across the x-axis',
                                        'desc': 'Find the image of \\(A(3, 5)\\) when reflected '
                                                'across the x-axis.',
                                        'analysis': 'Rule: \\((x, y) \\to (x, -y)\\). The '
                                                    'x-coordinate remains 3, while the '
                                                    "y-coordinate negates to -5. So, \\(A' = (3, "
                                                    '-5)\\).'},
                                    {   'title': 'Example 2: Reflecting Across the y-axis',
                                        'desc': 'Find the image of \\(B(-6, -2)\\) when reflected '
                                                'across the y-axis.',
                                        'analysis': 'Rule: \\((x, y) \\to (-x, y)\\). The '
                                                    'x-coordinate negates: \\(-(-6) = 6\\), and y '
                                                    "stays -2. So, \\(B' = (6, -2)\\)."}],
        'workedExample': {   'title': 'Worked Example: Reflecting a Triangle Across y-axis & Line '
                                      'y = x',
                             'problem': 'Triangle \\(JKL\\) has vertices \\(J(2, 4)\\), \\(K(5, '
                                        '1)\\), and \\(L(2, 1)\\). (a) Find the coordinates of '
                                        "\\(\\triangle J'K'L'\\) after reflection across the "
                                        'y-axis. (b) Find the coordinates of \\(\\triangle '
                                        "J''K''L''\\) after reflecting original \\(\\triangle "
                                        'JKL\\) across the line \\(y = x\\). (c) State the '
                                        'orientation of the images compared to the preimage.',
                             'step1': '<strong>Step 1: Reflect across y-axis using \\((x, y) \\to '
                                      "(-x, y)\\):</strong><br>• \\(J(2, 4) \\to J'(-2, 4)\\)<br>• "
                                      "\\(K(5, 1) \\to K'(-5, 1)\\)<br>• \\(L(2, 1) \\to L'(-2, "
                                      '1)\\).',
                             'step2': '<strong>Step 2: Reflect across \\(y = x\\) using \\((x, y) '
                                      "\\to (y, x)\\):</strong><br>• \\(J(2, 4) \\to J''(4, "
                                      "2)\\)<br>• \\(K(5, 1) \\to K''(1, 5)\\)<br>• \\(L(2, 1) "
                                      "\\to L''(1, 2)\\).",
                             'step3': '<strong>Step 3: Analyze orientation:</strong> In both '
                                      'cases, the reflection flips the figure across the mirror '
                                      'line, so the orientation reverses from clockwise to '
                                      'counterclockwise.',
                             'modelAnswer': '<strong>Student Model Answer:</strong> Reflection '
                                            "across y-axis gives \\(J'(-2, 4)\\), \\(K'(-5, 1)\\), "
                                            "\\(L'(-2, 1)\\). Reflection across \\(y = x\\) gives "
                                            "\\(J''(4, 2)\\), \\(K''(1, 5)\\), \\(L''(1, 2)\\). In "
                                            'both reflections, vertex orientation is reversed '
                                            'while side lengths and angle measures are preserved.'},
        'practice': {   'mcqs': [   {   'id': 'p-1-3-mcq-1',
                                        'q': 'Point $A(-4, 7)$ is reflected across the $x$-axis. '
                                             "What are the coordinates of the image point $A'$?",
                                        'opts': [   '$(-4, -7)$',
                                                    '$(4, 7)$',
                                                    '$(4, -7)$',
                                                    '$(7, -4)$'],
                                        'correct': 0,
                                        'hint': 'Reflecting across the $x$-axis preserves the '
                                                'horizontal position ($x$) and inverts the '
                                                'vertical position ($y$): $(x, y) \\to (x, -y)$.',
                                        'explanation': 'Option A is correct. The coordinate rule '
                                                       'for reflection across the $x$-axis is $(x, '
                                                       'y) \\to (x, -y)$. The $x$-coordinate '
                                                       'remains $-4$, while the $y$-coordinate is '
                                                       "negated from $7$ to $-7$, giving $A'(-4, "
                                                       '-7)$. Option B $(4, 7)$ negates the '
                                                       '$x$-coordinate instead (reflection across '
                                                       'the $y$-axis). Option C $(4, -7)$ negates '
                                                       'both coordinates (equivalent to a '
                                                       '$180^\\circ$ rotation about the origin). '
                                                       'Option D $(7, -4)$ swaps the coordinates '
                                                       '(reflection across the diagonal line $y = '
                                                       'x$).',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-2',
                                        'q': 'Triangle $\\triangle JKL$ with vertex $K(5, -8)$ is '
                                             'reflected across the $y$-axis to produce $\\triangle '
                                             "J'K'L'$. Which coordinate pair represents the "
                                             "location of $K'$?",
                                        'opts': [   '$(5, 8)$',
                                                    '$(-5, -8)$',
                                                    '$(-5, 8)$',
                                                    '$(-8, 5)$'],
                                        'correct': 1,
                                        'hint': 'Reflecting across the $y$-axis keeps the vertical '
                                                'height ($y$) identical and reflects the '
                                                'horizontal position ($x$): $(x, y) \\to (-x, y)$.',
                                        'explanation': 'Option B is correct. Under a reflection '
                                                       'across the $y$-axis, the algebraic mapping '
                                                       'rule is $(x, y) \\to (-x, y)$. The '
                                                       '$x$-coordinate $5$ becomes $-5$, while the '
                                                       '$y$-coordinate remains $-8$. Therefore, '
                                                       "$K'(-5, -8)$. Option A $(5, 8)$ reflects "
                                                       'across the $x$-axis by negating $y$. '
                                                       'Option C $(-5, 8)$ negates both '
                                                       'coordinates, which is a $180^\\circ$ '
                                                       'rotation. Option D $(-8, 5)$ incorrectly '
                                                       'interchanges the $x$- and $y$-coordinates.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-3',
                                        'q': 'A polygon vertex located at $P(-3, 8)$ is reflected '
                                             'across the diagonal line $y = x$. What are the '
                                             "coordinates of the reflected image $P'$?",
                                        'opts': [   '$(3, -8)$',
                                                    '$(-8, 3)$',
                                                    '$(8, -3)$',
                                                    '$(-3, -8)$'],
                                        'correct': 2,
                                        'hint': 'On the line $y = x$, every point has equal '
                                                'coordinates. Reflecting across this line simply '
                                                'interchanges the roles of $x$ and $y$: $(x, y) '
                                                '\\to (y, x)$.',
                                        'explanation': 'Option C is correct. The algebraic mapping '
                                                       'rule for reflection across the line $y = '
                                                       'x$ is $(x, y) \\to (y, x)$. The '
                                                       'coordinates swap positions without '
                                                       'altering their signs: the new $x$-value is '
                                                       'the old $y$-value ($8$), and the new '
                                                       '$y$-value is the old $x$-value ($-3$). '
                                                       "Thus, $P' = (8, -3)$. Option A $(3, -8)$ "
                                                       'negates both coordinates without swapping. '
                                                       'Option B $(-8, 3)$ swaps and negates both '
                                                       'coordinates, which is the rule for '
                                                       'reflecting across $y = -x$. Option D $(-3, '
                                                       '-8)$ reflects across the $x$-axis.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-4',
                                        'q': 'Line segment $\\overline{CD}$ has endpoint $D(4, '
                                             '-6)$. If $\\overline{CD}$ is reflected across the '
                                             'diagonal line $y = -x$, which coordinates identify '
                                             "$D'$?",
                                        'opts': ['$(-6, 4)$', '$(-4, 6)$', '$(4, 6)$', '$(6, -4)$'],
                                        'correct': 3,
                                        'hint': 'Reflecting across the line $y = -x$ requires both '
                                                'swapping the coordinates and changing their '
                                                'signs: $(x, y) \\to (-y, -x)$.',
                                        'explanation': 'Option D is correct. The coordinate rule '
                                                       'for a reflection across the line $y = -x$ '
                                                       'is $(x, y) \\to (-y, -x)$. Starting with '
                                                       '$D(4, -6)$: the new $x$-coordinate is $-y '
                                                       '= -(-6) = 6$, and the new $y$-coordinate '
                                                       "is $-x = -(4) = -4$. Hence, $D' = (6, "
                                                       '-4)$. Option A $(-6, 4)$ swapped '
                                                       'coordinates without changing signs '
                                                       '(reflection across $y = x$). Option B '
                                                       '$(-4, 6)$ negated both coordinates without '
                                                       'swapping (a $180^\\circ$ rotation). Option '
                                                       'C $(4, 6)$ negated only the $y$-coordinate '
                                                       '(reflection across the $x$-axis).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-5',
                                        'q': 'Point $M(1, 5)$ is reflected across the vertical '
                                             'line $x = 4$. What are the coordinates of the '
                                             "reflected image $M'$?",
                                        'opts': ['$(7, 5)$', '$(-2, 5)$', '$(4, 5)$', '$(7, -5)$'],
                                        'correct': 0,
                                        'hint': 'The line $x = 4$ is vertical, so the '
                                                '$y$-coordinate does not change. Find how far $1$ '
                                                'is from $4$, and move that same distance to the '
                                                'other side of $4$.',
                                        'explanation': 'Option A is correct. In a reflection '
                                                       'across a vertical line $x = c$, the '
                                                       "$y$-coordinate remains invariant ($y' = "
                                                       '5$). The horizontal distance from $M(1, '
                                                       '5)$ to $x = 4$ is $4 - 1 = 3$ units to the '
                                                       "left. The reflected image $M'$ must be $3$ "
                                                       "units to the right of $x = 4$: $x' = 4 + 3 "
                                                       '= 7$. Alternatively, using the algebraic '
                                                       "formula: $x' = 2c - x = 2(4) - 1 = 7$. "
                                                       "Thus, $M' = (7, 5)$. Option B $(-2, 5)$ "
                                                       'incorrectly subtracted $3$ from $1$ '
                                                       'instead of adding to $4$. Option C $(4, '
                                                       '5)$ is the midpoint on the line of '
                                                       'reflection itself. Option D $(7, -5)$ '
                                                       'incorrectly negated the $y$-coordinate.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-6',
                                        'q': 'Vertex $V(-3, -2)$ is reflected across the '
                                             'horizontal line $y = 3$. What are the coordinates of '
                                             "the reflected image $V'$?",
                                        'opts': [   '$(-3, 5)$',
                                                    '$(-3, 1)$',
                                                    '$(3, -2)$',
                                                    '$(-3, 8)$'],
                                        'correct': 3,
                                        'hint': 'A reflection across a horizontal line keeps the '
                                                '$x$-coordinate constant. Calculate the vertical '
                                                'distance from $-2$ to $3$, then add that distance '
                                                'above $y = 3$.',
                                        'explanation': 'Option D is correct. Across the horizontal '
                                                       'line $y = c$, the $x$-coordinate is '
                                                       "unaffected ($x' = -3$). The vertical "
                                                       'distance from $V(-3, -2)$ to the mirror '
                                                       'line $y = 3$ is $3 - (-2) = 5$ units. The '
                                                       "image $V'$ must lie $5$ units above the "
                                                       "mirror line: $y' = 3 + 5 = 8$. Using the "
                                                       "formula: $y' = 2c - y = 2(3) - (-2) = 6 + "
                                                       "2 = 8$. Thus, $V' = (-3, 8)$. Option A "
                                                       '$(-3, 5)$ merely added the distance $5$ to '
                                                       '$0$ or forgot to double the offset. Option '
                                                       'B $(-3, 1)$ added $3$ to $-2$ instead of '
                                                       'reflecting across $y = 3$. Option C $(3, '
                                                       '-2)$ reflected horizontally across the '
                                                       '$y$-axis.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-7',
                                        'q': 'Point $P(2, 6)$ is reflected across line $\\ell$ to '
                                             "produce $P'(8, 6)$. Which mathematical statement "
                                             'accurately describes line $\\ell$ and its geometric '
                                             "relationship to segment $\\overline{PP'}$?",
                                        'opts': [   'Line $\\ell$ has equation $y = 6$ and is '
                                                    "parallel to segment $\\overline{PP'}$.",
                                                    'Line $\\ell$ has equation $x = 5$ and is the '
                                                    'perpendicular bisector of segment '
                                                    "$\\overline{PP'}$.",
                                                    'Line $\\ell$ has equation $x = 6$ and '
                                                    "intersects $\\overline{PP'}$ at a $45^\\circ$ "
                                                    'angle.',
                                                    'Line $\\ell$ has equation $y = 5$ and bisects '
                                                    "$\\overline{PP'}$ obliquely."],
                                        'correct': 1,
                                        'hint': 'Recall the fundamental geometric definition: The '
                                                'line of reflection is always the perpendicular '
                                                'bisector of every segment connecting a preimage '
                                                'point to its image point.',
                                        'explanation': 'Option B is correct. Segment '
                                                       "$\\overline{PP'}$ connects $(2, 6)$ and "
                                                       '$(8, 6)$, which is a horizontal segment on '
                                                       'the line $y = 6$ of length $|8 - 2| = 6$ '
                                                       "units. The midpoint of $\\overline{PP'}$ "
                                                       'is $\\left(\\frac{2+8}{2}, '
                                                       '\\frac{6+6}{2}\\right) = (5, 6)$. The line '
                                                       'of reflection must pass through this '
                                                       'midpoint and be perpendicular to the '
                                                       'horizontal segment. A line perpendicular '
                                                       'to a horizontal line is vertical, giving '
                                                       'the equation $x = 5$. Option A ($y = 6$) '
                                                       'is the line containing the segment itself, '
                                                       'not its perpendicular bisector. Option C '
                                                       '($x = 6$) does not pass through the '
                                                       'midpoint. Option D ($y = 5$) is horizontal '
                                                       'and cannot be perpendicular to another '
                                                       'horizontal segment.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-8',
                                        'q': 'Triangle $\\triangle ABC$ has vertices listed in '
                                             'clockwise order: $A(1, 2)$, $B(4, 2)$, and $C(1, '
                                             '6)$. After reflecting $\\triangle ABC$ across the '
                                             "$y$-axis to form $\\triangle A'B'C'$, which "
                                             'statement regarding the congruence and vertex '
                                             "orientation of $\\triangle A'B'C'$ is true?",
                                        'opts': [   "$\\triangle A'B'C' \\cong \\triangle ABC$, "
                                                    "and its vertices $A' \\to B' \\to C'$ remain "
                                                    'in clockwise order.',
                                                    "$\\triangle A'B'C'$ is not congruent to "
                                                    '$\\triangle ABC$ because reflections distort '
                                                    'vertex order.',
                                                    "$\\triangle A'B'C' \\cong \\triangle ABC$, "
                                                    "but its vertices $A' \\to B' \\to C'$ are now "
                                                    'ordered counterclockwise (orientation is '
                                                    'reversed).',
                                                    'The vertex orientation is unchanged because '
                                                    'all rigid motions preserve clockwise order.'],
                                        'correct': 2,
                                        'hint': 'Reflections are rigid motions (isometries) that '
                                                'preserve side lengths and angles, but they flip '
                                                'the plane like looking into a mirror, reversing '
                                                'chirality.',
                                        'explanation': 'Option C is correct. Because reflection is '
                                                       'a rigid motion (isometry), side lengths '
                                                       'and angle measures are strictly preserved, '
                                                       "guaranteeing that $\\triangle A'B'C' "
                                                       '\\cong \\triangle ABC$. However, '
                                                       'reflections are opposite isometries '
                                                       '(chirality-reversing): tracing $A(1,2) '
                                                       '\\to B(4,2) \\to C(1,6)$ runs clockwise, '
                                                       "but tracing their reflections $A'(-1,2) "
                                                       "\\to B'(-4,2) \\to C'(-1,6)$ runs "
                                                       'counterclockwise. Option A falsely asserts '
                                                       'that orientation is preserved '
                                                       '(translations and rotations preserve '
                                                       'orientation, but reflections do not). '
                                                       'Option B is false because orientation '
                                                       'reversal does not alter congruence. Option '
                                                       'D is incorrect because rigid motions '
                                                       'include opposite isometries.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-9',
                                        'q': 'A quadrilateral has vertices $Q(0, 4)$, $R(3, 0)$, '
                                             '$S(-2, 5)$, and $T(0, -6)$. If the quadrilateral is '
                                             'reflected across the $y$-axis, which vertex or '
                                             'vertices remain strictly fixed at their original '
                                             "coordinates ($P = P'$)?",
                                        'opts': [   'Only $R(3, 0)$',
                                                    'Only $S(-2, 5)$',
                                                    'None of the vertices, because transformations '
                                                    'always move every point',
                                                    'Both $Q(0, 4)$ and $T(0, -6)$'],
                                        'correct': 3,
                                        'hint': 'Which points lie directly ON the line of '
                                                'reflection? Points on the line of reflection '
                                                "never move ($P = P'$).",
                                        'explanation': 'Option D is correct. The line of '
                                                       'reflection is the $y$-axis, whose equation '
                                                       'is $x = 0$. Any point lying directly on '
                                                       'the line of reflection is an invariant '
                                                       '(fixed) point: $(0, y) \\to (-0, y) = (0, '
                                                       'y)$. Both $Q(0, 4)$ and $T(0, -6)$ have an '
                                                       "$x$-coordinate of $0$, so $Q' = Q(0, 4)$ "
                                                       "and $T' = T(0, -6)$. Option A $R(3, 0)$ "
                                                       'lies on the $x$-axis, not the $y$-axis; '
                                                       "its image is $R'(-3, 0) \\neq R$. Option B "
                                                       '$S(-2, 5)$ has $x = -2$, so its image is '
                                                       "$S'(2, 5)$. Option C is a common "
                                                       'misconception; points on the reflection '
                                                       'axis are always fixed.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-10',
                                        'q': 'A geometric figure is reflected across the line $y = '
                                             'x$. Which of the following points will map directly '
                                             "onto itself ($P = P'$)?",
                                        'opts': [   '$(4, -4)$',
                                                    '$(-7, -7)$',
                                                    '$(0, 5)$',
                                                    '$(3, -3)$'],
                                        'correct': 1,
                                        'hint': 'A point remains fixed under reflection if and '
                                                'only if it lies directly on the mirror line. Test '
                                                'which point satisfies $y = x$.',
                                        'explanation': 'Option B is correct. A point $(x, y)$ is '
                                                       'invariant under reflection across $y = x$ '
                                                       'if and only if it satisfies the equation '
                                                       'of the line, meaning $x = y$. For point '
                                                       '$(-7, -7)$, both coordinates are equal to '
                                                       '$-7$. Applying the reflection rule $(x, y) '
                                                       '\\to (y, x)$ gives $(-7, -7) \\to (-7, '
                                                       "-7)$, so $P = P'$. Options A $(4, -4)$ and "
                                                       'D $(3, -3)$ lie on the line $y = -x$, so '
                                                       'reflecting across $y = x$ swaps them to '
                                                       '$(-4, 4)$ and $(-3, 3)$. Option C $(0, 5)$ '
                                                       'maps to $(5, 0) \\neq (0, 5)$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-11',
                                        'q': 'Segment $\\overline{AB}$ connects $A(1, 2)$ and '
                                             '$B(4, 8)$, giving it a slope of $m = \\frac{8 - 2}{4 '
                                             '- 1} = 2$. If $\\overline{AB}$ is reflected across '
                                             "the $x$-axis to produce segment $\\overline{A'B'}$, "
                                             "what is the slope of $\\overline{A'B'}$?",
                                        'opts': [   '$2$',
                                                    '$\\frac{1}{2}$',
                                                    '$-2$',
                                                    '$-\\frac{1}{2}$'],
                                        'correct': 2,
                                        'hint': "Calculate the image coordinates $A'$ and $B'$ "
                                                'using $(x, y) \\to (x, -y)$, then compute the '
                                                "slope $m' = \\frac{y'_2 - y'_1}{x'_2 - x'_1}$.",
                                        'explanation': 'Option C is correct. Reflecting across the '
                                                       "$x$-axis maps $A(1, 2) \\to A'(1, -2)$ and "
                                                       "$B(4, 8) \\to B'(4, -8)$. The slope of "
                                                       "$\\overline{A'B'}$ is $m' = \\frac{-8 - "
                                                       '(-2)}{4 - 1} = \\frac{-6}{3} = -2$. In '
                                                       'general, reflecting across any horizontal '
                                                       'or vertical line negates the slope of a '
                                                       "line segment: $m' = -m = -(2) = -2$. "
                                                       'Option A ($2$) incorrectly assumes slope '
                                                       'is invariant under reflection (slope is '
                                                       'preserved under translations, not axis '
                                                       'reflections). Option B ($\\frac{1}{2}$) '
                                                       'took the reciprocal. Option D '
                                                       '($-\\frac{1}{2}$) took the negative '
                                                       'reciprocal (perpendicular slope).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-12',
                                        'q': 'Line segment $\\overline{GH}$ has a slope of '
                                             '$-\\frac{3}{5}$. If $\\overline{GH}$ is reflected '
                                             'across the $y$-axis, what will be the slope of the '
                                             "reflected image $\\overline{G'H'}$?",
                                        'opts': [   '$\\frac{3}{5}$',
                                                    '$-\\frac{3}{5}$',
                                                    '$\\frac{5}{3}$',
                                                    '$-\\frac{5}{3}$'],
                                        'correct': 0,
                                        'hint': 'Reflecting across the $y$-axis negates the run '
                                                '($\\Delta x$), which changes the sign of the '
                                                "slope: $m' = \\frac{\\Delta y}{-\\Delta x} = -m$.",
                                        'explanation': 'Option A is correct. Under a reflection '
                                                       'across the $y$-axis, the transformation is '
                                                       '$(x, y) \\to (-x, y)$. For any two points '
                                                       'with horizontal change $\\Delta x = x_2 - '
                                                       'x_1$ and vertical change $\\Delta y = y_2 '
                                                       '- y_1$, the reflected points have '
                                                       'horizontal change $-\\Delta x$ and '
                                                       'vertical change $\\Delta y$. Thus, the new '
                                                       "slope is $m' = \\frac{\\Delta y}{-\\Delta "
                                                       'x} = -m$. Given $m = -\\frac{3}{5}$, the '
                                                       "reflected slope is $m' = "
                                                       '-\\left(-\\frac{3}{5}\\right) = '
                                                       '\\frac{3}{5}$. Option B ($-\\frac{3}{5}$) '
                                                       'fails to negate the slope. Options C and D '
                                                       'invert the ratio of vertical to horizontal '
                                                       'change.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-13',
                                        'q': 'A figure is reflected across the vertical line $x = '
                                             '2$, and its image is immediately reflected across '
                                             'the parallel vertical line $x = 7$. What single '
                                             'transformation is equivalent to this composition of '
                                             'two reflections?',
                                        'opts': [   'A translation $5\\text{ units}$ to the right',
                                                    'A translation $10\\text{ units}$ to the right',
                                                    'A rotation of $180^\\circ$ about the point '
                                                    '$(4.5, 0)$',
                                                    'A translation $10\\text{ units}$ to the left'],
                                        'correct': 1,
                                        'hint': 'According to the Double Reflection Theorem, '
                                                'reflecting across two parallel lines separated by '
                                                'distance $d$ produces a translation of $2d$ in '
                                                'the direction from the first line to the second.',
                                        'explanation': 'Option B is correct. By the Double '
                                                       'Reflection Theorem across parallel lines, '
                                                       'the composition of reflections across two '
                                                       'parallel lines separated by distance $d$ '
                                                       'is equivalent to a translation by $2d$ '
                                                       'perpendicular to the lines. The lines $x = '
                                                       '2$ and $x = 7$ are parallel vertical lines '
                                                       'separated by $d = 7 - 2 = 5$ units '
                                                       'directed to the right. The composite '
                                                       'motion is therefore a translation to the '
                                                       'right by $2d = 2(5) = 10$ units: $(x, y) '
                                                       '\\to (x + 10, y)$. For verification, test '
                                                       '$x = 0$: reflect across $x = 2 \\implies '
                                                       '2(2) - 0 = 4$; reflect $4$ across $x = 7 '
                                                       '\\implies 2(7) - 4 = 10$. Net change: '
                                                       '$+10$. Option A forgets to multiply the '
                                                       'distance by $2$. Option C confuses '
                                                       'parallel reflection lines with '
                                                       'intersecting reflection lines. Option D '
                                                       'translates in the opposite direction.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-14',
                                        'q': 'Figure $F$ is reflected across the horizontal line '
                                             '$y = -1$, and the resulting image is then reflected '
                                             'across the horizontal line $y = -5$. Which algebraic '
                                             'mapping rule describes this composite '
                                             'transformation?',
                                        'opts': [   '$(x, y) \\to (x, y - 8)$',
                                                    '$(x, y) \\to (x, y + 8)$',
                                                    '$(x, y) \\to (x, y - 4)$',
                                                    '$(x, y) \\to (-x, -y - 6)$'],
                                        'correct': 0,
                                        'hint': 'The lines are horizontal and parallel. The motion '
                                                'goes from $y = -1$ down to $y = -5$ (a downward '
                                                'shift). What is $2 \\times$ the distance between '
                                                'them?',
                                        'explanation': 'Option A is correct. Let us algebraically '
                                                       'compose the two reflections: 1. First '
                                                       'reflection across $y = -1$: $y_1 = 2(-1) - '
                                                       'y = -2 - y$. 2. Second reflection across '
                                                       '$y = -5$: $y_2 = 2(-5) - y_1 = -10 - (-2 - '
                                                       'y) = -10 + 2 + y = y - 8$. The '
                                                       '$x$-coordinate is unaffected because both '
                                                       'lines are horizontal. Thus, the '
                                                       'composition is the pure translation $(x, '
                                                       'y) \\to (x, y - 8)$. This matches the '
                                                       'theorem: the directed distance from $y = '
                                                       '-1$ to $y = -5$ is $-4$, and doubling it '
                                                       'gives a shift of $2(-4) = -8$. Option B '
                                                       '$(x, y) \\to (x, y + 8)$ shifts upward '
                                                       'instead of downward. Option C $(x, y) \\to '
                                                       '(x, y - 4)$ forgot to double the distance. '
                                                       'Option D confuses the translation with a '
                                                       'point reflection.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-15',
                                        'q': 'Triangle $\\triangle RST$ is reflected across the '
                                             '$x$-axis, and its image is then reflected across the '
                                             '$y$-axis. Which single transformation achieves the '
                                             'exact same image from the original $\\triangle RST$?',
                                        'opts': [   'A translation $2\\text{ units}$ along the '
                                                    'vector $\\langle -1, -1 \\rangle$',
                                                    'A reflection across the diagonal line $y = '
                                                    '-x$',
                                                    'A rotation of $180^\\circ$ about the origin '
                                                    '$(0, 0)$',
                                                    'A reflection across the diagonal line $y = '
                                                    'x$'],
                                        'correct': 2,
                                        'hint': 'Trace what happens to coordinates: first $(x, y) '
                                                '\\to (x, -y)$, then apply the second reflection. '
                                                'Which single transformation rule is $(-x, -y)$?',
                                        'explanation': 'Option C is correct. Track an arbitrary '
                                                       'point $(x, y)$ under the two '
                                                       'transformations: First, reflection across '
                                                       'the $x$-axis maps $(x, y) \\to (x, -y)$. '
                                                       'Next, reflection across the $y$-axis maps '
                                                       '$(x, -y) \\to (-x, -y)$. The algebraic '
                                                       'rule $(x, y) \\to (-x, -y)$ is precisely '
                                                       'the rule for a $180^\\circ$ rotation '
                                                       '(clockwise or counterclockwise) about the '
                                                       'origin $(0, 0)$. Geometrically, when two '
                                                       'reflection lines intersect at an angle '
                                                       '$\\theta = 90^\\circ$, their composition '
                                                       'is a rotation about their intersection '
                                                       'point by $2\\theta = 2(90^\\circ) = '
                                                       '180^\\circ$. Option A is a translation. '
                                                       'Option B is a reflection across $y = -x$, '
                                                       'which has rule $(x, y) \\to (-y, -x)$. '
                                                       'Option D is a reflection across $y = x$, '
                                                       'which has rule $(x, y) \\to (y, x)$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-16',
                                        'q': 'A polygon has clockwise vertex ordering. It is '
                                             'reflected across the vertical line $x = 3$, and that '
                                             'image is subsequently reflected across the '
                                             'perpendicular horizontal line $y = -2$. What is the '
                                             'vertex orientation of the final image, and what '
                                             'geometric motion describes this combined '
                                             'transformation?',
                                        'opts': [   'Counterclockwise; the transformation is '
                                                    'equivalent to a single reflection across $y = '
                                                    '-x + 1$.',
                                                    'Counterclockwise; each reflection preserves '
                                                    'orientation so the net result is unchanged.',
                                                    'Clockwise; reflecting twice across '
                                                    'perpendicular lines preserves orientation and '
                                                    'is equivalent to a $180^\\circ$ rotation '
                                                    'about $(3, -2)$.',
                                                    'Undefined; intersecting reflections destroy '
                                                    'polygon vertex ordering.'],
                                        'correct': 2,
                                        'hint': 'A single reflection reverses orientation '
                                                '(clockwise $\\to$ counterclockwise). What does a '
                                                'second reflection do? Remember: two perpendicular '
                                                'reflections form a $180^\\circ$ rotation.',
                                        'explanation': 'Option C is correct. A single reflection '
                                                       'is an opposite isometry, reversing '
                                                       'orientation from clockwise to '
                                                       'counterclockwise. A second reflection '
                                                       'reverses orientation once again: '
                                                       'counterclockwise $\\to$ clockwise. Because '
                                                       'the two lines $x = 3$ and $y = -2$ are '
                                                       'perpendicular (intersecting at $(3, -2)$ '
                                                       'at $90^\\circ$), their composition is a '
                                                       '$180^\\circ$ rotation about $(3, -2)$. '
                                                       'Rotations are direct isometries that '
                                                       'preserve clockwise orientation. Option A '
                                                       'claims the composition of two reflections '
                                                       'is a single reflection (two reflections '
                                                       'can never equal an odd number of '
                                                       'reflections). Option B falsely claims that '
                                                       'individual reflections preserve '
                                                       'orientation. Option D is mathematically '
                                                       'meaningless because rigid motions always '
                                                       'preserve geometric structure.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-17',
                                        'q': 'Preimage point $W(-5, 3)$ is mapped to image point '
                                             "$W'(7, 3)$ by a single reflection. What is the "
                                             'equation of the line of reflection?',
                                        'opts': ['$x = 1$', '$y = 3$', '$x = 2$', '$y = 1$'],
                                        'correct': 0,
                                        'hint': 'The points share the same $y$-coordinate ($3$), '
                                                "so $\\overline{WW'}$ is horizontal. The line of "
                                                'reflection must be vertical ($x = c$) and pass '
                                                "through the midpoint of $\\overline{WW'}$.",
                                        'explanation': 'Option A is correct. Points $W(-5, 3)$ and '
                                                       "$W'(7, 3)$ have identical $y$-coordinates, "
                                                       "meaning segment $\\overline{WW'}$ is "
                                                       'horizontal. The line of reflection is the '
                                                       'perpendicular bisector of '
                                                       "$\\overline{WW'}$. A line perpendicular to "
                                                       'a horizontal line is a vertical line of '
                                                       'the form $x = c$. The line must pass '
                                                       'through the midpoint $x$-coordinate: $c = '
                                                       '\\frac{-5 + 7}{2} = \\frac{2}{2} = 1$. '
                                                       'Therefore, the line of reflection is $x = '
                                                       '1$. Option B ($y = 3$) is the horizontal '
                                                       'line on which the points lie, not the '
                                                       'perpendicular bisector. Option C ($x = 2$) '
                                                       'results from an arithmetic error in '
                                                       'calculating the average. Option D ($y = '
                                                       '1$) is a horizontal line.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-18',
                                        'q': 'During a geometry lab, a student discovers that '
                                             'preimage vertex $E(2, -5)$ maps to image vertex '
                                             "$E'(-5, 2)$ after a single reflection. Across which "
                                             'line was the point reflected?',
                                        'opts': [   'The $x$-axis ($y = 0$)',
                                                    'The line $y = -x$',
                                                    'The $y$-axis ($x = 0$)',
                                                    'The line $y = x$'],
                                        'correct': 3,
                                        'hint': "Compare the coordinates: $x = 2$ became $y' = 2$, "
                                                "and $y = -5$ became $x' = -5$. The coordinates "
                                                'swapped places without sign changes: $(x, y) \\to '
                                                '(y, x)$.',
                                        'explanation': 'Option D is correct. Comparing preimage '
                                                       "$E(2, -5)$ and image $E'(-5, 2)$, the $x$- "
                                                       'and $y$-coordinates have swapped values: '
                                                       '$(x, y) \\to (y, x)$. This is the defining '
                                                       'coordinate rule for reflection across the '
                                                       'diagonal line $y = x$. We can also verify '
                                                       'using the perpendicular bisector property: '
                                                       'The midpoint is $\\left(\\frac{2 + '
                                                       '(-5)}{2}, \\frac{-5 + 2}{2}\\right) = '
                                                       '(-1.5, -1.5)$, which lies directly on $y = '
                                                       "x$. The slope of $\\overline{EE'}$ is "
                                                       '$\\frac{2 - (-5)}{-5 - 2} = \\frac{7}{-7} '
                                                       '= -1$, which is perpendicular to the slope '
                                                       'of $y = x$ ($+1$). Option A reflects $(2, '
                                                       '-5)$ to $(2, 5)$. Option B ($y = -x$) '
                                                       'reflects $(2, -5)$ to $(5, -2)$ by '
                                                       'swapping and negating. Option C reflects '
                                                       '$(2, -5)$ to $(-2, -5)$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-19',
                                        'q': 'A regular octagon is centered at the origin on the '
                                             'coordinate plane. How many distinct lines of '
                                             'reflectional symmetry does this regular octagon '
                                             'possess?',
                                        'opts': ['$4$', '$8$', '$16$', 'Infinitely many'],
                                        'correct': 1,
                                        'hint': 'In any regular polygon with $n$ sides, how many '
                                                'lines of symmetry connect opposite vertices or '
                                                'midpoints of opposite sides?',
                                        'explanation': 'Option B is correct. Any regular polygon '
                                                       'with $n$ sides has exactly $n$ lines of '
                                                       'reflectional symmetry. For a regular '
                                                       'octagon ($n = 8$): • $4$ lines of symmetry '
                                                       'pass through pairs of opposite vertices.\n'
                                                       '• $4$ lines of symmetry pass through the '
                                                       'midpoints of opposite sides.\n'
                                                       'This gives a total of $4 + 4 = 8$ distinct '
                                                       'lines of reflectional symmetry. Option A '
                                                       '($4$) counts only the vertex lines or only '
                                                       'the side-bisector lines. Option C ($16$) '
                                                       'double-counts the axes or confuses lines '
                                                       'of symmetry with total symmetries '
                                                       '(dihedral group order $D_8$). Option D '
                                                       'applies only to a circle.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-3-mcq-20',
                                        'q': 'An isosceles trapezoid is positioned in the '
                                             'coordinate plane with vertices $A(-4, 1)$, $B(4, '
                                             '1)$, $C(2, 5)$, and $D(-2, 5)$. Which equation '
                                             'represents the line of reflectional symmetry that '
                                             'maps this trapezoid onto itself?',
                                        'opts': [   '$y = 0$ (the $x$-axis)',
                                                    '$y = 3$',
                                                    '$y = x$',
                                                    '$x = 0$ (the $y$-axis)'],
                                        'correct': 3,
                                        'hint': 'A line of symmetry must reflect every vertex of '
                                                'the trapezoid onto another vertex of the same '
                                                'trapezoid. Test which axis reflects $A(-4, 1)$ to '
                                                '$B(4, 1)$ and $D(-2, 5)$ to $C(2, 5)$.',
                                        'explanation': 'Option D is correct. Reflecting across the '
                                                       'line $x = 0$ (the $y$-axis) applies the '
                                                       'rule $(x, y) \\to (-x, y)$: • $A(-4, 1) '
                                                       '\\to (4, 1) = B$\n'
                                                       '• $B(4, 1) \\to (-4, 1) = A$\n'
                                                       '• $C(2, 5) \\to (-2, 5) = D$\n'
                                                       '• $D(-2, 5) \\to (2, 5) = C$\n'
                                                       'Every vertex maps directly onto a '
                                                       'corresponding vertex of the figure, '
                                                       'meaning the $y$-axis ($x = 0$) is the line '
                                                       'of symmetry. Option A ($y = 0$) flips the '
                                                       'trapezoid below the $x$-axis ($y < 0$), '
                                                       'completely outside its original region. '
                                                       'Option B ($y = 3$) is a horizontal '
                                                       'midline; reflecting over it would swap '
                                                       'base $AB$ (length $8$) with base $CD$ '
                                                       '(length $4$), distorting the figure. '
                                                       'Option C ($y = x$) tilts the figure '
                                                       'obliquely.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'}],
                        'fitb': [   {   'id': 'p-1-3-f1',
                                        'q': 'If point Q(5, -7) is reflected across the y-axis, '
                                             "what are the coordinates of Q'? Enter as (x, y):",
                                        'expected': '(-5, -7)',
                                        'altExpected': ['(-5,-7)', '-5, -7', '-5,-7'],
                                        'hint': 'Negate the x-coordinate: (x, y) → (-x, y).'},
                                    {   'id': 'p-1-3-f2',
                                        'q': 'Point R(4, 9) is reflected across the line y = x. '
                                             "Enter the image coordinates R':",
                                        'expected': '(9, 4)',
                                        'altExpected': ['(9,4)', '9, 4', '9,4'],
                                        'hint': 'Swap the x and y coordinates: (x, y) → (y, x).'}]},
        'bookQuestions': [   {   'num': 'HMH Into Math • Section 1.3 Problem 5',
                                 'q': 'Point \\(A(3, 4)\\) is reflected across line \\(m\\) to '
                                      "point \\(A'(3, -2)\\). (a) What is the equation of the line "
                                      'of reflection \\(m\\)? (b) Explain how you found it.',
                                 'modelAnswer': '<strong>Model Answer:</strong><br>(a) The line of '
                                                'reflection is \\(y = 1\\).<br>(b) The line of '
                                                'reflection must be the perpendicular bisector of '
                                                "segment \\(AA'\\). Since the x-coordinates are "
                                                "both 3, segment \\(AA'\\) is vertical. The "
                                                'midpoint has y-coordinate: \\(\\frac{4 + (-2)}{2} '
                                                '= \\frac{2}{2} = 1\\). The perpendicular bisector '
                                                'of a vertical segment through midpoint \\((3, '
                                                '1)\\) is the horizontal line \\(y = 1\\).'},
                             {   'num': 'HMH Into Math • Section 1.3 Problem 11',
                                 'q': 'Show why reflecting a point twice across the same line '
                                      'returns it to its original preimage position.',
                                 'modelAnswer': '<strong>Model Answer:</strong> Consider '
                                                'reflection across the x-axis: \\((x, y) \\to (x, '
                                                '-y)\\). Reflecting the image point \\((x, -y)\\) '
                                                'again across the x-axis yields \\((x, -(-y)) = '
                                                '(x, y)\\). Since negating a coordinate twice '
                                                'produces the original coordinate, two consecutive '
                                                'reflections across the same line act as the '
                                                'identity transformation.'}]},
    {   'id': '1.4',
        'modId': 'mod1',
        'modNum': 1,
        'modTitle': 'Transformations and Congruence',
        'themeColor': '#4f46e5',
        'badge': 'Module 1 • Lesson 1.4',
        'num': '1.4',
        'title': 'Explore Rotations',
        'tag': 'Angles of Rotation & Origin Turns',
        'standard': 'CCSS.MATH.CONTENT.8.G.A.1.b, 8.G.A.3',
        'canDo': 'I can rotate figures 90°, 180°, and 270° clockwise and counterclockwise about '
                 'the origin, apply algebraic rules, and verify that distances from the center are '
                 'preserved.',
        'conceptIntro': 'A <strong>rotation</strong> is a rigid motion that turns every point of a '
                        'figure through a specified angle and direction about a fixed point called '
                        'the <strong>center of rotation</strong>. When rotating about the origin '
                        '\\((0, 0)\\), every point \\(P\\) moves along a circular arc such that '
                        "\\(OP = OP'\\). Rotations preserve side lengths, angle measures, and "
                        'vertex orientation.',
        'rules': [   {   'name': '90° Clockwise (270° CCW)',
                         'formula': '(x, y) \\to (y, -x)',
                         'desc': 'Swap coordinates, then negate the new y.'},
                     {   'name': '180° Turn (Half-turn)',
                         'formula': '(x, y) \\to (-x, -y)',
                         'desc': 'Negate both coordinates; direction does not matter.'},
                     {   'name': '270° Clockwise (90° CCW)',
                         'formula': '(x, y) \\to (-y, x)',
                         'desc': 'Swap coordinates, then negate the new x.'},
                     {   'name': '360° Full Turn',
                         'formula': '(x, y) \\to (x, y)',
                         'desc': 'Complete turn returns shape to original position.'}],
        'vocab': [   {   'term': 'Rotation',
                         'def': 'A rigid transformation that turns a shape about a fixed center by '
                                'a specified angle.',
                         'ex': 'Turning hands of a clock.'},
                     {   'term': 'Center of Rotation',
                         'def': 'The fixed point about which all other points turn.',
                         'ex': 'The origin (0, 0).'},
                     {   'term': 'Angle of Rotation',
                         'def': 'The amount of turn measured in degrees (90°, 180°, 270°).',
                         'ex': 'Quarter turn = 90°; Half turn = 180°.'}],
        'invariance': [   {   'prop': 'Distance to Center (Radius)',
                              'status': "✓ Preserved (OP = OP')",
                              'cls': 'yes'},
                          {'prop': 'Side Lengths & Angles', 'status': '✓ Preserved', 'cls': 'yes'},
                          {   'prop': 'Orientation',
                              'status': '✓ Preserved (Clockwise stays CW)',
                              'cls': 'yes'},
                          {'prop': 'Area & Perimeter', 'status': '✓ Preserved', 'cls': 'yes'}],
        'illustrativeExamples': [   {   'title': 'Example 1: 90° Clockwise Rotation',
                                        'desc': 'Rotate point \\(A(2, 5)\\) by 90° clockwise about '
                                                'the origin.',
                                        'analysis': 'Rule: \\((x, y) \\to (y, -x)\\). Substitute: '
                                                    '\\(x = 2, y = 5\\). New coordinates: \\((5, '
                                                    '-2)\\). Point \\(A\\) moves from Quadrant I '
                                                    'to Quadrant IV.'},
                                    {   'title': 'Example 2: 180° Rotation',
                                        'desc': 'Rotate point \\(B(-3, 4)\\) by 180° about the '
                                                'origin.',
                                        'analysis': 'Rule: \\((x, y) \\to (-x, -y)\\). Both '
                                                    'coordinates negate: \\(-(-3) = 3\\) and '
                                                    "\\(-4\\). Image \\(B' = (3, -4)\\). It passes "
                                                    'straight through the origin to the opposite '
                                                    'quadrant.'}],
        'workedExample': {   'title': 'Worked Example: Rotating a Triangle 90° Counterclockwise',
                             'problem': 'Triangle \\(XYZ\\) has vertices \\(X(1, 3)\\), \\(Y(4, '
                                        '3)\\), and \\(Z(1, 6)\\). Rotate \\(\\triangle XYZ\\) by '
                                        '90° counterclockwise about the origin. (a) State the '
                                        'coordinate rule. (b) Calculate the image coordinates '
                                        "\\(X'\\), \\(Y'\\), and \\(Z'\\). (c) Prove that "
                                        "\\(\\triangle XYZ \\cong \\triangle X'Y'Z'\\).",
                             'step1': '<strong>Step 1: Identify the algebraic rule:</strong> A 90° '
                                      'counterclockwise (CCW) rotation is identical to 270° '
                                      'clockwise: \\((x, y) \\to (-y, x)\\).',
                             'step2': '<strong>Step 2: Apply the rule to each '
                                      "vertex:</strong><br>• \\(X(1, 3) \\to X'(-3, 1)\\)<br>• "
                                      "\\(Y(4, 3) \\to Y'(-3, 4)\\)<br>• \\(Z(1, 6) \\to Z'(-6, "
                                      '1)\\).',
                             'step3': '<strong>Step 3: Justify congruence:</strong> Side length '
                                      "\\(XY = 3\\) and \\(X'Y' = 3\\). Side \\(XZ = 3\\) and "
                                      "\\(X'Z' = 3\\). Angle \\(\\angle X = 90^\\circ\\) and "
                                      "\\(\\angle X' = 90^\\circ\\). Because rotations are rigid "
                                      'motions, all distances and angles are preserved; therefore, '
                                      "\\(\\triangle XYZ \\cong \\triangle X'Y'Z'\\).",
                             'modelAnswer': '<strong>Student Model Answer:</strong> The rule is '
                                            '\\((x, y) \\to (-y, x)\\). The image vertices are '
                                            "\\(X'(-3, 1)\\), \\(Y'(-3, 4)\\), and \\(Z'(-6, "
                                            '1)\\). Because rotations are rigid motions, side '
                                            'lengths and angle measures are preserved, proving '
                                            "\\(\\triangle XYZ \\cong \\triangle X'Y'Z'\\)."},
        'practice': {   'mcqs': [   {   'id': 'p-1-4-mcq-1',
                                        'q': 'In transformational geometry, a rotation by an angle '
                                             '$\\theta > 0^\\circ$ is defined by a center of '
                                             'rotation, an angle of rotation, and a direction. '
                                             'According to standard mathematical convention, which '
                                             'direction corresponds to a positive angle of '
                                             'rotation (such as $+90^\\circ$) on the coordinate '
                                             'plane?',
                                        'opts': [   'Clockwise',
                                                    'Counterclockwise',
                                                    'In the positive $x$-direction (to the right)',
                                                    'In the positive $y$-direction (upward)'],
                                        'correct': 1,
                                        'hint': 'Think about how angles are measured in standard '
                                                'position on the coordinate plane starting from '
                                                'the positive $x$-axis.',
                                        'explanation': 'In standard mathematics and geometry, a '
                                                       'positive angle of rotation turns in the '
                                                       'counterclockwise direction (for example, '
                                                       '$+90^\\circ$ indicates a $90^\\circ$ '
                                                       'counterclockwise turn). A clockwise '
                                                       'rotation corresponds to a negative angle. '
                                                       'Choices C and D describe translations '
                                                       '(linear shifts along axes), not rotational '
                                                       'directions.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-2',
                                        'q': 'Triangle $ABC$ is rotated $90^\\circ$ '
                                             'counterclockwise about the origin $(0, 0)$. What '
                                             'happens to the coordinates of the origin itself '
                                             'during this transformation?',
                                        'opts': [   'The origin shifts to $(0, 1)$ because of the '
                                                    '$90^\\circ$ counterclockwise turn.',
                                                    'The origin is undefined after a rotation '
                                                    'because a pivot cannot move.',
                                                    'The origin remains at $(0, 0)$ because the '
                                                    'center of rotation is a fixed point that maps '
                                                    'onto itself.',
                                                    'The origin moves to $(-1, 0)$ following the '
                                                    'rule $(x, y) \\to (-y, x)$.'],
                                        'correct': 2,
                                        'hint': 'Consider what happens to the point where the tip '
                                                'of your pencil rests when turning tracing paper '
                                                '(Into Math TE p. 62-63).',
                                        'explanation': 'The center of rotation is a fixed point '
                                                       '(invariant point) under any rotation. '
                                                       'Under the coordinate mapping rule $(x, y) '
                                                       '\\to (-y, x)$, substituting $(0, 0)$ '
                                                       'yields $(-0, 0) = (0, 0)$. Choices A and D '
                                                       'incorrectly assign non-zero coordinates to '
                                                       'the center of rotation, while Choice B '
                                                       'incorrectly claims the point is undefined.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-3',
                                        'q': 'Point $A(3, 7)$ is rotated $90^\\circ$ '
                                             'counterclockwise about the origin. What are the '
                                             "coordinates of the image point $A'$?",
                                        'opts': [   "$A'(7, -3)$",
                                                    "$A'(-7, 3)$",
                                                    "$A'(-3, -7)$",
                                                    "$A'(-7, -3)$"],
                                        'correct': 1,
                                        'hint': 'Apply the algebraic mapping rule for a '
                                                '$90^\\circ$ counterclockwise rotation: $(x, y) '
                                                '\\to (-y, x)$.',
                                        'explanation': 'For a $90^\\circ$ counterclockwise '
                                                       'rotation about the origin, the mapping '
                                                       'rule is $(x, y) \\to (-y, x)$. Given $A(3, '
                                                       '7)$, we have $x = 3$ and $y = 7$. '
                                                       "Substituting these values gives $A'(-7, "
                                                       '3)$. Choice A $(7, -3)$ is the result of a '
                                                       '$90^\\circ$ clockwise rotation $(y, -x)$. '
                                                       'Choice C $(-3, -7)$ is a $180^\\circ$ '
                                                       'rotation $(-x, -y)$. Choice D $(-7, -3)$ '
                                                       'incorrectly negates both coordinates after '
                                                       'swapping.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-4',
                                        'q': 'Point $B(-4, -6)$ in Quadrant III is rotated '
                                             '$90^\\circ$ counterclockwise about the origin. What '
                                             "are the coordinates of the image point $B'$?",
                                        'opts': [   "$B'(-6, 4)$",
                                                    "$B'(4, -6)$",
                                                    "$B'(-6, -4)$",
                                                    "$B'(6, -4)$"],
                                        'correct': 3,
                                        'hint': 'Be careful with signs: $-y$ means the opposite of '
                                                '$y$. If $y = -6$, what is $-y$?',
                                        'explanation': 'The algebraic rule for a $90^\\circ$ '
                                                       'counterclockwise rotation about the origin '
                                                       'is $(x, y) \\to (-y, x)$. For $B(-4, -6)$, '
                                                       'the new $x$-coordinate is $-y = -(-6) = '
                                                       '6$, and the new $y$-coordinate is $x = '
                                                       "-4$. Thus $B'(6, -4)$ lies in Quadrant IV. "
                                                       'Choice A $(-6, 4)$ forgets that $-(-6) = '
                                                       '+6$. Choice B $(4, -6)$ negates $x$ and '
                                                       'leaves $y$ unchanged (a reflection across '
                                                       'the $y$-axis). Choice C $(-6, -4)$ swaps '
                                                       'coordinates without applying the required '
                                                       'negation.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-5',
                                        'q': 'In HMH Into Math Lesson 1.4, a figure with vertex '
                                             '$J(-3, 4)$ is rotated $180^\\circ$ about the origin. '
                                             "What are the coordinates of the image vertex $J'$?",
                                        'opts': [   "$J'(3, -4)$",
                                                    "$J'(-4, -3)$",
                                                    "$J'(4, 3)$",
                                                    "$J'(-3, -4)$"],
                                        'correct': 0,
                                        'hint': 'A $180^\\circ$ rotation takes every point $(x, '
                                                'y)$ to $(-x, -y)$, whether turned clockwise or '
                                                'counterclockwise.',
                                        'explanation': 'The rule for a $180^\\circ$ rotation about '
                                                       'the origin is $(x, y) \\to (-x, -y)$. '
                                                       "Applying this to $J(-3, 4)$ gives $x' = "
                                                       "-(-3) = 3$ and $y' = -(4) = -4$, resulting "
                                                       "in $J'(3, -4)$. Note that turning "
                                                       '$180^\\circ$ clockwise or $180^\\circ$ '
                                                       'counterclockwise yields the identical '
                                                       'image. Choice B $(-4, -3)$ mistakenly '
                                                       'swaps the coordinates. Choice C $(4, 3)$ '
                                                       'applies a $90^\\circ$ clockwise rule with '
                                                       'sign errors. Choice D $(-3, -4)$ only '
                                                       'negates the $y$-coordinate.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-6',
                                        'q': "In the textbook activity (TE p. 64), the letter 'N' "
                                             'has vertex $A(2, 1)$ and is rotated $90^\\circ$ '
                                             "clockwise about the origin to create the letter 'Z'. "
                                             "What are the coordinates of image vertex $A'$?",
                                        'opts': [   "$A'(-1, 2)$",
                                                    "$A'(1, -2)$",
                                                    "$A'(-2, 1)$",
                                                    "$A'(-2, -1)$"],
                                        'correct': 1,
                                        'hint': 'A $90^\\circ$ clockwise rotation follows the '
                                                'algebraic rule $(x, y) \\to (y, -x)$.',
                                        'explanation': 'Rotating $90^\\circ$ clockwise about the '
                                                       'origin follows the mapping rule $(x, y) '
                                                       '\\to (y, -x)$. With preimage $A(2, 1)$, we '
                                                       'swap coordinates and negate the new second '
                                                       "component: $x' = y = 1$ and $y' = -x = "
                                                       "-2$. Therefore, $A'(1, -2)$. Choice A "
                                                       '$(-1, 2)$ is the result of a $90^\\circ$ '
                                                       'counterclockwise rotation $(-y, x)$. '
                                                       'Choice C $(-2, 1)$ is a reflection across '
                                                       'the $y$-axis. Choice D $(-2, -1)$ is a '
                                                       '$180^\\circ$ rotation.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-7',
                                        'q': 'Which algebraic mapping rule represents both a '
                                             '$270^\\circ$ counterclockwise rotation and a '
                                             '$90^\\circ$ clockwise rotation about the origin?',
                                        'opts': [   '$(x, y) \\to (-y, x)$',
                                                    '$(x, y) \\to (-x, -y)$',
                                                    '$(x, y) \\to (y, -x)$',
                                                    '$(x, y) \\to (-y, -x)$'],
                                        'correct': 2,
                                        'hint': 'A full circle is $360^\\circ$. Turning '
                                                '$90^\\circ$ clockwise brings a figure to the same '
                                                'position as turning $360^\\circ - 90^\\circ = '
                                                '270^\\circ$ counterclockwise.',
                                        'explanation': 'Because a full rotation is $360^\\circ$, '
                                                       'moving $90^\\circ$ clockwise places a '
                                                       'figure in the exact same position as '
                                                       'moving $360^\\circ - 90^\\circ = '
                                                       '270^\\circ$ counterclockwise. Both '
                                                       'rotations share the coordinate rule $(x, '
                                                       'y) \\to (y, -x)$. Choice A $(-y, x)$ '
                                                       'represents a $90^\\circ$ counterclockwise '
                                                       '(or $270^\\circ$ clockwise) rotation. '
                                                       'Choice B $(-x, -y)$ represents a '
                                                       '$180^\\circ$ rotation. Choice D $(-y, -x)$ '
                                                       'is a reflection across the line $y = -x$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-8',
                                        'q': 'Point $P(5, -2)$ undergoes a $270^\\circ$ clockwise '
                                             'rotation about the origin. What are the coordinates '
                                             "of image point $P'$?",
                                        'opts': [   "$P'(2, 5)$",
                                                    "$P'(-2, -5)$",
                                                    "$P'(-5, 2)$",
                                                    "$P'(5, 2)$"],
                                        'correct': 0,
                                        'hint': 'Convert the $270^\\circ$ clockwise rotation to '
                                                'its equivalent counterclockwise turn: $360^\\circ '
                                                '- 270^\\circ = 90^\\circ$ counterclockwise.',
                                        'explanation': 'Rotating $270^\\circ$ clockwise is '
                                                       'equivalent to rotating $360^\\circ - '
                                                       '270^\\circ = 90^\\circ$ counterclockwise '
                                                       'about the origin. The rule for $90^\\circ$ '
                                                       'counterclockwise is $(x, y) \\to (-y, x)$. '
                                                       "For $P(5, -2)$, $x' = -(-2) = 2$ and $y' = "
                                                       "x = 5$, giving $P'(2, 5)$. Choice B $(-2, "
                                                       '-5)$ uses the $90^\\circ$ clockwise rule '
                                                       '$(y, -x)$. Choice C $(-5, 2)$ is a '
                                                       '$180^\\circ$ rotation $(-x, -y)$. Choice D '
                                                       '$(5, 2)$ reflects across the $x$-axis.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-9',
                                        'q': 'A quadrilateral in the coordinate plane is rotated '
                                             '$360^\\circ$ about the origin. Which statement '
                                             'correctly describes the relationship between the '
                                             'preimage and its image?',
                                        'opts': [   'The image is inverted into the opposite '
                                                    'quadrant according to $(x, y) \\to (-x, -y)$.',
                                                    'The coordinates swap axes according to $(x, '
                                                    'y) \\to (y, x)$.',
                                                    'The image is identical to the preimage and '
                                                    'occupies the exact same position because a '
                                                    '$360^\\circ$ rotation is a full turn: $(x, y) '
                                                    '\\to (x, y)$.',
                                                    'The coordinates are multiplied by 2 because '
                                                    '$360^\\circ$ is twice $180^\\circ$.'],
                                        'correct': 2,
                                        'hint': 'How many degrees are in one complete circle or '
                                                'full turn?',
                                        'explanation': 'A $360^\\circ$ rotation represents one '
                                                       'complete revolution around the center of '
                                                       'rotation. Every point completes a full '
                                                       'circular path and returns to its initial '
                                                       'location, described by the identity rule '
                                                       '$(x, y) \\to (x, y)$. Choice A describes a '
                                                       '$180^\\circ$ rotation. Choice B is a '
                                                       'reflection across the line $y = x$. Choice '
                                                       'D confuses rotation with a dilation of '
                                                       'scale factor 2.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-10',
                                        'q': 'Triangle $ABC$ has vertices named in clockwise '
                                             'order: $A(1, 2)$, $B(4, 2)$, and $C(1, 6)$. Which '
                                             'transformation will result in an image triangle '
                                             "whose corresponding vertices $A' \\to B' \\to C'$ "
                                             'remain in clockwise order?',
                                        'opts': [   'A reflection across the $x$-axis',
                                                    'A reflection across the $y$-axis',
                                                    'A reflection across the line $y = x$',
                                                    'A rotation of $90^\\circ$ counterclockwise '
                                                    'about the origin'],
                                        'correct': 3,
                                        'hint': 'Which rigid motions preserve orientation '
                                                '(clockwise remains clockwise), and which rigid '
                                                'motion reverses orientation?',
                                        'explanation': 'Rotations and translations preserve vertex '
                                                       'orientation: if the vertices of the '
                                                       'preimage read in clockwise order, the '
                                                       'vertices of the image also read in '
                                                       'clockwise order. In contrast, reflections '
                                                       'reverse orientation (turning clockwise '
                                                       'order into counterclockwise order). '
                                                       'Therefore, only the rotation in Choice D '
                                                       'preserves the clockwise order. Choices A, '
                                                       'B, and C are all reflections, each of '
                                                       'which reverses vertex orientation.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-11',
                                        'q': 'In HMH Into Math Lesson 1.4 (p. 67 Problem 8), '
                                             '$\\triangle JKL$ has an area of $3.25\\text{ square '
                                             'units}$ and a perimeter of $8.5\\text{ units}$. What '
                                             'happens to its area and perimeter when it is rotated '
                                             '$180^\\circ$ about vertex $J$?',
                                        'opts': [   'Both area and perimeter remain unchanged: '
                                                    '$\\text{Area} = 3.25\\text{ square units}$ '
                                                    'and $\\text{Perimeter} = 8.5\\text{ units}$.',
                                                    'The perimeter doubles to $17.0\\text{ '
                                                    'units}$, but the area remains $3.25\\text{ '
                                                    'square units}$.',
                                                    'The area becomes negative ($-3.25\\text{ '
                                                    'square units}$) because the figure is '
                                                    'inverted.',
                                                    'The area becomes $0$ because the center of '
                                                    'rotation is located at vertex $J$.'],
                                        'correct': 0,
                                        'hint': 'Remember that a rotation is a rigid motion '
                                                '(isometry). What properties are preserved by all '
                                                'rigid motions?',
                                        'explanation': 'Rotations are rigid motions (isometries), '
                                                       'which preserve all distances (segment '
                                                       'lengths) and angle measures regardless of '
                                                       'the chosen center of rotation. Because all '
                                                       'side lengths are preserved, the perimeter '
                                                       'remains $8.5\\text{ units}$. Because side '
                                                       'lengths and angle measures are preserved, '
                                                       'the area remains strictly $3.25\\text{ '
                                                       'square units}$. Area cannot be negative '
                                                       '(Choice C), does not collapse to zero '
                                                       '(Choice D), and perimeter does not change '
                                                       '(Choice B).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-12',
                                        'q': 'Line segment $AB$ has endpoints $A(1, 2)$ and $B(3, '
                                             '8)$, giving it a slope of $m = \\frac{8 - 2}{3 - 1} '
                                             '= 3$. If segment $AB$ is rotated $90^\\circ$ '
                                             'counterclockwise about the origin to form segment '
                                             "$A'B'$, what is the slope $m'$ of the image segment?",
                                        'opts': [   "$m' = 3$",
                                                    "$m' = -3$",
                                                    "$m' = -\\frac{1}{3}$",
                                                    "$m' = \\frac{1}{3}$"],
                                        'correct': 2,
                                        'hint': 'A $90^\\circ$ rotation turns a line so that it is '
                                                'perpendicular to the original line. What is the '
                                                'relationship between the slopes of two '
                                                'perpendicular lines?',
                                        'explanation': 'Rotating a line segment by $90^\\circ$ '
                                                       'turns the segment perpendicular to its '
                                                       'original orientation. Two non-vertical '
                                                       'perpendicular lines have slopes that are '
                                                       "negative reciprocals ($m' = "
                                                       '-\\frac{1}{m}$). Since the original slope '
                                                       "is $m = 3$, the new slope is $m' = "
                                                       '-\\frac{1}{3}$. We can verify with '
                                                       "coordinates: $A'(-2, 1)$ and $B'(-8, 3)$ "
                                                       "using $(x, y) \\to (-y, x)$. Slope $m' = "
                                                       '\\frac{3 - 1}{-8 - (-2)} = \\frac{2}{-6} = '
                                                       '-\\frac{1}{3}$. Choice A assumes slope is '
                                                       'invariant (true for $180^\\circ$ or '
                                                       'translations, not $90^\\circ$). Choice B '
                                                       'only negates the slope without taking the '
                                                       'reciprocal. Choice D takes the reciprocal '
                                                       'without negating.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-13',
                                        'q': 'Line segment $CD$ has a slope of $m = '
                                             '-\\frac{4}{7}$. After undergoing a $180^\\circ$ '
                                             'rotation about the origin, what is the slope of the '
                                             "resulting image segment $C'D'$?",
                                        'opts': [   "$m' = \\frac{7}{4}$",
                                                    "$m' = -\\frac{4}{7}$",
                                                    "$m' = \\frac{4}{7}$",
                                                    "$m' = -\\frac{7}{4}$"],
                                        'correct': 1,
                                        'hint': 'A $180^\\circ$ rotation turns a segment in the '
                                                'opposite direction along a parallel line. What is '
                                                'true about the slopes of parallel lines?',
                                        'explanation': 'Under a $180^\\circ$ rotation about the '
                                                       'origin, every point $(x, y)$ maps to $(-x, '
                                                       '-y)$. The slope formula between image '
                                                       "points is $m' = \\frac{-y_2 - (-y_1)}{-x_2 "
                                                       '- (-x_1)} = \\frac{-(y_2 - y_1)}{-(x_2 - '
                                                       'x_1)} = \\frac{y_2 - y_1}{x_2 - x_1} = m$. '
                                                       'A $180^\\circ$ rotation preserves the '
                                                       "slope ($m' = m$) because the image line is "
                                                       'parallel to (or lies on the same line as) '
                                                       'the preimage line. Thus, the slope remains '
                                                       '$-\\frac{4}{7}$. Choice A is the '
                                                       'perpendicular negative reciprocal (for '
                                                       '$90^\\circ$). Choice C erroneously flips '
                                                       'the sign. Choice D is the reciprocal '
                                                       'without preserving the sign.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-14',
                                        'q': 'In Lesson 1.4 Spark Your Learning (TE p. 61-62), '
                                             'students investigate rotational symmetry. What is '
                                             'the minimum positive angle of rotation about its '
                                             'center that will map a regular hexagon ($6$ equal '
                                             'sides) onto itself?',
                                        'opts': [   '$90^\\circ$',
                                                    '$120^\\circ$',
                                                    '$45^\\circ$',
                                                    '$60^\\circ$'],
                                        'correct': 3,
                                        'hint': 'The minimum angle of rotational symmetry for a '
                                                'regular $n$-sided polygon is '
                                                '$\\frac{360^\\circ}{n}$.',
                                        'explanation': 'A regular polygon with $n$ sides has '
                                                       '$n$-fold rotational symmetry. The minimum '
                                                       'positive angle of rotation that maps the '
                                                       'figure onto itself is '
                                                       '$\\frac{360^\\circ}{n}$. For a regular '
                                                       'hexagon ($n = 6$), the minimum angle is '
                                                       '$\\frac{360^\\circ}{6} = 60^\\circ$. '
                                                       'Choice A ($90^\\circ$) is for a square ($n '
                                                       '= 4$). Choice B ($120^\\circ$) is a '
                                                       'multiple of $60^\\circ$ and the minimum '
                                                       'angle for an equilateral triangle ($n = '
                                                       '3$), but not the minimum for a hexagon. '
                                                       'Choice C ($45^\\circ$) is for a regular '
                                                       'octagon ($n = 8$).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-15',
                                        'q': 'In HMH Into Math Lesson 1.4 Step It Out (TE p. 64), '
                                             'students identify uppercase letters that look '
                                             'identical after a $180^\\circ$ rotation about their '
                                             'center point. Which group consists ENTIRELY of '
                                             'letters with $180^\\circ$ rotational symmetry?',
                                        'opts': [   '$\\text{A, M, T, V}$',
                                                    '$\\text{B, C, D, E}$',
                                                    '$\\text{H, N, O, Z}$',
                                                    '$\\text{F, G, J, L}$'],
                                        'correct': 2,
                                        'hint': 'Imagine turning the letters upside down '
                                                '($180^\\circ$). Which group contains letters that '
                                                'still look exactly the same?',
                                        'explanation': 'As highlighted in the Teacher Edition (p. '
                                                       '64 Turn and Talk), the uppercase letters '
                                                       'possessing $180^\\circ$ rotational '
                                                       'symmetry are H, I, N, O, S, X, and Z. '
                                                       'Turning any of these letters upside down '
                                                       'results in the exact same letter. Choice A '
                                                       'contains letters with vertical reflection '
                                                       "symmetry (turning upside down reverses 'M' "
                                                       "into 'W' and inverts 'A'). Choice B "
                                                       'contains letters with horizontal '
                                                       'reflection symmetry. Choice D contains '
                                                       'asymmetric letters with neither '
                                                       'reflectional nor rotational symmetry.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-16',
                                        'q': 'In Lesson 1.4 On Your Own (TE p. 67 Problem 9), a '
                                             'triangle has vertices at $(-2, 1)$, $(-5, 2)$, and '
                                             '$(-3, 6)$. After a rotation about the origin, the '
                                             'image has vertices at $(1, 2)$, $(2, 5)$, and $(6, '
                                             '3)$. Which rotation was performed?',
                                        'opts': [   '$90^\\circ$ counterclockwise rotation about '
                                                    'the origin',
                                                    '$180^\\circ$ rotation about the origin',
                                                    '$360^\\circ$ rotation about the origin',
                                                    '$90^\\circ$ clockwise rotation about the '
                                                    'origin'],
                                        'correct': 3,
                                        'hint': "Compare $(x, y) = (-2, 1)$ with its image $(x', "
                                                "y') = (1, 2)$. How do the positions and signs of "
                                                '$x$ and $y$ relate?',
                                        'explanation': 'Testing preimage point $(-2, 1)$ against '
                                                       'image $(1, 2)$: The original $y$-value '
                                                       "($1$) becomes the new $x'$-value, and the "
                                                       'opposite of the original $x$-value ($-(-2) '
                                                       "= 2$) becomes the new $y'$-value. This "
                                                       'matches the algebraic rule $(x, y) \\to '
                                                       '(y, -x)$. Checking the other vertices '
                                                       'confirms this rule: $(-5, 2) \\to (2, '
                                                       '-(-5)) = (2, 5)$ and $(-3, 6) \\to (6, '
                                                       '-(-3)) = (6, 3)$. The rule $(x, y) \\to '
                                                       '(y, -x)$ represents a $90^\\circ$ '
                                                       'clockwise rotation about the origin (or '
                                                       '$270^\\circ$ counterclockwise). Choice A '
                                                       'is $90^\\circ$ counterclockwise, which '
                                                       'follows $(-y, x)$ and would yield $(-1, '
                                                       '-2)$. Choice B is $180^\\circ$, which '
                                                       'follows $(-x, -y)$ and would yield $(2, '
                                                       '-1)$. Choice C is $360^\\circ$, which '
                                                       'leaves coordinates unchanged.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-17',
                                        'q': 'In Lesson 1.4 (TE p. 67 Problem 10), a shape is '
                                             'first rotated by the rule $(x, y) \\to (y, -x)$, and '
                                             'then the resulting image is rotated by the rule $(x, '
                                             'y) \\to (-x, -y)$. Which single transformation maps '
                                             'the original preimage directly to the final image?',
                                        'opts': [   'A $90^\\circ$ counterclockwise rotation about '
                                                    'the origin: $(x, y) \\to (-y, x)$',
                                                    'A $90^\\circ$ clockwise rotation about the '
                                                    'origin: $(x, y) \\to (y, -x)$',
                                                    'A $180^\\circ$ rotation about the origin: '
                                                    '$(x, y) \\to (-x, -y)$',
                                                    'A $360^\\circ$ rotation about the origin: '
                                                    '$(x, y) \\to (x, y)$'],
                                        'correct': 0,
                                        'hint': 'Track what happens to the coordinates '
                                                'step-by-step: first $(x, y) \\to (y, -x)$, then '
                                                'apply the second rule $(-x, -y)$ to the '
                                                'intermediate coordinates $(y, -x)$.',
                                        'explanation': 'Let us compose the two rules step-by-step: '
                                                       'Step 1 applies $(x, y) \\to (y, -x)$ (a '
                                                       '$90^\\circ$ clockwise rotation). Step 2 '
                                                       'applies $(-x, -y)$ (a $180^\\circ$ '
                                                       'rotation), which negates both components '
                                                       'of the intermediate pair: $(y, -x) \\to '
                                                       '(-y, -(-x)) = (-y, x)$. The resulting '
                                                       'composite rule is $(x, y) \\to (-y, x)$, '
                                                       'which is a $90^\\circ$ counterclockwise '
                                                       'rotation about the origin. Geometrically, '
                                                       'rotating $90^\\circ$ clockwise '
                                                       '($-90^\\circ$) followed by $180^\\circ$ '
                                                       'yields $-90^\\circ + 180^\\circ = '
                                                       '+90^\\circ$ (or $90^\\circ$ '
                                                       'counterclockwise). Choices B, C, and D do '
                                                       'not match the composite mapping rule.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-18',
                                        'q': 'In HMH Into Math Lesson 1.4 Check Understanding (TE '
                                             'p. 65 Problem 1), Antoine and Bobby each rotated a '
                                             'pentagon about Point $P$, but got different results. '
                                             "Bobby's transformed pentagon has the exact same "
                                             'orientation (sides remain parallel to the original '
                                             'directions and it points upward like the preimage). '
                                             "Antoine's transformed pentagon turned so that its "
                                             'top vertex now points to the right. Which student '
                                             'performed a correct rotation?',
                                        'opts': [   'Bobby, because rigid motions must keep all '
                                                    'corresponding sides parallel to their '
                                                    'preimages.',
                                                    'Antoine, because rotating around a point '
                                                    'turns the figure and changes the direction it '
                                                    'faces; Bobby performed a translation.',
                                                    'Both students performed valid rotations of '
                                                    'different angles about Point $P$.',
                                                    'Neither student is correct, because Point $P$ '
                                                    'must be the origin $(0, 0)$.'],
                                        'correct': 1,
                                        'hint': 'What is the key visual difference between sliding '
                                                'a figure (translation) and turning a figure '
                                                'around a pivot point (rotation)?',
                                        'explanation': 'As stated in the Into Math Teacher Edition '
                                                       "(p. 65 Check Understanding 1): 'Antoine’s "
                                                       'rotation is correct. Bobby appears to have '
                                                       "performed a translation.' In a rotation, "
                                                       'all points travel along circular arcs '
                                                       'around the center of rotation, which '
                                                       'alters the direction the figure faces. '
                                                       'Bobby merely slid the figure without '
                                                       'turning it, which is the definition of a '
                                                       'translation. Choice A is incorrect because '
                                                       'rotations do not keep sides parallel to '
                                                       'their preimages (except for $180^\\circ$ '
                                                       'rotations). Choice D is incorrect because '
                                                       'any point in the plane can serve as a '
                                                       'center of rotation.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-19',
                                        'q': 'A student attempts to rotate the point $M(4, -3)$ by '
                                             '$90^\\circ$ counterclockwise about the origin, but '
                                             "writes the image coordinates as $M'(-4, -3)$. What "
                                             'error did the student commit?',
                                        'opts': [   'The student correctly applied the $90^\\circ$ '
                                                    'counterclockwise rotation rule.',
                                                    'The student performed a $180^\\circ$ rotation '
                                                    'about the origin.',
                                                    'The student performed a $90^\\circ$ clockwise '
                                                    'rotation instead of counterclockwise.',
                                                    'The student only negated the $x$-coordinate, '
                                                    'producing a reflection across the $y$-axis '
                                                    'instead of swapping the coordinates and '
                                                    'negating $y$ via $(x, y) \\to (-y, x)$.'],
                                        'correct': 3,
                                        'hint': 'Recall the $90^\\circ$ counterclockwise rule: '
                                                '$(x, y) \\to (-y, x)$. Did the student swap the '
                                                '$x$ and $y$ values?',
                                        'explanation': 'The correct rule for a $90^\\circ$ '
                                                       'counterclockwise rotation is $(x, y) \\to '
                                                       '(-y, x)$. For $M(4, -3)$, the correct '
                                                       "image is $M'(-(-3), 4) = M'(3, 4)$. The "
                                                       'student wrote $(-4, -3)$, which kept the '
                                                       'coordinates in their original positions '
                                                       'and only negated $x$: $(x, y) \\to (-x, '
                                                       'y)$. This is a reflection across the '
                                                       '$y$-axis, not a rotation. The student '
                                                       'forgot to swap the coordinates. Choice B '
                                                       '($180^\\circ$ rotation) would result in '
                                                       '$(-4, 3)$. Choice C ($90^\\circ$ clockwise '
                                                       'rotation) would result in $(-3, -4)$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'},
                                    {   'id': 'p-1-4-mcq-20',
                                        'q': 'In Lesson 1.4 Test Prep (TE p. 69 Problem 6), '
                                             'triangle $MNP$ is rotated about vertex $P$ to '
                                             'produce triangle $PQR$. Which of the following '
                                             'geometric properties MUST be true regarding vertex '
                                             '$P$ and the transformation?',
                                        'opts': [   'Vertex $P$ must move according to the '
                                                    'coordinate origin rule $(x, y) \\to (-y, x)$.',
                                                    'The area of $\\triangle PQR$ is cut in half '
                                                    'because one vertex is pinned at the center.',
                                                    "Vertex $P$ remains at its exact location ($P' "
                                                    '= P$) because it is the center of rotation, '
                                                    'and side lengths and angle measures are '
                                                    'preserved.',
                                                    'The orientation of the vertices reverses from '
                                                    'clockwise to counterclockwise.'],
                                        'correct': 2,
                                        'hint': 'The center of rotation does not move during a '
                                                'rotation, and rotations are rigid motions.',
                                        'explanation': 'When a figure is rotated about one of its '
                                                       'own vertices (Point $P$), that vertex '
                                                       'serves as the center of rotation and is a '
                                                       'fixed point: its image coincides with '
                                                       "itself ($P' = P$). Furthermore, because "
                                                       'rotation is a rigid motion, all side '
                                                       'lengths, angle measures, and areas are '
                                                       'strictly preserved '
                                                       '($\\text{Area}(\\triangle PQR) = '
                                                       '\\text{Area}(\\triangle MNP)$), and vertex '
                                                       'orientation is preserved. Choice A '
                                                       'incorrectly applies an origin-centered '
                                                       'rule to a vertex-centered rotation. Choice '
                                                       'B falsely claims area changes. Choice D '
                                                       'confuses rotations with reflections (which '
                                                       'reverse orientation).',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3'}],
                        'fitb': [   {   'id': 'p-1-4-f1',
                                        'q': 'Rotate point M(-2, 5) 90° clockwise about the '
                                             "origin. Enter image M' as (x, y):",
                                        'expected': '(5, 2)',
                                        'altExpected': ['(5,2)', '5, 2', '5,2'],
                                        'hint': 'Rule is (x, y) → (y, -x). y becomes first, and -x '
                                                'is -(-2) = 2.'},
                                    {   'id': 'p-1-4-f2',
                                        'q': 'Point T(6, 8) is rotated 270° clockwise about the '
                                             "origin. Enter image T' as (x, y):",
                                        'expected': '(-8, 6)',
                                        'altExpected': ['(-8,6)', '-8, 6', '-8,6'],
                                        'hint': '270° CW is the same as 90° CCW: (x, y) → (-y, '
                                                'x).'}]},
        'bookQuestions': [   {   'num': 'HMH Into Math • Section 1.4 Problem 6',
                                 'q': 'A student rotates \\(P(3, -4)\\) 90° clockwise and writes '
                                      "\\(P'(-4, 3)\\). Identify and correct the student's error.",
                                 'modelAnswer': '<strong>Model Answer:</strong> The student '
                                                'swapped the coordinates to \\((-4, 3)\\) but '
                                                'forgot to negate the new y-coordinate! The rule '
                                                'for 90° clockwise is \\((x, y) \\to (y, -x)\\). '
                                                'For \\((3, -4)\\), the new x is \\(-4\\) and the '
                                                'new y is \\(-(3) = -3\\). The correct image is '
                                                "\\(P'(-4, -3)\\)."},
                             {   'num': 'HMH Into Math • Section 1.4 Problem 14',
                                 'q': 'Explain why a 180° clockwise rotation and a 180° '
                                      'counterclockwise rotation produce the exact same image.',
                                 'modelAnswer': '<strong>Model Answer:</strong> Since a complete '
                                                'circle is 360°, rotating 180° in either direction '
                                                'covers exactly half of the circle. Algebraically, '
                                                'both rules map \\((x, y) \\to (-x, -y)\\). '
                                                'Because the algebraic rules and terminal '
                                                'positions are identical, direction does not '
                                                'matter for 180° rotations.'}]},
    {   'id': '1.5',
        'modId': 'mod1',
        'modNum': 1,
        'modTitle': 'Transformations and Congruence',
        'themeColor': '#4f46e5',
        'badge': 'Module 1 • Lesson 1.5',
        'num': '1.5',
        'title': 'Understand and Recognize Congruent Figures',
        'tag': 'Sequences & Congruence Proofs',
        'standard': 'CCSS.MATH.CONTENT.8.G.A.2',
        'canDo': 'I can prove whether two figures are congruent by discovering and writing the '
                 'precise sequence of rigid motions (translations, reflections, rotations) that '
                 'maps one onto the other.',
        'conceptIntro': '<strong>The Fundamental Congruence Theorem:</strong> Two two-dimensional '
                        'geometric figures are <strong>congruent (\\(\\cong\\))</strong> if and '
                        'only if there exists a sequence of rigid motions that maps the first '
                        'figure directly onto the second figure. When figures are congruent, all '
                        'corresponding side lengths are equal, all corresponding angles are equal, '
                        'and perimeter and area are identical.',
        'rules': [   {   'name': 'Definition of Congruence',
                         'formula': '\\triangle ABC \\cong \\triangle DEF \\iff \\text{Rigid '
                                    'Sequence maps } ABC \\to DEF',
                         'desc': 'Existence of a rigid motion sequence is the exact mathematical '
                                 'proof of congruence.'},
                     {   'name': 'Corresponding Parts Property',
                         'formula': 'AB = DE, BC = EF, AC = DF \\text{ and } \\angle A \\cong '
                                    '\\angle D, \\angle B \\cong \\angle E, \\angle C \\cong '
                                    '\\angle F',
                         'desc': 'Corresponding Parts of Congruent Figures are Congruent '
                                 '(CPCTC).'}],
        'vocab': [   {   'term': 'Congruent Figures (\\(\\cong\\))',
                         'def': 'Figures that have the exact same size and shape.',
                         'ex': 'Two identical puzzle pieces.'},
                     {   'term': 'Sequence of Transformations',
                         'def': 'Performing two or more transformations in succession.',
                         'ex': 'Translate 3 units right, then reflect across the x-axis.'},
                     {   'term': 'Glide Reflection',
                         'def': 'A composition consisting of a translation along a line followed '
                                'by a reflection across that same line.',
                         'ex': 'Footprint patterns in sand.'}],
        'invariance': [   {'prop': 'All Side Lengths', 'status': '✓ 100% Equal', 'cls': 'yes'},
                          {'prop': 'All Angle Measures', 'status': '✓ 100% Equal', 'cls': 'yes'},
                          {'prop': 'Perimeter & Area', 'status': '✓ Identical', 'cls': 'yes'},
                          {'prop': 'Shape & Size', 'status': '✓ Identical', 'cls': 'yes'}],
        'illustrativeExamples': [   {   'title': 'Example 1: Identifying Congruence via Sequence',
                                        'desc': 'Figure 1 is in Quadrant II. Figure 2 is in '
                                                'Quadrant IV, turned upside down. Can they be '
                                                'congruent?',
                                        'analysis': 'Yes! A 180° rotation about the origin turns a '
                                                    'shape upside down and moves it from Quadrant '
                                                    'II to Quadrant IV. Because rotation is a '
                                                    'rigid motion, Figure 1 is congruent to Figure '
                                                    '2.'},
                                    {   'title': 'Example 2: Determining Required Sequence Type',
                                        'desc': '\\(\\triangle ABC\\) has clockwise vertices. '
                                                'Image \\(\\triangle DEF\\) has counterclockwise '
                                                'vertices. What type of transformation MUST be '
                                                'included in the sequence?',
                                        'analysis': 'Because the orientation changed from '
                                                    'clockwise to counterclockwise, the sequence '
                                                    '<strong>must contain at least one '
                                                    'reflection</strong> (or an odd number of '
                                                    'reflections) to reverse orientation.'}],
        'workedExample': {   'title': 'Worked Example: Writing a Two-Step Congruence Proof',
                             'problem': '\\(\\triangle ABC\\) has vertices \\(A(1, 1)\\), \\(B(4, '
                                        '1)\\), \\(C(1, 5)\\). \\(\\triangle DEF\\) has vertices '
                                        '\\(D(-1, -1)\\), \\(E(-1, -4)\\), \\(F(-5, -1)\\). Prove '
                                        'whether \\(\\triangle ABC \\cong \\triangle DEF\\) by '
                                        'describing a sequence of rigid motions.',
                             'step1': '<strong>Step 1: Compare side lengths:</strong> \\(AB = '
                                      '3\\), \\(AC = 4\\), \\(BC = 5\\). For \\(\\triangle DEF\\), '
                                      '\\(DE = 3\\), \\(DF = 4\\), \\(EF = 5\\). Corresponding '
                                      'sides are equal.',
                             'step2': '<strong>Step 2: Test a sequence of rigid '
                                      'transformations:</strong><br>1. Reflect \\(\\triangle '
                                      'ABC\\) across the line \\(y = -x\\): \\((x, y) \\to (-y, '
                                      '-x)\\).<br>• \\(A(1, 1) \\to (-1, -1) = D\\)<br>• \\(B(4, '
                                      '1) \\to (-1, -4) = E\\)<br>• \\(C(1, 5) \\to (-5, -1) = '
                                      'F\\).',
                             'step3': '<strong>Step 3: Formal Proof Conclusion:</strong> A '
                                      'reflection across the line \\(y = -x\\) maps \\(\\triangle '
                                      'ABC\\) directly onto \\(\\triangle DEF\\). Since reflection '
                                      'is a rigid motion, \\(\\triangle ABC \\cong \\triangle '
                                      'DEF\\).',
                             'modelAnswer': '<strong>Student Model Answer:</strong> \\(\\triangle '
                                            'ABC \\cong \\triangle DEF\\) because a reflection '
                                            'across the line \\(y = -x\\) maps each vertex \\(A, '
                                            'B, C\\) directly onto \\(D, E, F\\). Since reflection '
                                            'is a rigid motion that preserves distances and angle '
                                            'measures, the figures are congruent.'},
        'practice': {   'mcqs': [   {   'id': 'p-1-5-mcq-1',
                                        'q': 'According to the geometric definition of congruence '
                                             'based on transformations, two two-dimensional '
                                             'figures are congruent ($\\cong$) if and only if:',
                                        'opts': [   'There is a sequence of one or more rigid '
                                                    'motions (translations, reflections, '
                                                    'rotations) that maps one figure onto the '
                                                    'other.',
                                                    'One figure can be mapped onto the other using '
                                                    'a dilation with a scale factor $k > 1$.',
                                                    'Both figures have the exact same number of '
                                                    'sides, regardless of side lengths or interior '
                                                    'angle measures.',
                                                    'The figures have the same perimeter even if '
                                                    'their corresponding angle measures are '
                                                    'different.'],
                                        'correct': 0,
                                        'hint': 'Recall from Into Math Lesson 1.5 that rigid '
                                                'motions preserve both side lengths and angle '
                                                'measures without stretching, shrinking, or '
                                                'distorting.',
                                        'explanation': 'By the Common Core and HMH Into Math '
                                                       'definition (8.G.A.2), two figures are '
                                                       'congruent ($\\cong$) if and only if there '
                                                       'is a sequence of rigid motions '
                                                       '(translations, reflections, and rotations) '
                                                       'that maps one figure exactly onto the '
                                                       'other. Rigid motions preserve distance and '
                                                       'angle measure.\n'
                                                       '• Distractor B describes an enlargement '
                                                       'dilation, which changes size ($k \\neq 1$) '
                                                       'and produces similar, not congruent, '
                                                       'figures.\n'
                                                       '• Distractor C is incorrect because having '
                                                       'the same number of sides (e.g., any two '
                                                       'arbitrary triangles) does not guarantee '
                                                       'identical shape or size.\n'
                                                       '• Distractor D is incorrect because equal '
                                                       'perimeter does not guarantee congruent '
                                                       'shapes (e.g., a $3 \\times 5$ rectangle '
                                                       'and a $4 \\times 4$ square both have '
                                                       'perimeter 16, but different shapes).',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-2',
                                        'q': 'Polygon $P$ undergoes a transformation on the '
                                             'Cartesian coordinate plane. Which resulting polygon '
                                             'is **guaranteed** to be congruent to Polygon $P$ ($P '
                                             '\\cong \\text{Image}$)? ',
                                        'opts': [   'Polygon $Q$ formed by multiplying all '
                                                    'coordinates by $1.5$: $(x, y) \\to (1.5x, '
                                                    '1.5y)$',
                                                    'Polygon $R$ formed by a horizontal stretch: '
                                                    '$(x, y) \\to (3x, y)$',
                                                    'Polygon $S$ formed by a $90^\\circ$ '
                                                    'counterclockwise rotation followed by a '
                                                    'translation 6 units left: $(x, y) \\to (-y - '
                                                    '6, x)$',
                                                    'Polygon $T$ formed by adding 4 to $x$ while '
                                                    'multiplying $y$ by $0.5$: $(x, y) \\to (x + '
                                                    '4, 0.5y)$'],
                                        'correct': 2,
                                        'hint': 'Identify which operation is a composition '
                                                'composed purely of rigid motions (isometries) '
                                                'that preserve distances between all pairs of '
                                                'points.',
                                        'explanation': 'Rotations and translations are rigid '
                                                       'motions. Any sequence consisting solely of '
                                                       'rigid motions preserves all distances and '
                                                       'angle measures, guaranteeing that the '
                                                       'image is congruent to the preimage ($P '
                                                       '\\cong S$). A $90^\\circ$ rotation '
                                                       'counterclockwise maps $(x, y) \\to (-y, '
                                                       'x)$, and a translation 6 units left maps '
                                                       'that to $(-y - 6, x)$.\n'
                                                       '• Distractor A is a dilation by scale '
                                                       'factor $1.5$, which increases side lengths '
                                                       'by $50\\%$.\n'
                                                       '• Distractor B triples the horizontal '
                                                       'dimension, distorting the shape.\n'
                                                       '• Distractor D compresses the vertical '
                                                       'dimension by half ($0.5y$), destroying '
                                                       'congruence.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-3',
                                        'q': 'Given the formal congruence statement $\\triangle '
                                             'MNP \\cong \\triangle STW$, which pair of '
                                             'corresponding parts **must** be congruent?',
                                        'opts': [   'Side $MN \\cong \\text{side } TW$ and '
                                                    '$\\angle P \\cong \\angle S$',
                                                    'Side $NP \\cong \\text{side } TW$ and '
                                                    '$\\angle M \\cong \\angle S$',
                                                    'Side $MP \\cong \\text{side } ST$ and '
                                                    '$\\angle N \\cong \\angle W$',
                                                    'Side $MN \\cong \\text{side } SW$ and '
                                                    '$\\angle P \\cong \\angle T$'],
                                        'correct': 1,
                                        'hint': 'In a congruence statement, vertices are written '
                                                'in exact matching order: 1st to 1st ($M '
                                                '\\leftrightarrow S$), 2nd to 2nd ($N '
                                                '\\leftrightarrow T$), and 3rd to 3rd ($P '
                                                '\\leftrightarrow W$).',
                                        'explanation': 'The order of vertices in a congruence '
                                                       'statement defines the one-to-one '
                                                       'correspondence:\n'
                                                       '• 1st vertex: $M \\leftrightarrow S$\n'
                                                       '• 2nd vertex: $N \\leftrightarrow T$\n'
                                                       '• 3rd vertex: $P \\leftrightarrow W$\n'
                                                       'Therefore, side $NP$ (vertices 2 and 3) '
                                                       'corresponds to side $TW$ (vertices 2 and '
                                                       '3), and $\\angle M$ (vertex 1) corresponds '
                                                       'to $\\angle S$ (vertex 1). Hence, side $NP '
                                                       '\\cong \\text{side } TW$ and $\\angle M '
                                                       '\\cong \\angle S$.\n'
                                                       '• Distractor A mismatches side $MN$ (1-2) '
                                                       'with $TW$ (2-3) and $\\angle P$ (3) with '
                                                       '$\\angle S$ (1).\n'
                                                       '• Distractor C mismatches side $MP$ (1-3) '
                                                       'with $ST$ (1-2) and $\\angle N$ (2) with '
                                                       '$\\angle W$ (3).\n'
                                                       '• Distractor D mismatches side $MN$ (1-2) '
                                                       'with $SW$ (1-3) and $\\angle P$ (3) with '
                                                       '$\\angle T$ (2).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-4',
                                        'q': 'Triangle $\\triangle ABC$ has vertices $A(1, 2)$, '
                                             '$B(4, 2)$, and $C(1, 6)$. It is reflected across the '
                                             '$y$-axis to produce an image with vertices $X(-1, '
                                             '2)$, $Y(-4, 2)$, and $Z(-1, 6)$, where $A$ maps to '
                                             '$X$, $B$ maps to $Y$, and $C$ maps to $Z$. Which '
                                             'congruence statement correctly expresses this '
                                             'relationship?',
                                        'opts': [   '$\\triangle ABC \\cong \\triangle YXZ$',
                                                    '$\\triangle ABC \\cong \\triangle ZYX$',
                                                    '$\\triangle ABC \\cong \\triangle YZX$',
                                                    '$\\triangle ABC \\cong \\triangle XYZ$'],
                                        'correct': 3,
                                        'hint': 'Match each letter in the preimage to its specific '
                                                'reflection image: $A(1, 2) \\to X(-1, 2)$, $B(4, '
                                                '2) \\to Y(-4, 2)$, $C(1, 6) \\to Z(-1, 6)$.',
                                        'explanation': 'Under reflection across the $y$-axis, $(x, '
                                                       'y) \\to (-x, y)$:\n'
                                                       '• $A(1, 2) \\to X(-1, 2)$, so $A '
                                                       '\\leftrightarrow X$\n'
                                                       '• $B(4, 2) \\to Y(-4, 2)$, so $B '
                                                       '\\leftrightarrow Y$\n'
                                                       '• $C(1, 6) \\to Z(-1, 6)$, so $C '
                                                       '\\leftrightarrow Z$\n'
                                                       'A congruence statement must write matching '
                                                       'vertices in the exact same positional '
                                                       'sequence. Therefore, $\\triangle ABC '
                                                       '\\cong \\triangle XYZ$ is the only '
                                                       'correctly ordered statement.\n'
                                                       '• Distractors A, B, and C place the '
                                                       'vertices out of correspondence.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-5',
                                        'q': 'If $\\triangle DEF \\cong \\triangle JKL$, with '
                                             '$m\\angle D = 43^\\circ$, $m\\angle E = 79^\\circ$, '
                                             'side $DE = 6.8\\text{ cm}$, and side $EF = '
                                             '9.2\\text{ cm}$, what are the measure of $\\angle L$ '
                                             'and the length of side $JK$?',
                                        'opts': [   '$m\\angle L = 58^\\circ$ and $JK = 6.8\\text{ '
                                                    'cm}$',
                                                    '$m\\angle L = 43^\\circ$ and $JK = 9.2\\text{ '
                                                    'cm}$',
                                                    '$m\\angle L = 79^\\circ$ and $JK = 6.8\\text{ '
                                                    'cm}$',
                                                    '$m\\angle L = 58^\\circ$ and $JK = 9.2\\text{ '
                                                    'cm}$'],
                                        'correct': 0,
                                        'hint': 'Use the triangle angle sum ($180^\\circ$) to '
                                                'calculate $m\\angle F$ first. Then use CPCTC: '
                                                '$\\angle L \\cong \\angle F$ and side $JK \\cong '
                                                '\\text{side } DE$.',
                                        'explanation': 'Step 1: Find the missing angle measure in '
                                                       '$\\triangle DEF$ using the Triangle Angle '
                                                       'Sum Theorem:\n'
                                                       '$$m\\angle F = 180^\\circ - (43^\\circ + '
                                                       '79^\\circ) = 180^\\circ - 122^\\circ = '
                                                       '58^\\circ$$\n'
                                                       'Step 2: By CPCTC (Corresponding Parts of '
                                                       'Congruent Triangles are Congruent):\n'
                                                       '• Vertex $F$ corresponds to vertex $L$, so '
                                                       '$m\\angle L = m\\angle F = 58^\\circ$.\n'
                                                       '• Side $DE$ (vertices 1-2) corresponds to '
                                                       'side $JK$ (vertices 1-2), so $JK = DE = '
                                                       '6.8\\text{ cm}$.\n'
                                                       '• Distractor B incorrectly equates '
                                                       '$\\angle L$ with $\\angle D$ and $JK$ with '
                                                       '$EF$.\n'
                                                       '• Distractor C incorrectly equates '
                                                       '$\\angle L$ with $\\angle E$.\n'
                                                       '• Distractor D gets the angle right '
                                                       '($58^\\circ$) but mistakenly pairs $JK$ '
                                                       'with $EF$ ($9.2\\text{ cm}$).',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-6',
                                        'q': 'Quadrilaterals $ABCD$ and $EFGH$ are congruent '
                                             '($ABCD \\cong EFGH$). If side $BC = 4x - 7$ and '
                                             'corresponding side $FG = 2x + 9$, what is the actual '
                                             'numerical length of side $FG$?',
                                        'opts': [   '$x = 8$, so $FG = 17$',
                                                    '$x = 1$, so $FG = 11$',
                                                    '$x = 8$, so $FG = 25$',
                                                    '$x = 16$, so $FG = 41$'],
                                        'correct': 2,
                                        'hint': 'Corresponding sides of congruent figures have '
                                                'equal lengths. Set $4x - 7 = 2x + 9$ to solve for '
                                                '$x$, then substitute $x$ into $2x + 9$.',
                                        'explanation': 'Step 1: Set the lengths of corresponding '
                                                       'sides equal because $ABCD \\cong EFGH$ '
                                                       'implies $BC = FG$:\n'
                                                       '$$4x - 7 = 2x + 9$$\n'
                                                       'Step 2: Solve the linear equation for '
                                                       '$x$:\n'
                                                       '$$4x - 2x = 9 + 7 \\implies 2x = 16 '
                                                       '\\implies x = 8$$\n'
                                                       'Step 3: Substitute $x = 8$ back into the '
                                                       'expression for $FG$:\n'
                                                       '$$FG = 2(8) + 9 = 16 + 9 = 25$$\n'
                                                       '(Check: $BC = 4(8) - 7 = 32 - 7 = 25$, '
                                                       'confirming $BC = FG$).\n'
                                                       '• Distractor A solves $x = 8$ correctly '
                                                       'but subtracts 8 from 25 or miscalculates '
                                                       '$2(8) + 1$.\n'
                                                       '• Distractor B makes a sign error when '
                                                       'moving terms ($4x - 2x = 9 - 7 \\implies '
                                                       '2x = 2 \\implies x = 1$).\n'
                                                       '• Distractor D forgets to divide 16 by 2 '
                                                       'when solving $2x = 16$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-7',
                                        'q': 'A polygon vertex located at $P(-3, 5)$ undergoes a '
                                             'two-step sequence of rigid motions:\n'
                                             '• **Step 1:** Reflection across the $x$-axis.\n'
                                             '• **Step 2:** Translation by the vector rule $(x, y) '
                                             '\\to (x + 7, y - 2)$.\n'
                                             'What are the coordinates of the final image point '
                                             "$P''$?",
                                        'opts': [   '$(4, 3)$',
                                                    '$(4, -7)$',
                                                    '$(-10, -7)$',
                                                    '$(4, -3)$'],
                                        'correct': 1,
                                        'hint': 'Apply the transformations in order: first reflect '
                                                'across the $x$-axis: $(x, y) \\to (x, -y)$, then '
                                                'apply the translation to the resulting '
                                                'coordinates.',
                                        'explanation': 'Step 1 (Reflection across $x$-axis): The '
                                                       'rule is $(x, y) \\to (x, -y)$.\n'
                                                       "$$P(-3, 5) \\to P'(-3, -5)$$\n"
                                                       'Step 2 (Translation $(x + 7, y - 2)$):\n'
                                                       "$$P'(-3, -5) \\to P''(-3 + 7, -5 - 2) = "
                                                       "P''(4, -7)$$\n"
                                                       '• Distractor A translates the original '
                                                       'point $P(-3, 5)$ directly without '
                                                       'reflecting: $(-3 + 7, 5 - 2) = (4, 3)$.\n'
                                                       '• Distractor C subtracts 7 from $x$ '
                                                       'instead of adding: $(-3 - 7, -5 - 2) = '
                                                       '(-10, -7)$.\n'
                                                       '• Distractor D reflects across the '
                                                       '$y$-axis first instead of the $x$-axis: '
                                                       '$(3, 5) \\to (3 + 7, 5 - 2) = (10, 3)$ or '
                                                       'miscalculates $-5 - 2$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-8',
                                        'q': 'In HMH Into Math Lesson 1.5 Task 3, students '
                                             'investigate whether the order of transformations '
                                             'matters. Starting with the point $A(2, 5)$:\n'
                                             '• **Order 1:** Reflect across the $y$-axis, then '
                                             'translate 3 units right.\n'
                                             '• **Order 2:** Translate 3 units right, then reflect '
                                             'across the $y$-axis.\n'
                                             'What are the resulting coordinates for Order 1 and '
                                             'Order 2, and what key geometric principle does this '
                                             'prove?',
                                        'opts': [   'Order 1 produces $(1, 5)$; Order 2 produces '
                                                    '$(1, 5)$. This proves that the order of '
                                                    'transformations never matters.',
                                                    'Order 1 produces $(-5, 5)$; Order 2 produces '
                                                    '$(5, 5)$. This proves that reflecting across '
                                                    'an axis doubles distance.',
                                                    'Order 1 produces $(-1, 5)$; Order 2 produces '
                                                    '$(-5, 5)$. This proves that the figures cease '
                                                    'to be congruent.',
                                                    'Order 1 produces $(1, 5)$; Order 2 produces '
                                                    '$(-5, 5)$. This proves that transformation '
                                                    'composition is non-commutative (order '
                                                    'matters).'],
                                        'correct': 3,
                                        'hint': 'Calculate the coordinates for each order '
                                                'separately. For Order 1: reflect across $y$-axis '
                                                'first, then add 3 to $x$. For Order 2: add 3 to '
                                                '$x$ first, then reflect across $y$-axis.',
                                        'explanation': 'Order 1:\n'
                                                       '1. Reflect $A(2, 5)$ across the $y$-axis: '
                                                       "$(x, y) \\to (-x, y) \\implies A'(-2, "
                                                       '5)$.\n'
                                                       '2. Translate 3 units right: $(-2 + 3, 5) = '
                                                       '(1, 5)$.\n'
                                                       'Order 2:\n'
                                                       '1. Translate $A(2, 5)$ 3 units right: $(2 '
                                                       '+ 3, 5) = (5, 5)$.\n'
                                                       '2. Reflect $(5, 5)$ across the $y$-axis: '
                                                       '$(x, y) \\to (-x, y) \\implies (-5, 5)$.\n'
                                                       'Because $(1, 5) \\neq (-5, 5)$, the order '
                                                       'in which transformations are performed '
                                                       'affects the final position. This '
                                                       'demonstrates that transformation '
                                                       'composition is generally non-commutative '
                                                       '($T_2 \\circ T_1 \\neq T_1 \\circ T_2$).\n'
                                                       '• Distractor A incorrectly claims that '
                                                       'order never matters.\n'
                                                       '• Distractor B has incorrect coordinates '
                                                       'for Order 1.\n'
                                                       '• Distractor C incorrectly claims the '
                                                       'figures are no longer congruent; rigid '
                                                       'motions always preserve congruence even '
                                                       'when landing at different locations.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-9',
                                        'q': 'In transformational geometry, what is the precise '
                                             'definition of a **glide reflection** mapping a '
                                             "geometric figure $F$ onto its congruent image $F'$ "
                                             "($F \\cong F'$)? ",
                                        'opts': [   'A sequence consisting of a translation along '
                                                    'a line followed by a reflection across that '
                                                    'same line (or a line parallel to the '
                                                    'translation direction).',
                                                    'A reflection across a line followed by a '
                                                    'rotation of $180^\\circ$ about a point on '
                                                    'that line.',
                                                    'A translation followed by an enlargement '
                                                    'dilation with scale factor $k = 1.5$.',
                                                    'Two consecutive reflections across two '
                                                    'perpendicular coordinate axes that produce a '
                                                    'half-turn.'],
                                        'correct': 0,
                                        'hint': 'Think of footprints left by walking in wet sand: '
                                                'one foot steps forward (translation) and reflects '
                                                'across the centerline.',
                                        'explanation': 'A **glide reflection** is defined as the '
                                                       'composition of a translation (the glide) '
                                                       'and a reflection across a line that is '
                                                       'parallel to the direction of translation '
                                                       '(or along the line of translation itself). '
                                                       'Because both translations and reflections '
                                                       'are isometries, a glide reflection is an '
                                                       'isometry that reverses orientation.\n'
                                                       '• Distractor B describes a reflection '
                                                       'combined with a rotation, not a glide '
                                                       'reflection.\n'
                                                       '• Distractor C includes a dilation, which '
                                                       'alters size and is non-rigid.\n'
                                                       '• Distractor D describes reflections '
                                                       'across intersecting perpendicular lines, '
                                                       'which is equivalent to a $180^\\circ$ '
                                                       'rotation, not a glide reflection.',
                                        'dok': 1,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-10',
                                        'q': 'Triangle $\\triangle ABC$ has vertices $A(1, 2)$, '
                                             '$B(4, 2)$, and $C(1, 5)$. It undergoes a glide '
                                             'reflection composed of:\n'
                                             '1. A translation by the rule $(x, y) \\to (x + 3, '
                                             'y)$\n'
                                             '2. A reflection across the $x$-axis ($y = 0$).\n'
                                             'What are the vertices of the image triangle '
                                             "$\\triangle A''B''C''$?",
                                        'opts': [   "$A''(4, 2), B''(7, 2), C''(4, 5)$",
                                                    "$A''(-4, -2), B''(-7, -2), C''(-4, -5)$",
                                                    "$A''(4, -2), B''(7, -2), C''(4, -5)$",
                                                    "$A''(1, -5), B''(4, -5), C''(1, -8)$"],
                                        'correct': 2,
                                        'hint': 'First add 3 to each $x$-coordinate: $(x + 3, y)$. '
                                                'Then reflect across the $x$-axis by negating each '
                                                '$y$-coordinate: $(x, -y)$.',
                                        'explanation': 'Step 1: Translate $(x, y) \\to (x + 3, '
                                                       'y)$:\n'
                                                       "• $A(1, 2) \\to A'(1 + 3, 2) = (4, 2)$\n"
                                                       "• $B(4, 2) \\to B'(4 + 3, 2) = (7, 2)$\n"
                                                       "• $C(1, 5) \\to C'(1 + 3, 5) = (4, 5)$\n"
                                                       'Step 2: Reflect across the $x$-axis: $(x, '
                                                       'y) \\to (x, -y)$:\n'
                                                       "• $A'(4, 2) \\to A''(4, -2)$\n"
                                                       "• $B'(7, 2) \\to B''(7, -2)$\n"
                                                       "• $C'(4, 5) \\to C''(4, -5)$\n"
                                                       '• Distractor A performs only the '
                                                       'translation and forgets the reflection.\n'
                                                       '• Distractor B incorrectly negates the '
                                                       '$x$-coordinates as well.\n'
                                                       '• Distractor D applies the translation to '
                                                       '$y$ instead of $x$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-11',
                                        'q': 'In HMH Into Math Lesson 1.5 On Your Own Problem 3, '
                                             'students are asked: "Can a square with side length '
                                             '$s_1$ ever be congruent to a regular pentagon with '
                                             'side length $s_2$? Explain."\n'
                                             'Which response provides the mathematically correct '
                                             'explanation?',
                                        'opts': [   'Yes, as long as both polygons are scaled so '
                                                    'that their perimeters are equal.',
                                                    'No, because congruent figures must have the '
                                                    'exact same size and shape. A square has 4 '
                                                    'sides and four $90^\\circ$ angles, while a '
                                                    'regular pentagon has 5 sides and five '
                                                    '$108^\\circ$ angles; no sequence of rigid '
                                                    'motions can change the number of sides or '
                                                    'angle measures.',
                                                    'Yes, because a square can be transformed into '
                                                    'a pentagon by a sequence of a reflection '
                                                    'followed by a dilation with scale factor $k = '
                                                    '\\frac{5}{4}$.',
                                                    'No, because squares are two-dimensional '
                                                    'planar figures while pentagons are '
                                                    'three-dimensional polyhedra.'],
                                        'correct': 1,
                                        'hint': 'Consider the invariance properties of rigid '
                                                'motions: rigid motions preserve the number of '
                                                'vertices, side lengths, and angle measures.',
                                        'explanation': 'Congruent figures must have identical '
                                                       'shape and size. A square has 4 vertices, 4 '
                                                       'sides, and interior angles of $90^\\circ$. '
                                                       'A regular pentagon has 5 vertices, 5 '
                                                       'sides, and interior angles of '
                                                       '$108^\\circ$. Because rigid motions '
                                                       'preserve the number of sides and the '
                                                       'measures of all angles, no sequence of '
                                                       'translations, reflections, and rotations '
                                                       'can map a 4-sided polygon onto a 5-sided '
                                                       'polygon.\n'
                                                       '• Distractor A is false; having equal '
                                                       'perimeters does not make different shapes '
                                                       'congruent.\n'
                                                       '• Distractor C is false; dilations are not '
                                                       'rigid motions, and dilating a square '
                                                       'cannot add a fifth side.\n'
                                                       '• Distractor D is false; both squares and '
                                                       'pentagons are two-dimensional polygons.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-12',
                                        'q': 'Figure 1 is a rectangle with dimensions $4\\text{ '
                                             'cm} \\times 9\\text{ cm}$ (area $= 36\\text{ '
                                             'cm}^2$). Figure 2 is a square with dimensions '
                                             '$6\\text{ cm} \\times 6\\text{ cm}$ (area $= '
                                             '36\\text{ cm}^2$). Are Figure 1 and Figure 2 '
                                             'congruent?',
                                        'opts': [   'Yes, because both figures have the exact same '
                                                    'area of $36\\text{ cm}^2$.',
                                                    'Yes, because both figures have four '
                                                    '$90^\\circ$ interior angles.',
                                                    'No, because rigid motions cannot be performed '
                                                    'on figures that have right angles.',
                                                    'No, because their corresponding side lengths '
                                                    'are not equal ($4 \\neq 6$ and $9 \\neq 6$), '
                                                    'and rigid motions strictly preserve distance; '
                                                    'equal area alone does not establish '
                                                    'congruence.'],
                                        'correct': 3,
                                        'hint': 'Check whether rigid motions preserve side '
                                                'lengths. Can you translate, reflect, or rotate a '
                                                'side of length 4 cm so that it covers a side of '
                                                'length 6 cm without stretching?',
                                        'explanation': 'While both figures have the same area '
                                                       '($36\\text{ cm}^2$) and both have four '
                                                       'right angles, their side lengths are '
                                                       'different ($4$ and $9$ vs. $6$ and $6$). '
                                                       'Because rigid motions preserve distance '
                                                       '(segment length), any image of Figure 1 '
                                                       'must have side lengths of $4\\text{ cm}$ '
                                                       'and $9\\text{ cm}$. It is impossible to '
                                                       'map a side of length $4\\text{ cm}$ onto a '
                                                       'side of length $6\\text{ cm}$ using rigid '
                                                       'motions. Thus, Figure 1 is not congruent '
                                                       'to Figure 2.\n'
                                                       '• Distractor A is a common student trap: '
                                                       'equal area is necessary for congruence, '
                                                       'but not sufficient.\n'
                                                       '• Distractor B is incorrect because having '
                                                       'equal angles only implies similarity (for '
                                                       'certain shapes), not congruence.\n'
                                                       '• Distractor C is mathematically absurd; '
                                                       'rigid motions apply to all geometric '
                                                       'figures.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-13',
                                        'q': 'On a math critique task (HMH Into Math Problem 8), '
                                             'Nathan claims: "Figure $B$ is congruent to Figure '
                                             '$A$ because both figures have the exact same '
                                             'orientation on the grid." How should Nathan\'s '
                                             'mathematical reasoning be evaluated?',
                                        'opts': [   'Nathan is incorrect. Having the same '
                                                    'orientation is neither necessary nor '
                                                    'sufficient for congruence; two figures are '
                                                    'congruent if and only if there is a sequence '
                                                    'of rigid motions mapping one onto the other, '
                                                    'which preserves all side lengths and angle '
                                                    'measures.',
                                                    'Nathan is correct because having the same '
                                                    'orientation is the definition of congruence '
                                                    'in the coordinate plane.',
                                                    'Nathan is correct because reflections reverse '
                                                    'orientation, meaning reflected figures can '
                                                    'never be congruent.',
                                                    'Nathan is incorrect because congruent figures '
                                                    'must always have opposite orientations.'],
                                        'correct': 0,
                                        'hint': 'Can two figures face the same direction but have '
                                                'completely different sizes? Can two congruent '
                                                'figures face opposite directions?',
                                        'explanation': "Nathan's reasoning is mathematically "
                                                       'flawed on two levels:\n'
                                                       '1. Having the same orientation is not '
                                                       'sufficient: a dilated triangle can have '
                                                       'the exact same orientation as its '
                                                       'preimage, but have double the size (not '
                                                       'congruent).\n'
                                                       '2. Having the same orientation is not '
                                                       'necessary: a figure reflected across a '
                                                       'line has reversed orientation, yet it '
                                                       'remains completely congruent to its '
                                                       'preimage.\n'
                                                       'Two figures are congruent if and only if a '
                                                       'sequence of rigid motions maps one onto '
                                                       'the other.\n'
                                                       '• Distractors B, C, and D reflect common '
                                                       'student misconceptions regarding '
                                                       'orientation and congruence.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-14',
                                        'q': 'In HMH Into Math Lesson 1.5 Problem 14, Henrietta '
                                             'claims that Figure $B$ can be transformed into '
                                             'Figure $A$ by translating it 2 units right and then '
                                             'rotating it $90^\\circ$ clockwise about the origin. '
                                             "However, following Henrietta's instructions places "
                                             'the image in the wrong quadrant. How should '
                                             "Henrietta's sequence be corrected?",
                                        'opts': [   'She must replace the rotation with a dilation '
                                                    'of scale factor $k = 1$.',
                                                    'She must perform the transformations in the '
                                                    'reverse order: rotate $90^\\circ$ clockwise '
                                                    'about the origin first, and then translate '
                                                    'the resulting figure.',
                                                    'She must reflect the figure across the '
                                                    'diagonal line $y = x$ instead of rotating.',
                                                    'She must translate the figure 4 units down '
                                                    'before doing anything else.'],
                                        'correct': 1,
                                        'hint': "Check Into Math TE Page 79 Problem 14: 'The "
                                                "transformations must be done in the other order.' "
                                                'Rotating after translating swings the translation '
                                                'displacement around the origin!',
                                        'explanation': 'When a figure is translated first and then '
                                                       'rotated about the origin, the rotation '
                                                       "affects both the figure's shape "
                                                       'orientation and its entire position vector '
                                                       'relative to the origin. In Into Math '
                                                       'Lesson 1.5 Problem 14, the TE explicitly '
                                                       "notes: 'The transformations must be done "
                                                       "in the other order.' Rotating $90^\\circ$ "
                                                       'clockwise about the origin first, followed '
                                                       'by the translation, places the figure in '
                                                       'the exact location of Figure $A$.\n'
                                                       '• Distractor A is incorrect because '
                                                       'dilating by $k = 1$ is an identity '
                                                       'transformation that does not change '
                                                       'position.\n'
                                                       '• Distractors C and D suggest incorrect '
                                                       'transformation families or wrong '
                                                       'translation vectors.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-15',
                                        'q': 'Right triangle $\\triangle ABC$ has legs of length '
                                             '$5\\text{ units}$ and $12\\text{ units}$. It '
                                             'undergoes a multi-step sequence of rigid motions: a '
                                             'rotation of $90^\\circ$ clockwise about the origin, '
                                             'followed by a translation of $(x - 4, y + 6)$, and '
                                             'finally a reflection across the line $y = 3$. What '
                                             'are the perimeter and area of the final image '
                                             "triangle $\\triangle A'''B'''C'''$?",
                                        'opts': [   '$\\text{Perimeter} = 17\\text{ units}$ and '
                                                    '$\\text{Area} = 30\\text{ sq units}$',
                                                    '$\\text{Perimeter} = 30\\text{ units}$ and '
                                                    '$\\text{Area} = 60\\text{ sq units}$',
                                                    '$\\text{Perimeter} = 30\\text{ units}$ and '
                                                    '$\\text{Area} = 30\\text{ sq units}$',
                                                    '$\\text{Perimeter} = 60\\text{ units}$ and '
                                                    '$\\text{Area} = 30\\text{ sq units}$'],
                                        'correct': 2,
                                        'hint': 'Find the hypotenuse using the Pythagorean '
                                                'theorem: $c = \\sqrt{5^2 + 12^2}$. Then recall '
                                                'that rigid motions preserve both perimeter and '
                                                'area.',
                                        'explanation': 'Step 1: Compute the hypotenuse and '
                                                       'measurements of the preimage $\\triangle '
                                                       'ABC$:\n'
                                                       '$$c = \\sqrt{5^2 + 12^2} = \\sqrt{25 + '
                                                       '144} = \\sqrt{169} = 13\\text{ units}$$\n'
                                                       '$$\\text{Perimeter} = 5 + 12 + 13 = '
                                                       '30\\text{ units}$$\n'
                                                       '$$\\text{Area} = \\frac{1}{2} \\times '
                                                       '\\text{base} \\times \\text{height} = '
                                                       '\\frac{1}{2}(5)(12) = 30\\text{ sq '
                                                       'units}$$\n'
                                                       'Step 2: Because rotations, translations, '
                                                       'and reflections are all rigid motions '
                                                       '(isometries), distances and enclosed areas '
                                                       'are strictly invariant.\n'
                                                       'Therefore, $\\text{Perimeter}(\\triangle '
                                                       "A'''B'''C''') = 30\\text{ units}$ and "
                                                       "$\\text{Area}(\\triangle A'''B'''C''') = "
                                                       '30\\text{ sq units}$.\n'
                                                       '• Distractor A fails to include the '
                                                       'hypotenuse in the perimeter ($5 + 12 = '
                                                       '17$).\n'
                                                       '• Distractor B forgets the $\\frac{1}{2}$ '
                                                       'in the triangle area formula ($5 \\times '
                                                       '12 = 60$).\n'
                                                       '• Distractor D mistakenly doubles the '
                                                       'perimeter.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-16',
                                        'q': 'Polygon $G$ has a perimeter of $34\\text{ cm}$ and '
                                             'an area of $60\\text{ cm}^2$. Polygon $H$ is the '
                                             'result of applying a transformation to Polygon $G$. '
                                             'Which condition **proves definitively** that Polygon '
                                             '$H$ is **NOT** congruent to Polygon $G$?',
                                        'opts': [   'Polygon $H$ has its vertices labeled in '
                                                    'counterclockwise order while Polygon $G$ has '
                                                    'vertices in clockwise order.',
                                                    'Polygon $H$ lies entirely in Quadrant IV '
                                                    'while Polygon $G$ lies in Quadrant II.',
                                                    'Polygon $H$ is rotated $180^\\circ$ relative '
                                                    'to Polygon $G$.',
                                                    'Polygon $H$ has a perimeter of $38\\text{ '
                                                    'cm}$.'],
                                        'correct': 3,
                                        'hint': 'Rigid motions preserve distances, so the '
                                                'perimeter of a transformed figure must remain '
                                                'strictly unchanged if the figures are congruent.',
                                        'explanation': 'A sequence of rigid motions preserves all '
                                                       'segment lengths, which means the sum of '
                                                       'side lengths (perimeter) must remain '
                                                       'exactly the same. If Polygon $H$ has a '
                                                       'perimeter of $38\\text{ cm}$ while Polygon '
                                                       '$G$ has a perimeter of $34\\text{ cm}$, '
                                                       'the side lengths have changed ($38 \\neq '
                                                       '34$). Therefore, no sequence of rigid '
                                                       'motions can map $G$ to $H$, proving '
                                                       'definitively that $G \\not\\cong H$.\n'
                                                       '• Distractor A occurs whenever a '
                                                       'reflection is performed; reflected shapes '
                                                       'are still congruent.\n'
                                                       '• Distractor B occurs when shapes are '
                                                       'translated or rotated across quadrants; '
                                                       'location does not affect congruence.\n'
                                                       '• Distractor C is a rigid rotation, which '
                                                       'preserves congruence.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-17',
                                        'q': 'In HMH Into Math Lesson 1.5 Spark Your Learning '
                                             '(quilt pattern), Maribel creates quilt blocks using '
                                             'congruent fabric triangles. One fabric triangle in '
                                             'Quadrant II has vertices at $(-5, 1)$, $(-2, 1)$, '
                                             'and $(-2, 5)$. Maribel rotates this triangle '
                                             '$180^\\circ$ about the center of the quilt $(0, 0)$ '
                                             'to place a congruent piece in Quadrant IV. What are '
                                             'the coordinates of the rotated quilt piece?',
                                        'opts': [   '$(5, -1)$, $(2, -1)$, and $(2, -5)$',
                                                    '$(-5, -1)$, $(-2, -1)$, and $(-2, -5)$',
                                                    '$(1, 5)$, $(1, 2)$, and $(5, 2)$',
                                                    '$(-1, -5)$, $(-1, -2)$, and $(-5, -2)$'],
                                        'correct': 0,
                                        'hint': 'The coordinate rule for a $180^\\circ$ rotation '
                                                'about the origin is $(x, y) \\to (-x, -y)$.',
                                        'explanation': 'Applying the coordinate rule for a '
                                                       '$180^\\circ$ rotation about the origin, '
                                                       '$(x, y) \\to (-x, -y)$:\n'
                                                       '• $(-5, 1) \\to (-(-5), -(1)) = (5, -1)$\n'
                                                       '• $(-2, 1) \\to (-(-2), -(1)) = (2, -1)$\n'
                                                       '• $(-2, 5) \\to (-(-2), -(5)) = (2, -5)$\n'
                                                       'All coordinates are in Quadrant IV $(+, '
                                                       '-)$. Because a rotation is a rigid motion, '
                                                       'the rotated quilt block is guaranteed to '
                                                       'be congruent to the original template.\n'
                                                       '• Distractor B reflects across the '
                                                       '$x$-axis only: $(x, -y)$.\n'
                                                       '• Distractor C rotates $90^\\circ$ '
                                                       'clockwise: $(y, -x)$ or swaps '
                                                       'coordinates.\n'
                                                       '• Distractor D rotates $90^\\circ$ '
                                                       'counterclockwise: $(-y, x)$.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-18',
                                        'q': 'In HMH Into Math Lesson 1.5 Step It Out Task 2, five '
                                             'congruent triangles are positioned on a fabric grid. '
                                             'Triangle $B$ has vertices $(2, -1), (5, -1),$ and '
                                             '$(2, -4)$. Triangle $D$ has vertices $(8, 1), (11, '
                                             '1),$ and $(8, 4)$. Which sequence of transformations '
                                             'maps Triangle $B$ onto Triangle $D$, proving '
                                             '$\\triangle B \\cong \\triangle D$?',
                                        'opts': [   'A translation 6 units right and 2 units up',
                                                    'A $180^\\circ$ rotation about the origin',
                                                    'A reflection across the $x$-axis followed by '
                                                    'a translation 6 units right',
                                                    'A reflection across the $y$-axis followed by '
                                                    'a translation 10 units right'],
                                        'correct': 2,
                                        'hint': 'Notice that Triangle $B$ points down in the '
                                                'negative $y$-direction, while Triangle $D$ points '
                                                'up in the positive $y$-direction. This requires a '
                                                'reflection across a horizontal line!',
                                        'explanation': "Let's trace the vertices through the "
                                                       'sequence in Choice C:\n'
                                                       '1. Reflection across the $x$-axis: $(x, y) '
                                                       '\\to (x, -y)$:\n'
                                                       '• $(2, -1) \\to (2, 1)$\n'
                                                       '• $(5, -1) \\to (5, 1)$\n'
                                                       '• $(2, -4) \\to (2, 4)$\n'
                                                       '2. Translation 6 units right: $(x, y) \\to '
                                                       '(x + 6, y)$:\n'
                                                       '• $(2, 1) \\to (2 + 6, 1) = (8, 1)$\n'
                                                       '• $(5, 1) \\to (5 + 6, 1) = (11, 1)$\n'
                                                       '• $(2, 4) \\to (2 + 6, 4) = (8, 4)$\n'
                                                       'These match the vertices of Triangle $D$ '
                                                       'exactly! Since reflections and '
                                                       'translations are rigid motions, '
                                                       '$\\triangle B \\cong \\triangle D$.\n'
                                                       '• Distractor A fails because a pure '
                                                       'translation cannot change the vertical '
                                                       'orientation from pointing down to pointing '
                                                       'up.\n'
                                                       '• Distractor B maps $(2, -1) \\to (-2, '
                                                       '1)$, placing the shape on the negative '
                                                       '$x$-axis.\n'
                                                       '• Distractor D reflects horizontally, '
                                                       'leaving the shape still pointing downward.',
                                        'dok': 2,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-19',
                                        'q': 'Triangle 1 has vertices $A(1, 1), B(4, 1),$ and '
                                             '$C(1, 3)$. Triangle 2 has vertices $D(-1, 2), E(-1, '
                                             '-1),$ and $F(1, 2)$. Which sequence of '
                                             'transformations maps Triangle 1 directly onto '
                                             'Triangle 2, proving that $\\triangle 1 \\cong '
                                             '\\triangle 2$?',
                                        'opts': [   'Translate 2 units left and 1 unit up, then '
                                                    'reflect across the $x$-axis.',
                                                    'Rotate $90^\\circ$ clockwise about the '
                                                    'origin, then translate 2 units left and 3 '
                                                    'units up.',
                                                    'Reflect across the $y$-axis, then translate 3 '
                                                    'units down and 1 unit right.',
                                                    'Rotate $180^\\circ$ about the origin, then '
                                                    'translate 1 unit right and 2 units up.'],
                                        'correct': 1,
                                        'hint': 'Analyze the side orientation: In Triangle 1, the '
                                                '3-unit leg $AB$ is horizontal. In Triangle 2, the '
                                                '3-unit leg $DE$ is vertical. This rotation of '
                                                '$90^\\circ$ indicates a $90^\\circ$ turn!',
                                        'explanation': 'Step 1: Rotate $90^\\circ$ clockwise about '
                                                       'the origin using $(x, y) \\to (y, -x)$:\n'
                                                       "• $A(1, 1) \\to A'(1, -1)$\n"
                                                       "• $B(4, 1) \\to B'(1, -4)$\n"
                                                       "• $C(1, 3) \\to C'(3, -1)$\n"
                                                       'Step 2: Translate 2 units left and 3 units '
                                                       'up: $(x, y) \\to (x - 2, y + 3)$:\n'
                                                       "• $A'(1, -1) \\to (1 - 2, -1 + 3) = (-1, "
                                                       '2) = D$\n'
                                                       "• $B'(1, -4) \\to (1 - 2, -4 + 3) = (-1, "
                                                       '-1) = E$\n'
                                                       "• $C'(3, -1) \\to (3 - 2, -1 + 3) = (1, 2) "
                                                       '= F$\n'
                                                       'This maps Triangle 1 precisely onto '
                                                       'Triangle 2. Because both transformations '
                                                       'are rigid motions, $\\triangle 1 \\cong '
                                                       '\\triangle 2$.\n'
                                                       '• Distractors A, C, and D do not produce '
                                                       'the correct orientation or vertex '
                                                       'coordinates.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'},
                                    {   'id': 'p-1-5-mcq-20',
                                        'q': 'Triangle $\\triangle JKL$ with vertices $J(-5, 2), '
                                             'K(-2, 2),$ and $L(-2, 6)$ is transformed into '
                                             '$\\triangle PQR$ with vertices $P(5, -2), Q(2, -2),$ '
                                             'and $R(2, 2)$. Which sequence of rigid motions '
                                             'proves that $\\triangle JKL \\cong \\triangle PQR$?',
                                        'opts': [   'A reflection across the $y$-axis: $(x, y) '
                                                    '\\to (-x, y)$, followed by a translation 4 '
                                                    'units down: $(x, y) \\to (x, y - 4)$',
                                                    'A translation 7 units right followed by a '
                                                    'reflection across the line $y = x$',
                                                    'A $90^\\circ$ counterclockwise rotation about '
                                                    'the origin followed by a translation 2 units '
                                                    'right',
                                                    'A reflection across the $x$-axis followed by '
                                                    'a translation 3 units left'],
                                        'correct': 0,
                                        'hint': 'Check the $x$-coordinates: $J(-5, 2) \\to P(5, '
                                                '-2)$ has $x$ negated from $-5$ to $5$, suggesting '
                                                'a reflection across the $y$-axis first.',
                                        'explanation': 'Step 1: Reflect across the $y$-axis: $(x, '
                                                       'y) \\to (-x, y)$:\n'
                                                       "• $J(-5, 2) \\to J'(5, 2)$\n"
                                                       "• $K(-2, 2) \\to K'(2, 2)$\n"
                                                       "• $L(-2, 6) \\to L'(2, 6)$\n"
                                                       'Step 2: Translate 4 units down: $(x, y) '
                                                       '\\to (x, y - 4)$:\n'
                                                       "• $J'(5, 2) \\to (5, 2 - 4) = (5, -2) = "
                                                       'P$\n'
                                                       "• $K'(2, 2) \\to (2, 2 - 4) = (2, -2) = "
                                                       'Q$\n'
                                                       "• $L'(2, 6) \\to (2, 6 - 4) = (2, 2) = R$\n"
                                                       'The image matches $\\triangle PQR$ in '
                                                       'every coordinate. Because reflection and '
                                                       'translation are rigid motions, this proves '
                                                       'that $\\triangle JKL \\cong \\triangle '
                                                       'PQR$.\n'
                                                       '• Distractor B gives $(x + 7, y) \\to (y, '
                                                       'x + 7)$, which does not match $\\triangle '
                                                       'PQR$.\n'
                                                       '• Distractor C rotates $90^\\circ$ '
                                                       'counterclockwise, which turns horizontal '
                                                       'sides vertical, whereas side $JK$ and side '
                                                       '$PQ$ are both horizontal.\n'
                                                       '• Distractor D reflects across the '
                                                       '$x$-axis first, giving negative $x$ '
                                                       'coordinates.',
                                        'dok': 3,
                                        'standard': 'CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3'}],
                        'fitb': [   {   'id': 'p-1-5-f1',
                                        'q': 'If \\(\\triangle ABC \\cong \\triangle DEF\\), and '
                                             'side AB = 8.5 cm, what is the length of side DE in '
                                             'cm?',
                                        'expected': '8.5',
                                        'hint': 'Corresponding sides of congruent triangles are '
                                                'strictly equal.'},
                                    {   'id': 'p-1-5-f2',
                                        'q': 'Two figures are congruent if they have the exact '
                                             'same ________ and shape.',
                                        'expected': 'size',
                                        'hint': 'Same s___ and shape.'}]},
        'bookQuestions': [   {   'num': 'HMH Into Math • Section 1.5 Performance Task',
                                 'q': 'Polygon \\(P\\) is translated 5 units right and then '
                                      'dilated by a scale factor of 2 to form Polygon \\(Q\\). Are '
                                      'Polygons \\(P\\) and \\(Q\\) congruent? Explain thoroughly.',
                                 'modelAnswer': '<strong>Model Answer:</strong> No, Polygons '
                                                '\\(P\\) and \\(Q\\) are NOT congruent. Although '
                                                'the translation is a rigid motion, the dilation '
                                                'with scale factor \\(k = 2\\) multiplies all side '
                                                'lengths by 2 and doubles the perimeter. Because '
                                                'size is not preserved, there is no sequence of '
                                                'purely rigid motions that maps \\(P\\) to '
                                                '\\(Q\\); therefore, the polygons are similar, not '
                                                'congruent.'},
                             {   'num': 'HMH Into Math • Section 1.5 Problem 15',
                                 'q': 'Describe how to test if two complex figures on a grid are '
                                      'congruent without measuring every single point.',
                                 'modelAnswer': '<strong>Model Answer:</strong> First, check if '
                                                'corresponding side lengths and angle measures are '
                                                'equal. Next, identify the orientation of '
                                                'vertices. If orientation is preserved, look for a '
                                                'combination of translation and rotation. If '
                                                'reversed, include a reflection. If you can define '
                                                'the exact algebraic mapping sequence that takes '
                                                'all vertices of the first figure onto the second, '
                                                'congruence is mathematically proven.'}]},
    {   'id': '2.1',
        'modId': 'mod2',
        'modNum': 2,
        'modTitle': 'Transformations and Similarity',
        'themeColor': '#0ea5e9',
        'badge': 'Module 2 • Lesson 2.1',
        'num': '2.1',
        'title': 'Investigate Reductions and Enlargements',
        'tag': 'Scale Factors & Dilations',
        'standard': 'CCSS.MATH.CONTENT.8.G.A.3',
        'canDo': 'I can identify dilations as non-rigid transformations, determine whether a '
                 'dilation is an enlargement or reduction based on scale factor k, and calculate '
                 'scale factors.',
        'conceptIntro': 'A <strong>dilation</strong> is a transformation that changes the size of '
                        'a figure but maintains its overall shape and angle measures. A dilation '
                        'is governed by two parameters: a fixed point called the <strong>center of '
                        'dilation</strong> and a numerical ratio called the <strong>scale factor '
                        '\\(k\\)</strong>. If \\(k > 1\\), the figure grows into an '
                        '<strong>enlargement</strong>. If \\(0 < k < 1\\), the figure shrinks into '
                        'a <strong>reduction</strong>.',
        'rules': [   {   'name': 'Scale Factor Formula',
                         'formula': 'k = \\frac{\\text{Image Dimension}}{\\text{Preimage '
                                    'Dimension}} = \\frac{\\text{NEW}}{\\text{OLD}}',
                         'desc': 'Always divide the image measurement by the preimage '
                                 'measurement.'},
                     {   'name': 'Enlargement Criterion',
                         'formula': 'k > 1',
                         'desc': 'Image is larger than the preimage.'},
                     {   'name': 'Reduction Criterion',
                         'formula': '0 < k < 1',
                         'desc': 'Image is smaller than the preimage.'}],
        'vocab': [   {   'term': 'Dilation',
                         'def': 'A non-rigid transformation that expands or shrinks a figure '
                                'proportionally.',
                         'ex': 'Using a photocopier zoom function.'},
                     {   'term': 'Scale Factor (k)',
                         'def': 'The ratio of corresponding linear dimensions of image to '
                                'preimage.',
                         'ex': 'k = 2 doubles side lengths; k = 0.5 halves side lengths.'},
                     {   'term': 'Center of Dilation',
                         'def': 'The fixed point from which all points are expanded or contracted.',
                         'ex': 'The origin (0, 0).'}],
        'invariance': [   {   'prop': 'Angle Measures',
                              'status': '✓ Preserved (Angles stay same!)',
                              'cls': 'yes'},
                          {'prop': 'Geometric Shape', 'status': '✓ Preserved', 'cls': 'yes'},
                          {'prop': 'Side Lengths', 'status': '✕ Changed by factor k', 'cls': 'no'},
                          {'prop': 'Perimeter', 'status': '✕ Multiplied by k', 'cls': 'no'},
                          {'prop': 'Area', 'status': '✕ Multiplied by k²', 'cls': 'no'}],
        'illustrativeExamples': [   {   'title': 'Example 1: Classifying Scale Factors',
                                        'desc': 'Classify the following scale factors: (a) \\(k = '
                                                '3.5\\), (b) \\(k = \\frac{2}{5}\\), (c) \\(k = '
                                                '1\\).',
                                        'analysis': '(a) \\(k = 3.5 > 1 \\implies\\) '
                                                    'Enlargement.<br>(b) \\(k = 0.4 < 1 '
                                                    '\\implies\\) Reduction.<br>(c) \\(k = 1 '
                                                    '\\implies\\) Identity (congruent, neither '
                                                    'enlarged nor reduced).'},
                                    {   'title': 'Example 2: Finding Scale Factor from Side '
                                                 'Lengths',
                                        'desc': 'A photo has width 4 inches. After dilation, the '
                                                'new photo has width 10 inches. What is the scale '
                                                'factor \\(k\\)?',
                                        'analysis': '\\(k = '
                                                    '\\frac{\\text{Image}}{\\text{Preimage}} = '
                                                    '\\frac{10}{4} = 2.5\\). Since \\(k = 2.5 > '
                                                    '1\\), this is an enlargement.'}],
        'workedExample': {   'title': 'Worked Example: Calculating Scale Factor & Missing '
                                      'Dimensions',
                             'problem': 'Rectangle \\(ABCD\\) has length 12 cm and width 8 cm. '
                                        'After a dilation with center at the origin, rectangle '
                                        "\\(A'B'C'D'\\) has length 18 cm. (a) Find scale factor "
                                        '\\(k\\). (b) Is this an enlargement or reduction? (c) '
                                        "Find width \\(B'C'\\).",
                             'step1': '<strong>Step 1: Compute scale factor \\(k\\):</strong> '
                                      "Using 'NEW over OLD':<br>\\[k = \\frac{\\text{Length of "
                                      'Image}}{\\text{Length of Preimage}} = \\frac{18}{12} = '
                                      '\\frac{3}{2} = 1.5\\]',
                             'step2': '<strong>Step 2: Classify the transformation:</strong> Since '
                                      '\\(k = 1.5 > 1\\), the dilation is an '
                                      '<strong>enlargement</strong>.',
                             'step3': '<strong>Step 3: Calculate the missing width:</strong> '
                                      'Multiply the original width by \\(k\\):<br>\\[\\text{Width '
                                      "of } A'B'C'D' = k \\times 8 = 1.5 \\times 8 = 12\\text{ "
                                      'cm}\\]',
                             'modelAnswer': '<strong>Student Model Answer:</strong> The scale '
                                            'factor is \\(k = 1.5\\). Because \\(k > 1\\), this is '
                                            'an enlargement. The width of the image rectangle '
                                            "\\(A'B'C'D'\\) is \\(12\\text{ cm}\\)."},
        'practice': {   'mcqs': [   {   'id': 'p-2-1-m1',
                                        'q': 'Which scale factor produces a reduction?',
                                        'opts': ['k = 4/3', 'k = 1.25', 'k = 3/5', 'k = 2.0'],
                                        'correct': 2,
                                        'hint': 'A reduction has a scale factor between 0 and 1.'},
                                    {   'id': 'p-2-1-m2',
                                        'q': 'If a preimage segment of length 15 is dilated with k '
                                             '= 1/3, what is the image length?',
                                        'opts': ['5', '45', '12', '15'],
                                        'correct': 0,
                                        'hint': 'Multiply 15 by 1/3: 15 / 3 = 5.'}],
                        'fitb': [   {   'id': 'p-2-1-f1',
                                        'q': 'A dilation has scale factor k = 0.75. This dilation '
                                             'is classified as a(n) ________ (enlargement or '
                                             'reduction).',
                                        'expected': 'reduction',
                                        'hint': '0.75 is less than 1.'},
                                    {   'id': 'p-2-1-f2',
                                        'q': 'A blueprint model has length 6 cm. The actual '
                                             'building length is 24 meters (2400 cm). What is the '
                                             'scale factor k from model to actual building?',
                                        'expected': '400',
                                        'hint': 'Divide 2400 by 6.'}]},
        'bookQuestions': [   {   'num': 'HMH Into Math • Section 2.1 Problem 4',
                                 'q': 'A microscope magnifies an insect leg from \\(0.8\\text{ '
                                      'mm}\\) to \\(20\\text{ mm}\\). Determine the scale factor '
                                      'of the magnification and state whether it is a reduction or '
                                      'enlargement.',
                                 'modelAnswer': '<strong>Model Answer:</strong> \\(k = '
                                                '\\frac{\\text{Image}}{\\text{Preimage}} = '
                                                '\\frac{20}{0.8} = 25\\). Since \\(k = 25 > 1\\), '
                                                'this is an enlargement of \\(25\\times\\).'},
                             {   'num': 'HMH Into Math • Section 2.1 Problem 9',
                                 'q': 'Can a dilation ever be a rigid motion? Explain why or why '
                                      'not using the scale factor \\(k\\).',
                                 'modelAnswer': '<strong>Model Answer:</strong> A dilation is only '
                                                'a rigid motion in the trivial case where \\(k = '
                                                '1\\), which is the identity transformation where '
                                                'the image is identical to the preimage. For all '
                                                'other values of \\(k \\neq 1\\), side lengths '
                                                'change by factor \\(k\\), which violates distance '
                                                'preservation.'}]},
    {   'id': '2.2',
        'modId': 'mod2',
        'modNum': 2,
        'modTitle': 'Transformations and Similarity',
        'themeColor': '#0ea5e9',
        'badge': 'Module 2 • Lesson 2.2',
        'num': '2.2',
        'title': 'Explore Dilations',
        'tag': 'Coordinate Plane Mappings',
        'standard': 'CCSS.MATH.CONTENT.8.G.A.3',
        'canDo': 'I can graph dilations on the coordinate plane centered at the origin, express '
                 'them with algebraic notation \\((x, y) \\to (kx, ky)\\), and determine scale '
                 'factors from coordinates.',
        'conceptIntro': 'When a dilation has its center at the origin \\((0, 0)\\), the algebraic '
                        'coordinate mapping rule is: \\((x, y) \\to (kx, ky)\\). Every '
                        'x-coordinate and every y-coordinate is multiplied by the scale factor '
                        '\\(k\\). Lines through the origin stay on the same line, while lines not '
                        'passing through the origin are mapped to parallel lines.',
        'rules': [   {   'name': 'Origin Dilation Rule',
                         'formula': '(x, y) \\to (kx, ky)',
                         'desc': 'Multiply each coordinate by scale factor k.'},
                     {   'name': 'Finding k from Coordinates',
                         'formula': "k = \\frac{x'}{x} = \\frac{y'}{y}",
                         'desc': 'Ratio of any non-zero image coordinate to preimage coordinate.'}],
        'vocab': [   {   'term': 'Dilation Mapping',
                         'def': 'The rule (x, y) → (kx, ky) mapping coordinates under dilation '
                                'centered at the origin.',
                         'ex': '(x, y) → (3x, 3y).'},
                     {   'term': 'Center at Origin',
                         'def': 'The point (0, 0) remains fixed; all other points move directly '
                                'toward or away from (0, 0).',
                         'ex': '(0, 0) → (0, 0).'},
                     {   'term': 'Ray from Origin',
                         'def': 'A point and its image always lie on the exact same ray '
                                'originating from the center of dilation.',
                         'ex': "Points O(0,0), P(2,3), and P'(6,9) are collinear."}],
        'invariance': [   {   'prop': 'Origin Point (0, 0)',
                              'status': '✓ Fixed Invariant Point',
                              'cls': 'yes'},
                          {   'prop': 'Slope of Lines',
                              'status': '✓ Preserved (Parallel lines)',
                              'cls': 'yes'},
                          {'prop': 'Angle Measures', 'status': '✓ Preserved', 'cls': 'yes'},
                          {'prop': 'Coordinates', 'status': '✕ Multiplied by k', 'cls': 'no'}],
        'illustrativeExamples': [   {   'title': 'Example 1: Dilating a Vertex by k = 3',
                                        'desc': 'Point \\(A(2, -4)\\) is dilated by scale factor '
                                                '\\(k = 3\\) with center at the origin.',
                                        'analysis': "Rule: \\((x, y) \\to (3x, 3y)\\). \\(x' = "
                                                    "3(2) = 6\\), \\(y' = 3(-4) = -12\\). Image: "
                                                    "\\(A'(6, -12)\\)."},
                                    {   'title': 'Example 2: Finding k from Preimage and Image',
                                        'desc': 'Preimage vertex \\(B(-6, 9)\\) maps to image '
                                                "vertex \\(B'(-2, 3)\\) with center at origin. "
                                                'What is \\(k\\)?',
                                        'analysis': "\\(k = \\frac{x'}{x} = \\frac{-2}{-6} = "
                                                    '\\frac{1}{3}\\). Verify with y: \\(k = '
                                                    "\\frac{y'}{y} = \\frac{3}{9} = "
                                                    '\\frac{1}{3}\\). The scale factor is \\(k = '
                                                    '\\frac{1}{3}\\) (reduction).'}],
        'workedExample': {   'title': 'Worked Example: Dilating a Triangle on the Coordinate Plane',
                             'problem': '\\(\\triangle ABC\\) has vertices \\(A(1, 2)\\), \\(B(3, '
                                        '2)\\), and \\(C(1, 4)\\). (a) Dilate \\(\\triangle ABC\\) '
                                        'by scale factor \\(k = 2.5\\) centered at the origin. (b) '
                                        'List all image coordinates. (c) Verify that the slope of '
                                        "\\(AC\\) equals the slope of \\(A'C'\\).",
                             'step1': '<strong>Step 1: State the coordinate mapping rule:</strong> '
                                      'With \\(k = 2.5\\), the rule is \\((x, y) \\to (2.5x, '
                                      '2.5y)\\).',
                             'step2': '<strong>Step 2: Multiply each coordinate by '
                                      "2.5:</strong><br>• \\(A(1, 2) \\to A'(1 \\times 2.5, 2 "
                                      "\\times 2.5) = A'(2.5, 5)\\)<br>• \\(B(3, 2) \\to B'(3 "
                                      "\\times 2.5, 2 \\times 2.5) = B'(7.5, 5)\\)<br>• \\(C(1, 4) "
                                      "\\to C'(1 \\times 2.5, 4 \\times 2.5) = C'(2.5, 10)\\).",
                             'step3': '<strong>Step 3: Verify slopes:</strong> Segment \\(AC\\) is '
                                      "vertical (undefined slope). Segment \\(A'C'\\) has \\(x = "
                                      '2.5\\) for both points, so it is also vertical (undefined '
                                      'slope). Lines remain parallel.',
                             'modelAnswer': '<strong>Student Model Answer:</strong> Mapping rule: '
                                            '\\((x, y) \\to (2.5x, 2.5y)\\). Image vertices: '
                                            "\\(A'(2.5, 5)\\), \\(B'(7.5, 5)\\), \\(C'(2.5, "
                                            '10)\\). Corresponding segments \\(AC\\) and '
                                            "\\(A'C'\\) are both vertical and parallel."},
        'practice': {   'mcqs': [   {   'id': 'p-2-2-m1',
                                        'q': 'If vertex M(4, -6) is dilated with center at origin '
                                             "by k = 0.5, what are the coordinates of M'?",
                                        'opts': ['(2, -3)', '(8, -12)', '(4.5, -5.5)', '(2, 3)'],
                                        'correct': 0,
                                        'hint': 'Multiply both 4 and -6 by 0.5.'},
                                    {   'id': 'p-2-2-m2',
                                        'q': "Point P(3, 5) maps to P'(12, 20) under an origin "
                                             'dilation. What is scale factor k?',
                                        'opts': ['3', '4', '9', '15'],
                                        'correct': 1,
                                        'hint': 'Divide image by preimage: 12 / 3 = 4.'}],
                        'fitb': [   {   'id': 'p-2-2-f1',
                                        'q': 'Dilate point R(-5, 2) by scale factor k = 4 with '
                                             "center at origin. Enter R' as (x, y):",
                                        'expected': '(-20, 8)',
                                        'altExpected': ['(-20,8)', '-20, 8', '-20,8'],
                                        'hint': 'Multiply both coordinates by 4: (-5 * 4, 2 * 4).'},
                                    {   'id': 'p-2-2-f2',
                                        'q': 'If (x, y) → (kx, ky) maps (8, 12) to (2, 3), what is '
                                             'the value of k in decimal form?',
                                        'expected': '0.25',
                                        'altExpected': ['1/4', '.25'],
                                        'hint': '2 / 8 = 1/4 = 0.25.'}]},
        'bookQuestions': [   {   'num': 'HMH Into Math • Section 2.2 Exercise 8',
                                 'q': 'A quadrilateral with vertices \\(A(0, 0), B(2, 4), C(6, 4), '
                                      'D(4, 0)\\) is dilated by \\(k = 1.5\\) from the origin. '
                                      "Find the coordinates of \\(B'\\) and \\(C'\\), and explain "
                                      'why vertex \\(A\\) does not move.',
                                 'modelAnswer': "<strong>Model Answer:</strong> \\(B'(2 \\times "
                                                "1.5, 4 \\times 1.5) = B'(3, 6)\\) and \\(C'(6 "
                                                "\\times 1.5, 4 \\times 1.5) = C'(9, 6)\\). Vertex "
                                                '\\(A(0, 0)\\) does not move because \\((0 \\times '
                                                '1.5, 0 \\times 1.5) = (0, 0)\\). The center of '
                                                'dilation is always an invariant (fixed) point.'},
                             {   'num': 'HMH Into Math • Section 2.2 Exercise 15',
                                 'q': 'Prove that lines connecting corresponding points under an '
                                      'origin dilation all pass through the origin \\((0, 0)\\).',
                                 'modelAnswer': '<strong>Model Answer:</strong> For any point '
                                                "\\(P(x, y)\\) and its image \\(P'(kx, ky)\\), the "
                                                'slope of line \\(OP\\) is \\(\\frac{y - 0}{x - 0} '
                                                "= \\frac{y}{x}\\). The slope of line \\(OP'\\) is "
                                                '\\(\\frac{ky - 0}{kx - 0} = \\frac{y}{x}\\). '
                                                'Since both segments share point \\(O(0, 0)\\) and '
                                                'have identical slopes, points \\(O\\), \\(P\\), '
                                                "and \\(P'\\) are collinear, proving the line "
                                                'passes through the origin.'}]},
    {   'id': '2.3',
        'modId': 'mod2',
        'modNum': 2,
        'modTitle': 'Transformations and Similarity',
        'themeColor': '#0ea5e9',
        'badge': 'Module 2 • Lesson 2.3',
        'num': '2.3',
        'title': 'Understand and Recognize Similar Figures',
        'tag': 'Similarity Proofs & Golden Laws',
        'standard': 'CCSS.MATH.CONTENT.8.G.A.4',
        'canDo': 'I can verify similarity using similarity transformations, explain that similar '
                 'figures have congruent angles and proportional sides, and calculate perimeter '
                 '(k) and area (k²) ratios.',
        'conceptIntro': '<strong>The Fundamental Similarity Theorem:</strong> Two figures are '
                        '<strong>similar (\\(\\sim\\))</strong> if and only if there exists a '
                        'sequence of transformations (combining rigid motions and at least one '
                        'dilation) that maps the first figure onto the second. For similar '
                        'figures: <strong>all corresponding angles are congruent '
                        '(\\(\\cong\\))</strong> and <strong>all corresponding side lengths are in '
                        'constant proportion (\\(k\\))</strong>. Most importantly: '
                        '<strong>Perimeter scales by \\(k\\)</strong>, while <strong>Area scales '
                        'by \\(k^2\\)</strong>!',
        'rules': [   {   'name': 'Angle Congruence Condition',
                         'formula': "\\angle A \\cong \\angle A', \\angle B \\cong \\angle B', "
                                    "\\angle C \\cong \\angle C'",
                         'desc': 'All corresponding angles must be congruent.'},
                     {   'name': 'Side Proportionality Condition',
                         'formula': "\\frac{A'B'}{AB} = \\frac{B'C'}{BC} = \\frac{A'C'}{AC} = k",
                         'desc': 'All corresponding side length ratios must equal the exact same '
                                 'scale factor k.'},
                     {   'name': 'Linear Perimeter Scaling Law',
                         'formula': "P' = k \\cdot P",
                         'desc': 'Perimeter scales linearly with the scale factor k.'},
                     {   'name': 'Quadratic Area Scaling Law',
                         'formula': "A' = k^2 \\cdot A",
                         'desc': 'Area scales with the SQUARE of the scale factor k².'}],
        'vocab': [   {   'term': 'Similar Figures (\\(\\sim\\))',
                         'def': 'Figures that have the same shape, congruent angles, and '
                                'proportional side lengths.',
                         'ex': 'An architectural model and the completed skyscraper.'},
                     {   'term': 'Similarity Transformation',
                         'def': 'A composition of a dilation and one or more rigid motions.',
                         'ex': 'Dilate by k = 2, then rotate 90° clockwise.'},
                     {   'term': 'Area Ratio (k²)',
                         'def': 'The ratio of image area to preimage area equals scale factor '
                                'squared.',
                         'ex': 'If k = 3, area is 3² = 9 times larger.'}],
        'invariance': [   {   'prop': 'Angle Measures',
                              'status': '✓ Strictly Congruent',
                              'cls': 'yes'},
                          {'prop': 'Geometric Shape', 'status': '✓ Identical Shape', 'cls': 'yes'},
                          {   'prop': 'Side Lengths',
                              'status': 'Proportional (Ratio = k)',
                              'cls': 'warn'},
                          {'prop': 'Perimeter Ratio', 'status': "P' / P = k", 'cls': 'warn'},
                          {'prop': 'Area Ratio', 'status': "A' / A = k²", 'cls': 'warn'}],
        'illustrativeExamples': [   {   'title': 'Example 1: Verifying Similarity',
                                        'desc': 'Triangle 1 has angles 40° and 60°. Triangle 2 has '
                                                'angles 60° and 80°. Are they similar?',
                                        'analysis': 'Third angle of Triangle 1: \\(180^\\circ - '
                                                    '(40^\\circ + 60^\\circ) = 80^\\circ\\). All '
                                                    'three angles of Triangle 1 are 40°, 60°, 80°. '
                                                    'All three angles of Triangle 2 are 40°, 60°, '
                                                    '80°. Because all corresponding angles are '
                                                    'congruent, the triangles are <strong>similar '
                                                    '(\\(\\sim\\))</strong> by AA similarity.'},
                                    {   'title': 'Example 2: The Golden Area Scaling Rule',
                                        'desc': 'A triangle with Area = \\(12\\text{ cm}^2\\) is '
                                                'dilated by scale factor \\(k = 4\\). What is the '
                                                'area of the image?',
                                        'analysis': "Rule: \\(A' = k^2 \\times A\\). \\(k^2 = 4^2 "
                                                    "= 16\\). \\(A' = 16 \\times 12 = 192\\text{ "
                                                    'cm}^2\\). (Perimeter would only be '
                                                    '\\(4\\times\\), but Area is \\(16\\times\\) '
                                                    'larger!).'}],
        'workedExample': {   'title': 'Worked Example: Comprehensive Similarity & Area Proof',
                             'problem': 'Right triangle \\(ABC\\) has legs 6 cm and 8 cm '
                                        '(hypotenuse 10 cm, Area \\(= 24\\text{ cm}^2\\), '
                                        'Perimeter \\(= 24\\text{ cm}\\)). It undergoes a '
                                        'similarity transformation with scale factor \\(k = 3\\) '
                                        "to form \\(\\triangle A'B'C'\\). (a) State the side "
                                        "lengths of \\(\\triangle A'B'C'\\). (b) Calculate the new "
                                        "perimeter \\(P'\\). (c) Calculate the new area \\(A'\\) "
                                        'using both direct geometry and the \\(k^2\\) theorem.',
                             'step1': '<strong>Step 1: Calculate image side lengths:</strong> '
                                      'Multiply each side by \\(k = 3\\):<br>• Leg 1: \\(6 \\times '
                                      '3 = 18\\text{ cm}\\)<br>• Leg 2: \\(8 \\times 3 = 24\\text{ '
                                      'cm}\\)<br>• Hypotenuse: \\(10 \\times 3 = 30\\text{ cm}\\).',
                             'step2': '<strong>Step 2: Calculate perimeter '
                                      "\\(P'\\):</strong><br>\\[P' = 18 + 24 + 30 = 72\\text{ "
                                      "cm}\\]<br>Verification using formula: \\(P' = k \\times P = "
                                      '3 \\times 24 = 72\\text{ cm}\\). (Matches!)',
                             'step3': '<strong>Step 3: Calculate area '
                                      "\\(A'\\):</strong><br>Direct: \\(A' = \\frac{1}{2} \\times "
                                      '\\text{base} \\times \\text{height} = \\frac{1}{2} \\times '
                                      '18 \\times 24 = 216\\text{ cm}^2\\).<br>Using \\(k^2\\) '
                                      "rule: \\(A' = k^2 \\times A = 3^2 \\times 24 = 9 \\times 24 "
                                      '= 216\\text{ cm}^2\\). (Exact match!)',
                             'modelAnswer': '<strong>Student Model Answer:</strong> The side '
                                            "lengths of \\(\\triangle A'B'C'\\) are \\(18\\text{ "
                                            'cm}\\), \\(24\\text{ cm}\\), and \\(30\\text{ cm}\\). '
                                            "The perimeter scales linearly to \\(P' = 3 \\times 24 "
                                            '= 72\\text{ cm}\\). The area scales quadratically to '
                                            "\\(A' = 3^2 \\times 24 = 9 \\times 24 = 216\\text{ "
                                            'cm}^2\\).'},
        'practice': {   'mcqs': [   {   'id': 'p-2-3-m1',
                                        'q': 'If two polygons are similar with scale factor k = 5, '
                                             'what is the ratio of their areas?',
                                        'opts': ['5', '10', '25', '125'],
                                        'correct': 2,
                                        'hint': 'Area ratio is k² = 5² = 25.'},
                                    {   'id': 'p-2-3-m2',
                                        'q': 'Which condition is ALWAYS true for two similar '
                                             'geometric figures?',
                                        'opts': [   'Side lengths are equal',
                                                    'Corresponding angles are congruent',
                                                    'Perimeters are equal',
                                                    'Orientation is reversed'],
                                        'correct': 1,
                                        'hint': 'Similar shapes keep their exact shape and angles, '
                                                'only size changes.'}],
                        'fitb': [   {   'id': 'p-2-3-f1',
                                        'q': 'A rectangle has Area = 15 cm². If it is dilated by '
                                             'scale factor k = 2, what is the new Area in cm²?',
                                        'expected': '60',
                                        'hint': 'Multiply original area by k² = 2² = 4: 15 * 4 = '
                                                '60.'},
                                    {   'id': 'p-2-3-f2',
                                        'q': 'If the perimeter of a preimage is 20 cm and the '
                                             'image perimeter is 50 cm, what is the scale factor '
                                             'k?',
                                        'expected': '2.5',
                                        'altExpected': ['5/2'],
                                        'hint': 'Divide 50 by 20.'}]},
        'bookQuestions': [   {   'num': 'HMH Into Math • Section 2.3 Comprehensive Problem 10',
                                 'q': 'Two similar billboards have heights 10 ft and 25 ft. If the '
                                      'smaller billboard costs $400 to paint, how much will the '
                                      'larger billboard cost to paint assuming paint cost is '
                                      'directly proportional to area?',
                                 'modelAnswer': '<strong>Model Answer:</strong><br>1. Scale '
                                                'factor: \\(k = \\frac{25}{10} = 2.5\\).<br>2. '
                                                'Area ratio: \\(k^2 = (2.5)^2 = 6.25\\).<br>3. '
                                                'Painting cost scales with area: \\(\\text{Cost} = '
                                                '6.25 \\times \\$400 = \\$2,500\\).<br>Notice that '
                                                'even though height is only \\(2.5\\times\\), the '
                                                'area and cost are \\(6.25\\times\\) larger!'},
                             {   'num': 'HMH Into Math • Section 2.3 Theorem Proof Problem 16',
                                 'q': 'Explain why all circles are similar to one another, but not '
                                      'all rectangles are similar to one another.',
                                 'modelAnswer': '<strong>Model Answer:</strong> Every circle is '
                                                'determined by a single dimension: its radius '
                                                '\\(r\\). Dilating any circle by \\(k = '
                                                '\\frac{r_2}{r_1}\\) maps it perfectly onto any '
                                                'other circle, and all circle angles are full '
                                                '\\(360^\\circ\\) rotations. Rectangles, however, '
                                                'have two independent dimensions (length and '
                                                'width). Two rectangles can both have four '
                                                '\\(90^\\circ\\) angles but have different aspect '
                                                'ratios (e.g. \\(2 \\times 8\\) vs \\(4 \\times '
                                                '6\\)), meaning their side lengths are not in '
                                                'constant proportion; therefore, not all '
                                                'rectangles are similar.'}]}]

print(f"Loaded {len(LESSONS)} complete lessons.")
