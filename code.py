import streamlit as st
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="TechNova Executive Sim", page_icon="🏢", layout="centered")

# --- SIMULATION DATA: 12 ROUNDS ---
# Weights reflect OB theory: Personal/Rational = high positive, Formal = moderate, Coercive/Negative Politics = negative/risky.
SCENARIOS = [
    {"round": 1, "type": "Downward", "title": "The Overdue Milestone", "desc": "The dev team is missing critical integration deadlines.", "labels": ["Expert Power (Mentoring/Pair-programming)", "Reward Power (Bonus for finishing)", "Coercive Power (Threaten termination)"], "weights": [0.04, 0.02, -0.03]},
    {"round": 2, "type": "Lateral", "title": "IT Server Access", "desc": "IT is prioritizing other departments over your server requests.", "labels": ["Exchange (Trade dev hours)", "Coalition (Unite with other VPs)", "Legitimate (Demand SLA compliance)"], "weights": [0.04, 0.03, 0.01]},
    {"round": 3, "type": "Upward", "title": "Board Budget Pitch", "desc": "You need a 15% budget expansion from the CEO.", "labels": ["Rational Persuasion (ROI data)", "Ingratiation (Flatter the CEO)", "Upward Coalition (Use external advisors)"], "weights": [0.05, 0.01, 0.02]},
    {"round": 4, "type": "Politics", "title": "Zero-Sum Reviews", "desc": "A new competitive evaluation system increases performance pressure.", "labels": ["Focus on Core Performance", "Legitimate Politics (Bypass chain of command)", "Withhold Data from Peers"], "weights": [0.03, 0.02, -0.04]},
    {"round": 5, "type": "Dependence", "title": "Vendor Price Hike", "desc": "Your sole cloud provider suddenly raises rates by 20%.", "labels": ["Build Internal Substitute", "Legal/Contract Enforcement", "Acquiesce and Pay"], "weights": [0.04, 0.02, -0.02]},
    {"round": 6, "type": "Downward", "title": "Quality Control Crisis", "desc": "A junior team shipped a major bug to production.", "labels": ["Expert (Lead the root-cause analysis)", "Legitimate (Enforce strict protocols)", "Coercive (Publicly reprimand)"], "weights": [0.04, 0.02, -0.05]},
    {"round": 7, "type": "Lateral", "title": "Marketing Misalignment", "desc": "Marketing is overpromising AI features to clients.", "labels": ["Consultation (Involve them in planning)", "Exchange (Offer early feature access)", "Pressure (Threaten to escalate)"], "weights": [0.04, 0.03, -0.03]},
    {"round": 8, "type": "Upward", "title": "Project Delay Disclosure", "desc": "You must inform the board that the launch is delayed by a month.", "labels": ["Rational Persuasion (Data-backed recovery plan)", "Personal Appeals (Rely on CEO loyalty)", "Legitimacy (Cite policy allowances)"], "weights": [0.05, 0.02, 0.01]},
    {"round": 9, "type": "Politics", "title": "Credit Stealing", "desc": "A peer VP is taking credit for your team's AI module.", "labels": ["Rational Persuasion (Show commit logs)", "Legitimate Politics (Complain to supervisor)", "Retaliate (Sabotage their project)"], "weights": [0.04, 0.02, -0.06]},
    {"round": 10, "type": "Lateral", "title": "Data Silos", "desc": "The analytics team won't share user data needed for your model.", "labels": ["Exchange (Trade access)", "Inspirational Appeals (Share vision)", "Legitimate (Cite company data rules)"], "weights": [0.04, 0.03, 0.01]},
    {"round": 11, "type": "Downward", "title": "Team Burnout", "desc": "Engineers are exhausted and turnover risk is high.", "labels": ["Referent Power (Empathy & role modeling)", "Reward Power (Give paid time off)", "Pressure (Demand resilience)"], "weights": [0.05, 0.03, -0.06]},
    {"round": 12, "type": "Upward", "title": "The Pivot Decision", "desc": "The market shifted. You must convince the board to pivot the entire product.", "labels": ["Rational Persuasion (Market data)", "Inspirational Appeals (New vision)", "Coalition (Employee petition)"], "weights": [0.05, 0.04, 0.02]}
]

NEWS_FLASHES = [
    "🔴 Global Tech Talent Crunch Hits Record Peak",
    "⚖️ Major AI Compliance Accord Finalized",
    "⚡ Rival Tech Giant Suffers Massive Cloud Outage",
    "🚢 Silicon Chip Shipments Delayed Globally",
    "📉 Economic Downturn Freezes Venture Capital",
    "🚀 Breakthrough in Quantum Computing Announced"
]

# --- INITIALIZE SESSION STATE ---
if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'profit' not in st.session_state:
    st.session_state.profit = 2000000.0
if 'news' not in st.session_state:
    st.session_state.news = random.choice(NEWS_FLASHES)
if 'market_risk' not in st.session_state:
    st.session_state.market_risk = random.choice(["Low", "Moderate", "High", "Critical"])

def next_round(mult):
    st.session_state.profit *= mult
    st.session_state.stage += 1
    st.session_state.news = random.choice(NEWS_FLASHES)
    st.session_state.market_risk = random.choice(["Low", "Moderate", "High", "Critical"])

def reset_sim():
    st.session_state.stage = 0
    st.session_state.profit = 2000000.0
    st.session_state.news = random.choice(NEWS_FLASHES)
    st.session_state.market_risk = random.choice(["Low", "Moderate", "High", "Critical"])

# --- UI HEADER ---
st.title("🏢 TechNova Executive: 12-Month Pivot")
st.metric("TechNova Project Net Profit", f"${st.session_state.profit:,.0f}")
st.progress(min(st.session_state.stage / 12, 1.0), text=f"Month {st.session_state.stage + 1} of 12")
st.divider()

# --- GAME ENGINE ---
if st.session_state.stage < 12:
    current = SCENARIOS[st.session_state.stage]
    
    # Header & Randomizers
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**News Flash:** {st.session_state.news}")
    with col2:
        risk_color = "🔴" if st.session_state.market_risk in ["High", "Critical"] else "🟢"
        st.warning(f"{risk_color} **Market Risk Level:** {st.session_state.market_risk}")

    st.subheader(f"Month {current['round']}: {current['title']} ({current['type']} Influence)")
    st.write(current['desc'])
    st.write("Allocate your 100% management bandwidth across these tactics:")

    # Sliders
    val1 = st.slider(current['labels'][0], 0, 100, 40)
    val2 = st.slider(current['labels'][1], 0, 100 - val1, 30)
    val3 = 100 - val1 - val2
    st.write(f"**{current['labels'][2]}:** {val3}%")

    if st.button("Commit Monthly Strategy", type="primary"):
        # Risk amplifies the volatility of the weights
        risk_modifier = {"Low": 0.8, "Moderate": 1.0, "High": 1.5, "Critical": 2.0}[st.session_state.market_risk]
        
        # Calculate multiplier (convert percentages to decimals)
        impact = ((val1/100) * current['weights'][0]) + ((val2/100) * current['weights'][1]) + ((val3/100) * current['weights'][2])
        mult = 1.0 + (impact * risk_modifier)
        
        next_round(mult)
        st.rerun()

# --- END SCREEN ---
else:
    st.balloons()
    st.header("🏁 Fiscal Year Complete")
    
    final_p = st.session_state.profit
    initial_p = 2000000.0
    growth = ((final_p - initial_p) / initial_p) * 100
    
    st.metric("TechNova Final Value", f"${final_p:,.0f}", f"{growth:+.2f}% YoY")
    
    st.divider()
    st.subheader("Faculty Debrief Question")
    st.info("**Question for the Class:** Throughout this simulation, relying on Personal Power (Expert/Referent) and Rational Persuasion consistently generated the highest returns. However, in the real world—especially during periods of 'Critical Market Risk'—many companies immediately revert to strict hierarchies, Legitimate Power, and even Coercive tactics. *Why do organizations default to less effective formal power structures during a crisis?*")
    
    if st.button("Restart Simulation", type="primary", use_container_width=True):
        reset_sim()
        st.rerun()
