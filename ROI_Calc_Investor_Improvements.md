# Opereta ROI Calculator – Improvement Roadmap

> Version 1.0  |  Last updated: <!--DATE_PLACEHOLDER-->

This document consolidates feedback from the recent investor-lens review of the `ROI Calc Investor.py` Streamlit app and the supporting research file.  It is organized into five focus areas with concrete, actionable tasks and quick-win checklists.

---

## 1  Narrative & Credibility

### Goals
* Strengthen believability of savings assumptions.
* Provide transparent, source-linked traceability.
* Offer downside / upside views to pre-empt investor sensitivity questions.

### Action Items
1. **Scenario Sensitivity** – add a `selectbox` (`Conservative / Base / Aggressive`) that globally scales `OPERETA_IMPACT` values (e.g., ×0.5, ×1.0, ×1.25).
2. **Variance Bands in UI** – display low / mid / high totals alongside the single headline figures.
3. **Inline Citations** – add clickable info-icons next to each impact % that open a modal or tooltip displaying the source paragraph from `Opereta Talent Intelligence ROI – Data by Employee Lifecycle Stage.md`.
4. **Multi-Year View** – embed a line chart of cumulative cash flow (36 months) to demonstrate NPV and payback visually.
5. **Benchmark Appendix** – append a short table in the expander linking each constant (e.g., `AVG_TIME_TO_FILL_DAYS`) to its source.

---

## 2  Unit Economics & Pricing Logic

### Goals
* Connect customer ROI to Opereta's own SaaS metrics.
* Allow real-time pricing stress tests.

### Action Items
1. **Economics Toggle** – sidebar checkbox "Show SaaS Unit Economics".  When active, display: gross margin %, CAC, churn %, resulting LTV/CAC ratio.
2. **Dynamic Pricing Slider** – let users drag Opereta price (±50 %) and instantly see ROI % and LTV/CAC adjustments.
3. **CAC Placeholder** – include a constant `ASSUMED_CAC_PER_TIER` array for quick modeling until real data exists.

---

## 3  UX & Investor Polish

### Goals
* Faster first paint, mobile-friendly, downloadable artifacts.

### Quick Wins
- 🌐 Wrap heavy markdown (value props, long tables) in `st.expander(open=False)` to cut initial render time.
- 📱 Add responsive CSS `@media` queries so 4-column metric row collapses gracefully on narrow screens.
- 📄 Provide `Download PDF / PPTX` button (use `pdfkit` or `python-pptx`) for investors to save snapshots.
- 📊 Use emojis sparingly—confirm with brand guidelines.

---

## 4  Technical & Code Quality

### Goals
* Improve maintainability, performance, and testability.

### Action Items
1. **Decompose Calculations** – move each ROI bucket into its own function (`def savings_time_to_fill(...)`).
2. **Add Type Hints & Docstrings** – follow PEP 484 & NumPy docstring style.
3. **Validation Layer** – guard against divide-by-zero (e.g., annual hires = 0) and missing price input.
4. **Caching** – decorate heavy computations with `@st.cache_data`.
5. **requirements.txt** – create file (`streamlit`, `pandas`, `pdfkit`, `python-pptx`, exact versions).
6. **Unit Tests** – scaffold `tests/` using `pytest` to cover calculation functions with edge cases.

---

## 5  Data & Sensitivity Management

### Goals
* Ensure every constant is defensible and easy to tweak.

### Action Items
1. **Central Constants Module** – extract all `AVG_*`, `OPERETA_IMPACT`, etc. into `constants.py`; import into the app.
2. **Parameter Dashboard** – optional advanced sidebar that exposes key constants behind a password toggle for internal tweaking.
3. **Stress-Test Slider** – single slider (0–120 %) multiplies all impact metrics to show robustness.
4. **Sources Column** – in `constants.py`, store a `source` attribute or dict next to each constant.

---

## Implementation Timeline (Suggested)
| Week | Focus Area | Key Deliverables |
|------|------------|------------------|
| 1 | Code Quality | Decompose functions, add type hints, constants module, requirements.txt |
| 2 | Narrative & Credibility | Scenario sensitivity controls, inline citations, benchmark appendix |
| 3 | UX Polish | Expander wrappers, responsive metrics row, download button |
| 4 | Unit Economics | SaaS toggle, pricing slider, CAC constants |
| 5 | Data Governance | Stress-test slider, source mapping, parameter dashboard |

---

### Next Steps
1. Approve this roadmap or adjust priorities.
2. Create a new Git branch `roi-improvements` and begin Week 1 tasks.
3. Schedule a demo with stakeholders after Week 3 to gather feedback before finalizing.

> **Reminder:** keep commits small and reference the task numbers above (e.g., `[Narrative-2] Add low/base/high scenario selectbox`). 