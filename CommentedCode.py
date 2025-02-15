# Import necessary libraries
import tkinter as ui  # For GUI creation
import time  # For getting current time/date

# ==================================================================#
# Window Configuration                                              #
# ==================================================================#
window = ui.Tk()
window.configure(bg="#000000")  # Set window background to black
window.geometry("500x200")  # Window size (width x height)

# ==================================================================#
# Widget Creation (Time and Date Labels)                            #
# ==================================================================#
# Time Label - Larger font for emphasis
timelabel = ui.Label(
    text="00:00:00",
    font=("Arial", 40),  # Customize: Change font (e.g., "Verdana") or size (40)
    bg="#000000",  # Background color (matches window)
    fg="#ffffff"  # Text color (white)
)
timelabel.pack(pady=20)  # Add vertical padding

# Date Label - Smaller font for secondary information
datelabel = ui.Label(
    text="DayName , MonthName day, Year",
    font=("Arial", 20),  # Customize: Adjust font size here
    bg="#000000",
    fg="#ffffff"
)
datelabel.pack(pady=20)

# ==================================================================#
# Function Definitions                                              #
# ==================================================================#
def updateTime():
    """Updates the time label every second."""
    # Get current time components
    hour = time.strftime("%I")  # 12-hour format (use "%H" for 24-hour)
    minute = time.strftime("%M")  # Minutes (00-59)
    second = time.strftime("%S")  # Seconds (00-59)
    AMorPM = time.strftime("%p")  # AM/PM

    # Format time string (e.g., "03:45:30 PM")
    timetext = f"{hour}:{minute}:{second} {AMorPM}"
    
    # Update the time label
    timelabel.config(text=timetext)
    
    # Schedule next update in 1000ms (1 second)
    timelabel.after(1000, updateTime)  # Creates a refresh loop

def updateDate():
    """Updates the date label (currently updates once - uncomment line 68 for auto-refresh)."""
    # Get date components
    dayName = time.strftime("%A")  # Full weekday name (e.g., "Monday")
    monthName = time.strftime("%B")  # Full month name (e.g., "January")
    day = time.strftime("%d")  # Day of month (01-31)
    year = time.strftime("%Y")  # 4-digit year (e.g., "2024")

    # Format date string (e.g., "Monday, July 15, 2024")
    datetext = f"{dayName}, {monthName} {day}, {year}"
    
    # Update the date label
    datelabel.config(text=datetext)
    
    # To auto-refresh date daily at midnight, uncomment:
    # datelabel.after(86400000, updateDate)  # 86400000ms = 24 hours
    
    # To refresh every second (optional):
    # datelabel.after(1000, updateDate)  # Currently commented out

# ==================================================================#
# Start Updates & Run App                                           #
# ==================================================================#
updateDate()  # Initial date update (runs once)
updateTime()  # Start the time update loop
window.mainloop()  # Keep the window open and responsive
