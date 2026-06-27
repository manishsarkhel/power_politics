import streamlit as st

# Set page configuration
st.set_page_config(page_title="The Influence Architect", page_icon="🏢", layout="centered")

# --- SCENARIOS & SCORING LOGIC ---
# Scores are based on OB principles: Rational persuasion & Personal Power are highly effective. Coercion is risky.
scenarios = [
    {
        "id": 1,
        "title": "Scenario 1: The Stalled Project (Downward Influence)",
        "context": "You are managing a team establishing a new logistics simulation lab. The team is missing critical deadlines for software integration.",
        "question": "How do you get the team back on track?",
        "options": [
            {"text": "Inform them that anyone missing the next deadline will be removed from this high-profile project and assigned to mundane maintenance tasks.", "tactic": "Coercive Power", "score": 2, "feedback": "Coercive power relies on fear. While it might force immediate compliance, it can be damaging to long-term satisfaction."},
            {"text": "Announce that the sub-team that finishes their module first will receive extra funding for their specific research interests.", "tactic": "Reward Power", "score": 6, "feedback": "Reward power works by producing positive benefits[cite: 42]. However, the expectation of reward becomes necessary to maintain this influence[cite: 58]."},
            {"text": "Sit down with them, roll up your sleeves, and use your technical background in system architecture to help them troubleshoot the bottleneck.", "tactic": "Expert Power", "score": 10, "feedback": "Excellent. Expert power relies on special skills or knowledge[cite: 61]. Personal sources of power are the most effective for generating commitment[cite: 54]."}
        ]
    },
    {
        "id": 2,
        "title": "Scenario 2: The Budget Request (Upward Influence)",
        "context": "You need an additional 15% budget approval from the Institute Director to procure advanced hardware for the lab.",
        "question": "How do you approach the Director?",
        "options": [
            {"text": "Present a detailed ROI analysis showing how the new hardware will increase research output and attract industry grants.", "tactic": "Rational Persuasion", "score": 10, "feedback": "Perfect. Rational persuasion (logical arguments and factual evidence) [cite: 76] is the most effective tactic for upward influence."},
            {"text": "Use friendly flattery, praising the Director's recent strategic initiatives before slipping in your budget request.", "tactic": "Ingratiation", "score": 4, "feedback": "Ingratiation involves using flattery before making a request[cite: 76]. It is generally less effective for upward influence compared to logical data."},
            {"text": "Politely remind the Director that the institutional policy guarantees a contingency fund for all 'Center of Excellence' projects.", "tactic": "Legitimacy", "score": 7, "feedback": "Legitimating tactics rely on organizational policies[cite: 76]. It works, but it doesn't build emotional or logical commitment."}
        ]
    },
    {
        "id": 3,
        "title": "Scenario 3: The Uncooperative Department (Lateral Influence)",
        "context": "You are heavily dependent on the IT department to configure the servers. However, they are prioritizing other tasks because they do not report to you.",
        "question": "How do you secure their cooperation?",
        "options": [
            {"text": "Remind them that you are a Senior Project Chairperson and demand they respect your formal authority.", "tactic": "Legitimate Power", "score": 3, "feedback": "Legitimate power relies on formal hierarchy[cite: 44]. This doesn't work well when there is no clear chain of command over the target[cite: 58]."},
            {"text": "Offer to share some of your lab's student assistants to help IT with their data-entry backlog if they configure your servers this week.", "tactic": "Exchange", "score": 8, "feedback": "Exchange rewards the target with benefits or favors[cite: 76]. This is a highly effective tactic for lateral (peer-to-peer) influence."},
            {"text": "Enlist the support of three other department heads who also need the servers, presenting a united front to the IT manager.", "tactic": "Coalitions", "score": 7, "feedback": "Enlisting the aid of others to persuade the target is a Coalition tactic[cite: 76]. It is effective for lateral influence."}
        ]
    },
    {
        "id": 4,
        "title": "Scenario 4: Navigating Office Politics",
        "context": "A new 'zero-sum' performance evaluation system has been introduced, increasing high performance pressures[cite: 84]. You notice peers withholding critical supply chain data to make themselves look better.",
        "question": "How do you respond to this political behavior?",
        "options": [
            {"text": "Complain directly to your supervisor about the lack of data sharing.", "tactic": "Legitimate Political Behavior", "score": 8, "feedback": "Complaining to a supervisor is an example of legitimate, everyday political behavior[cite: 80, 82]."},
            {"text": "Become anxious, reduce your own performance, and start looking for a new job.", "tactic": "Negative Response to Politics", "score": 0, "feedback": "Organizational politics often threaten employees, leading to increased stress, decreased satisfaction, and turnover."},
            {"text": "Quietly bypass the chain of command to secure the data directly from junior analysts in the other department.", "tactic": "Legitimate Political Behavior", "score": 6, "feedback": "Bypassing the chain of command is a standard political behavior[cite: 83]. It can get results but carries interpersonal risks."}
        ]
    }
]

# --- SESSION STATE INITIALIZATION ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'history' not in st.session_state:
    st.session_state.history = []

def next_step(selected_option):
    st.session_state.score += selected_option['score']
    st.session_state.history.append({
        "scenario": scenarios[st.session_state.step]['title'],
        "tactic": selected_option['tactic'],
        "feedback": selected_option['feedback'],
        "points": selected_option['score']
    })
    st.session_state.step += 1

def reset_app():
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.history = []

# --- UI RENDERING ---
st.title("🏛️ The Influence Architect")
st.markdown("Navigate the scenarios below. Your choices will determine your Power Profile.")
st.divider()

# Progress Bar
if st.session_state.step < len(scenarios):
    progress = int((st.session_state.step / len(scenarios)) * 100)
    st.progress(progress, text=f"Scenario {st.session_state.step + 1} of {len(scenarios)}")

    current_scenario = scenarios[st.session_state.step]
    
    st.subheader(current_scenario['title'])
    st.info(current_scenario['context'])
    st.write(f"**{current_scenario['question']}**")

    # Render Options as buttons
    for option in current_scenario['options']:
        if st.button(option['text'], use_container_width=True):
            next_step(option)
            st.rerun()

else:
    # --- RESULTS SCREEN ---
    st.balloons()
    st.header("📊 Final Power Profile")
    
    max_score = 38 # Total possible points
    percentage = (st.session_state.score / max_score) * 100

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Influence Score", f"{st.session_state.score} / {max_score}")
    with col2:
        st.metric("Effectiveness Rating", f"{percentage:.0f}%")

    if percentage >= 80:
        st.success("**Master Influencer:** You successfully rely on Personal Power and Rational Persuasion, which are the most effective bases of power[cite: 54, 77].")
    elif percentage >= 50:
        st.warning("**Transactional Manager:** You rely heavily on Formal Power (Reward/Legitimate)[cite: 38]. While effective in the short term, you need to build more Expert and Referent power.")
    else:
        st.error("**Coercive Operator:** You rely too much on fear and formal authority. This damages organizational commitment.")

    st.divider()
    st.subheader("Your Decision Debrief")
    
    for item in st.session_state.history:
        with st.expander(f"{item['scenario']} - You used: {item['tactic']}"):
            st.write(f"**Score Awarded:** {item['points']} points")
            st.write(f"**Analysis:** {item['feedback']}")

    st.divider()
    if st.button("Restart Simulation", type="primary"):
        reset_app()
        st.rerun()
