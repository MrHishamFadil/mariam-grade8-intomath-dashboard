/**
 * Quiz Arena & Gamification Builder
 * Mariam Hisham AbdelFadil - Grade 8 Into Math Dashboard
 *
 * Features:
 * 1. Web Audio API Engine (Safe, synthesized sound effects: click, chime, fanfare, gentle boop).
 * 2. Gamification & Profile Tracking (Mariam's XP, Tiered Levels, Badges, Streaks, LocalStorage persistence).
 * 3. Quiz Modes:
 *    - Module 1 Final Test (25 Authentic Questions from build_module1_final_test.py / CURRICULUM_DATA)
 *    - Lesson Practice (Lessons 1.1, 1.2, 1.3, 1.4, 1.5 - exactly 20 authentic questions each)
 *    - Module 2 Practice (10 Questions on Dilations & Similarity)
 *    - Grand Mastery (15 Mixed Questions across Modules 1 & 2)
 * 4. Interactive Question Engine (Multiple Choice, Coordinate (x,y) Entry, True/False, Sequence/Order Builder).
 * 5. Hint Engine, Step-by-Step KaTeX Math Explanations, Confetti celebration for >= 80% scores.
 * 6. Bulletproof zero-dependency fallbacks with complete error isolation.
 */

(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.QuizArena = factory();
  }
})(typeof window !== 'undefined' ? window : this, function () {
  'use strict';

  // --- AUDIO SYNTHESIZER (Web Audio API) ---
  const AudioEngine = (function () {
    let audioCtx = null;
    let isMuted = false;

    try {
      if (typeof localStorage !== 'undefined') {
        isMuted = localStorage.getItem('mariam_quiz_muted') === 'true';
      }
    } catch (e) {
      // Safe fallback for restricted localStorage
    }

    function getContext() {
      if (typeof window === 'undefined') return null;
      try {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (!AudioContextClass) return null;
        if (!audioCtx) {
          audioCtx = new AudioContextClass();
        }
        if (audioCtx && audioCtx.state === 'suspended') {
          audioCtx.resume().catch(function () {});
        }
        return audioCtx;
      } catch (err) {
        return null;
      }
    }

    function playTone(freq, type, duration, startTimeOffset, gainValue) {
      if (isMuted) return;
      try {
        const ctx = getContext();
        if (!ctx) return;

        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        const now = ctx.currentTime + (startTimeOffset || 0);

        osc.type = type || 'sine';
        osc.frequency.setValueAtTime(freq, now);

        gain.gain.setValueAtTime(gainValue || 0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + duration);
      } catch (e) {
        // Silent catch for audio hardware restrictions
      }
    }

    return {
      getMuted: function () {
        return isMuted;
      },
      toggleMute: function () {
        isMuted = !isMuted;
        try {
          if (typeof localStorage !== 'undefined') {
            localStorage.setItem('mariam_quiz_muted', String(isMuted));
          }
        } catch (e) {}
        return isMuted;
      },
      playClick: function () {
        if (isMuted) return;
        playTone(620, 'triangle', 0.05, 0, 0.1);
      },
      playCorrect: function () {
        if (isMuted) return;
        const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
        notes.forEach(function (freq, i) {
          playTone(freq, 'sine', 0.22, i * 0.08, 0.15);
        });
      },
      playWrong: function () {
        if (isMuted) return;
        try {
          const ctx = getContext();
          if (!ctx) return;
          const now = ctx.currentTime;
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();

          osc.type = 'sine';
          osc.frequency.setValueAtTime(220, now);
          osc.frequency.linearRampToValueAtTime(140, now + 0.28);

          gain.gain.setValueAtTime(0.12, now);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.28);

          osc.connect(gain);
          gain.connect(ctx.destination);

          osc.start(now);
          osc.stop(now + 0.28);
        } catch (e) {}
      },
      playVictory: function () {
        if (isMuted) return;
        try {
          const notes = [
            { f: 523.25, d: 0.12, t: 0 },       // C5
            { f: 659.25, d: 0.12, t: 0.11 },    // E5
            { f: 783.99, d: 0.12, t: 0.22 },    // G5
            { f: 1046.50, d: 0.35, t: 0.34 },   // C6
            { f: 880.00, d: 0.15, t: 0.65 },    // A5
            { f: 1046.50, d: 0.55, t: 0.82 }    // C6
          ];
          notes.forEach(function (n) {
            playTone(n.f, 'triangle', n.d, n.t, 0.18);
          });
        } catch (e) {}
      }
    };
  })();

  // --- GAMIFICATION & PROFILE SYSTEM ---
  const LEVEL_TITLES = [
    { level: 1, title: 'Coordinate Apprentice', minXP: 0 },
    { level: 2, title: 'Vector Explorer', minXP: 250 },
    { level: 3, title: 'Symmetry Knight', minXP: 600 },
    { level: 4, title: 'Rotation Wizard', minXP: 1100 },
    { level: 5, title: 'Similarity Grandmaster', minXP: 1800 }
  ];

  const BADGE_DEFINITIONS = [
    { id: 'first_step', name: 'First Step', desc: 'Completed first question in the arena', icon: '🌱' },
    { id: 'translation_pro', name: 'Translation Pro', desc: 'Mastered translations with 100% accuracy', icon: '🚀' },
    { id: 'mirror_marvel', name: 'Mirror Marvel', desc: 'Mastered reflections across axes & lines', icon: '🪞' },
    { id: 'spin_doctor', name: 'Spin Doctor', desc: 'Solved rotation challenges with flying colors', icon: '🔄' },
    { id: 'congruence_champion', name: 'Congruence Champion', desc: 'Mastered congruent figures & sequences', icon: '💎' },
    { id: 'dilation_dynamo', name: 'Dilation Dynamo', desc: 'Mastered scale factors, enlargements & reductions', icon: '🔍' },
    { id: 'quiz_champion', name: 'Quiz Champion', desc: 'Finished a full 10+ question test', icon: '🏆' },
    { id: 'module1_master', name: 'Module 1 Master', desc: 'Aced the 25-Question Module 1 Final Exam', icon: '👑' },
    { id: 'perfect_streak', name: 'Perfect Streak', desc: 'Answered 5 questions correctly in a row', icon: '🔥' }
  ];

  const STORAGE_KEY = 'mariam_math_profile';

  function defaultProfile() {
    return {
      name: 'Mariam Hisham AbdelFadil',
      xp: 0,
      level: 1,
      levelTitle: 'Coordinate Apprentice',
      streak: 0,
      maxStreak: 0,
      questionsAnswered: 0,
      correctAnswers: 0,
      quizzesCompleted: 0,
      badges: [],
      history: []
    };
  }

  const ProfileManager = (function () {
    let profile = null;

    function load() {
      if (profile) return profile;
      try {
        if (typeof localStorage !== 'undefined') {
          const raw = localStorage.getItem(STORAGE_KEY);
          if (raw) {
            profile = Object.assign(defaultProfile(), JSON.parse(raw));
            recalcLevel();
            return profile;
          }
        }
      } catch (e) {
        console.warn('Failed reading profile from storage:', e);
      }
      profile = defaultProfile();
      save();
      return profile;
    }

    function save() {
      if (!profile) return;
      try {
        if (typeof localStorage !== 'undefined') {
          localStorage.setItem(STORAGE_KEY, JSON.stringify(profile));
        }
      } catch (e) {
        console.warn('Failed saving profile:', e);
      }
      updateUIHeader();
    }

    function recalcLevel() {
      let current = LEVEL_TITLES[0];
      for (let i = 0; i < LEVEL_TITLES.length; i++) {
        if (profile.xp >= LEVEL_TITLES[i].minXP) {
          current = LEVEL_TITLES[i];
        }
      }
      const leveledUp = current.level > profile.level;
      profile.level = current.level;
      profile.levelTitle = current.title;
      return leveledUp;
    }

    function awardXP(amount) {
      load();
      profile.xp += amount;
      const leveledUp = recalcLevel();
      save();
      if (leveledUp) {
        AudioEngine.playVictory();
        showToast('🎉 Level Up! You are now a ' + profile.levelTitle + '!');
      }
      return profile.xp;
    }

    function awardBadge(badgeId) {
      load();
      if (!profile.badges.includes(badgeId)) {
        profile.badges.push(badgeId);
        save();
        const badgeObj = BADGE_DEFINITIONS.find(function (b) { return b.id === badgeId; });
        const name = badgeObj ? badgeObj.name : badgeId;
        AudioEngine.playVictory();
        showToast('🎖️ Badge Unlocked: ' + name + '!');
        return true;
      }
      return false;
    }

    function recordAnswer(isCorrect, topic) {
      load();
      profile.questionsAnswered += 1;
      awardBadge('first_step');

      if (isCorrect) {
        profile.correctAnswers += 1;
        profile.streak += 1;
        if (profile.streak > profile.maxStreak) {
          profile.maxStreak = profile.streak;
        }
        // Track +50 XP per correct question
        awardXP(50);

        if (profile.streak >= 5) {
          awardBadge('perfect_streak');
        }

        if (topic) {
          const t = topic.toLowerCase();
          if (t.includes('translation')) awardBadge('translation_pro');
          if (t.includes('reflection')) awardBadge('mirror_marvel');
          if (t.includes('rotation')) awardBadge('spin_doctor');
          if (t.includes('congruen')) awardBadge('congruence_champion');
          if (t.includes('dilation') || t.includes('scale') || t.includes('reduction')) awardBadge('dilation_dynamo');
        }
      } else {
        profile.streak = 0;
      }

      save();
    }

    function recordQuizCompletion(quizLength, scorePercent, mode) {
      load();
      profile.quizzesCompleted += 1;
      awardXP(100); // Completion bonus

      if (quizLength >= 10) {
        awardBadge('quiz_champion');
      }
      if ((mode === 'mod1' || mode === 'mod1_final' || mode === 'module1_final') && scorePercent >= 80) {
        awardBadge('module1_master');
      }

      profile.history.push({
        date: new Date().toISOString(),
        mode: mode,
        length: quizLength,
        score: scorePercent
      });

      save();
    }

    function reset() {
      profile = defaultProfile();
      save();
    }

    function updateUIHeader() {
      if (typeof document === 'undefined') return;
      const p = load();
      const xpEl = document.getElementById('userXP') || document.getElementById('user-xp') || document.querySelector('.stat-pill.xp span:last-child');
      const streakEl = document.getElementById('userStreak') || document.getElementById('user-streak') || document.querySelector('.stat-pill.streak span:last-child');
      const levelEl = document.getElementById('userLevel') || document.getElementById('user-level-title') || document.querySelector('.user-level');
      const nameEl = document.querySelector('.user-name');

      if (xpEl) xpEl.textContent = p.xp + ' XP';
      if (streakEl) streakEl.textContent = p.streak + ' 🔥';
      if (levelEl) levelEl.textContent = 'Lv.' + p.level + ' ' + p.levelTitle;
      if (nameEl && (!nameEl.textContent || !nameEl.textContent.trim())) nameEl.textContent = p.name;

      BADGE_DEFINITIONS.forEach(function (b) {
        const badgeEl = document.getElementById('badge-' + b.id);
        if (badgeEl) {
          if (p.badges.includes(b.id)) {
            badgeEl.classList.remove('locked');
            badgeEl.classList.add('unlocked');
          } else {
            badgeEl.classList.add('locked');
            badgeEl.classList.remove('unlocked');
          }
        }
      });
    }

    return {
      get: load,
      save: save,
      awardXP: awardXP,
      awardBadge: awardBadge,
      recordAnswer: recordAnswer,
      recordQuizCompletion: recordQuizCompletion,
      reset: reset,
      updateUIHeader: updateUIHeader,
      BADGES: BADGE_DEFINITIONS,
      LEVELS: LEVEL_TITLES
    };
  })();

  // --- TOAST NOTIFICATIONS ---
  function showToast(message) {
    if (typeof document === 'undefined') return;
    let toast = document.getElementById('toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'toast';
      document.body.appendChild(toast);
    }
    toast.innerHTML = message;
    toast.classList.add('show');
    clearTimeout(toast._timer);
    toast._timer = setTimeout(function () {
      toast.classList.remove('show');
    }, 3200);
  }

  // --- TOPIC NAMES MAP ---
  const LESSON_TOPICS = {
    '1.1': 'Investigate Transformations',
    '1.2': 'Explore Translations',
    '1.3': 'Explore Reflections',
    '1.4': 'Explore Rotations',
    '1.5': 'Understand Congruent Figures',
    '2.1': 'Dilations',
    '2.2': 'Reductions & Enlargements',
    '2.3': 'Similar Figures'
  };

  // --- 1. AUTHENTIC MODULE 1 FINAL TEST (25 Authentic Questions from build_module1_final_test.py) ---
  const AUTHENTIC_MODULE1_FINAL_TEST = [
  {
    "id": "mod1-test-q1",
    "module": 1,
    "lesson": "1.1",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1.b",
    "dok": 1,
    "type": "multiple_choice",
    "question": "Roberto slides a rectangular picture frame $5\\text{ ft}$ to the right across a wall, and Dionne slides an isosceles triangular flag with base angles measuring $70^\\circ$ up a $9\\text{-meter}$ flagpole. Which statement correctly identifies the geometric properties preserved by these movements?",
    "options": [
      "The picture frame still has $4$ right angles ($90^\\circ$) and the flag still has $2$ congruent base angles ($70^\\circ$) because translations are rigid motions that preserve angle measures.",
      "The picture frame's angles increase due to horizontal displacement, while the flag's base angles decrease as it ascends.",
      "The picture frame preserves its right angles, but the flag's base angles change because vertical translations distort acute angles.",
      "The angle measures of both figures change in direct proportion to the distance each figure was translated."
    ],
    "correctAnswer": 0,
    "hint": "Recall that a translation is a rigid motion (isometry). Does sliding a physical object change the angles between its edges?",
    "explanation": "Step 1: Identify the transformation type: Sliding an object horizontally or vertically without turning or resizing is a pure translation.\nStep 2: Apply properties of rigid motions (isometries): Under CCSS 8.G.A.1.b, rigid motions (translations, reflections, and rotations) strictly preserve angle measures. Therefore, every angle in the image is congruent to its corresponding angle in the preimage.\nStep 3: Analyze each figure: Roberto's rectangular frame began with 4 right angles ($90^\\circ$) and retains all 4 right angles ($90^\\circ$). Dionne's isosceles triangular flag began with base angles of $70^\\circ$ each and retains both $70^\\circ$ angles.\nWhy other choices are incorrect: Choices B, C, and D violate the fundamental angle invariance principle of rigid motions by claiming angles change when an object is shifted."
  },
  {
    "id": "mod1-test-q2",
    "module": 1,
    "lesson": "1.1",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1.c",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Parallelogram $RSTU$ has opposite sides $\\overline{RS} \\parallel \\overline{UT}$ and $\\overline{RU} \\parallel \\overline{ST}$. Parallelogram $RSTU$ is rotated $180^\\circ$ clockwise about vertex $R$ to form image $R'S'T'U'$. How many pairs of parallel sides does the rotated image have, and why?",
    "options": [
      "$0$ pairs, because rotating a polygon reverses slope directions and breaks all parallelism.",
      "$1$ pair, because only horizontal side pairs maintain parallelism after a half-turn rotation.",
      "$2$ pairs, because a rotation is a rigid motion that maps parallel lines to parallel lines.",
      "$4$ pairs, because rotating around a vertex doubles each pair of parallel segments."
    ],
    "correctAnswer": 2,
    "hint": "Look at CCSS 8.G.A.1.c: what happens to parallel lines when a figure undergoes a rigid motion such as a rotation?",
    "explanation": "Step 1: Identify the initial figure properties: Parallelogram $RSTU$ has 2 pairs of parallel opposite sides: $\\overline{RS} \\parallel \\overline{UT}$ and $\\overline{RU} \\parallel \\overline{ST}$.\nStep 2: Apply the invariance of parallelism: Under CCSS 8.G.A.1.c, rigid motions (including rotations of any degree about any center) always map parallel lines to parallel lines. If line $L_1 \\parallel L_2$, then their image lines satisfy $L_1' \\parallel L_2'$.\nStep 3: Evaluate the image figure: The image $R'S'T'U'$ remains a parallelogram with exactly 2 pairs of parallel sides: $\\overline{R'S'} \\parallel \\overline{U'T'}$ and $\\overline{R'U'} \\parallel \\overline{S'T'}$.\nWhy other choices are incorrect: Choice A is false because rotations preserve parallelism. Choice B is false because both pairs are preserved, not just one. Choice D is false because a quadrilateral always has at most 2 pairs of opposite parallel sides."
  },
  {
    "id": "mod1-test-q3",
    "module": 1,
    "lesson": "1.1",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1",
    "dok": 2,
    "type": "multiple_choice",
    "question": "A student analyzes four transformations applied to a geometric figure on a coordinate plane:\nI. A slide $6\\text{ units}$ left and $2\\text{ units}$ down\nII. A reflection across the line $x = 3$\nIII. A rotation of $90^\\circ$ counterclockwise about the origin\nIV. A dilation centered at the origin with scale factor $k = 1.5$\nWhich of the following correctly classifies these transformations as rigid motions (isometries) and describes their effect on vertex orientation?",
    "options": [
      "I, II, and III are rigid motions because they preserve distances and angles; I and III preserve orientation, whereas II reverses orientation.",
      "All four transformations are rigid motions because geometric shape is preserved in all four cases.",
      "Only I and III are rigid motions; reflections and dilations are non-rigid transformations that alter side lengths.",
      "Only II and IV reverse orientation, while I, II, and III all alter side lengths."
    ],
    "correctAnswer": 0,
    "hint": "Think about which transformations keep the exact size (side lengths) of the figure unchanged, and which flip the figure like a mirror.",
    "explanation": "Step 1: Classify rigid vs. non-rigid motions: Rigid motions (isometries) preserve Euclidean distances (side lengths) and angle measures. Translations (I), reflections (II), and rotations (III) preserve distances and angles. Dilations (IV) with scale factor $k \\neq 1$ multiply all lengths by $k$ (here $1.5$), so IV is non-rigid.\nStep 2: Analyze vertex orientation: Translations (I) and rotations (III) are direct isometries (they preserve clockwise/counterclockwise vertex ordering). Reflections (II) are opposite isometries (they flip the figure across a reflection axis, reversing clockwise ordering to counterclockwise).\nWhy other choices are incorrect: Choice B is wrong because a dilation changes size and is non-rigid. Choice C is wrong because reflections strictly preserve side lengths and are rigid motions. Choice D incorrectly asserts that rigid motions alter side lengths."
  },
  {
    "id": "mod1-test-q4",
    "module": 1,
    "lesson": "1.1",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1.a",
    "dok": 1,
    "type": "multiple_choice",
    "question": "Halley cuts a square piece of plywood with a side length of $7\\text{ inches}$. She rotates the piece $90^\\circ$ counterclockwise. Next, Amelia has a rectangular table that measures $4\\text{ ft}$ wide and $5\\text{ ft}$ long, which she rotates $90^\\circ$ clockwise. What is the side length of Halley's plywood square and the perimeter of Amelia's table after their rotations?",
    "options": [
      "Halley's square has side length $9.9\\text{ inches}$; Amelia's table has perimeter $20\\text{ ft}$.",
      "Halley's square has side length $7\\text{ inches}$; Amelia's table has perimeter $18\\text{ ft}$.",
      "Halley's square has side length $3.5\\text{ inches}$; Amelia's table has perimeter $9\\text{ ft}$.",
      "Halley's square has side length $7\\text{ inches}$; Amelia's table has perimeter $14\\text{ ft}$."
    ],
    "correctAnswer": 1,
    "hint": "Do rotations change the length of sides or the total perimeter around an object?",
    "explanation": "Step 1: Understand the effect of a rotation on segment lengths: Under CCSS 8.G.A.1.a, rotations map line segments to line segments of the exact same length.\nStep 2: Evaluate Halley's square: Preimage side length = $7\\text{ in.}$ Since rotation is an isometry, each image side length remains exactly $7\\text{ in.}$\nStep 3: Evaluate Amelia's table: Preimage dimensions are width $= 4\\text{ ft}$ and length $= 5\\text{ ft}$. The perimeter of a rectangle is $P = 2(\\text{length} + \\text{width}) = 2(5 + 4) = 18\\text{ ft}$. Because all side lengths are invariant under rotation, the perimeter remains $18\\text{ ft}$.\nWhy other choices are incorrect: Choice A confuses side length with the diagonal $(\\approx 7\\sqrt{2} \\approx 9.9)$ or area. Choice C halves the dimensions. Choice D incorrectly computes $2 \\times 5 + 4 = 14$ instead of $2(5 + 4) = 18$."
  },
  {
    "id": "mod1-test-q5",
    "module": 1,
    "lesson": "1.1",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1.a",
    "dok": 2,
    "type": "multiple_choice",
    "question": "On line segment $\\overline{AB}$, point $C$ lies between $A$ and $B$ such that $AC = 3\\text{ cm}$ and $CB = 5\\text{ cm}$, giving a total length $AB = 8\\text{ cm}$. The segment is mapped to $\\overline{A'B'}$ by a rigid motion (isometry), with $C'$ being the image of point $C$. Which statement MUST be true?",
    "options": [
      "Point $C'$ can be displaced off line segment $\\overline{A'B'}$, forming a triangle with vertices $A', B', C'$.",
      "The total length $A'B' = 8\\text{ cm}$, but the position of $C'$ shifts such that $A'C' = C'B' = 4\\text{ cm}$.",
      "Point $C'$ lies on segment $\\overline{A'B'}$ between $A'$ and $B'$, with $A'C' = 3\\text{ cm}$, $C'B' = 5\\text{ cm}$, and $A'B' = 8\\text{ cm}$.",
      "The length $A'B'$ depends on whether the transformation was a reflection or a rotation."
    ],
    "correctAnswer": 2,
    "hint": "Rigid motions preserve collinearity (points on a line stay on a line) and betweenness (the order of points is maintained).",
    "explanation": "Step 1: Understand collinearity and betweenness invariance: Rigid motions preserve lines, line segments, distances, and point order. If points $A$, $C$, and $B$ are collinear with $C$ between $A$ and $B$, then their images $A'$, $C'$, and $B'$ are collinear with $C'$ between $A'$ and $B'$.\nStep 2: Verify distances: By distance preservation (CCSS 8.G.A.1.a), $d(A', C') = d(A, C) = 3\\text{ cm}$ and $d(C', B') = d(C, B) = 5\\text{ cm}$. Therefore, $A'B' = A'C' + C'B' = 3 + 5 = 8\\text{ cm}$.\nWhy other choices are incorrect: Choice A is false because rigid motions preserve lines (collinearity). Choice B is false because individual segment lengths are invariant, so $C'$ cannot become a midpoint. Choice D is false because all rigid motions (translations, reflections, rotations) preserve lengths identically."
  },
  {
    "id": "mod1-test-q6",
    "module": 1,
    "lesson": "1.2",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Triangle $ABC$ has vertices $A(-2, 3)$, $B(5, 4)$, and $C(-1, -1)$. The triangle is translated using the coordinate rule $(x, y) \\to (x - 3, y + 4)$. What are the coordinates of the image vertices $A'$, $B'$, and $C'$?",
    "options": [
      "$A'(-5, 7)$, $B'(2, 8)$, and $C'(-4, 3)$",
      "$A'(1, -1)$, $B'(8, 0)$, and $C'(2, -5)$",
      "$A'(-5, -1)$, $B'(2, 0)$, and $C'(-4, -5)$",
      "$A'(-6, 12)$, $B'(15, 16)$, and $C'(-3, -4)$"
    ],
    "correctAnswer": 0,
    "hint": "Subtract $3$ from each $x$-coordinate ($x - 3$) and add $4$ to each $y$-coordinate ($y + 4$).",
    "explanation": "Step 1: Apply the translation rule $(x, y) \\to (x - 3, y + 4)$ to each vertex individually.\nStep 2: Compute $A'$: $A(-2, 3) \\to (-2 - 3, 3 + 4) = (-5, 7)$.\nStep 3: Compute $B'$: $B(5, 4) \\to (5 - 3, 4 + 4) = (2, 8)$.\nStep 4: Compute $C'$: $C(-1, -1) \\to (-1 - 3, -1 + 4) = (-4, 3)$.\nThus, the image vertices are $A'(-5, 7)$, $B'(2, 8)$, and $C'(-4, 3)$.\nWhy other choices are incorrect: Choice B accidentally added $3$ and subtracted $4$ ($(x+3, y-4)$). Choice C subtracted $4$ from $y$. Choice D multiplied the coordinates instead of adding/subtracting."
  },
  {
    "id": "mod1-test-q7",
    "module": 1,
    "lesson": "1.2",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "A triangle with vertices $D(-1, 1)$, $E(2, -1)$, and $F(3, 0)$ is translated $2\\text{ units}$ right and $6\\text{ units}$ down. Which coordinate rule and set of image vertices represent this translation?",
    "options": [
      "Rule: $(x, y) \\to (x - 2, y + 6)$; Vertices: $D'(-3, 7)$, $E'(0, 5)$, $F'(1, 6)$",
      "Rule: $(x, y) \\to (x + 2, y + 6)$; Vertices: $D'(1, 7)$, $E'(4, 5)$, $F'(5, 6)$",
      "Rule: $(x, y) \\to (x - 6, y + 2)$; Vertices: $D'(-7, 3)$, $E'(-4, 1)$, $F'(-3, 2)$",
      "Rule: $(x, y) \\to (x + 2, y - 6)$; Vertices: $D'(1, -5)$, $E'(4, -7)$, $F'(5, -6)$"
    ],
    "correctAnswer": 3,
    "hint": "Moving 'right' adds to $x$, while moving 'down' subtracts from $y$.",
    "explanation": "Step 1: Write the algebraic translation rule: Moving $2\\text{ units}$ right means $x \\to x + 2$. Moving $6\\text{ units}$ down means $y \\to y - 6$. So the rule is $(x, y) \\to (x + 2, y - 6)$.\nStep 2: Calculate image of $D(-1, 1)$: $D'(-1 + 2, 1 - 6) = D'(1, -5)$.\nStep 3: Calculate image of $E(2, -1)$: $E'(2 + 2, -1 - 6) = E'(4, -7)$.\nStep 4: Calculate image of $F(3, 0)$: $F'(3 + 2, 0 - 6) = F'(5, -6)$.\nWhy other choices are incorrect: Choice A uses $(x - 2, y + 6)$ (left and up). Choice B uses $(x + 2, y + 6)$ (right and up). Choice C swaps the $x$ and $y$ translation amounts."
  },
  {
    "id": "mod1-test-q8",
    "module": 1,
    "lesson": "1.2",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Triangle $PQR$ has vertices $P(2, -4)$, $Q(4, -5)$, and $R(7, -2)$. After a translation, the image vertex $P'$ is located at $(-4, -1)$. What is the coordinate rule for this translation, and what are the coordinates of image vertex $Q'$?",
    "options": [
      "Rule: $(x, y) \\to (x + 6, y - 3)$; $Q'(10, -8)$",
      "Rule: $(x, y) \\to (x - 6, y + 3)$; $Q'(-2, -2)$",
      "Rule: $(x, y) \\to (x - 2, y + 5)$; $Q'(2, 0)$",
      "Rule: $(x, y) \\to (x - 6, y - 3)$; $Q'(-2, -8)$"
    ],
    "correctAnswer": 1,
    "hint": "Find the change in $x$ ($\\Delta x = x' - x$) and change in $y$ ($\\Delta y = y' - y$) from $P$ to $P'$.",
    "explanation": "Step 1: Determine the horizontal shift: $\\Delta x = x_{P'} - x_P = -4 - 2 = -6$.\nStep 2: Determine the vertical shift: $\\Delta y = y_{P'} - y_P = -1 - (-4) = -1 + 4 = +3$.\nStep 3: Formulate the coordinate rule: $(x, y) \\to (x - 6, y + 3)$.\nStep 4: Apply the rule to find $Q'$: Given $Q(4, -5)$, $Q'(4 - 6, -5 + 3) = Q'(-2, -2)$.\nWhy other choices are incorrect: Choice A reverses the signs of the shifts. Choice C calculates incorrect differences. Choice D subtracts $3$ instead of adding $3$ to $y$."
  },
  {
    "id": "mod1-test-q9",
    "module": 1,
    "lesson": "1.2",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Quadrilateral $WXYZ$ is first translated $5\\text{ units}$ right and $2\\text{ units}$ down. It is then translated an additional $3\\text{ units}$ left and $7\\text{ units}$ up. Which single translation rule maps quadrilateral $WXYZ$ directly to its final image position?",
    "options": [
      "$(x, y) \\to (x + 8, y + 9)$",
      "$(x, y) \\to (x + 2, y + 5)$",
      "$(x, y) \\to (x - 2, y - 5)$",
      "$(x, y) \\to (x + 2, y - 9)$"
    ],
    "correctAnswer": 1,
    "hint": "Combine the horizontal changes ($+5$ and $-3$) and the vertical changes ($-2$ and $+7$).",
    "explanation": "Step 1: Write the algebraic expression for the first translation $T_1$: $(x, y) \\to (x + 5, y - 2)$.\nStep 2: Apply the second translation $T_2$ to the result: $(x', y') \\to (x' - 3, y' + 7)$.\nStep 3: Substitute $x' = x + 5$ and $y' = y - 2$ into $T_2$:\n$x'' = (x + 5) - 3 = x + 2$\n$y'' = (y - 2) + 7 = y + 5$\nTherefore, the combined translation rule is $(x, y) \\to (x + 2, y + 5)$.\nWhy other choices are incorrect: Choice A adds the magnitudes without respecting direction ($5+3=8$ and $2+7=9$). Choice C reverses the net signs. Choice D subtracts $7$ instead of adding $7$."
  },
  {
    "id": "mod1-test-q10",
    "module": 1,
    "lesson": "1.2",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "A game graphic on a coordinate grid is translated using the rule $(x, y) \\to (x - 8, y + 5)$. If the translated image of a key vertex is located at $S'(3, -2)$, what were the coordinates of the original preimage vertex $S$?",
    "options": [
      "$S(-5, 3)$",
      "$S(-5, -7)$",
      "$S(11, -7)$",
      "$S(11, 3)$"
    ],
    "correctAnswer": 2,
    "hint": "You are given the image $(x', y') = (3, -2)$. Work backwards to find the original $(x, y)$.",
    "explanation": "Step 1: Set up the equations from the coordinate rule $(x', y') = (x - 8, y + 5)$:\n$x - 8 = 3$\n$y + 5 = -2$\nStep 2: Solve for the preimage coordinates $x$ and $y$:\n$x = 3 + 8 = 11$\n$y = -2 - 5 = -7$\nStep 3: Check by applying the rule forward to $S(11, -7)$:\n$11 - 8 = 3$ and $-7 + 5 = -2$, which matches $S'(3, -2)$.\nWhy other choices are incorrect: Choice A mistakenly applied the translation rule forward to the image point ($3 - 8 = -5, -2 + 5 = 3$). Choices B and D contain sign errors when solving the linear equations."
  },
  {
    "id": "mod1-test-q11",
    "module": 1,
    "lesson": "1.3",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 1,
    "type": "multiple_choice",
    "question": "Point $M(2, -4)$ is reflected across the $x$-axis to produce $M'$, and point $N(-3, 1)$ is reflected across the $y$-axis to produce $N'$. What are the coordinates of $M'$ and $N'$?",
    "options": [
      "$M'(2, 4)$ and $N'(3, 1)$",
      "$M'(-2, -4)$ and $N'(-3, -1)$",
      "$M'(-2, 4)$ and $N'(3, -1)$",
      "$M'(-4, 2)$ and $N'(1, -3)$"
    ],
    "correctAnswer": 0,
    "hint": "Reflection across the $x$-axis negates $y$: $(x, -y)$. Reflection across the $y$-axis negates $x$: $(-x, y)$.",
    "explanation": "Step 1: Apply the $x$-axis reflection rule $(x, y) \\to (x, -y)$ to point $M(2, -4)$:\n$x' = 2$, $y' = -(-4) = 4 \\implies M'(2, 4)$.\nStep 2: Apply the $y$-axis reflection rule $(x, y) \\to (-x, y)$ to point $N(-3, 1)$:\n$x' = -(-3) = 3$, $y' = 1 \\implies N'(3, 1)$.\nWhy other choices are incorrect: Choice B swaps the rules (negating $x$ for the $x$-axis and negating $y$ for the $y$-axis). Choice C negates both coordinates (which is a $180^\\circ$ rotation). Choice D swaps the $x$ and $y$ values."
  },
  {
    "id": "mod1-test-q12",
    "module": 1,
    "lesson": "1.3",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1",
    "dok": 2,
    "type": "multiple_choice",
    "question": "In a coordinate plane, the vertices of $\\triangle ABC$ are $A(1, 2)$, $B(4, 2)$, and $C(2, 5)$. The vertices of its reflected image $\\triangle A'B'C'$ are $A'(-5, 2)$, $B'(-8, 2)$, and $C'(-6, 5)$. What is the equation of the line of reflection?",
    "options": [
      "$y = 2$",
      "$x = -2$",
      "$x = -1$",
      "$y = -2$"
    ],
    "correctAnswer": 1,
    "hint": "The line of reflection is the perpendicular bisector of the segment connecting any preimage point and its image point. Find the midpoint of $\\overline{AA'}$.",
    "explanation": "Step 1: Understand the geometric definition of a reflection line: The line of reflection is the perpendicular bisector of every segment connecting a preimage point to its corresponding image point.\nStep 2: Compare corresponding points $A(1, 2)$ and $A'(-5, 2)$:\nThe $y$-coordinates are identical ($y = 2$), while the $x$-coordinates change from $1$ to $-5$. The segment $\\overline{AA'}$ is horizontal, so the line of reflection must be vertical (perpendicular to horizontal).\nStep 3: Find the midpoint of $\\overline{AA'}$:\n$x_{\\text{mid}} = \\frac{1 + (-5)}{2} = \\frac{-4}{2} = -2$.\nCheck with $B(4, 2)$ and $B'(-8, 2)$: $\\frac{4 + (-8)}{2} = -2$.\nCheck with $C(2, 5)$ and $C'(-6, 5)$: $\\frac{2 + (-6)}{2} = -2$.\nTherefore, the line of reflection is the vertical line $x = -2$.\nWhy other choices are incorrect: Choice A ($y = 2$) is a horizontal line passing through the vertices, not a perpendicular bisector. Choice C miscalculates the midpoint. Choice D is horizontal instead of vertical."
  },
  {
    "id": "mod1-test-q13",
    "module": 1,
    "lesson": "1.3",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Which coordinate rule represents a reflection across the line $y = x$, and what is the image of point $K(-4, 7)$ under this reflection?",
    "options": [
      "Rule: $(x, y) \\to (-y, -x)$; Image: $K'(-7, 4)$",
      "Rule: $(x, y) \\to (-x, -y)$; Image: $K'(4, -7)$",
      "Rule: $(x, y) \\to (x, -y)$; Image: $K'(-4, -7)$",
      "Rule: $(x, y) \\to (y, x)$; Image: $K'(7, -4)$"
    ],
    "correctAnswer": 3,
    "hint": "Reflecting across the diagonal line $y = x$ interchanges the roles of $x$ and $y$.",
    "explanation": "Step 1: Recall the coordinate rule for reflection across the line $y = x$: Every point $(x, y)$ swaps its coordinates: $(x, y) \\to (y, x)$.\nStep 2: Apply the rule to point $K(-4, 7)$:\n$x' = y = 7$\n$y' = x = -4$\nThus, $K'(7, -4)$.\nWhy other choices are incorrect: Choice A, $(x, y) \\to (-y, -x)$, represents a reflection across the line $y = -x$. Choice B, $(x, y) \\to (-x, -y)$, represents a $180^\\circ$ rotation about the origin. Choice C, $(x, y) \\to (x, -y)$, represents a reflection across the $x$-axis."
  },
  {
    "id": "mod1-test-q14",
    "module": 1,
    "lesson": "1.3",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1.a",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Point $P(5, 3)$ is reflected across the horizontal line $y = -1$ to produce image point $P'$. What are the coordinates of $P'$, and what is the total distance between $P$ and $P'$?",
    "options": [
      "Coordinates: $P'(5, -3)$; Total distance: $6\\text{ units}$",
      "Coordinates: $P'(-7, 3)$; Total distance: $12\\text{ units}$",
      "Coordinates: $P'(5, -5)$; Total distance: $8\\text{ units}$",
      "Coordinates: $P'(5, -1)$; Total distance: $4\\text{ units}$"
    ],
    "correctAnswer": 2,
    "hint": "Find the vertical distance from $P$ to the line $y = -1$, then move that same distance past the line.",
    "explanation": "Step 1: Determine the distance from $P(5, 3)$ to the line $y = -1$:\nThe point has $y = 3$. The vertical distance to $y = -1$ is $d = 3 - (-1) = 4\\text{ units}$.\nStep 2: Find the coordinates of $P'$:\nUnder reflection across a horizontal line, the $x$-coordinate remains unchanged ($x' = 5$). The $y$-coordinate is $4\\text{ units}$ below the reflection line: $y' = -1 - 4 = -5$. Thus, $P'(5, -5)$.\nStep 3: Calculate the total distance between $P$ and $P'$:\nDistance $= 2 \\times d = 2 \\times 4 = 8\\text{ units}$ (or $|3 - (-5)| = 8\\text{ units}$).\nWhy other choices are incorrect: Choice A reflects across the $x$-axis ($y = 0$). Choice B reflects horizontally instead of vertically. Choice D places the point directly on the line of reflection."
  },
  {
    "id": "mod1-test-q15",
    "module": 1,
    "lesson": "1.3",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Right triangle $XYZ$ has vertices listed in clockwise order: $X(1, 1)$, $Y(1, 4)$, and $Z(5, 1)$. Triangle $XYZ$ is reflected across the $y$-axis to produce $\\triangle X'Y'Z'$. Which statement correctly describes the side lengths and vertex orientation of $\\triangle X'Y'Z'$?",
    "options": [
      "Side lengths are preserved, and the vertex order $X' \\to Y' \\to Z'$ remains clockwise because all rigid motions preserve orientation.",
      "Side lengths are preserved ($X'Y' = 3$, $X'Z' = 4$, $Y'Z' = 5$), but the vertex order $X' \\to Y' \\to Z'$ is now counterclockwise because reflection reverses orientation.",
      "Side lengths are negated ($X'Y' = -3$, $X'Z' = -4$), and the vertex order remains clockwise.",
      "The hypotenuse length decreases because the figure was flipped across the vertical axis."
    ],
    "correctAnswer": 1,
    "hint": "Reflections are 'mirror images' (opposite isometries). What does a mirror do to left and right?",
    "explanation": "Step 1: Compute side lengths of preimage $\\triangle XYZ$:\n$XY = |4 - 1| = 3$\n$XZ = |5 - 1| = 4$\n$YZ = \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5$.\nStep 2: Apply reflection across the $y$-axis: $(x, y) \\to (-x, y)$:\n$X'(-1, 1)$, $Y'(-1, 4)$, $Z'(-5, 1)$.\nDistances are strictly preserved: $X'Y' = 3$, $X'Z' = 4$, $Y'Z' = 5$.\nStep 3: Analyze orientation:\nIn $\\triangle XYZ$, tracing $X(1, 1) \\to Y(1, 4) \\to Z(5, 1) \\to X(1, 1)$ proceeds in a clockwise direction. In $\\triangle X'Y'Z'$, tracing $X'(-1, 1) \\to Y'(-1, 4) \\to Z'(-5, 1) \\to X'(-1, 1)$ proceeds in a counterclockwise direction.\nThus, reflection reverses orientation.\nWhy other choices are incorrect: Choice A fails to recognize that reflection reverses orientation. Choice C mentions negative lengths, which cannot exist. Choice D violates distance invariance (CCSS 8.G.A.1.a)."
  },
  {
    "id": "mod1-test-q16",
    "module": 1,
    "lesson": "1.4",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 1,
    "type": "multiple_choice",
    "question": "The coordinates of a figure are transformed using the algebraic rule $(x, y) \\to (-y, x)$. Which transformation is represented by this rule?",
    "options": [
      "A $90^\\circ$ counterclockwise rotation about the origin",
      "A $90^\\circ$ clockwise rotation about the origin",
      "A $180^\\circ$ rotation about the origin",
      "A reflection across the line $y = -x$"
    ],
    "correctAnswer": 0,
    "hint": "Test a point like $(1, 0)$: under $(x, y) \\to (-y, x)$, where does it go?",
    "explanation": "Step 1: Test with the standard unit point $(1, 0)$ on the positive $x$-axis:\nApplying $(x, y) \\to (-y, x)$: $(1, 0) \\to (0, 1)$.\nMoving from $(1, 0)$ to $(0, 1)$ is a turn of $90^\\circ$ counterclockwise (or $270^\\circ$ clockwise).\nStep 2: Confirm with $(0, 1)$ on the positive $y$-axis:\n$(0, 1) \\to (-1, 0)$, which continues the $90^\\circ$ counterclockwise rotation.\nStep 3: Verify the standard rotation rules about the origin:\n- $90^\\circ$ counterclockwise (or $270^\\circ$ clockwise): $(x, y) \\to (-y, x)$\n- $180^\\circ$ rotation: $(x, y) \\to (-x, -y)$\n- $90^\\circ$ clockwise (or $270^\\circ$ counterclockwise): $(x, y) \\to (y, -x)$\nWhy other choices are incorrect: Choice B is $(y, -x)$. Choice C is $(-x, -y)$. Choice D is $(-y, -x)$."
  },
  {
    "id": "mod1-test-q17",
    "module": 1,
    "lesson": "1.4",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Parallelogram $ABCD$ has a vertex at $A(3, -5)$. The parallelogram is rotated $90^\\circ$ clockwise about the origin. What are the coordinates of the image vertex $A'$?",
    "options": [
      "$A'(5, 3)$",
      "$A'(-3, 5)$",
      "$A'(-5, -3)$",
      "$A'(5, -3)$"
    ],
    "correctAnswer": 2,
    "hint": "The coordinate rule for a $90^\\circ$ clockwise rotation about the origin is $(x, y) \\to (y, -x)$.",
    "explanation": "Step 1: Identify the rotation rule: A $90^\\circ$ clockwise rotation about the origin maps each point $(x, y)$ to $(y, -x)$.\nStep 2: Substitute the coordinates of $A(3, -5)$ into the rule:\nHere, $x = 3$ and $y = -5$.\n$x' = y = -5$\n$y' = -x = -(3) = -3$\nStep 3: Write the resulting coordinate pair: $A'(-5, -3)$.\nWhy other choices are incorrect: Choice A is $(-y, x)$, which is a $90^\\circ$ counterclockwise rotation ($(-(-5), 3) = (5, 3)$). Choice B is $(-x, -y)$, which is a $180^\\circ$ rotation. Choice D has an incorrect sign on the new $x$-coordinate."
  },
  {
    "id": "mod1-test-q18",
    "module": 1,
    "lesson": "1.4",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Triangle $RST$ has vertices $R(-4, 2)$, $S(-1, 5)$, and $T(-2, 1)$. The triangle is rotated $180^\\circ$ about the origin. What are the coordinates of the image vertices, and how does a $180^\\circ$ clockwise rotation compare to a $180^\\circ$ counterclockwise rotation?",
    "options": [
      "Image vertices: $R'(-2, 4)$, $S'(-5, 1)$, $T'(-1, 2)$; clockwise and counterclockwise produce perpendicular images.",
      "Image vertices: $R'(4, 2)$, $S'(1, 5)$, $T'(2, 1)$; clockwise rotates right, counterclockwise rotates left.",
      "Image vertices: $R'(-4, -2)$, $S'(-1, -5)$, $T'(-2, -1)$; only counterclockwise negates the $y$-coordinate.",
      "Image vertices: $R'(4, -2)$, $S'(1, -5)$, $T'(2, -1)$; both directions yield the identical image."
    ],
    "correctAnswer": 3,
    "hint": "Rotating a full half-circle ($180^\\circ$) lands on the exact same opposite ray whether you turn clockwise or counterclockwise: $(x, y) \\to (-x, -y)$.",
    "explanation": "Step 1: Identify the coordinate rule for a $180^\\circ$ rotation: A half-turn ($180^\\circ$) about the origin negates both coordinates: $(x, y) \\to (-x, -y)$.\nStep 2: Compute each vertex:\n$R(-4, 2) \\to (-(-4), -(2)) = (4, -2)$\n$S(-1, 5) \\to (-(-1), -(5)) = (1, -5)$\n$T(-2, 1) \\to (-(-2), -(1)) = (2, -1)$\nStep 3: Compare rotational directions: Because $180^\\circ + 180^\\circ = 360^\\circ$ (a full circle), rotating $180^\\circ$ clockwise lands in the exact same position as rotating $180^\\circ$ counterclockwise.\nWhy other choices are incorrect: Choice A swaps and negates coordinates. Choice B only negates the $x$-coordinate. Choice C only negates the $y$-coordinate."
  },
  {
    "id": "mod1-test-q19",
    "module": 1,
    "lesson": "1.4",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.1",
    "dok": 2,
    "type": "multiple_choice",
    "question": "A regular hexagon is centered at the origin of a coordinate plane. What is the smallest positive angle of rotation about its center that maps the hexagon onto itself, and what is its total order of rotational symmetry?",
    "options": [
      "Smallest angle: $60^\\circ$; Order of rotational symmetry: $6$",
      "Smallest angle: $90^\\circ$; Order of rotational symmetry: $4$",
      "Smallest angle: $120^\\circ$; Order of rotational symmetry: $3$",
      "Smallest angle: $45^\\circ$; Order of rotational symmetry: $8$"
    ],
    "correctAnswer": 0,
    "hint": "A regular polygon with $n$ sides has $n$ equal central angles. Divide $360^\\circ$ by the number of sides $n$.",
    "explanation": "Step 1: Identify the number of sides: A regular hexagon has $n = 6$ congruent sides and $6$ congruent central angles.\nStep 2: Calculate the fundamental angle of rotational symmetry:\nAngle $= \\frac{360^\\circ}{n} = \\frac{360^\\circ}{6} = 60^\\circ$.\nStep 3: Determine the order of rotational symmetry: The figure maps onto itself at rotations of $60^\\circ, 120^\\circ, 180^\\circ, 240^\\circ, 300^\\circ,$ and $360^\\circ$ (or $0^\\circ$). That is a total of $6$ rotational alignments within one complete turn, so its order of rotational symmetry is $6$.\nWhy other choices are incorrect: Choice B corresponds to a square ($n=4$). Choice C uses $120^\\circ$ (which maps the hexagon onto itself, but is not the *smallest* positive angle). Choice D corresponds to a regular octagon ($n=8$)."
  },
  {
    "id": "mod1-test-q20",
    "module": 1,
    "lesson": "1.4",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Rectangle $PQRS$ is rotated $270^\\circ$ counterclockwise about the origin. Vertex $P$ has coordinates $(-6, 2)$. Which coordinate rule represents a $270^\\circ$ counterclockwise rotation, and what are the coordinates of $P'$?",
    "options": [
      "Rule: $(x, y) \\to (-y, x)$; Coordinates: $P'(-2, -6)$",
      "Rule: $(x, y) \\to (y, -x)$; Coordinates: $P'(2, 6)$",
      "Rule: $(x, y) \\to (-x, -y)$; Coordinates: $P'(6, -2)$",
      "Rule: $(x, y) \\to (-y, -x)$; Coordinates: $P'(-2, 6)$"
    ],
    "correctAnswer": 1,
    "hint": "Notice that $270^\\circ$ counterclockwise is the exact same rotational motion as $90^\\circ$ clockwise: $(x, y) \\to (y, -x)$.",
    "explanation": "Step 1: Connect angles of rotation: Turning $270^\\circ$ counterclockwise leaves $360^\\circ - 270^\\circ = 90^\\circ$ clockwise. Hence, a $270^\\circ$ counterclockwise rotation is mathematically equivalent to a $90^\\circ$ clockwise rotation.\nStep 2: Recall the coordinate rule: $(x, y) \\to (y, -x)$.\nStep 3: Evaluate point $P(-6, 2)$ where $x = -6$ and $y = 2$:\n$x' = y = 2$\n$y' = -x = -(-6) = 6$\nSo $P'(2, 6)$.\nWhy other choices are incorrect: Choice A is the rule for $90^\\circ$ counterclockwise ($270^\\circ$ clockwise). Choice C is the rule for $180^\\circ$ rotation. Choice D is a reflection across the line $y = -x$."
  },
  {
    "id": "mod1-test-q21",
    "module": 1,
    "lesson": "1.5",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.3",
    "dok": 2,
    "type": "multiple_choice",
    "question": "The point $(a, b)$ is reflected across the $x$-axis and then translated $4\\text{ units}$ to the right and $2\\text{ units}$ down. Which expression gives the coordinates of the final image point?",
    "options": [
      "$(-a + 4, b - 2)$",
      "$(a + 4, -b + 2)$",
      "$(a - 4, -b - 2)$",
      "$(a + 4, -b - 2)$"
    ],
    "correctAnswer": 3,
    "hint": "Apply each transformation step-by-step: first reflect across the $x$-axis ($(x, y) \\to (x, -y)$), then apply the translation to the new coordinates.",
    "explanation": "Step 1: Perform the reflection across the $x$-axis: The rule is $(x, y) \\to (x, -y)$. Applying this to $(a, b)$ yields the intermediate point $(a, -b)$.\nStep 2: Apply the translation: Translating $4\\text{ units}$ to the right adds $4$ to the $x$-coordinate: $x' = a + 4$. Translating $2\\text{ units}$ down subtracts $2$ from the current $y$-coordinate: $y' = -b - 2$.\nStep 3: Combine into the final coordinate pair: $(a + 4, -b - 2)$.\nWhy other choices are incorrect: Choice A incorrectly negates $a$ (as if reflected across the $y$-axis). Choice B adds $2$ instead of subtracting $2$. Choice C subtracts $4$ from $a$ (translating left instead of right)."
  },
  {
    "id": "mod1-test-q22",
    "module": 1,
    "lesson": "1.5",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.2",
    "dok": 3,
    "type": "multiple_choice",
    "question": "Consider the point $T(3, 2)$ subjected to two different sequences of transformations:\nSequence 1: Translate $3\\text{ units}$ up, then reflect across the $x$-axis.\nSequence 2: Reflect across the $x$-axis, then translate $3\\text{ units}$ up.\nWhat are the resulting coordinates for Sequence 1 and Sequence 2, respectively, and what does this demonstrate?",
    "options": [
      "Sequence 1 produces $(3, 5)$; Sequence 2 produces $(3, 5)$; this demonstrates that transformations always commute.",
      "Sequence 1 produces $(-3, -5)$; Sequence 2 produces $(3, -1)$; this demonstrates that reflections always reverse the $x$-coordinate.",
      "Sequence 1 produces $(3, -5)$; Sequence 2 produces $(3, 1)$; this demonstrates that the order of transformations matters (transformations do not generally commute).",
      "Sequence 1 produces $(3, -1)$; Sequence 2 produces $(3, -5)$; this demonstrates that translating up is equivalent to subtracting from $y$."
    ],
    "correctAnswer": 2,
    "hint": "Work through each sequence step-by-step from left to right. Does the order in which you perform operations affect the final answer?",
    "explanation": "Step 1: Calculate Sequence 1 for $T(3, 2)$:\n- First translate $3$ up: $(3, 2) \\to (3, 2 + 3) = (3, 5)$.\n- Then reflect across the $x$-axis: $(3, 5) \\to (3, -5)$.\nStep 2: Calculate Sequence 2 for $T(3, 2)$:\n- First reflect across the $x$-axis: $(3, 2) \\to (3, -2)$.\n- Then translate $3$ up: $(3, -2) \\to (3, -2 + 3) = (3, 1)$.\nStep 3: Compare results: Since $(3, -5) \\neq (3, 1)$, reversing the order of the reflection and translation produces different final locations. In mathematics, this means transformations are generally non-commutative ($T \\circ R \\neq R \\circ T$).\nWhy other choices are incorrect: Choice A falsely claims both sequences yield $(3, 5)$. Choice B introduces erroneous sign flips on the $x$-coordinate. Choice D swaps the results of the two sequences."
  },
  {
    "id": "mod1-test-q23",
    "module": 1,
    "lesson": "1.5",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.2",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Trapezoid $WXYZ$ has angles $\\angle W = 100^\\circ$ and $\\angle X = 80^\\circ$, with side lengths $WX = 5\\text{ cm}$ and $ZW = 7\\text{ cm}$. Trapezoid $WXYZ$ is rotated $90^\\circ$ clockwise about its center and then translated $6\\text{ units}$ down and $4\\text{ units}$ right to produce trapezoid $HJKL$, where vertices $W, X, Y, Z$ correspond to $H, J, K, L$. What are the measure of $\\angle J$ and the length of side $\\overline{LH}$?",
    "options": [
      "$m\\angle J = 100^\\circ$ and $LH = 5\\text{ cm}$",
      "$m\\angle J = 80^\\circ$ and $LH = 7\\text{ cm}$",
      "$m\\angle J = 170^\\circ$ and $LH = 13\\text{ cm}$",
      "$m\\angle J = 80^\\circ$ and $LH = 11\\text{ cm}$"
    ],
    "correctAnswer": 1,
    "hint": "Identify corresponding parts between the preimage $WXYZ$ and image $HJKL$. Which vertex corresponds to $J$? Which side corresponds to $\\overline{LH}$?",
    "explanation": "Step 1: Identify congruence of figures: Because the sequence consists entirely of rigid motions (a rotation followed by a translation), $\\text{Trapezoid } WXYZ \\cong \\text{Trapezoid } HJKL$ by CCSS 8.G.A.2.\nStep 2: Map corresponding vertices and angles: The correspondence is $W \\mapsto H$, $X \\mapsto J$, $Y \\mapsto K$, and $Z \\mapsto L$. Therefore, $\\angle J$ corresponds to $\\angle X$. Since rigid motions preserve angle measures, $m\\angle J = m\\angle X = 80^\\circ$.\nStep 3: Map corresponding sides: Segment $\\overline{LH}$ connects the 4th and 1st vertices, corresponding to $\\overline{ZW}$. Since rigid motions preserve distances, $LH = ZW = 7\\text{ cm}$.\nWhy other choices are incorrect: Choice A swaps the corresponding angle and side with $W$ and $WX$. Choice C adds the translation amounts to the angle and side length (a common misconception). Choice D adds the translation horizontal shift ($4$) to side length ($7+4=11$)."
  },
  {
    "id": "mod1-test-q24",
    "module": 1,
    "lesson": "1.5",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.2",
    "dok": 3,
    "type": "multiple_choice",
    "question": "Triangle $J$ has vertices at $(1, 1)$, $(4, 1)$, and $(1, 3)$. Triangle $P$ has vertices at $(-1, -1)$, $(-1, -4)$, and $(-3, -1)$. Which sequence of transformations proves that Triangle $J$ is congruent to Triangle $P$?",
    "options": [
      "A reflection across the $y$-axis followed by a $90^\\circ$ counterclockwise rotation about the origin",
      "A translation $2\\text{ units}$ left and $2\\text{ units}$ down followed by a dilation of scale factor $1$",
      "A reflection across the $x$-axis followed by a reflection across the line $y = x$",
      "A $180^\\circ$ rotation about the origin followed by a reflection across the horizontal line $y = 0$"
    ],
    "correctAnswer": 0,
    "hint": "Trace what happens to the right-angle vertex $(1, 1)$ and long leg $(4, 1)$ under each sequence of transformations.",
    "explanation": "Step 1: Test Choice A step-by-step:\n- Step 1a: Reflect across the $y$-axis: $(x, y) \\to (-x, y)$:\n  $(1, 1) \\to (-1, 1)$\n  $(4, 1) \\to (-4, 1)$\n  $(1, 3) \\to (-1, 3)$\n- Step 1b: Rotate $90^\\circ$ counterclockwise about the origin: $(x', y') \\to (-y', x')$:\n  $(-1, 1) \\to (-1, -1)$\n  $(-4, 1) \\to (-1, -4)$\n  $(-1, 3) \\to (-3, -1)$\nNotice that the resulting set of vertices is $\\{(-1, -1), (-1, -4), (-3, -1)\\}$, which matches Triangle $P$ exactly!\nStep 2: Conclusion on congruence: Since Triangle $P$ is obtained from Triangle $J$ through a sequence of rigid motions (a reflection followed by a rotation), Triangle $J \\cong \\text{Triangle } P$ by CCSS 8.G.A.2.\nWhy other choices are incorrect: Choice B only translates $(1, 1) \\to (-1, -1)$ but leaves $(4, 1) \\to (2, -1) \\neq (-1, -4)$. Choice C maps $(x, y) \\to (x, -y) \\to (-y, x)$ which is a pure rotation, but Triangle $J$ and Triangle $P$ have opposite orientations so a single reflection must be involved. Choice D does not map $(4, 1)$ to $(-1, -4)$."
  },
  {
    "id": "mod1-test-q25",
    "module": 1,
    "lesson": "1.5",
    "topic": "Module 1 Final Review",
    "standard": "CCSS.MATH.CONTENT.8.G.A.2",
    "dok": 2,
    "type": "multiple_choice",
    "question": "Pentagon $PQRST$ undergoes a sequence of rigid motions consisting of a reflection across a vertical line followed by a translation $2\\text{ units}$ left and $5\\text{ units}$ up to produce pentagon $ABCDE$, with vertex correspondence $P \\mapsto A$, $Q \\mapsto B$, $R \\mapsto C$, $S \\mapsto D$, and $T \\mapsto E$. Which statement about the two pentagons is FALSE?",
    "options": [
      "Pentagon $ABCDE$ is congruent to Pentagon $PQRST$ ($\text{Pentagon } ABCDE \\cong \\text{Pentagon } PQRST$).",
      "Side length $DC$ is equal to side length $SR$ ($DC = SR$).",
      "The angle measure of $\\angle E$ equals the angle measure of $\\angle T$ ($m\\angle E = m\\angle T$).",
      "The clockwise vertex orientation of Pentagon $ABCDE$ is identical to the clockwise vertex orientation of Pentagon $PQRST$."
    ],
    "correctAnswer": 3,
    "hint": "Recall the effect of reflections on orientation: an odd number of reflections reverses the clockwise order of vertices.",
    "explanation": "Step 1: Recall congruence and rigid motion properties (CCSS 8.G.A.2): Any figure produced by a sequence of rigid motions (reflections and translations) is congruent to the original figure. Thus, Pentagon $ABCDE \\cong \\text{Pentagon } PQRST$ (Choice A is TRUE).\nStep 2: Check corresponding parts of congruent figures: Corresponding side lengths are equal, so $DC = SR$ (Choice B is TRUE). Corresponding angle measures are equal, so $m\\angle E = m\\angle T$ (Choice C is TRUE).\nStep 3: Analyze orientation: A reflection reverses the orientation of a figure (flips clockwise to counterclockwise). A translation preserves orientation. Therefore, a sequence consisting of one reflection and one translation results in a reversed orientation. Tracing vertices $A \\to B \\to C \\to D \\to E$ proceeds in the opposite rotational sense compared to $P \\to Q \\to R \\to S \\to T$.\nTherefore, the statement claiming orientation is identical is FALSE and is the correct answer.\nWhy other choices are incorrect: Choices A, B, and C are all true statements about congruent polygons resulting from rigid motions."
  }
];

  // --- 2. AUTHENTIC LESSON PRACTICE (20 Questions per lesson from build_lesson_1_x.py) ---
  const AUTHENTIC_LESSON_PRACTICE = {
  "1.1": [
    {
      "id": "p-1-1-mcq-1",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 1,
      "type": "multiple_choice",
      "question": "Which of the following transformations represents a **rigid motion** (isometry) on the coordinate plane?",
      "options": [
        "Doubling the $x$-coordinates while keeping the $y$-coordinates the same: $(x, y) \\to (2x, y)$",
        "Dilating a polygon by a scale factor of $0.5$ centered at the origin: $(x, y) \\to (0.5x, 0.5y)$",
        "Tripling both coordinates: $(x, y) \\to (3x, 3y)$",
        "Translating a polygon $5\\text{ units}$ to the left and $3\\text{ units}$ up: $(x, y) \\to (x - 5, y + 3)$"
      ],
      "correctAnswer": 3,
      "hint": "A rigid motion (isometry) must preserve all segment lengths and angle measures without stretching, shrinking, or distorting the shape.",
      "explanation": "Option D is correct because a translation slides every point by a fixed distance without changing side lengths or angles, making it a rigid motion (isometry). Options A, B, and C are non-rigid transformations: Option A is a horizontal stretch that distorts proportions; Options B and C are dilations that alter segment lengths and areas."
    },
    {
      "id": "p-1-1-mcq-2",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 1,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle ABC$ has side lengths $AB = 7.4\\text{ cm}$, $BC = 5.1\\text{ cm}$, and $AC = 9.8\\text{ cm}$. If $\\triangle ABC$ is rotated $90^\\circ$ clockwise about the origin to form $\\triangle A'B'C'$, what is the exact length of side $\\overline{A'B'}$?",
      "options": [
        "$5.1\\text{ cm}$",
        "$9.8\\text{ cm}$",
        "$7.4\\text{ cm}$",
        "Cannot be determined without knowing the center of rotation"
      ],
      "correctAnswer": 2,
      "hint": "Remember the distance preservation property of rigid motions: $\\text{Length}(A'B') = \\text{Length}(AB)$.",
      "explanation": "Option C is correct because rotation is a rigid motion (isometry). Under any rigid motion, line segments are taken to line segments of the exact same length: $\\text{Length}(A'B') = \\text{Length}(AB) = 7.4\\text{ cm}$. Options A and B cite lengths of other sides ($BC$ and $AC$). Option D is incorrect because the preservation of distance holds regardless of the chosen center of rotation."
    },
    {
      "id": "p-1-1-mcq-3",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In right triangle $\\triangle DEF$, $m\\angle D = 38^\\circ$ and $m\\angle E = 90^\\circ$. The triangle is reflected across the $y$-axis to produce $\\triangle D'E'F'$. What is the measure of angle $\\angle F'$?",
      "options": [
        "$38^\\circ$",
        "$90^\\circ$",
        "$142^\\circ$",
        "$52^\\circ$"
      ],
      "correctAnswer": 3,
      "hint": "First calculate the third angle in the preimage using the triangle angle sum ($180^\\circ$), then apply angle preservation.",
      "explanation": "Option D is correct. In preimage $\\triangle DEF$, the sum of angles is $180^\\circ$, so $m\\angle F = 180^\\circ - (90^\\circ + 38^\\circ) = 52^\\circ$. Because reflection is a rigid motion, angle measures are preserved: $m\\angle F' = m\\angle F = 52^\\circ$. Option A is $m\\angle D'$, Option B is $m\\angle E'$, and Option C is the obtuse supplement ($180^\\circ - 38^\\circ$)."
    },
    {
      "id": "p-1-1-mcq-4",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Trapezoid $PQRS$ has parallel bases $\\overline{PQ} \\parallel \\overline{RS}$, which are separated by a perpendicular distance of $4.5\\text{ cm}$. After trapezoid $PQRS$ is translated $6\\text{ units}$ down and reflected across a vertical line to form $P'Q'R'S'$, which statement must be true?",
      "options": [
        "$\\overline{P'Q'}$ and $\\overline{R'S'}$ intersect at a right angle.",
        "$\\overline{P'Q'} \\parallel \\overline{R'S'}$ and the perpendicular distance between them remains $4.5\\text{ cm}$.",
        "$\\overline{P'Q'} \\parallel \\overline{R'S'}$, but the distance between them increases to $9.0\\text{ cm}$ because two transformations were performed.",
        "$\\overline{P'Q'}$ is no longer parallel to $\\overline{R'S'}$ because reflection changes line slopes."
      ],
      "correctAnswer": 1,
      "hint": "Consider standard 8.G.A.1.c: Parallel lines are taken to parallel lines under rigid motions.",
      "explanation": "Option B is correct. Translations and reflections are rigid motions, and their composition is also a rigid motion. Under rigid motions, parallel lines map to parallel lines ($\\overline{P'Q'} \\parallel \\overline{R'S'}$), and distances between corresponding points or parallel segments are invariant ($4.5\\text{ cm}$). Options A and D falsely claim parallelism is lost. Option C confuses performing multiple rigid motions with scaling/dilating."
    },
    {
      "id": "p-1-1-mcq-5",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Three points $L$, $M$, and $N$ lie on the same straight line with $M$ located between $L$ and $N$. Given $LM = 3.2\\text{ cm}$ and $MN = 4.8\\text{ cm}$, the segment undergoes a rigid motion mapping $L \\to L'$, $M \\to M'$, and $N \\to N'$. Which deduction is mathematically guaranteed?",
      "options": [
        "$L'$, $M'$, and $N'$ form the vertices of a scalene triangle with perimeter $16\\text{ cm}$.",
        "$L'$, $M'$, and $N'$ are non-collinear because turning a line curves it into an arc.",
        "$L'$, $M'$, and $N'$ remain collinear, $M'$ is between $L'$ and $N'$, and $L'N' = 8.0\\text{ cm}$.",
        "$M'$ is no longer between $L'$ and $N'$ because rigid motions reverse the internal order of points."
      ],
      "correctAnswer": 2,
      "hint": "Rigid motions preserve collinearity (lines map to lines) and betweenness of points on a line.",
      "explanation": "Option C is correct. Rigid motions take straight lines to straight lines and preserve betweenness of points and segment addition. In the preimage, $LN = LM + MN = 3.2 + 4.8 = 8.0\\text{ cm}$. Under rigid motion, $L'M' = 3.2\\text{ cm}$, $M'N' = 4.8\\text{ cm}$, points remain collinear with $M'$ between $L'$ and $N'$, and $L'N' = 8.0\\text{ cm}$. Options A and B contradict the fact that lines map to lines. Option D is incorrect because betweenness along a segment is preserved."
    },
    {
      "id": "p-1-1-mcq-6",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle JKL$ has vertices named in clockwise order around its perimeter. The triangle undergoes a rotation of $180^\\circ$ about the origin, followed by a reflection across the vertical line $x = 2$. What is the vertex orientation of the final image $J''K''L''$?",
      "options": [
        "Clockwise, because both rotations and reflections preserve clockwise vertex order.",
        "Undefined, because multiple transformations destroy vertex order.",
        "Clockwise, because a $180^\\circ$ rotation reverses orientation and the reflection reverses it back.",
        "Counterclockwise, because rotation preserves clockwise orientation, and reflection reverses it to counterclockwise."
      ],
      "correctAnswer": 3,
      "hint": "Recall orientation behavior: translations and rotations are direct isometries (preserve orientation); reflections are opposite isometries (reverse orientation).",
      "explanation": "Option D is correct. A rotation is a direct isometry, so after the $180^\\circ$ turn, the vertices $J'K'L'$ remain in clockwise order. Then, reflecting across the line $x = 2$ is an opposite isometry, which flips the chirality (orientation) from clockwise to counterclockwise. Option C contains a common student misconception: rotations do NOT reverse orientation; only reflections reverse orientation."
    },
    {
      "id": "p-1-1-mcq-7",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A parallelogram has base $b = 8\\text{ cm}$, slant side $s = 5\\text{ cm}$, perpendicular height $h = 4\\text{ cm}$, perimeter $P = 26\\text{ cm}$, and area $A = 32\\text{ cm}^2$. If it undergoes a $90^\\circ$ rotation followed by a translation of $\\langle -4, 7 \\rangle$, what are the perimeter and area of the resulting image?",
      "options": [
        "$\\text{Perimeter} = 26\\text{ cm}$ and $\\text{Area} = 32\\text{ cm}^2$",
        "$\\text{Perimeter} = 52\\text{ cm}$ and $\\text{Area} = 64\\text{ cm}^2$",
        "$\\text{Perimeter} = 26\\text{ cm}$ and $\\text{Area} = 16\\text{ cm}^2$",
        "$\\text{Perimeter} = 32\\text{ cm}$ and $\\text{Area} = 26\\text{ cm}^2$"
      ],
      "correctAnswer": 0,
      "hint": "Since all side lengths and angles are strictly invariant under rigid motions, what happens to their perimeter and enclosed area?",
      "explanation": "Option A is correct. Both rotation and translation are rigid motions (isometries). Rigid motions preserve all linear distances ($A'B' = AB$), meaning the perimeter remains $P' = P = 26\\text{ cm}$. They also preserve angle measures and height, guaranteeing that the enclosed two-dimensional area is completely invariant: $A' = A = 32\\text{ cm}^2$. Options B, C, and D incorrectly alter perimeter or area."
    },
    {
      "id": "p-1-1-mcq-8",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A student graphs polygon $ABCD$ in Quadrant I. She translates the polygon $10\\text{ units}$ left and $12\\text{ units}$ down into Quadrant III. A peer argues: *'Since the coordinates changed from positive to negative, the shape got smaller and its area became negative.'* How should this argument be refuted?",
      "options": [
        "The peer is correct because coordinates in Quadrant III represent negative geometric lengths.",
        "The peer is incorrect; coordinates only specify position on the grid. Distance and area depend on absolute differences, which remain invariant under translation.",
        "The peer is incorrect because translations only change the area when moving diagonally.",
        "The peer is partially correct; side lengths stay positive, but area is mathematically defined as negative in Quadrant III."
      ],
      "correctAnswer": 1,
      "hint": "Look at the teacher edition note on misconceptions: shifting a figure into a different quadrant changes location, not size or physical attributes.",
      "explanation": "Option B is correct. A major misconception addressed in the HMH Teacher Edition is confusing coordinate signs with geometric measures. Coordinates denote position, but lengths are Euclidean distances $\\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$, which are always non-negative. Translation is a rigid motion, so side lengths, angles, perimeter, and area are 100% preserved. Area cannot be negative. Options A, C, and D reflect misconceptions."
    },
    {
      "id": "p-1-1-mcq-9",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A graphic design software applies the algebraic mapping $(x, y) \\to (x + 4, 2y)$ to a rectangle with vertices $(0,0)$, $(3,0)$, $(3,2)$, and $(0,2)$. Which statement correctly classifies this transformation?",
      "options": [
        "It is a rigid motion because all corners remain $90^\\circ$ right angles.",
        "It is a rigid motion because it includes a translation of $+4$ along the $x$-axis.",
        "It is NOT a rigid motion because the vertical sides are stretched by a factor of $2$, altering side lengths and doubling area.",
        "It is a rigid motion because it is a combination of a slide and a flip."
      ],
      "correctAnswer": 2,
      "hint": "Check whether corresponding side lengths are equal before and after the mapping.",
      "explanation": "Option C is correct. In the preimage, the height is $|2 - 0| = 2$. In the image, the $y$-coordinates are doubled, so the height becomes $|4 - 0| = 4$. Because the side length changed from $2$ to $4$, distance is not preserved ($A'B' \\neq AB$). A transformation that alters distance is by definition non-rigid (here, a vertical stretch). Option A is wrong because preserving right angles alone is insufficient (as in dilations and stretches). Options B and D are factually inaccurate."
    },
    {
      "id": "p-1-1-mcq-10",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 3,
      "type": "multiple_choice",
      "question": "Consider the following claim: *'If a transformation preserves all angle measures of any polygon ($m\\angle A' = m\\angle A, m\\angle B' = m\\angle B, \\dots$), then the transformation is guaranteed to be a rigid motion.'* Which counterexample definitively disproves this claim?",
      "options": [
        "Rotating a square $90^\\circ$ clockwise about its center",
        "Dilating an equilateral triangle by a scale factor of $k = 3$, which keeps all angles at $60^\\circ$ but triples all side lengths",
        "Reflecting an isosceles trapezoid across the line $y = x$",
        "Translating a scalene triangle $5\\text{ units}$ horizontally and $2\\text{ units}$ vertically"
      ],
      "correctAnswer": 1,
      "hint": "A counterexample must show that angle preservation alone does not guarantee distance preservation.",
      "explanation": "Option B is correct. In a dilation by a scale factor of $k = 3$, all interior angles remain exactly $60^\\circ$, yet every side length is tripled ($s' = 3s$). Because side lengths are not preserved, the dilation is NOT a rigid motion. This proves that angle preservation alone is insufficient to guarantee an isometry; distance must also be preserved. Options A, C, and D are actual rigid motions and cannot serve as counterexamples."
    },
    {
      "id": "p-1-1-mcq-11",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle ABC$ has vertices $A(2, 1)$, $B(5, 1)$, and $C(2, 6)$. Under a transformation, the image vertices are $A'(-2, 1)$, $B'(-5, 1)$, and $C'(-2, 6)$. Which transformation was performed, and what happened to its vertex orientation?",
      "options": [
        "Reflection across the $y$-axis; vertex orientation reversed from clockwise to counterclockwise.",
        "Translation $4\\text{ units}$ left; vertex orientation was preserved.",
        "Rotation $180^\\circ$ about the origin; vertex orientation was preserved.",
        "Reflection across the $x$-axis; vertex orientation remained clockwise."
      ],
      "correctAnswer": 0,
      "hint": "Observe the coordinates: $(x, y) \\to (-x, y)$. What transformation negates only the $x$-coordinate?",
      "explanation": "Option A is correct. The coordinate rule $(x, y) \\to (-x, y)$ represents a reflection across the $y$-axis. In the preimage, tracing $A(2,1) \\to B(5,1) \\to C(2,6)$ moves along the base rightward, then up-left back to $A$, which is counterclockwise. In the image, $A'(-2,1) \\to B'(-5,1) \\to C'(-2,6)$ moves leftward along the base, then up-right, which is clockwise. Testing shows that reflection across a line always reverses orientation (swaps chirality). Option B is wrong because $B$ shifted by $-10$, not $-4$. Option C rule would be $(-x, -y)$. Option D rule would be $(x, -y)$."
    },
    {
      "id": "p-1-1-mcq-12",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A carpenter cuts boards to create identical pieces for a birdhouse (from Into Math TE). A board in the shape of a trapezoid has one pair of parallel sides that are $2\\text{ inches}$ apart. The carpenter turns the board one-quarter turn ($90^\\circ$) clockwise on her table. What is true about the parallel sides of the turned board?",
      "options": [
        "The parallel sides remain parallel and are still exactly $2\\text{ inches}$ apart.",
        "The sides are no longer parallel because turning them changed their directions.",
        "The parallel sides remain parallel, but the distance between them is now $2 \\times \\sqrt{2} \\approx 2.83\\text{ inches}$.",
        "The parallel sides become perpendicular to each other."
      ],
      "correctAnswer": 0,
      "hint": "Teacher Edition problem 7 & 12 note: Parallel lines stay parallel, and the distance between them remains constant under rigid motions.",
      "explanation": "Option A is correct. As emphasized in Into Math TE Lesson 1.1 Problems 7 and 11-12, when a shape undergoes a turn (rotation), rigid motion properties guarantee that: (1) parallel lines are taken to parallel lines, and (2) the distance between parallel lines remains exactly the same ($2\\text{ inches}$). Option B is a misconception. Options C and D incorrectly assume rotating changes metric distance between lines."
    },
    {
      "id": "p-1-1-mcq-13",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Line segment $\\overline{AB}$ is horizontal with length $AB = 6\\text{ cm}$. A student rotates the segment $45^\\circ$ counterclockwise about endpoint $A$. The student claims: *'Because the segment is now slanted diagonally across grid squares, its length must be greater than $6\\text{ cm}$.'* What error did the student make?",
      "options": [
        "The student should have measured the length in inches instead of centimeters.",
        "The student forgot that rotating a segment by $45^\\circ$ cuts its length in half.",
        "The student failed to realize that only $90^\\circ$ and $180^\\circ$ rotations preserve lengths.",
        "The student confused the visual slope/slant with geometric length; rotations are rigid motions, so distance is invariant regardless of tilt."
      ],
      "correctAnswer": 3,
      "hint": "Teacher Edition Common Error: Students often believe that diagonal segments are automatically longer than horizontal ones, confusing coordinate grid alignment with physical length.",
      "explanation": "Option D is correct. A well-documented misconception in the HMH Into Math TE is that students equate diagonal orientation with increased length (often thinking of the hypotenuse of grid squares). However, rotation is a rigid motion (isometry), which guarantees that the distance between endpoints remains invariant: $\\text{Length}(A'B') = \\text{Length}(AB) = 6\\text{ cm}$. Options A, B, and C contain false mathematical claims."
    },
    {
      "id": "p-1-1-mcq-14",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle PQR$ has angle measures $m\\angle P = 40^\\circ$, $m\\angle Q = 60^\\circ$, and $m\\angle R = 80^\\circ$, with an area of $24\\text{ cm}^2$. It is reflected across line $\\ell$ and then rotated $60^\\circ$ about point $P'$. What are the interior angle sum and area of the resulting triangle $P''Q''R''$?",
      "options": [
        "Interior angle sum $= 240^\\circ$, $\\text{Area} = 24\\text{ cm}^2$",
        "Interior angle sum $= 360^\\circ$, $\\text{Area} = 48\\text{ cm}^2$",
        "Interior angle sum $= 180^\\circ$, $\\text{Area} = 24\\text{ cm}^2$",
        "Interior angle sum $= 180^\\circ$, $\\text{Area} = 12\\text{ cm}^2$"
      ],
      "correctAnswer": 2,
      "hint": "Sequences of rigid motions preserve angle measures, side lengths, and area.",
      "explanation": "Option C is correct. The composition of two rigid motions (a reflection followed by a rotation) is also a rigid motion. Every individual angle measure is preserved ($40^\\circ, 60^\\circ, 80^\\circ$), so their sum remains strictly $180^\\circ$. Furthermore, because side lengths and altitudes are invariant, the area remains exactly $24\\text{ cm}^2$. Options A, B, and D incorrectly alter the angle sum or area."
    },
    {
      "id": "p-1-1-mcq-15",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Which of the following correctly describes how basic transformations affect the **orientation** (clockwise vs. counterclockwise ordering of vertices) of a figure?",
      "options": [
        "Translations and reflections preserve orientation; rotations reverse it.",
        "Translations and rotations preserve orientation (direct isometries); reflections reverse orientation (opposite isometries).",
        "Rotations and reflections preserve orientation; translations reverse it.",
        "All transformations (translations, rotations, reflections) reverse orientation."
      ],
      "correctAnswer": 1,
      "hint": "Think of looking at a clock face: when you slide it or turn it, the numbers still run clockwise. What happens when you look at it in a mirror?",
      "explanation": "Option B is correct. Translations (slides) and rotations (turns) keep vertices in the same relative clockwise order around the perimeter, so they are direct isometries. A reflection (flip) produces a mirror image, reversing the clockwise order to counterclockwise (or vice versa), making it an opposite isometry. Options A, C, and D misstate these fundamental properties."
    },
    {
      "id": "p-1-1-mcq-16",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 3,
      "type": "multiple_choice",
      "question": "On straight line segment $\\overline{AC}$, point $B$ lies between $A$ and $C$ such that $AB = x + 3$, $BC = 2x - 1$, and $AC = 14\\text{ cm}$. The segment undergoes a rigid motion mapping $A \\to A'$, $B \\to B'$, and $C \\to C'$. What is the length of image segment $\\overline{A'B'}$?",
      "options": [
        "$4\\text{ cm}$",
        "$5\\text{ cm}$",
        "$9\\text{ cm}$",
        "$7\\text{ cm}$"
      ],
      "correctAnswer": 3,
      "hint": "Use the segment addition postulate $AB + BC = AC$ to solve for $x$, find $AB$, and apply distance preservation.",
      "explanation": "Option D is correct. By betweenness and the segment addition postulate: $AB + BC = AC \\implies (x + 3) + (2x - 1) = 14 \\implies 3x + 2 = 14 \\implies 3x = 12 \\implies x = 4$. Therefore, $AB = 4 + 3 = 7\\text{ cm}$ (and $BC = 2(4) - 1 = 7\\text{ cm}$). Because a rigid motion preserves distances between all points, $A'B' = AB = 7\\text{ cm}$. Option A is the value of $x$, Option B is an arithmetic error, and Option C is $x+5$."
    },
    {
      "id": "p-1-1-mcq-17",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Which of the following coordinate rules represents a transformation that is **NEVER** a rigid motion?",
      "options": [
        "$(x, y) \\to (x - 7, y + 4)$",
        "$(x, y) \\to (-y, x)$",
        "$(x, y) \\to (x, -y)$",
        "$(x, y) \\to (3x, 3y)$"
      ],
      "correctAnswer": 3,
      "hint": "Look for a rule where coordinates are multiplied by a number other than $1$ or $-1$, scaling the size of the shape.",
      "explanation": "Option D is correct. The rule $(x, y) \\to (3x, 3y)$ multiplies all coordinates by $3$, creating a dilation with scale factor $k = 3$. This triples all segment lengths ($d' = 3d$) and multiplies the area by $3^2 = 9$. Because distance is not preserved, it is never a rigid motion. Option A is a translation, Option B is a $90^\\circ$ counterclockwise rotation, and Option C is a reflection across the $x$-axis\u2014all of which are rigid motions."
    },
    {
      "id": "p-1-1-mcq-18",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 3,
      "type": "multiple_choice",
      "question": "A student examines two rhombuses:\n- **Rhombus 1:** Side length $5\\text{ cm}$, perimeter $20\\text{ cm}$, and interior angles $74^\\circ$ and $106^\\circ$.\n- **Rhombus 2:** Side length $5\\text{ cm}$, perimeter $20\\text{ cm}$, and interior angles $60^\\circ$ and $120^\\circ$.\nCan Rhombus 2 be formed by applying a rigid motion to Rhombus 1?",
      "options": [
        "Yes, because both rhombuses have the exact same side lengths and perimeter of $20\\text{ cm}$.",
        "Yes, because turning a rhombus changes its angle measures to fit a new orientation.",
        "No, because rigid motions MUST preserve all angle measures, and $74^\\circ \\neq 60^\\circ$.",
        "No, because rigid motions cannot be applied to four-sided shapes."
      ],
      "correctAnswer": 2,
      "hint": "Recall: A rigid motion must preserve BOTH distance (side lengths) AND angle measures simultaneously.",
      "explanation": "Option C is correct. A rigid motion (isometry) requires the preservation of BOTH side lengths AND angle measures ($m\\angle A' = m\\angle A$). Although both shapes share the same side lengths ($5\\text{ cm}$) and perimeter ($20\\text{ cm}$), their angle measures differ ($74^\\circ \\neq 60^\\circ$). Because angle measures are not preserved, Rhombus 2 cannot be the image of Rhombus 1 under any rigid motion. Option A confuses perimeter equality with congruence. Option B is a common misconception."
    },
    {
      "id": "p-1-1-mcq-19",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Reginald draws regular hexagon $ABCDEF$ with side length $s = 4\\text{ cm}$ and three pairs of opposite parallel sides (from Into Math TE Wrap-Up Exit Ticket). He rotates the hexagon $120^\\circ$ counterclockwise about its center. Which statement accurately describes image $A'B'C'D'E'F'$?",
      "options": [
        "All side lengths remain $4\\text{ cm}$, all interior angles remain $120^\\circ$, opposite sides remain parallel, and perimeter is $24\\text{ cm}$.",
        "Side lengths increase to $6\\text{ cm}$ and opposite sides intersect because rotation turns sides in different directions.",
        "The interior angles increase by $120^\\circ$ to $240^\\circ$, but side lengths stay $4\\text{ cm}$.",
        "The hexagon becomes irregular because horizontal sides stay fixed while slanted sides rotate."
      ],
      "correctAnswer": 0,
      "hint": "See HMH Into Math TE page 31 Exit Ticket: Reginald rotates a regular hexagon. What is true of the angles, side lengths, and parallel sides?",
      "explanation": "Option A is correct. In the TE Wrap-Up Exit Ticket (page 31), students verify that when Reginald rotates a regular hexagon, angles stay the same ($120^\\circ$), side lengths stay the same ($4\\text{ cm}$), perimeter stays the same ($6 \\times 4 = 24\\text{ cm}$), and opposite parallel sides remain parallel. Rigid motions preserve all metric properties and parallelism uniformly across the entire polygon. Options B, C, and D are false."
    },
    {
      "id": "p-1-1-mcq-20",
      "module": 1,
      "lesson": "1.1",
      "topic": "Investigate Transformations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1",
      "dok": 3,
      "type": "multiple_choice",
      "question": "A mathematics class analyzes four statements about transformations:\n1. *Under any rigid motion, if line $m \\parallel \\text{line } n$, then their images satisfy $m' \\parallel n'$.*\n2. *If a transformation preserves the area of a rectangle, it is guaranteed to be a rigid motion.*\n3. *A reflection across a line preserves all side lengths and angle measures, but reverses vertex orientation (chirality).*\n4. *Translating a polygon from Quadrant I to Quadrant III reduces the side lengths of the polygon because the coordinates become negative.*\nWhich of these statements are mathematically **TRUE**?",
      "options": [
        "Statements 1 and 3 only",
        "Statements 1, 2, and 3 only",
        "Statements 2 and 4 only",
        "Statements 1, 3, and 4 only"
      ],
      "correctAnswer": 0,
      "hint": "Evaluate each statement individually: Statement 1 (parallelism), Statement 2 (can non-rigid shear or stretch preserve area?), Statement 3 (reflection properties), Statement 4 (quadrant misconception).",
      "explanation": "Option A is correct.\n- Statement 1 is TRUE: CCSS 8.G.A.1.c states that parallel lines are taken to parallel lines under rigid motions.\n- Statement 2 is FALSE: A horizontal stretch by $2$ combined with a vertical compression by $\\frac{1}{2}$ preserves area ($2 \\times \\frac{1}{2} = 1$), but distorts side lengths and angles, so it is NOT a rigid motion.\n- Statement 3 is TRUE: Reflections preserve distance and angle measures, but reverse vertex orientation from clockwise to counterclockwise.\n- Statement 4 is FALSE: Coordinates become negative, but side lengths are distances, which are invariant under translation.\nTherefore, only Statements 1 and 3 are true."
    }
  ],
  "1.2": [
    {
      "id": "p-1-2-mcq-1",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "A translation slides a geometric figure $6\\text{ units left}$ and $8\\text{ units up}$ on a coordinate plane. Which vector represents this transformation in component vector notation?",
      "options": [
        "$\\langle 6, -8 \\rangle$",
        "$\\langle -6, 8 \\rangle$",
        "$\\langle 8, -6 \\rangle$",
        "$\\langle -8, 6 \\rangle$"
      ],
      "correctAnswer": 1,
      "hint": "In vector notation $\\langle a, b \\rangle$, the first value $a$ represents horizontal change (negative for left, positive for right), and the second value $b$ represents vertical change (positive for up, negative for down).",
      "explanation": "A horizontal shift of 6 units to the left is represented by $a = -6$, and a vertical shift of 8 units up is represented by $b = +8$. Thus, the vector in component notation is $\\langle -6, 8 \\rangle$. Choice A reverses the positive and negative directions. Choices C and D swap the horizontal and vertical components."
    },
    {
      "id": "p-1-2-mcq-2",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "Which algebraic mapping rule correctly represents translating a polygon $4\\text{ units right}$ and $7\\text{ units down}$ on a Cartesian coordinate plane?",
      "options": [
        "$(x, y) \\to (x + 4, y - 7)$",
        "$(x, y) \\to (x - 4, y + 7)$",
        "$(x, y) \\to (x + 7, y - 4)$",
        "$(x, y) \\to (4x, -7y)$"
      ],
      "correctAnswer": 0,
      "hint": "Moving right increases the $x$-coordinate, while moving down decreases the $y$-coordinate.",
      "explanation": "Moving 4 units right adds 4 to each $x$-coordinate ($x \\to x + 4$). Moving 7 units down subtracts 7 from each $y$-coordinate ($y \\to y - 7$). Combining these gives $(x, y) \\to (x + 4, y - 7)$. Choice B incorrectly subtracts for right and adds for down. Choice C swaps the $x$ and $y$ shifts. Choice D uses multiplication, which describes a dilation rather than a translation."
    },
    {
      "id": "p-1-2-mcq-3",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "Point $W(-5, 9)$ undergoes the pure horizontal translation $(x, y) \\to (x + 8, y)$. What are the coordinates of the image point $W'$?",
      "options": [
        "$(-13, 9)$",
        "$(-5, 17)$",
        "$(3, 9)$",
        "$(3, 17)$"
      ],
      "correctAnswer": 2,
      "hint": "Only the $x$-coordinate is modified by adding 8; the $y$-coordinate remains completely unchanged.",
      "explanation": "Applying the rule $(x, y) \\to (x + 8, y)$ to $W(-5, 9)$: $x' = -5 + 8 = 3$, and $y' = 9$. Thus, $W' = (3, 9)$. Choice A mistakenly subtracts 8 ($-5 - 8 = -13$). Choice B mistakenly adds 8 to the $y$-coordinate. Choice D erroneously adds 8 to both coordinates."
    },
    {
      "id": "p-1-2-mcq-4",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "A line segment on a blueprint with endpoint $P(4, -3)$ is translated vertically such that its image is $P'(4, -11)$. Which translation rule was applied to the segment?",
      "options": [
        "$(x, y) \\to (x, y - 8)$",
        "$(x, y) \\to (x, y + 8)$",
        "$(x, y) \\to (x - 8, y)$",
        "$(x, y) \\to (x, y - 14)$"
      ],
      "correctAnswer": 0,
      "hint": "Calculate the vertical change: $b = y_{\\text{image}} - y_{\\text{preimage}} = -11 - (-3)$.",
      "explanation": "The $x$-coordinate does not change ($4 \\to 4$), so there is zero horizontal displacement. The vertical displacement is $b = y' - y = -11 - (-3) = -11 + 3 = -8$, meaning the segment moved 8 units down. The mapping rule is $(x, y) \\to (x, y - 8)$. Choice B incorrectly adds 8 instead of subtracting. Choice C applies the shift horizontally. Choice D adds $-11$ and $-3$ to get $-14$."
    },
    {
      "id": "p-1-2-mcq-5",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $DEF$ has vertices $D(-3, 4)$, $E(1, 6)$, and $F(2, -1)$. The triangle is translated according to the rule $(x, y) \\to (x + 5, y - 6)$. What are the coordinates of vertex $D'$?",
      "options": [
        "$(-8, 10)$",
        "$(2, 10)$",
        "$(-8, -2)$",
        "$(2, -2)$"
      ],
      "correctAnswer": 3,
      "hint": "Substitute $x = -3$ and $y = 4$ directly into the algebraic rule: $x' = -3 + 5$ and $y' = 4 - 6$.",
      "explanation": "Substituting $D(-3, 4)$ into $(x + 5, y - 6)$ yields $x' = -3 + 5 = 2$ and $y' = 4 - 6 = -2$. Therefore, $D' = (2, -2)$. Choice A subtracts 5 and adds 6 ($(-8, 10)$). Choice B mistakenly adds 6 to $y$ ($4 + 6 = 10$). Choice C subtracts 5 from $x$ ($-3 - 5 = -8$)."
    },
    {
      "id": "p-1-2-mcq-6",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In a computer graphic animation, polygon vertex $K(7, -3)$ maps to image vertex $K'(-1, 5)$ under a translation. Which algebraic rule describes this translation?",
      "options": [
        "$(x, y) \\to (x + 8, y - 8)$",
        "$(x, y) \\to (x - 8, y + 8)$",
        "$(x, y) \\to (x - 6, y + 2)$",
        "$(x, y) \\to (x + 6, y - 2)$"
      ],
      "correctAnswer": 1,
      "hint": "Always subtract the preimage coordinates from the image coordinates: $a = x' - x$ and $b = y' - y$.",
      "explanation": "Calculate the horizontal displacement: $a = x' - x = -1 - 7 = -8$. Calculate the vertical displacement: $b = y' - y = 5 - (-3) = 5 + 3 = 8$. Thus, the rule is $(x, y) \\to (x - 8, y + 8)$. Choice A subtracts image from preimage ($7 - (-1) = 8$), which reverses the direction vector. Choices C and D add coordinates instead of computing differences."
    },
    {
      "id": "p-1-2-mcq-7",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "After a translation using the rule $(x, y) \\to (x - 6, y + 9)$, the image of point $M$ is $M'(2, -4)$. What were the coordinates of the original preimage point $M$?",
      "options": [
        "$(8, -13)$",
        "$(-4, 5)$",
        "$(8, 5)$",
        "$(-4, -13)$"
      ],
      "correctAnswer": 0,
      "hint": "Work backward from the image coordinates by applying inverse operations: solve $x - 6 = 2$ and $y + 9 = -4$.",
      "explanation": "To recover the preimage from the image, apply the inverse operations: $x = x' + 6 = 2 + 6 = 8$, and $y = y' - 9 = -4 - 9 = -13$. Thus, $M = (8, -13)$. Verifying forward: $(8 - 6, -13 + 9) = (2, -4) = M'$. Choice B erroneously applies the forward rule to $M'$ ($2 - 6 = -4, -4 + 9 = 5$). Choice C adds 9 to $y$ instead of subtracting. Choice D subtracts 6 from $x$."
    },
    {
      "id": "p-1-2-mcq-8",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $ABC$ lies in **Quadrant II** with vertex $A(-4, 5)$. The triangle is translated by the rule $(x, y) \\to (x + 9, y - 8)$. In which quadrant of the coordinate plane does the image vertex $A'$ lie?",
      "options": [
        "Quadrant I",
        "Quadrant II",
        "Quadrant III",
        "Quadrant IV"
      ],
      "correctAnswer": 3,
      "hint": "Calculate the image coordinates $A'(x', y')$ and inspect their signs: $(+, +)$ is Quadrant I, $(-, +)$ is Quadrant II, $(-, -)$ is Quadrant III, and $(+, -)$ is Quadrant IV.",
      "explanation": "Applying the translation rule to $A(-4, 5)$: $x' = -4 + 9 = 5$ (positive) and $y' = 5 - 8 = -3$ (negative). An ordered pair with a positive $x$-value and negative $y$-value $(5, -3)$ lies in **Quadrant IV**. Choice A represents Quadrant I ($x > 0, y > 0$). Choice B represents Quadrant II ($x < 0, y > 0$). Choice C represents Quadrant III ($x < 0, y < 0$)."
    },
    {
      "id": "p-1-2-mcq-9",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "Rectangle $PQRS$ has side lengths $PQ = 8\\text{ cm}$ and $QR = 5\\text{ cm}$, with $m\\angle P = 90^\\circ$. If $PQRS$ is translated $12\\text{ units left}$ and $15\\text{ units down}$ to form rectangle $P'Q'R'S'$, which statement is **NOT** true?",
      "options": [
        "The perimeter of $P'Q'R'S'$ is greater than the perimeter of $PQRS$ because the figure was translated by a large distance.",
        "The length of segment $P'Q'$ is equal to $8\\text{ cm}$.",
        "$m\\angle P' = 90^\\circ$.",
        "Segment $P'Q'$ is parallel to segment $PQ$."
      ],
      "correctAnswer": 0,
      "hint": "A translation is a rigid motion (isometry). Does sliding a shape across a flat plane change its perimeter or dimensions?",
      "explanation": "Translations are rigid motions that preserve side lengths, angle measures, perimeter, area, and parallelism. Sliding a figure never stretches or shrinks it, so the perimeter remains exactly $2(8 + 5) = 26\\text{ cm}$. Therefore, statement A is false (making it the correct answer to the question). Choices B, C, and D are all fundamental invariant properties preserved under translation."
    },
    {
      "id": "p-1-2-mcq-10",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "On a coordinate grid, line segment $\\overline{AB}$ connects $A(1, 2)$ to $B(4, 8)$, giving it a slope of $m = \\frac{8 - 2}{4 - 1} = 2$. Segment $\\overline{AB}$ is translated by $(x, y) \\to (x - 5, y + 3)$ to create image segment $\\overline{A'B'}$. What is the slope of $\\overline{A'B'}$?",
      "options": [
        "$-2$",
        "$\\frac{1}{2}$",
        "$2$",
        "$-\\frac{3}{5}$"
      ],
      "correctAnswer": 2,
      "hint": "Under a translation, line segments map to parallel line segments. What do you know about the slopes of parallel lines?",
      "explanation": "Translations preserve the orientation and steepness of lines; every translated segment is parallel to its preimage segment. Since parallel lines have identical slopes, the slope of $\\overline{A'B'}$ is equal to the slope of $\\overline{AB}$, which is $2$. Calculating directly: $A'(-4, 5)$ and $B'(-1, 11)$; slope $= \\frac{11 - 5}{-1 - (-4)} = \\frac{6}{3} = 2$. Choice A is the negative slope. Choice B is the reciprocal slope. Choice D confuses the slope with the ratio of translation vector components."
    },
    {
      "id": "p-1-2-mcq-11",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A polygon is translated on a coordinate grid according to the vector $\\langle 6, -8 \\rangle$. What is the straight-line distance that each vertex of the polygon travels during this translation?",
      "options": [
        "$14\\text{ units}$",
        "$10\\text{ units}$",
        "$2\\text{ units}$",
        "$\\sqrt{28}\\text{ units}$"
      ],
      "correctAnswer": 1,
      "hint": "Use the Pythagorean theorem $d = \\sqrt{a^2 + b^2}$ to find the length (magnitude) of the translation vector.",
      "explanation": "The straight-line Euclidean distance traveled by any point under vector $\\langle a, b \\rangle$ is given by $d = \\sqrt{a^2 + b^2}$. Here, $d = \\sqrt{6^2 + (-8)^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10\\text{ units}$. Choice A simply adds the absolute shifts $6 + 8 = 14$ (taxicab distance, not straight-line distance). Choice C subtracts the components ($8 - 6 = 2$). Choice D subtracts the squares ($\\sqrt{64 - 36} = \\sqrt{28}$)."
    },
    {
      "id": "p-1-2-mcq-12",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $XYZ$ is translated along vector $\\langle -5, 12 \\rangle$ to form Triangle $X'Y'Z'$. Vertex $X$ travels a straight-line distance of $13\\text{ units}$ to $X'$. How far does vertex $Z$ travel to reach its image $Z'$?",
      "options": [
        "Exactly $13\\text{ units}$",
        "More than $13\\text{ units}$ if $Z$ is farther from the origin than $X$",
        "Less than $13\\text{ units}$ because $Z$ is at the opposite end of the triangle",
        "It cannot be determined without knowing the exact initial coordinates of $Z$"
      ],
      "correctAnswer": 0,
      "hint": "By definition, does a translation move every point by the same distance, or do different points travel different distances?",
      "explanation": "By definition, a translation slides EVERY point of a figure by the exact same distance and in the exact same direction along parallel paths. Because the vector is $\\langle -5, 12 \\rangle$, every point in the triangle travels $d = \\sqrt{(-5)^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13\\text{ units}$. Choices B, C, and D are misconceptions; distance traveled during a translation is constant across all points and does not depend on position relative to the origin."
    },
    {
      "id": "p-1-2-mcq-13",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A geometric figure is first translated by $T_1: (x, y) \\to (x + 4, y - 3)$, and then its image is translated by $T_2: (x, y) \\to (x - 9, y + 8)$. Which single algebraic rule represents the composition of these two successive translations?",
      "options": [
        "$(x, y) \\to (x + 13, y - 11)$",
        "$(x, y) \\to (x + 5, y - 5)$",
        "$(x, y) \\to (x - 5, y + 5)$",
        "$(x, y) \\to (x - 36, y - 24)$"
      ],
      "correctAnswer": 2,
      "hint": "Add the corresponding horizontal displacements together ($a_1 + a_2$) and the vertical displacements together ($b_1 + b_2$).",
      "explanation": "To combine successive translations, sum their respective components: $a_{\\text{net}} = 4 + (-9) = -5$, and $b_{\\text{net}} = -3 + 8 = 5$. Thus, the single equivalent mapping rule is $(x, y) \\to (x - 5, y + 5)$. Choice A subtracts the shifts ($4 - (-9) = 13, -3 - 8 = -11$). Choice B reverses the signs of the net shifts. Choice D multiplies the shifts."
    },
    {
      "id": "p-1-2-mcq-14",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.2 *Turn and Talk*, students explore moving a chess piece $1\\text{ space right and } 2\\text{ spaces up}$ versus moving it $2\\text{ spaces up and } 1\\text{ space right}$. What mathematical property explains why both sequences result in the exact same final position?",
      "options": [
        "The distributive property of multiplication over addition",
        "The commutative property of addition for real numbers ($x + a_1 + a_2 = x + a_2 + a_1$)",
        "The reflexive property of geometric congruence",
        "The inverse property of coordinate reflections"
      ],
      "correctAnswer": 1,
      "hint": "Translations are represented by adding constants to coordinate values. Does the order in which you add two real numbers change their sum?",
      "explanation": "Translations modify coordinates by adding constants: $x \\to x + a_1 + a_2$ and $y \\to y + b_1 + b_2$. Because addition of real numbers is commutative ($a_1 + a_2 = a_2 + a_1$ and $b_1 + b_2 = b_2 + b_1$), changing the sequence of the translations results in the identical final coordinates. Translations commute with each other. Choices A, C, and D cite unrelated properties."
    },
    {
      "id": "p-1-2-mcq-15",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "An agricultural inspection drone hovers over a crop field at coordinate $(15, 28)$, where coordinates are measured in meters. The flight computer executes a translation along vector $\\langle -32, -45 \\rangle$ to inspect an irrigation valve. What are the new coordinates of the drone?",
      "options": [
        "$(-17, -17)$",
        "$(47, 73)$",
        "$(-17, 73)$",
        "$(47, -17)$"
      ],
      "correctAnswer": 0,
      "hint": "Add the vector components directly to the drone's initial coordinates: $x' = 15 + (-32)$ and $y' = 28 + (-45)$.",
      "explanation": "Applying the translation vector $\\langle -32, -45 \\rangle$: $x' = 15 + (-32) = -17\\text{ m}$, and $y' = 28 + (-45) = -17\\text{ m}$. Thus, the drone's new position is $(-17, -17)$. Choice B incorrectly subtracts negative values ($15 - (-32) = 47, 28 - (-45) = 73$). Choice C computes $x$ correctly but adds for $y$. Choice D adds for $x$ but subtracts for $y$."
    },
    {
      "id": "p-1-2-mcq-16",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "On a chessboard modeled as a coordinate grid (HMH TE p. 38), a knight begins at position $(3, 2)$. A player makes two consecutive legal moves: first sliding 1 unit right and 2 units up, and then sliding 2 units left and 1 unit up. What is the knight's final coordinate position?",
      "options": [
        "$(4, 4)$",
        "$(0, 5)$",
        "$(2, 3)$",
        "$(2, 5)$"
      ],
      "correctAnswer": 3,
      "hint": "Calculate the intermediate position after the first move, then apply the second move to that result.",
      "explanation": "Move 1 (1 right, 2 up): $(x, y) \\to (x + 1, y + 2)$, landing the knight at $(3 + 1, 2 + 2) = (4, 4)$. Move 2 (2 left, 1 up): $(x, y) \\to (x - 2, y + 1)$, moving the knight from $(4, 4)$ to $(4 - 2, 4 + 1) = (2, 5)$. Choice A is the intermediate coordinate after only move 1. Choice B subtracts 2 from the initial $x$ without adding 1. Choice C subtracts 1 from $y$ on the second move instead of adding 1."
    },
    {
      "id": "p-1-2-mcq-17",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "An architect places Building $A$ on a city planning grid with vertices at $(1, 1)$, $(3, 1)$, $(3, 3)$, and $(1, 3)$ (a $2 \\times 2$ square; HMH TE p. 42-43). A developer proposes four new building footprints. Which proposal represents a **valid translation** of Building $A$?",
      "options": [
        "Building $B'$ with vertices at $(1, 1)$, $(4, 1)$, $(4, 4)$, and $(1, 4)$",
        "Building $C'$ with vertices at $(-1, 1)$, $(-3, 1)$, $(-3, 3)$, and $(-1, 3)$",
        "Building $A'$ with vertices at $(5, -4)$, $(7, -4)$, $(7, -2)$, and $(5, -2)$",
        "Building $D'$ with vertices at $(2, 2)$, $(6, 2)$, $(6, 6)$, and $(2, 6)$"
      ],
      "correctAnswer": 2,
      "hint": "In a true translation, every vertex shifts by the exact same $a$ and $b$, and the dimensions ($2 \\times 2$) and orientation remain unchanged.",
      "explanation": "In Building $A'$, every single vertex is shifted by the identical rule $(x, y) \\to (x + 4, y - 5)$: $(1+4, 1-5)=(5, -4)$, $(3+4, 1-5)=(7, -4)$, $(3+4, 3-5)=(7, -2)$, and $(1+4, 3-5)=(5, -2)$. The size ($2 \\times 2$) and orientation are perfectly preserved. Choice A has dimensions $3 \\times 3$ (dilation). Choice B has vertices with opposite $x$-coordinates, representing a reflection across the $y$-axis. Choice D has dimensions $4 \\times 4$ (dilation by factor 2)."
    },
    {
      "id": "p-1-2-mcq-18",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Parallelogram $ABCD$ is translated on a coordinate plane. Vertex $A(-2, 3)$ maps to $A'(4, -1)$. If vertex $C$ is located at $(1, -4)$, what are the coordinates of image vertex $C'$?",
      "options": [
        "$(-5, 0)$",
        "$(7, -8)$",
        "$(7, 0)$",
        "$(-5, -8)$"
      ],
      "correctAnswer": 1,
      "hint": "Find the translation vector from $A$ to $A'$: $a = 4 - (-2)$ and $b = -1 - 3$. Then apply this exact same vector to vertex $C$.",
      "explanation": "Determine the translation rule from $A(-2, 3) \\to A'(4, -1)$: $a = 4 - (-2) = 6$ and $b = -1 - 3 = -4$. The rule is $(x, y) \\to (x + 6, y - 4)$. Because translations shift all vertices equally, apply this rule to $C(1, -4)$: $x' = 1 + 6 = 7$, and $y' = -4 - 4 = -8$. Therefore, $C' = (7, -8)$. Choice A applies the inverse rule ($1 - 6 = -5, -4 + 4 = 0$). Choice C adds 4 to $y$ instead of subtracting 4. Choice D subtracts 6 from $x$."
    },
    {
      "id": "p-1-2-mcq-19",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.2 Task 1D, students are asked: *\u201cWhat translation must be performed on the image so that it returns to the exact location of the preimage?\u201d* If a figure was translated by $(x, y) \\to (x - 7, y + 4)$, which rule will return the image back to its original preimage?",
      "options": [
        "$(x, y) \\to (x - 7, y + 4)$",
        "$(x, y) \\to (x + 7, y + 4)$",
        "$(x, y) \\to (x - 4, y + 7)$",
        "$(x, y) \\to (x + 7, y - 4)$"
      ],
      "correctAnswer": 3,
      "hint": "The inverse translation reverses both directions: the opposite of moving left 7 is moving right 7, and the opposite of moving up 4 is moving down 4.",
      "explanation": "To undo a translation and return an image to its starting position, apply the inverse translation by negating both displacements. The opposite of shifting 7 units left ($-7$) is shifting 7 units right ($+7$), and the opposite of shifting 4 units up ($+4$) is shifting 4 units down ($-4$). Thus, the returning rule is $(x, y) \\to (x + 7, y - 4)$. Choice A repeats the forward translation. Choice B fails to reverse the vertical shift. Choice C swaps the horizontal and vertical numbers."
    },
    {
      "id": "p-1-2-mcq-20",
      "module": 1,
      "lesson": "1.2",
      "topic": "Explore Translations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "A homeowner wants to slide a rectangular sofa from the center of a living room flush against a wall (HMH TE p. 39 DOK 3). The sofa has dimensions $84\\text{ inches long}$ by $36\\text{ inches deep}$. The available wall space between two doorways measures $90\\text{ inches wide}$. Why does the homeowner know with mathematical certainty that the sofa will fit against the wall after being pushed along a straight-line path without rotating?",
      "options": [
        "Because sliding a shape across a floor slightly compresses its length along the direction of motion.",
        "Because translations alter the angle measures of a quadrilateral to adapt to boundary constraints.",
        "Because translations preserve side lengths, angle measures, and parallelism, the sofa's dimensions remain exactly $84\\text{ in.} \\times 36\\text{ in.}$, which is less than the $90\\text{ in.}$ space.",
        "Because the translation vector's magnitude reduces the perimeter of any translated object by a factor of $\\sqrt{a^2 + b^2}$."
      ],
      "correctAnswer": 2,
      "hint": "Translations are rigid motions. What happens to the side lengths, perimeter, and rectangular angles of an object when it slides?",
      "explanation": "Translations are rigid motions (isometries) that preserve side lengths, angle measures, collinearity, perimeter, and area. Because the sofa does not rotate, stretch, compress, or deform during the translation, its length remains exactly 84 inches. Since $84\\text{ in.} < 90\\text{ in.}$, the sofa is guaranteed to fit flush against the wall. Choice A falsely assumes physical deformation occurs during a geometric translation. Choices B and D contradict the fundamental property that translations preserve all angles, side lengths, and perimeter."
    }
  ],
  "1.3": [
    {
      "id": "p-1-3-mcq-1",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "Point $A(-4, 7)$ is reflected across the $x$-axis. What are the coordinates of the image point $A'$?",
      "options": [
        "$(-4, -7)$",
        "$(4, 7)$",
        "$(4, -7)$",
        "$(7, -4)$"
      ],
      "correctAnswer": 0,
      "hint": "Reflecting across the $x$-axis preserves the horizontal position ($x$) and inverts the vertical position ($y$): $(x, y) \\to (x, -y)$.",
      "explanation": "Option A is correct. The coordinate rule for reflection across the $x$-axis is $(x, y) \\to (x, -y)$. The $x$-coordinate remains $-4$, while the $y$-coordinate is negated from $7$ to $-7$, giving $A'(-4, -7)$. Option B $(4, 7)$ negates the $x$-coordinate instead (reflection across the $y$-axis). Option C $(4, -7)$ negates both coordinates (equivalent to a $180^\\circ$ rotation about the origin). Option D $(7, -4)$ swaps the coordinates (reflection across the diagonal line $y = x$)."
    },
    {
      "id": "p-1-3-mcq-2",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle JKL$ with vertex $K(5, -8)$ is reflected across the $y$-axis to produce $\\triangle J'K'L'$. Which coordinate pair represents the location of $K'$?",
      "options": [
        "$(5, 8)$",
        "$(-5, -8)$",
        "$(-5, 8)$",
        "$(-8, 5)$"
      ],
      "correctAnswer": 1,
      "hint": "Reflecting across the $y$-axis keeps the vertical height ($y$) identical and reflects the horizontal position ($x$): $(x, y) \\to (-x, y)$.",
      "explanation": "Option B is correct. Under a reflection across the $y$-axis, the algebraic mapping rule is $(x, y) \\to (-x, y)$. The $x$-coordinate $5$ becomes $-5$, while the $y$-coordinate remains $-8$. Therefore, $K'(-5, -8)$. Option A $(5, 8)$ reflects across the $x$-axis by negating $y$. Option C $(-5, 8)$ negates both coordinates, which is a $180^\\circ$ rotation. Option D $(-8, 5)$ incorrectly interchanges the $x$- and $y$-coordinates."
    },
    {
      "id": "p-1-3-mcq-3",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A polygon vertex located at $P(-3, 8)$ is reflected across the diagonal line $y = x$. What are the coordinates of the reflected image $P'$?",
      "options": [
        "$(3, -8)$",
        "$(-8, 3)$",
        "$(8, -3)$",
        "$(-3, -8)$"
      ],
      "correctAnswer": 2,
      "hint": "On the line $y = x$, every point has equal coordinates. Reflecting across this line simply interchanges the roles of $x$ and $y$: $(x, y) \\to (y, x)$.",
      "explanation": "Option C is correct. The algebraic mapping rule for reflection across the line $y = x$ is $(x, y) \\to (y, x)$. The coordinates swap positions without altering their signs: the new $x$-value is the old $y$-value ($8$), and the new $y$-value is the old $x$-value ($-3$). Thus, $P' = (8, -3)$. Option A $(3, -8)$ negates both coordinates without swapping. Option B $(-8, 3)$ swaps and negates both coordinates, which is the rule for reflecting across $y = -x$. Option D $(-3, -8)$ reflects across the $x$-axis."
    },
    {
      "id": "p-1-3-mcq-4",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Line segment $\\overline{CD}$ has endpoint $D(4, -6)$. If $\\overline{CD}$ is reflected across the diagonal line $y = -x$, which coordinates identify $D'$?",
      "options": [
        "$(-6, 4)$",
        "$(-4, 6)$",
        "$(4, 6)$",
        "$(6, -4)$"
      ],
      "correctAnswer": 3,
      "hint": "Reflecting across the line $y = -x$ requires both swapping the coordinates and changing their signs: $(x, y) \\to (-y, -x)$.",
      "explanation": "Option D is correct. The coordinate rule for a reflection across the line $y = -x$ is $(x, y) \\to (-y, -x)$. Starting with $D(4, -6)$: the new $x$-coordinate is $-y = -(-6) = 6$, and the new $y$-coordinate is $-x = -(4) = -4$. Hence, $D' = (6, -4)$. Option A $(-6, 4)$ swapped coordinates without changing signs (reflection across $y = x$). Option B $(-4, 6)$ negated both coordinates without swapping (a $180^\\circ$ rotation). Option C $(4, 6)$ negated only the $y$-coordinate (reflection across the $x$-axis)."
    },
    {
      "id": "p-1-3-mcq-5",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Point $M(1, 5)$ is reflected across the vertical line $x = 4$. What are the coordinates of the reflected image $M'$?",
      "options": [
        "$(7, 5)$",
        "$(-2, 5)$",
        "$(4, 5)$",
        "$(7, -5)$"
      ],
      "correctAnswer": 0,
      "hint": "The line $x = 4$ is vertical, so the $y$-coordinate does not change. Find how far $1$ is from $4$, and move that same distance to the other side of $4$.",
      "explanation": "Option A is correct. In a reflection across a vertical line $x = c$, the $y$-coordinate remains invariant ($y' = 5$). The horizontal distance from $M(1, 5)$ to $x = 4$ is $4 - 1 = 3$ units to the left. The reflected image $M'$ must be $3$ units to the right of $x = 4$: $x' = 4 + 3 = 7$. Alternatively, using the algebraic formula: $x' = 2c - x = 2(4) - 1 = 7$. Thus, $M' = (7, 5)$. Option B $(-2, 5)$ incorrectly subtracted $3$ from $1$ instead of adding to $4$. Option C $(4, 5)$ is the midpoint on the line of reflection itself. Option D $(7, -5)$ incorrectly negated the $y$-coordinate."
    },
    {
      "id": "p-1-3-mcq-6",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Vertex $V(-3, -2)$ is reflected across the horizontal line $y = 3$. What are the coordinates of the reflected image $V'$?",
      "options": [
        "$(-3, 5)$",
        "$(-3, 1)$",
        "$(3, -2)$",
        "$(-3, 8)$"
      ],
      "correctAnswer": 3,
      "hint": "A reflection across a horizontal line keeps the $x$-coordinate constant. Calculate the vertical distance from $-2$ to $3$, then add that distance above $y = 3$.",
      "explanation": "Option D is correct. Across the horizontal line $y = c$, the $x$-coordinate is unaffected ($x' = -3$). The vertical distance from $V(-3, -2)$ to the mirror line $y = 3$ is $3 - (-2) = 5$ units. The image $V'$ must lie $5$ units above the mirror line: $y' = 3 + 5 = 8$. Using the formula: $y' = 2c - y = 2(3) - (-2) = 6 + 2 = 8$. Thus, $V' = (-3, 8)$. Option A $(-3, 5)$ merely added the distance $5$ to $0$ or forgot to double the offset. Option B $(-3, 1)$ added $3$ to $-2$ instead of reflecting across $y = 3$. Option C $(3, -2)$ reflected horizontally across the $y$-axis."
    },
    {
      "id": "p-1-3-mcq-7",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Point $P(2, 6)$ is reflected across line $\\ell$ to produce $P'(8, 6)$. Which mathematical statement accurately describes line $\\ell$ and its geometric relationship to segment $\\overline{PP'}$?",
      "options": [
        "Line $\\ell$ has equation $y = 6$ and is parallel to segment $\\overline{PP'}$.",
        "Line $\\ell$ has equation $x = 5$ and is the perpendicular bisector of segment $\\overline{PP'}$.",
        "Line $\\ell$ has equation $x = 6$ and intersects $\\overline{PP'}$ at a $45^\\circ$ angle.",
        "Line $\\ell$ has equation $y = 5$ and bisects $\\overline{PP'}$ obliquely."
      ],
      "correctAnswer": 1,
      "hint": "Recall the fundamental geometric definition: The line of reflection is always the perpendicular bisector of every segment connecting a preimage point to its image point.",
      "explanation": "Option B is correct. Segment $\\overline{PP'}$ connects $(2, 6)$ and $(8, 6)$, which is a horizontal segment on the line $y = 6$ of length $|8 - 2| = 6$ units. The midpoint of $\\overline{PP'}$ is $\\left(\\frac{2+8}{2}, \\frac{6+6}{2}\\right) = (5, 6)$. The line of reflection must pass through this midpoint and be perpendicular to the horizontal segment. A line perpendicular to a horizontal line is vertical, giving the equation $x = 5$. Option A ($y = 6$) is the line containing the segment itself, not its perpendicular bisector. Option C ($x = 6$) does not pass through the midpoint. Option D ($y = 5$) is horizontal and cannot be perpendicular to another horizontal segment."
    },
    {
      "id": "p-1-3-mcq-8",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle ABC$ has vertices listed in clockwise order: $A(1, 2)$, $B(4, 2)$, and $C(1, 6)$. After reflecting $\\triangle ABC$ across the $y$-axis to form $\\triangle A'B'C'$, which statement regarding the congruence and vertex orientation of $\\triangle A'B'C'$ is true?",
      "options": [
        "$\\triangle A'B'C' \\cong \\triangle ABC$, and its vertices $A' \\to B' \\to C'$ remain in clockwise order.",
        "$\\triangle A'B'C'$ is not congruent to $\\triangle ABC$ because reflections distort vertex order.",
        "$\\triangle A'B'C' \\cong \\triangle ABC$, but its vertices $A' \\to B' \\to C'$ are now ordered counterclockwise (orientation is reversed).",
        "The vertex orientation is unchanged because all rigid motions preserve clockwise order."
      ],
      "correctAnswer": 2,
      "hint": "Reflections are rigid motions (isometries) that preserve side lengths and angles, but they flip the plane like looking into a mirror, reversing chirality.",
      "explanation": "Option C is correct. Because reflection is a rigid motion (isometry), side lengths and angle measures are strictly preserved, guaranteeing that $\\triangle A'B'C' \\cong \\triangle ABC$. However, reflections are opposite isometries (chirality-reversing): tracing $A(1,2) \\to B(4,2) \\to C(1,6)$ runs clockwise, but tracing their reflections $A'(-1,2) \\to B'(-4,2) \\to C'(-1,6)$ runs counterclockwise. Option A falsely asserts that orientation is preserved (translations and rotations preserve orientation, but reflections do not). Option B is false because orientation reversal does not alter congruence. Option D is incorrect because rigid motions include opposite isometries."
    },
    {
      "id": "p-1-3-mcq-9",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "A quadrilateral has vertices $Q(0, 4)$, $R(3, 0)$, $S(-2, 5)$, and $T(0, -6)$. If the quadrilateral is reflected across the $y$-axis, which vertex or vertices remain strictly fixed at their original coordinates ($P = P'$)?",
      "options": [
        "Only $R(3, 0)$",
        "Only $S(-2, 5)$",
        "None of the vertices, because transformations always move every point",
        "Both $Q(0, 4)$ and $T(0, -6)$"
      ],
      "correctAnswer": 3,
      "hint": "Which points lie directly ON the line of reflection? Points on the line of reflection never move ($P = P'$).",
      "explanation": "Option D is correct. The line of reflection is the $y$-axis, whose equation is $x = 0$. Any point lying directly on the line of reflection is an invariant (fixed) point: $(0, y) \\to (-0, y) = (0, y)$. Both $Q(0, 4)$ and $T(0, -6)$ have an $x$-coordinate of $0$, so $Q' = Q(0, 4)$ and $T' = T(0, -6)$. Option A $R(3, 0)$ lies on the $x$-axis, not the $y$-axis; its image is $R'(-3, 0) \\neq R$. Option B $S(-2, 5)$ has $x = -2$, so its image is $S'(2, 5)$. Option C is a common misconception; points on the reflection axis are always fixed."
    },
    {
      "id": "p-1-3-mcq-10",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A geometric figure is reflected across the line $y = x$. Which of the following points will map directly onto itself ($P = P'$)?",
      "options": [
        "$(4, -4)$",
        "$(-7, -7)$",
        "$(0, 5)$",
        "$(3, -3)$"
      ],
      "correctAnswer": 1,
      "hint": "A point remains fixed under reflection if and only if it lies directly on the mirror line. Test which point satisfies $y = x$.",
      "explanation": "Option B is correct. A point $(x, y)$ is invariant under reflection across $y = x$ if and only if it satisfies the equation of the line, meaning $x = y$. For point $(-7, -7)$, both coordinates are equal to $-7$. Applying the reflection rule $(x, y) \\to (y, x)$ gives $(-7, -7) \\to (-7, -7)$, so $P = P'$. Options A $(4, -4)$ and D $(3, -3)$ lie on the line $y = -x$, so reflecting across $y = x$ swaps them to $(-4, 4)$ and $(-3, 3)$. Option C $(0, 5)$ maps to $(5, 0) \\neq (0, 5)$."
    },
    {
      "id": "p-1-3-mcq-11",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Segment $\\overline{AB}$ connects $A(1, 2)$ and $B(4, 8)$, giving it a slope of $m = \\frac{8 - 2}{4 - 1} = 2$. If $\\overline{AB}$ is reflected across the $x$-axis to produce segment $\\overline{A'B'}$, what is the slope of $\\overline{A'B'}$?",
      "options": [
        "$2$",
        "$\\frac{1}{2}$",
        "$-2$",
        "$-\\frac{1}{2}$"
      ],
      "correctAnswer": 2,
      "hint": "Calculate the image coordinates $A'$ and $B'$ using $(x, y) \\to (x, -y)$, then compute the slope $m' = \\frac{y'_2 - y'_1}{x'_2 - x'_1}$.",
      "explanation": "Option C is correct. Reflecting across the $x$-axis maps $A(1, 2) \\to A'(1, -2)$ and $B(4, 8) \\to B'(4, -8)$. The slope of $\\overline{A'B'}$ is $m' = \\frac{-8 - (-2)}{4 - 1} = \\frac{-6}{3} = -2$. In general, reflecting across any horizontal or vertical line negates the slope of a line segment: $m' = -m = -(2) = -2$. Option A ($2$) incorrectly assumes slope is invariant under reflection (slope is preserved under translations, not axis reflections). Option B ($\\frac{1}{2}$) took the reciprocal. Option D ($-\\frac{1}{2}$) took the negative reciprocal (perpendicular slope)."
    },
    {
      "id": "p-1-3-mcq-12",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Line segment $\\overline{GH}$ has a slope of $-\\frac{3}{5}$. If $\\overline{GH}$ is reflected across the $y$-axis, what will be the slope of the reflected image $\\overline{G'H'}$?",
      "options": [
        "$\\frac{3}{5}$",
        "$-\\frac{3}{5}$",
        "$\\frac{5}{3}$",
        "$-\\frac{5}{3}$"
      ],
      "correctAnswer": 0,
      "hint": "Reflecting across the $y$-axis negates the run ($\\Delta x$), which changes the sign of the slope: $m' = \\frac{\\Delta y}{-\\Delta x} = -m$.",
      "explanation": "Option A is correct. Under a reflection across the $y$-axis, the transformation is $(x, y) \\to (-x, y)$. For any two points with horizontal change $\\Delta x = x_2 - x_1$ and vertical change $\\Delta y = y_2 - y_1$, the reflected points have horizontal change $-\\Delta x$ and vertical change $\\Delta y$. Thus, the new slope is $m' = \\frac{\\Delta y}{-\\Delta x} = -m$. Given $m = -\\frac{3}{5}$, the reflected slope is $m' = -\\left(-\\frac{3}{5}\\right) = \\frac{3}{5}$. Option B ($-\\frac{3}{5}$) fails to negate the slope. Options C and D invert the ratio of vertical to horizontal change."
    },
    {
      "id": "p-1-3-mcq-13",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "A figure is reflected across the vertical line $x = 2$, and its image is immediately reflected across the parallel vertical line $x = 7$. What single transformation is equivalent to this composition of two reflections?",
      "options": [
        "A translation $5\\text{ units}$ to the right",
        "A translation $10\\text{ units}$ to the right",
        "A rotation of $180^\\circ$ about the point $(4.5, 0)$",
        "A translation $10\\text{ units}$ to the left"
      ],
      "correctAnswer": 1,
      "hint": "According to the Double Reflection Theorem, reflecting across two parallel lines separated by distance $d$ produces a translation of $2d$ in the direction from the first line to the second.",
      "explanation": "Option B is correct. By the Double Reflection Theorem across parallel lines, the composition of reflections across two parallel lines separated by distance $d$ is equivalent to a translation by $2d$ perpendicular to the lines. The lines $x = 2$ and $x = 7$ are parallel vertical lines separated by $d = 7 - 2 = 5$ units directed to the right. The composite motion is therefore a translation to the right by $2d = 2(5) = 10$ units: $(x, y) \\to (x + 10, y)$. For verification, test $x = 0$: reflect across $x = 2 \\implies 2(2) - 0 = 4$; reflect $4$ across $x = 7 \\implies 2(7) - 4 = 10$. Net change: $+10$. Option A forgets to multiply the distance by $2$. Option C confuses parallel reflection lines with intersecting reflection lines. Option D translates in the opposite direction."
    },
    {
      "id": "p-1-3-mcq-14",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "Figure $F$ is reflected across the horizontal line $y = -1$, and the resulting image is then reflected across the horizontal line $y = -5$. Which algebraic mapping rule describes this composite transformation?",
      "options": [
        "$(x, y) \\to (x, y - 8)$",
        "$(x, y) \\to (x, y + 8)$",
        "$(x, y) \\to (x, y - 4)$",
        "$(x, y) \\to (-x, -y - 6)$"
      ],
      "correctAnswer": 0,
      "hint": "The lines are horizontal and parallel. The motion goes from $y = -1$ down to $y = -5$ (a downward shift). What is $2 \\times$ the distance between them?",
      "explanation": "Option A is correct. Let us algebraically compose the two reflections: 1. First reflection across $y = -1$: $y_1 = 2(-1) - y = -2 - y$. 2. Second reflection across $y = -5$: $y_2 = 2(-5) - y_1 = -10 - (-2 - y) = -10 + 2 + y = y - 8$. The $x$-coordinate is unaffected because both lines are horizontal. Thus, the composition is the pure translation $(x, y) \\to (x, y - 8)$. This matches the theorem: the directed distance from $y = -1$ to $y = -5$ is $-4$, and doubling it gives a shift of $2(-4) = -8$. Option B $(x, y) \\to (x, y + 8)$ shifts upward instead of downward. Option C $(x, y) \\to (x, y - 4)$ forgot to double the distance. Option D confuses the translation with a point reflection."
    },
    {
      "id": "p-1-3-mcq-15",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle RST$ is reflected across the $x$-axis, and its image is then reflected across the $y$-axis. Which single transformation achieves the exact same image from the original $\\triangle RST$?",
      "options": [
        "A translation $2\\text{ units}$ along the vector $\\langle -1, -1 \\rangle$",
        "A reflection across the diagonal line $y = -x$",
        "A rotation of $180^\\circ$ about the origin $(0, 0)$",
        "A reflection across the diagonal line $y = x$"
      ],
      "correctAnswer": 2,
      "hint": "Trace what happens to coordinates: first $(x, y) \\to (x, -y)$, then apply the second reflection. Which single transformation rule is $(-x, -y)$?",
      "explanation": "Option C is correct. Track an arbitrary point $(x, y)$ under the two transformations: First, reflection across the $x$-axis maps $(x, y) \\to (x, -y)$. Next, reflection across the $y$-axis maps $(x, -y) \\to (-x, -y)$. The algebraic rule $(x, y) \\to (-x, -y)$ is precisely the rule for a $180^\\circ$ rotation (clockwise or counterclockwise) about the origin $(0, 0)$. Geometrically, when two reflection lines intersect at an angle $\\theta = 90^\\circ$, their composition is a rotation about their intersection point by $2\\theta = 2(90^\\circ) = 180^\\circ$. Option A is a translation. Option B is a reflection across $y = -x$, which has rule $(x, y) \\to (-y, -x)$. Option D is a reflection across $y = x$, which has rule $(x, y) \\to (y, x)$."
    },
    {
      "id": "p-1-3-mcq-16",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "A polygon has clockwise vertex ordering. It is reflected across the vertical line $x = 3$, and that image is subsequently reflected across the perpendicular horizontal line $y = -2$. What is the vertex orientation of the final image, and what geometric motion describes this combined transformation?",
      "options": [
        "Counterclockwise; the transformation is equivalent to a single reflection across $y = -x + 1$.",
        "Counterclockwise; each reflection preserves orientation so the net result is unchanged.",
        "Clockwise; reflecting twice across perpendicular lines preserves orientation and is equivalent to a $180^\\circ$ rotation about $(3, -2)$.",
        "Undefined; intersecting reflections destroy polygon vertex ordering."
      ],
      "correctAnswer": 2,
      "hint": "A single reflection reverses orientation (clockwise $\\to$ counterclockwise). What does a second reflection do? Remember: two perpendicular reflections form a $180^\\circ$ rotation.",
      "explanation": "Option C is correct. A single reflection is an opposite isometry, reversing orientation from clockwise to counterclockwise. A second reflection reverses orientation once again: counterclockwise $\\to$ clockwise. Because the two lines $x = 3$ and $y = -2$ are perpendicular (intersecting at $(3, -2)$ at $90^\\circ$), their composition is a $180^\\circ$ rotation about $(3, -2)$. Rotations are direct isometries that preserve clockwise orientation. Option A claims the composition of two reflections is a single reflection (two reflections can never equal an odd number of reflections). Option B falsely claims that individual reflections preserve orientation. Option D is mathematically meaningless because rigid motions always preserve geometric structure."
    },
    {
      "id": "p-1-3-mcq-17",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Preimage point $W(-5, 3)$ is mapped to image point $W'(7, 3)$ by a single reflection. What is the equation of the line of reflection?",
      "options": [
        "$x = 1$",
        "$y = 3$",
        "$x = 2$",
        "$y = 1$"
      ],
      "correctAnswer": 0,
      "hint": "The points share the same $y$-coordinate ($3$), so $\\overline{WW'}$ is horizontal. The line of reflection must be vertical ($x = c$) and pass through the midpoint of $\\overline{WW'}$.",
      "explanation": "Option A is correct. Points $W(-5, 3)$ and $W'(7, 3)$ have identical $y$-coordinates, meaning segment $\\overline{WW'}$ is horizontal. The line of reflection is the perpendicular bisector of $\\overline{WW'}$. A line perpendicular to a horizontal line is a vertical line of the form $x = c$. The line must pass through the midpoint $x$-coordinate: $c = \\frac{-5 + 7}{2} = \\frac{2}{2} = 1$. Therefore, the line of reflection is $x = 1$. Option B ($y = 3$) is the horizontal line on which the points lie, not the perpendicular bisector. Option C ($x = 2$) results from an arithmetic error in calculating the average. Option D ($y = 1$) is a horizontal line."
    },
    {
      "id": "p-1-3-mcq-18",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "During a geometry lab, a student discovers that preimage vertex $E(2, -5)$ maps to image vertex $E'(-5, 2)$ after a single reflection. Across which line was the point reflected?",
      "options": [
        "The $x$-axis ($y = 0$)",
        "The line $y = -x$",
        "The $y$-axis ($x = 0$)",
        "The line $y = x$"
      ],
      "correctAnswer": 3,
      "hint": "Compare the coordinates: $x = 2$ became $y' = 2$, and $y = -5$ became $x' = -5$. The coordinates swapped places without sign changes: $(x, y) \\to (y, x)$.",
      "explanation": "Option D is correct. Comparing preimage $E(2, -5)$ and image $E'(-5, 2)$, the $x$- and $y$-coordinates have swapped values: $(x, y) \\to (y, x)$. This is the defining coordinate rule for reflection across the diagonal line $y = x$. We can also verify using the perpendicular bisector property: The midpoint is $\\left(\\frac{2 + (-5)}{2}, \\frac{-5 + 2}{2}\\right) = (-1.5, -1.5)$, which lies directly on $y = x$. The slope of $\\overline{EE'}$ is $\\frac{2 - (-5)}{-5 - 2} = \\frac{7}{-7} = -1$, which is perpendicular to the slope of $y = x$ ($+1$). Option A reflects $(2, -5)$ to $(2, 5)$. Option B ($y = -x$) reflects $(2, -5)$ to $(5, -2)$ by swapping and negating. Option C reflects $(2, -5)$ to $(-2, -5)$."
    },
    {
      "id": "p-1-3-mcq-19",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "A regular octagon is centered at the origin on the coordinate plane. How many distinct lines of reflectional symmetry does this regular octagon possess?",
      "options": [
        "$4$",
        "$8$",
        "$16$",
        "Infinitely many"
      ],
      "correctAnswer": 1,
      "hint": "In any regular polygon with $n$ sides, how many lines of symmetry connect opposite vertices or midpoints of opposite sides?",
      "explanation": "Option B is correct. Any regular polygon with $n$ sides has exactly $n$ lines of reflectional symmetry. For a regular octagon ($n = 8$): \u2022 $4$ lines of symmetry pass through pairs of opposite vertices.\n\u2022 $4$ lines of symmetry pass through the midpoints of opposite sides.\nThis gives a total of $4 + 4 = 8$ distinct lines of reflectional symmetry. Option A ($4$) counts only the vertex lines or only the side-bisector lines. Option C ($16$) double-counts the axes or confuses lines of symmetry with total symmetries (dihedral group order $D_8$). Option D applies only to a circle."
    },
    {
      "id": "p-1-3-mcq-20",
      "module": 1,
      "lesson": "1.3",
      "topic": "Explore Reflections",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "An isosceles trapezoid is positioned in the coordinate plane with vertices $A(-4, 1)$, $B(4, 1)$, $C(2, 5)$, and $D(-2, 5)$. Which equation represents the line of reflectional symmetry that maps this trapezoid onto itself?",
      "options": [
        "$y = 0$ (the $x$-axis)",
        "$y = 3$",
        "$y = x$",
        "$x = 0$ (the $y$-axis)"
      ],
      "correctAnswer": 3,
      "hint": "A line of symmetry must reflect every vertex of the trapezoid onto another vertex of the same trapezoid. Test which axis reflects $A(-4, 1)$ to $B(4, 1)$ and $D(-2, 5)$ to $C(2, 5)$.",
      "explanation": "Option D is correct. Reflecting across the line $x = 0$ (the $y$-axis) applies the rule $(x, y) \\to (-x, y)$: \u2022 $A(-4, 1) \\to (4, 1) = B$\n\u2022 $B(4, 1) \\to (-4, 1) = A$\n\u2022 $C(2, 5) \\to (-2, 5) = D$\n\u2022 $D(-2, 5) \\to (2, 5) = C$\nEvery vertex maps directly onto a corresponding vertex of the figure, meaning the $y$-axis ($x = 0$) is the line of symmetry. Option A ($y = 0$) flips the trapezoid below the $x$-axis ($y < 0$), completely outside its original region. Option B ($y = 3$) is a horizontal midline; reflecting over it would swap base $AB$ (length $8$) with base $CD$ (length $4$), distorting the figure. Option C ($y = x$) tilts the figure obliquely."
    }
  ],
  "1.4": [
    {
      "id": "p-1-4-mcq-1",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "In transformational geometry, a rotation by an angle $\\theta > 0^\\circ$ is defined by a center of rotation, an angle of rotation, and a direction. According to standard mathematical convention, which direction corresponds to a positive angle of rotation (such as $+90^\\circ$) on the coordinate plane?",
      "options": [
        "Clockwise",
        "Counterclockwise",
        "In the positive $x$-direction (to the right)",
        "In the positive $y$-direction (upward)"
      ],
      "correctAnswer": 1,
      "hint": "Think about how angles are measured in standard position on the coordinate plane starting from the positive $x$-axis.",
      "explanation": "In standard mathematics and geometry, a positive angle of rotation turns in the counterclockwise direction (for example, $+90^\\circ$ indicates a $90^\\circ$ counterclockwise turn). A clockwise rotation corresponds to a negative angle. Choices C and D describe translations (linear shifts along axes), not rotational directions."
    },
    {
      "id": "p-1-4-mcq-2",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "Triangle $ABC$ is rotated $90^\\circ$ counterclockwise about the origin $(0, 0)$. What happens to the coordinates of the origin itself during this transformation?",
      "options": [
        "The origin shifts to $(0, 1)$ because of the $90^\\circ$ counterclockwise turn.",
        "The origin is undefined after a rotation because a pivot cannot move.",
        "The origin remains at $(0, 0)$ because the center of rotation is a fixed point that maps onto itself.",
        "The origin moves to $(-1, 0)$ following the rule $(x, y) \\to (-y, x)$."
      ],
      "correctAnswer": 2,
      "hint": "Consider what happens to the point where the tip of your pencil rests when turning tracing paper (Into Math TE p. 62-63).",
      "explanation": "The center of rotation is a fixed point (invariant point) under any rotation. Under the coordinate mapping rule $(x, y) \\to (-y, x)$, substituting $(0, 0)$ yields $(-0, 0) = (0, 0)$. Choices A and D incorrectly assign non-zero coordinates to the center of rotation, while Choice B incorrectly claims the point is undefined."
    },
    {
      "id": "p-1-4-mcq-3",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Point $A(3, 7)$ is rotated $90^\\circ$ counterclockwise about the origin. What are the coordinates of the image point $A'$?",
      "options": [
        "$A'(7, -3)$",
        "$A'(-7, 3)$",
        "$A'(-3, -7)$",
        "$A'(-7, -3)$"
      ],
      "correctAnswer": 1,
      "hint": "Apply the algebraic mapping rule for a $90^\\circ$ counterclockwise rotation: $(x, y) \\to (-y, x)$.",
      "explanation": "For a $90^\\circ$ counterclockwise rotation about the origin, the mapping rule is $(x, y) \\to (-y, x)$. Given $A(3, 7)$, we have $x = 3$ and $y = 7$. Substituting these values gives $A'(-7, 3)$. Choice A $(7, -3)$ is the result of a $90^\\circ$ clockwise rotation $(y, -x)$. Choice C $(-3, -7)$ is a $180^\\circ$ rotation $(-x, -y)$. Choice D $(-7, -3)$ incorrectly negates both coordinates after swapping."
    },
    {
      "id": "p-1-4-mcq-4",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Point $B(-4, -6)$ in Quadrant III is rotated $90^\\circ$ counterclockwise about the origin. What are the coordinates of the image point $B'$?",
      "options": [
        "$B'(-6, 4)$",
        "$B'(4, -6)$",
        "$B'(-6, -4)$",
        "$B'(6, -4)$"
      ],
      "correctAnswer": 3,
      "hint": "Be careful with signs: $-y$ means the opposite of $y$. If $y = -6$, what is $-y$?",
      "explanation": "The algebraic rule for a $90^\\circ$ counterclockwise rotation about the origin is $(x, y) \\to (-y, x)$. For $B(-4, -6)$, the new $x$-coordinate is $-y = -(-6) = 6$, and the new $y$-coordinate is $x = -4$. Thus $B'(6, -4)$ lies in Quadrant IV. Choice A $(-6, 4)$ forgets that $-(-6) = +6$. Choice B $(4, -6)$ negates $x$ and leaves $y$ unchanged (a reflection across the $y$-axis). Choice C $(-6, -4)$ swaps coordinates without applying the required negation."
    },
    {
      "id": "p-1-4-mcq-5",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.4, a figure with vertex $J(-3, 4)$ is rotated $180^\\circ$ about the origin. What are the coordinates of the image vertex $J'$?",
      "options": [
        "$J'(3, -4)$",
        "$J'(-4, -3)$",
        "$J'(4, 3)$",
        "$J'(-3, -4)$"
      ],
      "correctAnswer": 0,
      "hint": "A $180^\\circ$ rotation takes every point $(x, y)$ to $(-x, -y)$, whether turned clockwise or counterclockwise.",
      "explanation": "The rule for a $180^\\circ$ rotation about the origin is $(x, y) \\to (-x, -y)$. Applying this to $J(-3, 4)$ gives $x' = -(-3) = 3$ and $y' = -(4) = -4$, resulting in $J'(3, -4)$. Note that turning $180^\\circ$ clockwise or $180^\\circ$ counterclockwise yields the identical image. Choice B $(-4, -3)$ mistakenly swaps the coordinates. Choice C $(4, 3)$ applies a $90^\\circ$ clockwise rule with sign errors. Choice D $(-3, -4)$ only negates the $y$-coordinate."
    },
    {
      "id": "p-1-4-mcq-6",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In the textbook activity (TE p. 64), the letter 'N' has vertex $A(2, 1)$ and is rotated $90^\\circ$ clockwise about the origin to create the letter 'Z'. What are the coordinates of image vertex $A'$?",
      "options": [
        "$A'(-1, 2)$",
        "$A'(1, -2)$",
        "$A'(-2, 1)$",
        "$A'(-2, -1)$"
      ],
      "correctAnswer": 1,
      "hint": "A $90^\\circ$ clockwise rotation follows the algebraic rule $(x, y) \\to (y, -x)$.",
      "explanation": "Rotating $90^\\circ$ clockwise about the origin follows the mapping rule $(x, y) \\to (y, -x)$. With preimage $A(2, 1)$, we swap coordinates and negate the new second component: $x' = y = 1$ and $y' = -x = -2$. Therefore, $A'(1, -2)$. Choice A $(-1, 2)$ is the result of a $90^\\circ$ counterclockwise rotation $(-y, x)$. Choice C $(-2, 1)$ is a reflection across the $y$-axis. Choice D $(-2, -1)$ is a $180^\\circ$ rotation."
    },
    {
      "id": "p-1-4-mcq-7",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Which algebraic mapping rule represents both a $270^\\circ$ counterclockwise rotation and a $90^\\circ$ clockwise rotation about the origin?",
      "options": [
        "$(x, y) \\to (-y, x)$",
        "$(x, y) \\to (-x, -y)$",
        "$(x, y) \\to (y, -x)$",
        "$(x, y) \\to (-y, -x)$"
      ],
      "correctAnswer": 2,
      "hint": "A full circle is $360^\\circ$. Turning $90^\\circ$ clockwise brings a figure to the same position as turning $360^\\circ - 90^\\circ = 270^\\circ$ counterclockwise.",
      "explanation": "Because a full rotation is $360^\\circ$, moving $90^\\circ$ clockwise places a figure in the exact same position as moving $360^\\circ - 90^\\circ = 270^\\circ$ counterclockwise. Both rotations share the coordinate rule $(x, y) \\to (y, -x)$. Choice A $(-y, x)$ represents a $90^\\circ$ counterclockwise (or $270^\\circ$ clockwise) rotation. Choice B $(-x, -y)$ represents a $180^\\circ$ rotation. Choice D $(-y, -x)$ is a reflection across the line $y = -x$."
    },
    {
      "id": "p-1-4-mcq-8",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Point $P(5, -2)$ undergoes a $270^\\circ$ clockwise rotation about the origin. What are the coordinates of image point $P'$?",
      "options": [
        "$P'(2, 5)$",
        "$P'(-2, -5)$",
        "$P'(-5, 2)$",
        "$P'(5, 2)$"
      ],
      "correctAnswer": 0,
      "hint": "Convert the $270^\\circ$ clockwise rotation to its equivalent counterclockwise turn: $360^\\circ - 270^\\circ = 90^\\circ$ counterclockwise.",
      "explanation": "Rotating $270^\\circ$ clockwise is equivalent to rotating $360^\\circ - 270^\\circ = 90^\\circ$ counterclockwise about the origin. The rule for $90^\\circ$ counterclockwise is $(x, y) \\to (-y, x)$. For $P(5, -2)$, $x' = -(-2) = 2$ and $y' = x = 5$, giving $P'(2, 5)$. Choice B $(-2, -5)$ uses the $90^\\circ$ clockwise rule $(y, -x)$. Choice C $(-5, 2)$ is a $180^\\circ$ rotation $(-x, -y)$. Choice D $(5, 2)$ reflects across the $x$-axis."
    },
    {
      "id": "p-1-4-mcq-9",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "A quadrilateral in the coordinate plane is rotated $360^\\circ$ about the origin. Which statement correctly describes the relationship between the preimage and its image?",
      "options": [
        "The image is inverted into the opposite quadrant according to $(x, y) \\to (-x, -y)$.",
        "The coordinates swap axes according to $(x, y) \\to (y, x)$.",
        "The image is identical to the preimage and occupies the exact same position because a $360^\\circ$ rotation is a full turn: $(x, y) \\to (x, y)$.",
        "The coordinates are multiplied by 2 because $360^\\circ$ is twice $180^\\circ$."
      ],
      "correctAnswer": 2,
      "hint": "How many degrees are in one complete circle or full turn?",
      "explanation": "A $360^\\circ$ rotation represents one complete revolution around the center of rotation. Every point completes a full circular path and returns to its initial location, described by the identity rule $(x, y) \\to (x, y)$. Choice A describes a $180^\\circ$ rotation. Choice B is a reflection across the line $y = x$. Choice D confuses rotation with a dilation of scale factor 2."
    },
    {
      "id": "p-1-4-mcq-10",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $ABC$ has vertices named in clockwise order: $A(1, 2)$, $B(4, 2)$, and $C(1, 6)$. Which transformation will result in an image triangle whose corresponding vertices $A' \\to B' \\to C'$ remain in clockwise order?",
      "options": [
        "A reflection across the $x$-axis",
        "A reflection across the $y$-axis",
        "A reflection across the line $y = x$",
        "A rotation of $90^\\circ$ counterclockwise about the origin"
      ],
      "correctAnswer": 3,
      "hint": "Which rigid motions preserve orientation (clockwise remains clockwise), and which rigid motion reverses orientation?",
      "explanation": "Rotations and translations preserve vertex orientation: if the vertices of the preimage read in clockwise order, the vertices of the image also read in clockwise order. In contrast, reflections reverse orientation (turning clockwise order into counterclockwise order). Therefore, only the rotation in Choice D preserves the clockwise order. Choices A, B, and C are all reflections, each of which reverses vertex orientation."
    },
    {
      "id": "p-1-4-mcq-11",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.4 (p. 67 Problem 8), $\\triangle JKL$ has an area of $3.25\\text{ square units}$ and a perimeter of $8.5\\text{ units}$. What happens to its area and perimeter when it is rotated $180^\\circ$ about vertex $J$?",
      "options": [
        "Both area and perimeter remain unchanged: $\\text{Area} = 3.25\\text{ square units}$ and $\\text{Perimeter} = 8.5\\text{ units}$.",
        "The perimeter doubles to $17.0\\text{ units}$, but the area remains $3.25\\text{ square units}$.",
        "The area becomes negative ($-3.25\\text{ square units}$) because the figure is inverted.",
        "The area becomes $0$ because the center of rotation is located at vertex $J$."
      ],
      "correctAnswer": 0,
      "hint": "Remember that a rotation is a rigid motion (isometry). What properties are preserved by all rigid motions?",
      "explanation": "Rotations are rigid motions (isometries), which preserve all distances (segment lengths) and angle measures regardless of the chosen center of rotation. Because all side lengths are preserved, the perimeter remains $8.5\\text{ units}$. Because side lengths and angle measures are preserved, the area remains strictly $3.25\\text{ square units}$. Area cannot be negative (Choice C), does not collapse to zero (Choice D), and perimeter does not change (Choice B)."
    },
    {
      "id": "p-1-4-mcq-12",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "Line segment $AB$ has endpoints $A(1, 2)$ and $B(3, 8)$, giving it a slope of $m = \\frac{8 - 2}{3 - 1} = 3$. If segment $AB$ is rotated $90^\\circ$ counterclockwise about the origin to form segment $A'B'$, what is the slope $m'$ of the image segment?",
      "options": [
        "$m' = 3$",
        "$m' = -3$",
        "$m' = -\\frac{1}{3}$",
        "$m' = \\frac{1}{3}$"
      ],
      "correctAnswer": 2,
      "hint": "A $90^\\circ$ rotation turns a line so that it is perpendicular to the original line. What is the relationship between the slopes of two perpendicular lines?",
      "explanation": "Rotating a line segment by $90^\\circ$ turns the segment perpendicular to its original orientation. Two non-vertical perpendicular lines have slopes that are negative reciprocals ($m' = -\\frac{1}{m}$). Since the original slope is $m = 3$, the new slope is $m' = -\\frac{1}{3}$. We can verify with coordinates: $A'(-2, 1)$ and $B'(-8, 3)$ using $(x, y) \\to (-y, x)$. Slope $m' = \\frac{3 - 1}{-8 - (-2)} = \\frac{2}{-6} = -\\frac{1}{3}$. Choice A assumes slope is invariant (true for $180^\\circ$ or translations, not $90^\\circ$). Choice B only negates the slope without taking the reciprocal. Choice D takes the reciprocal without negating."
    },
    {
      "id": "p-1-4-mcq-13",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Line segment $CD$ has a slope of $m = -\\frac{4}{7}$. After undergoing a $180^\\circ$ rotation about the origin, what is the slope of the resulting image segment $C'D'$?",
      "options": [
        "$m' = \\frac{7}{4}$",
        "$m' = -\\frac{4}{7}$",
        "$m' = \\frac{4}{7}$",
        "$m' = -\\frac{7}{4}$"
      ],
      "correctAnswer": 1,
      "hint": "A $180^\\circ$ rotation turns a segment in the opposite direction along a parallel line. What is true about the slopes of parallel lines?",
      "explanation": "Under a $180^\\circ$ rotation about the origin, every point $(x, y)$ maps to $(-x, -y)$. The slope formula between image points is $m' = \\frac{-y_2 - (-y_1)}{-x_2 - (-x_1)} = \\frac{-(y_2 - y_1)}{-(x_2 - x_1)} = \\frac{y_2 - y_1}{x_2 - x_1} = m$. A $180^\\circ$ rotation preserves the slope ($m' = m$) because the image line is parallel to (or lies on the same line as) the preimage line. Thus, the slope remains $-\\frac{4}{7}$. Choice A is the perpendicular negative reciprocal (for $90^\\circ$). Choice C erroneously flips the sign. Choice D is the reciprocal without preserving the sign."
    },
    {
      "id": "p-1-4-mcq-14",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In Lesson 1.4 Spark Your Learning (TE p. 61-62), students investigate rotational symmetry. What is the minimum positive angle of rotation about its center that will map a regular hexagon ($6$ equal sides) onto itself?",
      "options": [
        "$90^\\circ$",
        "$120^\\circ$",
        "$45^\\circ$",
        "$60^\\circ$"
      ],
      "correctAnswer": 3,
      "hint": "The minimum angle of rotational symmetry for a regular $n$-sided polygon is $\\frac{360^\\circ}{n}$.",
      "explanation": "A regular polygon with $n$ sides has $n$-fold rotational symmetry. The minimum positive angle of rotation that maps the figure onto itself is $\\frac{360^\\circ}{n}$. For a regular hexagon ($n = 6$), the minimum angle is $\\frac{360^\\circ}{6} = 60^\\circ$. Choice A ($90^\\circ$) is for a square ($n = 4$). Choice B ($120^\\circ$) is a multiple of $60^\\circ$ and the minimum angle for an equilateral triangle ($n = 3$), but not the minimum for a hexagon. Choice C ($45^\\circ$) is for a regular octagon ($n = 8$)."
    },
    {
      "id": "p-1-4-mcq-15",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.4 Step It Out (TE p. 64), students identify uppercase letters that look identical after a $180^\\circ$ rotation about their center point. Which group consists ENTIRELY of letters with $180^\\circ$ rotational symmetry?",
      "options": [
        "$\\text{A, M, T, V}$",
        "$\\text{B, C, D, E}$",
        "$\\text{H, N, O, Z}$",
        "$\\text{F, G, J, L}$"
      ],
      "correctAnswer": 2,
      "hint": "Imagine turning the letters upside down ($180^\\circ$). Which group contains letters that still look exactly the same?",
      "explanation": "As highlighted in the Teacher Edition (p. 64 Turn and Talk), the uppercase letters possessing $180^\\circ$ rotational symmetry are H, I, N, O, S, X, and Z. Turning any of these letters upside down results in the exact same letter. Choice A contains letters with vertical reflection symmetry (turning upside down reverses 'M' into 'W' and inverts 'A'). Choice B contains letters with horizontal reflection symmetry. Choice D contains asymmetric letters with neither reflectional nor rotational symmetry."
    },
    {
      "id": "p-1-4-mcq-16",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In Lesson 1.4 On Your Own (TE p. 67 Problem 9), a triangle has vertices at $(-2, 1)$, $(-5, 2)$, and $(-3, 6)$. After a rotation about the origin, the image has vertices at $(1, 2)$, $(2, 5)$, and $(6, 3)$. Which rotation was performed?",
      "options": [
        "$90^\\circ$ counterclockwise rotation about the origin",
        "$180^\\circ$ rotation about the origin",
        "$360^\\circ$ rotation about the origin",
        "$90^\\circ$ clockwise rotation about the origin"
      ],
      "correctAnswer": 3,
      "hint": "Compare $(x, y) = (-2, 1)$ with its image $(x', y') = (1, 2)$. How do the positions and signs of $x$ and $y$ relate?",
      "explanation": "Testing preimage point $(-2, 1)$ against image $(1, 2)$: The original $y$-value ($1$) becomes the new $x'$-value, and the opposite of the original $x$-value ($-(-2) = 2$) becomes the new $y'$-value. This matches the algebraic rule $(x, y) \\to (y, -x)$. Checking the other vertices confirms this rule: $(-5, 2) \\to (2, -(-5)) = (2, 5)$ and $(-3, 6) \\to (6, -(-3)) = (6, 3)$. The rule $(x, y) \\to (y, -x)$ represents a $90^\\circ$ clockwise rotation about the origin (or $270^\\circ$ counterclockwise). Choice A is $90^\\circ$ counterclockwise, which follows $(-y, x)$ and would yield $(-1, -2)$. Choice B is $180^\\circ$, which follows $(-x, -y)$ and would yield $(2, -1)$. Choice C is $360^\\circ$, which leaves coordinates unchanged."
    },
    {
      "id": "p-1-4-mcq-17",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "In Lesson 1.4 (TE p. 67 Problem 10), a shape is first rotated by the rule $(x, y) \\to (y, -x)$, and then the resulting image is rotated by the rule $(x, y) \\to (-x, -y)$. Which single transformation maps the original preimage directly to the final image?",
      "options": [
        "A $90^\\circ$ counterclockwise rotation about the origin: $(x, y) \\to (-y, x)$",
        "A $90^\\circ$ clockwise rotation about the origin: $(x, y) \\to (y, -x)$",
        "A $180^\\circ$ rotation about the origin: $(x, y) \\to (-x, -y)$",
        "A $360^\\circ$ rotation about the origin: $(x, y) \\to (x, y)$"
      ],
      "correctAnswer": 0,
      "hint": "Track what happens to the coordinates step-by-step: first $(x, y) \\to (y, -x)$, then apply the second rule $(-x, -y)$ to the intermediate coordinates $(y, -x)$.",
      "explanation": "Let us compose the two rules step-by-step: Step 1 applies $(x, y) \\to (y, -x)$ (a $90^\\circ$ clockwise rotation). Step 2 applies $(-x, -y)$ (a $180^\\circ$ rotation), which negates both components of the intermediate pair: $(y, -x) \\to (-y, -(-x)) = (-y, x)$. The resulting composite rule is $(x, y) \\to (-y, x)$, which is a $90^\\circ$ counterclockwise rotation about the origin. Geometrically, rotating $90^\\circ$ clockwise ($-90^\\circ$) followed by $180^\\circ$ yields $-90^\\circ + 180^\\circ = +90^\\circ$ (or $90^\\circ$ counterclockwise). Choices B, C, and D do not match the composite mapping rule."
    },
    {
      "id": "p-1-4-mcq-18",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.4 Check Understanding (TE p. 65 Problem 1), Antoine and Bobby each rotated a pentagon about Point $P$, but got different results. Bobby's transformed pentagon has the exact same orientation (sides remain parallel to the original directions and it points upward like the preimage). Antoine's transformed pentagon turned so that its top vertex now points to the right. Which student performed a correct rotation?",
      "options": [
        "Bobby, because rigid motions must keep all corresponding sides parallel to their preimages.",
        "Antoine, because rotating around a point turns the figure and changes the direction it faces; Bobby performed a translation.",
        "Both students performed valid rotations of different angles about Point $P$.",
        "Neither student is correct, because Point $P$ must be the origin $(0, 0)$."
      ],
      "correctAnswer": 1,
      "hint": "What is the key visual difference between sliding a figure (translation) and turning a figure around a pivot point (rotation)?",
      "explanation": "As stated in the Into Math Teacher Edition (p. 65 Check Understanding 1): 'Antoine\u2019s rotation is correct. Bobby appears to have performed a translation.' In a rotation, all points travel along circular arcs around the center of rotation, which alters the direction the figure faces. Bobby merely slid the figure without turning it, which is the definition of a translation. Choice A is incorrect because rotations do not keep sides parallel to their preimages (except for $180^\\circ$ rotations). Choice D is incorrect because any point in the plane can serve as a center of rotation."
    },
    {
      "id": "p-1-4-mcq-19",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A student attempts to rotate the point $M(4, -3)$ by $90^\\circ$ counterclockwise about the origin, but writes the image coordinates as $M'(-4, -3)$. What error did the student commit?",
      "options": [
        "The student correctly applied the $90^\\circ$ counterclockwise rotation rule.",
        "The student performed a $180^\\circ$ rotation about the origin.",
        "The student performed a $90^\\circ$ clockwise rotation instead of counterclockwise.",
        "The student only negated the $x$-coordinate, producing a reflection across the $y$-axis instead of swapping the coordinates and negating $y$ via $(x, y) \\to (-y, x)$."
      ],
      "correctAnswer": 3,
      "hint": "Recall the $90^\\circ$ counterclockwise rule: $(x, y) \\to (-y, x)$. Did the student swap the $x$ and $y$ values?",
      "explanation": "The correct rule for a $90^\\circ$ counterclockwise rotation is $(x, y) \\to (-y, x)$. For $M(4, -3)$, the correct image is $M'(-(-3), 4) = M'(3, 4)$. The student wrote $(-4, -3)$, which kept the coordinates in their original positions and only negated $x$: $(x, y) \\to (-x, y)$. This is a reflection across the $y$-axis, not a rotation. The student forgot to swap the coordinates. Choice B ($180^\\circ$ rotation) would result in $(-4, 3)$. Choice C ($90^\\circ$ clockwise rotation) would result in $(-3, -4)$."
    },
    {
      "id": "p-1-4-mcq-20",
      "module": 1,
      "lesson": "1.4",
      "topic": "Explore Rotations",
      "standard": "CCSS.MATH.CONTENT.8.G.A.1, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "In Lesson 1.4 Test Prep (TE p. 69 Problem 6), triangle $MNP$ is rotated about vertex $P$ to produce triangle $PQR$. Which of the following geometric properties MUST be true regarding vertex $P$ and the transformation?",
      "options": [
        "Vertex $P$ must move according to the coordinate origin rule $(x, y) \\to (-y, x)$.",
        "The area of $\\triangle PQR$ is cut in half because one vertex is pinned at the center.",
        "Vertex $P$ remains at its exact location ($P' = P$) because it is the center of rotation, and side lengths and angle measures are preserved.",
        "The orientation of the vertices reverses from clockwise to counterclockwise."
      ],
      "correctAnswer": 2,
      "hint": "The center of rotation does not move during a rotation, and rotations are rigid motions.",
      "explanation": "When a figure is rotated about one of its own vertices (Point $P$), that vertex serves as the center of rotation and is a fixed point: its image coincides with itself ($P' = P$). Furthermore, because rotation is a rigid motion, all side lengths, angle measures, and areas are strictly preserved ($\\text{Area}(\\triangle PQR) = \\text{Area}(\\triangle MNP)$), and vertex orientation is preserved. Choice A incorrectly applies an origin-centered rule to a vertex-centered rotation. Choice B falsely claims area changes. Choice D confuses rotations with reflections (which reverse orientation)."
    }
  ],
  "1.5": [
    {
      "id": "p-1-5-mcq-1",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "According to the geometric definition of congruence based on transformations, two two-dimensional figures are congruent ($\\cong$) if and only if:",
      "options": [
        "There is a sequence of one or more rigid motions (translations, reflections, rotations) that maps one figure onto the other.",
        "One figure can be mapped onto the other using a dilation with a scale factor $k > 1$.",
        "Both figures have the exact same number of sides, regardless of side lengths or interior angle measures.",
        "The figures have the same perimeter even if their corresponding angle measures are different."
      ],
      "correctAnswer": 0,
      "hint": "Recall from Into Math Lesson 1.5 that rigid motions preserve both side lengths and angle measures without stretching, shrinking, or distorting.",
      "explanation": "By the Common Core and HMH Into Math definition (8.G.A.2), two figures are congruent ($\\cong$) if and only if there is a sequence of rigid motions (translations, reflections, and rotations) that maps one figure exactly onto the other. Rigid motions preserve distance and angle measure.\n\u2022 Distractor B describes an enlargement dilation, which changes size ($k \\neq 1$) and produces similar, not congruent, figures.\n\u2022 Distractor C is incorrect because having the same number of sides (e.g., any two arbitrary triangles) does not guarantee identical shape or size.\n\u2022 Distractor D is incorrect because equal perimeter does not guarantee congruent shapes (e.g., a $3 \\times 5$ rectangle and a $4 \\times 4$ square both have perimeter 16, but different shapes)."
    },
    {
      "id": "p-1-5-mcq-2",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Polygon $P$ undergoes a transformation on the Cartesian coordinate plane. Which resulting polygon is **guaranteed** to be congruent to Polygon $P$ ($P \\cong \\text{Image}$)? ",
      "options": [
        "Polygon $Q$ formed by multiplying all coordinates by $1.5$: $(x, y) \\to (1.5x, 1.5y)$",
        "Polygon $R$ formed by a horizontal stretch: $(x, y) \\to (3x, y)$",
        "Polygon $S$ formed by a $90^\\circ$ counterclockwise rotation followed by a translation 6 units left: $(x, y) \\to (-y - 6, x)$",
        "Polygon $T$ formed by adding 4 to $x$ while multiplying $y$ by $0.5$: $(x, y) \\to (x + 4, 0.5y)$"
      ],
      "correctAnswer": 2,
      "hint": "Identify which operation is a composition composed purely of rigid motions (isometries) that preserve distances between all pairs of points.",
      "explanation": "Rotations and translations are rigid motions. Any sequence consisting solely of rigid motions preserves all distances and angle measures, guaranteeing that the image is congruent to the preimage ($P \\cong S$). A $90^\\circ$ rotation counterclockwise maps $(x, y) \\to (-y, x)$, and a translation 6 units left maps that to $(-y - 6, x)$.\n\u2022 Distractor A is a dilation by scale factor $1.5$, which increases side lengths by $50\\%$.\n\u2022 Distractor B triples the horizontal dimension, distorting the shape.\n\u2022 Distractor D compresses the vertical dimension by half ($0.5y$), destroying congruence."
    },
    {
      "id": "p-1-5-mcq-3",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Given the formal congruence statement $\\triangle MNP \\cong \\triangle STW$, which pair of corresponding parts **must** be congruent?",
      "options": [
        "Side $MN \\cong \\text{side } TW$ and $\\angle P \\cong \\angle S$",
        "Side $NP \\cong \\text{side } TW$ and $\\angle M \\cong \\angle S$",
        "Side $MP \\cong \\text{side } ST$ and $\\angle N \\cong \\angle W$",
        "Side $MN \\cong \\text{side } SW$ and $\\angle P \\cong \\angle T$"
      ],
      "correctAnswer": 1,
      "hint": "In a congruence statement, vertices are written in exact matching order: 1st to 1st ($M \\leftrightarrow S$), 2nd to 2nd ($N \\leftrightarrow T$), and 3rd to 3rd ($P \\leftrightarrow W$).",
      "explanation": "The order of vertices in a congruence statement defines the one-to-one correspondence:\n\u2022 1st vertex: $M \\leftrightarrow S$\n\u2022 2nd vertex: $N \\leftrightarrow T$\n\u2022 3rd vertex: $P \\leftrightarrow W$\nTherefore, side $NP$ (vertices 2 and 3) corresponds to side $TW$ (vertices 2 and 3), and $\\angle M$ (vertex 1) corresponds to $\\angle S$ (vertex 1). Hence, side $NP \\cong \\text{side } TW$ and $\\angle M \\cong \\angle S$.\n\u2022 Distractor A mismatches side $MN$ (1-2) with $TW$ (2-3) and $\\angle P$ (3) with $\\angle S$ (1).\n\u2022 Distractor C mismatches side $MP$ (1-3) with $ST$ (1-2) and $\\angle N$ (2) with $\\angle W$ (3).\n\u2022 Distractor D mismatches side $MN$ (1-2) with $SW$ (1-3) and $\\angle P$ (3) with $\\angle T$ (2)."
    },
    {
      "id": "p-1-5-mcq-4",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle ABC$ has vertices $A(1, 2)$, $B(4, 2)$, and $C(1, 6)$. It is reflected across the $y$-axis to produce an image with vertices $X(-1, 2)$, $Y(-4, 2)$, and $Z(-1, 6)$, where $A$ maps to $X$, $B$ maps to $Y$, and $C$ maps to $Z$. Which congruence statement correctly expresses this relationship?",
      "options": [
        "$\\triangle ABC \\cong \\triangle YXZ$",
        "$\\triangle ABC \\cong \\triangle ZYX$",
        "$\\triangle ABC \\cong \\triangle YZX$",
        "$\\triangle ABC \\cong \\triangle XYZ$"
      ],
      "correctAnswer": 3,
      "hint": "Match each letter in the preimage to its specific reflection image: $A(1, 2) \\to X(-1, 2)$, $B(4, 2) \\to Y(-4, 2)$, $C(1, 6) \\to Z(-1, 6)$.",
      "explanation": "Under reflection across the $y$-axis, $(x, y) \\to (-x, y)$:\n\u2022 $A(1, 2) \\to X(-1, 2)$, so $A \\leftrightarrow X$\n\u2022 $B(4, 2) \\to Y(-4, 2)$, so $B \\leftrightarrow Y$\n\u2022 $C(1, 6) \\to Z(-1, 6)$, so $C \\leftrightarrow Z$\nA congruence statement must write matching vertices in the exact same positional sequence. Therefore, $\\triangle ABC \\cong \\triangle XYZ$ is the only correctly ordered statement.\n\u2022 Distractors A, B, and C place the vertices out of correspondence."
    },
    {
      "id": "p-1-5-mcq-5",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "If $\\triangle DEF \\cong \\triangle JKL$, with $m\\angle D = 43^\\circ$, $m\\angle E = 79^\\circ$, side $DE = 6.8\\text{ cm}$, and side $EF = 9.2\\text{ cm}$, what are the measure of $\\angle L$ and the length of side $JK$?",
      "options": [
        "$m\\angle L = 58^\\circ$ and $JK = 6.8\\text{ cm}$",
        "$m\\angle L = 43^\\circ$ and $JK = 9.2\\text{ cm}$",
        "$m\\angle L = 79^\\circ$ and $JK = 6.8\\text{ cm}$",
        "$m\\angle L = 58^\\circ$ and $JK = 9.2\\text{ cm}$"
      ],
      "correctAnswer": 0,
      "hint": "Use the triangle angle sum ($180^\\circ$) to calculate $m\\angle F$ first. Then use CPCTC: $\\angle L \\cong \\angle F$ and side $JK \\cong \\text{side } DE$.",
      "explanation": "Step 1: Find the missing angle measure in $\\triangle DEF$ using the Triangle Angle Sum Theorem:\n$$m\\angle F = 180^\\circ - (43^\\circ + 79^\\circ) = 180^\\circ - 122^\\circ = 58^\\circ$$\nStep 2: By CPCTC (Corresponding Parts of Congruent Triangles are Congruent):\n\u2022 Vertex $F$ corresponds to vertex $L$, so $m\\angle L = m\\angle F = 58^\\circ$.\n\u2022 Side $DE$ (vertices 1-2) corresponds to side $JK$ (vertices 1-2), so $JK = DE = 6.8\\text{ cm}$.\n\u2022 Distractor B incorrectly equates $\\angle L$ with $\\angle D$ and $JK$ with $EF$.\n\u2022 Distractor C incorrectly equates $\\angle L$ with $\\angle E$.\n\u2022 Distractor D gets the angle right ($58^\\circ$) but mistakenly pairs $JK$ with $EF$ ($9.2\\text{ cm}$)."
    },
    {
      "id": "p-1-5-mcq-6",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Quadrilaterals $ABCD$ and $EFGH$ are congruent ($ABCD \\cong EFGH$). If side $BC = 4x - 7$ and corresponding side $FG = 2x + 9$, what is the actual numerical length of side $FG$?",
      "options": [
        "$x = 8$, so $FG = 17$",
        "$x = 1$, so $FG = 11$",
        "$x = 8$, so $FG = 25$",
        "$x = 16$, so $FG = 41$"
      ],
      "correctAnswer": 2,
      "hint": "Corresponding sides of congruent figures have equal lengths. Set $4x - 7 = 2x + 9$ to solve for $x$, then substitute $x$ into $2x + 9$.",
      "explanation": "Step 1: Set the lengths of corresponding sides equal because $ABCD \\cong EFGH$ implies $BC = FG$:\n$$4x - 7 = 2x + 9$$\nStep 2: Solve the linear equation for $x$:\n$$4x - 2x = 9 + 7 \\implies 2x = 16 \\implies x = 8$$\nStep 3: Substitute $x = 8$ back into the expression for $FG$:\n$$FG = 2(8) + 9 = 16 + 9 = 25$$\n(Check: $BC = 4(8) - 7 = 32 - 7 = 25$, confirming $BC = FG$).\n\u2022 Distractor A solves $x = 8$ correctly but subtracts 8 from 25 or miscalculates $2(8) + 1$.\n\u2022 Distractor B makes a sign error when moving terms ($4x - 2x = 9 - 7 \\implies 2x = 2 \\implies x = 1$).\n\u2022 Distractor D forgets to divide 16 by 2 when solving $2x = 16$."
    },
    {
      "id": "p-1-5-mcq-7",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "A polygon vertex located at $P(-3, 5)$ undergoes a two-step sequence of rigid motions:\n\u2022 **Step 1:** Reflection across the $x$-axis.\n\u2022 **Step 2:** Translation by the vector rule $(x, y) \\to (x + 7, y - 2)$.\nWhat are the coordinates of the final image point $P''$?",
      "options": [
        "$(4, 3)$",
        "$(4, -7)$",
        "$(-10, -7)$",
        "$(4, -3)$"
      ],
      "correctAnswer": 1,
      "hint": "Apply the transformations in order: first reflect across the $x$-axis: $(x, y) \\to (x, -y)$, then apply the translation to the resulting coordinates.",
      "explanation": "Step 1 (Reflection across $x$-axis): The rule is $(x, y) \\to (x, -y)$.\n$$P(-3, 5) \\to P'(-3, -5)$$\nStep 2 (Translation $(x + 7, y - 2)$):\n$$P'(-3, -5) \\to P''(-3 + 7, -5 - 2) = P''(4, -7)$$\n\u2022 Distractor A translates the original point $P(-3, 5)$ directly without reflecting: $(-3 + 7, 5 - 2) = (4, 3)$.\n\u2022 Distractor C subtracts 7 from $x$ instead of adding: $(-3 - 7, -5 - 2) = (-10, -7)$.\n\u2022 Distractor D reflects across the $y$-axis first instead of the $x$-axis: $(3, 5) \\to (3 + 7, 5 - 2) = (10, 3)$ or miscalculates $-5 - 2$."
    },
    {
      "id": "p-1-5-mcq-8",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.5 Task 3, students investigate whether the order of transformations matters. Starting with the point $A(2, 5)$:\n\u2022 **Order 1:** Reflect across the $y$-axis, then translate 3 units right.\n\u2022 **Order 2:** Translate 3 units right, then reflect across the $y$-axis.\nWhat are the resulting coordinates for Order 1 and Order 2, and what key geometric principle does this prove?",
      "options": [
        "Order 1 produces $(1, 5)$; Order 2 produces $(1, 5)$. This proves that the order of transformations never matters.",
        "Order 1 produces $(-5, 5)$; Order 2 produces $(5, 5)$. This proves that reflecting across an axis doubles distance.",
        "Order 1 produces $(-1, 5)$; Order 2 produces $(-5, 5)$. This proves that the figures cease to be congruent.",
        "Order 1 produces $(1, 5)$; Order 2 produces $(-5, 5)$. This proves that transformation composition is non-commutative (order matters)."
      ],
      "correctAnswer": 3,
      "hint": "Calculate the coordinates for each order separately. For Order 1: reflect across $y$-axis first, then add 3 to $x$. For Order 2: add 3 to $x$ first, then reflect across $y$-axis.",
      "explanation": "Order 1:\n1. Reflect $A(2, 5)$ across the $y$-axis: $(x, y) \\to (-x, y) \\implies A'(-2, 5)$.\n2. Translate 3 units right: $(-2 + 3, 5) = (1, 5)$.\nOrder 2:\n1. Translate $A(2, 5)$ 3 units right: $(2 + 3, 5) = (5, 5)$.\n2. Reflect $(5, 5)$ across the $y$-axis: $(x, y) \\to (-x, y) \\implies (-5, 5)$.\nBecause $(1, 5) \\neq (-5, 5)$, the order in which transformations are performed affects the final position. This demonstrates that transformation composition is generally non-commutative ($T_2 \\circ T_1 \\neq T_1 \\circ T_2$).\n\u2022 Distractor A incorrectly claims that order never matters.\n\u2022 Distractor B has incorrect coordinates for Order 1.\n\u2022 Distractor C incorrectly claims the figures are no longer congruent; rigid motions always preserve congruence even when landing at different locations."
    },
    {
      "id": "p-1-5-mcq-9",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 1,
      "type": "multiple_choice",
      "question": "In transformational geometry, what is the precise definition of a **glide reflection** mapping a geometric figure $F$ onto its congruent image $F'$ ($F \\cong F'$)? ",
      "options": [
        "A sequence consisting of a translation along a line followed by a reflection across that same line (or a line parallel to the translation direction).",
        "A reflection across a line followed by a rotation of $180^\\circ$ about a point on that line.",
        "A translation followed by an enlargement dilation with scale factor $k = 1.5$.",
        "Two consecutive reflections across two perpendicular coordinate axes that produce a half-turn."
      ],
      "correctAnswer": 0,
      "hint": "Think of footprints left by walking in wet sand: one foot steps forward (translation) and reflects across the centerline.",
      "explanation": "A **glide reflection** is defined as the composition of a translation (the glide) and a reflection across a line that is parallel to the direction of translation (or along the line of translation itself). Because both translations and reflections are isometries, a glide reflection is an isometry that reverses orientation.\n\u2022 Distractor B describes a reflection combined with a rotation, not a glide reflection.\n\u2022 Distractor C includes a dilation, which alters size and is non-rigid.\n\u2022 Distractor D describes reflections across intersecting perpendicular lines, which is equivalent to a $180^\\circ$ rotation, not a glide reflection."
    },
    {
      "id": "p-1-5-mcq-10",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle ABC$ has vertices $A(1, 2)$, $B(4, 2)$, and $C(1, 5)$. It undergoes a glide reflection composed of:\n1. A translation by the rule $(x, y) \\to (x + 3, y)$\n2. A reflection across the $x$-axis ($y = 0$).\nWhat are the vertices of the image triangle $\\triangle A''B''C''$?",
      "options": [
        "$A''(4, 2), B''(7, 2), C''(4, 5)$",
        "$A''(-4, -2), B''(-7, -2), C''(-4, -5)$",
        "$A''(4, -2), B''(7, -2), C''(4, -5)$",
        "$A''(1, -5), B''(4, -5), C''(1, -8)$"
      ],
      "correctAnswer": 2,
      "hint": "First add 3 to each $x$-coordinate: $(x + 3, y)$. Then reflect across the $x$-axis by negating each $y$-coordinate: $(x, -y)$.",
      "explanation": "Step 1: Translate $(x, y) \\to (x + 3, y)$:\n\u2022 $A(1, 2) \\to A'(1 + 3, 2) = (4, 2)$\n\u2022 $B(4, 2) \\to B'(4 + 3, 2) = (7, 2)$\n\u2022 $C(1, 5) \\to C'(1 + 3, 5) = (4, 5)$\nStep 2: Reflect across the $x$-axis: $(x, y) \\to (x, -y)$:\n\u2022 $A'(4, 2) \\to A''(4, -2)$\n\u2022 $B'(7, 2) \\to B''(7, -2)$\n\u2022 $C'(4, 5) \\to C''(4, -5)$\n\u2022 Distractor A performs only the translation and forgets the reflection.\n\u2022 Distractor B incorrectly negates the $x$-coordinates as well.\n\u2022 Distractor D applies the translation to $y$ instead of $x$."
    },
    {
      "id": "p-1-5-mcq-11",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.5 On Your Own Problem 3, students are asked: \"Can a square with side length $s_1$ ever be congruent to a regular pentagon with side length $s_2$? Explain.\"\nWhich response provides the mathematically correct explanation?",
      "options": [
        "Yes, as long as both polygons are scaled so that their perimeters are equal.",
        "No, because congruent figures must have the exact same size and shape. A square has 4 sides and four $90^\\circ$ angles, while a regular pentagon has 5 sides and five $108^\\circ$ angles; no sequence of rigid motions can change the number of sides or angle measures.",
        "Yes, because a square can be transformed into a pentagon by a sequence of a reflection followed by a dilation with scale factor $k = \\frac{5}{4}$.",
        "No, because squares are two-dimensional planar figures while pentagons are three-dimensional polyhedra."
      ],
      "correctAnswer": 1,
      "hint": "Consider the invariance properties of rigid motions: rigid motions preserve the number of vertices, side lengths, and angle measures.",
      "explanation": "Congruent figures must have identical shape and size. A square has 4 vertices, 4 sides, and interior angles of $90^\\circ$. A regular pentagon has 5 vertices, 5 sides, and interior angles of $108^\\circ$. Because rigid motions preserve the number of sides and the measures of all angles, no sequence of translations, reflections, and rotations can map a 4-sided polygon onto a 5-sided polygon.\n\u2022 Distractor A is false; having equal perimeters does not make different shapes congruent.\n\u2022 Distractor C is false; dilations are not rigid motions, and dilating a square cannot add a fifth side.\n\u2022 Distractor D is false; both squares and pentagons are two-dimensional polygons."
    },
    {
      "id": "p-1-5-mcq-12",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Figure 1 is a rectangle with dimensions $4\\text{ cm} \\times 9\\text{ cm}$ (area $= 36\\text{ cm}^2$). Figure 2 is a square with dimensions $6\\text{ cm} \\times 6\\text{ cm}$ (area $= 36\\text{ cm}^2$). Are Figure 1 and Figure 2 congruent?",
      "options": [
        "Yes, because both figures have the exact same area of $36\\text{ cm}^2$.",
        "Yes, because both figures have four $90^\\circ$ interior angles.",
        "No, because rigid motions cannot be performed on figures that have right angles.",
        "No, because their corresponding side lengths are not equal ($4 \\neq 6$ and $9 \\neq 6$), and rigid motions strictly preserve distance; equal area alone does not establish congruence."
      ],
      "correctAnswer": 3,
      "hint": "Check whether rigid motions preserve side lengths. Can you translate, reflect, or rotate a side of length 4 cm so that it covers a side of length 6 cm without stretching?",
      "explanation": "While both figures have the same area ($36\\text{ cm}^2$) and both have four right angles, their side lengths are different ($4$ and $9$ vs. $6$ and $6$). Because rigid motions preserve distance (segment length), any image of Figure 1 must have side lengths of $4\\text{ cm}$ and $9\\text{ cm}$. It is impossible to map a side of length $4\\text{ cm}$ onto a side of length $6\\text{ cm}$ using rigid motions. Thus, Figure 1 is not congruent to Figure 2.\n\u2022 Distractor A is a common student trap: equal area is necessary for congruence, but not sufficient.\n\u2022 Distractor B is incorrect because having equal angles only implies similarity (for certain shapes), not congruence.\n\u2022 Distractor C is mathematically absurd; rigid motions apply to all geometric figures."
    },
    {
      "id": "p-1-5-mcq-13",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "On a math critique task (HMH Into Math Problem 8), Nathan claims: \"Figure $B$ is congruent to Figure $A$ because both figures have the exact same orientation on the grid.\" How should Nathan's mathematical reasoning be evaluated?",
      "options": [
        "Nathan is incorrect. Having the same orientation is neither necessary nor sufficient for congruence; two figures are congruent if and only if there is a sequence of rigid motions mapping one onto the other, which preserves all side lengths and angle measures.",
        "Nathan is correct because having the same orientation is the definition of congruence in the coordinate plane.",
        "Nathan is correct because reflections reverse orientation, meaning reflected figures can never be congruent.",
        "Nathan is incorrect because congruent figures must always have opposite orientations."
      ],
      "correctAnswer": 0,
      "hint": "Can two figures face the same direction but have completely different sizes? Can two congruent figures face opposite directions?",
      "explanation": "Nathan's reasoning is mathematically flawed on two levels:\n1. Having the same orientation is not sufficient: a dilated triangle can have the exact same orientation as its preimage, but have double the size (not congruent).\n2. Having the same orientation is not necessary: a figure reflected across a line has reversed orientation, yet it remains completely congruent to its preimage.\nTwo figures are congruent if and only if a sequence of rigid motions maps one onto the other.\n\u2022 Distractors B, C, and D reflect common student misconceptions regarding orientation and congruence."
    },
    {
      "id": "p-1-5-mcq-14",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.5 Problem 14, Henrietta claims that Figure $B$ can be transformed into Figure $A$ by translating it 2 units right and then rotating it $90^\\circ$ clockwise about the origin. However, following Henrietta's instructions places the image in the wrong quadrant. How should Henrietta's sequence be corrected?",
      "options": [
        "She must replace the rotation with a dilation of scale factor $k = 1$.",
        "She must perform the transformations in the reverse order: rotate $90^\\circ$ clockwise about the origin first, and then translate the resulting figure.",
        "She must reflect the figure across the diagonal line $y = x$ instead of rotating.",
        "She must translate the figure 4 units down before doing anything else."
      ],
      "correctAnswer": 1,
      "hint": "Check Into Math TE Page 79 Problem 14: 'The transformations must be done in the other order.' Rotating after translating swings the translation displacement around the origin!",
      "explanation": "When a figure is translated first and then rotated about the origin, the rotation affects both the figure's shape orientation and its entire position vector relative to the origin. In Into Math Lesson 1.5 Problem 14, the TE explicitly notes: 'The transformations must be done in the other order.' Rotating $90^\\circ$ clockwise about the origin first, followed by the translation, places the figure in the exact location of Figure $A$.\n\u2022 Distractor A is incorrect because dilating by $k = 1$ is an identity transformation that does not change position.\n\u2022 Distractors C and D suggest incorrect transformation families or wrong translation vectors."
    },
    {
      "id": "p-1-5-mcq-15",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Right triangle $\\triangle ABC$ has legs of length $5\\text{ units}$ and $12\\text{ units}$. It undergoes a multi-step sequence of rigid motions: a rotation of $90^\\circ$ clockwise about the origin, followed by a translation of $(x - 4, y + 6)$, and finally a reflection across the line $y = 3$. What are the perimeter and area of the final image triangle $\\triangle A'''B'''C'''$?",
      "options": [
        "$\\text{Perimeter} = 17\\text{ units}$ and $\\text{Area} = 30\\text{ sq units}$",
        "$\\text{Perimeter} = 30\\text{ units}$ and $\\text{Area} = 60\\text{ sq units}$",
        "$\\text{Perimeter} = 30\\text{ units}$ and $\\text{Area} = 30\\text{ sq units}$",
        "$\\text{Perimeter} = 60\\text{ units}$ and $\\text{Area} = 30\\text{ sq units}$"
      ],
      "correctAnswer": 2,
      "hint": "Find the hypotenuse using the Pythagorean theorem: $c = \\sqrt{5^2 + 12^2}$. Then recall that rigid motions preserve both perimeter and area.",
      "explanation": "Step 1: Compute the hypotenuse and measurements of the preimage $\\triangle ABC$:\n$$c = \\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13\\text{ units}$$\n$$\\text{Perimeter} = 5 + 12 + 13 = 30\\text{ units}$$\n$$\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2}(5)(12) = 30\\text{ sq units}$$\nStep 2: Because rotations, translations, and reflections are all rigid motions (isometries), distances and enclosed areas are strictly invariant.\nTherefore, $\\text{Perimeter}(\\triangle A'''B'''C''') = 30\\text{ units}$ and $\\text{Area}(\\triangle A'''B'''C''') = 30\\text{ sq units}$.\n\u2022 Distractor A fails to include the hypotenuse in the perimeter ($5 + 12 = 17$).\n\u2022 Distractor B forgets the $\\frac{1}{2}$ in the triangle area formula ($5 \\times 12 = 60$).\n\u2022 Distractor D mistakenly doubles the perimeter."
    },
    {
      "id": "p-1-5-mcq-16",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "Polygon $G$ has a perimeter of $34\\text{ cm}$ and an area of $60\\text{ cm}^2$. Polygon $H$ is the result of applying a transformation to Polygon $G$. Which condition **proves definitively** that Polygon $H$ is **NOT** congruent to Polygon $G$?",
      "options": [
        "Polygon $H$ has its vertices labeled in counterclockwise order while Polygon $G$ has vertices in clockwise order.",
        "Polygon $H$ lies entirely in Quadrant IV while Polygon $G$ lies in Quadrant II.",
        "Polygon $H$ is rotated $180^\\circ$ relative to Polygon $G$.",
        "Polygon $H$ has a perimeter of $38\\text{ cm}$."
      ],
      "correctAnswer": 3,
      "hint": "Rigid motions preserve distances, so the perimeter of a transformed figure must remain strictly unchanged if the figures are congruent.",
      "explanation": "A sequence of rigid motions preserves all segment lengths, which means the sum of side lengths (perimeter) must remain exactly the same. If Polygon $H$ has a perimeter of $38\\text{ cm}$ while Polygon $G$ has a perimeter of $34\\text{ cm}$, the side lengths have changed ($38 \\neq 34$). Therefore, no sequence of rigid motions can map $G$ to $H$, proving definitively that $G \\not\\cong H$.\n\u2022 Distractor A occurs whenever a reflection is performed; reflected shapes are still congruent.\n\u2022 Distractor B occurs when shapes are translated or rotated across quadrants; location does not affect congruence.\n\u2022 Distractor C is a rigid rotation, which preserves congruence."
    },
    {
      "id": "p-1-5-mcq-17",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.5 Spark Your Learning (quilt pattern), Maribel creates quilt blocks using congruent fabric triangles. One fabric triangle in Quadrant II has vertices at $(-5, 1)$, $(-2, 1)$, and $(-2, 5)$. Maribel rotates this triangle $180^\\circ$ about the center of the quilt $(0, 0)$ to place a congruent piece in Quadrant IV. What are the coordinates of the rotated quilt piece?",
      "options": [
        "$(5, -1)$, $(2, -1)$, and $(2, -5)$",
        "$(-5, -1)$, $(-2, -1)$, and $(-2, -5)$",
        "$(1, 5)$, $(1, 2)$, and $(5, 2)$",
        "$(-1, -5)$, $(-1, -2)$, and $(-5, -2)$"
      ],
      "correctAnswer": 0,
      "hint": "The coordinate rule for a $180^\\circ$ rotation about the origin is $(x, y) \\to (-x, -y)$.",
      "explanation": "Applying the coordinate rule for a $180^\\circ$ rotation about the origin, $(x, y) \\to (-x, -y)$:\n\u2022 $(-5, 1) \\to (-(-5), -(1)) = (5, -1)$\n\u2022 $(-2, 1) \\to (-(-2), -(1)) = (2, -1)$\n\u2022 $(-2, 5) \\to (-(-2), -(5)) = (2, -5)$\nAll coordinates are in Quadrant IV $(+, -)$. Because a rotation is a rigid motion, the rotated quilt block is guaranteed to be congruent to the original template.\n\u2022 Distractor B reflects across the $x$-axis only: $(x, -y)$.\n\u2022 Distractor C rotates $90^\\circ$ clockwise: $(y, -x)$ or swaps coordinates.\n\u2022 Distractor D rotates $90^\\circ$ counterclockwise: $(-y, x)$."
    },
    {
      "id": "p-1-5-mcq-18",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 2,
      "type": "multiple_choice",
      "question": "In HMH Into Math Lesson 1.5 Step It Out Task 2, five congruent triangles are positioned on a fabric grid. Triangle $B$ has vertices $(2, -1), (5, -1),$ and $(2, -4)$. Triangle $D$ has vertices $(8, 1), (11, 1),$ and $(8, 4)$. Which sequence of transformations maps Triangle $B$ onto Triangle $D$, proving $\\triangle B \\cong \\triangle D$?",
      "options": [
        "A translation 6 units right and 2 units up",
        "A $180^\\circ$ rotation about the origin",
        "A reflection across the $x$-axis followed by a translation 6 units right",
        "A reflection across the $y$-axis followed by a translation 10 units right"
      ],
      "correctAnswer": 2,
      "hint": "Notice that Triangle $B$ points down in the negative $y$-direction, while Triangle $D$ points up in the positive $y$-direction. This requires a reflection across a horizontal line!",
      "explanation": "Let's trace the vertices through the sequence in Choice C:\n1. Reflection across the $x$-axis: $(x, y) \\to (x, -y)$:\n\u2022 $(2, -1) \\to (2, 1)$\n\u2022 $(5, -1) \\to (5, 1)$\n\u2022 $(2, -4) \\to (2, 4)$\n2. Translation 6 units right: $(x, y) \\to (x + 6, y)$:\n\u2022 $(2, 1) \\to (2 + 6, 1) = (8, 1)$\n\u2022 $(5, 1) \\to (5 + 6, 1) = (11, 1)$\n\u2022 $(2, 4) \\to (2 + 6, 4) = (8, 4)$\nThese match the vertices of Triangle $D$ exactly! Since reflections and translations are rigid motions, $\\triangle B \\cong \\triangle D$.\n\u2022 Distractor A fails because a pure translation cannot change the vertical orientation from pointing down to pointing up.\n\u2022 Distractor B maps $(2, -1) \\to (-2, 1)$, placing the shape on the negative $x$-axis.\n\u2022 Distractor D reflects horizontally, leaving the shape still pointing downward."
    },
    {
      "id": "p-1-5-mcq-19",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "Triangle 1 has vertices $A(1, 1), B(4, 1),$ and $C(1, 3)$. Triangle 2 has vertices $D(-1, 2), E(-1, -1),$ and $F(1, 2)$. Which sequence of transformations maps Triangle 1 directly onto Triangle 2, proving that $\\triangle 1 \\cong \\triangle 2$?",
      "options": [
        "Translate 2 units left and 1 unit up, then reflect across the $x$-axis.",
        "Rotate $90^\\circ$ clockwise about the origin, then translate 2 units left and 3 units up.",
        "Reflect across the $y$-axis, then translate 3 units down and 1 unit right.",
        "Rotate $180^\\circ$ about the origin, then translate 1 unit right and 2 units up."
      ],
      "correctAnswer": 1,
      "hint": "Analyze the side orientation: In Triangle 1, the 3-unit leg $AB$ is horizontal. In Triangle 2, the 3-unit leg $DE$ is vertical. This rotation of $90^\\circ$ indicates a $90^\\circ$ turn!",
      "explanation": "Step 1: Rotate $90^\\circ$ clockwise about the origin using $(x, y) \\to (y, -x)$:\n\u2022 $A(1, 1) \\to A'(1, -1)$\n\u2022 $B(4, 1) \\to B'(1, -4)$\n\u2022 $C(1, 3) \\to C'(3, -1)$\nStep 2: Translate 2 units left and 3 units up: $(x, y) \\to (x - 2, y + 3)$:\n\u2022 $A'(1, -1) \\to (1 - 2, -1 + 3) = (-1, 2) = D$\n\u2022 $B'(1, -4) \\to (1 - 2, -4 + 3) = (-1, -1) = E$\n\u2022 $C'(3, -1) \\to (3 - 2, -1 + 3) = (1, 2) = F$\nThis maps Triangle 1 precisely onto Triangle 2. Because both transformations are rigid motions, $\\triangle 1 \\cong \\triangle 2$.\n\u2022 Distractors A, C, and D do not produce the correct orientation or vertex coordinates."
    },
    {
      "id": "p-1-5-mcq-20",
      "module": 1,
      "lesson": "1.5",
      "topic": "Understand Congruent Figures",
      "standard": "CCSS.MATH.CONTENT.8.G.A.2, 8.G.A.3",
      "dok": 3,
      "type": "multiple_choice",
      "question": "Triangle $\\triangle JKL$ with vertices $J(-5, 2), K(-2, 2),$ and $L(-2, 6)$ is transformed into $\\triangle PQR$ with vertices $P(5, -2), Q(2, -2),$ and $R(2, 2)$. Which sequence of rigid motions proves that $\\triangle JKL \\cong \\triangle PQR$?",
      "options": [
        "A reflection across the $y$-axis: $(x, y) \\to (-x, y)$, followed by a translation 4 units down: $(x, y) \\to (x, y - 4)$",
        "A translation 7 units right followed by a reflection across the line $y = x$",
        "A $90^\\circ$ counterclockwise rotation about the origin followed by a translation 2 units right",
        "A reflection across the $x$-axis followed by a translation 3 units left"
      ],
      "correctAnswer": 0,
      "hint": "Check the $x$-coordinates: $J(-5, 2) \\to P(5, -2)$ has $x$ negated from $-5$ to $5$, suggesting a reflection across the $y$-axis first.",
      "explanation": "Step 1: Reflect across the $y$-axis: $(x, y) \\to (-x, y)$:\n\u2022 $J(-5, 2) \\to J'(5, 2)$\n\u2022 $K(-2, 2) \\to K'(2, 2)$\n\u2022 $L(-2, 6) \\to L'(2, 6)$\nStep 2: Translate 4 units down: $(x, y) \\to (x, y - 4)$:\n\u2022 $J'(5, 2) \\to (5, 2 - 4) = (5, -2) = P$\n\u2022 $K'(2, 2) \\to (2, 2 - 4) = (2, -2) = Q$\n\u2022 $L'(2, 6) \\to (2, 6 - 4) = (2, 2) = R$\nThe image matches $\\triangle PQR$ in every coordinate. Because reflection and translation are rigid motions, this proves that $\\triangle JKL \\cong \\triangle PQR$.\n\u2022 Distractor B gives $(x + 7, y) \\to (y, x + 7)$, which does not match $\\triangle PQR$.\n\u2022 Distractor C rotates $90^\\circ$ counterclockwise, which turns horizontal sides vertical, whereas side $JK$ and side $PQ$ are both horizontal.\n\u2022 Distractor D reflects across the $x$-axis first, giving negative $x$ coordinates."
    }
  ]
};

  // --- 3. BUILTIN MODULE 2 PRACTICE BANK ---
  const BUILTIN_MODULE2_BANK = [
  {
    "id": "m2_q1",
    "module": 2,
    "lesson": "2.1",
    "topic": "Dilations",
    "type": "multiple_choice",
    "question": "A dilation centered at the origin maps (4, -6) to (10, -15). What is the scale factor k?",
    "options": [
      "k = 2.5",
      "k = 0.4",
      "k = 1.5",
      "k = 6"
    ],
    "correctAnswer": 0,
    "hint": "Calculate k = x' / x or y' / y: 10 / 4.",
    "explanation": "k = 10 / 4 = 2.5. Checking y: -15 / -6 = 2.5. Since k > 1, this is an enlargement with scale factor 2.5."
  },
  {
    "id": "m2_q2",
    "module": 2,
    "lesson": "2.1",
    "topic": "Dilations",
    "type": "coordinate_input",
    "question": "Point D(-9, 12) is dilated by a scale factor of k = 1/3 centered at the origin. What are the image coordinates?",
    "expectedCoords": {
      "x": -3,
      "y": 4
    },
    "hint": "Multiply both coordinates by the scale factor k = 1/3: (kx, ky).",
    "explanation": "x' = -9 * (1/3) = -3. y' = 12 * (1/3) = 4. The image D' is (-3, 4)."
  },
  {
    "id": "m2_q3",
    "module": 2,
    "lesson": "2.2",
    "topic": "Reductions & Enlargements",
    "type": "true_false",
    "question": "True or False: A dilation with a scale factor of k = 0.75 results in an enlargement of the original figure.",
    "correctAnswer": false,
    "justification": "Since 0 < k < 1, the transformation is a reduction, making the image smaller than the preimage.",
    "hint": "Enlargements require k > 1. What happens when 0 < k < 1?",
    "explanation": "False! When the scale factor k satisfies 0 < k < 1, the figure shrinks, which is a reduction. Enlargements require k > 1."
  },
  {
    "id": "m2_q4",
    "module": 2,
    "lesson": "2.2",
    "topic": "Reductions & Enlargements",
    "type": "multiple_choice",
    "question": "A photo measuring 4 inches by 6 inches is enlarged so that its longer side is 15 inches. What is the length of the shorter side?",
    "options": [
      "10 inches",
      "9 inches",
      "12 inches",
      "8 inches"
    ],
    "correctAnswer": 0,
    "hint": "Find the scale factor k from the longer side (15 / 6), then multiply by the shorter side (4).",
    "explanation": "Scale factor k = 15 / 6 = 2.5. Shorter side = 4 * 2.5 = 10 inches."
  },
  {
    "id": "m2_q5",
    "module": 2,
    "lesson": "2.3",
    "topic": "Similar Figures",
    "type": "multiple_choice",
    "question": "Two triangles are similar. Triangle 1 has side lengths 6, 8, 10. Triangle 2 has a shortest side of 15. What is the perimeter of Triangle 2?",
    "options": [
      "60",
      "48",
      "50",
      "72"
    ],
    "correctAnswer": 0,
    "hint": "Shortest side ratio k = 15 / 6 = 2.5. Perimeter of Triangle 1 = 6 + 8 + 10 = 24. Perimeter of Triangle 2 = 24 * k.",
    "explanation": "Scale factor k = 15 / 6 = 2.5. Perimeter of original = 6 + 8 + 10 = 24. Perimeter of similar triangle = 24 * 2.5 = 60."
  },
  {
    "id": "m2_q6",
    "module": 2,
    "lesson": "2.1",
    "topic": "Dilations",
    "type": "multiple_choice",
    "question": "Under any dilation centered at the origin, which property of geometric figures is ALWAYS preserved?",
    "options": [
      "Angle measures",
      "Perimeter",
      "Area",
      "Distance between points"
    ],
    "correctAnswer": 0,
    "hint": "Dilations preserve the shape of figures, meaning angles stay exactly the same even though side lengths change.",
    "explanation": "Dilations preserve angle measures and collinearity, but change distance, perimeter, and area by powers of the scale factor k."
  },
  {
    "id": "m2_q7",
    "module": 2,
    "lesson": "2.3",
    "topic": "Similar Figures",
    "type": "true_false",
    "question": "True or False: All congruent figures are similar, but not all similar figures are congruent.",
    "correctAnswer": true,
    "justification": "Congruent figures are similar figures with a scale factor of exactly k = 1.",
    "hint": "Consider whether congruence is just a special case of similarity.",
    "explanation": "True! Congruent figures have corresponding angles equal and side lengths in a 1:1 ratio (k = 1), so they are always similar. Similar figures with k \u2260 1 are not congruent."
  },
  {
    "id": "m2_q8",
    "module": 2,
    "lesson": "2.1",
    "topic": "Dilations",
    "type": "coordinate_input",
    "question": "Preimage point H(5, -2) is dilated by k = 4 centered at the origin. Enter the coordinates of H':",
    "expectedCoords": {
      "x": 20,
      "y": -8
    },
    "hint": "Multiply both x and y coordinates by 4: (5 * 4, -2 * 4).",
    "explanation": "Rule (x, y) \u2192 (kx, ky) with k = 4: x' = 5 * 4 = 20, y' = -2 * 4 = -8. Result: (20, -8)."
  },
  {
    "id": "m2_q9",
    "module": 2,
    "lesson": "2.2",
    "topic": "Reductions & Enlargements",
    "type": "multiple_choice",
    "question": "If the scale factor of a dilation is k = 3, by what factor does the AREA of the polygon increase?",
    "options": [
      "9 times",
      "3 times",
      "6 times",
      "27 times"
    ],
    "correctAnswer": 0,
    "hint": "While lengths scale by k, area scales by k\u00b2.",
    "explanation": "Area scales as k\u00b2. With k = 3, area is multiplied by 3\u00b2 = 9."
  },
  {
    "id": "m2_q10",
    "module": 2,
    "lesson": "2.3",
    "topic": "Similar Figures",
    "type": "sequence_builder",
    "question": "Order the steps to prove that Figure A is similar to Figure B on a coordinate plane:",
    "steps": [
      "Identify corresponding vertices and calculate the scale factor k between side lengths",
      "Apply a dilation by scale factor k centered at the origin",
      "Map the dilated figure onto Figure B using a sequence of rigid motions (translation/rotation/reflection)"
    ],
    "correctOrder": [
      0,
      1,
      2
    ],
    "hint": "First find the scale factor, dilate the shape, and then apply rigid transformations.",
    "explanation": "To establish similarity: 1) determine scale factor k, 2) dilate to match size, 3) apply rigid motions to map the vertices onto each other."
  }
];

  // Combined fallback bank
  const BUILTIN_QUIZ_BANK = AUTHENTIC_MODULE1_FINAL_TEST.concat(BUILTIN_MODULE2_BANK);

  // --- QUESTION NORMALIZER ---
  function normalizeQuestion(q) {
    if (!q) return null;
    const norm = {
      id: q.id || ('q_' + Math.random().toString(36).substr(2, 9)),
      module: q.module || (q.lesson && String(q.lesson).startsWith('1.') ? 1 : 2),
      lesson: q.lesson || (q.lessonId ? q.lessonId.replace('lesson-', '') : '1.1'),
      topic: q.topic || q.title || (LESSON_TOPICS[q.lesson] || 'Grade 8 Math'),
      standard: q.standard || '',
      dok: q.dok || 1,
      type: (q.type === 'multiple-choice' || !q.type) ? 'multiple_choice' : q.type,
      question: q.question || q.q || q.prompt || '',
      options: q.options || q.opts || [],
      correctAnswer: 0,
      hint: q.hint || '',
      explanation: q.explanation || '',
      expectedCoords: q.expectedCoords || null,
      steps: q.steps || null,
      correctOrder: q.correctOrder || null,
      justification: q.justification || ''
    };

    if (typeof q.correct === 'number') {
      norm.correctAnswer = q.correct;
    } else if (typeof q.correctAnswer === 'number') {
      norm.correctAnswer = q.correctAnswer;
    } else if (typeof q.correctAnswer === 'string' && Array.isArray(norm.options)) {
      const idx = norm.options.findIndex(function (opt) {
        return opt.trim() === q.correctAnswer.trim() || opt.startsWith(q.correctAnswer);
      });
      norm.correctAnswer = (idx !== -1) ? idx : 0;
    } else if (typeof q.correctAnswer === 'boolean') {
      norm.correctAnswer = q.correctAnswer;
    }

    return norm;
  }

  // --- QUIZ ARENA STATE & CONTROLLER ---
  let activeQuizQuestions = [];
  let currentQuestionIndex = 0;
  let currentScore = 0;
  let currentMode = 'mod1';
  let currentLessonFilter = '';
  let isAnswerSubmitted = false;
  let userSelectedAnswer = null;
  let userOrderState = [];

  function getQuestionsForMode(mode, lessonFilter) {
    // 1. LESSON PRACTICE FILTER (Mariam practices all 20 questions for any individual lesson)
    if (lessonFilter) {
      // First check authentic embedded lesson questions
      if (AUTHENTIC_LESSON_PRACTICE && AUTHENTIC_LESSON_PRACTICE[lessonFilter] && AUTHENTIC_LESSON_PRACTICE[lessonFilter].length > 0) {
        return AUTHENTIC_LESSON_PRACTICE[lessonFilter].map(normalizeQuestion);
      }

      // Check window.LESSONS_CONTENT
      if (typeof window !== 'undefined' && window.LESSONS_CONTENT && window.LESSONS_CONTENT.lessons) {
        const lObj = window.LESSONS_CONTENT.lessons[lessonFilter] || window.LESSONS_CONTENT['lesson-' + lessonFilter];
        if (lObj) {
          const pq = lObj.practiceQuestions || (lObj.practice && lObj.practice.mcqs);
          if (Array.isArray(pq) && pq.length > 0) {
            return pq.map(normalizeQuestion);
          }
        }
      }

      // Check window.CURRICULUM_DATA.quizBank
      if (typeof window !== 'undefined' && window.CURRICULUM_DATA && Array.isArray(window.CURRICULUM_DATA.quizBank)) {
        const fromCurriculum = window.CURRICULUM_DATA.quizBank.filter(function (q) {
          const l = q.lesson || (q.lessonId ? q.lessonId.replace('lesson-', '') : '');
          return l === lessonFilter;
        });
        if (fromCurriculum.length > 0) return fromCurriculum.map(normalizeQuestion);
      }

      // Fallback
      const fromBuiltin = BUILTIN_QUIZ_BANK.filter(function (q) { return q.lesson === lessonFilter; });
      if (fromBuiltin.length > 0) return fromBuiltin.map(normalizeQuestion);
    }

    // 2. MODULE 1 FINAL TEST (Loads the authentic 25 questions)
    if (mode === 'mod1' || mode === 'mod1_final' || mode === 'module1_final' || mode === 'module1' || mode === 'mod1_test' || mode === 'mod1-test') {
      if (typeof window !== 'undefined' && window.CURRICULUM_DATA) {
        if (Array.isArray(window.CURRICULUM_DATA.module1FinalTest) && window.CURRICULUM_DATA.module1FinalTest.length === 25) {
          return window.CURRICULUM_DATA.module1FinalTest.map(normalizeQuestion);
        }
        if (Array.isArray(window.CURRICULUM_DATA.quizBank)) {
          const fromBank = window.CURRICULUM_DATA.quizBank.filter(function (q) {
            return (q.id && String(q.id).startsWith('mod1-test')) || q.isModule1FinalTest;
          });
          if (fromBank.length === 25) {
            return fromBank.map(normalizeQuestion);
          }
        }
      }
      if (typeof window !== 'undefined' && Array.isArray(window.MODULE_1_FINAL_TEST_QUESTIONS) && window.MODULE_1_FINAL_TEST_QUESTIONS.length === 25) {
        return window.MODULE_1_FINAL_TEST_QUESTIONS.map(normalizeQuestion);
      }
      // Return authentic 25 questions
      return AUTHENTIC_MODULE1_FINAL_TEST.map(normalizeQuestion);
    }

    // 3. MODULE 2 PRACTICE (10 Questions on Dilations & Similarity)
    if (mode === 'mod2' || mode === 'module2') {
      let pool = [];
      if (typeof window !== 'undefined' && window.CURRICULUM_DATA && Array.isArray(window.CURRICULUM_DATA.quizBank)) {
        pool = window.CURRICULUM_DATA.quizBank.filter(function (q) { return q.module === 2; }).map(normalizeQuestion);
      }
      if (pool.length === 0) {
        pool = BUILTIN_MODULE2_BANK.map(normalizeQuestion);
      }
      return shuffle(pool).slice(0, 10);
    }

    // 4. GRAND MASTERY (15 Questions mixed across Module 1 and Module 2)
    if (mode === 'grand_mastery' || mode === 'grand') {
      let pool = AUTHENTIC_MODULE1_FINAL_TEST.map(normalizeQuestion);
      let m2Pool = BUILTIN_MODULE2_BANK.map(normalizeQuestion);
      if (typeof window !== 'undefined' && window.CURRICULUM_DATA && Array.isArray(window.CURRICULUM_DATA.quizBank)) {
        const m2FromBank = window.CURRICULUM_DATA.quizBank.filter(function (q) { return q.module === 2; }).map(normalizeQuestion);
        if (m2FromBank.length > 0) m2Pool = m2FromBank;
      }
      pool = pool.concat(m2Pool);
      return shuffle(pool).slice(0, 15);
    }

    return shuffle(AUTHENTIC_MODULE1_FINAL_TEST.map(normalizeQuestion)).slice(0, 10);
  }

  function shuffle(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      const tmp = a[i];
      a[i] = a[j];
      a[j] = tmp;
    }
    return a;
  }

  // --- KATEX MATH RENDERING HELPER ---
  function triggerKaTeX(elem) {
    if (typeof window === 'undefined') return;
    const target = elem || document.getElementById('quiz-arena-container') || document.body;
    if (!target) return;
    if (typeof window.renderMathInElement === 'function') {
      try {
        window.renderMathInElement(target, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '\\[', right: '\\]', display: true },
            { left: '\\(', right: '\\)', display: false },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false
        });
      } catch (e) {
        // KaTeX parsing warning
      }
    }
  }

  // --- CELEBRATORY CONFETTI ENGINE ---
  function triggerConfetti() {
    if (typeof window !== 'undefined' && typeof window.confetti === 'function') {
      try {
        window.confetti({
          particleCount: 100,
          spread: 70,
          origin: { y: 0.6 }
        });
        setTimeout(function () {
          window.confetti({
            particleCount: 60,
            angle: 60,
            spread: 55,
            origin: { x: 0 }
          });
          window.confetti({
            particleCount: 60,
            angle: 120,
            spread: 55,
            origin: { x: 1 }
          });
        }, 300);
      } catch (e) {
        console.warn('Canvas confetti error:', e);
      }
    }
    // Floating DOM celebratory burst
    fallbackDomConfetti();
  }

  function fallbackDomConfetti() {
    if (typeof document === 'undefined') return;
    const container = document.body;
    if (!container) return;
    const emojis = ['🎉', '⭐', '🌟', '✨', '🎈', '🏆', '💎'];
    for (let i = 0; i < 25; i++) {
      const el = document.createElement('div');
      el.className = 'dom-confetti-particle';
      el.textContent = emojis[Math.floor(Math.random() * emojis.length)];
      el.style.position = 'fixed';
      el.style.left = (Math.random() * 90 + 5) + 'vw';
      el.style.top = '-40px';
      el.style.fontSize = (Math.random() * 20 + 20) + 'px';
      el.style.zIndex = '99999';
      el.style.pointerEvents = 'none';
      el.style.transition = 'all ' + (Math.random() * 1.5 + 1.2) + 's ease-out';
      container.appendChild(el);
      setTimeout(function () {
        el.style.top = (window.innerHeight + 40) + 'px';
        el.style.transform = 'rotate(' + (Math.random() * 720 - 360) + 'deg)';
        el.style.opacity = '0';
      }, 20);
      setTimeout(function () {
        if (el.parentNode) el.parentNode.removeChild(el);
      }, 3000);
    }
  }

  let isQuizCompleted = false;

  // --- RENDERING FUNCTIONS ---
  function renderArena() {
    if (!activeQuizQuestions || activeQuizQuestions.length === 0) {
      if (typeof document !== 'undefined') {
        const container = document.getElementById('quiz-arena-container') || document.querySelector('.quiz-container');
        if (container) renderQuizMenu(container);
      }
      return;
    }

    if (currentQuestionIndex >= activeQuizQuestions.length) {
      if (!isQuizCompleted) {
        isQuizCompleted = true;
        const totalQ = activeQuizQuestions.length;
        const scorePct = totalQ > 0 ? Math.round((currentScore / totalQ) * 100) : 0;
        ProfileManager.recordQuizCompletion(totalQ, scorePct, currentMode);
        if (scorePct >= 80) {
          AudioEngine.playVictory();
          triggerConfetti();
        } else if (scorePct >= 70) {
          AudioEngine.playVictory();
        } else {
          AudioEngine.playClick();
        }
      }
      if (typeof document !== 'undefined') {
        const container = document.getElementById('quiz-arena-container') || document.querySelector('.quiz-container');
        if (container) renderQuizSummary(container);
      }
      return;
    }

    if (typeof document !== 'undefined') {
      const container = document.getElementById('quiz-arena-container') || document.querySelector('.quiz-container');
      if (container) renderCurrentQuestion(container);
    }
  }

  function renderQuizMenu(container) {
    const p = ProfileManager.get();
    container.innerHTML = `
      <div class="card" style="text-align: center; padding: 40px 24px;">
        <div style="font-size: 3rem; margin-bottom: 12px;">⚔️</div>
        <h2 style="font-size: 1.7rem; font-weight: 800; margin-bottom: 8px; background: linear-gradient(135deg, #4f46e5, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          Mariam's Math Quiz Arena
        </h2>
        <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto 28px; font-size: 0.95rem; line-height: 1.5;">
          Test your mastery of Grade 8 Into Math Transformations, Congruence & Similarity! Earn <strong>+50 XP per correct question</strong>, build winning streaks, and unlock champion badges!
        </p>

        <div style="display: flex; justify-content: center; gap: 16px; margin-bottom: 30px; flex-wrap: wrap;">
          <div class="stat-pill xp" style="font-size: 0.95rem; padding: 6px 16px;">
            <span>⭐</span>
            <span>${p.xp} Total XP</span>
          </div>
          <div class="stat-pill streak" style="font-size: 0.95rem; padding: 6px 16px;">
            <span>🔥</span>
            <span>${p.streak} Streak (Best: ${p.maxStreak})</span>
          </div>
          <button id="quiz-sound-toggle" class="btn btn-secondary btn-sm" style="display: inline-flex; align-items: center; gap: 6px;">
            <span>${AudioEngine.getMuted() ? '🔇 Unmute Sound' : '🔊 Sound On'}</span>
          </button>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; max-width: 860px; margin: 0 auto 30px; text-align: left;">
          <div class="card" style="border: 2px solid #e0e7ff; background: #fafbff; cursor: pointer; transition: transform 0.2s;" onclick="window.QuizArena.startQuiz('mod1')">
            <div style="font-size: 1.8rem; margin-bottom: 8px;">📘</div>
            <h3 style="font-size: 1.15rem; font-weight: 800; color: #3730a3; margin-bottom: 6px;">Module 1 Final Test (25 Questions)</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 14px;">Authentic HMH Into Math test with 25 comprehensive questions (5 per lesson) covering all Module 1 standards.</p>
            <span class="btn btn-primary btn-sm" style="width: 100%;">Start Final Test (25 Qs)</span>
          </div>

          <div class="card" style="border: 2px solid #ccfbf1; background: #f0fdfa; cursor: pointer; transition: transform 0.2s;" onclick="window.QuizArena.startQuiz('mod2')">
            <div style="font-size: 1.8rem; margin-bottom: 8px;">📐</div>
            <h3 style="font-size: 1.15rem; font-weight: 800; color: #0f766e; margin-bottom: 6px;">Module 2 Practice</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 14px;">10 Questions on Dilations, Reductions, Scale Factors & Similarity.</p>
            <span class="btn btn-primary btn-sm" style="width: 100%; background: linear-gradient(135deg, #0d9488, #059669);">Start Module 2 (10 Qs)</span>
          </div>

          <div class="card" style="border: 2px solid #fce7f3; background: #fff5f9; cursor: pointer; transition: transform 0.2s;" onclick="window.QuizArena.startQuiz('grand_mastery')">
            <div style="font-size: 1.8rem; margin-bottom: 8px;">👑</div>
            <h3 style="font-size: 1.15rem; font-weight: 800; color: #9d174d; margin-bottom: 6px;">Grand Mastery</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 14px;">15 Mixed Questions across Modules 1 & 2 for ultimate badge mastery!</p>
            <span class="btn btn-accent btn-sm" style="width: 100%;">Start Challenge (15 Qs)</span>
          </div>
        </div>

        <div style="display: flex; justify-content: center; align-items: center; gap: 12px; margin-top: 10px; flex-wrap: wrap;">
          <label style="font-size: 0.9rem; font-weight: 700; color: var(--text-muted);">Practice by Lesson (20 Questions each):</label>
          <select id="quiz-lesson-filter" class="select-input" style="padding: 7px 14px; font-weight: 600;">
            <option value="">-- Choose a Lesson to Practice --</option>
            <option value="1.1">Lesson 1.1: Investigate Transformations (20 Qs)</option>
            <option value="1.2">Lesson 1.2: Explore Translations (20 Qs)</option>
            <option value="1.3">Lesson 1.3: Explore Reflections (20 Qs)</option>
            <option value="1.4">Lesson 1.4: Explore Rotations (20 Qs)</option>
            <option value="1.5">Lesson 1.5: Congruent Figures (20 Qs)</option>
            <option value="2.1">Lesson 2.1: Dilations</option>
            <option value="2.2">Lesson 2.2: Reductions & Enlargements</option>
            <option value="2.3">Lesson 2.3: Similar Figures</option>
          </select>
          <button id="btnStartLessonPractice" class="btn btn-secondary btn-sm" onclick="const sel = document.getElementById('quiz-lesson-filter'); if (sel && sel.value) window.QuizArena.startQuiz('practice', sel.value);">Start Practice ➔</button>
        </div>
      </div>
    `;

    const soundBtn = document.getElementById('quiz-sound-toggle');
    if (soundBtn) {
      soundBtn.onclick = function () {
        const muted = AudioEngine.toggleMute();
        soundBtn.innerHTML = `<span>${muted ? '🔇 Unmute Sound' : '🔊 Sound On'}</span>`;
        if (!muted) AudioEngine.playClick();
      };
    }
  }

  function renderCurrentQuestion(container) {
    const q = activeQuizQuestions[currentQuestionIndex];
    const totalQ = activeQuizQuestions.length;
    const progressPercent = Math.round((currentQuestionIndex / totalQ) * 100);
    isAnswerSubmitted = false;
    userSelectedAnswer = null;

    let modeName = 'Quiz Arena';
    if (currentMode === 'mod1' || currentMode === 'mod1_final' || currentMode === 'module1_final') {
      modeName = 'Module 1 Final Test';
    } else if (currentMode === 'mod2' || currentMode === 'module2') {
      modeName = 'Module 2 Practice';
    } else if (currentMode === 'grand_mastery' || currentMode === 'grand') {
      modeName = 'Grand Mastery Challenge';
    } else if (currentMode === 'practice') {
      modeName = 'Lesson ' + (currentLessonFilter || q.lesson || '') + ' Practice';
    }

    let visualBadge = `<span class="question-badge">${modeName} • Lesson ${q.lesson || 'Review'} • ${q.topic || 'Grade 8 Math'}</span>`;

    let hintHtml = '';
    if (q.hint) {
      hintHtml = '<button id="btn-show-hint" class="btn btn-secondary btn-sm" onclick="window.QuizArena.toggleHint()">💡 Show Hint</button>';
    }

    container.innerHTML = `
      <div class="quiz-progress-bar">
        <div class="quiz-progress-fill" style="width: ${progressPercent}%;"></div>
      </div>

      <div class="question-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <div>${visualBadge}</div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 0.85rem; font-weight: 700; color: var(--text-muted);">Question ${currentQuestionIndex + 1} of ${totalQ}</span>
            <button id="btn-sound-quiz" class="icon-btn" title="Toggle Sound" style="width: 30px; height: 30px; font-size: 0.8rem;">
              ${AudioEngine.getMuted() ? '🔇' : '🔊'}
            </button>
          </div>
        </div>

        <div class="question-text" id="quiz-question-text">${escapeHtml(q.question)}</div>

        <div id="quiz-question-body">
          ${renderQuestionBody(q)}
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 24px; flex-wrap: wrap; gap: 12px;">
          <div>
            ${hintHtml}
          </div>
          <div style="display: flex; gap: 10px;">
            <button id="btn-submit-answer" class="btn btn-primary" onclick="window.QuizArena.handleAnswerSubmit()">
              Submit Answer
            </button>
            <button id="btn-next-question" class="btn btn-secondary" style="display: none;" onclick="window.QuizArena.nextQuestion()">
              Next Question ➔
            </button>
          </div>
        </div>

        <div id="quiz-hint-box" style="display: none; background: #fffbeb; border: 1px dashed #f59e0b; border-radius: var(--radius-sm); padding: 14px; margin-top: 16px; font-size: 0.875rem; color: #92400e;">
          <strong>💡 Hint:</strong> ${escapeHtml(q.hint || '')}
        </div>

        <div id="quiz-explanation-box" style="display: none;"></div>
      </div>
    `;

    const soundBtn = document.getElementById('btn-sound-quiz');
    if (soundBtn) {
      soundBtn.onclick = function () {
        const muted = AudioEngine.toggleMute();
        soundBtn.textContent = muted ? '🔇' : '🔊';
        if (!muted) AudioEngine.playClick();
      };
    }

    if (q.type === 'sequence_builder') {
      initSequenceBuilder(q);
    }

    // Trigger KaTeX math rendering on question text and options
    triggerKaTeX(container);
  }

  function renderQuestionBody(q) {
    if (q.type === 'multiple_choice') {
      const letters = ['A', 'B', 'C', 'D', 'E'];
      return `
        <div class="options-grid">
          ${q.options.map(function (opt, idx) {
            return `
              <button class="option-btn" data-index="${idx}" onclick="window.QuizArena.selectOption(${idx})">
                <span class="option-letter">${letters[idx] || (idx + 1)}</span>
                <span class="option-text">${escapeHtml(opt)}</span>
              </button>
            `;
          }).join('')}
        </div>
      `;
    }

    if (q.type === 'coordinate_input') {
      return `
        <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 24px; margin-bottom: 20px;">
          <p style="font-weight: 600; font-size: 0.9rem; color: var(--text-muted); margin-bottom: 14px;">
            Enter the coordinate pair (x, y):
          </p>
          <div style="display: flex; align-items: center; gap: 12px; font-size: 1.5rem; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: var(--primary-dark);">
            <span>(</span>
            <div style="display: flex; flex-direction: column; gap: 4px;">
              <input type="number" id="coord-input-x" class="text-input" placeholder="x" style="width: 100px; font-size: 1.2rem; text-align: center;" step="any" />
              <span style="font-size: 0.7rem; color: var(--text-muted); font-family: sans-serif; text-align: center;">x-coordinate</span>
            </div>
            <span>,</span>
            <div style="display: flex; flex-direction: column; gap: 4px;">
              <input type="number" id="coord-input-y" class="text-input" placeholder="y" style="width: 100px; font-size: 1.2rem; text-align: center;" step="any" />
              <span style="font-size: 0.7rem; color: var(--text-muted); font-family: sans-serif; text-align: center;">y-coordinate</span>
            </div>
            <span>)</span>
          </div>
        </div>
      `;
    }

    if (q.type === 'true_false') {
      return `
        <div class="options-grid" style="grid-template-columns: 1fr 1fr;">
          <button class="option-btn" data-value="true" onclick="window.QuizArena.selectOption(true)">
            <span class="option-letter" style="background: #dcfce7; color: #166534;">✓</span>
            <span class="option-text" style="font-weight: 700; font-size: 1.1rem;">TRUE</span>
          </button>
          <button class="option-btn" data-value="false" onclick="window.QuizArena.selectOption(false)">
            <span class="option-letter" style="background: #fee2e2; color: #991b1b;">✕</span>
            <span class="option-text" style="font-weight: 700; font-size: 1.1rem;">FALSE</span>
          </button>
        </div>
      `;
    }

    if (q.type === 'sequence_builder') {
      userOrderState = (q.steps || []).map(function (_, i) { return i; });
      return `
        <div style="margin-bottom: 20px;">
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 12px; font-weight: 600;">
            Use the Move Up (▲) / Move Down (▼) buttons to arrange the steps in the correct chronological order:
          </p>
          <div id="sequence-steps-list" style="display: flex; flex-direction: column; gap: 10px;">
            ${renderSequenceItems(q, userOrderState)}
          </div>
        </div>
      `;
    }

    return `<p>Unsupported question format</p>`;
  }

  function renderSequenceItems(q, order) {
    return order.map(function (origIndex, pos) {
      const stepText = q.steps[origIndex];
      return `
        <div class="card" style="padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px; border: 1px solid var(--border);" data-pos="${pos}">
          <div style="display: flex; align-items: center; gap: 12px;">
            <span style="width: 28px; height: 28px; border-radius: 50%; background: var(--primary-light); color: var(--primary-dark); font-weight: 800; display: flex; align-items: center; justify-content: center; font-size: 0.85rem;">
              ${pos + 1}
            </span>
            <span style="font-size: 0.925rem; font-weight: 600;">${escapeHtml(stepText)}</span>
          </div>
          <div style="display: flex; gap: 6px;">
            <button class="icon-btn" style="width: 32px; height: 32px;" onclick="window.QuizArena.moveSequenceStep(${pos}, -1)" ${pos === 0 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''}>▲</button>
            <button class="icon-btn" style="width: 32px; height: 32px;" onclick="window.QuizArena.moveSequenceStep(${pos}, 1)" ${pos === order.length - 1 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''}>▼</button>
          </div>
        </div>
      `;
    }).join('');
  }

  function initSequenceBuilder(q) {
    // Ready
  }

  function moveSequenceStep(pos, dir) {
    AudioEngine.playClick();
    const newPos = pos + dir;
    if (newPos < 0 || newPos >= userOrderState.length) return;
    const item = userOrderState.splice(pos, 1)[0];
    userOrderState.splice(newPos, 0, item);

    const q = activeQuizQuestions[currentQuestionIndex];
    const listEl = document.getElementById('sequence-steps-list');
    if (listEl) {
      listEl.innerHTML = renderSequenceItems(q, userOrderState);
    }
  }

  function selectOption(val) {
    if (isAnswerSubmitted) return;
    AudioEngine.playClick();
    userSelectedAnswer = val;

    if (typeof document !== 'undefined') {
      const btns = document.querySelectorAll('.option-btn');
      btns.forEach(function (btn) {
        btn.classList.remove('selected');
        const idx = btn.getAttribute('data-index');
        const dataVal = btn.getAttribute('data-value');
        if (idx !== null && parseInt(idx, 10) === val) {
          btn.classList.add('selected');
        }
        if (dataVal !== null && (dataVal === 'true') === val) {
          btn.classList.add('selected');
        }
      });
    }
  }

  function toggleHint() {
    AudioEngine.playClick();
    if (typeof document === 'undefined') return;
    const hintBox = document.getElementById('quiz-hint-box');
    if (hintBox) {
      hintBox.style.display = (hintBox.style.display === 'none') ? 'block' : 'none';
      if (hintBox.style.display === 'block') {
        triggerKaTeX(hintBox);
      }
    }
  }

  function handleAnswerSubmit() {
    if (isAnswerSubmitted) return;
    const q = activeQuizQuestions[currentQuestionIndex];
    let answer = null;

    if (q.type === 'multiple_choice') {
      if (userSelectedAnswer === null) {
        showToast('⚠️ Please select an option first!');
        return;
      }
      answer = userSelectedAnswer;
    } else if (q.type === 'coordinate_input') {
      if (typeof document === 'undefined') return;
      const xVal = document.getElementById('coord-input-x').value;
      const yVal = document.getElementById('coord-input-y').value;
      if (xVal === '' || yVal === '') {
        showToast('⚠️ Please enter both x and y coordinates!');
        return;
      }
      answer = { x: parseFloat(xVal), y: parseFloat(yVal) };
    } else if (q.type === 'true_false') {
      if (userSelectedAnswer === null) {
        showToast('⚠️ Please select True or False!');
        return;
      }
      answer = userSelectedAnswer;
    } else if (q.type === 'sequence_builder') {
      answer = userOrderState.slice();
    }

    submitAnswer(answer);
  }

  function submitAnswer(answer) {
    if (isAnswerSubmitted) return;
    isAnswerSubmitted = true;
    const q = activeQuizQuestions[currentQuestionIndex];
    let isCorrect = false;

    if (q.type === 'multiple_choice') {
      let targetIdx = q.correctAnswer;
      if (typeof targetIdx === 'string') {
        const found = q.options.findIndex(function (opt) {
          return opt.trim() === targetIdx.trim() || opt.startsWith(targetIdx);
        });
        if (found !== -1) targetIdx = found;
      }
      isCorrect = (answer === targetIdx);

      if (typeof document !== 'undefined') {
        const btns = document.querySelectorAll('.option-btn');
        btns.forEach(function (btn) {
          const idx = parseInt(btn.getAttribute('data-index'), 10);
          if (idx === targetIdx) {
            btn.classList.add('correct');
          } else if (idx === answer) {
            btn.classList.add('incorrect');
          }
        });
      }
    } else if (q.type === 'coordinate_input') {
      const eps = 0.01;
      isCorrect = Math.abs(answer.x - q.expectedCoords.x) < eps && Math.abs(answer.y - q.expectedCoords.y) < eps;
      if (typeof document !== 'undefined') {
        const xInput = document.getElementById('coord-input-x');
        const yInput = document.getElementById('coord-input-y');
        if (xInput && yInput) {
          xInput.disabled = true;
          yInput.disabled = true;
          if (isCorrect) {
            xInput.style.borderColor = '#10b981';
            yInput.style.borderColor = '#10b981';
          } else {
            xInput.style.borderColor = '#ef4444';
            yInput.style.borderColor = '#ef4444';
          }
        }
      }
    } else if (q.type === 'true_false') {
      isCorrect = (answer === q.correctAnswer);
      if (typeof document !== 'undefined') {
        const btns = document.querySelectorAll('.option-btn');
        btns.forEach(function (btn) {
          const val = btn.getAttribute('data-value') === 'true';
          if (val === q.correctAnswer) {
            btn.classList.add('correct');
          } else if (val === answer) {
            btn.classList.add('incorrect');
          }
        });
      }
    } else if (q.type === 'sequence_builder') {
      isCorrect = JSON.stringify(answer) === JSON.stringify(q.correctOrder);
    }

    // Audio & Gamification tracking (+50 XP per correct question)
    if (isCorrect) {
      AudioEngine.playCorrect();
      currentScore += 1;
      ProfileManager.recordAnswer(true, q.topic);
      showToast('🌟 Correct! +50 XP earned!');
    } else {
      AudioEngine.playWrong();
      ProfileManager.recordAnswer(false, q.topic);
      showToast('💭 Nice try! Check the explanation below.');
    }

    if (typeof window !== 'undefined' && typeof window.recordMcqResult === 'function') {
      window.recordMcqResult(isCorrect, q.lesson);
    }

    // Render mathematical explanation with KaTeX support
    if (typeof document !== 'undefined') {
      const expBox = document.getElementById('quiz-explanation-box');
      if (expBox) {
        expBox.style.display = 'block';
        expBox.className = 'explanation-card';
        expBox.innerHTML = `
          <div class="explanation-title" style="font-weight: 800; margin-bottom: 8px; font-size: 1rem; color: ${isCorrect ? '#065f46' : '#1e3a8a'};">
            <span>${isCorrect ? '✅ Excellent Work, Mariam!' : 'ℹ️ Step-by-Step Mathematical Explanation:'}</span>
          </div>
          <div style="font-size: 0.925rem; line-height: 1.55; color: var(--text-main); margin-bottom: 8px; white-space: pre-line;">
            ${escapeHtml(q.explanation || '')}
          </div>
          ${q.standard ? `<div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 6px;"><strong>Standard:</strong> ${escapeHtml(q.standard)}</div>` : ''}
          ${q.justification ? `<p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 6px;"><em>Justification:</em> ${escapeHtml(q.justification)}</p>` : ''}
        `;
        triggerKaTeX(expBox);
      }

      // Toggle button states
      const submitBtn = document.getElementById('btn-submit-answer');
      const nextBtn = document.getElementById('btn-next-question');
      if (submitBtn) submitBtn.style.display = 'none';
      if (nextBtn) {
        nextBtn.style.display = 'inline-flex';
        nextBtn.textContent = (currentQuestionIndex + 1 >= activeQuizQuestions.length) ? 'View Results 🏆' : 'Next Question ➔';
        nextBtn.focus();
      }
    }
  }

  function nextQuestion() {
    AudioEngine.playClick();
    currentQuestionIndex += 1;
    isAnswerSubmitted = false;
    userSelectedAnswer = null;
    renderArena();
  }

  function renderQuizSummary(container) {
    const totalQ = activeQuizQuestions.length;
    const scorePct = totalQ > 0 ? Math.round((currentScore / totalQ) * 100) : 0;

    let medalEmoji = '🥉';
    let feedbackMsg = 'Good effort! Practice makes perfect.';
    if (scorePct >= 90) {
      medalEmoji = '🥇';
      feedbackMsg = 'Magnificent! Mariam, you are a true Transformation & Similarity Master!';
    } else if (scorePct >= 80) {
      medalEmoji = '🥈';
      feedbackMsg = 'Awesome work! You demonstrated outstanding geometric mastery!';
    } else if (scorePct >= 70) {
      medalEmoji = '⭐';
      feedbackMsg = 'Great job passing! Review any tricky questions to achieve 100%!';
    }

    let modeTitle = 'Quiz Arena';
    if (currentMode === 'mod1' || currentMode === 'mod1_final' || currentMode === 'module1_final') {
      modeTitle = 'Module 1 Final Test';
    } else if (currentMode === 'mod2' || currentMode === 'module2') {
      modeTitle = 'Module 2 Practice';
    } else if (currentMode === 'grand_mastery' || currentMode === 'grand') {
      modeTitle = 'Grand Mastery Challenge';
    } else if (currentMode === 'practice') {
      modeTitle = 'Lesson ' + (currentLessonFilter || '') + ' Practice';
    }

    container.innerHTML = `
      <div class="card" style="text-align: center; padding: 40px 24px; max-width: 680px; margin: 0 auto;">
        <div style="font-size: 4rem; margin-bottom: 12px; animation: bounce 0.6s ease;">${medalEmoji}</div>
        <h2 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 6px;">${modeTitle} Completed!</h2>
        <p style="color: var(--text-muted); font-size: 1rem; margin-bottom: 24px;">${feedbackMsg}</p>

        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 30px; flex-wrap: wrap;">
          <div class="hero-stat-card" style="background: #f8fafc; border: 1px solid var(--border); min-width: 140px;">
            <div class="hero-stat-val" style="color: ${scorePct >= 80 ? '#10b981' : '#6366f1'};">${scorePct}%</div>
            <div class="hero-stat-lbl" style="color: var(--text-muted);">Final Score</div>
          </div>
          <div class="hero-stat-card" style="background: #f8fafc; border: 1px solid var(--border); min-width: 140px;">
            <div class="hero-stat-val" style="color: #d97706;">${currentScore} / ${totalQ}</div>
            <div class="hero-stat-lbl" style="color: var(--text-muted);">Correct Answers</div>
          </div>
          <div class="hero-stat-card" style="background: #f8fafc; border: 1px solid var(--border); min-width: 140px;">
            <div class="hero-stat-val" style="color: #ec4899;">+100 XP</div>
            <div class="hero-stat-lbl" style="color: var(--text-muted);">Completion Bonus</div>
          </div>
        </div>

        <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
          <button class="btn btn-primary" onclick="window.QuizArena.startQuiz('${currentMode}', '${currentLessonFilter || ''}')">
            🔄 Retake This Quiz
          </button>
          <button class="btn btn-secondary" onclick="window.QuizArena.resetToMenu()">
            📋 Choose Another Mode
          </button>
        </div>
      </div>
    `;
  }

  function escapeHtml(str) {
    if (typeof str !== 'string') return str;
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // --- PUBLIC API ---
  const API = {
    init: function () {
      ProfileManager.updateUIHeader();

      // Sync top navigation buttons if present in DOM
      if (typeof document !== 'undefined') {
        const btnMod1 = document.getElementById('quizModeMod1');
        if (btnMod1) btnMod1.textContent = '📘 Module 1 Final Test (25 Qs)';
        const btnMod2 = document.getElementById('quizModeMod2');
        if (btnMod2) btnMod2.textContent = '📐 Module 2 Practice (10 Qs)';
        const btnGrand = document.getElementById('quizModeGrand');
        if (btnGrand) btnGrand.textContent = '🌟 Grand Mastery (15 Qs)';
      }

      renderArena();
    },
    startQuiz: function (mode, lessonFilter) {
      AudioEngine.playClick();
      currentMode = mode || 'mod1';
      currentLessonFilter = lessonFilter || '';
      activeQuizQuestions = getQuestionsForMode(currentMode, currentLessonFilter);
      currentQuestionIndex = 0;
      currentScore = 0;
      isAnswerSubmitted = false;
      isQuizCompleted = false;
      userSelectedAnswer = null;
      renderArena();
    },
    resetToMenu: function () {
      AudioEngine.playClick();
      activeQuizQuestions = [];
      currentQuestionIndex = 0;
      currentScore = 0;
      currentLessonFilter = '';
      isAnswerSubmitted = false;
      isQuizCompleted = false;
      userSelectedAnswer = null;
      renderArena();
    },
    selectOption: selectOption,
    moveSequenceStep: moveSequenceStep,
    toggleHint: toggleHint,
    handleAnswerSubmit: handleAnswerSubmit,
    submitAnswer: submitAnswer,
    nextQuestion: nextQuestion,
    resetProgress: function () {
      ProfileManager.reset();
      this.init();
      showToast('Profile progress has been reset.');
    },
    getProfile: function () {
      return ProfileManager.get();
    },
    awardXP: function (amount) {
      return ProfileManager.awardXP(amount);
    },
    getAudioEngine: function () {
      return AudioEngine;
    },
    getQuestionsForMode: function (mode, lessonFilter) {
      return getQuestionsForMode(mode, lessonFilter);
    },
    getModule1FinalTest: function () {
      return AUTHENTIC_MODULE1_FINAL_TEST.slice();
    },
    getLessonPractice: function (lesson) {
      return (AUTHENTIC_LESSON_PRACTICE[lesson] || []).slice();
    },
    triggerConfetti: triggerConfetti
  };

  // Auto initialize on DOM ready in browser
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function () {
        API.init();
      });
    } else {
      API.init();
    }
  }

  return API;
});
