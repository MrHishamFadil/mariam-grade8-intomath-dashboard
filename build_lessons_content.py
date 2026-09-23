# -*- coding: utf-8 -*-
"""
Builds the final lessons-content.js file
Merging Module 1 (Lessons 1.1 - 1.5) and Module 2 (Lessons 2.1 - 2.3)
With all 20 MCQs per lesson and Module 1 Final Test questions.
Exports window.LESSONS_CONTENT
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from gen_module1 import get_module1_lessons
from gen_module2 import get_module2_lessons
import build_lesson_1_1
import build_lesson_1_2
import build_lesson_1_3
import build_lesson_1_4
import build_lesson_1_5
import build_module1_final_test

def main():
    m1_lessons = get_module1_lessons()
    m2_lessons = get_module2_lessons()

    lesson_mcqs_map = {
        "1.1": build_lesson_1_1.LESSON_1_1_DATA["mcqs"],
        "1.2": build_lesson_1_2.MCQS,
        "1.3": build_lesson_1_3.LESSON_1_3_DATA["mcqs"],
        "1.4": build_lesson_1_4.LESSON_1_4_DATA["mcqs"],
        "1.5": build_lesson_1_5.LESSON_1_5_DATA["mcqs"],
    }

    final_test_qs = build_module1_final_test.MODULE_1_FINAL_TEST_QUESTIONS

    # Inject 20 MCQs into each Module 1 lesson
    for lid, mcqs in lesson_mcqs_map.items():
        if lid in m1_lessons:
            practice_qs = []
            for item in mcqs:
                practice_qs.append({
                    "id": item["id"],
                    "type": "mcq",
                    "prompt": item["q"],
                    "question": item["q"],
                    "q": item["q"],
                    "options": list(item["opts"]),
                    "opts": list(item["opts"]),
                    "correctIndex": int(item["correct"]),
                    "correctAnswer": int(item["correct"]),
                    "correct": int(item["correct"]),
                    "hint": str(item.get("hint", "")),
                    "explanation": str(item.get("explanation", "")),
                    "dok": int(item.get("dok", 2)),
                    "standard": str(item.get("standard", ""))
                })
            m1_lessons[lid]["practiceQuestions"] = practice_qs
            m1_lessons[lid]["mcqs"] = practice_qs
            m1_lessons[lid]["practice"] = {"mcqs": practice_qs}

    all_lessons = {}
    all_lessons.update(m1_lessons)
    all_lessons.update(m2_lessons)

    master_data = {
        "chapterInfo": {
            "title": "Chapter 1: Transformational Geometry",
            "curriculum": "HMH Into Math NM Grade 8 Teacher Edition",
            "student": "Mariam Hisham AbdelFadil",
            "grade": "Grade 8",
            "standards": [
                "CCSS.MATH.CONTENT.8.G.A.1",
                "CCSS.MATH.CONTENT.8.G.A.1.a",
                "CCSS.MATH.CONTENT.8.G.A.1.b",
                "CCSS.MATH.CONTENT.8.G.A.1.c",
                "CCSS.MATH.CONTENT.8.G.A.2",
                "CCSS.MATH.CONTENT.8.G.A.3",
                "CCSS.MATH.CONTENT.8.G.A.4"
            ]
        },
        "modules": [
            {
                "id": "module-1",
                "number": 1,
                "title": "Transformations and Congruence",
                "subtitle": "Rigid Motions, Mapping Rules, and Congruence Proofs",
                "lessonIds": ["1.1", "1.2", "1.3", "1.4", "1.5"]
            },
            {
                "id": "module-2",
                "number": 2,
                "title": "Transformations and Similarity",
                "subtitle": "Reductions, Enlargements, Dilations, and Similar Figures",
                "lessonIds": ["2.1", "2.2", "2.3"]
            }
        ],
        "moduleTests": {
            "module-1": [
                {
                    "id": q["id"],
                    "module": 1,
                    "lesson": q["lesson"],
                    "standard": q["standard"],
                    "dok": q["dok"],
                    "type": "multiple_choice",
                    "question": q["q"],
                    "options": list(q["opts"]),
                    "correctAnswer": int(q["correct"]),
                    "correctIndex": int(q["correct"]),
                    "hint": str(q.get("hint", "")),
                    "explanation": str(q.get("explanation", ""))
                }
                for q in final_test_qs
            ]
        },
        "lessons": all_lessons
    }

    # Add direct lookup aliases for convenience: '1.1', 'lesson-1.1', etc.
    for lid, lobj in all_lessons.items():
        master_data[lid] = lobj
        master_data[f"lesson-{lid}"] = lobj

    json_str = json.dumps(master_data, indent=2, ensure_ascii=False)

    js_template = f"""/**
 * ============================================================================
 * MARIAM HISHAM ABDELFADIL - GRADE 8 INTO MATH INTERACTIVE DASHBOARD
 * Chapter 1: Transformational Geometry (HMH Into Math NM Grade 8 TE)
 * Master Curriculum Content, Worked Examples, Practice Questions & Book Question Bank
 * File: lessons-content.js
 *
 * Modules Covered:
 *  - Module 1: Transformations and Congruence
 *      • Lesson 1.1: Investigate Transformations (20 MCQs)
 *      • Lesson 1.2: Explore Translations (20 MCQs)
 *      • Lesson 1.3: Explore Reflections (20 MCQs)
 *      • Lesson 1.4: Explore Rotations (20 MCQs)
 *      • Lesson 1.5: Understand and Recognize Congruent Figures (20 MCQs)
 *  - Module 1 Final Mastery Test: 25 High-Quality Exam Questions
 *  - Module 2: Transformations and Similarity
 *      • Lesson 2.1: Investigate Reductions and Enlargements
 *      • Lesson 2.2: Explore Dilations
 *      • Lesson 2.3: Understand and Recognize Similar Figures
 * ============================================================================
 */

(function (root, factory) {{
  if (typeof module === 'object' && module.exports) {{
    module.exports = factory();
  }} else {{
    var content = factory();
    root.LESSONS_CONTENT = content;
    if (typeof window !== 'undefined') {{
      window.LESSONS_CONTENT = content;
    }}
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this), function () {{
  'use strict';

  var DATA = {json_str};

  // Helper Methods on LESSONS_CONTENT
  DATA.getLesson = function (id) {{
    if (!id) return null;
    var cleanId = String(id).replace(/^lesson-/, '');
    return DATA.lessons[cleanId] || DATA.lessons[id] || null;
  }};

  DATA.getAllLessonIds = function () {{
    return ['1.1', '1.2', '1.3', '1.4', '1.5', '2.1', '2.2', '2.3'];
  }};

  DATA.getModuleLessons = function (moduleNum) {{
    var mod = DATA.modules.find(function (m) {{ return m.number === Number(moduleNum); }});
    if (!mod) return [];
    return mod.lessonIds.map(function (id) {{ return DATA.lessons[id]; }});
  }};

  return DATA;
}});
"""

    output_path = os.path.join(BASE_DIR, "lessons-content.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js_template)

    print(f"Successfully wrote {output_path} ({os.path.getsize(output_path):,} bytes)")

    # Secondary output to scratch directory if present
    scratch_dir = "/Users/hishammohamedabdelfadil/.gemini/antigravity/scratch/mariam-math-dashboard"
    if os.path.exists(scratch_dir):
        scratch_path = os.path.join(scratch_dir, "lessons-content.js")
        with open(scratch_path, "w", encoding="utf-8") as f:
            f.write(js_template)
        print(f"Successfully synced {scratch_path}")

if __name__ == "__main__":
    main()
