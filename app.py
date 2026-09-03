import streamlit as st

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="AI Multi-Agent Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Multi-Agent Assistant")
st.caption("Your Personal AI Consultant")

st.divider()


# ============================================================
# SESSION STATE
# ============================================================

if "started" not in st.session_state:
    st.session_state.started = False

if "step" not in st.session_state:
    st.session_state.step = 1


# ============================================================
# AGENT SELECTION
# ============================================================

agent = st.selectbox(
    "Choose an AI Agent",
    [
        "📚 Study Planner",
        "💰 Finance Agent",
        "🐐 Goat & Sheep Farming",
        "📄 Resume Analyzer",
        "💡 Business Idea Agent"
    ]
)


# ============================================================
# STARTING QUESTION
# ============================================================

question = st.text_area(
    "💬 Start your question",
    placeholder="Example: I have ₹2 lakh. Which goat farming business should I start?"
)


if st.button("🚀 Start Consultation", use_container_width=True):

    if not question.strip():
        st.warning("⚠️ Please enter your question.")

    else:
        st.session_state.started = True
        st.session_state.step = 1
        st.session_state.question = question

        st.session_state.breed = ""
        st.session_state.goal = ""
        st.session_state.duration = ""
        st.session_state.shed = ""
        st.session_state.budget = 0
        st.session_state.feed = ""

        st.session_state.subject = ""
        st.session_state.level = ""
        st.session_state.study_hours = ""
        st.session_state.exam_date = ""

        st.session_state.income = 0
        st.session_state.expenses = 0
        st.session_state.goal_finance = ""

        st.session_state.resume_level = ""
        st.session_state.resume_target = ""
        st.session_state.skills = ""
        st.session_state.experience = ""

        st.session_state.business_type = ""
        st.session_state.business_budget = 0
        st.session_state.location = ""
        st.session_state.business_goal = ""

        st.rerun()


# ============================================================
# CONSULTATION
# ============================================================

if st.session_state.started:

    st.divider()

    st.header("💬 Let's understand your goal")

    st.write(
        f"**Your question:** {st.session_state.question}"
    )


    # ========================================================
    # FARMING AGENT
    # ========================================================

    if agent == "🐐 Goat & Sheep Farming":

        st.header("🐐 Farming Consultation")

        if st.session_state.step == 1:

            st.subheader("1️⃣ Which breed are you interested in?")

            breed = st.radio(
                "Choose one:",
                [
                    "🐐 Tellicherry",
                    "🐐 Boer",
                    "🐐 Jamunapari",
                    "🐐 Kanni Adu",
                    "🐐 Sirohi",
                    "🤖 I don't know — Recommend one"
                ]
            )

            custom = st.text_input(
                "✍️ Or type your own answer:",
                placeholder="Example: Pure Tellicherry"
            )

            if st.button("Next ➡️", use_container_width=True):

                st.session_state.breed = custom if custom.strip() else breed
                st.session_state.step = 2
                st.rerun()


        elif st.session_state.step == 2:

            st.subheader("2️⃣ What is your main goal?")

            goal = st.radio(
                "Choose one:",
                [
                    "🥩 Meat production",
                    "🐐 Breeding",
                    "💰 Buy → Grow → Resell",
                    "🐐 Only male goats",
                    "🐐 Only female goats",
                    "🤖 I don't know — Recommend one"
                ]
            )

            custom = st.text_input(
                "✍️ Or type your own answer:",
                placeholder="Example: I want only male goats for resale"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.step = 1
                    st.rerun()

            with col2:
                if st.button("Next ➡️", use_container_width=True):
                    st.session_state.goal = custom if custom.strip() else goal
                    st.session_state.step = 3
                    st.rerun()


        elif st.session_state.step == 3:

            st.subheader("3️⃣ How long do you want to run the plan?")

            duration = st.radio(
                "Choose one:",
                [
                    "3 months",
                    "6 months",
                    "1 year",
                    "🤖 Recommend for me"
                ]
            )

            custom = st.text_input(
                "✍️ Or type your own answer:",
                placeholder="Example: 4 months"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.step = 2
                    st.rerun()

            with col2:
                if st.button("Next ➡️", use_container_width=True):
                    st.session_state.duration = custom if custom.strip() else duration
                    st.session_state.step = 4
                    st.rerun()


        elif st.session_state.step == 4:

            st.subheader("4️⃣ Do you already have a shed?")

            shed = st.radio(
                "Choose one:",
                [
                    "🏠 Yes, I already have a shed",
                    "❌ No, I need a shed",
                    "🔨 I will use a temporary shed"
                ]
            )

            custom = st.text_input(
                "✍️ Or type your own answer:",
                placeholder="Example: I have land but need to build a shed"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.step = 3
                    st.rerun()

            with col2:
                if st.button("Next ➡️", use_container_width=True):
                    st.session_state.shed = custom if custom.strip() else shed
                    st.session_state.step = 5
                    st.rerun()


        elif st.session_state.step == 5:

            st.subheader("5️⃣ How much money are you planning to invest?")

            budget = st.number_input(
                "Investment amount (₹)",
                min_value=0,
                step=10000,
                value=200000
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.step = 4
                    st.rerun()

            with col2:
                if st.button("Next ➡️", use_container_width=True):
                    st.session_state.budget = budget
                    st.session_state.step = 6
                    st.rerun()


        elif st.session_state.step == 6:

            st.subheader("6️⃣ Do you have your own green fodder?")

            feed = st.radio(
                "Choose one:",
                [
                    "🌿 Yes, I have green fodder",
                    "🌱 Partially available",
                    "🛒 No, I need to buy feed"
                ]
            )

            custom = st.text_input(
                "✍️ Or type your own answer:",
                placeholder="Example: I have Napier grass"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.step = 5
                    st.rerun()

            with col2:
                if st.button("✅ Finish Consultation", use_container_width=True):
                    st.session_state.feed = custom if custom.strip() else feed
                    st.session_state.step = 7
                    st.rerun()


        elif st.session_state.step == 7:

            st.success("✅ Consultation completed!")

            st.header("🐐 Your Personalized Goat Farming Plan")

            st.subheader("🎯 Your Requirements")

            st.write(
                f"**Original Question:** {st.session_state.question}"
            )
            st.write(
                f"**Breed:** {st.session_state.breed}"
            )
            st.write(
                f"**Goal:** {st.session_state.goal}"
            )
            st.write(
                f"**Duration:** {st.session_state.duration}"
            )
            st.write(
                f"**Shed:** {st.session_state.shed}"
            )
            st.write(
                f"**Investment:** ₹{st.session_state.budget:,.0f}"
            )
            st.write(
                f"**Feed:** {st.session_state.feed}"
            )

            st.divider()

            budget = st.session_state.budget

            animal_budget = budget * 0.65
            feed_budget = budget * 0.20
            health_budget = budget * 0.05
            emergency_budget = budget * 0.10

            st.subheader("🐐 Recommended Starting Plan")

            if "male" in st.session_state.goal.lower():
                animal_count = 10
                recommendation = (
                    "Start with around 10 healthy male goats and use a "
                    "Buy → Grow → Resell model."
                )
            elif "breeding" in st.session_state.goal.lower():
                animal_count = 10
                recommendation = (
                    "Start with a manageable breeding group and focus on "
                    "healthy breeding animals."
                )
            else:
                animal_count = 10
                recommendation = (
                    "Start with around 10 healthy goats and monitor the "
                    "first production cycle before expanding."
                )

            st.info(recommendation)

            st.subheader("💰 Budget Allocation")

            budget_table = {
                "Category": [
                    "🐐 Animal purchase",
                    "🌿 Feed",
                    "💊 Health & veterinary",
                    "🛡️ Emergency reserve"
                ],
                "Estimated Amount": [
                    f"₹{animal_budget:,.0f}",
                    f"₹{feed_budget:,.0f}",
                    f"₹{health_budget:,.0f}",
                    f"₹{emergency_budget:,.0f}"
                ]
            }

            st.table(budget_table)

            st.write(
                f"**Total planned investment: ₹{budget:,.0f}**"
            )

            st.divider()

            st.subheader("🌿 Feeding Plan")

            st.markdown("""
**Daily feeding should be adjusted according to body weight, age,
growth stage and health.**

### Green Fodder
- Napier grass
- Fodder maize
- Hedge lucerne
- Other suitable local green fodder

### Dry Fodder
- Good-quality dry grass
- Clean crop residues where suitable

### Concentrate
Use a balanced concentrate according to the animal's weight and production stage.

### Minerals
Provide suitable mineral supplementation and salt according to veterinary/feed guidance.

### Water
Provide clean drinking water regularly.

⚠️ Never suddenly increase concentrate feed.
""")

            st.subheader("📈 Growth Tracking")

            st.markdown("""
For every goat record:

**Purchase weight → Month 1 → Month 2 → Month 3 → Selling weight**

Also record:

- Feed cost
- Medicine cost
- Veterinary cost
- Weight gain
- Selling price
""")

            st.subheader("💰 Profit Calculation")

            st.markdown("""
**Revenue = Number of goats sold × Selling price per goat**

**Profit = Revenue − Total expenses**

Do not assume a guaranteed selling price or guaranteed profit.
Actual results depend on breed, health, feeding, management and market conditions.
""")

            st.subheader("🏠 Shed Plan")

            st.markdown("""
A suitable shed should have:

- Good ventilation
- Dry floor
- Protection from rain
- Shade from heat
- Easy cleaning
- Enough space
- Separate sick-animal area
""")

            st.subheader("💉 Health Plan")

            st.markdown("""
- Buy healthy animals.
- Observe animals every day.
- Follow a local veterinarian's vaccination schedule.
- Follow veterinary advice for deworming.
- Keep water and feeding areas clean.
- Separate sick animals.
- Maintain weight and health records.
""")

            st.subheader("📅 3-Month Example")

            st.markdown("""
### Month 1
- Purchase healthy goats.
- Record starting weight.
- Start feeding routine.
- Begin health records.

### Month 2
- Check body weight.
- Review feed expenses.
- Monitor health.
- Adjust feeding with veterinary/feed guidance.

### Month 3
- Record final weight.
- Check current local market price.
- Calculate actual cost per goat.
- Compare selling options.
- Decide whether to sell or continue growing.
""")

            st.warning(
                "⚠️ This is an estimated planning model, not a guaranteed profit forecast."
            )


    # ========================================================
    # FINANCE AGENT
    # ========================================================

    elif agent == "💰 Finance Agent":

        st.header("💰 Finance Consultation")

        if st.session_state.step == 1:

            st.subheader("1️⃣ What is your monthly income?")

            income = st.number_input(
                "Monthly income (₹)",
                min_value=0,
                step=1000,
                value=30000
            )

            if st.button("Next ➡️", use_container_width=True):
                st.session_state.income = income
                st.session_state.step = 2
                st.rerun()


        elif st.session_state.step == 2:

            st.subheader("2️⃣ What are your monthly expenses?")

            expenses = st.number_input(
                "Monthly expenses (₹)",
                min_value=0,
                step=1000,
                value=20000
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.step = 1
                    st.rerun()

            with col2:
                if st.button("Next ➡️", use_container_width=True):
                    st.session_state.expenses = expenses
                    st.session_state.step = 3
                    st.rerun()


        elif st.session_state.step == 3:

            st.subheader("3️⃣ What is your main financial goal?")

            goal = st.radio(
                "Choose one:",
                [
                    "💰 Build savings",
                    "🛡️ Build emergency fund",
                    "🎓 Education",
                    "🐄 Start a business",
                    "🏠 Buy something important",
                    "🤖 Recommend for me"
                ]
            )

            custom = st.text_input(
                "✍️ Or type your own goal:"
            )

            if st.button("Next ➡️", use_container_width=True):
                st.session_state.goal_finance = custom if custom.strip() else goal
                st.session_state.step = 4
                st.rerun()


        elif st.session_state.step == 4:

            st.subheader("4️⃣ How long is your savings plan?")

            duration = st.radio(
                "Choose one:",
                [
                    "3 months",
                    "6 months",
                    "1 year",
                    "2 years",
                    "🤖 Recommend for me"
                ]
            )

            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.step = 3
                st.rerun()

            if st.button("✅ Create Financial Plan", use_container_width=True):
                st.session_state.duration = duration
                st.session_state.step = 5
                st.rerun()


        elif st.session_state.step == 5:

            income = st.session_state.income
            expenses = st.session_state.expenses

            savings = income - expenses
            yearly = savings * 12

            st.success("✅ Consultation completed!")

            st.header("💰 Your Personalized Financial Plan")

            st.subheader("🎯 Your Requirements")

            st.write(f"**Income:** ₹{income:,.0f} / month")
            st.write(f"**Expenses:** ₹{expenses:,.0f} / month")
            st.write(f"**Goal:** {st.session_state.goal_finance}")
            st.write(f"**Duration:** {st.session_state.duration}")

            st.divider()

            st.subheader("💵 Savings Calculation")

            st.write(f"Monthly potential savings: **₹{savings:,.0f}**")
            st.write(f"Potential yearly savings: **₹{yearly:,.0f}**")

            if savings > 0:
                st.success(
                    f"You currently have approximately ₹{savings:,.0f} "
                    "available after your stated expenses."
                )
            else:
                st.warning(
                    "Your stated expenses are equal to or greater than your income."
                )

            st.subheader("📊 Suggested Budget Structure")

            st.markdown("""
- Essential expenses
- Regular savings
- Emergency fund
- Goal-based savings
- Personal spending

The exact split should be based on your real expenses and goals.
""")

            st.subheader("🛡️ Emergency Fund")

            st.markdown("""
Build an emergency reserve gradually based on your essential monthly expenses.

Keep emergency money accessible and avoid putting all emergency funds into risky investments.
""")

            st.subheader("📅 Action Plan")

            st.markdown("""
### Month 1
Track every expense.

### Month 2
Reduce unnecessary spending.

### Month 3
Increase automatic savings.

### Month 4 onward
Review income, expenses and savings every month.
""")

            st.warning(
                "⚠️ This is general financial planning information, not personalized investment advice."
            )


    # ========================================================
    # STUDY PLANNER
    # ========================================================

    elif agent == "📚 Study Planner":

        st.header("📚 Study Planner Consultation")

        if st.session_state.step == 1:

            st.subheader("1️⃣ What subject do you want to study?")

            subject = st.text_input(
                "Subject",
                placeholder="Example: Python"
            )

            if st.button("Next ➡️", use_container_width=True):

                if subject.strip():
                    st.session_state.subject = subject
                    st.session_state.step = 2
                    st.rerun()
                else:
                    st.warning("Please enter a subject.")


        elif st.session_state.step == 2:

            st.subheader("2️⃣ What is your current level?")

            level = st.radio(
                "Choose one:",
                [
                    "🌱 Beginner",
                    "📘 Intermediate",
                    "🚀 Advanced",
                    "🤖 I don't know"
                ]
            )

            if st.button("Next ➡️", use_container_width=True):
                st.session_state.level = level
                st.session_state.step = 3
                st.rerun()


        elif st.session_state.step == 3:

            st.subheader("3️⃣ How many hours can you study per day?")

            hours = st.radio(
                "Choose one:",
                [
                    "1 hour",
                    "2 hours",
                    "3 hours",
                    "4+ hours"
                ]
            )

            if st.button("Next ➡️", use_container_width=True):
                st.session_state.study_hours = hours
                st.session_state.step = 4
                st.rerun()


        elif st.session_state.step == 4:

            st.subheader("4️⃣ What is your target?")

            target = st.text_input(
                "Exam / skill / goal",
                placeholder="Example: Learn Python for AI"
            )

            if st.button("Next ➡️", use_container_width=True):

                st.session_state.exam_date = target
                st.session_state.step = 5
                st.rerun()


        elif st.session_state.step == 5:

            st.success("✅ Consultation completed!")

            st.header("📚 Your Personalized Study Plan")

            st.write(
                f"**Subject:** {st.session_state.subject}"
            )
            st.write(
                f"**Level:** {st.session_state.level}"
            )
            st.write(
                f"**Study time:** {st.session_state.study_hours}"
            )
            st.write(
                f"**Goal:** {st.session_state.exam_date}"
            )

            st.divider()

            st.subheader("📅 Daily Method")

            st.markdown("""
### 1. Learn
Understand one new concept.

### 2. Practice
Solve exercises related to that concept.

### 3. Revise
Review what you learned earlier.

### 4. Test
Try questions without looking at notes.

### 5. Correct
Write down your mistakes and learn from them.
""")

            st.subheader("📊 Weekly Plan")

            st.markdown("""
**Monday:** Learn new concepts  
**Tuesday:** Practice basics  
**Wednesday:** Intermediate practice  
**Thursday:** Revision  
**Friday:** Problem solving  
**Saturday:** Mock test  
**Sunday:** Review mistakes
""")

            st.subheader("🎯 Progress Tracking")

            st.markdown("""
Track:

- Topics completed
- Practice questions
- Test scores
- Mistakes
- Revision dates
""")

            st.success(
                "Consistency is more important than studying for extremely long hours."
            )


    # ========================================================
    # RESUME ANALYZER
    # ========================================================

    elif agent == "📄 Resume Analyzer":

        st.header("📄 Resume Consultation")

        if st.session_state.step == 1:

            st.subheader("1️⃣ What type of resume do you need?")

            level = st.radio(
                "Choose one:",
                [
                    "🎓 Fresher Resume",
                    "💼 Experienced Resume",
                    "🔄 Career Change Resume",
                    "🤖 Recommend for me"
                ]
            )

            if st.button("Next ➡️", use_container_width=True):
                st.session_state.resume_level = level
                st.session_state.step = 2
                st.rerun()


        elif st.session_state.step == 2:

            st.subheader("2️⃣ What job are you targeting?")

            target = st.text_input(
                "Target role",
                placeholder="Example: Python Developer"
            )

            if st.button("Next ➡️", use_container_width=True):

                st.session_state.resume_target = target
                st.session_state.step = 3
                st.rerun()


        elif st.session_state.step == 3:

            st.subheader("3️⃣ What technical skills do you have?")

            skills = st.text_area(
                "Your skills",
                placeholder="Example: Python, SQL, HTML, Git"
            )

            if st.button("Next ➡️", use_container_width=True):

                st.session_state.skills = skills
                st.session_state.step = 4
                st.rerun()


        elif st.session_state.step == 4:

            st.subheader("4️⃣ Do you have project or work experience?")

            experience = st.radio(
                "Choose one:",
                [
                    "🚀 Projects only",
                    "💼 Work experience",
                    "🎓 Internship",
                    "❌ No experience yet"
                ]
            )

            if st.button("✅ Analyze Resume", use_container_width=True):

                st.session_state.experience = experience
                st.session_state.step = 5
                st.rerun()


        elif st.session_state.step == 5:

            st.success("✅ Consultation completed!")

            st.header("📄 Your Personalized Resume Plan")

            st.write(
                f"**Resume type:** {st.session_state.resume_level}"
            )
            st.write(
                f"**Target role:** {st.session_state.resume_target}"
            )
            st.write(
                f"**Skills:** {st.session_state.skills}"
            )
            st.write(
                f"**Experience:** {st.session_state.experience}"
            )

            st.divider()

            st.subheader("📝 Recommended Resume Structure")

            st.markdown("""
1. Name and contact information
2. Career summary
3. Education
4. Technical skills
5. Projects
6. Internship / experience
7. Certifications
8. Achievements
""")

            st.subheader("🚀 Project Section")

            st.markdown("""
For every project explain:

- Project name
- Problem
- Technology used
- Features
- Your contribution
- Result
""")

            st.subheader("⚠️ Avoid")

            st.markdown("""
- Fake skills
- Spelling mistakes
- Very long paragraphs
- Unnecessary personal information
- Poor formatting
- Copying another person's resume
""")

            st.success(
                "Your resume should clearly show what you know, what you built and what role you are targeting."
            )


    # ========================================================
    # BUSINESS IDEA AGENT
    # ========================================================

    elif agent == "💡 Business Idea Agent":

        st.header("💡 Business Consultation")

        if st.session_state.step == 1:

            st.subheader("1️⃣ What type of business are you interested in?")

            business_type = st.radio(
                "Choose one:",
                [
                    "🐄 Agriculture / Farming",
                    "💻 Technology / IT",
                    "🛒 Trading",
                    "🍔 Food Business",
                    "🏪 Local Business",
                    "🤖 I don't know — Recommend one"
                ]
            )

            custom = st.text_input(
                "✍️ Or type your own idea:",
                placeholder="Example: Goat farming"
            )

            if st.button("Next ➡️", use_container_width=True):

                st.session_state.business_type = (
                    custom if custom.strip() else business_type
                )

                st.session_state.step = 2
                st.rerun()


        elif st.session_state.step == 2:

            st.subheader("2️⃣ How much can you invest?")

            budget = st.number_input(
                "Business investment (₹)",
                min_value=0,
                step=10000,
                value=100000
            )

            if st.button("Next ➡️", use_container_width=True):

                st.session_state.business_budget = budget
                st.session_state.step = 3
                st.rerun()


        elif st.session_state.step == 3:

            st.subheader("3️⃣ Where will you operate the business?")

            location = st.text_input(
                "Location",
                placeholder="Example: Kanchipuram"
            )

            if st.button("Next ➡️", use_container_width=True):

                st.session_state.location = location
                st.session_state.step = 4
                st.rerun()


        elif st.session_state.step == 4:

            st.subheader("4️⃣ What is your main goal?")

            goal = st.radio(
                "Choose one:",
                [
                    "💰 Monthly income",
                    "📈 Long-term growth",
                    "👨‍🌾 Full-time business",
                    "💼 Part-time business",
                    "🤖 Recommend for me"
                ]
            )

            if st.button("🚀 Create Business Plan", use_container_width=True):

                st.session_state.business_goal = goal
                st.session_state.step = 5
                st.rerun()


        elif st.session_state.step == 5:

            st.success("✅ Consultation completed!")

            st.header("💡 Your Personalized Business Plan")

            st.write(
                f"**Business interest:** {st.session_state.business_type}"
            )
            st.write(
                f"**Investment:** ₹{st.session_state.business_budget:,.0f}"
            )
            st.write(
                f"**Location:** {st.session_state.location}"
            )
            st.write(
                f"**Goal:** {st.session_state.business_goal}"
            )

            st.divider()

            budget = st.session_state.business_budget

            st.subheader("💰 Suggested Budget Structure")

            st.markdown(f"""
- Equipment / setup: **₹{budget * 0.35:,.0f}**
- Initial stock / materials: **₹{budget * 0.25:,.0f}**
- Marketing: **₹{budget * 0.10:,.0f}**
- Working capital: **₹{budget * 0.20:,.0f}**
- Emergency reserve: **₹{budget * 0.10:,.0f}**
""")

            st.subheader("🎯 Customer Research")

            st.markdown("""
Before investing fully, find out:

- Who will buy?
- How often will they buy?
- What price will they pay?
- Who are the competitors?
- Why will customers choose you?
""")

            st.subheader("📈 Revenue & Profit")

            st.markdown("""
**Revenue = Number of sales × Selling price**

**Profit = Revenue − Total expenses**

Revenue is not the same as profit.

Consider raw materials, rent, electricity, transport, labour,
marketing, maintenance and other applicable expenses.
""")

            st.subheader("📅 90-Day Plan")

            st.markdown("""
### Days 1–30
Research customers and competitors.

### Days 31–60
Start with a small test version.

### Days 61–90
Measure sales, expenses and customer feedback.

Then decide whether to expand.
""")

            st.warning(
                "⚠️ Business profit is not guaranteed. Test demand and calculate actual costs before investing heavily."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🤖 AI Multi-Agent Assistant • Interactive Consultant Prototype"
)