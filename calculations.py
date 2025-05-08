"""calculations.py
Core financial-impact calculations for the Opereta ROI calculator.
All heavy-lift math lives here so the Streamlit front-end stays tidy.
"""

from __future__ import annotations

from typing import Dict, List, Tuple

import pandas as pd

from constants import (
    AVG_TIME_TO_FILL_DAYS,
    AVG_COST_PER_HIRE_SHRM,
    AVG_COST_PER_HIRE_SMALL_BIZ,
    AVG_TIME_TO_PRODUCTIVITY_MONTHS,
    COST_TO_REPLACE_PERCENT_OF_SALARY,
    COST_OF_VACANCY_PER_DAY_ESTIMATE_FACTOR,
    EXTERNAL_HIRE_SALARY_PREMIUM_PERCENT,
    INTERVIEWS_PER_HIRE,
    NEW_HIRES_LEAVING_IN_90_DAYS_PERCENT,
    OPERETA_IMPACT,
    RECRUITER_AVG_HOURLY_RATE,
)

__all__ = [
    "calculate_daily_salary",
    "calculate_cost_of_vacancy_per_day",
    "compute_all_savings",
]


def calculate_daily_salary(annual_salary: float) -> float:
    """Convert an annual salary to its approximate daily equivalent.

    Assumes 260 working days/year (52 weeks × 5 days).
    """
    return annual_salary / 260.0


def calculate_cost_of_vacancy_per_day(annual_salary: float) -> float:
    """Estimate the productivity cost per unfilled day of a given role."""
    return calculate_daily_salary(annual_salary) * COST_OF_VACANCY_PER_DAY_ESTIMATE_FACTOR


def _baseline_cost_per_hire(num_employees: int) -> float:
    """Return baseline cost ‑ per-hire figure based on company size."""
    return (
        AVG_COST_PER_HIRE_SHRM if num_employees >= 500 else AVG_COST_PER_HIRE_SMALL_BIZ
    )


def compute_all_savings(
    *,
    num_employees: int,
    annual_hires: int,
    avg_annual_salary: float,
    avg_recruiter_salary: float,
    num_recruiters: int,
    impact: Dict[str, float] | None = None,
) -> Tuple[List[Dict[str, float]], float]:
    """Return a list of savings line-items and the combined annual total.

    This logic mirrors the original calculations in *ROI Calc Investor.py*
    but is encapsulated for reusability and easier unit testing.
    """

    all_savings_details: List[Dict[str, float]] = []
    total_annual_savings: float = 0.0

    # Use supplied impact dict or default global constants
    impact = impact or OPERETA_IMPACT

    # ---------- Baseline values ---------- #
    current_time_to_fill_days = AVG_TIME_TO_FILL_DAYS
    current_cost_per_hire = _baseline_cost_per_hire(num_employees)
    current_mishire_rate_percent = 0.15  # Industry average
    current_early_turnover_90_days_percent = NEW_HIRES_LEAVING_IN_90_DAYS_PERCENT
    current_annual_voluntary_turnover_percent = 0.12  # Baseline industry average
    current_internal_fill_rate_percent = 0.24  # Baseline from research

    # ---------- 1. Hiring Process Optimisation ---------- #
    daily_vacancy_cost = calculate_cost_of_vacancy_per_day(avg_annual_salary)
    ttf_reduction_days = current_time_to_fill_days * impact["ttf_total_reduction_percent"]
    savings_ttf = ttf_reduction_days * daily_vacancy_cost * annual_hires
    all_savings_details.append(
        {
            "Category": "1. Hiring Process Optimization",
            "Area": "Reduced Time-to-Fill",
            "Annual Savings ($)": savings_ttf,
        }
    )
    total_annual_savings += savings_ttf

    recruiter_hours_saved_annual = (
        impact["recruiter_total_hours_saved_per_week_per_recruiter"] * 50 * num_recruiters
    )
    savings_recruiter_time = recruiter_hours_saved_annual * (
        avg_recruiter_salary / 2080.0
    )
    all_savings_details.append(
        {
            "Category": "1. Hiring Process Optimization",
            "Area": "Increased Recruiter Productivity",
            "Annual Savings ($)": savings_recruiter_time,
        }
    )
    total_annual_savings += savings_recruiter_time

    cph_reduction_amount = current_cost_per_hire * impact["cph_total_reduction_percent"]
    savings_cph = cph_reduction_amount * annual_hires
    all_savings_details.append(
        {
            "Category": "1. Hiring Process Optimization",
            "Area": "Lower Cost-Per-Hire",
            "Annual Savings ($)": savings_cph,
        }
    )
    total_annual_savings += savings_cph

    # ---------- 2. Hiring Quality & Mis-Hires ---------- #
    avg_cost_of_mishire = avg_annual_salary * 0.30  # DOL estimate
    current_annual_mishires = annual_hires * current_mishire_rate_percent
    mishires_reduced = current_annual_mishires * impact["mishire_rate_reduction_percent"]
    savings_mishires = mishires_reduced * avg_cost_of_mishire
    all_savings_details.append(
        {
            "Category": "2. Enhanced Hiring Quality",
            "Area": "Reduced Mis-Hire Costs",
            "Annual Savings ($)": savings_mishires,
        }
    )
    total_annual_savings += savings_mishires

    # ---------- 3. Role Definition & Strategic Alignment ---------- #
    cost_per_early_leaver_replacement = avg_annual_salary * COST_TO_REPLACE_PERCENT_OF_SALARY
    num_early_leavers_shift_shock = (
        annual_hires * current_early_turnover_90_days_percent * 0.43
    )
    shift_shock_leavers_prevented = num_early_leavers_shift_shock * impact[
        "shift_shock_turnover_reduction_percent"
    ]
    savings_shift_shock = shift_shock_leavers_prevented * cost_per_early_leaver_replacement
    all_savings_details.append(
        {
            "Category": "3. Strategic Role Alignment",
            "Area": "Lower Early Attrition (Role Clarity)",
            "Annual Savings ($)": savings_shift_shock,
        }
    )
    total_annual_savings += savings_shift_shock

    # ---------- 4. Interviewing & Assessment ---------- #
    num_interviews_annually = annual_hires * INTERVIEWS_PER_HIRE
    time_saved_scheduling = (
        num_interviews_annually
        * 1
        * impact["interview_scheduling_time_reduction_percent"]
    )
    savings_interview_sched = time_saved_scheduling * RECRUITER_AVG_HOURLY_RATE
    all_savings_details.append(
        {
            "Category": "4. Optimized Interviewing",
            "Area": "Efficient Interview Scheduling",
            "Annual Savings ($)": savings_interview_sched,
        }
    )
    total_annual_savings += savings_interview_sched

    # ---------- 5. Onboarding & Time-to-Productivity ---------- #
    current_ramp_months = AVG_TIME_TO_PRODUCTIVITY_MONTHS
    ramp_months_opereta = current_ramp_months * (
        1 - impact["time_to_productivity_reduction_percent"]
    )
    months_ramp_saved = current_ramp_months - ramp_months_opereta
    savings_faster_ttp = (
        (avg_annual_salary / 12)
        * months_ramp_saved
        * 0.5
        * annual_hires
    )
    all_savings_details.append(
        {
            "Category": "5. Accelerated Onboarding",
            "Area": "Faster Time-to-Productivity",
            "Annual Savings ($)": savings_faster_ttp,
        }
    )
    total_annual_savings += savings_faster_ttp

    # ---------- 6. Internal Mobility & Skill Visibility ---------- #
    external_hires_baseline = annual_hires * (1 - current_internal_fill_rate_percent)
    new_internal_fill_rate = current_internal_fill_rate_percent + impact[
        "internal_fill_rate_increase_points"
    ]
    external_hires_avoided = annual_hires * (
        new_internal_fill_rate - current_internal_fill_rate_percent
    )
    cost_saving_per_internal_hire = (
        avg_annual_salary * EXTERNAL_HIRE_SALARY_PREMIUM_PERCENT
    ) + (current_cost_per_hire * 0.5)
    savings_internal_fill = external_hires_avoided * cost_saving_per_internal_hire
    all_savings_details.append(
        {
            "Category": "6. Improved Internal Mobility",
            "Area": "Increased Internal Fill Rate & Cost Savings",
            "Annual Savings ($)": savings_internal_fill,
        }
    )
    total_annual_savings += savings_internal_fill

    # ---------- 7. Performance Management & Development ---------- #
    total_payroll = num_employees * avg_annual_salary
    savings_pm_productivity = (
        total_payroll * 0.20
    ) * impact["productivity_gain_from_better_pm_percent_of_payroll_segment"]
    all_savings_details.append(
        {
            "Category": "7. Effective Performance & Development",
            "Area": "Productivity Gains from Engaged PM",
            "Annual Savings ($)": savings_pm_productivity,
        }
    )
    total_annual_savings += savings_pm_productivity

    num_voluntary_leavers = num_employees * current_annual_voluntary_turnover_percent
    leavers_prevented_pm = num_voluntary_leavers * impact[
        "turnover_reduction_from_better_pm_percent_of_turnover"
    ]
    savings_pm_turnover = leavers_prevented_pm * (
        avg_annual_salary * COST_TO_REPLACE_PERCENT_OF_SALARY
    )
    all_savings_details.append(
        {
            "Category": "7. Effective Performance & Development",
            "Area": "Reduced Turnover (Better Growth Paths)",
            "Annual Savings ($)": savings_pm_turnover,
        }
    )
    total_annual_savings += savings_pm_turnover

    # ---------- 8. Strategic Workforce Planning ---------- #
    savings_swp_labor_opt = total_payroll * impact[
        "labor_budget_swp_total_saving_percent"
    ]
    all_savings_details.append(
        {
            "Category": "8. Strategic Workforce Planning",
            "Area": "Optimized Labor Budget & Skill Deployment",
            "Annual Savings ($)": savings_swp_labor_opt,
        }
    )
    total_annual_savings += savings_swp_labor_opt

    return all_savings_details, total_annual_savings 