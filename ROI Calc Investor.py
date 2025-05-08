# External libs
import streamlit as st
import pandas as pd

# Internal modules
from constants import *  # Centralized constants
from calculations import compute_all_savings  # Encapsulated ROI math

# --- Apply custom theming for a professional investor-ready look ---
st.set_page_config(
    page_title="Opereta ROI Calculator - Investor Edition",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to improve appearance
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #2C3333;
    }
    .metric-label {
        font-size: 1.2rem;
        font-weight: 600;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0e5394;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #0e5394;
        color: white;
    }
    .info-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 5px;
        border-left: 5px solid #0e5394;
        margin-bottom: 20px;
    }
    .value-prop {
        border-left: 4px solid #0e5394;
        padding-left: 20px;
        margin-bottom: 30px;
    }
    .tier-header {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Additional CSS to force light palette background and improve readability
st.markdown("""
<style>
/* ---------- FORCE LIGHT PALETTE BACKGROUND ----------*/
body, .stApp, .main .block-container {
    background-color: #ffffff !important;
    color: #222222;
}

/* Adjust sidebar background */
section[data-testid="stSidebar"], .sidebar .sidebar-content {
    background-color: #f8f9fa !important;
}

/* Ensure tables look crisp in light mode */
.dataframe th {
    background-color: #f1f3f5 !important;
    color: #222222;
}
.dataframe td {
    background-color: #ffffff !important;
    color: #222222;
}
</style>
""", unsafe_allow_html=True)

# Ensure header bar and form inputs use light theme
st.markdown("""
<style>
/* Top header bar */
div[data-testid="stHeader"] {
    background-color: #ffffff !important;
}

/* Input widgets */
input, textarea, select {
    background-color: #ffffff !important;
    color: #222222 !important;
}

/* Streamlit selectbox dropdown */
div[role="combobox"] {
    background-color: #ffffff !important;
    color: #222222 !important;
}

/* Streamlit number input field */
div[data-testid="stNumberInput"] input {
    background-color: #ffffff !important;
    color: #222222 !important;
}

/* Streamlit sidebar header text */
section[data-testid="stSidebar"] h2 {
    color: #0e5394 !important;
}
</style>
""", unsafe_allow_html=True)

# Final comprehensive styling to ensure consistent light theme
st.markdown("""
<style>
/* ---------- COMPLETE LIGHT THEME OVERRIDES ----------*/

/* Streamlit app container - Force light background */
.stApp {
    background-color: #ffffff !important;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #f8f9fa !important;
    color: #212529 !important;
}

/* Configuration header in sidebar */
section[data-testid="stSidebar"] [data-testid="stImage"],
section[data-testid="stSidebar"] h1 {
    color: #0e5394 !important;
    background-color: #f8f9fa !important;
}

/* Sidebar header text */
section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] h1,
section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] h2,
section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] h3 {
    color: #0e5394 !important;
}

/* Streamlit UI elements */
.stButton button, .stDownloadButton button {
    background-color: #0e5394 !important;
    color: white !important;
    border: none !important;
}

/* Number input buttons */
div[data-testid="stNumberInput"] button {
    background-color: #f8f9fa !important;
    color: #0e5394 !important;
    border: 1px solid #dee2e6 !important;
}

/* Form inputs */
div[data-testid="stNumberInput"] input,
div[role="textbox"],
div[data-baseweb="select"] div,
div[data-baseweb="select"] input,
div[data-baseweb="select"] span {
    background-color: white !important;
    color: #212529 !important;
}

/* Selectbox */
div[data-testid="stSelectbox"] {
    background-color: white !important;
    color: #212529 !important;
}

/* Dropdown menus */
ul[role="listbox"] {
    background-color: white !important;
    color: #212529 !important;
}

/* Dropdown options */
ul[role="listbox"] li {
    background-color: white !important;
    color: #212529 !important;
}

/* Dropdown options on hover */
ul[role="listbox"] li:hover {
    background-color: #f8f9fa !important;
    color: #212529 !important;
}

/* Main page header */
div[data-testid="stHeader"] {
    background-color: white !important;
    color: #212529 !important;
}

/* Buttons in header */
div[data-testid="stHeader"] button {
    background-color: white !important;
    color: #0e5394 !important;
    border: 1px solid #dee2e6 !important;
}

/* App info button (hamburger menu) */
button[kind="headerNoPadding"] {
    background-color: white !important;
    color: #0e5394 !important;
}

/* Expander styling */
details[data-testid="stExpander"] summary {
    background-color: #f8f9fa !important;
    color: #0e5394 !important;
}

/* Code blocks - ensure light background */
pre {
    background-color: #f8f9fa !important;
    color: #212529 !important;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: #0e5394 !important;
}

/* Fixed height for card content to maintain alignment */
div.value-prop p {
    min-height: 100px;
}
</style>
""", unsafe_allow_html=True)

# --- Constants from Research (Same as before) ---
AVG_TIME_TO_FILL_DAYS = 44
AVG_COST_PER_HIRE_SHRM = 4700
AVG_COST_PER_HIRE_SMALL_BIZ = 7645
RECRUITER_INTERVIEW_SCHEDULING_TIME_MAX_HOURS = 2
RECRUITER_AVG_HOURLY_RATE = 35
AVG_CANDIDATES_PER_OPENING = 250
INTERVIEWS_PER_HIRE = 5
AVG_MISHIRE_COST_LOW = 17000
AVG_MISHIRE_COST_HIGH = 240000
MISHIRE_COST_PERCENT_OF_SALARY_DOL = 0.30
MANAGERS_TIME_ON_UNDERPERFORMERS_PERCENT = 0.17
NEW_HIRES_LEAVING_IN_90_DAYS_PERCENT = 0.30
COST_TO_REPLACE_PERCENT_OF_SALARY = 0.21 # Can be higher for key roles, this is conservative
TOP_PERFORMER_PRODUCTIVITY_MULTIPLIER_LOW = 4
AVG_TIME_TO_PRODUCTIVITY_MONTHS = 8
NEW_HIRE_TURNOVER_FIRST_45_DAYS_PERCENT = 0.20
EXTERNAL_HIRE_SALARY_PREMIUM_PERCENT = 0.18
INTERNAL_HIRE_TTF_REDUCTION_DAYS = 11
AVG_MANAGER_HOURS_PERF_REVIEWS_YEAR = 210
LABOR_BUDGET_SAVING_WITH_GOOD_SWP_PERCENT = 0.05
COST_OF_VACANCY_PER_DAY_ESTIMATE_FACTOR = 1.5 # Adjusted to be slightly more conservative for general calc

# --- Opereta's Assumed Impact (Full Vision - KEEP THESE DEFENSIBLE FOR INVESTORS) ---
OPERETA_IMPACT = {
    "ttf_total_reduction_percent": 0.30, # Total TTF reduction (combines general AI + Opereta specific)
    "recruiter_total_hours_saved_per_week_per_recruiter": 13, # Total hours (11 general + 2 Opereta)
    "cph_total_reduction_percent": 0.15, # Total CPH reduction
    "mishire_rate_reduction_percent": 0.35, # Slightly more confident for full vision
    "shift_shock_turnover_reduction_percent": 0.60,
    "role_def_manager_time_reduction_percent": 0.75,
    "interview_scheduling_time_reduction_percent": 0.90,
    "interviewer_hours_per_hire_reduction_percent": 0.25,
    "time_to_productivity_reduction_percent": 0.35,
    "onboarding_early_turnover_reduction_percent": 0.65,
    "internal_fill_rate_increase_points": 0.20, # More ambitious target for full vision
    "internal_mobility_retention_improvement_percent_of_turnover": 0.15, # 15% of voluntary turnover saved
    "productivity_gain_from_better_pm_percent_of_payroll_segment": 0.03, # 3% gain on 20% of payroll
    "turnover_reduction_from_better_pm_percent_of_turnover": 0.30, # 30% reduction of voluntary turnover
    "critical_skill_shortage_cost_reduction_percent": 0.60,
    "labor_budget_swp_total_saving_percent": 0.04, # Total SWP impact (e.g. 4% of labor budget)
}

# --- Tier Definitions (Align with your investor slide) ---
TIER_DATA = {
    "Mid-Market": {
        "employee_range": "500-1,000",
        "avg_employees": 750,
        "annual_hires_percent": 0.15,
        "avg_annual_salary": 75000,
        "avg_recruiter_salary": 70000,
        "default_num_recruiters": 3, # (750 * 0.15) / 40 hires per recruiter
        "opereta_target_annual_price": 100000, # Example price for this tier
        "target_value_range": "$0.5M - $0.6M",
        "target_roi_percent": "~500%"
    },
    "Lower Enterprise": {
        "employee_range": "1,001-5,000",
        "avg_employees": 3000,
        "annual_hires_percent": 0.12,
        "avg_annual_salary": 85000,
        "avg_recruiter_salary": 75000,
        "default_num_recruiters": 8, # (3000 * 0.12) / 45
        "opereta_target_annual_price": 200000, # Example price
        "target_value_range": "$1.5M - $1.7M",
        "target_roi_percent": "~750%"
    },
    "Mid Enterprise": {
        "employee_range": "5,001-10,000",
        "avg_employees": 7500,
        "annual_hires_percent": 0.10,
        "avg_annual_salary": 95000,
        "avg_recruiter_salary": 80000,
        "default_num_recruiters": 15, # (7500 * 0.10) / 50
        "opereta_target_annual_price": 450000, # Example price
        "target_value_range": "$4.3M - $5.0M",
        "target_roi_percent": "~900%+" # Adjusted to match your higher values
    },
    "Large Enterprise": {
        "employee_range": "10,000+",
        "avg_employees": 15000, # Example within range
        "annual_hires_percent": 0.10,
        "avg_annual_salary": 100000,
        "avg_recruiter_salary": 85000,
        "default_num_recruiters": 30, # (15000 * 0.10) / 50
        "opereta_target_annual_price": 800000, # Example price
        "target_value_range": "$10M - $12M",
        "target_roi_percent": "~1000%+"
    }
}

# --- Main App UI ---
st.image("https://storage.googleapis.com/komodobucket/opereta_logo.png", width=200) # Replace with your logo URL or path

# Create a more professional header/intro
st.markdown("<div class='tier-header'>", unsafe_allow_html=True)
st.title("Opereta: Full Vision Talent Intelligence Hub - Investor ROI Demonstration")

intro_col1, intro_col2 = st.columns([2,1])
with intro_col1:
    st.markdown("""
    <div class="info-box">
    <h3>💡 The Ground Truth Talent Intelligence Opportunity</h3>
    <p>Traditional talent acquisition and management are fraught with inefficiencies: lengthy hiring cycles (avg. 44 days), 
    high costs per hire (avg. $4,700+), significant expenses from mis-hires (30% of first-year salary), and lost productivity 
    from disengaged employees and poorly aligned roles.</p>
    
    <p>Opereta addresses these critical pain points by providing a unified, AI-driven platform that enhances strategic 
    capabilities across the entire talent lifecycle—from smarter hiring and onboarding to optimized internal mobility 
    and performance development.</p>
    </div>
    """, unsafe_allow_html=True)

with intro_col2:
    st.markdown("""
    <div style="background-color: #e8f4f8; padding: 15px; border-radius: 5px; height: 100%;">
    <h3>🎯 Key ROI Drivers</h3>
    <ul>
      <li>Reduced Time-to-Fill</li>
      <li>Lower Hiring Costs</li>
      <li>Improved Hiring Quality</li>
      <li>Enhanced Internal Mobility</li>
      <li>Optimized Performance</li>
      <li>Strategic Workforce Planning</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Tier Selection ---
st.sidebar.markdown("""
<div style="background-color: #0e5394; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
    <h2 style="color: white; margin: 0; font-size: 22px;">⚙️ Configuration</h2>
</div>
""", unsafe_allow_html=True)

selected_tier_name = st.sidebar.selectbox("Select Customer Tier:", list(TIER_DATA.keys()))
tier_config = TIER_DATA[selected_tier_name]

# --- Tier-Specific Inputs styled better ---
st.sidebar.markdown(f"""
<div style="background-color: #f0f2f6; padding: 10px; border-radius: 5px; margin: 15px 0;">
    <h3 style="margin-top: 0; font-size: 18px; color: #0e5394;">Customer Profile: {selected_tier_name}</h3>
    <p style="font-size: 14px; margin-bottom: 10px; color: #596e79;">({tier_config['employee_range']} Employees)</p>
</div>
""", unsafe_allow_html=True)

num_employees = st.sidebar.number_input("Avg. Number of Employees in Tier", value=tier_config["avg_employees"], disabled=True)
annual_hires_percent = st.sidebar.number_input("Annual Hiring Rate (% of Employees)", value=tier_config["annual_hires_percent"], disabled=True, format="%.2f")
annual_hires = int(num_employees * annual_hires_percent)
st.sidebar.markdown(f"<p style='color: #596e79; font-size: 14px;'>Annual Hires: <b>{annual_hires}</b></p>", unsafe_allow_html=True)

avg_annual_salary = st.sidebar.number_input("Average Annual Salary ($)", value=tier_config["avg_annual_salary"], disabled=True)
avg_recruiter_salary = st.sidebar.number_input("Average Recruiter Salary ($)", value=tier_config["avg_recruiter_salary"], disabled=True)
num_recruiters = st.sidebar.number_input("Number of Recruiters", value=tier_config["default_num_recruiters"], disabled=True)

# Add a styled pricing section
st.sidebar.markdown("""
<div style="background-color: #e1f5fe; padding: 15px; border-radius: 5px; margin: 20px 0;">
    <h3 style="margin-top: 0; color: #0277bd; font-size: 16px;">Opereta Pricing</h3>
""", unsafe_allow_html=True)
opereta_annual_cost = st.sidebar.number_input("Opereta Target Annual Price for this Tier ($)", value=tier_config["opereta_target_annual_price"], disabled=False) # Allow investor to see price impact
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Better styling for the impact assumptions
st.sidebar.markdown("""
<div style="background-color: #fffde7; padding: 15px; border-radius: 5px; border-left: 4px solid #fbc02d;">
    <h3 style="margin-top: 0; color: #5d4037; font-size: 16px;">Impact Assumptions</h3>
    <p style="font-size: 14px;">The 'Opereta Impact %' assumptions below are targets for our comprehensive Full Vision product. These are based on industry benchmarks for AI in HR, with Opereta aiming to deliver superior results due to its unique 'Ground Truth' data differentiators and a holistic approach to the talent lifecycle.</p>
    <p style="font-size: 14px;">We believe these are defensible and form the basis of our strong value proposition.</p>
</div>
""", unsafe_allow_html=True)

# Add a visualization of key impacts (optional additional feature)
st.sidebar.markdown("""
<div style="margin-top: 20px;">
    <h4 style="font-size: 16px; color: #0e5394;">Key Impact Metrics</h4>
</div>
""", unsafe_allow_html=True)

# --- Scenario Sensitivity ---
SCENARIOS = {
    "Conservative (50% Impact)": 0.5,
    "Base (100% Impact)": 1.0,
    "Aggressive (125% Impact)": 1.25,
}

selected_scenario_label = st.sidebar.selectbox("Assumption Scenario:", list(SCENARIOS.keys()), index=1)
scenario_multiplier = SCENARIOS[selected_scenario_label]

# Build a scenario-scaled impact dict
scaled_impact = {k: v * scenario_multiplier for k, v in OPERETA_IMPACT.items()}

# Display a few key impact metrics as a horizontal bar chart using HTML/CSS
impact_metrics = [
    {"name": "Time-to-Fill Reduction", "value": f"{scaled_impact['ttf_total_reduction_percent']*100:.0f}%"},
    {"name": "Mis-hire Reduction", "value": f"{scaled_impact['mishire_rate_reduction_percent']*100:.0f}%"},
    {"name": "Internal Fill Rate Increase", "value": f"{scaled_impact['internal_fill_rate_increase_points']*100:.0f}%"},
    {"name": "Time-to-Productivity Reduction", "value": f"{scaled_impact['time_to_productivity_reduction_percent']*100:.0f}%"}
]

for metric in impact_metrics:
    percentage = float(metric["value"].strip('%'))
    st.sidebar.markdown(f"""
    <div style="margin-bottom: 10px;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
            <span style="font-size: 13px;">{metric["name"]}</span>
            <span style="font-size: 13px; font-weight: bold;">{metric["value"]}</span>
        </div>
        <div style="background-color: #e0e0e0; height: 8px; border-radius: 4px; overflow: hidden;">
            <div style="background-color: #0e5394; width: {percentage}%; height: 100%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Current Baseline Values (Can be average industry stats for simplicity for investors) ---
current_time_to_fill_days = AVG_TIME_TO_FILL_DAYS
current_cost_per_hire = AVG_COST_PER_HIRE_SHRM if num_employees >=500 else AVG_COST_PER_HIRE_SMALL_BIZ
current_mishire_rate_percent = 0.15 # Baseline industry average often cited
current_early_turnover_90_days_percent = NEW_HIRES_LEAVING_IN_90_DAYS_PERCENT
current_annual_voluntary_turnover_percent = 0.12 # Baseline industry average
current_internal_fill_rate_percent = 0.24 # Baseline from research

st.caption("Note: 'Current Baseline Values' are derived from established industry research and benchmarks, as detailed in Opereta's comprehensive ROI data. These represent typical challenges Opereta addresses.")

# --- Calculations (Simplified for Investor View) ---
# Compute savings via centralised calculations module (cached)

@st.cache_data(show_spinner=False)
def _get_savings(
    num_employees: int,
    annual_hires: int,
    avg_annual_salary: float,
    avg_recruiter_salary: float,
    num_recruiters: int,
    impact: dict,
):
    return compute_all_savings(
        num_employees=num_employees,
        annual_hires=annual_hires,
        avg_annual_salary=avg_annual_salary,
        avg_recruiter_salary=avg_recruiter_salary,
        num_recruiters=num_recruiters,
        impact=impact,
    )


all_savings_details, total_annual_savings = _get_savings(
    num_employees,
    annual_hires,
    avg_annual_salary,
    avg_recruiter_salary,
    num_recruiters,
    scaled_impact,
)

# --- Display ROI Summary for Investor ---
net_annual_benefit = total_annual_savings - opereta_annual_cost
# Ensure roi_percentage is defined before being used for pre-formatting
if opereta_annual_cost > 0:
    roi_percentage_calc = (net_annual_benefit / opereta_annual_cost) * 100
else:
    roi_percentage_calc = float('inf') # Or some other indicator for undefined ROI

payback_period_months = (opereta_annual_cost / (total_annual_savings / 12)) if total_annual_savings > 0 else float('inf')

# Pre-format strings for use throughout the UI
total_savings_str = f"${total_annual_savings:,.0f}"
opereta_cost_str = f"${opereta_annual_cost:,.0f}"
roi_percentage_display = f"{roi_percentage_calc:.0f}%" if opereta_annual_cost > 0 and total_annual_savings > 0 else "N/A"
payback_str = f"{payback_period_months:.1f} months" if total_annual_savings > 0 else "N/A"

# Create an impressive header for the ROI section
st.markdown(f"""
<div style="background: linear-gradient(90deg, #f0f2f6 0%, #ffffff 100%); padding: 20px; border-radius: 10px; margin-bottom: 30px;">
    <h2 style="margin-bottom: 20px; color: #0e5394;">📈 Projected Annual ROI for {selected_tier_name} Clients</h2>
    <p style="font-style: italic; margin-bottom: 25px;">Based on an average company of <b>{num_employees:,} employees</b> in this tier</p>
</div>
""", unsafe_allow_html=True)

# Create a visually impressive metrics row
metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

with metrics_col1:
    st.markdown(f"""
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;">
        <p class="metric-label">Total Annual Value</p>
        <p class="metric-value">{total_savings_str}</p>
        <p style="font-size: 0.9rem; color: #596e79;">Matches Target: {tier_config['target_value_range']}</p>
    </div>
    """, unsafe_allow_html=True)

with metrics_col2:
    st.markdown(f"""
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;">
        <p class="metric-label">Opereta Annual Price</p>
        <p class="metric-value">{opereta_cost_str}</p>
        <p style="font-size: 0.9rem; color: #596e79;">Target pricing for this tier</p>
    </div>
    """, unsafe_allow_html=True)

with metrics_col3:
    st.markdown(f"""
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;">
        <p class="metric-label">Customer ROI</p>
        <p class="metric-value" style="color: #2e7d32;">{roi_percentage_display}</p>
        <p style="font-size: 0.9rem; color: #596e79;">Matches Target: {tier_config['target_roi_percent']}</p>
    </div>
    """, unsafe_allow_html=True)

with metrics_col4:
    st.markdown(f"""
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;">
        <p class="metric-label">Payback Period</p>
        <p class="metric-value">{payback_str}</p>
        <p style="font-size: 0.9rem; color: #596e79;">Time to recoup investment</p>
    </div>
    """, unsafe_allow_html=True)

# --- Expandable Details ---
with st.expander(f"Click for Detailed ROI Breakdown for {selected_tier_name} (Justification for Investor Slide)"):
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="color: #0e5394;"><strong>Value Generation Framework</strong></h3>
        <p>The total estimated annual value is derived from quantifiable improvements across the talent lifecycle,
        powered by Opereta's "Ground Truth" Talent Intelligence. The sections below detail the problem areas,
        their typical costs to businesses, and how Opereta's targeted interventions generate significant savings.</p>
    </div>
    """, unsafe_allow_html=True)

    # Fetch data from the markdown content (conceptual - in a real app, this might be loaded from the file)
    # For this edit, we will manually insert representative text based on the markdown.

    category_explanations = {
        "1. Hiring Process Optimization": {
            "problem": "**The Problem:** Businesses face lengthy time-to-fill (avg. 44 days), high cost-per-hire (avg. $4,700), and massive recruiter workloads (e.g., 67% spend 30 mins-2 hours to schedule one interview). This leads to lost productivity valued at tens of thousands per vacancy.",
            "solution": "**Opereta's Impact:** By optimizing sourcing, screening, and scheduling, Opereta reduces time-to-fill (by ~25-30% based on AI platform benchmarks), increases recruiter capacity (saving ~11 hours/week/recruiter), and lowers direct hiring costs (e.g., reducing agency reliance).",
            "areas": ["Reduced Time-to-Fill", "Increased Recruiter Productivity", "Lower Cost-Per-Hire"]
        },
        "2. Enhanced Hiring Quality": {
            "problem": "**The Problem:** Mis-hires are common (75% of employers admit to them) and costly, ranging from $17,000 to 30% of first-year salary. Poor hires also drag down team performance (managers spend ~17% of time on underperformers) and fuel early turnover.",
            "solution": "**Opereta's Impact:** AI-driven matching and assessment improve quality-of-hire, directly reducing mis-hire rates and associated costs. Better hires lead to higher productivity (top talent can be 8x more productive) and improved retention.",
            "areas": ["Reduced Mis-Hire Costs"]
        },
        "3. Strategic Role Alignment": {
            "problem": "**The Problem:** 'Shift shock' from poorly defined roles causes early attrition (43% of early leavers cite mismatched expectations). Misalignment with business strategy (a challenge for 71% of orgs) leads to talent not being optimally deployed and strategic initiatives stalling.",
            "solution": "**Opereta's Impact:** Opereta ensures precise role definitions based on success-driving skills and aligns talent to strategic value. This reduces early turnover from role ambiguity and ensures human capital is deployed effectively, improving strategy execution.",
            "areas": ["Lower Early Attrition (Role Clarity)"]
        },
        "4. Optimized Interviewing": {
            "problem": "**The Problem:** Interview processes are often lengthy (avg. 23 days) and time-consuming for managers (e.g., ~21% more interviewer hours per hire recently). Unstructured interviews have low predictive validity, contributing to mis-hires, and a poor candidate experience can lose top talent (53% cite bad questions as a deal-breaker).",
            "solution": "**Opereta's Impact:** Opereta streamlines interview scheduling (saving hours per interview), enables structured, data-driven assessments to improve predictive quality, and reduces the overall interview load on hiring teams, while enhancing candidate experience.",
            "areas": ["Efficient Interview Scheduling"]
        },
        "5. Accelerated Onboarding": {
            "problem": "**The Problem:** New hires take an average of 8 months to reach full productivity, representing significant lost output. Poor onboarding leads to high early turnover (20% in first 45 days) because only 12% of employees feel their company excels at it.",
            "solution": "**Opereta's Impact:** Opereta provides structured, personalized onboarding experiences that can improve new hire productivity by ~50% and significantly increase retention (strong onboarding can retain 50% more new hires), getting employees to contribute value faster.",
            "areas": ["Faster Time-to-Productivity"]
        },
        "6. Improved Internal Mobility": {
            "problem": "**The Problem:** Low internal fill rates (avg. 24%) mean companies over-rely on costly external hires (18% salary premium, plus recruiting costs). Lack of visibility into internal skills leads to skill gaps and high turnover from employees seeing no growth paths (companies with high mobility retain employees 41% longer).",
            "solution": "**Opereta's Impact:** Opereta's talent marketplace provides visibility into internal skills, boosting internal fill rates (e.g., by 30%+), saving significantly on external hiring costs, filling roles faster, and retaining top talent by offering clear career pathways.",
            "areas": ["Increased Internal Fill Rate & Cost Savings"]
        },
        "7. Effective Performance & Development": {
            "problem": "**The Problem:** Traditional performance reviews are often ineffective (90% fail to improve performance), yet time-consuming (managers spend ~210 hours/year). This leads to skill stagnation, disengagement (only 21% globally engaged), and turnover (24% would quit due to poor PM).",
            "solution": "**Opereta's Impact:** Opereta facilitates continuous, AI-backed performance management and development. This increases productivity (engaged teams are ~12-21% more productive/profitable), reduces turnover (by ~15%+ through regular feedback), and builds a stronger talent pipeline.",
            "areas": ["Productivity Gains from Engaged PM", "Reduced Turnover (Better Growth Paths)"]
        },
        "8. Strategic Workforce Planning": {
            "problem": "**The Problem:** Lack of workforce foresight (71% struggle to align workforce to strategy) leads to costly reactive decisions like talent shortages or overstaffing. Skills gaps alone can cost enterprises ~$59M/year per enterprise in lost productivity.",
            "solution": "**Opereta's Impact:** Opereta enables proactive, AI-driven SWP, helping predict future talent needs, optimize workforce size/mix, and bridge skill gaps through reskilling (1/6th cost of hiring new). This can save 5-7% of labor budget annually and ensure strategic readiness.",
            "areas": ["Optimized Labor Budget & Skill Deployment"]
        }
    }

    # Convert to dataframe to organize data - this stays the same
    df_savings_details = pd.DataFrame(all_savings_details) # Define df_savings_details here

    # Display detailed explanations for each category
    unique_categories = df_savings_details["Category"].unique()
    for category_name in unique_categories:
        if category_name in category_explanations:
            st.markdown(f"""
            <div style="margin-bottom: 30px; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <h3 style="color: #0e5394; border-bottom: 1px solid #e0e0e0; padding-bottom: 10px;">{category_name}</h3>
                <div style="margin: 15px 0;">
                    <div style="margin-bottom: 15px; background-color: #fafafa; padding: 15px; border-left: 4px solid #ff6b6b; border-radius: 4px;">
                        {category_explanations[category_name]["problem"]}
                    </div>
                    <div style="background-color: #f0f8ff; padding: 15px; border-left: 4px solid #0e5394; border-radius: 4px;">
                        {category_explanations[category_name]["solution"]}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Display specific line items under this category
            category_items_df = df_savings_details[df_savings_details["Category"] == category_name][["Area", "Annual Savings ($)"]]
            category_items_df["Annual Savings ($)"] = category_items_df["Annual Savings ($)"].apply(lambda x: f"${x:,.0f}")
            
            # Convert DataFrame to HTML for better styling
            html_table = category_items_df.to_html(index=False)
            styled_table = f"""
            <div style="margin-top: 15px;">
                <h4 style="font-size: 1rem; margin-bottom: 10px;">Projected Savings in This Category:</h4>
                <div style="max-height: 200px; overflow-y: auto;">
                    {html_table.replace('<table', '<table style="width:100%; border-collapse: collapse;" class="dataframe"')
                     .replace('<th>', '<th style="text-align: left; padding: 8px; background-color: #f2f2f2; border-bottom: 2px solid #ddd;">')
                     .replace('<td>', '<td style="text-align: left; padding: 8px; border-top: 1px solid #ddd;">')}
                </div>
            </div>
            """
            st.markdown(styled_table, unsafe_allow_html=True)

            # --- Detailed math formulas (optional) ---
            formulas_lookup = {
                "1. Hiring Process Optimization": """#### 🔍 Calculation Details\n- **Reduced TTF:** `TTF_saved_days × Daily Vacancy Cost × Annual Hires`\n- **Recruiter Productivity:** `Hours saved × Hourly recruiter cost`\n- **Lower CPH:** `Baseline CPH × Reduction % × Annual Hires`\n\n_See `docs/value_generation_framework.md#1-hiring-process-optimization` for full walkthrough and source links._""",
                "2. Enhanced Hiring Quality": """#### 🔍 Calculation Details\n`Mis-hire Cost × Bad Hires Prevented`\n\nWhere:\n- `Mis-hire Cost = Avg Salary × 30 %` (US DoL)\n- `Bad Hires Prevented = Annual Hires × 15 % mis-hire rate × 35 % reduction`\n\n_See `docs/value_generation_framework.md#2-enhanced-hiring-quality` for worked example._""",
                "3. Strategic Role Alignment": """#### 🔍 Calculation Details\n`Early_Turnover × 43 % shift-shock × 60 % reduction × Replacement_Cost`\n\nReplacement cost = `Avg Salary × 21 %`\n\n_See `docs/value_generation_framework.md#3-strategic-role-alignment` for full breakdown._""",
                "4. Optimized Interviewing": """#### 🔍 Calculation Details\n`Interviews_per_year × Time_saved × Recruiter_hourly_rate`\n\nTime saved ≈ 0.9 h/interview (90 % reduction).\n\n_See `docs/value_generation_framework.md#4-optimized-interviewing`._""",
                "5. Accelerated Onboarding": """#### 🔍 Calculation Details\n`(Avg Sal / 12) × Months_saved × 50 % productivity_gap × Annual_Hires`\n\nMonths_saved = `8 mo × 35 %`\n\n_See `docs/value_generation_framework.md#5-accelerated-onboarding`._""",
                "6. Improved Internal Mobility": """#### 🔍 Calculation Details\n`External_Hires_Avoided × (Salary_Premium + 0.5 × CPH)`\n\nExternal_Hires_Avoided derives from 20 pp increase in internal fill rate.\n\n_See `docs/value_generation_framework.md#6-improved-internal-mobility`._""",
                "7. Effective Performance & Development": """#### 🔍 Calculation Details\n• **Productivity Gains:** `Total_Payroll × 20 % segment × 3 % uplift`\n• **Turnover Savings:** `Voluntary Leavers × 30 % reduction × Replacement_Cost`\n\n_See `docs/value_generation_framework.md#7-effective-performance--development`._""",
                "8. Strategic Workforce Planning": """#### 🔍 Calculation Details\n`Total_Payroll × 4 %` labor budget optimisation.\n\n_See `docs/value_generation_framework.md#8-strategic-workforce-planning`._""",
            }

            if category_name in formulas_lookup:
                st.markdown(formulas_lookup[category_name], unsafe_allow_html=True)
        else:
            # Fallback for any category not explicitly defined (should not happen if all_savings_details matches)
            st.subheader(category_name)
            category_items_df = df_savings_details[df_savings_details["Category"] == category_name][["Area", "Annual Savings ($)"]]
            category_items_df["Annual Savings ($)"] = category_items_df["Annual Savings ($)"].apply(lambda x: f"${x:,.0f}")
            st.dataframe(category_items_df, use_container_width=True, hide_index=True)
            st.markdown("---")

    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 5px; margin-top: 30px; border-left: 5px solid #0e5394;">
        <h4 style="color: #0e5394;">Note on 'Opereta Impact' Assumptions:</h4>
        <p>The projected savings are based on Opereta achieving specific impact percentages (defined as <code>OPERETA_IMPACT</code> in the model).
        These percentages reflect the comprehensive capabilities of our Full Vision product and its "Ground Truth" data differentiators.
        They are targets built upon industry benchmarks for AI in HR, with Opereta aiming to deliver superior results due to its unique, contextual approach.
        We believe these are achievable and form the basis of our strong value proposition.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Create a visually impressive "Why This Matters" section
st.markdown("""
<div style="background: linear-gradient(90deg, #f0f2f6 0%, #ffffff 100%); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
    <h2 style="margin-bottom: 20px; color: #0e5394;">Why This Matters to Our Investors</h2>
</div>
""", unsafe_allow_html=True)

# Define the items as a list for easier maintenance
investor_value_props = [
    {
        "icon": "💰",
        "title": "Massive & Quantifiable Value Creation",
        "content": f"Opereta is projected to deliver **{total_savings_str}** in annual value for a typical {selected_tier_name} client. This isn't just incremental improvement; it addresses systemic issues that cost businesses dearly (e.g., an average of $4,700 per hire, $17k-$240k per mis-hire, and managers spending 17% of their time on underperformers)."
    },
    {
        "icon": "📈",
        "title": "Strong Justification for Pricing & Compelling ROI",
        "content": f"The significant value delivered (**{total_savings_str}**) provides a robust foundation for Opereta's target annual price of **{opereta_cost_str}** for this tier. This ensures a compelling and easily justifiable ROI for customers (estimated at **{roi_percentage_display}**), making Opereta a high-value, strategic investment rather than a cost center."
    },
    {
        "icon": "🌐",
        "title": "Large & Underserved Market Opportunity", 
        "content": "The talent-related challenges Opereta solves are pervasive and enormously costly across all enterprise tiers. Consider the scale: U.S. businesses lose $450-$550 billion annually to employee disengagement, and enterprises can lose ~$59 million per year *each* due to digital skills gaps. Opereta taps into this vast market need for a comprehensive 'Ground Truth' solution."
    },
    {
        "icon": "⚖️",
        "title": "Scalable & Predictable Revenue Model",
        "content": "The ROI potential, and therefore Opereta's value, scales directly with customer size and complexity. This demonstrates a clear path to growing average contract value (ACV) as we engage larger clients and expand within existing ones. The problems only get bigger and more expensive for larger organizations."
    },
    {
        "icon": "🚀",
        "title": "Foundation for Sustainable Growth & Market Leadership",
        "content": "Strong, demonstrable customer ROI is the bedrock of a successful SaaS business. It drives faster sales cycles, higher customer retention and satisfaction, increased upsell/cross-sell opportunities, and powerful organic referrals. This positions Opereta for rapid growth and market leadership in the emerging Talent Intelligence Hub category."
    },
    {
        "icon": "🔑",
        "title": "Strategic Differentiator",
        "content": "Opereta isn't just another HR tool; it's a strategic platform providing 'Ground Truth' intelligence. In an era where talent is the key differentiator, enabling companies to hire better, align talent to value, develop employees effectively, and plan their workforce strategically offers a profound competitive advantage to our customers—and a unique investment opportunity."
    }
]

# Create a 2-column layout for the value props
col1, col2 = st.columns(2)
for i, prop in enumerate(investor_value_props):
    # Alternate between columns
    col = col1 if i % 2 == 0 else col2
    with col:
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; min-height: 220px;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="font-size: 24px; margin-right: 10px;">{prop["icon"]}</span>
                <h3 style="margin: 0; color: #0e5394; font-size: 18px;">{prop["title"]}</h3>
            </div>
            <p style="color: #333;">{prop["content"]}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer info banner
st.markdown("""
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px; margin-top: 30px; text-align: center; border: 1px solid #e0e0e0;">
    <p style="margin: 0;">This ROI demonstration is based on industry data and reasoned assumptions. Opereta offers customized value assessments for prospective clients and detailed discussions for investors. (Internal Model Version: Investor Pitch v1.0)</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# OPTIONAL: full math deep-dive markdown
# -------------------------------------------------------------------

with st.expander("📚 Full Value Generation Framework – formulas & assumptions"):
    try:
        with open("docs/value_generation_framework.md", "r") as md_file:
            st.markdown(md_file.read())
    except FileNotFoundError:
        st.warning("Detailed markdown file not found. Please ensure docs/value_generation_framework.md is present.")