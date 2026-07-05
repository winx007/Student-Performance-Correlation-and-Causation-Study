import customtkinter as ctk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

# Set appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Performance Analysis Dashboard")
        self.geometry("900x650")
        
        # Grid layout (1x2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Load Data
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_data.csv')
        try:
            self.df = pd.read_csv(data_path)
        except Exception as e:
            print(f"Error loading data: {e}")
            self.df = pd.DataFrame({'GPA': [], 'StudyHours': [], 'SleepHours': [], 'Attendance': []})

        # --- Sidebar ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Data Science\nDashboard", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.var_label = ctk.CTkLabel(self.sidebar_frame, text="Select Variable (X-axis):")
        self.var_label.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")
        
        self.var_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["StudyHours", "SleepHours", "Attendance", "PastGrades"],
                                                command=self.change_plot)
        self.var_optionmenu.grid(row=2, column=0, padx=20, pady=(10, 20))

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))

        # --- Main Area ---
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self.main_frame, text="Correlation & Causation Analysis", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, pady=20)
        
        self.stats_label = ctk.CTkLabel(self.main_frame, text="Correlation: N/A", font=ctk.CTkFont(size=16))
        self.stats_label.grid(row=2, column=0, pady=10)

        # Plot Canvas
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        # Initialize Plot
        self.var_optionmenu.set("StudyHours")
        self.change_plot("StudyHours")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        # Re-draw plot to match theme if needed (simple implementation just redraws)
        self.change_plot(self.var_optionmenu.get())

    def change_plot(self, x_col):
        if self.df.empty:
            return

        y_col = 'GPA'
        
        self.ax.clear()
        
        # Style based on theme
        mode = ctk.get_appearance_mode()
        bg_color = "#2b2b2b" if mode == "Dark" else "#f0f0f0"
        text_color = "white" if mode == "Dark" else "black"
        scatter_color = "#1f538d" if mode == "Dark" else "#3a7ebf"

        self.fig.patch.set_facecolor(bg_color)
        self.ax.set_facecolor(bg_color)
        self.ax.tick_params(colors=text_color)
        for spine in self.ax.spines.values():
            spine.set_color(text_color)
            
        self.ax.scatter(self.df[x_col], self.df[y_col], alpha=0.6, color=scatter_color)
        self.ax.set_xlabel(x_col, color=text_color)
        self.ax.set_ylabel(y_col, color=text_color)
        self.ax.set_title(f"{x_col} vs {y_col}", color=text_color)
        
        # Calculate correlation
        corr = self.df[x_col].corr(self.df[y_col])
        self.stats_label.configure(text=f"Pearson Correlation (r): {corr:.3f}")
        
        # Draw trendline
        m, b = np.polyfit(self.df[x_col], self.df[y_col], 1)
        self.ax.plot(self.df[x_col], m * self.df[x_col] + b, color="red")

        self.fig.tight_layout()
        self.canvas.draw()

if __name__ == "__main__":
    app = App()
    app.mainloop()
