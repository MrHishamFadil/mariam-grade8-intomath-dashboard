/**
 * ============================================================================
 * MARIAM HISHAM ABDELFADIL - GRADE 8 INTO MATH INTERACTIVE DASHBOARD
 * Interactive Coordinate Geometry Engine (HTML5 Canvas)
 * File: geometry-engine.js
 * 
 * Capabilities:
 *  1. High-DPI / Retina Canvas Scaling (window.devicePixelRatio)
 *  2. Infinite-feel Cartesian Coordinate System with Pan & Zoom
 *  3. Interactive Pre-built Shapes & Draggable Vertices with Grid Snapping
 *  4. Rigorous Mathematical Transformations (Translation, Reflection, Rotation, Dilation)
 *  5. Educational Visual Aids (Motion vectors, mirror lines, rotation arcs, projection rays)
 *  6. Multi-Step Transformation Sequence Pipeline with Animated Playback
 *  7. Real-Time Math Metrics (Perimeter ratio, area ratio, coordinate tables, algebraic rules)
 * ============================================================================
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.GeometryEngine = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // --- Constants & Color Themes ---
  const THEME = {
    grid: {
      background: '#ffffff',
      majorLine: '#cbd5e1',
      minorLine: '#f1f5f9',
      axis: '#1e293b',
      subtleText: '#64748b',
      axisLabel: '#0f172a'
    },
    preimage: {
      stroke: '#6366f1',       // Indigo
      fill: 'rgba(99, 102, 241, 0.18)',
      vertexFill: '#ffffff',
      vertexBorder: '#4f46e5',
      vertexHover: '#4338ca',
      labelColor: '#3730a3',
      badgeBg: 'rgba(224, 231, 255, 0.92)',
      badgeBorder: '#c7d2fe'
    },
    image: {
      stroke: '#ec4899',       // Pink / Rose
      fill: 'rgba(236, 72, 153, 0.20)',
      vertexFill: '#ffffff',
      vertexBorder: '#db2777',
      vertexHover: '#be185d',
      labelColor: '#9d174d',
      badgeBg: 'rgba(252, 231, 243, 0.92)',
      badgeBorder: '#fbcfe8'
    },
    intermediate: {
      stroke: '#0ea5e9',       // Cyan / Sky
      fill: 'rgba(14, 165, 233, 0.14)',
      vertexBorder: '#0284c7'
    },
    helpers: {
      vector: '#8b5cf6',       // Purple vector arrows
      mirrorLine: '#0284c7',   // Ocean mirror line
      mirrorGlow: 'rgba(14, 165, 233, 0.35)',
      projLine: '#f59e0b',     // Amber projections
      rotationArc: '#10b981',  // Emerald rotation arcs
      dilationRay: '#d946ef',  // Fuchsia rays
      centerPoint: '#ef4444'   // Red center point
    }
  };

  // Pre-defined Shape Library for Grade 8 Geometry
  const SHAPE_PRESETS = {
    triangle: {
      name: 'Triangle ABC',
      labels: ['A', 'B', 'C'],
      vertices: [
        { x: 1, y: 2 },
        { x: 4, y: 2 },
        { x: 1, y: 5 }
      ]
    },
    quadrilateral: {
      name: 'Trapezoid ABCD',
      labels: ['A', 'B', 'C', 'D'],
      vertices: [
        { x: -3, y: -1 },
        { x: 3, y: -1 },
        { x: 2, y: 3 },
        { x: -2, y: 3 }
      ]
    },
    mariamM: {
      name: "Letter 'M' (Mariam)",
      labels: ['M1', 'M2', 'M3', 'M4', 'M5'],
      vertices: [
        { x: -3, y: -2 },
        { x: -3, y: 3 },
        { x: 0, y: 0 },
        { x: 3, y: 3 },
        { x: 3, y: -2 }
      ]
    },
    house: {
      name: 'House Polygon',
      labels: ['A', 'B', 'C', 'D', 'E'],
      vertices: [
        { x: -2, y: -2 },
        { x: 2, y: -2 },
        { x: 2, y: 1 },
        { x: 0, y: 4 },
        { x: -2, y: 1 }
      ]
    },
    custom: {
      name: 'Custom Pentagon',
      labels: ['P1', 'P2', 'P3', 'P4', 'P5'],
      vertices: [
        { x: 0, y: 4 },
        { x: 4, y: 1 },
        { x: 2, y: -3 },
        { x: -2, y: -3 },
        { x: -4, y: 1 }
      ]
    }
  };

  // --- Geometry Mathematical Utilities ---
  function distance(p1, p2) {
    const dx = p2.x - p1.x;
    const dy = p2.y - p1.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  function polygonPerimeter(vertices) {
    if (!vertices || vertices.length < 2) return 0;
    let perimeter = 0;
    for (let i = 0; i < vertices.length; i++) {
      const next = (i + 1) % vertices.length;
      perimeter += distance(vertices[i], vertices[next]);
    }
    return perimeter;
  }

  // Shoelace formula for polygon area
  function polygonArea(vertices) {
    if (!vertices || vertices.length < 3) return 0;
    let sum = 0;
    for (let i = 0; i < vertices.length; i++) {
      const next = (i + 1) % vertices.length;
      sum += (vertices[i].x * vertices[next].y) - (vertices[next].x * vertices[i].y);
    }
    return Math.abs(sum) / 2;
  }

  function roundCoord(val, decimals = 2) {
    return Math.round(val * Math.pow(10, decimals)) / Math.pow(10, decimals);
  }

  // --- Engine Class Definition ---
  class CoordinateGeometryEngine {
    constructor() {
      this.canvas = null;
      this.ctx = null;
      this.dpr = 1;

      // Coordinate Viewport state
      this.unitPx = 36;          // pixels per coordinate unit
      this.defaultUnitPx = 36;
      this.minUnitPx = 18;
      this.maxUnitPx = 90;
      this.panX = 0;             // offset from center
      this.panY = 0;
      this.centerX = 0;
      this.centerY = 0;

      // Model state
      this.currentShapeKey = 'triangle';
      this.preimageVertices = JSON.parse(JSON.stringify(SHAPE_PRESETS.triangle.vertices));
      this.labels = [...SHAPE_PRESETS.triangle.labels];

      // Transformation state
      this.transformation = {
        type: 'translation',     // 'translation' | 'reflection' | 'rotation' | 'dilation' | 'sequence'
        params: {
          dx: 3,
          dy: 2
        }
      };

      // Sequence state (multi-step transformation pipeline)
      this.sequence = [
        { type: 'translation', params: { dx: 2, dy: 3 } },
        { type: 'reflection', params: { axis: 'y-axis' } }
      ];
      this.animationState = {
        isPlaying: false,
        stepIndex: 0,
        progress: 1.0,         // 0.0 to 1.0 within current step
        animId: null,
        durationPerStep: 1200, // ms
        startTime: 0,
        stages: []             // list of vertex arrays for each step
      };

      // Interaction state
      this.isDraggingVertex = false;
      this.draggedVertexIndex = -1;
      this.isPanning = false;
      this.lastMousePos = { x: 0, y: 0 };
      this.hoveredVertexIndex = -1;

      // Listeners
      this.updateCallbacks = [];
      this.resizeObserver = null;

      // Bound handlers
      this._boundRender = this.render.bind(this);
      this._onMouseDown = this._handleMouseDown.bind(this);
      this._onMouseMove = this._handleMouseMove.bind(this);
      this._onMouseUp = this._handleMouseUp.bind(this);
      this._onWheel = this._handleWheel.bind(this);
      this._onTouchStart = this._handleTouchStart.bind(this);
      this._onTouchMove = this._handleTouchMove.bind(this);
      this._onTouchEnd = this._handleTouchEnd.bind(this);
    }

    // --- Public API Methods ---

    init(canvasId = 'interactiveCanvas') {
      if (typeof window === 'undefined') return this;

      this.canvas = typeof canvasId === 'string' ? document.getElementById(canvasId) : canvasId;
      if (!this.canvas) {
        console.warn(`[GeometryEngine] Canvas element '${canvasId}' not found yet.`);
        return this;
      }

      this.ctx = this.canvas.getContext('2d', { alpha: false });
      this.setupHighDpi();
      this.attachEventListeners();
      this.recalculateAndNotify();
      this.render();
      return this;
    }

    setShape(shapeKey) {
      if (SHAPE_PRESETS[shapeKey]) {
        this.currentShapeKey = shapeKey;
        this.preimageVertices = JSON.parse(JSON.stringify(SHAPE_PRESETS[shapeKey].vertices));
        this.labels = [...SHAPE_PRESETS[shapeKey].labels];
        this.recalculateAndNotify();
        this.render();
      } else {
        console.warn(`[GeometryEngine] Preset '${shapeKey}' not recognized.`);
      }
    }

    setCustomVertices(vertices, labels = null) {
      if (Array.isArray(vertices) && vertices.length >= 3) {
        this.preimageVertices = vertices.map(v => ({ x: Math.round(v.x), y: Math.round(v.y) }));
        if (labels && labels.length === vertices.length) {
          this.labels = [...labels];
        } else {
          this.labels = vertices.map((_, i) => String.fromCharCode(65 + i));
        }
        this.currentShapeKey = 'custom';
        this.recalculateAndNotify();
        this.render();
      }
    }

    setTransformation(type, params) {
      this.transformation = {
        type,
        params: Object.assign({}, params)
      };
      // Stop sequence animation if currently playing
      this.pauseSequence();
      this.recalculateAndNotify();
      this.render();
    }

    setSequence(steps) {
      if (Array.isArray(steps) && steps.length > 0) {
        this.sequence = steps.map(s => ({
          type: s.type,
          params: Object.assign({}, s.params)
        }));
        this.transformation.type = 'sequence';
        this.recalculateAndNotify();
        this.render();
      }
    }

    playSequence() {
      if (typeof window === 'undefined') return;
      this.pauseSequence();
      this.computeSequenceStages();
      if (this.animationState.stages.length < 2) return;

      this.animationState.isPlaying = true;
      this.animationState.stepIndex = 0;
      this.animationState.progress = 0.0;
      this.animationState.startTime = performance.now();

      const animate = (now) => {
        if (!this.animationState.isPlaying) return;

        const elapsed = now - this.animationState.startTime;
        const totalDuration = this.animationState.durationPerStep;
        let progress = elapsed / totalDuration;

        if (progress >= 1.0) {
          // Advance step
          this.animationState.stepIndex++;
          if (this.animationState.stepIndex >= this.sequence.length) {
            // Finished playing entire sequence
            this.animationState.isPlaying = false;
            this.animationState.stepIndex = this.sequence.length - 1;
            this.animationState.progress = 1.0;
            this.recalculateAndNotify();
            this.render();
            return;
          }
          this.animationState.startTime = now;
          this.animationState.progress = 0.0;
        } else {
          // Smooth cubic easing
          this.animationState.progress = this._easeInOutCubic(progress);
        }

        this.render();
        this.animationState.animId = requestAnimationFrame(animate);
      };

      this.animationState.animId = requestAnimationFrame(animate);
    }

    pauseSequence() {
      this.animationState.isPlaying = false;
      if (this.animationState.animId && typeof cancelAnimationFrame !== 'undefined') {
        cancelAnimationFrame(this.animationState.animId);
        this.animationState.animId = null;
      }
    }

    stepSequence(stepIndex) {
      this.pauseSequence();
      this.computeSequenceStages();
      const maxIndex = Math.max(0, this.sequence.length - 1);
      this.animationState.stepIndex = Math.min(Math.max(0, stepIndex), maxIndex);
      this.animationState.progress = 1.0;
      this.recalculateAndNotify();
      this.render();
    }

    resetView() {
      this.panX = 0;
      this.panY = 0;
      this.unitPx = this.defaultUnitPx;
      this.render();
    }

    zoomIn() {
      if (!this.canvas) return;
      this.zoomAt(this.canvas.clientWidth / 2, this.canvas.clientHeight / 2, 1.15);
    }

    zoomOut() {
      if (!this.canvas) return;
      this.zoomAt(this.canvas.clientWidth / 2, this.canvas.clientHeight / 2, 0.85);
    }

    onUpdate(callback) {
      if (typeof callback === 'function') {
        this.updateCallbacks.push(callback);
        // Dispatch immediately with current state
        this.notifyUpdate();
      }
    }

    getState() {
      const imageVertices = this.calculateImageVertices();
      const prePerimeter = polygonPerimeter(this.preimageVertices);
      const postPerimeter = polygonPerimeter(imageVertices);
      const preArea = polygonArea(this.preimageVertices);
      const postArea = polygonArea(imageVertices);

      let perimeterRatio = prePerimeter > 0.0001 ? postPerimeter / prePerimeter : 1;
      let areaRatio = preArea > 0.0001 ? postArea / preArea : 1;

      // Clean precision for display
      perimeterRatio = roundCoord(perimeterRatio, 2);
      areaRatio = roundCoord(areaRatio, 2);

      return {
        shapeKey: this.currentShapeKey,
        labels: this.labels,
        preimageVertices: this.preimageVertices.map(v => ({ x: v.x, y: v.y })),
        imageVertices: imageVertices.map(v => ({ x: roundCoord(v.x, 2), y: roundCoord(v.y, 2) })),
        transformation: JSON.parse(JSON.stringify(this.transformation)),
        transformationRule: this.getAlgebraicRuleString(),
        perimeterRatio,
        areaRatio,
        prePerimeter: roundCoord(prePerimeter, 2),
        postPerimeter: roundCoord(postPerimeter, 2),
        preArea: roundCoord(preArea, 2),
        postArea: roundCoord(postArea, 2),
        sequence: JSON.parse(JSON.stringify(this.sequence))
      };
    }

    // --- Mathematical Transformation Core ---

    transformPoint(p, transformation) {
      const { type, params } = transformation;
      let { x, y } = p;

      switch (type) {
        case 'translation': {
          const dx = (params && typeof params.dx === 'number') ? params.dx : 0;
          const dy = (params && typeof params.dy === 'number') ? params.dy : 0;
          return { x: x + dx, y: y + dy };
        }

        case 'reflection': {
          const axis = (params && params.axis) || 'x-axis';
          const k = (params && typeof params.k === 'number') ? params.k : 0;

          if (axis === 'x-axis') {
            // Over line y = 0
            return { x: x, y: -y };
          } else if (axis === 'y-axis') {
            // Over line x = 0
            return { x: -x, y: y };
          } else if (axis === 'y=x') {
            return { x: y, y: x };
          } else if (axis === 'y=-x') {
            return { x: -y, y: -x };
          } else if (axis === 'line-x') {
            // Over line x = k: reflected is 2k - x
            return { x: 2 * k - x, y: y };
          } else if (axis === 'line-y') {
            // Over line y = k: reflected is 2k - y
            return { x: x, y: 2 * k - y };
          }
          return { x, y };
        }

        case 'rotation': {
          const deg = (params && typeof params.angle === 'number') ? params.angle : 90;
          const rad = (deg * Math.PI) / 180;
          const cx = (params && typeof params.cx === 'number') ? params.cx : 0;
          const cy = (params && typeof params.cy === 'number') ? params.cy : 0;

          // Standard math CCW angle if positive, or CW if specified
          const isClockwise = params && params.clockwise === true;
          const effectiveRad = isClockwise ? -rad : rad;

          const cos = Math.cos(effectiveRad);
          const sin = Math.sin(effectiveRad);

          const relX = x - cx;
          const relY = y - cy;

          return {
            x: cx + (relX * cos - relY * sin),
            y: cy + (relX * sin + relY * cos)
          };
        }

        case 'dilation': {
          const k = (params && typeof params.scale === 'number') ? params.scale : 1.0;
          const cx = (params && typeof params.cx === 'number') ? params.cx : 0;
          const cy = (params && typeof params.cy === 'number') ? params.cy : 0;

          return {
            x: cx + k * (x - cx),
            y: cy + k * (y - cy)
          };
        }

        default:
          return { x, y };
      }
    }

    calculateImageVertices() {
      if (this.transformation.type === 'sequence') {
        let current = this.preimageVertices.map(v => ({ x: v.x, y: v.y }));
        for (const step of this.sequence) {
          current = current.map(p => this.transformPoint(p, step));
        }
        return current;
      }
      return this.preimageVertices.map(p => this.transformPoint(p, this.transformation));
    }

    computeSequenceStages() {
      const stages = [];
      let current = this.preimageVertices.map(v => ({ x: v.x, y: v.y }));
      stages.push(current);

      for (const step of this.sequence) {
        current = current.map(p => this.transformPoint(p, step));
        stages.push(current);
      }
      this.animationState.stages = stages;
      return stages;
    }

    getAlgebraicRuleString() {
      const { type, params } = this.transformation;
      switch (type) {
        case 'translation': {
          const dx = params.dx || 0;
          const dy = params.dy || 0;
          const xSign = dx >= 0 ? `+ ${dx}` : `- ${Math.abs(dx)}`;
          const ySign = dy >= 0 ? `+ ${dy}` : `- ${Math.abs(dy)}`;
          return `(x, y) → (x ${xSign}, y ${ySign})`;
        }
        case 'reflection': {
          const axis = params.axis || 'x-axis';
          if (axis === 'x-axis') return '(x, y) → (x, -y)';
          if (axis === 'y-axis') return '(x, y) → (-x, y)';
          if (axis === 'y=x') return '(x, y) → (y, x)';
          if (axis === 'y=-x') return '(x, y) → (-y, -x)';
          if (axis === 'line-x') return `(x, y) → (${2 * (params.k || 0)} - x, y)`;
          if (axis === 'line-y') return `(x, y) → (x, ${2 * (params.k || 0)} - y)`;
          return 'Reflection';
        }
        case 'rotation': {
          const deg = params.angle || 90;
          const cw = params.clockwise;
          const cx = params.cx || 0;
          const cy = params.cy || 0;

          if (cx === 0 && cy === 0) {
            if ((deg === 90 && cw) || (deg === 270 && !cw)) return '(x, y) → (y, -x) [90° CW]';
            if (deg === 180) return '(x, y) → (-x, -y) [180°]';
            if ((deg === 270 && cw) || (deg === 90 && !cw)) return '(x, y) → (-y, x) [90° CCW / 270° CW]';
          }
          return `Rotation by ${deg}° ${cw ? 'CW' : 'CCW'} around (${cx}, ${cy})`;
        }
        case 'dilation': {
          const k = params.scale !== undefined ? params.scale : 1.0;
          const cx = params.cx || 0;
          const cy = params.cy || 0;
          if (cx === 0 && cy === 0) {
            return `(x, y) → (${k}x, ${k}y)`;
          }
          return `(x, y) → (${cx} + ${k}(x - ${cx}), ${cy} + ${k}(y - ${cy}))`;
        }
        case 'sequence': {
          return this.sequence.map((step, idx) => {
            const rule = new CoordinateGeometryEngine();
            rule.setTransformation(step.type, step.params);
            return `Step ${idx + 1}: ${rule.getAlgebraicRuleString()}`;
          }).join('  ➜  ');
        }
        default:
          return '(x, y) → (x, y)';
      }
    }

    recalculateAndNotify() {
      this.notifyUpdate();
    }

    notifyUpdate() {
      if (this.updateCallbacks.length === 0) return;
      const state = this.getState();
      for (const cb of this.updateCallbacks) {
        try {
          cb(state);
        } catch (err) {
          console.error('[GeometryEngine] Error in update callback:', err);
        }
      }
    }

    // --- High-DPI & Viewport Transformations ---

    setupHighDpi() {
      if (!this.canvas || typeof window === 'undefined') return;
      this.dpr = window.devicePixelRatio || 1;
      const rect = this.canvas.getBoundingClientRect();
      const width = rect.width || this.canvas.clientWidth || 800;
      const height = rect.height || this.canvas.clientHeight || 520;

      this.canvas.width = Math.round(width * this.dpr);
      this.canvas.height = Math.round(height * this.dpr);

      this.ctx.setTransform(1, 0, 0, 1, 0, 0);
      this.ctx.scale(this.dpr, this.dpr);

      this.centerX = width / 2;
      this.centerY = height / 2;
    }

    // Convert Grid (x, y) -> Screen (sx, sy) in CSS pixels
    toScreen(x, y) {
      return {
        x: this.centerX + this.panX + (x * this.unitPx),
        y: this.centerY + this.panY - (y * this.unitPx)
      };
    }

    // Convert Screen (sx, sy) -> Grid (x, y)
    toGrid(sx, sy) {
      return {
        x: (sx - this.centerX - this.panX) / this.unitPx,
        y: (this.centerY + this.panY - sy) / this.unitPx
      };
    }

    zoomAt(screenX, screenY, factor) {
      const oldUnitPx = this.unitPx;
      const newUnitPx = Math.min(this.maxUnitPx, Math.max(this.minUnitPx, oldUnitPx * factor));
      if (newUnitPx === oldUnitPx) return;

      // Keep screenX, screenY anchored to same grid point
      const gridPos = this.toGrid(screenX, screenY);
      this.unitPx = newUnitPx;

      // Adjust pan so gridPos still maps to screenX, screenY
      this.panX = screenX - this.centerX - (gridPos.x * this.unitPx);
      this.panY = screenY - this.centerY + (gridPos.y * this.unitPx);

      this.render();
    }

    // --- Rendering Pipeline ---

    render() {
      if (!this.ctx || !this.canvas) return;

      const width = this.canvas.clientWidth || 800;
      const height = this.canvas.clientHeight || 520;

      // Ensure canvas size is synchronized with bounding box
      const rect = this.canvas.getBoundingClientRect();
      if (Math.round(rect.width * this.dpr) !== this.canvas.width ||
          Math.round(rect.height * this.dpr) !== this.canvas.height) {
        this.setupHighDpi();
      }

      this.ctx.save();
      // Clear canvas with crisp white background
      this.ctx.fillStyle = THEME.grid.background;
      this.ctx.fillRect(0, 0, width, height);

      // 1. Draw Cartesian Grid & Axes
      this.drawGrid(width, height);

      // 2. Draw Transformation-Specific Visual Aids (Mirror lines, vectors, rays, arcs)
      this.drawTransformationHelpers();

      // 3. Draw Polygons & Vertices
      if (this.transformation.type === 'sequence' && this.animationState.isPlaying) {
        this.renderSequenceAnimation();
      } else {
        const imageVertices = this.calculateImageVertices();
        // Draw Preimage
        this.drawPolygon(this.preimageVertices, this.labels, THEME.preimage, false);
        // Draw Image (with prime labels A', B', etc.)
        const imageLabels = this.labels.map(l => l + "'");
        this.drawPolygon(imageVertices, imageLabels, THEME.image, true);
      }

      this.ctx.restore();
    }

    drawGrid(width, height) {
      const ctx = this.ctx;
      const ox = this.centerX + this.panX;
      const oy = this.centerY + this.panY;

      // Grid bounds in integer grid coordinates
      const minX = Math.floor(-ox / this.unitPx) - 1;
      const maxX = Math.ceil((width - ox) / this.unitPx) + 1;
      const minY = Math.floor(-(height - oy) / this.unitPx) - 1;
      const maxY = Math.ceil(oy / this.unitPx) + 1;

      // Grid lines
      ctx.lineWidth = 1;
      for (let x = minX; x <= maxX; x++) {
        const sx = Math.round(ox + x * this.unitPx) + 0.5;
        if (x === 0) continue; // Drawn later as bold axis
        ctx.strokeStyle = (x % 5 === 0) ? THEME.grid.majorLine : THEME.grid.minorLine;
        ctx.beginPath();
        ctx.moveTo(sx, 0);
        ctx.lineTo(sx, height);
        ctx.stroke();
      }

      for (let y = minY; y <= maxY; y++) {
        const sy = Math.round(oy - y * this.unitPx) + 0.5;
        if (y === 0) continue;
        ctx.strokeStyle = (y % 5 === 0) ? THEME.grid.majorLine : THEME.grid.minorLine;
        ctx.beginPath();
        ctx.moveTo(0, sy);
        ctx.lineTo(width, sy);
        ctx.stroke();
      }

      // Bold Main Axes
      ctx.lineWidth = 2;
      ctx.strokeStyle = THEME.grid.axis;

      // X-Axis (y = 0)
      if (oy >= -20 && oy <= height + 20) {
        ctx.beginPath();
        ctx.moveTo(0, Math.round(oy) + 0.5);
        ctx.lineTo(width, Math.round(oy) + 0.5);
        ctx.stroke();
        this.drawArrowhead(width - 4, oy, 0, 10, THEME.grid.axis);
        this.drawArrowhead(4, oy, Math.PI, 10, THEME.grid.axis);
      }

      // Y-Axis (x = 0)
      if (ox >= -20 && ox <= width + 20) {
        ctx.beginPath();
        ctx.moveTo(Math.round(ox) + 0.5, 0);
        ctx.lineTo(Math.round(ox) + 0.5, height);
        ctx.stroke();
        this.drawArrowhead(ox, 4, -Math.PI / 2, 10, THEME.grid.axis);
        this.drawArrowhead(ox, height - 4, Math.PI / 2, 10, THEME.grid.axis);
      }

      // Axis Numbers & Labels
      ctx.font = '600 11px Outfit, -apple-system, sans-serif';
      ctx.fillStyle = THEME.grid.subtleText;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';

      // X-axis tick labels
      const step = this.unitPx < 26 ? 2 : 1;
      for (let x = minX; x <= maxX; x += step) {
        if (x === 0) continue;
        const sx = ox + x * this.unitPx;
        const sy = Math.max(16, Math.min(height - 24, oy + 6));
        ctx.fillText(x.toString(), sx, sy);
      }

      // Y-axis tick labels
      ctx.textAlign = 'right';
      ctx.textBaseline = 'middle';
      for (let y = minY; y <= maxY; y += step) {
        if (y === 0) continue;
        const sy = oy - y * this.unitPx;
        const sx = Math.max(26, Math.min(width - 12, ox - 8));
        ctx.fillText(y.toString(), sx, sy);
      }

      // Axis names (x and y)
      ctx.font = '800 13px Outfit, sans-serif';
      ctx.fillStyle = THEME.grid.axisLabel;
      ctx.textAlign = 'right';
      ctx.textBaseline = 'bottom';
      ctx.fillText('x', width - 14, Math.max(20, Math.min(height - 10, oy - 8)));

      ctx.textAlign = 'left';
      ctx.textBaseline = 'top';
      ctx.fillText('y', Math.max(10, Math.min(width - 24, ox + 10)), 12);

      // Origin label '0'
      if (ox >= 10 && ox <= width - 10 && oy >= 10 && oy <= height - 10) {
        ctx.font = '700 11px Outfit, sans-serif';
        ctx.fillStyle = THEME.grid.subtleText;
        ctx.textAlign = 'right';
        ctx.textBaseline = 'top';
        ctx.fillText('0', ox - 5, oy + 4);
      }
    }

    drawArrowhead(x, y, angle, size, color) {
      const ctx = this.ctx;
      ctx.save();
      ctx.fillStyle = color;
      ctx.translate(x, y);
      ctx.rotate(angle);
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.lineTo(-size, -size * 0.45);
      ctx.lineTo(-size * 0.7, 0);
      ctx.lineTo(-size, size * 0.45);
      ctx.closePath();
      ctx.fill();
      ctx.restore();
    }

    drawPolygon(vertices, labels, theme, isImage = false) {
      if (!vertices || vertices.length < 2) return;
      const ctx = this.ctx;
      const screenPts = vertices.map(v => this.toScreen(v.x, v.y));

      // Fill polygon
      ctx.beginPath();
      ctx.moveTo(screenPts[0].x, screenPts[0].y);
      for (let i = 1; i < screenPts.length; i++) {
        ctx.lineTo(screenPts[i].x, screenPts[i].y);
      }
      ctx.closePath();
      ctx.fillStyle = theme.fill;
      ctx.fill();

      // Stroke polygon boundary
      ctx.strokeStyle = theme.stroke;
      ctx.lineWidth = isImage ? 3 : 2.5;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';
      ctx.stroke();

      // Render vertices and label pills
      for (let i = 0; i < screenPts.length; i++) {
        const pt = screenPts[i];
        const isHovered = !isImage && (this.hoveredVertexIndex === i);
        const radius = isHovered ? 7.5 : 5.5;

        // Outer halo on hover
        if (isHovered) {
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, 14, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(99, 102, 241, 0.25)';
          ctx.fill();
        }

        // Vertex circle
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, radius, 0, Math.PI * 2);
        ctx.fillStyle = theme.vertexFill;
        ctx.fill();
        ctx.strokeStyle = isHovered ? theme.vertexHover : theme.vertexBorder;
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Label with coordinates pill: e.g. A(1, 2)
        const v = vertices[i];
        const labelText = `${labels[i] || 'P'}(${roundCoord(v.x, 1)}, ${roundCoord(v.y, 1)})`;
        this.drawVertexBadge(pt.x, pt.y, labelText, theme, i);
      }
    }

    drawVertexBadge(x, y, text, theme, index = 0) {
      const ctx = this.ctx;
      ctx.save();
      ctx.font = '700 11px JetBrains Mono, monospace';
      const textMetrics = ctx.measureText(text);
      const paddingX = 7;
      const paddingY = 4;
      const badgeW = textMetrics.width + paddingX * 2;
      const badgeH = 20;

      // Smart offset based on vertex position
      const angle = (index * (Math.PI * 2 / 5)) - Math.PI / 4;
      const offsetDist = 18;
      const badgeX = x + Math.cos(angle) * offsetDist - (badgeW / 2);
      const badgeY = y + Math.sin(angle) * offsetDist - (badgeH / 2);

      // Pill shadow
      ctx.shadowColor = 'rgba(0,0,0,0.08)';
      ctx.shadowBlur = 6;
      ctx.shadowOffsetY = 2;

      // Pill background
      ctx.fillStyle = theme.badgeBg;
      ctx.beginPath();
      this.drawRoundedRect(ctx, badgeX, badgeY, badgeW, badgeH, 6);
      ctx.fill();

      // Pill border
      ctx.shadowColor = 'transparent';
      ctx.strokeStyle = theme.badgeBorder;
      ctx.lineWidth = 1;
      ctx.stroke();

      // Text
      ctx.fillStyle = theme.labelColor;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(text, badgeX + badgeW / 2, badgeY + badgeH / 2);

      ctx.restore();
    }

    drawRoundedRect(ctx, x, y, width, height, radius) {
      ctx.beginPath();
      ctx.moveTo(x + radius, y);
      ctx.lineTo(x + width - radius, y);
      ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
      ctx.lineTo(x + width, y + height - radius);
      ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
      ctx.lineTo(x + radius, y + height);
      ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
      ctx.lineTo(x, y + radius);
      ctx.quadraticCurveTo(x, y, x + radius, y);
      ctx.closePath();
    }

    // --- Educational Visual Aids ---

    drawTransformationHelpers() {
      const { type } = this.transformation;

      if (type === 'translation') {
        this.drawTranslationVectors();
      } else if (type === 'reflection') {
        this.drawReflectionHelpers();
      } else if (type === 'rotation') {
        this.drawRotationHelpers();
      } else if (type === 'dilation') {
        this.drawDilationHelpers();
      }
    }

    drawTranslationVectors() {
      const ctx = this.ctx;
      const imageVertices = this.calculateImageVertices();

      ctx.save();
      ctx.setLineDash([5, 4]);
      ctx.strokeStyle = THEME.helpers.vector;
      ctx.lineWidth = 1.8;

      for (let i = 0; i < this.preimageVertices.length; i++) {
        const p1 = this.toScreen(this.preimageVertices[i].x, this.preimageVertices[i].y);
        const p2 = this.toScreen(imageVertices[i].x, imageVertices[i].y);

        // Dashed line
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();

        // Arrowhead at image vertex
        const angle = Math.atan2(p2.y - p1.y, p2.x - p1.x);
        this.drawArrowhead(p2.x, p2.y, angle, 9, THEME.helpers.vector);
      }
      ctx.restore();
    }

    drawReflectionHelpers() {
      const ctx = this.ctx;
      const width = this.canvas.clientWidth || 800;
      const height = this.canvas.clientHeight || 520;
      const axis = this.transformation.params.axis || 'x-axis';
      const k = this.transformation.params.k || 0;

      ctx.save();

      // 1. Draw Mirror Line
      ctx.strokeStyle = THEME.helpers.mirrorLine;
      ctx.lineWidth = 2.5;
      ctx.shadowColor = THEME.helpers.mirrorGlow;
      ctx.shadowBlur = 8;
      ctx.setLineDash([8, 4]);

      if (axis === 'x-axis') {
        const sy = this.toScreen(0, 0).y;
        ctx.beginPath();
        ctx.moveTo(0, sy);
        ctx.lineTo(width, sy);
        ctx.stroke();
      } else if (axis === 'y-axis') {
        const sx = this.toScreen(0, 0).x;
        ctx.beginPath();
        ctx.moveTo(sx, 0);
        ctx.lineTo(sx, height);
        ctx.stroke();
      } else if (axis === 'y=x') {
        const p1 = this.toScreen(-60, -60);
        const p2 = this.toScreen(60, 60);
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();
      } else if (axis === 'y=-x') {
        const p1 = this.toScreen(-60, 60);
        const p2 = this.toScreen(60, -60);
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();
      } else if (axis === 'line-x') {
        const sx = this.toScreen(k, 0).x;
        ctx.beginPath();
        ctx.moveTo(sx, 0);
        ctx.lineTo(sx, height);
        ctx.stroke();
      } else if (axis === 'line-y') {
        const sy = this.toScreen(0, k).y;
        ctx.beginPath();
        ctx.moveTo(0, sy);
        ctx.lineTo(width, sy);
        ctx.stroke();
      }

      ctx.restore();

      // 2. Draw Perpendicular Projection Lines with Midpoints
      const imageVertices = this.calculateImageVertices();
      ctx.save();
      ctx.strokeStyle = THEME.helpers.projLine;
      ctx.lineWidth = 1.4;
      ctx.setLineDash([4, 4]);

      for (let i = 0; i < this.preimageVertices.length; i++) {
        const p1 = this.toScreen(this.preimageVertices[i].x, this.preimageVertices[i].y);
        const p2 = this.toScreen(imageVertices[i].x, imageVertices[i].y);

        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();

        // Midpoint on mirror line
        const midX = (p1.x + p2.x) / 2;
        const midY = (p1.y + p2.y) / 2;
        ctx.fillStyle = THEME.helpers.mirrorLine;
        ctx.beginPath();
        ctx.arc(midX, midY, 3, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    }

    drawRotationHelpers() {
      const ctx = this.ctx;
      const params = this.transformation.params || {};
      const cx = params.cx || 0;
      const cy = params.cy || 0;
      const isClockwise = params.clockwise === true;
      const centerScreen = this.toScreen(cx, cy);

      ctx.save();

      // 1. Center of Rotation Crosshair
      ctx.strokeStyle = THEME.helpers.centerPoint;
      ctx.fillStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(centerScreen.x, centerScreen.y, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(centerScreen.x - 10, centerScreen.y);
      ctx.lineTo(centerScreen.x + 10, centerScreen.y);
      ctx.moveTo(centerScreen.x, centerScreen.y - 10);
      ctx.lineTo(centerScreen.x, centerScreen.y + 10);
      ctx.stroke();

      // 2. Circular Arc Paths from Preimage to Image
      const imageVertices = this.calculateImageVertices();
      ctx.strokeStyle = THEME.helpers.rotationArc;
      ctx.lineWidth = 1.6;
      ctx.setLineDash([4, 4]);

      for (let i = 0; i < this.preimageVertices.length; i++) {
        const v1 = this.preimageVertices[i];
        const v2 = imageVertices[i];
        const p1 = this.toScreen(v1.x, v1.y);
        const p2 = this.toScreen(v2.x, v2.y);

        const r = distance(v1, { x: cx, y: cy }) * this.unitPx;
        if (r < 4) continue;

        // Angle in screen space
        const startAngle = Math.atan2(p1.y - centerScreen.y, p1.x - centerScreen.x);
        const endAngle = Math.atan2(p2.y - centerScreen.y, p2.x - centerScreen.x);

        ctx.beginPath();
        ctx.arc(centerScreen.x, centerScreen.y, r, startAngle, endAngle, !isClockwise);
        ctx.stroke();

        // Arrowhead at end of arc
        const tangentAngle = endAngle + (isClockwise ? Math.PI / 2 : -Math.PI / 2);
        this.drawArrowhead(p2.x, p2.y, tangentAngle, 8, THEME.helpers.rotationArc);
      }

      ctx.restore();
    }

    drawDilationHelpers() {
      const ctx = this.ctx;
      const params = this.transformation.params || {};
      const cx = params.cx || 0;
      const cy = params.cy || 0;
      const centerScreen = this.toScreen(cx, cy);
      const imageVertices = this.calculateImageVertices();

      ctx.save();

      // Center of Dilation
      ctx.strokeStyle = THEME.helpers.dilationRay;
      ctx.fillStyle = '#ffffff';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.arc(centerScreen.x, centerScreen.y, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Projection Rays from Center through Preimage to Image (and beyond)
      ctx.setLineDash([5, 4]);
      ctx.strokeStyle = THEME.helpers.dilationRay;
      ctx.lineWidth = 1.4;

      for (let i = 0; i < this.preimageVertices.length; i++) {
        const p2 = this.toScreen(imageVertices[i].x, imageVertices[i].y);

        // Extended ray
        const dirX = p2.x - centerScreen.x;
        const dirY = p2.y - centerScreen.y;
        const farX = centerScreen.x + dirX * 1.3;
        const farY = centerScreen.y + dirY * 1.3;

        ctx.beginPath();
        ctx.moveTo(centerScreen.x, centerScreen.y);
        ctx.lineTo(farX, farY);
        ctx.stroke();
      }

      ctx.restore();
    }

    // --- Sequence Animation Player ---

    renderSequenceAnimation() {
      const stages = this.animationState.stages;
      const stepIdx = this.animationState.stepIndex;
      const t = this.animationState.progress;

      if (!stages || stages.length < 2) return;

      // Draw initial preimage
      this.drawPolygon(stages[0], this.labels, THEME.preimage, false);

      // Draw past stages in soft intermediate styling
      for (let s = 1; s <= stepIdx; s++) {
        const stageLabels = this.labels.map(l => l + "'".repeat(s));
        this.drawPolygon(stages[s], stageLabels, THEME.intermediate, false);
      }

      // Interpolate current active step: from stages[stepIdx] to stages[stepIdx + 1]
      const fromStage = stages[stepIdx];
      const toStage = stages[stepIdx + 1];

      if (fromStage && toStage) {
        const interpolated = fromStage.map((p, i) => ({
          x: p.x + (toStage[i].x - p.x) * t,
          y: p.y + (toStage[i].y - p.y) * t
        }));

        const activeLabels = this.labels.map(l => l + "'".repeat(stepIdx + 1));
        this.drawPolygon(interpolated, activeLabels, THEME.image, true);
      }
    }

    _easeInOutCubic(t) {
      return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    }

    // --- Interaction & Event Handlers ---

    attachEventListeners() {
      if (!this.canvas) return;

      this.canvas.addEventListener('mousedown', this._onMouseDown);
      window.addEventListener('mousemove', this._onMouseMove);
      window.addEventListener('mouseup', this._onMouseUp);
      this.canvas.addEventListener('wheel', this._onWheel, { passive: false });

      this.canvas.addEventListener('touchstart', this._onTouchStart, { passive: false });
      window.addEventListener('touchmove', this._onTouchMove, { passive: false });
      window.addEventListener('touchend', this._onTouchEnd);

      // Resize observer to handle dynamic responsive layout changes
      if (typeof window !== 'undefined' && window.ResizeObserver) {
        this.resizeObserver = new ResizeObserver(() => {
          this.setupHighDpi();
          this.render();
        });
        this.resizeObserver.observe(this.canvas);
      }
    }

    destroy() {
      this.pauseSequence();
      if (this.canvas) {
        this.canvas.removeEventListener('mousedown', this._onMouseDown);
        this.canvas.removeEventListener('wheel', this._onWheel);
        this.canvas.removeEventListener('touchstart', this._onTouchStart);
      }
      if (typeof window !== 'undefined') {
        window.removeEventListener('mousemove', this._onMouseMove);
        window.removeEventListener('mouseup', this._onMouseUp);
        window.removeEventListener('touchmove', this._onTouchMove);
        window.removeEventListener('touchend', this._onTouchEnd);
      }

      if (this.resizeObserver) {
        this.resizeObserver.disconnect();
      }
    }

    _getCanvasCoords(e) {
      const rect = this.canvas.getBoundingClientRect();
      return {
        x: e.clientX - rect.left,
        y: e.clientY - rect.top
      };
    }

    _findPreimageVertexUnderCursor(screenX, screenY, hitRadius = 14) {
      for (let i = 0; i < this.preimageVertices.length; i++) {
        const pt = this.toScreen(this.preimageVertices[i].x, this.preimageVertices[i].y);
        const dist = Math.hypot(pt.x - screenX, pt.y - screenY);
        if (dist <= hitRadius) {
          return i;
        }
      }
      return -1;
    }

    _handleMouseDown(e) {
      if (e.button !== 0) return; // Primary mouse button only
      const pos = this._getCanvasCoords(e);
      const hitIdx = this._findPreimageVertexUnderCursor(pos.x, pos.y);

      if (hitIdx !== -1) {
        this.isDraggingVertex = true;
        this.draggedVertexIndex = hitIdx;
        this.canvas.style.cursor = 'crosshair';
      } else {
        this.isPanning = true;
        this.lastMousePos = { x: e.clientX, y: e.clientY };
        this.canvas.style.cursor = 'grabbing';
      }
    }

    _handleMouseMove(e) {
      const pos = this._getCanvasCoords(e);

      if (this.isDraggingVertex && this.draggedVertexIndex !== -1) {
        // Convert screen coordinates to grid coordinates and snap to integer!
        const gridPos = this.toGrid(pos.x, pos.y);
        const snappedX = Math.round(gridPos.x);
        const snappedY = Math.round(gridPos.y);

        const v = this.preimageVertices[this.draggedVertexIndex];
        if (v.x !== snappedX || v.y !== snappedY) {
          v.x = snappedX;
          v.y = snappedY;
          this.recalculateAndNotify();
          this.render();
        }
      } else if (this.isPanning) {
        const dx = e.clientX - this.lastMousePos.x;
        const dy = e.clientY - this.lastMousePos.y;
        this.panX += dx;
        this.panY += dy;
        this.lastMousePos = { x: e.clientX, y: e.clientY };
        this.render();
      } else {
        // Hover state check
        const hitIdx = this._findPreimageVertexUnderCursor(pos.x, pos.y);
        if (hitIdx !== this.hoveredVertexIndex) {
          this.hoveredVertexIndex = hitIdx;
          this.canvas.style.cursor = hitIdx !== -1 ? 'grab' : 'default';
          this.render();
        }
      }
    }

    _handleMouseUp() {
      if (this.isDraggingVertex) {
        this.isDraggingVertex = false;
        this.draggedVertexIndex = -1;
        this.canvas.style.cursor = this.hoveredVertexIndex !== -1 ? 'grab' : 'default';
      }
      if (this.isPanning) {
        this.isPanning = false;
        this.canvas.style.cursor = this.hoveredVertexIndex !== -1 ? 'grab' : 'default';
      }
    }

    _handleWheel(e) {
      e.preventDefault();
      const pos = this._getCanvasCoords(e);
      const zoomFactor = e.deltaY < 0 ? 1.08 : 0.92;
      this.zoomAt(pos.x, pos.y, zoomFactor);
    }

    // Touch Support for mobile and tablet
    _handleTouchStart(e) {
      if (e.touches.length === 1) {
        e.preventDefault();
        const touch = e.touches[0];
        const pos = this._getCanvasCoords(touch);
        const hitIdx = this._findPreimageVertexUnderCursor(pos.x, pos.y, 22);

        if (hitIdx !== -1) {
          this.isDraggingVertex = true;
          this.draggedVertexIndex = hitIdx;
        } else {
          this.isPanning = true;
          this.lastMousePos = { x: touch.clientX, y: touch.clientY };
        }
      }
    }

    _handleTouchMove(e) {
      if (e.touches.length === 1) {
        e.preventDefault();
        const touch = e.touches[0];
        const pos = this._getCanvasCoords(touch);

        if (this.isDraggingVertex && this.draggedVertexIndex !== -1) {
          const gridPos = this.toGrid(pos.x, pos.y);
          const snappedX = Math.round(gridPos.x);
          const snappedY = Math.round(gridPos.y);

          const v = this.preimageVertices[this.draggedVertexIndex];
          if (v.x !== snappedX || v.y !== snappedY) {
            v.x = snappedX;
            v.y = snappedY;
            this.recalculateAndNotify();
            this.render();
          }
        } else if (this.isPanning) {
          const dx = touch.clientX - this.lastMousePos.x;
          const dy = touch.clientY - this.lastMousePos.y;
          this.panX += dx;
          this.panY += dy;
          this.lastMousePos = { x: touch.clientX, y: touch.clientY };
          this.render();
        }
      }
    }

    _handleTouchEnd() {
      this.isDraggingVertex = false;
      this.draggedVertexIndex = -1;
      this.isPanning = false;
    }
  }

  // Singleton instance & Public Facade
  const defaultEngine = new CoordinateGeometryEngine();

  return {
    CoordinateGeometryEngine,
    init: (canvasId) => defaultEngine.init(canvasId),
    setShape: (shapeKey) => defaultEngine.setShape(shapeKey),
    setCustomVertices: (verts, labels) => defaultEngine.setCustomVertices(verts, labels),
    setTransformation: (type, params) => defaultEngine.setTransformation(type, params),
    setSequence: (steps) => defaultEngine.setSequence(steps),
    playSequence: () => defaultEngine.playSequence(),
    pauseSequence: () => defaultEngine.pauseSequence(),
    stepSequence: (stepIdx) => defaultEngine.stepSequence(stepIdx),
    resetView: () => defaultEngine.resetView(),
    zoomIn: () => defaultEngine.zoomIn(),
    zoomOut: () => defaultEngine.zoomOut(),
    onUpdate: (cb) => defaultEngine.onUpdate(cb),
    getState: () => defaultEngine.getState(),
    destroy: () => defaultEngine.destroy(),
    presets: SHAPE_PRESETS
  };
});
