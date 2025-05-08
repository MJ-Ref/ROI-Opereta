# Opereta ROI – Detailed Value Generation Framework

_All figures shown below use the **Mid-Market** tier with the **Base (100 % impact)** scenario for illustration.  Variable names match those in `constants.py` and `calculations.py` so investors / engineers can trace every number through the code._

---

## Table of Contents
1. [Hiring Process Optimization](#1-hiring-process-optimization)
2. [Enhanced Hiring Quality](#2-enhanced-hiring-quality)
3. [Strategic Role Alignment](#3-strategic-role-alignment)
4. [Optimized Interviewing](#4-optimized-interviewing)
5. [Accelerated Onboarding](#5-accelerated-onboarding)
6. [Improved Internal Mobility](#6-improved-internal-mobility)
7. [Effective Performance & Development](#7-effective-performance--development)
8. [Strategic Workforce Planning](#8-strategic-workforce-planning)

---

## 1  Hiring Process Optimization

### Problem Statement
* Average **Time-to-Fill** (TTF) = **44 days** (SHRM 2022).  Each vacancy day reduces output.
* Average **Cost-per-Hire** (CPH) = **$4,700**; higher for SMBs.
* Recruiters spend **30 min–2 hrs** scheduling each interview → significant hidden labor cost.

### Opereta Impact
* **TTF reduction:** 30 % (benchmark: AI platforms 25-35 %).
* **Recruiter hours saved:** 13 h/week per recruiter (11 h generic AI + 2 h Opereta specific).
* **CPH reduction:** 15 % via less agency spend & smarter ad spend.

### Formulas & Example Calculation
| Savings Area | Formula | Example Inputs | Annual Savings |
|--------------|---------|----------------|----------------|
| Reduced TTF | `TTF_DAYS_SAVED × DAILY_VACANCY_COST × ANNUAL_HIRES` | 44 × 30 % = **13.2 days**<br/>Daily vacancy cost = `AVG_SAL/260 × 1.5` = $75 k / 260 ×1.5 = **$433**<br/>Annual hires = 750 × 15 % = **113** | **$5.43 M** |
| Recruiter Productivity | `HOURS_SAVED × HOURLY_RATE` | 13 h×50 wks×3 recruiters = **1,950 h**<br/>Hourly recruiter cost = $70 k / 2,080 = **$33.65** | **$0.38 M** |
| Lower CPH | `CPH × REDUCTION % × ANNUAL_HIRES` | $4,700 × 15 % × 113 | **$0.53 M** |

> **Total Category 1:** **$6.33 M**

---

## 2  Enhanced Hiring Quality

### Problem Statement
* **Mis-hire rate:** ~15 % of hires are "bad" (CareerBuilder).
* **Cost per bad hire:** 30 % of first-year salary ⇒ ~$22.5 k.

### Opereta Impact
* **Mis-hire reduction:** 35 % via skills-based matching & assessments.

### Formula & Example
```
MISHIRE_COST = AVG_SAL × 30 %
ANNUAL_BAD_HIRES = ANNUAL_HIRES × 15 %
PREVENTED_BAD_HIRES = ANNUAL_BAD_HIRES × 35 %
Savings = PREVENTED_BAD_HIRES × MISHIRE_COST
```
Numbers → `22.5 k × (113×15 %×35 %) = $1.12 M`

---

## 3  Strategic Role Alignment

### Problem Statement
* Poorly defined roles create **"shift shock"** – 43 % of early leavers say the job wasn't what they expected.
* Early attrition is expensive: replacing a new hire costs **21 % of salary** on average (SHRM).
* Misaligned roles stall strategy execution; 71 % of orgs struggle to link roles to strategic goals.

### Opereta Impact
* AI-generated, skill-backed role definitions reduce early attrition from mis-match by **60 %**.
* Clear role-to-value mapping ensures talent is deployed where it drives the greatest ROI.

### Formula & Example
| Savings Area | Formula | Example Inputs | Annual Savings |
|--------------|---------|----------------|----------------|
| Lower Early Attrition | `Early_Turnover × 43 % × 60 % × Replacement_Cost` | Early turnover = `ANNUAL_HIRES × 30 %` = `113 × 0.3 = 34`<br/>Shift-shock portion 43 % ⇒ **14.6**<br/>Prevented = 60 % ⇒ **8.8**<br/>Replacement cost = `AVG_SAL × 21 %` = **$15,750** | **$1.16 M** |

---

## 4  Optimized Interviewing

### Problem Statement
* Avg. interview cycle = **23 days**; interviewer hours per hire up **21 %** YoY (Ashby 2024).
* 67 % of recruiters spend 30 min–2 h scheduling one interview.
* Poor candidate experience leads to drop-offs and mis-hires.

### Opereta Impact
* 90 % reduction in scheduling effort via AI calendar orchestration.
* Structured, data-driven assessments improve predictive validity.

### Formula & Example
| Savings Area | Formula | Example Inputs | Annual Savings |
|--------------|---------|----------------|----------------|
| Efficient Scheduling | `Interviews × Time_Saved_Per_Interview × Recruiter_Hourly_Rate` | Interviews = `ANNUAL_HIRES × 5` = **565**<br/>Time saved = 1 h × 90 % = **0.9 h**<br/>Hourly rate = **$35** | **$118 k** |

---

## 5  Accelerated Onboarding

### Problem Statement
* New hires take **8 months** to full productivity (Forbes).
* 20 % quit in first 45 days; only 12 % say their onboarding is great.

### Opereta Impact
* 35 % faster time-to-productivity via personalised, skills-based onboarding tracks.
* Retains more new hires through early engagement.

### Formula & Example
| Savings Area | Formula | Example Inputs | Annual Savings |
|--------------|---------|----------------|----------------|
| Faster Ramp | `(Avg Sal ÷ 12) × Months_Saved × 50 % Deficit × Annual_Hires` | Months saved = `8 × 35 %` = **2.8**<br/>Half-productivity deficit = 50 % | **$8.31 M** |

---

## 6  Improved Internal Mobility

### Problem Statement
* Internal fill rate only **24 %**; external hires cost 18 % salary premium ± recruiting fees.
* Lack of growth paths → employees at low-mobility firms leave **41 % sooner** (LinkedIn).

### Opereta Impact
* Boosts internal fill rate by **20 pp** (e.g., 24 % → 44 %).
* AI talent marketplace reveals hidden skills and gig opportunities.

### Formula & Example
| Savings Area | Formula | Example Inputs | Annual Savings |
|--------------|---------|----------------|----------------|
| Internal Fill Savings | `External_Hires_Avoided × (Salary_Premium + 0.5×CPH)` | Ext hires avoided ≈ **35**<br/>Premium = $75 k × 18 % = **$13.5 k**<br/>0.5×CPH = $2.35 k | **$2.92 M** |

---

## 7  Effective Performance & Development

### Problem Statement
* 90 % of traditional reviews fail; managers waste **210 h/yr** on them.
* Only 21 % employees engaged; disengagement costs US firms $450–550 B.

### Opereta Impact
* Continuous, strengths-based feedback boosts productivity of 20 % of payroll by **3 %**.
* Reduces voluntary turnover **30 %** among leavers related to career growth.

### Formula & Example
| Savings Area | Formula | Annual Savings |
|--------------|---------|----------------|
| Productivity Gains | `Total_Payroll × 20 % × 3 %` | **$4.28 M** |
| Reduced Turnover | `Leavers × 30 % × Replacement_Cost` | **$5.39 M** |

---

## 8  Strategic Workforce Planning

### Problem Statement
* 71 % of HR leaders can't align workforce plans to strategy (SHRM 2023).
* Skills gaps bleed **$59 M/yr** from a typical large enterprise (WalkMe).

### Opereta Impact
* Saves **4 % of total payroll** via proactive sizing, skill gap mitigation and redeployment.

### Formula & Example
| Savings Area | Formula | Annual Savings |
|--------------|---------|----------------|
| Labor Budget Optimisation | `Total_Payroll × 4 %` | **$28.5 M** |

---

## How to Use This Document
1. **Traceability:** Variable names refer directly to code constants so diligence teams can reproduce figures.
2. **Scenario Analysis:** Swap in *Conservative* (0.5×) or *Aggressive* (1.25×) multipliers and recalc.
3. **Sensitivity:** Adjust any constant (e.g., `AVG_TIME_TO_FILL_DAYS`) in `constants.py`; savings recompute automatically.

---

> © 2024 Opereta Inc.  Confidential & Proprietary 