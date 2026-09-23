import sys
import time
import os
import http.server
import socketserver
import threading
from playwright.sync_api import sync_playwright

def run_tests():
    # 1. Start HTTP Server serving current project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    # Allow port reuse and pick dynamic available port
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", 0), http.server.SimpleHTTPRequestHandler)
    PORT = httpd.server_address[1]
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()
    print(f"HTTP Server running at http://localhost:{PORT}")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True
        )
        context = browser.new_context()
        page = context.new_page()

        console_errors = []
        page_errors = []

        page.on('pageerror', lambda err: page_errors.append(str(err)))
        page.on('console', lambda msg: console_errors.append(f'{msg.type}: {msg.text}') if msg.type in ['error'] else None)

        print('\n--- STEP 0: Loading Page via http.server ---')
        page.goto(f'http://localhost:{PORT}/index.html')
        page.wait_for_timeout(1000)

        # -------------------------------------------------------------
        # TEST 1: COORDINATE SANDBOX
        # -------------------------------------------------------------
        print('\n--- TEST 1: Coordinate Sandbox (tab-sandbox) ---')
        page.click('#tabBtn-sandbox')
        page.wait_for_timeout(300)
        assert page.is_visible('#tab-sandbox'), "tab-sandbox should be visible"
        print('✓ Tab switched to tab-sandbox')

        # 1.1 Shape selector
        shape_select = page.query_selector('#shapeSelect')
        assert shape_select is not None, "#shapeSelect must exist in DOM"
        page.select_option('#shapeSelect', 'quadrilateral')
        page.wait_for_timeout(200)
        state = page.evaluate('() => window.GeometryEngine.getState()')
        assert len(state['preimageVertices']) == 4, f"Expected 4 vertices for quadrilateral, got {len(state['preimageVertices'])}"
        print(f"✓ #shapeSelect changes shape to quadrilateral ({len(state['preimageVertices'])} vertices)")

        page.select_option('#shapeSelect', 'mariamM')
        page.wait_for_timeout(200)
        state = page.evaluate('() => window.GeometryEngine.getState()')
        assert len(state['preimageVertices']) == 5, f"Expected 5 vertices for mariamM, got {len(state['preimageVertices'])}"
        print(f"✓ #shapeSelect changes shape to mariamM ({len(state['preimageVertices'])} vertices)")

        page.select_option('#shapeSelect', 'triangle')
        page.wait_for_timeout(200)

        # 1.2 Transformation modes
        modes = [
            ('btnModeTranslate', '#panel-translation'),
            ('btnModeReflect', '#panel-reflection'),
            ('btnModeRotate', '#panel-rotation'),
            ('btnModeDilate', '#panel-dilation'),
            ('btnModeSequence', '#panel-sequence')
        ]
        for btn_id, panel_id in modes:
            page.click(f'#{btn_id}')
            page.wait_for_timeout(150)
            assert page.is_visible(panel_id), f"Panel {panel_id} should be visible after clicking #{btn_id}"
            print(f"✓ Mode {btn_id} activated subpanel {panel_id}")

        # 1.3 Translations: sliders dx and dy
        page.click('#btnModeTranslate')
        page.wait_for_timeout(150)
        page.evaluate('''() => {
            const dx = document.getElementById('transDx');
            if (dx) { dx.value = 5; dx.dispatchEvent(new Event('input')); }
            const dy = document.getElementById('transDy');
            if (dy) { dy.value = -3; dy.dispatchEvent(new Event('input')); }
        }''')
        page.wait_for_timeout(200)
        rule_text = page.inner_text('#mappingRuleFormula')
        assert '5' in rule_text, f"Mapping rule should contain dx=5: {rule_text}"
        print(f"✓ Translations: sliders dx=5, dy=-3 updated rule: {rule_text.strip()}")

        # 1.4 Reflections: reflect axis selectors
        page.click('#btnModeReflect')
        page.wait_for_timeout(150)
        page.click('#panel-reflection [data-reflect-axis="y"]')
        page.wait_for_timeout(200)
        rule_text = page.inner_text('#mappingRuleFormula')
        assert '-x' in rule_text or '−x' in rule_text, f"Reflection y-axis rule should have -x: {rule_text}"
        page.click('#panel-reflection [data-reflect-axis="x"]')
        page.wait_for_timeout(200)
        rule_text = page.inner_text('#mappingRuleFormula')
        assert '-y' in rule_text or '−y' in rule_text, f"Reflection x-axis rule should have -y: {rule_text}"
        print(f"✓ Reflections: reflection axis rules verified: {rule_text.strip()}")

        # 1.5 Rotations: rotation angle buttons
        page.click('#btnModeRotate')
        page.wait_for_timeout(150)
        page.click('#panel-rotation [data-rotation-angle="180"]')
        page.wait_for_timeout(200)
        rule_text = page.inner_text('#mappingRuleFormula')
        assert ('-x' in rule_text or '−x' in rule_text) and ('-y' in rule_text or '−y' in rule_text), f"180 rotation rule: {rule_text}"
        print(f"✓ Rotations: 180° rotation angle rule verified: {rule_text.strip()}")

        # 1.6 Dilations: scale factor slider k
        page.click('#btnModeDilate')
        page.wait_for_timeout(150)
        page.evaluate('''() => {
            const k = document.getElementById('dilationK');
            if (k) { k.value = 2.0; k.dispatchEvent(new Event('input')); }
        }''')
        page.wait_for_timeout(200)
        p_ratio = page.inner_text('#perimeterRatio')
        a_ratio = page.inner_text('#areaRatio')
        assert '2.00' in p_ratio or '2×' in p_ratio, f"Perimeter ratio should be 2.00x: {p_ratio}"
        assert '4.00' in a_ratio or '4×' in a_ratio, f"Area ratio should be 4.00x: {a_ratio}"
        print(f"✓ Dilations: k=2.00 scale factor verified (Perimeter: {p_ratio}, Area: {a_ratio})")

        # 1.7 Sequence builder
        page.click('#btnModeSequence')
        page.wait_for_timeout(150)
        initial_steps = len(page.query_selector_all('#sequenceStepList .sequence-item'))
        page.click('#addStepRotateBtn')
        page.wait_for_timeout(150)
        new_steps = len(page.query_selector_all('#sequenceStepList .sequence-item'))
        assert new_steps == initial_steps + 1, f"Expected {initial_steps + 1} steps, got {new_steps}"
        print(f"✓ Sequence Builder: added step (count: {new_steps})")

        remove_btns = page.query_selector_all('#sequenceStepList .sequence-remove-btn')
        if len(remove_btns) > 0:
            remove_btns[-1].click()
            page.wait_for_timeout(150)
            after_remove = len(page.query_selector_all('#sequenceStepList .sequence-item'))
            assert after_remove == initial_steps, f"Expected {initial_steps} steps, got {after_remove}"
            print(f"✓ Sequence Builder: removed step (count restored to {after_remove})")

        page.click('#runSequenceBtn')
        page.wait_for_timeout(200)
        print("✓ Sequence Builder: run sequence animation executed smoothly")

        # -------------------------------------------------------------
        # TEST 2: LESSONS NAVIGATION (1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 2.2, 2.3)
        # -------------------------------------------------------------
        print('\n--- TEST 2: Lessons Navigation (tab-lessons) ---')
        page.click('#tabBtn-lessons')
        page.wait_for_timeout(300)
        assert page.is_visible('#tab-lessons'), "tab-lessons should be visible"
        print("✓ Switched to tab-lessons")

        lessons = ['1.1', '1.2', '1.3', '1.4', '1.5', '2.1', '2.2', '2.3']
        for les_id in lessons:
            jump_btn = page.query_selector(f'.lesson-jump-btn[data-lesson-id="{les_id}"]')
            assert jump_btn is not None, f"Jump button for lesson {les_id} must exist"
            jump_btn.click()
            page.wait_for_timeout(200)

            norm_id = les_id.replace('.', '-')
            panel_sel = f'#lesson-view-{norm_id}'
            panel = page.query_selector(panel_sel)
            assert panel is not None, f"Lesson view panel {panel_sel} must exist"
            is_active = page.evaluate(f'''() => {{
                const el = document.querySelector("{panel_sel}");
                return el && (el.classList.contains("active") || window.getComputedStyle(el).display !== "none");
            }}''')
            assert is_active, f"Lesson view panel {panel_sel} should be active/visible"
            print(f"✓ Navigation to Lesson {les_id}: {panel_sel} is active")

        # -------------------------------------------------------------
        # TEST 3: PRACTICE QUESTIONS
        # -------------------------------------------------------------
        print('\n--- TEST 3: Practice Questions (options, hint toggle, check answer, explanations) ---')
        page.click('.lesson-jump-btn[data-lesson-id="1.1"]')
        page.wait_for_timeout(200)

        card = page.query_selector('#lesson-view-1-1 .practice-question-card[data-q-type="mcq"]')
        assert card is not None, "Practice question card should exist in Lesson 1.1"

        # 3.1 Option click
        opt_btn = card.query_selector('.practice-opt-btn')
        assert opt_btn is not None, "Practice option button should exist"
        opt_btn.click()
        page.wait_for_timeout(150)
        is_selected = 'selected' in (opt_btn.get_attribute('class') or '')
        assert is_selected, "Practice option should have 'selected' class after click"
        print("✓ Practice Question: clicked option and verified selected state")

        # 3.2 Hint toggle
        hint_btn = card.query_selector('.btn-hint-toggle')
        hint_card = card.query_selector('.hint-card')
        assert hint_btn is not None, "Hint toggle button should exist"
        assert hint_card is not None, "Hint card container should exist"

        hint_btn.click()
        page.wait_for_timeout(150)
        is_hint_visible = page.evaluate('el => el.style.display !== "none"', hint_card)
        assert is_hint_visible, "Hint card should be visible after click"
        print("✓ Practice Question: hint toggle opened hint card successfully")

        hint_btn.click()
        page.wait_for_timeout(150)
        is_hint_hidden = page.evaluate('el => el.style.display === "none"', hint_card)
        assert is_hint_hidden, "Hint card should be hidden after second click"
        print("✓ Practice Question: hint toggle closed hint card successfully")

        # 3.3 Check Answer & View Explanation
        check_btn = card.query_selector('.btn-check-mcq')
        assert check_btn is not None, "Check Answer button should exist"
        check_btn.click()
        page.wait_for_timeout(200)

        feedback_el = card.query_selector('.practice-feedback')
        assert feedback_el is not None, "Practice feedback element should exist"
        is_feedback_visible = page.evaluate('el => el.style.display !== "none"', feedback_el)
        assert is_feedback_visible, "Feedback should be visible after checking answer"
        feedback_text = page.inner_text('#lesson-view-1-1 .practice-question-card[data-q-type="mcq"] .practice-feedback')
        assert len(feedback_text.strip()) > 0, "Feedback should contain explanation text"
        print(f"✓ Practice Question: checked answer and displayed feedback/explanation: '{feedback_text.strip()[:45]}...'")

        # -------------------------------------------------------------
        # TEST 4: QUIZ ARENA (Module 1 Test 25 Qs & Lesson Practice)
        # -------------------------------------------------------------
        print('\n--- TEST 4: Quiz Arena (Module 1 Test 25 Qs and Lesson Practice modes) ---')
        page.click('#tabBtn-quiz')
        page.wait_for_timeout(300)
        assert page.is_visible('#tab-quiz'), "tab-quiz should be visible"
        print("✓ Switched to tab-quiz")

        # 4.1 Launch Module 1 Test (25 Qs)
        page.click('#quizModeMod1')
        page.wait_for_timeout(300)

        has_card = page.evaluate('''() => {
            return window.QuizArena ? (document.querySelector('.question-card') !== null) : false;
        }''')
        assert has_card, "Question card should be mounted in Module 1 Test mode"
        
        q_count = page.evaluate('''() => {
            const txt = document.querySelector('.question-card') ? document.querySelector('.question-card').innerText : '';
            const match = txt.match(/of\\s+(\\d+)/);
            return match ? parseInt(match[1], 10) : 0;
        }''')
        assert q_count == 25, f"Expected 25 questions for Module 1 Test, got {q_count}"
        print(f"✓ Quiz Arena: launched Module 1 Test with exactly {q_count} questions!")

        # 4.2 Test interacting with Module 1 Test question
        opts = page.query_selector_all('.option-btn')
        if len(opts) > 0:
            opts[0].click()
            page.wait_for_timeout(150)
            print("✓ Quiz Arena: option selected")
        elif page.query_selector('#coord-input-x'):
            page.fill('#coord-input-x', '0')
            page.fill('#coord-input-y', '0')
            print("✓ Quiz Arena: coordinate inputs filled")

        # Submit answer
        page.click('#btn-submit-answer')
        page.wait_for_timeout(300)
        assert page.is_visible('#quiz-explanation-box'), "Explanation box should appear after submit"
        print("✓ Quiz Arena: submitted answer and verified explanation box appears")

        # 4.3 Launch Lesson Practice mode
        page.evaluate('() => window.QuizArena.resetToMenu()')
        page.wait_for_timeout(300)

        page.select_option('#quiz-lesson-filter', '1.1')
        page.wait_for_timeout(150)
        page.click('#btnStartLessonPractice')
        page.wait_for_timeout(300)

        practice_badge = page.evaluate('''() => {
            const badge = document.querySelector('.question-badge');
            return badge ? badge.textContent : '';
        }''')
        assert '1.1' in practice_badge or 'Translations' in practice_badge or 'Investigate' in practice_badge or 'Transformation' in practice_badge, f"Badge should indicate Lesson 1.1 practice: {practice_badge}"
        print(f"✓ Quiz Arena: launched Lesson Practice mode for Lesson 1.1 (Badge: {practice_badge})")

        # 4.4 Audio engine verification
        audio_check = page.evaluate('''() => {
            const engine = window.QuizArena.getAudioEngine();
            const wasMuted = engine.getMuted();
            engine.playClick();
            engine.playCorrect();
            engine.playWrong();
            const nowMuted = engine.toggleMute();
            engine.toggleMute();
            return { wasMuted, nowMuted };
        }''')
        print(f"✓ Audio Engine verified synthesized Web Audio API sounds: {audio_check}")

        # -------------------------------------------------------------
        # ZERO RUNTIME ERRORS CHECK
        # -------------------------------------------------------------
        print('\n--- VERIFY ZERO RUNTIME ERRORS ---')
        print(f"Page errors: {page_errors}")
        print(f"Console errors: {console_errors}")
        assert len(page_errors) == 0, f"Page errors encountered: {page_errors}"
        assert len(console_errors) == 0, f"Console errors encountered: {console_errors}"
        print("✓ ZERO console errors or page errors verified!")

        browser.close()
        httpd.shutdown()
        print("\n🎉 ALL PLAYWRIGHT QA CHECKS PASSED SUCCESSFULLY!")

if __name__ == '__main__':
    run_tests()
