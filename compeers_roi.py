import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Agency ROI Demonstration", layout="wide")

# Title
st.markdown("# Agency ROI Demonstration")

# --- ASSUMPTIONS & NOTES IN COLUMNS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Assumptions:")
    assumptions = [
        "1) 10 IDIs or focus groups",
        "2) 5 English and 5 non-English IDIs, 60 minutes IDIs/FGs",
        "3) 3 hours per transcript",
        "4) $250 per file for translation/transcription",
        "5) $125 per file for transcription",
        "6) Day count starts on a Monday"
    ]
    st.write("\n\n".join(assumptions))

with col2:
    st.subheader("Notes:")
    user_notes = st.text_area("", height=200, label_visibility="collapsed")

# Spacing
st.markdown("<br>", unsafe_allow_html=True)

# Editable Time Saved Table
st.markdown("## Time Saved")
columns = ["Task", "Hours Without Compeers", "Hours With Compeers"]
data = [
    ["Define objectives", 1, 0.5],
    ["Desk research", 4, 2],
    ["Discussion guide", 8, 1.5],
    ["Recruitment efforts", 40, 40],
    ["Recruitment", 40, 40],
    ["Interviews", 80, 80],
    ["Translation/transcription", 80, 2],
    ["Analysis", 20, 8],
    ["Reporting", 40, 16]
]

df_time_saved = pd.DataFrame(data, columns=columns)

# Allow user to edit all columns
df_time_saved = st.data_editor(
    df_time_saved,
    column_config={
        "Task": {"editable": False},
        "Hours Without Compeers": {"editable": True},
        "Hours With Compeers": {"editable": True}
    },
    use_container_width=True,
    key="time_saved_editor",
    hide_index=True
)

# Calculate and display total hours
total_hours_without = df_time_saved["Hours Without Compeers"].sum()
total_hours_with = df_time_saved["Hours With Compeers"].sum()

st.markdown(f"## Total Hours:\n"
            f"#### Without Compeers: **{total_hours_without:,.0f}**\n"
            f"#### With Compeers: **{total_hours_with:,.0f}**")

# Spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# Editable Cost Comparison Table
st.markdown("## Cost Comparison")
cost_columns = ["Cost Item", "Without Compeers", "With Compeers"]
cost_data = [
    ["Recruitment efforts", "Same", "Same"],
    ["Honoraria", "Same", "Same"],
    ["Interviewing platform cost", "Same", "Same"],
    ["Translation/transcription", 1250, 0],
    ["Transcription", 625, 0],
    ["Platform", 100, 2200]
]

df_cost = pd.DataFrame(cost_data, columns=cost_columns)

# Allow user to edit cost columns
df_cost = st.data_editor(
    df_cost,
    column_config={
        "Cost Item": {"editable": False},
        "Without Compeers": {"editable": True},
        "With Compeers": {"editable": True}
    },
    use_container_width=True,
    key="cost_editor",
    hide_index=True
)

# Calculate and display total cost
total_cost_without = pd.to_numeric(df_cost["Without Compeers"].iloc[3:], errors='coerce').sum()
total_cost_with = pd.to_numeric(df_cost["With Compeers"].iloc[3:], errors='coerce').sum()

st.markdown(f"## Total Cost:\n\n"
            f"#### Without Compeers: **${total_cost_without:,.0f}**\n\n"
            f"#### With Compeers: **${total_cost_with:,.0f}**\n")

# Styling the tables with alternating colors
st.markdown(
    """
    <style>
        table {
            font-size: 18px !important;
        }
        .stDataFrame tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .stDataFrame tr:nth-child(odd) {
            background-color: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)