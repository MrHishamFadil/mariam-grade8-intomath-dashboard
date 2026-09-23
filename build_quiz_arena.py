import json
import os
import build_module1_final_test
import build_lesson_1_1
import build_lesson_1_2
import build_lesson_1_3
import build_lesson_1_4
import build_lesson_1_5

def get_mcqs(mod, attr):
    val = getattr(mod, attr)
    if isinstance(val, dict):
        return val.get('practice', {}).get('mcqs', val.get('mcqs', []))
    return val

def norm(q, default_lesson, default_topic):
    stem = q.get('q') or q.get('question')
    opts = q.get('opts') or q.get('options')
    corr = q.get('correct') if 'correct' in q else q.get('correctAnswer', 0)
    return {
        'id': q.get('id'),
        'module': 1,
        'lesson': q.get('lesson', default_lesson),
        'topic': default_topic,
        'standard': q.get('standard', ''),
        'dok': q.get('dok', 1),
        'type': 'multiple_choice',
        'question': stem,
        'options': opts,
        'correctAnswer': corr,
        'hint': q.get('hint', ''),
        'explanation': q.get('explanation', '')
    }

final_25 = [norm(q, q.get('lesson', '1.1'), 'Module 1 Final Review') for q in build_module1_final_test.MODULE_1_FINAL_TEST_QUESTIONS]
l1 = [norm(q, '1.1', 'Investigate Transformations') for q in get_mcqs(build_lesson_1_1, 'LESSON_1_1_DATA')]
l2 = [norm(q, '1.2', 'Explore Translations') for q in build_lesson_1_2.LESSON_1_2_MCQS]
l3 = [norm(q, '1.3', 'Explore Reflections') for q in build_lesson_1_3.LESSON_1_3_MCQS]
l4 = [norm(q, '1.4', 'Explore Rotations') for q in build_lesson_1_4.MCQS]
l5 = [norm(q, '1.5', 'Understand Congruent Figures') for q in get_mcqs(build_lesson_1_5, 'LESSON_1_5_DATA')]

m2_bank = [
    {
      'id': 'm2_q1',
      'module': 2,
      'lesson': '2.1',
      'topic': 'Dilations',
      'type': 'multiple_choice',
      'question': 'A dilation centered at the origin maps (4, -6) to (10, -15). What is the scale factor k?',
      'options': ['k = 2.5', 'k = 0.4', 'k = 1.5', 'k = 6'],
      'correctAnswer': 0,
      'hint': 'Calculate k = x\' / x or y\' / y: 10 / 4.',
      'explanation': 'k = 10 / 4 = 2.5. Checking y: -15 / -6 = 2.5. Since k > 1, this is an enlargement with scale factor 2.5.'
    },
    {
      'id': 'm2_q2',
      'module': 2,
      'lesson': '2.1',
      'topic': 'Dilations',
      'type': 'coordinate_input',
      'question': 'Point D(-9, 12) is dilated by a scale factor of k = 1/3 centered at the origin. What are the image coordinates?',
      'expectedCoords': {'x': -3, 'y': 4},
      'hint': 'Multiply both coordinates by the scale factor k = 1/3: (kx, ky).',
      'explanation': 'x\' = -9 * (1/3) = -3. y\' = 12 * (1/3) = 4. The image D\' is (-3, 4).'
    },
    {
      'id': 'm2_q3',
      'module': 2,
      'lesson': '2.2',
      'topic': 'Reductions & Enlargements',
      'type': 'true_false',
      'question': 'True or False: A dilation with a scale factor of k = 0.75 results in an enlargement of the original figure.',
      'correctAnswer': False,
      'justification': 'Since 0 < k < 1, the transformation is a reduction, making the image smaller than the preimage.',
      'hint': 'Enlargements require k > 1. What happens when 0 < k < 1?',
      'explanation': 'False! When the scale factor k satisfies 0 < k < 1, the figure shrinks, which is a reduction. Enlargements require k > 1.'
    },
    {
      'id': 'm2_q4',
      'module': 2,
      'lesson': '2.2',
      'topic': 'Reductions & Enlargements',
      'type': 'multiple_choice',
      'question': 'A photo measuring 4 inches by 6 inches is enlarged so that its longer side is 15 inches. What is the length of the shorter side?',
      'options': ['10 inches', '9 inches', '12 inches', '8 inches'],
      'correctAnswer': 0,
      'hint': 'Find the scale factor k from the longer side (15 / 6), then multiply by the shorter side (4).',
      'explanation': 'Scale factor k = 15 / 6 = 2.5. Shorter side = 4 * 2.5 = 10 inches.'
    },
    {
      'id': 'm2_q5',
      'module': 2,
      'lesson': '2.3',
      'topic': 'Similar Figures',
      'type': 'multiple_choice',
      'question': 'Two triangles are similar. Triangle 1 has side lengths 6, 8, 10. Triangle 2 has a shortest side of 15. What is the perimeter of Triangle 2?',
      'options': ['60', '48', '50', '72'],
      'correctAnswer': 0,
      'hint': 'Shortest side ratio k = 15 / 6 = 2.5. Perimeter of Triangle 1 = 6 + 8 + 10 = 24. Perimeter of Triangle 2 = 24 * k.',
      'explanation': 'Scale factor k = 15 / 6 = 2.5. Perimeter of original = 6 + 8 + 10 = 24. Perimeter of similar triangle = 24 * 2.5 = 60.'
    },
    {
      'id': 'm2_q6',
      'module': 2,
      'lesson': '2.1',
      'topic': 'Dilations',
      'type': 'multiple_choice',
      'question': 'Under any dilation centered at the origin, which property of geometric figures is ALWAYS preserved?',
      'options': ['Angle measures', 'Perimeter', 'Area', 'Distance between points'],
      'correctAnswer': 0,
      'hint': 'Dilations preserve the shape of figures, meaning angles stay exactly the same even though side lengths change.',
      'explanation': 'Dilations preserve angle measures and collinearity, but change distance, perimeter, and area by powers of the scale factor k.'
    },
    {
      'id': 'm2_q7',
      'module': 2,
      'lesson': '2.3',
      'topic': 'Similar Figures',
      'type': 'true_false',
      'question': 'True or False: All congruent figures are similar, but not all similar figures are congruent.',
      'correctAnswer': True,
      'justification': 'Congruent figures are similar figures with a scale factor of exactly k = 1.',
      'hint': 'Consider whether congruence is just a special case of similarity.',
      'explanation': 'True! Congruent figures have corresponding angles equal and side lengths in a 1:1 ratio (k = 1), so they are always similar. Similar figures with k ≠ 1 are not congruent.'
    },
    {
      'id': 'm2_q8',
      'module': 2,
      'lesson': '2.1',
      'topic': 'Dilations',
      'type': 'coordinate_input',
      'question': 'Preimage point H(5, -2) is dilated by k = 4 centered at the origin. Enter the coordinates of H\':',
      'expectedCoords': {'x': 20, 'y': -8},
      'hint': 'Multiply both x and y coordinates by 4: (5 * 4, -2 * 4).',
      'explanation': 'Rule (x, y) → (kx, ky) with k = 4: x\' = 5 * 4 = 20, y\' = -2 * 4 = -8. Result: (20, -8).'
    },
    {
      'id': 'm2_q9',
      'module': 2,
      'lesson': '2.2',
      'topic': 'Reductions & Enlargements',
      'type': 'multiple_choice',
      'question': 'If the scale factor of a dilation is k = 3, by what factor does the AREA of the polygon increase?',
      'options': ['9 times', '3 times', '6 times', '27 times'],
      'correctAnswer': 0,
      'hint': 'While lengths scale by k, area scales by k².',
      'explanation': 'Area scales as k². With k = 3, area is multiplied by 3² = 9.'
    },
    {
      'id': 'm2_q10',
      'module': 2,
      'lesson': '2.3',
      'topic': 'Similar Figures',
      'type': 'sequence_builder',
      'question': 'Order the steps to prove that Figure A is similar to Figure B on a coordinate plane:',
      'steps': [
        'Identify corresponding vertices and calculate the scale factor k between side lengths',
        'Apply a dilation by scale factor k centered at the origin',
        'Map the dilated figure onto Figure B using a sequence of rigid motions (translation/rotation/reflection)'
      ],
      'correctOrder': [0, 1, 2],
      'hint': 'First find the scale factor, dilate the shape, and then apply rigid transformations.',
      'explanation': 'To establish similarity: 1) determine scale factor k, 2) dilate to match size, 3) apply rigid motions to map the vertices onto each other.'
    }
]

lesson_practice = {
    '1.1': l1,
    '1.2': l2,
    '1.3': l3,
    '1.4': l4,
    '1.5': l5
}

js_template = r"""/**
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
  const AUTHENTIC_MODULE1_FINAL_TEST = __AUTHENTIC_MODULE1_FINAL_TEST__;

  // --- 2. AUTHENTIC LESSON PRACTICE (20 Questions per lesson from build_lesson_1_x.py) ---
  const AUTHENTIC_LESSON_PRACTICE = __AUTHENTIC_LESSON_PRACTICE__;

  // --- 3. BUILTIN MODULE 2 PRACTICE BANK ---
  const BUILTIN_MODULE2_BANK = __BUILTIN_MODULE2_BANK__;

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
    if (mode === 'mod1' || mode === 'mod1_final' || mode === 'module1_final' || mode === 'module1') {
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
          <button class="btn btn-secondary btn-sm" onclick="const sel = document.getElementById('quiz-lesson-filter'); if (sel && sel.value) window.QuizArena.startQuiz('practice', sel.value);">Start Practice ➔</button>
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
"""

full_code = js_template.replace(
    '__AUTHENTIC_MODULE1_FINAL_TEST__', json.dumps(final_25, indent=2)
).replace(
    '__AUTHENTIC_LESSON_PRACTICE__', json.dumps(lesson_practice, indent=2)
).replace(
    '__BUILTIN_MODULE2_BANK__', json.dumps(m2_bank, indent=2)
)

with open('quiz-arena.js', 'w', encoding='utf-8') as f:
    f.write(full_code)

print(f"quiz-arena.js successfully generated! Size: {os.path.getsize('quiz-arena.js')} bytes")
