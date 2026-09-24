# -*- coding: utf-8 -*-
import re
import json
from lessons_db import LESSONS
import build_lesson_1_1
import build_lesson_1_2
import build_lesson_1_3
import build_lesson_1_4
import build_lesson_1_5
import module2_mcqs
import build_module1_final_test

print("Generating upgraded index.html with all 20 MCQs per lesson and Module 1 Final Exam (25 Qs)...")

# Enrich each lesson with all 20 MCQs from our comprehensive question banks
lesson_mcq_sources = {
    "1.1": build_lesson_1_1.LESSON_1_1_DATA["mcqs"],
    "1.2": list(build_lesson_1_2.MCQS),
    "1.3": build_lesson_1_3.LESSON_1_3_DATA["mcqs"],
    "1.4": build_lesson_1_4.LESSON_1_4_DATA["mcqs"],
    "1.5": build_lesson_1_5.LESSON_1_5_DATA["mcqs"],
    "2.1": module2_mcqs.MODULE_2_MCQS["2.1"],
    "2.2": module2_mcqs.MODULE_2_MCQS["2.2"],
    "2.3": module2_mcqs.MODULE_2_MCQS["2.3"],
}

for les in LESSONS:
    lid = les["id"]
    if lid in lesson_mcq_sources:
        les["practice"]["mcqs"] = lesson_mcq_sources[lid]

MODULE_1_FINAL_TEST_QUESTIONS = build_module1_final_test.MODULE_1_FINAL_TEST_QUESTIONS
print(f"Loaded {len(LESSONS)} lessons (each with {len(LESSONS[0]['practice']['mcqs'])} MCQs).")
print(f"Loaded {len(MODULE_1_FINAL_TEST_QUESTIONS)} Module 1 Final Exam questions.")

# 1. Load old index.html to extract existing sandbox, quiz, study, badges sections
with open('index.html', 'r', encoding='utf-8') as f:
    old_html = f.read()

# Extract Sandbox section
sandbox_match = re.search(r'(<!-- =+\s*-->\s*<!-- TAB 1: INTERACTIVE SANDBOX\s*-->\s*<!-- =+\s*-->\s*<section id="tab-sandbox".*?</section>)', old_html, re.DOTALL)
if not sandbox_match:
    raise ValueError("Could not extract sandbox")
sandbox_html = sandbox_match.group(1).replace('class="tab-panel active"', 'class="tab-panel"')

# Extract Quiz section
quiz_match = re.search(r'(<!-- =+\s*-->\s*<!-- TAB 4: QUIZ & PRACTICE ARENA\s*-->\s*<!-- =+\s*-->\s*<section id="tab-quiz".*?</section>)', old_html, re.DOTALL)
if not quiz_match:
    raise ValueError("Could not extract quiz")
quiz_html = quiz_match.group(1)

# Enrich Quiz Section with Module 1 Final Exam button & callout card if not already added
if 'id="quizModeMod1Final"' not in quiz_html:
    quiz_html = re.sub(
        r'(<button class="quiz-mode-btn btn btn-secondary" data-quiz-mode="grand" id="quizModeGrand">[\s\S]*?</button>)',
        r'''\1
        <button class="quiz-mode-btn btn btn-secondary" data-quiz-mode="mod1_final" id="quizModeMod1Final" style="border: 2px solid #f59e0b; font-weight: 800; color: #b45309; background: #fffbeb;">
          🎓 Module 1 Final Exam (25 Qs)
        </button>''',
        quiz_html
    )

exam_callout_card_html = '''
      <!-- Module 1 Final Mastery Exam Hero Callout in Quiz Tab -->
      <div class="mod1-exam-callout-card" style="background: linear-gradient(135deg, #1e1b4b, #312e81 60%, #4338ca); color: white; border-radius: 16px; padding: 22px 26px; margin-bottom: 24px; box-shadow: 0 10px 25px -5px rgba(49, 46, 129, 0.4); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; border: 1.5px solid rgba(254, 240, 138, 0.4);">
        <div style="flex: 1; min-width: 280px;">
          <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(254, 240, 138, 0.2); color: #fef08a; padding: 4px 12px; border-radius: 999px; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 8px;">
            <span>👑 Module 1 Capstone Exam</span>
            <span>•</span>
            <span>25 Questions</span>
          </div>
          <h3 style="font-size: 1.35rem; font-weight: 800; margin: 0 0 6px 0; color: #ffffff;">Module 1 Final Quiz &amp; Mastery Exam</h3>
          <p style="font-size: 0.88rem; color: #c7d2fe; margin: 0; line-height: 1.5;">
            Mastered Lessons 1.1 through 1.5? Take this comprehensive 25-question test to evaluate your knowledge of rigid motions, coordinate mapping rules, and congruence proofs with full teacher model solutions!
          </p>
        </div>
        <div>
          <button class="btn btn-warning" id="btnLaunchMod1FinalQuiz" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: #ffffff; font-weight: 800; padding: 12px 22px; border-radius: 12px; border: none; cursor: pointer; box-shadow: 0 4px 14px rgba(217, 119, 6, 0.4); transition: transform 0.2s;" onclick="if(window.QuizArena && window.QuizArena.startQuiz) { window.QuizArena.startQuiz('mod1_final'); }">
            🚀 Launch 25-Question Test
          </button>
        </div>
      </div>
'''
if 'mod1-exam-callout-card' not in quiz_html:
    quiz_html = quiz_html.replace(
        '<div class="quiz-container" id="quiz-arena-container">',
        exam_callout_card_html + '\n      <div class="quiz-container" id="quiz-arena-container">'
    )

# Extract Study section
study_match = re.search(r'(<section id="tab-study".*?</section>)', old_html, re.DOTALL)
if not study_match:
    raise ValueError("Could not extract study")
study_html = study_match.group(1)

# Extract Badges section
badges_match = re.search(r'(<section id="tab-badges".*?</section>)', old_html, re.DOTALL)
if not badges_match:
    raise ValueError("Could not extract badges")
badges_html = badges_match.group(1)


# 2. Build the Quick Jump bar HTML
quick_jump_pills = []
for i, les in enumerate(LESSONS):
    active_cls = " active" if i == 0 else ""
    mod_tag = "Mod 1" if les["modNum"] == 1 else "Mod 2"
    pill = f'''
    <button class="lesson-jump-btn{active_cls}" data-lesson-id="{les['id']}">
      <span class="jump-pill-num">{les['num']}</span>
      <span class="jump-pill-title">{les['title']}</span>
      <span class="jump-pill-mod">{mod_tag}</span>
    </button>
    '''
    quick_jump_pills.append(pill)
    if les["id"] == "1.5":
        exam_jump_pill = '''
    <button class="lesson-jump-btn mod1-exam-jump-btn" data-lesson-id="mod1-exam" title="Module 1 Final Mastery Exam (25 Questions)">
      <span class="jump-pill-num" style="background: #fef3c7; color: #b45309;">1.Exam</span>
      <span class="jump-pill-title">Module 1 Mastery Exam</span>
      <span class="jump-pill-mod" style="background: #fef3c7; color: #b45309;">25 Qs 🏆</span>
    </button>
        '''
        quick_jump_pills.append(exam_jump_pill)
quick_jump_html = "\n".join(quick_jump_pills)


# 3. Build the 8 Lesson Panels + Dedicated Module 1 Final Exam Panel
lesson_panels_html = []
for i, les in enumerate(LESSONS):
    active_cls = " active" if i == 0 else ""
    prev_id = LESSONS[i - 1]["id"] if i > 0 else None
    next_id = LESSONS[i + 1]["id"] if i < len(LESSONS) - 1 else None
    les_slug = les['id'].replace('.', '-')

    # Vocabulary Cards
    vocab_cards_html = []
    for v in les["vocab"]:
        vocab_cards_html.append(f'''
        <div class="vocab-card">
          <div class="vocab-term">{v['term']}</div>
          <div class="vocab-def">{v['def']}</div>
          <div class="vocab-example"><strong>Example:</strong> {v['ex']}</div>
        </div>
        ''')
    vocab_html = "\n".join(vocab_cards_html)

    # Invariance Table Rows
    invar_rows_html = []
    for inv in les["invariance"]:
        cls_name = "status-check-yes" if inv["cls"] == "yes" else ("status-check-warn" if inv["cls"] == "warn" else "status-check-no")
        invar_rows_html.append(f'''
        <tr>
          <td><strong>{inv['prop']}</strong></td>
          <td class="{cls_name}">{inv['status']}</td>
        </tr>
        ''')
    invariance_table_html = "\n".join(invar_rows_html)

    # Core Rules Cards
    rules_html = []
    for r in les["rules"]:
        rules_html.append(f'''
        <div class="rule-box">
          <div class="rule-name">{r['name']}</div>
          <div class="rule-formula">\\[{r['formula']}\\]</div>
          <div class="rule-desc">{r['desc']}</div>
        </div>
        ''')
    rules_block_html = "\n".join(rules_html)

    # Illustrative Examples
    illus_examples_html = []
    for ex in les["illustrativeExamples"]:
        illus_examples_html.append(f'''
        <div class="illustrative-card">
          <div class="illustrative-header">
            <span class="illustrative-tag">Guided Demonstration</span>
            <h4 class="illustrative-title">{ex['title']}</h4>
          </div>
          <div class="illustrative-desc">{ex['desc']}</div>
          <div class="illustrative-analysis">
            <span class="analysis-label">💡 Step-by-Step Analysis:</span>
            <p>{ex['analysis']}</p>
          </div>
        </div>
        ''')
    illus_html = "\n".join(illus_examples_html)

    # Worked Example (Step 1, Step 2, Step 3 formatting)
    we = les["workedExample"]
    worked_example_html = f'''
    <div class="worked-example-card">
      <div class="worked-example-badge">✍️ Test-Ready Worked Example &amp; Model Answer</div>
      <h4 class="worked-example-problem-title">{we['title']}</h4>
      <div class="worked-problem-statement">
        <strong>Problem:</strong> {we['problem']}
      </div>

      <div class="solution-steps">
        <div class="solution-step">
          <div class="step-num">Step 1</div>
          <div class="step-body">{we['step1']}</div>
        </div>
        <div class="solution-step">
          <div class="step-num">Step 2</div>
          <div class="step-body">{we['step2']}</div>
        </div>
        <div class="solution-step">
          <div class="step-num">Step 3</div>
          <div class="step-body">{we['step3']}</div>
        </div>
      </div>

      <div class="model-student-box">
        <div class="model-box-header">
          <span>🏆 Perfect Exam Model Answer (Full Marks Response):</span>
        </div>
        <p class="model-box-text">{we['modelAnswer']}</p>
      </div>
    </div>
    '''

    # Section 4: Interactive Practice (ALL 20 MCQs)
    total_mcqs = len(les["practice"]["mcqs"])
    practice_items_html = []
    for q_idx, mcq in enumerate(les["practice"]["mcqs"], start=1):
        opts_html = []
        for opt_idx, opt_text in enumerate(mcq["opts"]):
            opts_html.append(f'''
            <button class="practice-opt-btn" type="button" data-opt-index="{opt_idx}">
              <span class="opt-letter">{chr(65 + opt_idx)}</span>
              <span class="opt-text">{opt_text}</span>
            </button>
            ''')
        opts_rendered = "\n".join(opts_html)
        dok_tag = mcq.get("dok", 2)
        std_tag = mcq.get("standard", les.get("standard", "CCSS.MATH.CONTENT.8.G.A"))

        practice_items_html.append(f'''
        <div class="practice-question-card" data-q-type="mcq" data-correct="{mcq['correct']}" data-q-id="{mcq['id']}" data-lesson="{les['id']}">
          <div class="practice-q-header-row">
            <div class="practice-q-badge">
              <span class="q-badge-num">Question {q_idx} of {total_mcqs}</span>
              <span class="q-badge-type">• Multiple Choice Challenge</span>
            </div>
            <div class="practice-q-meta-tags">
              <span class="q-tag-standard">{std_tag}</span>
              <span class="q-tag-dok">DOK {dok_tag}</span>
            </div>
          </div>
          <div class="practice-q-text">{mcq['q']}</div>
          <div class="practice-options-grid">
            {opts_rendered}
          </div>
          <div class="practice-action-row">
            <button class="btn btn-secondary btn-sm btn-hint-toggle" type="button">💡 Need a Hint?</button>
            <button class="btn btn-primary btn-sm btn-check-mcq" type="button">Check Answer</button>
          </div>
          <div class="hint-card" style="display: none;">
            <div class="hint-text">💡 <strong>Hint:</strong> {mcq['hint']}</div>
          </div>
          <div class="practice-feedback" style="display: none;"></div>
          <div class="practice-explanation-store" style="display: none;">
            <div class="teacher-explanation-card">
              <div class="teacher-explanation-header">
                <span>👩‍🏫 HMH Teacher Edition Step-by-Step Model Solution</span>
              </div>
              <div class="teacher-explanation-body">{mcq['explanation']}</div>
            </div>
          </div>
        </div>
        ''')
    practice_block_html = "\n".join(practice_items_html)

    # Section 5: HMH Book Questions Bank
    book_q_html = []
    for bq_idx, bq in enumerate(les["bookQuestions"]):
        book_q_html.append(f'''
        <div class="book-question-card">
          <div class="book-q-header">
            <span class="book-q-tag">📘 {bq['num']}</span>
          </div>
          <div class="book-q-text">{bq['q']}</div>
          <div class="book-q-actions">
            <button class="btn btn-secondary btn-sm btn-toggle-model-answer">
              👁️ Show Model Answer
            </button>
          </div>
          <div class="book-model-answer-card" style="display: none;">
            <div class="model-answer-banner">
              <span>👩‍🏫 HMH Teacher's Official Solution &amp; Rubric</span>
            </div>
            <div class="model-answer-content">{bq['modelAnswer']}</div>
          </div>
        </div>
        ''')
    book_block_html = "\n".join(book_q_html)

    # Navigation buttons
    if les["id"] == "1.5":
        prev_btn_html = '<button class="btn btn-secondary btn-nav-lesson" data-target-lesson="1.4">⬅ Previous (1.4)</button>'
        next_btn_html = '<button class="btn btn-warning btn-nav-lesson" data-target-lesson="mod1-exam" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; font-weight: 800;">Take Module 1 Exam (25 Qs) 🏆</button>'
    elif les["id"] == "2.1":
        prev_btn_html = '<button class="btn btn-secondary btn-nav-lesson" data-target-lesson="mod1-exam">⬅ Module 1 Exam</button>'
        next_btn_html = '<button class="btn btn-primary btn-nav-lesson" data-target-lesson="2.2">Next Lesson (2.2) ➡</button>'
    else:
        prev_btn_html = f'<button class="btn btn-secondary btn-nav-lesson" data-target-lesson="{prev_id}">⬅ Previous ({prev_id})</button>' if prev_id else '<button class="btn btn-secondary" disabled style="opacity: 0.4;">⬅ First Lesson</button>'
        next_btn_html = f'<button class="btn btn-primary btn-nav-lesson" data-target-lesson="{next_id}">Next Lesson ({next_id}) ➡</button>' if next_id else '<button class="btn btn-secondary" disabled style="opacity: 0.4;">End of Chapter 1 🎉</button>'

    panel_html = f'''
    <!-- LESSON {les['id']} PANEL -->
    <section id="lesson-view-{les['id'].replace('.', '-')}" class="lesson-view-panel{active_cls}" data-lesson-id="{les['id']}">
      
      <!-- Lesson Header Banner -->
      <div class="lesson-view-hero" style="background: linear-gradient(135deg, {les['themeColor']}, #6366f1 60%, #0ea5e9);">
        <div class="lesson-hero-meta">
          <span class="lesson-hero-badge">{les['badge']}</span>
          <span class="lesson-hero-standard">{les['standard']}</span>
        </div>
        <h2 class="lesson-hero-title">Lesson {les['num']}: {les['title']}</h2>
        <div class="lesson-hero-cando">
          <span class="cando-tag">🎯 I CAN:</span>
          <span class="cando-text">{les['canDo']}</span>
        </div>
        <div class="lesson-hero-actions">
          <button class="btn btn-light try-live-btn" data-lesson-target="{les['id']}">
            🚀 Launch Lesson {les['num']} in Interactive Coordinate Sandbox
          </button>
        </div>
      </div>

      <!-- 5-SECTION DEDICATED LAYOUT -->

      <!-- SECTION 1: CONCEPT & EXPLANATION -->
      <div class="lesson-section-container">
        <div class="section-title-bar">
          <div class="section-title-icon">📖</div>
          <div>
            <h3 class="section-title-text">Section 1: Concept &amp; Core Principles</h3>
            <p class="section-title-sub">Definitions, coordinate algebraic formulas, and geometric properties.</p>
          </div>
        </div>

        <div class="concept-explanation-card">
          <p class="concept-intro-paragraph">{les['conceptIntro']}</p>

          <div class="grid-2" style="margin-top: 20px;">
            <div>
              <h4 style="font-size: 0.95rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 10px;">
                📐 Mathematical Coordinate Rules:
              </h4>
              {rules_block_html}
            </div>
            <div>
              <h4 style="font-size: 0.95rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 10px;">
                ⚖️ Geometric Property Invariance:
              </h4>
              <table class="invariant-table">
                <thead>
                  <tr>
                    <th>Geometric Property</th>
                    <th>Preservation Status</th>
                  </tr>
                </thead>
                <tbody>
                  {invariance_table_html}
                </tbody>
              </table>
            </div>
          </div>

          <div style="margin-top: 24px;">
            <h4 style="font-size: 0.95rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 10px;">
              📚 Essential Vocabulary Cards:
            </h4>
            <div class="vocab-grid">
              {vocab_html}
            </div>
          </div>
        </div>
      </div>

      <!-- SECTION 2: ILLUSTRATIVE EXAMPLES -->
      <div class="lesson-section-container">
        <div class="section-title-bar">
          <div class="section-title-icon">💡</div>
          <div>
            <h3 class="section-title-text">Section 2: Illustrative Examples</h3>
            <p class="section-title-sub">Step-by-step demonstrations explaining key geometric concepts.</p>
          </div>
        </div>

        <div class="grid-2">
          {illus_html}
        </div>
      </div>

      <!-- SECTION 3: WORKED EXAMPLES & MODEL ANSWERS -->
      <div class="lesson-section-container">
        <div class="section-title-bar">
          <div class="section-title-icon">✍️</div>
          <div>
            <h3 class="section-title-text">Section 3: Worked Examples &amp; Model Answers</h3>
            <p class="section-title-sub">Step 1, Step 2, Step 3 formatting showing students how to write perfect exam responses.</p>
          </div>
        </div>

        {worked_example_html}
      </div>

      <!-- SECTION 4: INTERACTIVE PRACTICE ARENA (20 MCQS) -->
      <div class="lesson-section-container">
        <div class="section-title-bar">
          <div class="section-title-icon">🎯</div>
          <div style="flex: 1;">
            <h3 class="section-title-text">Section 4: Interactive Practice Arena ({total_mcqs} Questions)</h3>
            <p class="section-title-sub">Test your understanding with instant feedback, hints, celebratory rewards, and complete Teacher Edition model solutions.</p>
          </div>
        </div>

        <!-- Lesson 20-Q Mastery Progress Bar Card -->
        <div class="practice-mastery-progress-card" data-lesson-id="{les['id']}">
          <div class="practice-progress-header">
            <div class="practice-progress-title">
              <span class="practice-progress-icon">📊</span>
              <span>Lesson {les['num']} Mastery Progress</span>
            </div>
            <div class="practice-progress-stats">
              <span class="practice-score-badge">
                <span class="practice-solved-count" id="solved-count-{les_slug}">0</span> / {total_mcqs} Solved Correctly
              </span>
              <span class="practice-xp-pill">
                ⚡ <span class="practice-earned-xp" id="earned-xp-{les_slug}">0</span> / {total_mcqs * 10} XP
              </span>
            </div>
          </div>
          <div class="practice-progress-track">
            <div class="practice-progress-bar-fill" id="progress-fill-{les_slug}" style="width: 0%;"></div>
          </div>
          <div class="practice-progress-footer">
            <span class="practice-progress-status" id="progress-status-{les_slug}">Mariam, solve all {total_mcqs} questions to achieve 100% Mastery! 🌟</span>
            <span class="practice-score-pct" id="score-pct-{les_slug}" style="font-weight: 800; color: #2563eb;">0%</span>
          </div>
        </div>

        <div class="practice-grid">
          {practice_block_html}
        </div>
      </div>

      <!-- SECTION 5: HMH BOOK QUESTIONS BANK -->
      <div class="lesson-section-container">
        <div class="section-title-bar">
          <div class="section-title-icon">📘</div>
          <div>
            <h3 class="section-title-text">Section 5: HMH Book Questions Bank</h3>
            <p class="section-title-sub">Real Into Math Grade 8 textbook problems with teacher model answers hidden.</p>
          </div>
        </div>

        <div class="book-questions-grid">
          {book_block_html}
        </div>
      </div>

      <!-- Bottom Lesson Navigation Toolbar -->
      <div class="lesson-footer-nav">
        {prev_btn_html}
        <button class="btn btn-secondary try-live-btn" data-lesson-target="{les['id']}">
          🚀 Try Lesson {les['num']} in Sandbox
        </button>
        {next_btn_html}
      </div>

    </section>
    '''
    lesson_panels_html.append(panel_html)

    # Insert Dedicated Module 1 Final Exam Panel right after Lesson 1.5
    if les["id"] == "1.5":
        exam_q_items = []
        for eq_idx, eq in enumerate(MODULE_1_FINAL_TEST_QUESTIONS, start=1):
            eopts_html = []
            for eopt_idx, eopt_text in enumerate(eq["opts"]):
                eopts_html.append(f'''
                <button class="practice-opt-btn" type="button" data-opt-index="{eopt_idx}">
                  <span class="opt-letter">{chr(65 + eopt_idx)}</span>
                  <span class="opt-text">{eopt_text}</span>
                </button>
                ''')
            eopts_rendered = "\n".join(eopts_html)
            edok = eq.get("dok", 2)
            estd = eq.get("standard", "CCSS.MATH.CONTENT.8.G.A")

            exam_q_items.append(f'''
            <div class="practice-question-card" data-q-type="mcq" data-correct="{eq['correct']}" data-q-id="{eq['id']}" data-lesson="mod1-exam">
              <div class="practice-q-header-row">
                <div class="practice-q-badge" style="background: #fef3c7; color: #92400e;">
                  <span class="q-badge-num">Exam Question {eq_idx} of 25</span>
                  <span class="q-badge-type">• Lesson {eq.get('lesson', '1.1')} Focus</span>
                </div>
                <div class="practice-q-meta-tags">
                  <span class="q-tag-standard">{estd}</span>
                  <span class="q-tag-dok">DOK {edok}</span>
                </div>
              </div>
              <div class="practice-q-text">{eq['q']}</div>
              <div class="practice-options-grid">
                {eopts_rendered}
              </div>
              <div class="practice-action-row">
                <button class="btn btn-secondary btn-sm btn-hint-toggle" type="button">💡 Need a Hint?</button>
                <button class="btn btn-primary btn-sm btn-check-mcq" type="button">Check Answer</button>
              </div>
              <div class="hint-card" style="display: none;">
                <div class="hint-text">💡 <strong>Hint:</strong> {eq['hint']}</div>
              </div>
              <div class="practice-feedback" style="display: none;"></div>
              <div class="practice-explanation-store" style="display: none;">
                <div class="teacher-explanation-card">
                  <div class="teacher-explanation-header">
                    <span>👩‍🏫 HMH Teacher Edition Step-by-Step Model Solution</span>
                  </div>
                  <div class="teacher-explanation-body">{eq['explanation']}</div>
                </div>
              </div>
            </div>
            ''')
        exam_grid_html = "\n".join(exam_q_items)

        mod1_exam_panel_html = f'''
    <!-- ======================================================== -->
    <!-- DEDICATED MODULE 1 FINAL QUIZ & MASTERY EXAM (25 Qs)    -->
    <!-- ======================================================== -->
    <section id="lesson-view-mod1-exam" class="lesson-view-panel" data-lesson-id="mod1-exam">
      <div class="mod1-exam-hero-card">
        <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(254, 240, 138, 0.2); color: #fef08a; padding: 4px 14px; border-radius: 999px; font-size: 0.8rem; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 12px; border: 1px solid rgba(254, 240, 138, 0.3);">
          <span>🏆 Module 1 Capstone Assessment</span>
          <span>•</span>
          <span>25 Questions</span>
          <span>•</span>
          <span>HMH Into Math Grade 8</span>
        </div>
        <h2 style="font-size: 2.1rem; font-weight: 900; margin: 0 0 10px 0; color: #ffffff; letter-spacing: -0.02em;">
          Module 1 Final Quiz &amp; Mastery Exam
        </h2>
        <p style="font-size: 1.05rem; color: #c7d2fe; max-width: 820px; line-height: 1.6; margin: 0 0 20px 0;">
          Synthesized from HMH Into Math Module 1 Review, Form A, and Form B Tests. Evaluates complete mastery of Rigid Motions, Invariance Principles, Translations, Reflections, Rotations, and Congruence Proofs (CCSS 8.G.A.1, 8.G.A.2, 8.G.A.3).
        </p>
        <div style="display: flex; gap: 14px; flex-wrap: wrap; align-items: center;">
          <button class="btn btn-warning" id="btnLaunchMod1FinalFromLesson" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; font-weight: 800; font-size: 0.95rem; padding: 12px 24px; border-radius: 12px; border: none; cursor: pointer; box-shadow: 0 6px 18px rgba(217, 119, 6, 0.45); display: inline-flex; align-items: center; gap: 8px;" onclick="window.launchModule1ExamInArena()">
            <span>🚀 Launch in Timed Quiz Arena (with Sound &amp; XP)</span>
          </button>
          <span style="font-size: 0.875rem; color: #a5b4fc;">or practice all 25 questions below with instant teacher model solutions!</span>
        </div>
      </div>

      <!-- Exam Progress Bar Card -->
      <div class="practice-mastery-progress-card" data-lesson-id="mod1-exam" style="background: linear-gradient(135deg, #fffbeb, #fef3c7); border-color: #fde68a;">
        <div class="practice-progress-header">
          <div class="practice-progress-title" style="color: #92400e;">
            <span>🎓</span>
            <span>Module 1 Final Exam Mastery Progress</span>
          </div>
          <div class="practice-progress-stats">
            <span class="practice-score-badge" style="background: #fef08a; color: #854d0e; border-color: #fde047;">
              <span class="practice-solved-count" id="solved-count-mod1-exam">0</span> / 25 Solved Correctly
            </span>
            <span class="practice-xp-pill" style="background: #ffffff; color: #b45309; border-color: #fde68a;">
              ⚡ <span class="practice-earned-xp" id="earned-xp-mod1-exam">0</span> / 250 XP
            </span>
          </div>
        </div>
        <div class="practice-progress-track" style="background: #fef08a;">
          <div class="practice-progress-bar-fill" id="progress-fill-mod1-exam" style="width: 0%; background: linear-gradient(90deg, #f59e0b, #e11d48, #10b981);"></div>
        </div>
        <div class="practice-progress-footer">
          <span class="practice-progress-status" id="progress-status-mod1-exam" style="color: #92400e;">
            Mariam, solve all 25 capstone questions to claim the Module 1 Grand Champion Crown! 👑
          </span>
          <span class="practice-score-pct" id="score-pct-mod1-exam" style="font-weight: 800; color: #b45309;">0%</span>
        </div>
      </div>

      <!-- 25 Questions Grid -->
      <div class="practice-grid">
        {exam_grid_html}
      </div>

      <!-- Navigation -->
      <div class="lesson-footer-nav" style="margin-top: 30px;">
        <button class="btn btn-secondary btn-nav-lesson" data-target-lesson="1.5">⬅ Back to Lesson 1.5</button>
        <button class="btn btn-primary" onclick="window.launchModule1ExamInArena()">🚀 Launch in Quiz Arena</button>
        <button class="btn btn-secondary btn-nav-lesson" data-target-lesson="2.1">Forward to Module 2 (Lesson 2.1) ➡</button>
      </div>
    </section>
        '''
        lesson_panels_html.append(mod1_exam_panel_html)

all_lesson_panels_rendered = "\n".join(lesson_panels_html)


# 4. Build Complete Question Bank Tab
qbank_cards = []
for les in LESSONS:
    for bq in les["bookQuestions"]:
        qbank_cards.append(f'''
        <div class="book-question-card" data-mod="{les['modId']}">
          <div class="book-q-header">
            <span class="book-q-tag">Lesson {les['num']} • {bq['num']}</span>
            <span class="tag-mod-badge">{les['modTitle']}</span>
          </div>
          <div class="book-q-text">{bq['q']}</div>
          <div class="book-q-actions">
            <button class="btn btn-secondary btn-sm btn-toggle-model-answer">
              👁️ Show Model Answer
            </button>
          </div>
          <div class="book-model-answer-card" style="display: none;">
            <div class="model-answer-banner">
              <span>👩‍🏫 HMH Model Answer &amp; Explanation</span>
            </div>
            <div class="model-answer-content">{bq['modelAnswer']}</div>
          </div>
        </div>
        ''')
qbank_cards_html = "\n".join(qbank_cards)

qbank_tab_html = f'''
<!-- ======================================================== -->
<!-- TAB: COMPLETE QUESTION BANK                              -->
<!-- ======================================================== -->
<section id="tab-qbank" class="tab-panel" data-panel="qbank" role="tabpanel">
  <div class="hero-banner" style="background: linear-gradient(135deg, #4338ca, #7c3aed, #db2777);">
    <div class="hero-badge">📚 HMH Textbook Question Bank</div>
    <h2 class="hero-title">Chapter 1 Complete Question Bank</h2>
    <p class="hero-desc">
      Comprehensive collection of all HMH Into Math Grade 8 textbook problems across Modules 1 &amp; 2 with complete teacher solutions and hidden model answers.
    </p>
  </div>

  <div class="qbank-filter-bar">
    <button class="qbank-filter-btn active" data-filter="all">All Questions ({len(qbank_cards)})</button>
    <button class="qbank-filter-btn" data-filter="mod1">Module 1: Congruence (10 Qs)</button>
    <button class="qbank-filter-btn" data-filter="mod2">Module 2: Similarity (6 Qs)</button>
  </div>

  <div class="book-questions-grid" id="qbankGrid">
    {qbank_cards_html}
  </div>
</section>
'''


# JSON serialize the 25 exam questions for runtime Quiz Arena usage
exam_questions_json = json.dumps(MODULE_1_FINAL_TEST_QUESTIONS, ensure_ascii=False)

# 5. Assemble the Master index.html
final_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Into Math 8 • Chapter 1 Transformational Geometry | Mariam Hisham Mohamed AbdelFadil</title>
  
  <!-- Google Fonts: Plus Jakarta Sans, Outfit, Inter, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:ital,wght@0,400;0,600;0,700;0,800;1,500&family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,500;1,700&display=swap" rel="stylesheet">
  
  <!-- KaTeX for crisp mathematical formulas -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <!-- Canvas Confetti for celebrations -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <!-- Core Stylesheet -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- ======================================================== -->
  <!-- TOP APP HEADER & MARIAM'S WONDERFUL PROFILE SHOWCASE     -->
  <!-- ======================================================== -->
  <header class="app-header">
    <div class="header-container">
      
      <!-- Brand & Series -->
      <div class="brand-section">
        <div class="brand-logo" aria-label="Logo">📐</div>
        <div class="brand-info">
          <h1>Into Math 8 • Transformational Geometry</h1>
          <p>HMH Into Math Grade 8 • Advanced Mathematics Studio</p>
        </div>
      </div>

      <!-- Mariam's Wonderful Scholar Showcase Card -->
      <div class="scholar-showcase-card">
        
        <!-- Mariam's Photo Frame with Crown Badge & Upload Capability -->
        <div class="mariam-photo-frame" title="Mariam's Scholar Portrait">
          <div class="crown-badge" title="Champion Scholar">👑</div>
          <div class="photo-ring-glow"></div>
          <div class="photo-container">
            <img id="mariamPhotoImg" src="" alt="Mariam Hisham Mohamed AbdelFadil" style="display: none;">
            <div id="mariamAvatarPlaceholder" class="avatar-monogram">M</div>
            <label for="mariamPhotoInput" class="photo-upload-overlay" title="Click to upload Mariam's real photo!">
              <span class="cam-icon">📷</span>
            </label>
            <input type="file" id="mariamPhotoInput" accept="image/*" style="display: none;">
          </div>
          <div class="sparkle-badge" title="Math Star">✨</div>
        </div>

        <!-- Mariam's Scholar Info -->
        <div class="scholar-info">
          <div class="scholar-name-row">
            <h2 class="student-name">Mariam Hisham Mohamed AbdelFadil</h2>
            <button id="removePhotoBtn" class="btn-text-subtle" style="display: none;" title="Reset to default monogram">↺ Reset photo</button>
          </div>
          <div class="scholar-badges-row">
            <span class="badge-scholar">🌟 Grade 8 Math Star • Champion Scholar</span>
            <span class="badge-curriculum">📘 HMH Into Math Grade 8 Honors</span>
          </div>
        </div>

        <!-- Live Gamification Stats & Controls -->
        <div class="header-stats-group">
          <!-- XP Pill -->
          <div class="stat-pill xp" id="userXpPill" title="Mariam's Experience Points">
            <span>⚡</span> <span id="userXP">250 XP</span>
          </div>

          <!-- Streak Pill -->
          <div class="stat-pill streak" id="userStreakPill" title="Daily Math Learning Streak">
            <span>🔥</span> <span id="userStreak">3 Days</span>
          </div>

          <!-- Level Rank Pill -->
          <div class="stat-pill level" title="Mastery Rank">
            <span>🏆</span> <span id="userLevel">Level 1 • Math Virtuoso</span>
          </div>

          <!-- Audio FX Button -->
          <button id="soundToggleBtn" class="icon-btn" title="Toggle Sound FX" aria-label="Toggle Sound Effects">
            🔊
          </button>

          <!-- Quick Print Button -->
          <button id="headerPrintBtn" class="icon-btn" onclick="window.print()" title="Print Study Guide or Lesson" aria-label="Print Document">
            🖨️
          </button>
        </div>

      </div>

    </div>
  </header>

  <!-- ======================================================== -->
  <!-- CHAPTER 1 PROMINENT HERO HEADER                          -->
  <!-- ======================================================== -->
  <div class="chapter-hero-wrapper">
    <div class="chapter-hero-container">
      
      <!-- Breadcrumbs -->
      <nav class="chapter-breadcrumbs" aria-label="Breadcrumbs">
        <span>HMH Into Math 8</span>
        <span class="breadcrumb-separator">›</span>
        <span>Unit 1: Transformational Geometry</span>
        <span class="breadcrumb-separator">›</span>
        <span class="breadcrumb-active">Chapter 1: Rigid Motions, Dilations &amp; Similarity</span>
      </nav>

      <div class="chapter-hero-content">
        <div class="chapter-main-title">
          <span class="chapter-number-pill">Chapter 1 Focus</span>
          <h1 class="chapter-heading">Chapter 1: Transformational Geometry</h1>
          <p class="chapter-tagline">
            Mastering Rigid Motions (Translations, Reflections, Rotations), Congruence Proofs (\\(\\cong\\)), Dilations, Scale Factors (\\(k\\)), and Geometric Similarity (\\(\\sim\\)).
          </p>
        </div>

        <div class="chapter-stats-chips">
          <div class="chapter-chip">
            <span class="chip-icon">📘</span>
            <span class="chip-label"><strong>Module 1:</strong> Congruence (5 Lessons)</span>
          </div>
          <div class="chapter-chip">
            <span class="chip-icon">📐</span>
            <span class="chip-label"><strong>Module 2:</strong> Similarity (3 Lessons)</span>
          </div>
          <div class="chapter-chip">
            <span class="chip-icon">🎯</span>
            <span class="chip-label"><strong>8 In-Depth Lessons:</strong> Complete 5-Section Layout</span>
          </div>
          <div class="chapter-chip">
            <span class="chip-icon">🏆</span>
            <span class="chip-label"><strong>Module 1 Final Exam:</strong> 25 Capstone Questions</span>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MAIN APP NAVIGATION TABS                                 -->
  <!-- ======================================================== -->
  <nav class="nav-tabs-wrapper" aria-label="Main Navigation">
    <ul class="nav-tabs" role="tablist">
      <li>
        <button class="nav-tab-btn active" data-tab="tab-lessons" role="tab" aria-selected="true" id="tabBtn-lessons">
          <span class="tab-icon">📖</span> Chapter 1 Curriculum &amp; Lessons <span class="tab-tag highlight">8 Lessons + Exam</span>
        </button>
      </li>
      <li>
        <button class="nav-tab-btn" data-tab="tab-sandbox" role="tab" aria-selected="false" id="tabBtn-sandbox">
          <span class="tab-icon">🛠️</span> Coordinate Sandbox <span class="tab-tag">GeoGebra Studio</span>
        </button>
      </li>
      <li>
        <button class="nav-tab-btn" data-tab="tab-quiz" role="tab" aria-selected="false" id="tabBtn-quiz">
          <span class="tab-icon">🏆</span> Quiz &amp; Mastery Arena <span class="tab-tag">Challenges</span>
        </button>
      </li>
      <li>
        <button class="nav-tab-btn" data-tab="tab-qbank" role="tab" aria-selected="false" id="tabBtn-qbank">
          <span class="tab-icon">📚</span> Complete Question Bank <span class="tab-tag">HMH Book Qs</span>
        </button>
      </li>
      <li>
        <button class="nav-tab-btn" data-tab="tab-study" role="tab" aria-selected="false" id="tabBtn-study">
          <span class="tab-icon">🖨️</span> Printable Study Hub <span class="tab-tag">Cheat Sheet &amp; Notes</span>
        </button>
      </li>
      <li>
        <button class="nav-tab-btn" data-tab="tab-badges" role="tab" aria-selected="false" id="tabBtn-badges">
          <span class="tab-icon">🎖️</span> Badges &amp; Achievements <span class="tab-tag">8 Badges</span>
        </button>
      </li>
    </ul>
  </nav>

  <!-- ======================================================== -->
  <!-- MAIN APPLICATION CONTENT AREA                            -->
  <!-- ======================================================== -->
  <main class="app-main">

    <!-- ====================================================== -->
    <!-- TAB 1: CHAPTER 1 CURRICULUM & LESSONS STUDIO (DEFAULT) -->
    <!-- ====================================================== -->
    <section id="tab-lessons" class="tab-panel active" data-panel="lessons" role="tabpanel" aria-labelledby="tabBtn-lessons">
      
      <!-- Module Selection Overview Cards -->
      <div class="modules-overview-grid">
        
        <!-- Module 1 Card -->
        <div class="module-overview-card mod1-card active" data-module-id="mod1" id="cardModule1">
          <div class="module-card-top">
            <span class="mod-badge-pill">📘 Module 1</span>
            <span class="mod-lessons-count">5 Lessons (1.1 – 1.5) + Final Exam</span>
          </div>
          <h3 class="module-card-title">Transformations and Congruence</h3>
          <p class="module-card-subtitle">
            Rigid motions (Translations, Reflections, Rotations) are isometries. They preserve distance, angle measures, and collinearity. Preimage and image are <strong>congruent (\\(\\cong\\))</strong>.
          </p>
          <div class="module-card-footer">
            <span class="mod-status-text">✓ Distance &amp; Angles Preserved</span>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <button class="btn btn-sm btn-primary-mod1" data-jump-mod="1.1">View Lessons</button>
              <button class="btn btn-sm btn-gold-exam" data-jump-mod="mod1-exam" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; font-weight: 800; border: none; border-radius: 8px; padding: 6px 14px; cursor: pointer;">🏆 Final Exam (25 Qs)</button>
            </div>
          </div>
        </div>

        <!-- Module 2 Card -->
        <div class="module-overview-card mod2-card" data-module-id="mod2" id="cardModule2">
          <div class="module-card-top">
            <span class="mod-badge-pill">📐 Module 2</span>
            <span class="mod-lessons-count">3 Lessons (2.1 – 2.3)</span>
          </div>
          <h3 class="module-card-title">Transformations and Similarity</h3>
          <p class="module-card-subtitle">
            Dilations alter size by scale factor \\(k\\) while preserving shape and angle measures. Preimage and image are <strong>similar (\\(\\sim\\))</strong>. Perimeter scales by \\(k\\), area scales by \\(k^2\\)!
          </p>
          <div class="module-card-footer">
            <span class="mod-status-text">✓ Angles Preserved • Sides Proportional</span>
            <button class="btn btn-sm btn-primary-mod2" data-jump-mod="2.1">View Module 2 Lessons</button>
          </div>
        </div>

      </div>

      <!-- Sticky Quick Jump Bar Across All 8 Lessons + Final Exam -->
      <div class="quick-jump-bar-container">
        <div class="quick-jump-label">
          <span>⚡ Quick Jump:</span>
        </div>
        <div class="quick-jump-scroll-track" id="quickJumpTrack">
          {quick_jump_html}
        </div>
      </div>

      <!-- ACTIVE LESSON VIEWS (8 Full Lesson Studios + Dedicated Module 1 Final Exam) -->
      <div class="lesson-views-wrapper">
        {all_lesson_panels_rendered}
      </div>

    </section>

    <!-- ====================================================== -->
    <!-- TAB 2: INTERACTIVE COORDINATE SANDBOX (GeoGebra Style) -->
    <!-- ====================================================== -->
    {sandbox_html}

    <!-- ====================================================== -->
    <!-- TAB 3: QUIZ & PRACTICE ARENA                           -->
    <!-- ====================================================== -->
    {quiz_html}

    <!-- ====================================================== -->
    <!-- TAB 4: COMPLETE BOOK QUESTIONS BANK                    -->
    <!-- ====================================================== -->
    {qbank_tab_html}

    <!-- ====================================================== -->
    <!-- TAB 5: MARIAM'S STUDY HUB & PRINTABLE CHEAT SHEET      -->
    <!-- ====================================================== -->
    {study_html}

    <!-- ====================================================== -->
    <!-- TAB 6: ACHIEVEMENTS & BADGES SHOWCASE                  -->
    <!-- ====================================================== -->
    {badges_html}

  </main>

  <!-- ======================================================== -->
  <!-- TOAST NOTIFICATION CONTAINER                             -->
  <!-- ======================================================== -->
  <div id="toast" role="alert" aria-live="polite">
    <span id="toastIcon">🎉</span>
    <span id="toastMsg">Welcome to your Math Dashboard, Mariam!</span>
  </div>

  <!-- ======================================================== -->
  <!-- SCRIPTS & APPLICATION LOGIC                              -->
  <!-- ======================================================== -->
  <!-- Core Curriculum Data & Libraries -->
  <script src="curriculum-data.js"></script>
  <script src="geometry-engine.js"></script>
  <script src="quiz-arena.js"></script>
  <script src="app.js"></script>

  <!-- Redesign Enhancement Scripts: Photo Upload, Practice Checker, Lesson Navigation -->
  <script>
    (function () {{
      'use strict';

      // Expose the 25-Question Module 1 Final Exam on window
      window.MODULE_1_FINAL_TEST_QUESTIONS = {exam_questions_json};

      // Helper to launch Module 1 Final Exam directly in Quiz Arena
      window.launchModule1ExamInArena = function () {{
        const quizTabBtn = document.getElementById('tabBtn-quiz');
        if (quizTabBtn) {{
          quizTabBtn.click();
        }}
        setTimeout(function () {{
          const finalBtn = document.getElementById('quizModeMod1Final');
          if (finalBtn) {{
            finalBtn.click();
          }} else if (window.QuizArena && typeof window.QuizArena.startQuiz === 'function') {{
            window.QuizArena.startQuiz('mod1_final');
          }}
          if (window.showToast) {{
            window.showToast('🎓 Launched Module 1 Final Quiz & Mastery Exam (25 Questions)!', '🏆', 3500);
          }}
          window.scrollTo({{ top: 320, behavior: 'smooth' }});
        }}, 180);
      }};

      // --- 1. MARIAM'S PHOTO UPLOAD & LOCALSTORAGE PERSISTENCE ---
      const PHOTO_STORAGE_KEY = 'mariam_profile_photo_v2';
      const photoInput = document.getElementById('mariamPhotoInput');
      const photoImg = document.getElementById('mariamPhotoImg');
      const avatarPlaceholder = document.getElementById('mariamAvatarPlaceholder');
      const removePhotoBtn = document.getElementById('removePhotoBtn');

      function loadSavedPhoto() {{
        try {{
          const savedPhoto = localStorage.getItem(PHOTO_STORAGE_KEY);
          if (savedPhoto && photoImg) {{
            photoImg.src = savedPhoto;
            photoImg.style.display = 'block';
            if (avatarPlaceholder) avatarPlaceholder.style.display = 'none';
            if (removePhotoBtn) removePhotoBtn.style.display = 'inline-block';
          }}
        }} catch (e) {{
          console.warn('LocalStorage error reading photo:', e);
        }}
      }}

      if (photoInput) {{
        photoInput.addEventListener('change', function (e) {{
          const file = e.target.files && e.target.files[0];
          if (!file) return;

          const reader = new FileReader();
          reader.onload = function (evt) {{
            const dataUrl = evt.target.result;
            if (photoImg) {{
              photoImg.src = dataUrl;
              photoImg.style.display = 'block';
            }}
            if (avatarPlaceholder) avatarPlaceholder.style.display = 'none';
            if (removePhotoBtn) removePhotoBtn.style.display = 'inline-block';

            try {{
              localStorage.setItem(PHOTO_STORAGE_KEY, dataUrl);
              if (window.showToast) {{
                window.showToast("Looking brilliant, Mariam! Your photo is saved! 🌟", "📸", 3500);
              }}
            }} catch (err) {{
              console.warn('Could not persist image in localStorage (size limit?):', err);
            }}
          }};
          reader.readAsDataURL(file);
        }});
      }}

      if (removePhotoBtn) {{
        removePhotoBtn.addEventListener('click', function () {{
          try {{
            localStorage.removeItem(PHOTO_STORAGE_KEY);
          }} catch (e) {{}}
          if (photoImg) {{
            photoImg.src = '';
            photoImg.style.display = 'none';
          }}
          if (avatarPlaceholder) avatarPlaceholder.style.display = 'flex';
          removePhotoBtn.style.display = 'none';
          if (window.showToast) {{
            window.showToast("Avatar reset to monogram", "↺", 2000);
          }}
        }});
      }}

      // --- 2. LESSON SWITCHING & QUICK JUMP LOGIC ---
      function showLesson(lessonId) {{
        // Hide all lesson view panels
        const allPanels = document.querySelectorAll('.lesson-view-panel');
        allPanels.forEach(function (panel) {{
          panel.classList.remove('active');
        }});

        // Show matching lesson panel
        const targetPanel = document.querySelector('.lesson-view-panel[data-lesson-id="' + lessonId + '"]');
        if (targetPanel) {{
          targetPanel.classList.add('active');
        }}

        // Update Quick Jump Pills
        const allPills = document.querySelectorAll('.lesson-jump-btn');
        allPills.forEach(function (pill) {{
          if (pill.getAttribute('data-lesson-id') === lessonId) {{
            pill.classList.add('active');
            pill.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
          }} else {{
            pill.classList.remove('active');
          }}
        }});

        // Update active module card highlight
        const isMod1 = lessonId.startsWith('1.') || lessonId === 'mod1-exam';
        const cardMod1 = document.getElementById('cardModule1');
        const cardMod2 = document.getElementById('cardModule2');
        if (cardMod1 && cardMod2) {{
          if (isMod1) {{
            cardMod1.classList.add('active');
            cardMod2.classList.remove('active');
          }} else {{
            cardMod1.classList.remove('active');
            cardMod2.classList.add('active');
          }}
        }}

        // Re-render KaTeX if available
        if (window.renderMathInElement && targetPanel) {{
          try {{
            window.renderMathInElement(targetPanel, {{
              delimiters: [
                {{ left: "$$", right: "$$", display: true }},
                {{ left: "\\\\[", right: "\\\\]", display: true }},
                {{ left: "\\\\(", right: "\\\\)", display: false }},
                {{ left: "$", right: "$", display: false }}
              ],
              throwOnError: false
            }});
          }} catch (e) {{}}
        }}
      }}

      // Bind Quick Jump Buttons
      const jumpButtons = document.querySelectorAll('.lesson-jump-btn');
      jumpButtons.forEach(function (btn) {{
        btn.addEventListener('click', function () {{
          const lesId = btn.getAttribute('data-lesson-id');
          if (lesId) showLesson(lesId);
        }});
      }});

      // Bind Module Card Buttons
      const modButtons = document.querySelectorAll('[data-jump-mod]');
      modButtons.forEach(function (btn) {{
        btn.addEventListener('click', function () {{
          const lesId = btn.getAttribute('data-jump-mod');
          if (lesId) showLesson(lesId);
        }});
      }});

      // Bind Lesson Next/Prev buttons
      document.addEventListener('click', function (e) {{
        const navBtn = e.target.closest('.btn-nav-lesson');
        if (navBtn) {{
          const targetLesson = navBtn.getAttribute('data-target-lesson');
          if (targetLesson) {{
            showLesson(targetLesson);
            window.scrollTo({{ top: 350, behavior: 'smooth' }});
          }}
        }}
      }});

      // --- 3. INTERACTIVE PRACTICE (MCQs & FITB) CHECKERS ---
      // Option selection in MCQs
      document.addEventListener('click', function (e) {{
        const optBtn = e.target.closest('.practice-opt-btn');
        if (!optBtn) return;
        if (e._optHandled) return;
        e._optHandled = true;
        const grid = optBtn.closest('.practice-options-grid');
        if (!grid) return;
        grid.querySelectorAll('.practice-opt-btn').forEach(function (b) {{
          b.classList.remove('selected');
        }});
        optBtn.classList.add('selected');
      }});

      // Hint toggle
      document.addEventListener('click', function (e) {{
        const hintBtn = e.target.closest('.btn-hint-toggle');
        if (!hintBtn) return;
        if (e._hintHandled) return;
        e._hintHandled = true;
        const card = hintBtn.closest('.practice-question-card');
        if (!card) return;
        const hintCard = card.querySelector('.hint-card');
        if (!hintCard) return;
        if (hintCard.style.display === 'none' || !hintCard.style.display) {{
          hintCard.style.display = 'block';
          hintBtn.textContent = '🙈 Hide Hint';
        }} else {{
          hintCard.style.display = 'none';
          hintBtn.textContent = '💡 Need a Hint?';
        }}
      }});

      // Update Mastery Progress Bar for a lesson panel
      function updateLessonProgress(card, lessonId) {{
        if (card.dataset.solvedCorrectly === 'true') return;
        card.dataset.solvedCorrectly = 'true';

        const panel = card.closest('.lesson-view-panel');
        if (!panel) return;

        const allMcqs = panel.querySelectorAll('.practice-question-card[data-q-type="mcq"]');
        const total = allMcqs.length;
        let solved = 0;
        allMcqs.forEach(function (c) {{
          if (c.dataset.solvedCorrectly === 'true') solved++;
        }});

        const slug = lessonId.replace('.', '-');
        const countEl = document.getElementById('solved-count-' + slug);
        const xpEl = document.getElementById('earned-xp-' + slug);
        const fillEl = document.getElementById('progress-fill-' + slug);
        const pctEl = document.getElementById('score-pct-' + slug);
        const statusEl = document.getElementById('progress-status-' + slug);

        const pct = Math.round((solved / total) * 100);
        if (countEl) countEl.textContent = solved;
        if (xpEl) xpEl.textContent = solved * 10;
        if (fillEl) fillEl.style.width = pct + '%';
        if (pctEl) pctEl.textContent = pct + '%';

        if (statusEl) {{
          if (solved === total) {{
            statusEl.innerHTML = '🏆 <strong>100% MASTERY ACHIEVED!</strong> Mariam, you conquered every question in this arena! ✨';
            if (window.confetti) {{
              window.confetti({{ particleCount: 80, spread: 90, origin: {{ y: 0.6 }} }});
            }}
            if (window.QuizArena && window.QuizArena.getAudioEngine) {{
              window.QuizArena.getAudioEngine().playVictory();
            }}
          }} else {{
            statusEl.textContent = 'Great momentum, Mariam! ' + (total - solved) + ' question(s) left to 100% Mastery!';
          }}
        }}
      }}

      // Check MCQ Answer
      document.addEventListener('click', function (e) {{
        const checkBtn = e.target.closest('.btn-check-mcq');
        if (!checkBtn) return;
        if (e._checkMcqHandled) return;
        e._checkMcqHandled = true;
        const card = checkBtn.closest('.practice-question-card');
        if (!card) return;
        const correctIndex = parseInt(card.getAttribute('data-correct'), 10);
        const selectedOpt = card.querySelector('.practice-opt-btn.selected');
        const feedback = card.querySelector('.practice-feedback');
        const explanationStore = card.querySelector('.practice-explanation-store');
        const explanationHtml = explanationStore ? explanationStore.innerHTML : '';
        const lessonId = card.getAttribute('data-lesson') || '';

        if (!selectedOpt) {{
          if (feedback) {{
            feedback.className = 'practice-feedback warn';
            feedback.innerHTML = '⚠️ <strong>Please select an option first!</strong> Pick A, B, C, or D before checking.';
            feedback.style.display = 'block';
          }}
          return;
        }}

        const selectedIndex = parseInt(selectedOpt.getAttribute('data-opt-index'), 10);
        const allOpts = card.querySelectorAll('.practice-opt-btn');

        if (selectedIndex === correctIndex) {{
          selectedOpt.classList.add('correct');
          selectedOpt.classList.remove('wrong');
          if (feedback) {{
            feedback.className = 'practice-feedback correct';
            feedback.innerHTML = '<div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px;">' +
              '<span style="font-size: 1.6rem; line-height: 1;">🎉</span>' +
              '<div>' +
                '<div style="font-weight: 800; font-size: 1.05rem; color: #065f46;">Correct! Outstanding work, Mariam! (+10 XP)</div>' +
                '<div style="font-size: 0.88rem; color: #047857; margin-top: 2px;">Here is the complete HMH Teacher Edition step-by-step derivation:</div>' +
              '</div>' +
            '</div>' + explanationHtml;
            feedback.style.display = 'block';
          }}
          if (window.confetti) {{
            window.confetti({{ particleCount: 35, spread: 60, origin: {{ y: 0.7 }} }});
          }}
          if (window.QuizArena && window.QuizArena.getAudioEngine) {{
            window.QuizArena.getAudioEngine().playCorrect();
          }}
          if (window.QuizArena && window.QuizArena.awardXP) {{
            window.QuizArena.awardXP(10);
          }}
          if (window.recordMcqResult) {{
            window.recordMcqResult(true, lessonId);
          }}

          updateLessonProgress(card, lessonId);

        }} else {{
          selectedOpt.classList.add('wrong');
          // Highlight correct option for educational guidance
          allOpts.forEach(function (opt) {{
            if (parseInt(opt.getAttribute('data-opt-index'), 10) === correctIndex) {{
              opt.classList.add('correct');
            }}
          }});
          if (feedback) {{
            feedback.className = 'practice-feedback wrong';
            feedback.innerHTML = '<div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px;">' +
              '<span style="font-size: 1.6rem; line-height: 1;">✕</span>' +
              '<div>' +
                '<div style="font-weight: 800; font-size: 1.05rem; color: #991b1b;">Not quite right yet, Mariam!</div>' +
                '<div style="font-size: 0.88rem; color: #b91c1c; margin-top: 2px;">The correct choice is highlighted in green. Review the full Teacher Edition model explanation below:</div>' +
              '</div>' +
            '</div>' + explanationHtml;
            feedback.style.display = 'block';
          }}
          if (window.QuizArena && window.QuizArena.getAudioEngine) {{
            window.QuizArena.getAudioEngine().playWrong();
          }}
          if (window.recordMcqResult) {{
            window.recordMcqResult(false, lessonId);
          }}
        }}

        // Render KaTeX in newly revealed explanation
        if (window.renderMathInElement && feedback) {{
          try {{
            window.renderMathInElement(feedback, {{
              delimiters: [
                {{ left: "$$", right: "$$", display: true }},
                {{ left: "\\\\[", right: "\\\\]", display: true }},
                {{ left: "\\\\(", right: "\\\\)", display: false }},
                {{ left: "$", right: "$", display: false }}
              ],
              throwOnError: false
            }});
          }} catch (err) {{}}
        }}
      }});

      // --- 4. SHOW/HIDE BOOK MODEL ANSWERS ---
      document.addEventListener('click', function (e) {{
        const btn = e.target.closest('.btn-toggle-model-answer');
        if (!btn) return;
        const card = btn.closest('.book-question-card');
        if (!card) return;
        const answerCard = card.querySelector('.book-model-answer-card');
        if (!answerCard) return;

        if (answerCard.style.display === 'none' || !answerCard.style.display) {{
          answerCard.style.display = 'block';
          btn.textContent = '🙈 Hide Model Answer';
          btn.classList.add('btn-active');
        }} else {{
          answerCard.style.display = 'none';
          btn.textContent = '👁️ Show Model Answer';
          btn.classList.remove('btn-active');
        }}
      }});

      // --- 5. QUESTION BANK FILTER BUTTONS ---
      const qbankFilterBtns = document.querySelectorAll('.qbank-filter-btn');
      qbankFilterBtns.forEach(function (btn) {{
        btn.addEventListener('click', function () {{
          qbankFilterBtns.forEach(function (b) {{ b.classList.remove('active'); }});
          btn.classList.add('active');

          const filter = btn.getAttribute('data-filter');
          const cards = document.querySelectorAll('#qbankGrid .book-question-card');
          cards.forEach(function (card) {{
            if (filter === 'all' || card.getAttribute('data-mod') === filter) {{
              card.style.display = 'block';
            }} else {{
              card.style.display = 'none';
            }}
          }});
        }});
      }});

      // --- 6. INITIAL LOAD SETUP ---
      document.addEventListener('DOMContentLoaded', function () {{
        loadSavedPhoto();
        // Trigger initial math rendering
        setTimeout(function () {{
          if (window.renderMathInElement) {{
            window.renderMathInElement(document.body, {{
              delimiters: [
                {{ left: "$$", right: "$$", display: true }},
                {{ left: "\\\\[", right: "\\\\]", display: true }},
                {{ left: "\\\\(", right: "\\\\)", display: false }},
                {{ left: "$", right: "$", display: false }}
              ],
              throwOnError: false
            }});
          }}
        }}, 200);
      }});

    }})();
  </script>

</body>
</html>
'''

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("index.html written successfully! Size:", len(final_html), "bytes.")
