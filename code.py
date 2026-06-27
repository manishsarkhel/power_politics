import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="TechNova's Pivot", page_icon="📈", layout="centered")

# --- INITIALIZE SESSION STATE ---
if 'stage' not in st.session_state:
    st.session_state.stage = 1
if 'profit' not in st.session_state:
    st.session_state.profit = 1000000  # Starting profit $1,000,000

def reset_game():
    st.session_state.stage = 1
    st.session_state.profit = 1000000

def next_stage(multiplier):
    st.session_state.profit = int(st.session_state.profit * multiplier)
    st.session_state.stage += 1

# --- GAME HEADER ---
st.title("📈 TechNova's Pivot: Influence & Profit")
st.markdown("You are the VP of Product at TechNova Solutions. The market has shifted, and you must rapidly integrate a new AI architecture. Your influence choices directly impact the company's bottom line.")
st.metric("Current Projected Profit", f"${st.session_state.profit:,.0f}")
st.divider()

# --- STAGE 1: DOWNWARD INFLUENCE ---
if st.session_state.stage == 1:
    st.header("Stage 1: The Resisting Engineering Team")
    st.write("Your engineering team is experiencing high performance pressures and anxiety over the new AI integration[cite: 1]. You have 100 hours this week to influence them to adopt the new coding standards.")
    
    st.markdown("### Choose your tactic allocation:")
    st.write("Allocate your time between leveraging your technical expertise or using threats of punishment for missing deadlines.")
    
    expert_alloc = st.slider("Hours spent on Expert Power (Mentoring, sharing knowledge)", 0, 100, 50)
    coercive_alloc = 100 - expert_alloc
    
    st.write(f"**Remaining hours assigned to Coercive Power (Monitoring and threatening termination):** {coercive_alloc}")
    
    if st.button("Execute Strategy", use_container_width=True):
        # Math logic: Expert power is positively related to performance, Coercive is damaging[cite: 1]
        multiplier = 1.0 + (expert_alloc * 0.003) - (coercive_alloc * 0.002)
        
        st.info(f"**Analysis:** Personal sources of power are most effective. Expert power is positively related to employees' performance, whereas coercive power can be damaging[cite: 1].")
        next_stage(multiplier)
        st.rerun()

# --- STAGE 2: LATERAL INFLUENCE ---
elif st.session_state.stage == 2:
    st.header("Stage 2: The Siloed IT Department")
    st.write("You are completely dependent on the IT department to configure the new AI cloud servers. Because their skills are non-substitutable, they hold significant power[cite: 1]. They are prioritizing other projects.")
    
    st.markdown("### Choose your tactic allocation:")
    st.write("Allocate your time between negotiating an exchange or demanding compliance based on company rules.")
    
    exchange_alloc = st.slider("Hours spent on Exchange (Offering your developers to help with their backlog)", 0, 100, 50)
    legitimacy_alloc = 100 - exchange_alloc
    
    st.write(f"**Remaining hours assigned to Legitimacy (Citing organizational policies to force compliance):** {legitimacy_alloc}")
    
    if st.button("Execute Strategy", use_container_width=True):
        # Math logic: Exchange is highly effective for lateral influence[cite: 1]. Legitimacy is less effective laterally.
        multiplier = 1.0 + (exchange_alloc * 0.004) + (legitimacy_alloc * 0.0005)
        
        st.info(f"**Analysis:** For lateral influence (peer-to-peer), Exchange (rewarding the target with benefits/favors) is a preferred tactic[cite: 1]. Legitimacy (relying on authority/rules) is less optimal laterally[cite: 1].")
        next_stage(multiplier)
        st.rerun()

# --- STAGE 3: UPWARD INFLUENCE ---
elif st.session_state.stage == 3:
    st.header("Stage 3: Pitching the CEO")
    st.write("To finalize the pivot, you need a massive budget reallocation. You must influence the CEO. Organizational factors like resource reallocation often trigger high political behavior[cite: 1].")
    
    st.markdown("### Choose your tactic allocation:")
    st.write("Allocate your effort between presenting hard data versus flattering the CEO.")
    
    rational_alloc = st.slider("Effort (%) spent on Rational Persuasion (ROI data and factual evidence)", 0, 100, 50)
    ingratiation_alloc = 100 - rational_alloc
    
    st.write(f"**Remaining effort (%) assigned to Ingratiation (Using flattery and praise before making the request):** {ingratiation_alloc}")
    
    if st.button("Execute Strategy", use_container_width=True):
        # Math logic: Rational Persuasion is the primary effective upward tactic[cite: 1].
        multiplier = 1.0 + (rational_alloc * 0.005) - (ingratiation_alloc * 0.002)
        
        st.info(f"**Analysis:** Rational persuasion (presenting logical arguments and factual evidence) is the most preferred tactic for upward influence[cite: 1].")
        next_stage(multiplier)
        st.rerun()

# --- FINAL RESULTS ---
elif st.session_state.stage == 4:
    st.balloons()
    st.header("🏁 Fiscal Year Complete")
    
    final_profit = st.session_state.profit
    st.metric("Final Company Profit", f"${final_profit:,.0f}")
    
    st.markdown("### The Science Behind the Score")
    st.write("Your profit updates were calculated using a continuous function representing organizational behavior principles. For example, in Stage 1, the profit multiplier was modeled as:")
    
    # Using LaTeX explicitly for the complex formula as requested
    st.latex(r"Profit_{new} = Profit_{old} \times \left( 1.0 + (\alpha \cdot Expert_{hours}) - (\beta \cdot Coercive_{hours}) \right)")
    
    st.markdown("""
    **Debrief Points:**
    * **Personal Power:** Relying on Expert power yields high positive multipliers because it is positively related to organizational commitment and performance[cite: 1].
    * **Coercive Power:** Relying on fear and threats yields negative multipliers because coercive power can be damaging and increases stress[cite: 1].
    * **Directional Tactics:** Rational Persuasion is mathematically weighted higher for Upward influence, while Exchange is heavily weighted for Lateral influence[cite: 1].
    """)
    
    st.divider()
    if st.button("Play Again", type="primary", use_container_width=True):
        reset_game()
        st.rerun()
