import streamlit as st
import folium
from streamlit_folium import st_folium
from PIL import Image
import base64
from io import BytesIO
import os

# Page configuration
st.set_page_config(
    page_title="Our Burwood Adventure 💕",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for color customization
st.sidebar.title("🎨 Customize Colors")
st.sidebar.markdown("Personalize the app to your liking!")

primary_color = st.sidebar.color_picker("Primary Color (headings & markers)", "#2c5f4f")
primary_light = st.sidebar.color_picker("Primary Light (gradients)", "#4a9375")
accent_color = st.sidebar.color_picker("Accent Color (badges & highlights)", "#e8b86d")
bg_color = st.sidebar.color_picker("Background Color", "#faf9f6")
text_color = st.sidebar.color_picker("Text Color", "#1a1a1a")
card_bg = st.sidebar.color_picker("Card Background", "#ffffff")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Tips")
st.sidebar.markdown("- Click any color to change it")
st.sidebar.markdown("- Dark text works best with light backgrounds")
st.sidebar.markdown("- Try different accent colors for different moods!")

# Custom CSS with dynamic colors
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    .main {{
        background: linear-gradient(135deg, {bg_color} 0%, #f0ebe3 100%);
    }}
    
    h1 {{
        font-family: 'Playfair Display', serif;
        color: {primary_color};
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        animation: fadeIn 1s ease-out;
    }}
    
    .subtitle {{
        text-align: center;
        color: {primary_color};
        opacity: 0.9;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }}
    
    .intro-text {{
        text-align: center;
        font-size: 1.15rem;
        color: {text_color};
        margin: 2rem auto;
        max-width: 600px;
        line-height: 1.8;
        font-weight: 500;
    }}
    
    .stop-card {{
        background: {card_bg};
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        border-left: 5px solid {accent_color};
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }}
    
    .stop-card:hover {{
        transform: translateX(8px);
        border-left-color: {primary_color};
    }}
    
    .stop-number {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, {primary_color}, {primary_light});
        color: white;
        border-radius: 50%;
        font-weight: 600;
        margin-right: 1rem;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(44, 95, 79, 0.3);
    }}
    
    .stop-title {{
        font-family: 'Playfair Display', serif;
        color: {primary_color};
        font-size: 1.4rem;
        font-weight: 600;
        margin: 0;
    }}
    
    .stop-desc {{
        margin: 0.5rem 0;
        color: {text_color};
        opacity: 1;
        font-size: 1rem;
        font-weight: 400;
        line-height: 1.6;
    }}
    
    .time-badge {{
        display: inline-block;
        background: {accent_color};
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        color: {text_color};
        margin-top: 0.5rem;
    }}
    
    .footer-text {{
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: {primary_color};
        font-style: italic;
        margin-top: 3rem;
        padding: 2rem;
        border-top: 2px solid {accent_color};
        font-weight: 600;
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .stImage {{
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(44, 95, 79, 0.15);
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {card_bg} 0%, {bg_color} 100%);
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>Our Burwood Adventure 💕</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A Saturday morning walk together</p>", unsafe_allow_html=True)

# Intro
st.markdown("""
<div class='intro-text'>
    <p>I planned a special morning walk for us through Burwood ❤️</p>
    <p>Coffee, nature, exploring the shops together... just us.</p>
</div>
""", unsafe_allow_html=True)

# Load and display the photo
photo_paths = [
    'IMG_7850.JPG',
    './IMG_7850.JPG',
    '/mnt/user-data/uploads/IMG_7850.JPG',
    os.path.join(os.path.dirname(__file__), 'IMG_7850.JPG')
]

photo_loaded = False
for photo_path in photo_paths:
    try:
        if os.path.exists(photo_path):
            img = Image.open(photo_path)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(img, caption="Can't wait for more moments like this 💕", use_container_width=True)
            photo_loaded = True
            break
    except Exception as e:
        continue

if not photo_loaded:
    st.info("💡 Upload your photo as 'IMG_7850.JPG' in the same folder as this app!")

st.markdown("<br>", unsafe_allow_html=True)

def create_map():
    # Center on Burwood
    m = folium.Map(
        location=[-33.8765, 151.1045],
        zoom_start=15,
        tiles='OpenStreetMap'
    )
    
    # Route points
    route_points = [
        {
            "lat": -33.8745651,
            "lng": 151.1059151,
            "title": "1. Westfield Burwood",
            "desc": "Start here - grab coffee!",
            "time": "9:00 AM"
        },
        {
            "lat": -33.8730145,
            "lng": 151.10293819999998,
            "title": "2. Burwood Park",
            "desc": "Walk through the park together",
            "time": "9:20 AM - 10:05 AM"
        },
        {
            "lat": -33.877,
            "lng": 151.1045,
            "title": "3. Burwood Road Shops",
            "desc": "Browse and explore",
            "time": "10:10 AM - 10:40 AM"
        },
        {
            "lat": -33.8818428,
            "lng": 151.1045158,
            "title": "4. Church Street",
            "desc": "Turnaround point",
            "time": "10:45 AM"
        },
        {
            "lat": -33.877,
            "lng": 151.1055,
            "title": "5. Back Up Burwood Road",
            "desc": "Return journey",
            "time": "10:55 AM - 11:25 AM"
        },
        {
            "lat": -33.8745651,
            "lng": 151.1059151,
            "title": "6. Back to Westfield",
            "desc": "End of our adventure",
            "time": "11:30 AM"
        }
    ]
    
    # Add markers
    for i, point in enumerate(route_points, 1):
        folium.Marker(
            location=[point["lat"], point["lng"]],
            popup=folium.Popup(f"""
                <div style='font-family: Inter, sans-serif; min-width: 200px;'>
                    <h4 style='color: {primary_color}; margin-bottom: 0.5rem;'>{point['title']}</h4>
                    <p style='margin: 0.5rem 0; color: {text_color};'>{point['desc']}</p>
                    <p style='margin: 0; color: {accent_color}; font-weight: 600;'>⏰ {point['time']}</p>
                </div>
            """, max_width=300),
            tooltip=point["title"],
            icon=folium.DivIcon(html=f"""
                <div style='
                    background: linear-gradient(135deg, {primary_color}, {primary_light});
                    width: 36px;
                    height: 36px;
                    border-radius: 50%;
                    border: 3px solid white;
                    box-shadow: 0 4px 12px rgba(44,95,79,0.4);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-weight: bold;
                    font-size: 16px;
                    font-family: Inter, sans-serif;
                '>{i}</div>
            """)
        ).add_to(m)
    
    # Draw route line
    route_coords = [[p["lat"], p["lng"]] for p in route_points]
    folium.PolyLine(
        route_coords,
        color=primary_light,
        weight=4,
        opacity=0.7,
        dash_array='10, 10'
    ).add_to(m)
    
    # Add heart marker at Burwood Park
    folium.Marker(
        location=[-33.8730145, 151.10293819999998],
        popup=folium.Popup("<h4 style='color: #2c5f4f;'>Our favorite spot 💕</h4><p>Peaceful park walk together</p>", max_width=200),
        icon=folium.DivIcon(html="""
            <div style='font-size: 32px; animation: heartbeat 1.5s ease-in-out infinite;'>❤️</div>
            <style>
                @keyframes heartbeat {
                    0%, 100% { transform: scale(1); }
                    25% { transform: scale(1.1); }
                }
            </style>
        """)
    ).add_to(m)
    
    return m

# Display map
st.markdown("### 🗺️ Our Route")
map_obj = create_map()
st_folium(map_obj, width=None, height=500)

st.markdown("<br>", unsafe_allow_html=True)

# Stops details
st.markdown("### 📍 The Journey")

stops = [
    {
        "number": "1",
        "title": "Start at Westfield",
        "desc": "Park here (3 hours free!) and grab our coffees from one of the cafes inside",
        "time": "⏰ 9:00 AM"
    },
    {
        "number": "2",
        "title": "Burwood Park",
        "desc": "Cross Burwood Road to the park. Let's walk through together with our coffees - duck pond, gardens, and benches everywhere if we want to sit and chat",
        "time": "⏰ 9:20 AM - 10:05 AM"
    },
    {
        "number": "3",
        "title": "Walk Down Burwood Road",
        "desc": "Exit the park and browse the shops - Asian restaurants, bakeries, Korean BBQ, bubble tea, boutiques... Let's explore together",
        "time": "⏰ 10:10 AM - 10:40 AM"
    },
    {
        "number": "4",
        "title": "Church Street (Turnaround)",
        "desc": "We'll walk all the way to Church Street, then turn around and head back",
        "time": "⏰ 10:45 AM"
    },
    {
        "number": "5",
        "title": "Back Up Burwood Road",
        "desc": "Browse the other side of the street on our way back to Westfield",
        "time": "⏰ 10:55 AM - 11:25 AM"
    },
    {
        "number": "6",
        "title": "Return to Westfield",
        "desc": "Back where we started - about 2-2.5 hours of walking, talking, and exploring together",
        "time": "⏰ 11:30 AM"
    }
]

for stop in stops:
    st.markdown(f"""
    <div class='stop-card'>
        <div style='display: flex; align-items: center; margin-bottom: 0.75rem;'>
            <span class='stop-number'>{stop['number']}</span>
            <h3 class='stop-title'>{stop['title']}</h3>
        </div>
        <p class='stop-desc'>{stop['desc']}</p>
        <span class='time-badge'>{stop['time']}</span>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer-text'>
    <span style='font-size: 1.5rem; margin-right: 0.5rem;'>🚶‍♂️</span>
    Can't wait to spend this time with you
    <span style='font-size: 1.5rem; margin-left: 0.5rem;'>🚶‍♀️</span>
</div>
""", unsafe_allow_html=True)
