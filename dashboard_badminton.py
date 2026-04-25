import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Badminton Analytics Dashboard",
    page_icon="🏸",
    layout="wide",
)

st.title("🏸 Badminton Player Analytics Dashboard")
st.markdown("---")

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("Badminton_Dataset_CLEANED.csv")
    df.columns = df.columns.str.strip()   # remove accidental leading spaces
    return df

df = load_data()

# ── Sidebar filters ───────────────────────────────────────────────────────────
st.sidebar.header("🔧 Filters")

categories = ["All"] + sorted(df["Category Full"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Category", categories)

handedness_opts = ["All"] + sorted(df["Handedness"].dropna().unique().tolist())
selected_hand = st.sidebar.selectbox("Handedness", handedness_opts)

style_opts = ["All"] + sorted(df["Playing style"].dropna().unique().tolist())
selected_style = st.sidebar.selectbox("Playing Style", style_opts)

# Apply filters
filtered = df.copy()
if selected_category != "All":
    filtered = filtered[filtered["Category Full"] == selected_category]
if selected_hand != "All":
    filtered = filtered[filtered["Handedness"] == selected_hand]
if selected_style != "All":
    filtered = filtered[filtered["Playing style"] == selected_style]

st.sidebar.markdown(f"**Players shown:** {len(filtered)}")

# ── Colour palette ────────────────────────────────────────────────────────────
PALETTE = px.colors.qualitative.Bold

# ═══════════════════════════════════════════════════════════════════════════════
# 1.  HISTOGRAM SECTION
# ═══════════════════════════════════════════════════════════════════════════════
st.header("📊 Histograms")

hist_cols = st.columns(3)

numeric_cols = [
    "Age", "Height(cm)", "Win Rate %", "Rally Win Rate %",
    "Smash Speed kmh", "Smash Success %", "Unforced error %",
    "Agility Score", "Stamina Index", "Net Play Score",
    "Career Titles", "Years Active",
]

# Histogram 1 – Age distribution
with hist_cols[0]:
    fig = px.histogram(
        filtered, x="Age", nbins=20,
        title="Age Distribution",
        color_discrete_sequence=[PALETTE[0]],
        template="plotly_white",
    )
    fig.update_layout(bargap=0.05)
    st.plotly_chart(fig, use_container_width=True)

# Histogram 2 – Win Rate %
with hist_cols[1]:
    fig = px.histogram(
        filtered, x="Win Rate %", nbins=20,
        title="Win Rate % Distribution",
        color_discrete_sequence=[PALETTE[1]],
        template="plotly_white",
    )
    fig.update_layout(bargap=0.05)
    st.plotly_chart(fig, use_container_width=True)

# Histogram 3 – Smash Speed
with hist_cols[2]:
    fig = px.histogram(
        filtered, x="Smash Speed kmh", nbins=20,
        title="Smash Speed (km/h) Distribution",
        color_discrete_sequence=[PALETTE[2]],
        template="plotly_white",
    )
    fig.update_layout(bargap=0.05)
    st.plotly_chart(fig, use_container_width=True)

# User-defined histogram
st.subheader("Custom Histogram")
hist_x = st.selectbox("Select numeric column for Histogram", numeric_cols, key="hist_custom")
fig_h = px.histogram(
    filtered, x=hist_x, nbins=25,
    color="Category Full",
    barmode="overlay",
    title=f"Distribution of {hist_x} by Category",
    template="plotly_white",
    color_discrete_sequence=PALETTE,
)
fig_h.update_layout(bargap=0.05)
st.plotly_chart(fig_h, use_container_width=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# 2.  BOX PLOT SECTION
# ═══════════════════════════════════════════════════════════════════════════════
st.header("📦 Box Plots")

box_cols = st.columns(2)

# Box 1 – Win Rate by Category
with box_cols[0]:
    fig = px.box(
        filtered, x="Category Full", y="Win Rate %",
        color="Category Full",
        title="Win Rate % by Category",
        template="plotly_white",
        color_discrete_sequence=PALETTE,
        points="all",
    )
    fig.update_layout(showlegend=False, xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)

# Box 2 – Smash Speed by Playing Style
with box_cols[1]:
    fig = px.box(
        filtered, x="Playing style", y="Smash Speed kmh",
        color="Playing style",
        title="Smash Speed (km/h) by Playing Style",
        template="plotly_white",
        color_discrete_sequence=PALETTE,
        points="outliers",
    )
    fig.update_layout(showlegend=False, xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)

# User-defined box plot
st.subheader("Custom Box Plot")
b1, b2 = st.columns(2)
box_y = b1.selectbox("Y-axis (numeric)", numeric_cols, key="box_y")
box_x = b2.selectbox(
    "X-axis (group by)",
    ["Category Full", "Playing style", "Handedness", "Nationality"],
    key="box_x",
)
fig_b = px.box(
    filtered, x=box_x, y=box_y,
    color=box_x,
    title=f"{box_y} grouped by {box_x}",
    template="plotly_white",
    color_discrete_sequence=PALETTE,
    points="outliers",
)
fig_b.update_layout(showlegend=False, xaxis_tickangle=-30)
st.plotly_chart(fig_b, use_container_width=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# 3.  SCATTER PLOT SECTION
# ═══════════════════════════════════════════════════════════════════════════════
st.header("🔵 Scatter Plots")

sc1, sc2 = st.columns(2)

# Scatter 1 – Age vs Win Rate
with sc1:
    fig = px.scatter(
        filtered, x="Age", y="Win Rate %",
        color="Category Full",
        size="Career Titles",
        hover_name="Player Name",
        title="Age vs Win Rate % (bubble = Career Titles)",
        template="plotly_white",
        color_discrete_sequence=PALETTE,
    )
    st.plotly_chart(fig, use_container_width=True)

# Scatter 2 – Smash Speed vs Smash Success
with sc2:
    fig = px.scatter(
        filtered, x="Smash Speed kmh", y="Smash Success %",
        color="Playing style",
        hover_name="Player Name",
        title="Smash Speed vs Smash Success %",
        template="plotly_white",
        color_discrete_sequence=PALETTE,
    )
    # Add a simple numpy trendline (no statsmodels needed)
    import numpy as np
    x_vals = filtered["Smash Speed kmh"].dropna()
    y_vals = filtered["Smash Success %"].dropna()
    common_idx = x_vals.index.intersection(y_vals.index)
    if len(common_idx) > 1:
        m, b = np.polyfit(x_vals[common_idx], y_vals[common_idx], 1)
        x_line = np.linspace(x_vals.min(), x_vals.max(), 100)
        fig.add_trace(go.Scatter(
            x=x_line, y=m * x_line + b,
            mode="lines", name="Trend",
            line=dict(color="black", dash="dash", width=1.5),
        ))
    st.plotly_chart(fig, use_container_width=True)

# User-defined scatter
st.subheader("Custom Scatter Plot")
sc_a, sc_b, sc_c = st.columns(3)
sc_x = sc_a.selectbox("X-axis", numeric_cols, index=0, key="sc_x")
sc_y = sc_b.selectbox("Y-axis", numeric_cols, index=2, key="sc_y")
sc_col = sc_c.selectbox(
    "Color by",
    ["Category Full", "Playing style", "Handedness", "Nationality"],
    key="sc_col",
)
fig_s = px.scatter(
    filtered, x=sc_x, y=sc_y,
    color=sc_col,
    hover_name="Player Name",
    title=f"{sc_x} vs {sc_y}",
    template="plotly_white",
    color_discrete_sequence=PALETTE,
)
import numpy as np
x_vals = filtered[sc_x].dropna()
y_vals = filtered[sc_y].dropna()
common_idx = x_vals.index.intersection(y_vals.index)
if len(common_idx) > 1:
    m, b = np.polyfit(x_vals[common_idx], y_vals[common_idx], 1)
    x_line = np.linspace(x_vals.min(), x_vals.max(), 100)
    fig_s.add_trace(go.Scatter(
        x=x_line, y=m * x_line + b,
        mode="lines", name="Trend",
        line=dict(color="black", dash="dash", width=1.5),
    ))
st.plotly_chart(fig_s, use_container_width=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# 4.  BAR CHART SECTION
# ═══════════════════════════════════════════════════════════════════════════════
st.header("📈 Bar Charts")

bar1, bar2 = st.columns(2)

# Bar 1 – Top 15 players by Ranking Points
with bar1:
    top15 = filtered.nlargest(15, "Ranking points")
    fig = px.bar(
        top15, x="Ranking points", y="Player Name",
        orientation="h",
        color="Category Full",
        title="Top 15 Players by Ranking Points",
        template="plotly_white",
        color_discrete_sequence=PALETTE,
    )
    fig.update_layout(yaxis=dict(autorange="reversed"), showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

# Bar 2 – Avg Win Rate by Nationality (top 10)
with bar2:
    nat_avg = (
        filtered.groupby("Nationality")["Win Rate %"]
        .mean()
        .reset_index()
        .nlargest(10, "Win Rate %")
    )
    fig = px.bar(
        nat_avg, x="Nationality", y="Win Rate %",
        color="Nationality",
        title="Top 10 Nationalities by Avg Win Rate %",
        template="plotly_white",
        color_discrete_sequence=PALETTE,
    )
    fig.update_layout(showlegend=False, xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)

# User-defined bar chart
st.subheader("Custom Bar Chart")
bc1, bc2, bc3 = st.columns(3)
bar_grp = bc1.selectbox(
    "Group by",
    ["Nationality", "Category Full", "Playing style", "Handedness"],
    key="bar_grp",
)
bar_metric = bc2.selectbox("Metric (avg)", numeric_cols, index=2, key="bar_metric")
bar_top_n = bc3.slider("Top N groups", 5, 30, 10, key="bar_n")

agg = (
    filtered.groupby(bar_grp)[bar_metric]
    .mean()
    .reset_index()
    .nlargest(bar_top_n, bar_metric)
)
fig_bar = px.bar(
    agg, x=bar_grp, y=bar_metric,
    color=bar_grp,
    title=f"Avg {bar_metric} by {bar_grp} (Top {bar_top_n})",
    template="plotly_white",
    color_discrete_sequence=PALETTE,
)
fig_bar.update_layout(showlegend=False, xaxis_tickangle=-30)
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# 5.  PIE CHART SECTION
# ═══════════════════════════════════════════════════════════════════════════════
st.header("🥧 Pie Charts")

pie1, pie2, pie3 = st.columns(3)

# Pie 1 – Player distribution by Category
with pie1:
    cat_counts = filtered["Category Full"].value_counts().reset_index()
    cat_counts.columns = ["Category Full", "Count"]
    fig = px.pie(
        cat_counts, names="Category Full", values="Count",
        title="Players by Category",
        color_discrete_sequence=PALETTE,
        hole=0.35,
    )
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)

# Pie 2 – Handedness split
with pie2:
    hand_counts = filtered["Handedness"].value_counts().reset_index()
    hand_counts.columns = ["Handedness", "Count"]
    fig = px.pie(
        hand_counts, names="Handedness", values="Count",
        title="Right-handed vs Left-handed",
        color_discrete_sequence=PALETTE,
        hole=0.35,
    )
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)

# Pie 3 – Playing style split
with pie3:
    style_counts = filtered["Playing style"].value_counts().reset_index()
    style_counts.columns = ["Playing style", "Count"]
    fig = px.pie(
        style_counts, names="Playing style", values="Count",
        title="Playing Style Distribution",
        color_discrete_sequence=PALETTE,
        hole=0.35,
    )
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)

# User-defined pie
st.subheader("Custom Pie Chart")
pie_col = st.selectbox(
    "Slice by",
    ["Nationality", "Category Full", "Playing style", "Handedness"],
    key="pie_col",
)
pie_top = st.slider("Collapse into top N slices (rest = Other)", 5, 20, 10, key="pie_n")

pie_data = filtered[pie_col].value_counts().reset_index()
pie_data.columns = [pie_col, "Count"]
top_slices = pie_data.head(pie_top)
other_count = pie_data["Count"].iloc[pie_top:].sum()
if other_count > 0:
    top_slices = pd.concat(
        [top_slices, pd.DataFrame({pie_col: ["Other"], "Count": [other_count]})],
        ignore_index=True,
    )
fig_pie = px.pie(
    top_slices, names=pie_col, values="Count",
    title=f"Distribution by {pie_col}",
    color_discrete_sequence=PALETTE,
    hole=0.35,
)
fig_pie.update_traces(textinfo="percent+label")
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
st.caption("Badminton Analytics Dashboard · Built with Streamlit & Plotly")