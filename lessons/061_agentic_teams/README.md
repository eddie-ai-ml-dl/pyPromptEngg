# Lab 061: The Agentic Marketing Agency (Capstone)

## 1. Objective
Welcome to the finale. In this lab, you move from managing a single agent to orchestrating a **Multi-Agent Workforce**. You will act as the **Agency Director**, overseeing a "Centaur" workflow where human strategic intent combined with specialized AI agents produces high-velocity, high-integrity marketing campaigns.

**The Course Thesis:** *Orchestration is the new Management.*

## 2. Directory Structure
This lab simulates a professional agency environment with specialized roles and automated observability.

```text
061_agentic_teams/
├── orchestrator.py        # The Agency Manager (The "Pipeline")
├── database.json          # The "Ground Truth" (Competitor & Product facts)
├── agency_policy.json     # The "Employee Manual" (Unique prompts for 3 agents)
├── logs/                  # Automated Audit Trails (Created on run)
└── README.md              # This file
```

## 3. The Agency Team
You are managing three specialized agents, each using a model optimized for their specific task:

1.  **The Researcher (GPT-4o-mini):** Optimized for fast, low-cost data extraction.
2.  **The Copywriter (GPT-4o):** Optimized for high-quality creative prose.
3.  **The Compliance Governor (GPT-4o):** Optimized for high-reasoning audit and "Trace Integrity."

## 4. Lab Instructions

### Task 1: The Autonomous Failure (15 min)
Run the agency without human intervention to see how "Raw AI" handles competitive pressure.
1.  Run the orchestrator: `python lessons/061_agentic_teams/orchestrator.py`
2.  When prompted for **Stage 2 (Human Steering)**, simply **press Enter** to skip.
3.  **Observe the Logs:** Watch the interaction between the Copywriter and the Compliance Governor.
4.  **The Result:** The agent will likely be **REJECTED**. The Copywriter will "over-promise" or "hallucinate" to win, and the Governor will catch it.

### Task 2: The Centaur Model (30 min)
Now, apply the **Centaur Model** (Human + AI) to steer the agency toward an "Approved" launch.
1.  Run `orchestrator.py` again.
2.  At **Stage 2**, provide a **Strategic Steering Prompt**. 
    *   *Example:* "Focus on our security certification as a strength, but be strictly factual about RivalSoft. Do not make claims that aren't in the research."
3.  **Observe the Difference:** Does your intervention result in an **APPROVED** status?

### Task 3: Observability & Audit (15 min)
1.  Open the `logs/` folder.
2.  Open the latest `.log` file.
3.  **The Reflection:** Notice how the log captures the entire "Reasoning Handoff." This is your **Legal Shield**. In the enterprise, this log proves that your marketing is grounded in data.

## 5. Final Reflection
You have moved from asking "What is an agent?" in Session 1 to "How do I govern an agentic workforce?" in Session 5. 

As you finish this lab, look at the **Compliance Governor's** logic. It is doing the work you did manually in Session 4. This is how AI scales: **By turning your governance insights into automated agentic guardrails.**

---

### 🏁 Final Course Deliverable
Ensure your terminal shows a **GREEN [APPROVED]** panel. Take a screenshot of your successful orchestration and the corresponding log file name. 
