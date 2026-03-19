import streamlit as st
import pandas as pd
import mysql.connector

# --- 1. THE UI SETUP (HCI: Clear Visibility of System Status) ---
st.title("🎬 SceneWeaver")
st.markdown("### The Director's Command Center")
st.divider()

# --- 2. THE WAITSTAFF (Connecting to MySQL) ---
# Replace 'YOUR_PASSWORD' with your actual MySQL password just for testing locally!
def init_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="sceneweaver_db"
    )

conn = init_connection()
cursor = conn.cursor(dictionary=True)

# --- 3. THE SMART DETECTIVE (Running our Queries) ---

# Query 1: The Total Count
cursor.execute("SELECT COUNT(shot_id) as count_shots FROM Shots;")
total_shots = cursor.fetchone()['count_shots']

# Query 2: The Breakdown
cursor.execute("SELECT shot_type, COUNT(shot_id) AS total_in_category FROM Shots GROUP BY shot_type;")
breakdown_data = cursor.fetchall()

# --- 4. THE SILVER PLATTER (Displaying to the Director) ---

# HCI Principle: Important numbers should be massive and instantly readable
st.metric(label="Total Shots Planned", value=total_shots)

st.write("### Shot Breakdown")
# We use Pandas to turn our raw SQL data into a beautiful table for Streamlit to graph
df = pd.DataFrame(breakdown_data)

if not df.empty:
    # We tell the graph to use the 'shot_type' (A-Roll, B-Roll) as the labels at the bottom
    st.bar_chart(df.set_index('shot_type'))
else:
    st.info("No shots in the database yet. Time to start planning!")

# --- 5. THE ORDER SLIP (Adding New Data) ---
st.divider()
st.write("### 🎬 Add a New Shot")

# We create a form so the app doesn't refresh every time we type a single letter
with st.form("new_shot_form"):
    # We need to know which scene this belongs to (The Hook!)
    # For now, let's hardcode Scene 1, but we will make this dynamic later.
    selected_scene = 1 
    
    # The Input Fields
    description_input = st.text_input("Shot Description (e.g., Close up of coffee pouring)")
    
    # HCI Error Prevention: A dropdown menu matching our exact SQL constraints
    type_input = st.selectbox("Shot Type", ['A-Roll', 'B-Roll', 'Screen Recording'])
    
    # A simple number selector for frame rate
    fps_input = st.number_input("Frame Rate (FPS)", min_value=24, max_value=120, value=24)
    
    # The Submit Button
    submitted = st.form_submit_button("Save Shot to Database")
    
    if submitted:
        # 1. Write the SQL query string using %s as placeholders for security
        sql_query = "INSERT INTO Shots (scene_id, description, shot_type, frame_rate) VALUES (%s, %s, %s, %s)"
        
        # 2. Group our input variables into a tuple
        values = (selected_scene, description_input, type_input, fps_input)
        
        # 3. Tell the cursor to execute the query safely
        cursor.execute(sql_query, values)
        
        # 4. Tell the connection to commit the changes to the database
        conn.commit()
        
        st.success("Shot added successfully! Refresh the page to see the updated chart.")