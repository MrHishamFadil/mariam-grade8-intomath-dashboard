/**
 * ============================================================================
 * MARIAM HISHAM ABDELFADIL - GRADE 8 INTO MATH INTERACTIVE DASHBOARD
 * Master Application Controller & Integration Layer
 * File: app.js
 * 
 * Responsibilities:
 *  1. Smooth Tab Navigation & Panel Transition Management
 *  2. Interactive Geometry Engine Controller (Shapes, Sliders, Radios, Sequences, Animations)
 *  3. Real-Time Math Metric Synchronization (KaTeX formulas, live coordinates, area/perimeter meters)
 *  4. Quiz Arena Integration (Modes, question handling, audio toggles, gamified progress)
 *  5. Direct Sandbox Deep-linking from Lesson Hub Cards ("Try in Sandbox")
 *  6. Mariam's Profile, XP, Streak, Level, and Badges State Management
 *  7. Study Hub Notepad Persistence (localStorage, quick math symbols, print view)
 *  8. Toast Notification Dispatcher & Audio Feedback
 *  9. Resilient Fallbacks for asynchronous loading of curriculum & submodules
 * ============================================================================
 */

(function (window, document) {
  // Ensure dual compatibility for #shapeSelect and #presetShapeSelect
  const origGetById = document.getElementById.bind(document);
  document.getElementById = function(id) {
    if (id === 'presetShapeSelect') return origGetById('shapeSelect') || origGetById('presetShapeSelect');
    if (id === 'shapeSelect') return origGetById('shapeSelect') || origGetById('presetShapeSelect');
    return origGetById(id);
  };
  const origQuerySelector = document.querySelector.bind(document);
  document.querySelector = function(selector) {
    if (selector === '#presetShapeSelect') return origQuerySelector('#shapeSelect') || origQuerySelector('#presetShapeSelect');
    if (selector === '#shapeSelect') return origQuerySelector('#shapeSelect') || origQuerySelector('#presetShapeSelect');
    return origQuerySelector(selector);
  };

  // --- 1. GLOBAL FALLBACKS & SAMPLE DATASET ---
  if (!window.CURRICULUM_DATA) {
    console.warn('[Dashboard] CURRICULUM_DATA not detected. Injecting resilient fallback dataset.');
    window.CURRICULUM_DATA = {
      studentProfile: {
        name: 'Mariam Hisham AbdelFadil',
        grade: 'Grade 8',
        program: 'HMH Into Math',
        unit: 'Unit 1: Transformational Geometry'
      },
      modules: [
        {
          id: 'module-1',
          number: 1,
          title: 'Transformations and Congruence',
          subtitle: 'Rigid Motions, Mapping Rules, and Congruence Proofs',
          badge: 'Module 1',
          themeColor: '#4F46E5',
          lessons: [
            { id: '1.1', title: 'Investigate Transformations', target: '1.1' },
            { id: '1.2', title: 'Explore Translations', target: '1.2' },
            { id: '1.3', title: 'Explore Reflections', target: '1.3' },
            { id: '1.4', title: 'Explore Rotations', target: '1.4' },
            { id: '1.5', title: 'Understand and Recognize Congruent Figures', target: '1.5' }
          ]
        },
        {
          id: 'module-2',
          number: 2,
          title: 'Transformations and Similarity',
          subtitle: 'Reductions, Enlargements, Dilations, and Proportions',
          badge: 'Module 2',
          themeColor: '#0ea5e9',
          lessons: [
            { id: '2.1', title: 'Investigate Reductions and Enlargements', target: '2.1' },
            { id: '2.2', title: 'Explore Dilations', target: '2.2' },
            { id: '2.3', title: 'Understand and Recognize Similar Figures', target: '2.3' }
          ]
        }
      ]
    };
  }

  // --- 2. TOAST NOTIFICATION SYSTEM ---
  let toastTimer = null;
  function showToast(message, icon, duration) {
    icon = icon || '🎉';
    duration = duration || 3200;

    const toastEl = document.getElementById('toast');
    const toastIcon = document.getElementById('toastIcon');
    const toastMsg = document.getElementById('toastMsg');

    if (!toastEl) {
      console.log('[' + icon + '] ' + message);
      return;
    }

    if (toastIcon) toastIcon.textContent = icon;
    if (toastMsg) toastMsg.innerHTML = message;

    toastEl.classList.remove('show');
    // Force reflow
    void toastEl.offsetWidth;
    toastEl.classList.add('show');

    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toastEl.classList.remove('show');
    }, duration);
  }
  window.showToast = showToast;

  // --- 3. KATEX HELPER ---
  function renderMath(container) {
    if (!container) return;
    if (window.renderMathInElement) {
      try {
        window.renderMathInElement(container, {
          delimiters: [
            { left: '4959', right: '4959', display: true },
            { left: '\[', right: '\]', display: true },
            { left: '\(', right: '\)', display: false },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false
        });
      } catch (e) {
        console.warn('KaTeX auto-render warning:', e);
      }
    }
  }

  function renderFormulaLatex(elementId, latexStr) {
    const el = document.getElementById(elementId);
    if (!el) return;
    if (window.katex) {
      try {
        window.katex.render(latexStr, el, { throwOnError: false, displayMode: false });
        return;
      } catch (e) {
        // Fallback below
      }
    }
    el.textContent = latexStr;
  }

  // --- 4. TAB SWITCHING LOGIC ---
  let currentActiveTab = 'tab-lessons';

  function initTabNavigation() {
    // Robust document-level event delegation for all tab buttons
    document.addEventListener('click', function (e) {
      const btn = e.target.closest('.nav-tab-btn');
      if (!btn) return;
      const targetTabId = btn.getAttribute('data-tab');
      if (targetTabId) {
        switchTab(targetTabId);
      }
    });
  }

  function switchTab(tabId) {
    if (!tabId) return;

    const tabButtons = document.querySelectorAll('.nav-tab-btn');
    const tabPanels = document.querySelectorAll('.tab-panel');

    tabButtons.forEach(function (btn) {
      const match = btn.getAttribute('data-tab') === tabId;
      if (match) {
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
      } else {
        btn.classList.remove('active');
        btn.setAttribute('aria-selected', 'false');
      }
    });

    let activePanelEl = null;
    tabPanels.forEach(function (panel) {
      if (panel.id === tabId) {
        panel.classList.add('active');
        activePanelEl = panel;
      } else {
        panel.classList.remove('active');
      }
    });

    currentActiveTab = tabId;

    // Actions on specific tab activations
    if (tabId === 'tab-sandbox') {
      if (window.GeometryEngine) {
        setTimeout(function () {
          window.GeometryEngine.resetView();
        }, 60);
      }
    } else if (tabId === 'tab-quiz') {
      if (window.QuizArena && typeof window.QuizArena.init === 'function') {
        window.QuizArena.init();
      }
    } else if (tabId === 'tab-badges') {
      syncProfileAndBadgesUI();
    } else if (tabId === 'tab-analytics') {
      if (typeof window.updateAnalyticsUI === 'function') {
        window.updateAnalyticsUI();
      }
    } else if (tabId === 'tab-qbank' || tabId === 'tab-study' || tabId === 'tab-lessons') {
      if (activePanelEl) {
        renderMath(activePanelEl);
      }
    }

    // Scroll smoothly to main area on mobile
    if (window.innerWidth < 768) {
      const mainEl = document.querySelector('main.app-main');
      if (mainEl) {
        try { mainEl.scrollIntoView({ behavior: 'smooth' }); } catch (e) {}
      }
    }
  }
  window.switchTab = switchTab;

  // --- 5. MARIAM PROFILE & BADGES STATE SYNC ---
  function getProfileData() {
    if (window.QuizArena && typeof window.QuizArena.getProfile === 'function') {
      return window.QuizArena.getProfile();
    }
    try {
      const stored = localStorage.getItem('mariam_math_profile');
      if (stored) return JSON.parse(stored);
    } catch (e) {
      console.warn('Storage read error:', e);
    }
    return {
      name: 'Mariam Hisham AbdelFadil',
      xp: 250,
      level: 1,
      levelTitle: 'Coordinate Apprentice',
      streak: 3,
      badges: ['coord_commander', 'mirror_marvel', 'spin_doctor', 'sequence_strategist', 'streak_superstar']
    };
  }

  function addXP(amount) {
    if (!amount || amount <= 0) return 0;
    let newXP = 0;
    if (window.QuizArena && typeof window.QuizArena.awardXP === 'function') {
      newXP = window.QuizArena.awardXP(amount);
    } else {
      const profile = getProfileData();
      profile.xp = (profile.xp || 0) + amount;
      try {
        localStorage.setItem('mariam_math_profile', JSON.stringify(profile));
      } catch (e) {}
      newXP = profile.xp;
    }
    syncProfileAndBadgesUI();
    return newXP;
  }
  window.addXP = addXP;

  function syncProfileAndBadgesUI() {
    const profile = getProfileData();

    // 1. Header pills
    const xpElements = [
      document.getElementById('userXP'),
      document.getElementById('user-xp'),
      document.querySelector('.stat-pill.xp span:last-child')
    ];
    xpElements.forEach(function (el) {
      if (el) el.textContent = (profile.xp || 0) + ' XP';
    });

    const streakElements = [
      document.getElementById('userStreak'),
      document.getElementById('user-streak'),
      document.querySelector('.stat-pill.streak span:last-child')
    ];
    streakElements.forEach(function (el) {
      if (el) el.textContent = (profile.streak || 0) + ' 🔥';
    });

    const levelElements = [
      document.getElementById('userLevel'),
      document.getElementById('user-level-title'),
      document.querySelector('.user-level')
    ];
    levelElements.forEach(function (el) {
      if (el) {
        const title = profile.levelTitle || 'Grade 8 Math Star';
        const lvl = profile.level || 1;
        el.textContent = 'Lv.' + lvl + ' ' + title;
      }
    });

    // 2. Badges Showcase (tab-badges)
    const badgeElements = document.querySelectorAll('#badgesGridContainer .badge-item');
    badgeElements.forEach(function (bEl) {
      const badgeId = bEl.getAttribute('data-badge-id');
      if (!badgeId) return;

      const isUnlocked = profile.badges && (
        profile.badges.includes(badgeId) ||
        profile.badges.includes(badgeId.replace('-', '_')) ||
        profile.badges.includes(badgeId.replace('_', '-'))
      );

      if (isUnlocked) {
        bEl.classList.remove('locked');
        bEl.classList.add('unlocked');
        const statusDiv = bEl.querySelector('div:last-child');
        if (statusDiv && statusDiv.textContent.includes('LOCKED')) {
          statusDiv.style.color = '#d97706';
          statusDiv.style.fontWeight = '800';
          statusDiv.textContent = 'UNLOCKED • +50 XP';
        }
      }
    });

    // 3. Level progress bar
    const levelFill = document.querySelector('#tab-badges .level-progress-fill');
    if (levelFill) {
      const currentXP = profile.xp || 0;
      const targetXP = 500;
      const pct = Math.min(100, Math.round((currentXP / targetXP) * 100));
      levelFill.style.width = pct + '%';
    }
  }

  // --- 6. GEOMETRY ENGINE CONTROLLER ---
  let currentMode = 'translation'; // 'translation' | 'reflection' | 'rotation' | 'dilation' | 'sequence'
  let sequenceSteps = [
    { type: 'translation', params: { dx: 3, dy: 2 }, label: 'Translate: ⟨+3, +2⟩' },
    { type: 'reflection', params: { axis: 'x-axis' }, label: 'Reflect across x-axis' }
  ];

  function initGeometryController() {
    const canvas = document.getElementById('interactiveCanvas');
    if (!canvas) {
      console.warn('Canvas #interactiveCanvas not found.');
      return;
    }

    if (!window.GeometryEngine) {
      console.error('GeometryEngine library not loaded.');
      return;
    }

    // Initialize Canvas
    window.GeometryEngine.init('interactiveCanvas');

    // Wire up Update Callback
    window.GeometryEngine.onUpdate(handleGeometryUpdate);

    // 1. Preset Shapes Dropdown
    const shapeSelect = document.getElementById('shapeSelect') || document.getElementById('presetShapeSelect');
    if (shapeSelect) {
      shapeSelect.addEventListener('change', function () {
        const shapeKey = shapeSelect.value;
        window.GeometryEngine.setShape(shapeKey);
        const selOpt = shapeSelect.options && shapeSelect.selectedIndex >= 0 ? shapeSelect.options[shapeSelect.selectedIndex] : null;
        const optText = selOpt ? selOpt.text : shapeKey;
        showToast('Shape loaded: ' + optText, '📐', 2000);
      });
    }

    // 2. Toolbar Action Buttons
    const snapBtn = document.getElementById('toggleGridSnap');
    let snapActive = true;
    if (snapBtn) {
      snapBtn.classList.add('active');
      snapBtn.addEventListener('click', function () {
        snapActive = !snapActive;
        snapBtn.classList.toggle('active', snapActive);
        showToast(snapActive ? 'Grid Snapping: ON 🧲' : 'Grid Snapping: OFF', '🧲', 1500);
      });
    }

    const vectorsBtn = document.getElementById('toggleVectors');
    let vectorsActive = true;
    if (vectorsBtn) {
      vectorsBtn.classList.add('active');
      vectorsBtn.addEventListener('click', function () {
        vectorsActive = !vectorsActive;
        vectorsBtn.classList.toggle('active', vectorsActive);
        showToast(vectorsActive ? 'Vector Visual Aids: ON ↗️' : 'Vector Visual Aids: OFF', '↗️', 1500);
      });
    }

    const labelsBtn = document.getElementById('toggleLabels');
    let labelsActive = true;
    if (labelsBtn) {
      labelsBtn.classList.add('active');
      labelsBtn.addEventListener('click', function () {
        labelsActive = !labelsActive;
        labelsBtn.classList.toggle('active', labelsActive);
        showToast(labelsActive ? 'Vertex Labels: ON 🏷️' : 'Vertex Labels: OFF', '🏷️', 1500);
      });
    }

    const resetViewBtn = document.getElementById('resetViewBtn');
    if (resetViewBtn) {
      resetViewBtn.addEventListener('click', function () {
        window.GeometryEngine.resetView();
        showToast('Coordinate grid view centered', '🔍', 1500);
      });
    }

    const resetShapeBtn = document.getElementById('resetShapeBtn');
    if (resetShapeBtn) {
      resetShapeBtn.addEventListener('click', function () {
        const activeShape = shapeSelect ? shapeSelect.value : 'triangle';
        window.GeometryEngine.setShape(activeShape);
        showToast('Preimage vertices reset to default', '🔄', 1500);
      });
    }

    const playAnimationBtn = document.getElementById('playAnimationBtn');
    if (playAnimationBtn) {
      playAnimationBtn.addEventListener('click', function () {
        if (currentMode === 'sequence') {
          playSequenceAnimation();
        } else {
          // Play mini animation for single transformation
          playSingleTransformAnimation();
        }
      });
    }

    // 3. Transformation Mode Selector Buttons
    const modeButtons = {
      translation: document.getElementById('btnModeTranslate'),
      reflection: document.getElementById('btnModeReflect'),
      rotation: document.getElementById('btnModeRotate'),
      dilation: document.getElementById('btnModeDilate'),
      sequence: document.getElementById('btnModeSequence')
    };

    const subpanels = {
      translation: document.getElementById('panel-translation'),
      reflection: document.getElementById('panel-reflection'),
      rotation: document.getElementById('panel-rotation'),
      dilation: document.getElementById('panel-dilation'),
      sequence: document.getElementById('panel-sequence')
    };

    function setActiveMode(mode) {
      currentMode = mode;

      // Update button styles
      Object.keys(modeButtons).forEach(function (m) {
        const btn = modeButtons[m];
        if (!btn) return;
        if (m === mode) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });

      // Show/Hide subpanels
      Object.keys(subpanels).forEach(function (m) {
        const panel = subpanels[m];
        if (!panel) return;
        if (m === mode) {
          panel.style.display = 'block';
        } else {
          panel.style.display = 'none';
        }
      });

      // Apply current mode to GeometryEngine
      applyCurrentTransformation();
    }

    Object.keys(modeButtons).forEach(function (m) {
      const btn = modeButtons[m];
      if (btn) {
        btn.addEventListener('click', function () {
          setActiveMode(m);
        });
      }
    });

    // --- Subpanel 1: Translation Controls ---
    const transDx = document.getElementById('transDx');
    const transDy = document.getElementById('transDy');
    const valDx = document.getElementById('valDx');
    const valDy = document.getElementById('valDy');
    const applyTranslateBtn = document.getElementById('applyTranslateBtn');

    function updateTranslationUI() {
      const dx = parseInt(transDx ? transDx.value : '3', 10);
      const dy = parseInt(transDy ? transDy.value : '2', 10);

      if (valDx) valDx.textContent = (dx >= 0 ? '+' : '') + dx;
      if (valDy) valDy.textContent = (dy >= 0 ? '+' : '') + dy;

      if (applyTranslateBtn) {
        const signX = dx >= 0 ? '+' + dx : String(dx);
        const signY = dy >= 0 ? '+' + dy : String(dy);
        applyTranslateBtn.innerHTML = 'Apply Translation \((x' + signX + ', y' + signY + ')\)';
        renderMath(applyTranslateBtn);
      }

      if (currentMode === 'translation') {
        window.GeometryEngine.setTransformation('translation', { dx: dx, dy: dy });
      }
    }

    if (transDx) transDx.addEventListener('input', updateTranslationUI);
    if (transDy) transDy.addEventListener('input', updateTranslationUI);

    document.querySelectorAll('.nudge-group button').forEach(function (nudgeBtn) {
      nudgeBtn.addEventListener('click', function () {
        if (nudgeBtn.hasAttribute('data-nudge-x') && transDx) {
          const delta = parseInt(nudgeBtn.getAttribute('data-nudge-x'), 10);
          transDx.value = delta === 0 ? 0 : Math.max(-10, Math.min(10, parseInt(transDx.value, 10) + delta));
          updateTranslationUI();
        } else if (nudgeBtn.hasAttribute('data-nudge-y') && transDy) {
          const delta = parseInt(nudgeBtn.getAttribute('data-nudge-y'), 10);
          transDy.value = delta === 0 ? 0 : Math.max(-10, Math.min(10, parseInt(transDy.value, 10) + delta));
          updateTranslationUI();
        }
      });
    });

    if (applyTranslateBtn) {
      applyTranslateBtn.addEventListener('click', function () {
        updateTranslationUI();
        showToast('Translation applied successfully!', '✨', 1800);
      });
    }

    // --- Subpanel 2: Reflection Controls ---
    const reflectLabels = document.querySelectorAll('#panel-reflection .pill-radio-label');
    const customLineSliderGroup = document.getElementById('customLineSliderGroup');
    const reflectConst = document.getElementById('reflectConst');
    const valReflectConst = document.getElementById('valReflectConst');
    const customLineLabel = document.getElementById('customLineLabel');
    const applyReflectBtn = document.getElementById('applyReflectBtn');
    let selectedReflectAxis = 'x-axis';

    function updateReflectionUI() {
      const k = parseInt(reflectConst ? reflectConst.value : '0', 10);
      if (valReflectConst) valReflectConst.textContent = String(k);

      if (currentMode === 'reflection') {
        let engineAxis = selectedReflectAxis;
        if (selectedReflectAxis === 'x') engineAxis = 'x-axis';
        else if (selectedReflectAxis === 'y') engineAxis = 'y-axis';
        else if (selectedReflectAxis === 'yx') engineAxis = 'y=x';
        else if (selectedReflectAxis === 'ynx') engineAxis = 'y=-x';
        else if (selectedReflectAxis === 'custom_v') engineAxis = 'line-x';
        else if (selectedReflectAxis === 'custom_h') engineAxis = 'line-y';

        window.GeometryEngine.setTransformation('reflection', { axis: engineAxis, k: k });
      }
    }

    reflectLabels.forEach(function (lbl) {
      lbl.addEventListener('click', function () {
        reflectLabels.forEach(function (l) { l.classList.remove('active'); });
        lbl.classList.add('active');

        const axisKey = lbl.getAttribute('data-reflect-axis');
        selectedReflectAxis = axisKey;

        const isCustom = axisKey === 'custom_v' || axisKey === 'custom_h';
        if (customLineSliderGroup) {
          customLineSliderGroup.style.display = isCustom ? 'block' : 'none';
        }
        if (customLineLabel) {
          customLineLabel.textContent = axisKey === 'custom_v' ? 'Line x = c (c):' : 'Line y = c (c):';
        }

        updateReflectionUI();
      });
    });

    if (reflectConst) reflectConst.addEventListener('input', updateReflectionUI);
    if (applyReflectBtn) {
      applyReflectBtn.addEventListener('click', function () {
        updateReflectionUI();
        showToast('Reflection applied across selected mirror line!', '🪞', 1800);
      });
    }

    // --- Subpanel 3: Rotation Controls ---
    const rotAngleLabels = document.querySelectorAll('#panel-rotation [data-rotation-angle]');
    const rotCenterOrigin = document.getElementById('rotCenterOrigin');
    const rotCenterCustom = document.getElementById('rotCenterCustom');
    const applyRotateBtn = document.getElementById('applyRotateBtn');
    let selectedRotAngle = 90;
    let selectedRotClockwise = true;
    let rotCenter = { x: 0, y: 0 };

    function updateRotationUI() {
      if (currentMode === 'rotation') {
        window.GeometryEngine.setTransformation('rotation', {
          angle: Math.abs(selectedRotAngle),
          clockwise: selectedRotClockwise,
          cx: rotCenter.x,
          cy: rotCenter.y
        });
      }
    }

    rotAngleLabels.forEach(function (lbl) {
      lbl.addEventListener('click', function () {
        rotAngleLabels.forEach(function (l) { l.classList.remove('active'); });
        lbl.classList.add('active');

        const angleVal = parseInt(lbl.getAttribute('data-rotation-angle'), 10);
        if (angleVal === -90) {
          selectedRotAngle = 90;
          selectedRotClockwise = false; // CCW
        } else {
          selectedRotAngle = angleVal;
          selectedRotClockwise = true; // CW
        }
        updateRotationUI();
      });
    });

    if (rotCenterOrigin && rotCenterCustom) {
      rotCenterOrigin.addEventListener('click', function () {
        rotCenterOrigin.classList.add('active');
        rotCenterCustom.classList.remove('active');
        rotCenter = { x: 0, y: 0 };
        updateRotationUI();
      });
      rotCenterCustom.addEventListener('click', function () {
        rotCenterCustom.classList.add('active');
        rotCenterOrigin.classList.remove('active');
        rotCenter = { x: 1, y: 1 };
        updateRotationUI();
        showToast('Center of rotation set to (1, 1)', '📍', 1800);
      });
    }

    if (applyRotateBtn) {
      applyRotateBtn.addEventListener('click', function () {
        updateRotationUI();
        showToast('Rotation applied about center point!', '🔄', 1800);
      });
    }

    // --- Subpanel 4: Dilation Controls ---
    const dilationK = document.getElementById('dilationK');
    const valK = document.getElementById('valK');
    const dilationTypeBadge = document.getElementById('dilationTypeBadge');
    const applyDilateBtn = document.getElementById('applyDilateBtn');
    const kPresetButtons = document.querySelectorAll('#panel-dilation [data-k-preset]');

    function updateDilationUI() {
      const k = parseFloat(dilationK ? dilationK.value : '1.5');
      if (valK) valK.textContent = k.toFixed(2) + '×';

      if (dilationTypeBadge) {
        if (k > 1.0) {
          dilationTypeBadge.innerHTML = '<span class="badge-status-similar">🔍 Enlargement (\(k > 1\)) • Angles Preserved, Sides \(\times k\)</span>';
        } else if (k === 1.0) {
          dilationTypeBadge.innerHTML = '<span class="badge-status-congruent">✨ Identity (\(k = 1\)) • Exact Congruent Copy</span>';
        } else {
          dilationTypeBadge.innerHTML = '<span class="badge-status-similar">🔬 Reduction (\(0 < k < 1\)) • Angles Preserved, Sides \(\times k\)</span>';
        }
        renderMath(dilationTypeBadge);
      }

      if (applyDilateBtn) {
        applyDilateBtn.innerHTML = 'Apply Dilation \((' + k.toFixed(2) + 'x, ' + k.toFixed(2) + 'y)\)';
        renderMath(applyDilateBtn);
      }

      if (currentMode === 'dilation') {
        window.GeometryEngine.setTransformation('dilation', { scale: k, cx: 0, cy: 0 });
      }
    }

    if (dilationK) dilationK.addEventListener('input', updateDilationUI);

    kPresetButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        const val = parseFloat(btn.getAttribute('data-k-preset'));
        if (dilationK) {
          dilationK.value = val;
          updateDilationUI();
          showToast('Scale factor set to ' + val + '×', '🔍', 1500);
        }
      });
    });

    if (applyDilateBtn) {
      applyDilateBtn.addEventListener('click', function () {
        updateDilationUI();
        showToast('Dilation executed from center (0, 0)!', '📐', 1800);
      });
    }

    // --- Subpanel 5: Sequence Builder ---
    const sequenceStepList = document.getElementById('sequenceStepList');
    const addStepTranslateBtn = document.getElementById('addStepTranslateBtn');
    const addStepReflectBtn = document.getElementById('addStepReflectBtn');
    const addStepRotateBtn = document.getElementById('addStepRotateBtn');
    const addStepDilateBtn = document.getElementById('addStepDilateBtn');
    const runSequenceBtn = document.getElementById('runSequenceBtn');
    const clearSequenceBtn = document.getElementById('clearSequenceBtn');

    function renderSequenceStepList() {
      if (!sequenceStepList) return;
      sequenceStepList.innerHTML = '';

      sequenceSteps.forEach(function (step, index) {
        const item = document.createElement('div');
        item.className = 'sequence-item';
        item.setAttribute('data-step-index', index);
        item.innerHTML = 
          '<div class="sequence-step-left">' +
            '<div class="sequence-step-num">' + (index + 1) + '</div>' +
            '<div class="sequence-step-desc">' + step.label + '</div>' +
          '</div>' +
          '<button class="sequence-remove-btn" title="Remove Step" data-remove-step="' + index + '">✕</button>';
        sequenceStepList.appendChild(item);
      });

      renderMath(sequenceStepList);

      // Re-bind remove buttons
      sequenceStepList.querySelectorAll('.sequence-remove-btn').forEach(function (rBtn) {
        rBtn.addEventListener('click', function (e) {
          e.stopPropagation();
          const stepIdx = parseInt(rBtn.getAttribute('data-remove-step'), 10);
          if (sequenceSteps.length <= 1) {
            showToast('Keep at least 1 transformation in your sequence!', '⚠️', 2000);
            return;
          }
          sequenceSteps.splice(stepIdx, 1);
          renderSequenceStepList();
          applySequenceToEngine();
        });
      });
    }

    function applySequenceToEngine() {
      if (currentMode === 'sequence') {
        window.GeometryEngine.setSequence(sequenceSteps);
      }
    }

    if (addStepTranslateBtn) {
      addStepTranslateBtn.addEventListener('click', function () {
        if (sequenceSteps.length >= 5) {
          showToast('Maximum 5 sequence steps allowed.', '⚠️', 2000);
          return;
        }
        const dx = parseInt(transDx ? transDx.value : '3', 10);
        const dy = parseInt(transDy ? transDy.value : '2', 10);
        sequenceSteps.push({
          type: 'translation',
          params: { dx: dx, dy: dy },
          label: 'Translate: ⟨' + (dx >= 0 ? '+' + dx : dx) + ', ' + (dy >= 0 ? '+' + dy : dy) + '⟩'
        });
        renderSequenceStepList();
        applySequenceToEngine();
        showToast('Translation step added to sequence!', '⛓️', 1500);
      });
    }

    if (addStepReflectBtn) {
      addStepReflectBtn.addEventListener('click', function () {
        if (sequenceSteps.length >= 5) {
          showToast('Maximum 5 sequence steps allowed.', '⚠️', 2000);
          return;
        }
        sequenceSteps.push({
          type: 'reflection',
          params: { axis: 'x-axis' },
          label: 'Reflect across x-axis'
        });
        renderSequenceStepList();
        applySequenceToEngine();
        showToast('Reflection step added to sequence!', '🪞', 1500);
      });
    }

    if (addStepRotateBtn) {
      addStepRotateBtn.addEventListener('click', function () {
        if (sequenceSteps.length >= 5) {
          showToast('Maximum 5 sequence steps allowed.', '⚠️', 2000);
          return;
        }
        sequenceSteps.push({
          type: 'rotation',
          params: { angle: 90, clockwise: true, cx: 0, cy: 0 },
          label: 'Rotate 90° CW about Origin'
        });
        renderSequenceStepList();
        applySequenceToEngine();
        showToast('Rotation step added to sequence!', '🔄', 1500);
      });
    }

    if (addStepDilateBtn) {
      addStepDilateBtn.addEventListener('click', function () {
        if (sequenceSteps.length >= 5) {
          showToast('Maximum 5 sequence steps allowed.', '⚠️', 2000);
          return;
        }
        const k = parseFloat(dilationK ? dilationK.value : '1.5');
        sequenceSteps.push({
          type: 'dilation',
          params: { scale: k, cx: 0, cy: 0 },
          label: 'Dilate by \(k = ' + k.toFixed(2) + '\)'
        });
        renderSequenceStepList();
        applySequenceToEngine();
        showToast('Dilation step added to sequence!', '🔍', 1500);
      });
    }

    if (runSequenceBtn) {
      runSequenceBtn.addEventListener('click', function () {
        playSequenceAnimation();
      });
    }

    if (clearSequenceBtn) {
      clearSequenceBtn.addEventListener('click', function () {
        sequenceSteps = [
          { type: 'translation', params: { dx: 3, dy: 2 }, label: 'Translate: ⟨+3, +2⟩' }
        ];
        renderSequenceStepList();
        applySequenceToEngine();
        showToast('Sequence reset to default.', '🗑️', 1500);
      });
    }

    function playSequenceAnimation() {
      applySequenceToEngine();
      window.GeometryEngine.playSequence();
      showToast('▶ Playing transformation sequence...', '🎬', 2000);
    }

    function playSingleTransformAnimation() {
      showToast('Visualizing transformation vectors...', '✨', 1800);
      window.GeometryEngine.recalculateAndNotify();
    }

    function applyCurrentTransformation() {
      if (currentMode === 'translation') {
        updateTranslationUI();
      } else if (currentMode === 'reflection') {
        updateReflectionUI();
      } else if (currentMode === 'rotation') {
        updateRotationUI();
      } else if (currentMode === 'dilation') {
        updateDilationUI();
      } else if (currentMode === 'sequence') {
        applySequenceToEngine();
      }
    }

    // Initial setup
    renderSequenceStepList();
    updateTranslationUI();
  }

  // --- 7. LIVE METRICS & COORDINATES SYNCHRONIZER ---
  function handleGeometryUpdate(state) {
    if (!state) return;

    // 1. Live Algebraic Mapping Rule
    const ruleFormulaEl = document.getElementById('mappingRuleFormula');
    if (ruleFormulaEl && state.transformationRule) {
      renderFormulaLatex('mappingRuleFormula', state.transformationRule);
    }

    // 2. Isometry / Congruence Status Indicator
    const isometryStatus = document.getElementById('isometryStatus');
    if (isometryStatus) {
      const isCongruent = Math.abs((state.areaRatio || 1) - 1.0) < 0.05 && Math.abs((state.perimeterRatio || 1) - 1.0) < 0.05;
      if (isCongruent) {
        isometryStatus.innerHTML = '<span class="badge-status-congruent">✨ Rigid Motion • Congruent Figures (\(\cong\))</span>';
      } else {
        isometryStatus.innerHTML = '<span class="badge-status-similar">🔍 Similarity Transformation • Similar Figures (\(\sim\)) • Sides in Ratio ' + state.perimeterRatio + '</span>';
      }
      renderMath(isometryStatus);
    }

    // 3. Live Coordinates Table Body
    const coordsTableBody = document.getElementById('coordsTableBody');
    if (coordsTableBody && state.preimageVertices && state.imageVertices) {
      coordsTableBody.innerHTML = '';
      const labels = state.labels || [];

      for (let i = 0; i < state.preimageVertices.length; i++) {
        const pre = state.preimageVertices[i];
        const post = state.imageVertices[i] || { x: 0, y: 0 };
        const lbl = labels[i] || String.fromCharCode(65 + i);

        const tr = document.createElement('tr');
        tr.innerHTML = 
          '<td><span class="badge-pre">' + lbl + '</span> (' + pre.x + ', ' + pre.y + ')</td>' +
          '<td style="text-align: center; color: var(--text-muted);">➔</td>' +
          '<td><span class="badge-post">' + lbl + "'" + '</span> (' + post.x + ', ' + post.y + ')</td>';
        coordsTableBody.appendChild(tr);
      }
    }

    // 4. Perimeter Ratio & Area Ratio Meters
    const perimeterRatioEl = document.getElementById('perimeterRatio');
    const imagePerimeterEl = document.getElementById('imagePerimeter');
    const preimagePerimeterEl = document.getElementById('preimagePerimeter');
    const perimeterBarFill = document.getElementById('perimeterBarFill');

    if (perimeterRatioEl) perimeterRatioEl.textContent = (state.perimeterRatio || 1).toFixed(2) + '×';
    if (imagePerimeterEl) imagePerimeterEl.textContent = state.postPerimeter || '—';
    if (preimagePerimeterEl) preimagePerimeterEl.textContent = state.prePerimeter || '—';
    if (perimeterBarFill) {
      const pPct = Math.min(100, Math.max(10, Math.round((state.perimeterRatio || 1) * 33.3)));
      perimeterBarFill.style.width = pPct + '%';
    }

    const areaRatioEl = document.getElementById('areaRatio');
    const imageAreaEl = document.getElementById('imageArea');
    const preimageAreaEl = document.getElementById('preimageArea');
    const areaBarFill = document.getElementById('areaBarFill');

    if (areaRatioEl) areaRatioEl.textContent = (state.areaRatio || 1).toFixed(2) + '×';
    if (imageAreaEl) imageAreaEl.textContent = state.postArea || '—';
    if (preimageAreaEl) preimageAreaEl.textContent = state.preArea || '—';
    if (areaBarFill) {
      const aPct = Math.min(100, Math.max(10, Math.round((state.areaRatio || 1) * 25)));
      areaBarFill.style.width = aPct + '%';
    }

    // 5. Hero Banner Real-time Stats
    const bannerPreserved = document.getElementById('bannerPreservedLabel');
    const bannerScale = document.getElementById('bannerScaleFactor');
    const bannerVerts = document.getElementById('bannerVerticesCount');
    const bannerArea = document.getElementById('bannerAreaRatio');

    if (bannerPreserved) {
      const isRigid = Math.abs((state.perimeterRatio || 1) - 1.0) < 0.05;
      bannerPreserved.textContent = isRigid ? 'Congruent (≅)' : 'Similar (~)';
    }
    if (bannerScale) bannerScale.textContent = (state.perimeterRatio || 1.0).toFixed(2) + '×';
    if (bannerVerts) bannerVerts.textContent = (state.preimageVertices ? state.preimageVertices.length : 3);
    if (bannerArea) bannerArea.textContent = (state.areaRatio || 1.0).toFixed(2) + '×';
  }

  // --- 8. "TRY IN SANDBOX" LESSON DEEP-LINKING ---
  function initLessonCardLinks() {
    document.addEventListener('click', function (e) {
      const btn = e.target.closest('.try-live-btn, [data-lesson-target]');
      if (!btn) return;
      e.preventDefault();
      const targetLesson = btn.getAttribute('data-lesson-target');
      if (targetLesson) {
        launchLessonInSandbox(targetLesson);
      }
    });
  }

  function launchLessonInSandbox(lessonId) {
    // 1. Switch to Sandbox Tab
    switchTab('tab-sandbox');

    const shapeSelect = document.getElementById('shapeSelect') || document.getElementById('presetShapeSelect');
    const btnModeTranslate = document.getElementById('btnModeTranslate');
    const btnModeReflect = document.getElementById('btnModeReflect');
    const btnModeRotate = document.getElementById('btnModeRotate');
    const btnModeDilate = document.getElementById('btnModeDilate');
    const btnModeSequence = document.getElementById('btnModeSequence');

    const transDx = document.getElementById('transDx');
    const transDy = document.getElementById('transDy');
    const dilationK = document.getElementById('dilationK');

    // 2. Configure transformation specific to lesson pedagogy
    switch (lessonId) {
      case '1.1': // Investigate Transformations (Rigid Motions)
        if (shapeSelect) shapeSelect.value = 'triangle';
        if (btnModeTranslate) btnModeTranslate.click();
        if (transDx) transDx.value = 3;
        if (transDy) transDy.value = 2;
        transDx.dispatchEvent(new Event('input'));
        showToast('📘 Lesson 1.1 Loaded: Observe how side lengths & angles are strictly preserved!', '✨', 3500);
        break;

      case '1.2': // Explore Translations
        if (shapeSelect) shapeSelect.value = 'triangle';
        if (btnModeTranslate) btnModeTranslate.click();
        if (transDx) transDx.value = 4;
        if (transDy) transDy.value = -3;
        transDx.dispatchEvent(new Event('input'));
        showToast('📘 Lesson 1.2 Loaded: Translation vector ⟨+4, -3⟩ applied with mapping rule!', '🚀', 3500);
        break;

      case '1.3': // Explore Reflections
        if (shapeSelect) shapeSelect.value = 'mariamM';
        if (shapeSelect) shapeSelect.dispatchEvent(new Event('change'));
        if (btnModeReflect) btnModeReflect.click();
        const xAxisRadio = document.querySelector('#panel-reflection [data-reflect-axis="x"]');
        if (xAxisRadio) xAxisRadio.click();
        showToast("📘 Lesson 1.3 Loaded: Letter 'M' reflected across x-axis. Notice orientation flip!", '🪞', 3500);
        break;

      case '1.4': // Explore Rotations
        if (shapeSelect) shapeSelect.value = 'triangle';
        if (shapeSelect) shapeSelect.dispatchEvent(new Event('change'));
        if (btnModeRotate) btnModeRotate.click();
        const rot90Radio = document.querySelector('#panel-rotation [data-rotation-angle="90"]');
        if (rot90Radio) rot90Radio.click();
        showToast('📘 Lesson 1.4 Loaded: 90° Clockwise Rotation around origin (y, -x)!', '🔄', 3500);
        break;

      case '1.5': // Congruent Figures
        if (shapeSelect) shapeSelect.value = 'quadrilateral';
        if (shapeSelect) shapeSelect.dispatchEvent(new Event('change'));
        if (btnModeSequence) btnModeSequence.click();
        showToast('📘 Lesson 1.5 Loaded: Sequence of rigid motions proving figure congruence (≅)!', '⛓️', 3500);
        setTimeout(function () {
          const runBtn = document.getElementById('runSequenceBtn');
          if (runBtn) runBtn.click();
        }, 400);
        break;

      case '2.1': // Reductions and Enlargements
        if (shapeSelect) shapeSelect.value = 'triangle';
        if (shapeSelect) shapeSelect.dispatchEvent(new Event('change'));
        if (btnModeDilate) btnModeDilate.click();
        if (dilationK) dilationK.value = 2.0;
        dilationK.dispatchEvent(new Event('input'));
        showToast('📐 Lesson 2.1 Loaded: Scale factor k = 2.0 (Enlargement: shape expands from origin)!', '🔍', 3500);
        break;

      case '2.2': // Explore Dilations & Area Squaring Rule
        if (shapeSelect) shapeSelect.value = 'house';
        if (shapeSelect) shapeSelect.dispatchEvent(new Event('change'));
        if (btnModeDilate) btnModeDilate.click();
        if (dilationK) dilationK.value = 1.5;
        dilationK.dispatchEvent(new Event('input'));
        showToast('📐 Lesson 2.2 Loaded: Dilation k = 1.5. Notice: Perimeter ×1.5, Area ×2.25 (k²)!', '🌟', 3500);
        break;

      case '2.3': // Similar Figures Sequence
        if (shapeSelect) shapeSelect.value = 'triangle';
        if (shapeSelect) shapeSelect.dispatchEvent(new Event('change'));
        if (btnModeSequence) btnModeSequence.click();
        showToast('📐 Lesson 2.3 Loaded: Sequence of rigid motion + dilation proving similarity (~)!', '🎯', 3500);
        break;

      default:
        if (btnModeTranslate) btnModeTranslate.click();
        showToast('Switched to Interactive Geometry Sandbox', '📐', 2000);
    }
  }

  // --- 9. QUIZ ARENA INTEGRATION ---
  function initQuizArenaWiring() {
    const modeBtnMod1 = document.getElementById('quizModeMod1');
    const modeBtnMod2 = document.getElementById('quizModeMod2');
    const modeBtnGrand = document.getElementById('quizModeGrand');

    const quizModeButtons = [modeBtnMod1, modeBtnMod2, modeBtnGrand].filter(Boolean);

    quizModeButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        quizModeButtons.forEach(function (b) {
          b.classList.remove('btn-primary');
          b.classList.add('btn-secondary');
        });
        btn.classList.remove('btn-secondary');
        btn.classList.add('btn-primary');

        const mode = btn.getAttribute('data-quiz-mode') || 'mod1';
        if (window.QuizArena && typeof window.QuizArena.startQuiz === 'function') {
          window.QuizArena.startQuiz(mode);
          showToast('Starting ' + btn.textContent.trim(), '⚔️', 2000);
        }
      });
    });

    // Sound toggle button in header
    const soundToggleBtn = document.getElementById('soundToggleBtn');
    if (soundToggleBtn) {
      soundToggleBtn.addEventListener('click', function () {
        if (window.QuizArena && typeof window.QuizArena.getAudioEngine === 'function') {
          const audioEngine = window.QuizArena.getAudioEngine();
          audioEngine.toggleMute();
          const isMuted = audioEngine.getMuted();
          soundToggleBtn.textContent = isMuted ? '🔇' : '🔊';
          showToast(isMuted ? 'Sound muted' : 'Sound enabled 🔊', isMuted ? '🔇' : '🔊', 1500);
        }
      });
    }
  }

  // --- 10. STUDY HUB NOTEPAD PERSISTENCE ---
  const NOTES_STORAGE_KEY = 'mariam_study_notes';

  function initStudyNotepad() {
    const notesArea = document.getElementById('mariamNotesArea');
    const notesStatus = document.getElementById('notesSaveStatus');
    const quickButtons = document.querySelectorAll('.notes-quick-buttons [data-insert-note]');

    if (!notesArea) return;

    // Load saved notes
    try {
      const savedNotes = localStorage.getItem(NOTES_STORAGE_KEY);
      if (savedNotes !== null) {
        notesArea.value = savedNotes;
      }
    } catch (e) {
      console.warn('Could not read notes from localStorage:', e);
    }

    // Auto-save debounced
    let saveTimeout = null;
    notesArea.addEventListener('input', function () {
      if (notesStatus) notesStatus.textContent = 'Saving notes...';
      if (saveTimeout) clearTimeout(saveTimeout);
      saveTimeout = setTimeout(function () {
        try {
          localStorage.setItem(NOTES_STORAGE_KEY, notesArea.value);
          if (notesStatus) {
            notesStatus.textContent = '✓ Notes automatically saved';
            notesStatus.style.color = 'var(--success)';
          }
        } catch (e) {
          if (notesStatus) notesStatus.textContent = '⚠️ Storage unavailable';
        }
      }, 400);
    });

    // Quick Insert Buttons
    quickButtons.forEach(function (qBtn) {
      qBtn.addEventListener('click', function () {
        const textToInsert = qBtn.getAttribute('data-insert-note');
        if (!textToInsert) return;

        const start = notesArea.selectionStart || notesArea.value.length;
        const end = notesArea.selectionEnd || notesArea.value.length;
        const before = notesArea.value.substring(0, start);
        const after = notesArea.value.substring(end);

        notesArea.value = before + ' ' + textToInsert + ' ' + after;
        notesArea.focus();
        notesArea.selectionStart = notesArea.selectionEnd = start + textToInsert.length + 2;

        notesArea.dispatchEvent(new Event('input'));
        showToast('Inserted formula snippet: ' + textToInsert, '📝', 1500);
      });
    });

    // Print Button
    // Print Button
    const printBtn = document.getElementById('printCheatSheetBtn');
    if (printBtn) {
      printBtn.addEventListener('click', function () {
        window.print();
      });
    }
  }

  // --- 11. LESSON NAVIGATION CONTROLLER ---
  function showLesson(lessonId) {
    if (!lessonId) return;

    // Switch to lessons tab if not currently active
    if (currentActiveTab !== 'tab-lessons') {
      switchTab('tab-lessons');
    }

    // Hide all lesson panels and activate targeted one
    const allPanels = document.querySelectorAll('.lesson-view-panel');
    let targetPanel = null;
    allPanels.forEach(function (panel) {
      if (panel.getAttribute('data-lesson-id') === lessonId) {
        panel.classList.add('active');
        targetPanel = panel;
      } else {
        panel.classList.remove('active');
      }
    });

    // Update Quick Jump Pills
    const allPills = document.querySelectorAll('.lesson-jump-btn');
    allPills.forEach(function (pill) {
      if (pill.getAttribute('data-lesson-id') === lessonId) {
        pill.classList.add('active');
        try {
          pill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
        } catch (e) {}
      } else {
        pill.classList.remove('active');
      }
    });

    // Update active module card highlight
    const isMod1 = lessonId.startsWith('1.');
    const cardMod1 = document.getElementById('cardModule1');
    const cardMod2 = document.getElementById('cardModule2');
    if (cardMod1 && cardMod2) {
      if (isMod1) {
        cardMod1.classList.add('active');
        cardMod2.classList.remove('active');
      } else {
        cardMod1.classList.remove('active');
        cardMod2.classList.add('active');
      }
    }

    window.currentActiveLessonId = lessonId;

    // Render KaTeX inside target panel
    if (targetPanel) {
      renderMath(targetPanel);
    }
  }
  window.showLesson = showLesson;

  function initLessonNavigation() {
    document.addEventListener('click', function (e) {
      // 1. Quick Jump Button
      const jumpBtn = e.target.closest('.lesson-jump-btn');
      if (jumpBtn) {
        const lesId = jumpBtn.getAttribute('data-lesson-id');
        if (lesId) showLesson(lesId);
        return;
      }

      // 2. Module Card Jump Button (data-jump-mod)
      const modJumpBtn = e.target.closest('[data-jump-mod]');
      if (modJumpBtn) {
        const lesId = modJumpBtn.getAttribute('data-jump-mod');
        if (lesId) showLesson(lesId);
        return;
      }

      // 3. Module Overview Card Body Click
      const modCard = e.target.closest('.module-overview-card');
      if (modCard && !e.target.closest('button')) {
        const isMod1 = modCard.classList.contains('mod1-card') || modCard.getAttribute('data-module-id') === 'mod1';
        showLesson(isMod1 ? '1.1' : '2.1');
        return;
      }

      // 4. Previous / Next Lesson Button
      const navBtn = e.target.closest('.btn-nav-lesson');
      if (navBtn) {
        const targetLesson = navBtn.getAttribute('data-target-lesson');
        if (targetLesson) {
          showLesson(targetLesson);
          const hero = document.querySelector('.lesson-view-panel.active .lesson-view-hero');
          if (hero) {
            try { hero.scrollIntoView({ behavior: 'smooth' }); } catch (err) {}
          } else {
            try { window.scrollTo({ top: 350, behavior: 'smooth' }); } catch (err) {}
          }
        }
        return;
      }
    });
  }

  // --- 12. PRACTICE QUESTION CHECKERS (MCQ & FITB) ---
  function initPracticeCheckers() {
    // 1. Option selection in MCQs
    document.addEventListener('click', function (e) {
      const optBtn = e.target.closest('.practice-opt-btn');
      if (!optBtn) return;
      if (e._optHandled) return;
      e._optHandled = true;
      const grid = optBtn.closest('.practice-options-grid');
      if (!grid) return;
      grid.querySelectorAll('.practice-opt-btn').forEach(function (b) {
        b.classList.remove('selected', 'wrong', 'incorrect');
      });
      optBtn.classList.add('selected');
      const card = optBtn.closest('.practice-question-card');
      if (card) {
        const feedback = card.querySelector('.practice-feedback');
        if (feedback && (feedback.classList.contains('wrong') || feedback.classList.contains('warn'))) {
          feedback.style.display = 'none';
        }
      }
    });

    // 2. Hint toggle
    document.addEventListener('click', function (e) {
      const hintBtn = e.target.closest('.btn-hint-toggle');
      if (!hintBtn) return;
      if (e._hintHandled) return;
      e._hintHandled = true;
      const card = hintBtn.closest('.practice-question-card');
      if (!card) return;
      const hintCard = card.querySelector('.hint-card');
      if (!hintCard) return;

      const isHidden = (window.getComputedStyle ? window.getComputedStyle(hintCard).display : hintCard.style.display) === 'none' || hintCard.style.display === 'none' || !hintCard.style.display;
      if (isHidden) {
        hintCard.style.display = 'block';
        hintBtn.textContent = '🙈 Hide Hint';
      } else {
        hintCard.style.display = 'none';
        hintBtn.textContent = '💡 Need a Hint?';
      }
      if (typeof window.recordQuestionAttempt === 'function') {
        window.recordQuestionAttempt(false, true);
      }
    });

    // 3. Check MCQ Answer
    document.addEventListener('click', function (e) {
      const checkBtn = e.target.closest('.btn-check-mcq');
      if (!checkBtn) return;
      if (e._checkMcqHandled) return;
      e._checkMcqHandled = true;
      const card = checkBtn.closest('.practice-question-card');
      if (!card) return;
      const correctIndex = parseInt(card.getAttribute('data-correct'), 10);
      const selectedOpt = card.querySelector('.practice-opt-btn.selected');
      const feedback = card.querySelector('.practice-feedback');

      if (!selectedOpt) {
        if (feedback) {
          feedback.className = 'practice-feedback warn';
          feedback.innerHTML = '⚠️ Please select an option first!';
          feedback.style.display = 'block';
        }
        return;
      }

      const selectedIndex = parseInt(selectedOpt.getAttribute('data-opt-index'), 10);
      if (selectedIndex === correctIndex) {
        selectedOpt.classList.remove('wrong', 'incorrect');
        selectedOpt.classList.add('correct');
        card.setAttribute('data-is-correct', 'true');
        if (feedback) {
          feedback.className = 'practice-feedback correct';
          feedback.innerHTML = '🎉 <strong>Correct!</strong> Outstanding work, Mariam! (+10 XP)';
          feedback.style.display = 'block';
        }
        if (window.confetti) {
          window.confetti({ particleCount: 40, spread: 65, origin: { y: 0.7 } });
        }
        if (window.QuizArena && typeof window.QuizArena.getAudioEngine === 'function') {
          try { window.QuizArena.getAudioEngine().playCorrect(); } catch (err) {}
        }
        addXP(10);
        if (typeof window.recordQuestionAttempt === 'function') {
          window.recordQuestionAttempt(true, false);
        }
        showToast('Superb! +10 XP earned! 🌟', '🎉', 2200);
      } else {
        selectedOpt.classList.remove('correct');
        selectedOpt.classList.add('wrong', 'incorrect');
        card.setAttribute('data-is-correct', 'false');
        if (feedback) {
          feedback.className = 'practice-feedback wrong';
          feedback.innerHTML = '✕ <strong>Not quite!</strong> Review the hint above and try again!';
          feedback.style.display = 'block';
        }
        // Auto-reveal hint
        const hintCard = card.querySelector('.hint-card');
        if (hintCard) {
          hintCard.style.display = 'block';
          const hintBtn = card.querySelector('.btn-hint-toggle');
          if (hintBtn) hintBtn.textContent = '🙈 Hide Hint';
        }
        if (window.QuizArena && typeof window.QuizArena.getAudioEngine === 'function') {
          try { window.QuizArena.getAudioEngine().playWrong(); } catch (err) {}
        }
        if (typeof window.recordQuestionAttempt === 'function') {
          window.recordQuestionAttempt(false, false);
        }
      }
    });

    // 4. Check Fill-in-the-Blank Answer
    function checkFitb(card) {
      if (!card) return;
      const input = card.querySelector('.fitb-input');
      const feedback = card.querySelector('.practice-feedback');
      if (!input) return;

      const rawVal = input.value;
      if (!rawVal || !rawVal.trim()) {
        if (feedback) {
          feedback.className = 'practice-feedback warn';
          feedback.innerHTML = '⚠️ Please enter an answer before checking!';
          feedback.style.display = 'block';
        }
        return;
      }

      function cleanStr(s) {
        if (!s) return '';
        return String(s)
          .toLowerCase()
          .trim()
          .replace(/[\(\)\[\]\{\}<>]/g, '')
          .replace(/\s+/g, '')
          .replace(/degrees?|°/g, '')
          .replace(/units?$/g, '');
      }

      const userClean = cleanStr(rawVal);
      const expectedRaw = card.getAttribute('data-expected') || '';
      const expectedClean = cleanStr(expectedRaw);
      let alts = [];
      try {
        alts = JSON.parse(card.getAttribute('data-alts') || '[]');
      } catch (err) {}

      let isMatch = (userClean === expectedClean) || alts.some(function (a) {
        return cleanStr(a) === userClean;
      });

      // Numeric check fallback
      if (!isMatch) {
        const uNum = parseFloat(rawVal.trim().replace(/degrees?|°/g, ''));
        const eNum = parseFloat(expectedRaw.trim().replace(/degrees?|°/g, ''));
        if (!isNaN(uNum) && !isNaN(eNum) && Math.abs(uNum - eNum) < 0.001) {
          isMatch = true;
        }
        if (!isMatch) {
          for (let i = 0; i < alts.length; i++) {
            const aNum = parseFloat(String(alts[i]).trim().replace(/degrees?|°/g, ''));
            if (!isNaN(uNum) && !isNaN(aNum) && Math.abs(uNum - aNum) < 0.001) {
              isMatch = true;
              break;
            }
          }
        }
      }

      if (isMatch) {
        input.classList.remove('input-wrong');
        input.classList.add('input-correct');
        card.setAttribute('data-is-correct', 'true');
        if (feedback) {
          feedback.className = 'practice-feedback correct';
          feedback.innerHTML = '🎉 <strong>Correct!</strong> Perfect coordinate entry, Mariam! (+15 XP)';
          feedback.style.display = 'block';
        }
        if (window.confetti) {
          window.confetti({ particleCount: 45, spread: 65, origin: { y: 0.7 } });
        }
        if (window.QuizArena && typeof window.QuizArena.getAudioEngine === 'function') {
          try { window.QuizArena.getAudioEngine().playCorrect(); } catch (err) {}
        }
        addXP(15);
        if (typeof window.recordQuestionAttempt === 'function') {
          window.recordQuestionAttempt(true, false);
        }
        showToast('Spot on, Mariam! +15 XP earned! 🌟', '🎉', 2200);
      } else {
        input.classList.remove('input-correct');
        input.classList.add('input-wrong');
        card.setAttribute('data-is-correct', 'false');
        if (feedback) {
          feedback.className = 'practice-feedback wrong';
          feedback.innerHTML = '✕ <strong>Check your values!</strong> Check sign (+/-) or numbers and try again!';
          feedback.style.display = 'block';
        }
        const hintCard = card.querySelector('.hint-card');
        if (hintCard) {
          hintCard.style.display = 'block';
          const hintBtn = card.querySelector('.btn-hint-toggle');
          if (hintBtn) hintBtn.textContent = '🙈 Hide Hint';
        }
        if (window.QuizArena && typeof window.QuizArena.getAudioEngine === 'function') {
          try { window.QuizArena.getAudioEngine().playWrong(); } catch (err) {}
        }
        if (typeof window.recordQuestionAttempt === 'function') {
          window.recordQuestionAttempt(false, false);
        }
      }
    }

    document.addEventListener('click', function (e) {
      const checkBtn = e.target.closest('.btn-check-fitb');
      if (!checkBtn) return;
      const card = checkBtn.closest('.practice-question-card');
      checkFitb(card);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        const input = e.target.closest('.fitb-input');
        if (input) {
          const card = input.closest('.practice-question-card');
          checkFitb(card);
        }
      }
    });
  }

  // --- 13. BOOK QUESTIONS MODEL ANSWERS ---
  function initBookQuestions() {
    document.addEventListener('click', function (e) {
      const btn = e.target.closest('.btn-toggle-model-answer');
      if (!btn) return;
      const card = btn.closest('.book-question-card');
      if (!card) return;
      const answerCard = card.querySelector('.book-model-answer-card');
      if (!answerCard) return;

      const isHidden = (window.getComputedStyle ? window.getComputedStyle(answerCard).display : answerCard.style.display) === 'none' || answerCard.style.display === 'none' || !answerCard.style.display;
      if (isHidden) {
        answerCard.style.display = 'block';
        btn.textContent = '🙈 Hide Model Answer';
        btn.classList.add('btn-active');
        renderMath(answerCard);
      } else {
        answerCard.style.display = 'none';
        btn.textContent = '👁️ Show Model Answer';
        btn.classList.remove('btn-active');
      }
    });
  }

  // --- 14. QUESTION BANK FILTERING ---
  function initQuestionBank() {
    document.addEventListener('click', function (e) {
      const btn = e.target.closest('.qbank-filter-btn');
      if (!btn) return;
      document.querySelectorAll('.qbank-filter-btn').forEach(function (b) {
        b.classList.remove('active');
      });
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');
      const cards = document.querySelectorAll('#qbankGrid .book-question-card');
      cards.forEach(function (card) {
        if (filter === 'all' || card.getAttribute('data-mod') === filter) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  }

  // --- 15. HEADER CONTROLS (PHOTO UPLOAD, AUDIO, PRINT) ---
  const PHOTO_STORAGE_KEY = 'mariam_profile_photo_v2';

  function initHeaderControls() {
    const photoInput = document.getElementById('mariamPhotoInput');
    const photoImg = document.getElementById('mariamPhotoImg');
    const avatarPlaceholder = document.getElementById('mariamAvatarPlaceholder');
    const removePhotoBtn = document.getElementById('removePhotoBtn');

    // Load saved photo
    try {
      const savedPhoto = localStorage.getItem(PHOTO_STORAGE_KEY);
      if (savedPhoto && photoImg) {
        photoImg.src = savedPhoto;
        photoImg.style.display = 'block';
        if (avatarPlaceholder) avatarPlaceholder.style.display = 'none';
        if (removePhotoBtn) removePhotoBtn.style.display = 'inline-block';
      }
    } catch (e) {}

    // Upload photo
    if (photoInput) {
      photoInput.addEventListener('change', function (e) {
        const file = e.target.files && e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function (evt) {
          const dataUrl = evt.target.result;
          if (photoImg) {
            photoImg.src = dataUrl;
            photoImg.style.display = 'block';
          }
          if (avatarPlaceholder) avatarPlaceholder.style.display = 'none';
          if (removePhotoBtn) removePhotoBtn.style.display = 'inline-block';
          try {
            localStorage.setItem(PHOTO_STORAGE_KEY, dataUrl);
            showToast("Looking brilliant, Mariam! Your photo is saved! 🌟", "📸", 3500);
          } catch (err) {}
        };
        reader.readAsDataURL(file);
      });
    }

    // Reset photo
    document.addEventListener('click', function (e) {
      const resetBtn = e.target.closest('#removePhotoBtn');
      if (!resetBtn) return;
      try {
        localStorage.removeItem(PHOTO_STORAGE_KEY);
      } catch (e) {}
      if (photoImg) {
        photoImg.src = '';
        photoImg.style.display = 'none';
      }
      if (avatarPlaceholder) avatarPlaceholder.style.display = 'flex';
      resetBtn.style.display = 'none';
      showToast("Avatar reset to monogram", "↺", 2000);
    });

    // Sound FX toggle
    document.addEventListener('click', function (e) {
      const soundBtn = e.target.closest('#soundToggleBtn');
      if (!soundBtn) return;
      let isMuted = false;
      if (window.QuizArena && typeof window.QuizArena.getAudioEngine === 'function') {
        const engine = window.QuizArena.getAudioEngine();
        isMuted = engine.toggleMute();
      } else {
        window.__soundMuted = !window.__soundMuted;
        isMuted = window.__soundMuted;
      }
      soundBtn.textContent = isMuted ? '🔇' : '🔊';
      showToast(isMuted ? 'Sound muted' : 'Sound enabled 🔊', isMuted ? '🔇' : '🔊', 1500);
    });

    // Universal Print button delegation
    document.addEventListener('click', function (e) {
      const printBtn = e.target.closest('#headerPrintBtn, #printCheatSheetBtn, #printAnalyticsBtn');
      if (printBtn) {
        window.print();
      }
    });
  }

  // --- 16. INITIALIZATION DISPATCHER ---
  function initApp() {
    console.log("[Dashboard] Initializing Mariam Hisham AbdelFadil's Grade 8 Into Math Dashboard...");

    initTabNavigation();
    initGeometryController();
    initLessonCardLinks();
    initQuizArenaWiring();
    initStudyNotepad();
    initLessonNavigation();
    initPracticeCheckers();
    initBookQuestions();
    initQuestionBank();
    initHeaderControls();
    syncProfileAndBadgesUI();

    // Trigger initial KaTeX rendering over static elements
    setTimeout(function () {
      renderMath(document.body);
    }, 150);

    // Friendly greeting toast for Mariam!
    setTimeout(function () {
      showToast('Welcome to your Math Dashboard, Mariam! Ready to master Transformations?', '🌟', 4000);
    }, 600);
  }

  // Global exports for cross-module access
  window.showLesson = showLesson;
  window.launchLessonInSandbox = launchLessonInSandbox;
  window.switchTab = switchTab;
  window.addXP = addXP;
  window.syncProfileAndBadgesUI = syncProfileAndBadgesUI;
  window.showToast = showToast;

  // Bind to DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

})(window, document);
