import streamlit as st
import random

# --- PAGE LAYOUT & CONFIGURATION ---
st.set_page_config(page_title="TechNova Executive Sim", page_icon="🏢", layout="centered")

# --- SIMULATION CONFIGURATION & DATA ---
NEWS_EVENTS = {
    "talent_crunch": {
        "headline": "🔴 NEWS FLASH: Global Tech Talent Crunch Hits Record Peak",
        "desc": "An acute shortage of specialized systems engineers means skilled labor is highly scarce and non-substitutable.",
        "effect_desc": "Expert Power yields 50% higher returns this turn; Coercive Power is twice as damaging."
    },
    "regulatory_shift": {
        "headline": "⚖️ NEWS FLASH: Major AI Compliance Accord Finalized",
        "desc": "New international frameworks mandate strict architectural documentation and compliance tracking.",
        "effect_desc": "Legitimacy and Rational Persuasion tactics receive a significant performance boost."
    },
    "competitor_drop": {
        "headline": "⚡ NEWS FLASH: Rival Tech Giant Suffers Massive Cloud Outage",
        "desc": "A competitor's infrastructure failure drives wave of panicking clients toward TechNova's platform.",
        "effect_desc": "Market pressure spikes. Reward and Exchange tactics become highly effective to rush delivery."
    },
    "supply_chain": {
        "headline": "🚢 NEWS FLASH: Silicon Chip Shipments Delayed due to Global Port Bottlenecks",
        "desc": "Physical hardware has become extremely scarce, drastically increasing resource dependence.",
        "effect_desc": "Coalition and Exchange tactics are required to secure internal resources."
    }
}

# --- INITIALIZE SESSION STATE ---
if 'stage' not in st.session_state:
    st.session_state.stage = 1
if 'profit' not in st.session_state:
    st.session_state.profit = 2000000.0  # Starting profit $2 Million
if 'log' not in st.session_state:
    st.session_state.log = []
if 'current_event' not in st.session_state:
    st.session_state.current_event = random.choice(list(NEWS_EVENTS.keys()))

def reset_sim():
    st.session_state.stage = 1
    st.session_state.profit = 2000000.0
    st.session_state.log = []
    st.session_state.current_event = random.choice(list(NEWS_EVENTS.keys()))

# --- SIMULATION HEADER ---
st.title("🏢 TechNova Executive: Power & Politics Simulation")
st.markdown("Navigate macro shocks, manage critical dependencies, and maximize fiscal year profits through tactical alignment.")
st.metric("TechNova Project Net Profit", f"${st.session_state.profit:,.2f}")
st.progress(min((st.session_state.stage - 1) * 20, 100), text=f"Stage {st.session_state.stage} of 5")
st.divider()

# Fetch active news flash data
current_ev_data = NEWS_EVENTS[st.session_state.current_event]

# --- GAME STAGES ---

# STAGE 1: DOWNWARD INFLUENCE
if st.session_state.stage == 1:
    st.subheader("Stage 1: Deploying the AI Dev Team")
    st.warning(f"**{current_ev_data['headline']}**\n\n{current_ev_data['desc']}\n\n*Impact:* {current_ev_data['effect_desc']}")
    
    st.write("Your engineering team is anxious about tight deadlines. Allocate 100% of your management style across the three bases of Formal and Personal Power:")
    
    expert = st.slider("Expert Power % (Hands-on mentoring, architectural guidance)", 0, 100, 40)
    reward = st.slider("Reward Power % (Structuring performance bonuses & recognition)", 0, 100 - expert, 30)
    coercive = 100 - expert - reward
    st.info(f"Remaining allocation for **Coercive Power** (Threats of reassignment): {coercive}%")
    
    if st.button("Commit Quarterly Strategy", type="primary"):
        # Base weights modified by external event
        w_exp = 0.004 * (1.5 if st.session_state.current_event == "talent_crunch" else 1.0)
        w_rwd = 0.002 * (1.4 if st.session_state.current_event == "competitor_drop" else 1.0)
        w_coe = -0.003 * (2.0 if st.session_state.current_event == "talent_crunch" else 1.0)
        
        mult = 1.0 + (expert * w_exp) + (reward * w_rwd) + (coercive * w_coe)
        st.session_state.profit *= mult
        st.session_state.log.append(f"Stage 1 Dev Allocation: Expert={expert}%, Reward={reward}%, Coercive={coercive}%. Multiplier: {mult:.3f}")
        
        st.session_state.current_event = random.choice(list(NEWS_EVENTS.keys()))
        st.session_state.stage += 1
        st.rerun()

# STAGE 2: LATERAL INFLUENCE & RESOURCE DEPENDENCE
elif st.session_state.stage == 2:
    st.subheader("Stage 2: Overcoming the IT Core Infrastructure Bottleneck")
    st.warning(f"**{current_ev_data['headline']}**\n\n{current_ev_data['desc']}\n\n*Impact:* {current_ev_data['effect_desc']}")
    
    st.write("You are completely dependent on the IT cluster engineers. Their server access is non-substitutable[cite: 1]. Balance your 100% influence budget to win their priority:")
    
    exchange = st.slider("Exchange Tactics % (Trading dev support to clear their backlog)", 0, 100, 40)
    coalition = st.slider("Coalition Tactics % (Banding together with other affected VPs)", 0, 100 - exchange, 30)
    legitimacy = 100 - exchange - coalition
    st.info(f"Remaining allocation for **Legitimacy Tactics** (Demanding compliance via SLA policy): {legitimacy}%")
    
    if st.button("Commit Quarterly Strategy", type="primary"):
        w_exc = 0.003 * (1.5 if st.session_state.current_event == "competitor_drop" else 1.0)
        w_coa = 0.002 * (1.6 if st.session_state.current_event == "supply_chain" else 1.0)
        w_leg = 0.0005 * (2.0 if st.session_state.current_event == "regulatory_shift" else 1.0)
        
        mult = 1.0 + (exchange * w_exc) + (coalition * w_coa) + (legitimacy * w_leg)
        st.session_state.profit *= mult
        st.session_state.log.append(f"Stage 2 IT Allocation: Exchange={exchange}%, Coalition={coalition}%, Legitimacy={legitimacy}%. Multiplier: {mult:.3f}")
        
        st.session_state.current_event = random.choice(list(NEWS_EVENTS.keys()))
        st.session_state.stage += 1
        st.rerun()

# STAGE 3: UPWARD INFLUENCE
elif st.session_state.stage == 3:
    st.subheader("Stage 3: Securing Capital from the Executive Board")
    st.warning(f"**{current_ev_data['headline']}**\n\n{current_ev_data['desc']}\n\n*Impact:* {current_ev_data['effect_desc']}")
    
    st.write("You need a 20% budget expansion from the CEO and Board. Balance your 100% presentation focus:")
    
    rational = st.slider("Rational Persuasion % (Presenting strict financial data and ROI models)", 0, 100, 50)
    ingratiation = st.slider("Ingratiation % (Praising the CEO's recent strategic roadmap announcements)", 0, 100 - rational, 30)
    up_coalition = 100 - rational - ingratiation
    st.info(f"Remaining allocation for **Upward Coalitions** (Enlisting backing from external advisors): {up_coalition}%")
    
    if st.button("Commit Quarterly Strategy", type="primary"):
        w_rat = 0.005 * (1.5 if st.session_state.current_event == "regulatory_shift" else 1.0)
        w_ing = -0.001 * (0.5 if st.session_state.current_event == "talent_crunch" else 1.0)
        w_upt = 0.001
        
        mult = 1.0 + (rational * w_rat) + (ingratiation * w_ing) + (up_coalition * w_upt)
        st.session_state.profit *= mult
        st.session_state.log.append(f"Stage 3 Board Allocation: Rational={rational}%, Ingratiation={ingratiation}%, Upward Coalition={up_coalition}%. Multiplier: {mult:.3f}")
        
        st.session_state.current_event = random.choice(list(NEWS_EVENTS.keys()))
        st.session_state.stage += 1
        st.rerun()

# STAGE 4: MANAGING RESOURCE DEPENDENCE (SCARCITY)
elif st.session_state.stage == 4:
    st.subheader("Stage 4: Mitigating Single-Vendor Vulnerabilities")
    st.warning(f"**{current_ev_data['headline']}**\n\n{current_ev_data['desc']}\n\n*Impact:* {current_ev_data['effect_desc']}")
    
    st.write("Your primary cloud vendor has raised pricing, capitalizing on your dependence[cite: 1]. Balance your strategic response units:")
    
    substitute = st.slider("Substitute Creation % (Investing in building internal open-source fallbacks)", 0, 100, 40)
    contract_legit = st.slider("Contract Enforcement % (Using legal teams to freeze legacy pricing caps)", 0, 100 - substitute, 30)
    acquiescence = 100 - substitute - contract_legit
    st.info(f"Remaining allocation for **Accepting Terms** (Paying premiums to avoid operational disruption): {acquiescence}%")
    
    if st.button("Commit Quarterly Strategy", type="primary"):
        w_sub = 0.004 * (1.5 if st.session_state.current_event == "supply_chain" else 1.0)
        w_con = 0.0015 * (2.0 if st.session_state.current_event == "regulatory_shift" else 1.0)
        w_acq = -0.002
        
        mult = 1.0 + (substitute * w_sub) + (contract_legit * w_con) + (acquiescence * w_acq)
        st.session_state.profit *= mult
        st.session_state.log.append(f"Stage 4 Dependence Allocation: Substitutes={substitute}%, Contract Legitimacy={contract_legit}%, Acquiescence={acquiescence}%. Multiplier: {mult:.3f}")
        
        st.session_state.current_event = random.choice(list(NEWS_EVENTS.keys()))
        st.session_state.stage += 1
        st.rerun()

# STAGE 5: INTERNAL OFFICE POLITICS
elif st.session_state.stage == 5:
    st.subheader("Stage 5: Navigating a Zero-Sum Promotion Window")
    st.warning(f"**{current_ev_data['headline']}**\n\n{current_ev_data['desc']}\n\n*Impact:* {current_ev_data['effect_desc']}")
    
    st.write("TechNova introduces a highly competitive performance evaluation framework. High performance pressures often drive severe office politics[cite: 1]. Choose your stance:")
    
    perf_focus = st.slider("Core Performance Focus % (Ignoring distractions, focusing entirely on product shipping metrics)", 0, 100, 50)
    legit_pol = st.slider("Legitimate Political Behavior % (Bypassing chain of command to network with board members)", 0, 100 - perf_focus, 30)
    withholding = 100 - perf_focus - legit_pol
    st.info(f"Remaining allocation for **Defensive Information Siloing** (Withholding architecture patterns from rivals): {withholding}%")
    
    if st.button("Finalize Fiscal Year Strategy", type="primary"):
        w_prf = 0.003
        w_lpl = 0.001 * (1.5 if st.session_state.current_event == "talent_crunch" else 1.0)
        w_wth = -0.004 * (0.5 if st.session_state.current_event == "competitor_drop" else 1.0)
        
        mult = 1.0 + (perf_focus * w_prf) + (legit_pol * w_lpl) + (withholding * w_wth)
        st.session_state.profit *= mult
        st.session_state.log.append(f"Stage 5 Political Stance: Performance={perf_focus}%, Legitimate Politics={legit_pol}%, Siloing={withholding}%. Multiplier: {mult:.3f}")
        
        st.session_state.stage += 1
        st.rerun()

# --- SIMULATION COMPLETE / RESULTS ENGINE ---
elif st.session_state.stage == 6:
    st.balloons()
    st.header("🏁 Annual Financial Review")
    
    final_p = st.session_state.profit
    initial_p = 2000000.0
    growth = ((final_p - initial_p) / initial_p) * 100
    
    st.metric("TechNova Final Value", f"${final_p:,.2f}", f"{growth:+.2f}% YoY")
    
    if final_p > 2800000:
        st.success("🏆 **Executive Tier (Elite):** You flawlessly navigated resource dependencies and matched optimal directional tactics to real-time market anomalies[cite: 1].")
    elif final_p >= 2100000:
        st.warning("⚖️ **Managerial Tier (Moderate):** Your strategies kept TechNova stable, but excessive reliance on formal compliance or defensive tactics eroded potential optimization[cite: 1].")
    else:
        st.error("📉 **Sub-optimal Tier:** Destructive political behaviors or over-reliance on coercive frameworks triggered performance losses[cite: 1].")
        
    st.subheader("Simulated System Optimization Matrix")
    st.write("Your returns were calculated across state-dependent production matrices, where vector $W$ shifts according to resource scarcity and direction of influence:")
    
    st.latex(r"\Pi_{final} = \Pi_{initial} \times \prod_{t=1}^{5} \left(1.0 + \sum_{i=1}^{3} x_{i,t} \cdot w_{i,t}(\text{News}_t)\right)")
    
    with st.expander("Review Decision Audit Log"):
        for step in st.session_state.log:
            st.write(step)
            
    if st.button("Re-run Simulation Matrix", type="primary", use_container_width=True):
        reset_sim()
        st.rerun()
