import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def update_count(event=None):
    text_length = len(input_text.get("1.0", tk.END).strip())
    count_label.config(text=f"{text_length} words")

def summarize():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text first.")
        return
    
    choice = summary_choice.get()
    
    if choice == "paragraph":
        summary = " ".join(text.split()[:50]) + "..."
    else:  # sentences
        sentences = text.split('. ')
        summary = '. '.join(sentences[:3]) + "..."
    
    summary_box.config(state=tk.NORMAL)
    summary_box.delete("1.0", tk.END)
    summary_box.insert(tk.END, summary)
    summary_box.config(state=tk.DISABLED)
    
    # Show thank you message
    thank_you_label.config(text="✅ Thank you! Hope it helped.", fg="purple", font=("Arial", 14, "bold"))

    # Show the next question
    more_frame.pack(pady=10)

def restart():
    input_text.delete("1.0", tk.END)
    summary_box.config(state=tk.NORMAL)
    summary_box.delete("1.0", tk.END)
    summary_box.config(state=tk.DISABLED)
    thank_you_label.config(text="")
    more_frame.pack_forget()
    summary_choice.set("paragraph")

root = tk.Tk()
root.title("Text Summarizer")
root.geometry("600x600")

# Input area
tk.Label(root, text="Enter your text:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
input_text = ScrolledText(root, wrap=tk.WORD, width=70, height=10)
input_text.pack(padx=10, pady=5)
input_text.bind("<KeyRelease>", update_count)

# Live word count
count_label = tk.Label(root, text="0 words", font=("Arial", 10))
count_label.pack(anchor="e", padx=10)

# Summary type selection
tk.Label(root, text="Choose summary format:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
summary_choice = tk.StringVar(value="paragraph")
tk.Radiobutton(root, text="Paragraph", variable=summary_choice, value="paragraph").pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Sentences", variable=summary_choice, value="sentences").pack(anchor="w", padx=20)

# Summarize button
tk.Button(root, text="Summarize", command=summarize, bg="lightblue", font=("Arial", 12)).pack(pady=10)

# Summary box
tk.Label(root, text="Summary:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
summary_box = ScrolledText(root, wrap=tk.WORD, width=70, height=6, state=tk.DISABLED)
summary_box.pack(padx=10, pady=5)

# Thank you message
thank_you_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
thank_you_label.pack(pady=10)

# More or Exit frame
more_frame = tk.Frame(root)
tk.Label(more_frame, text="Do you want to summarize more?", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Button(more_frame, text="Yes", command=restart, bg="lightgreen").pack(side=tk.LEFT, padx=5)
tk.Button(more_frame, text="No (Exit)", command=root.quit, bg="red", fg="white").pack(side=tk.LEFT, padx=5)

root.mainloop()



