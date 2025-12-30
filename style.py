mishtee_css = """
/* Import elegant serif and sans-serif fonts */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@300;400&display=swap');

/* Main Container: Off-White Background */
.gradio-container {
    background-color: #FAF9F6 !important;
    font-family: 'Inter', sans-serif;
    color: #333333;
}

/* Headings: Clean, Spaced-out Serif */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    letter-spacing: 0.05em;
    font-weight: 400;
    text-transform: uppercase;
    color: #333333;
    margin-bottom: 1.5rem !important;
}

/* Buttons: Sober Terracotta with Sharp Edges */
button.primary, .gr-button-lg, .gr-button {
    background: #C06C5C !important;
    color: #FAF9F6 !important;
    border: none !important;
    border-radius: 0px !important; /* Removes 'bubbly' shapes */
    padding: 12px 24px !important;
    font-weight: 400;
    letter-spacing: 0.1em;
    transition: opacity 0.3s ease;
    box-shadow: none !important; /* No shadows */
}

button.primary:hover {
    opacity: 0.9;
}

/* Inputs and Textboxes: Sharp Lines & Whitespace */
input, textarea, .gr-input {
    border: 1px solid #333333 !important;
    border-radius: 0px !important;
    background-color: transparent !important;
    padding: 12px !important;
}

/* Tables: Lightweight Sans-Serif */
table, .gr-samples-table {
    font-family: 'Inter', sans-serif !important;
    font-weight: 300;
    border-collapse: collapse !important;
    font-size: 0.9rem;
}

th, td {
    border-bottom: 1px solid #E0E0E0 !important;
    padding: 15px !important;
    text-align: left;
}

/* Layout Padding: Emphasizing Whitespace */
.gr-block, .gr-box {
    margin-bottom: 40px !important;
    border: 1px solid #E0E0E0 !important;
    border-radius: 0px !important;
    padding: 30px !important;
    box-shadow: none !important;
}

/* Remove decorative shadows globally */
* {
    box-shadow: none !important;
}
"""
