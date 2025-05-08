# Constants module extracted from ROI_Calc_Investor.py
# -----------------------------------------------------
# Purpose: provide a single source of truth for all numeric
# and dictionary constants used across the ROI calculator app.
# Each constant is documented with a brief comment and, where
# possible, a citation placeholder for future traceability.

# ---------------------------
# Industry Benchmark Constants
# ---------------------------

AVG_TIME_TO_FILL_DAYS = 44  # SHRM (2022)
AVG_COST_PER_HIRE_SHRM = 4700  # SHRM (2022)
AVG_COST_PER_HIRE_SMALL_BIZ = 7645  # SHRM (2022)
RECRUITER_INTERVIEW_SCHEDULING_TIME_MAX_HOURS = 2  # Yello Survey (2020)
RECRUITER_AVG_HOURLY_RATE = 35  # Payscale (est.)
AVG_CANDIDATES_PER_OPENING = 250  # Workable (2023)
INTERVIEWS_PER_HIRE = 5  # Internal assumption
AVG_MISHIRE_COST_LOW = 17000  # Various studies
AVG_MISHIRE_COST_HIGH = 240000  # U.S. DoL (est.)
MISHIRE_COST_PERCENT_OF_SALARY_DOL = 0.30  # U.S. DoL
MANAGERS_TIME_ON_UNDERPERFORMERS_PERCENT = 0.17  # CFO survey
NEW_HIRES_LEAVING_IN_90_DAYS_PERCENT = 0.30  # 2022 survey
COST_TO_REPLACE_PERCENT_OF_SALARY = 0.21  # SHRM
TOP_PERFORMER_PRODUCTIVITY_MULTIPLIER_LOW = 4  # McKinsey
AVG_TIME_TO_PRODUCTIVITY_MONTHS = 8  # Forbes / UrbanBound
NEW_HIRE_TURNOVER_FIRST_45_DAYS_PERCENT = 0.20  # BambooHR
EXTERNAL_HIRE_SALARY_PREMIUM_PERCENT = 0.18  # Deloitte
INTERNAL_HIRE_TTF_REDUCTION_DAYS = 11  # Bersin/AMS
AVG_MANAGER_HOURS_PERF_REVIEWS_YEAR = 210  # Gartner
LABOR_BUDGET_SAVING_WITH_GOOD_SWP_PERCENT = 0.05  # Gartner
COST_OF_VACANCY_PER_DAY_ESTIMATE_FACTOR = 1.5  # Internal (conservative)

# ---------------------------
# Opereta Assumed Impact Values (Full Vision)
# ---------------------------

OPERETA_IMPACT = {
    "ttf_total_reduction_percent": 0.30,
    "recruiter_total_hours_saved_per_week_per_recruiter": 13,
    "cph_total_reduction_percent": 0.15,
    "mishire_rate_reduction_percent": 0.35,
    "shift_shock_turnover_reduction_percent": 0.60,
    "role_def_manager_time_reduction_percent": 0.75,
    "interview_scheduling_time_reduction_percent": 0.90,
    "interviewer_hours_per_hire_reduction_percent": 0.25,
    "time_to_productivity_reduction_percent": 0.35,
    "onboarding_early_turnover_reduction_percent": 0.65,
    "internal_fill_rate_increase_points": 0.20,
    "internal_mobility_retention_improvement_percent_of_turnover": 0.15,
    "productivity_gain_from_better_pm_percent_of_payroll_segment": 0.03,
    "turnover_reduction_from_better_pm_percent_of_turnover": 0.30,
    "critical_skill_shortage_cost_reduction_percent": 0.60,
    "labor_budget_swp_total_saving_percent": 0.04,
}

# ---------------------------
# Tier Definitions
# ---------------------------

TIER_DATA = {
    "Mid-Market": {
        "employee_range": "500-1,000",
        "avg_employees": 750,
        "annual_hires_percent": 0.15,
        "avg_annual_salary": 75000,
        "avg_recruiter_salary": 70000,
        "default_num_recruiters": 3,
        "opereta_target_annual_price": 100000,
        "target_value_range": "$0.5M - $0.6M",
        "target_roi_percent": "~500%",
    },
    "Lower Enterprise": {
        "employee_range": "1,001-5,000",
        "avg_employees": 3000,
        "annual_hires_percent": 0.12,
        "avg_annual_salary": 85000,
        "avg_recruiter_salary": 75000,
        "default_num_recruiters": 8,
        "opereta_target_annual_price": 200000,
        "target_value_range": "$1.5M - $1.7M",
        "target_roi_percent": "~750%",
    },
    "Mid Enterprise": {
        "employee_range": "5,001-10,000",
        "avg_employees": 7500,
        "annual_hires_percent": 0.10,
        "avg_annual_salary": 95000,
        "avg_recruiter_salary": 80000,
        "default_num_recruiters": 15,
        "opereta_target_annual_price": 450000,
        "target_value_range": "$4.3M - $5.0M",
        "target_roi_percent": "~900%+",
    },
    "Large Enterprise": {
        "employee_range": "10,000+",
        "avg_employees": 15000,
        "annual_hires_percent": 0.10,
        "avg_annual_salary": 100000,
        "avg_recruiter_salary": 85000,
        "default_num_recruiters": 30,
        "opereta_target_annual_price": 800000,
        "target_value_range": "$10M - $12M",
        "target_roi_percent": "~1000%+",
    },
} 