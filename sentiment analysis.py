import customtkinter as ctk
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download NLTK data
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to evaluate the sentiment
def evaluate_sentiment():
    feedback = text_area.get("1.0", "end").strip()  # Get the input text
    if not feedback:
        result_label.configure(text="Please enter some feedback.", text_color="red")
        return
    
    # Get the sentiment scores
    sentiment_scores = sia.polarity_scores(feedback)
    
    # Get the compound score
    compound_score = sentiment_scores['compound']
    
    # Color code the result based on sentiment
    if compound_score >= 0.05:
        result_text = f"Sentiment Score: {compound_score:.2f}\nOverall Sentiment: Positive"
        result_label.configure(text=result_text, text_color="green")
    elif compound_score <= -0.05:
        result_text = f"Sentiment Score: {compound_score:.2f}\nOverall Sentiment: Negative"
        result_label.configure(text=result_text, text_color="red")
    else:
        result_text = f"Sentiment Score: {compound_score:.2f}\nOverall Sentiment: Neutral"
        result_label.configure(text=result_text, text_color="gray")

# Create the modernized GUI
def create_gui():
    ctk.set_appearance_mode("light")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

    # Initialize window
    root = ctk.CTk()
    root.title("Modern Feedback Sentiment Analyzer")
    root.geometry("600x400")

    # Set the title label
    title_label = ctk.CTkLabel(root, text="Sentiment Analysis Tool", font=("Helvetica", 24))
    title_label.pack(pady=20)

    # Create a text area for input
    global text_area
    text_area = ctk.CTkTextbox(root, height=150, width=400)
    text_area.pack(pady=10)

    # Create a submit button
    submit_button = ctk.CTkButton(root, text="Submit Feedback", command=evaluate_sentiment, height=40, width=200)
    submit_button.pack(pady=10)

    # Create a label to display the sentiment score
    global result_label
    result_label = ctk.CTkLabel(root, text="", font=("Helvetica", 18))
    result_label.pack(pady=20)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
