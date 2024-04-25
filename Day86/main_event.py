import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text = tk.Text(self.root, height=10, width=50, wrap='word', font=("Arial", 16))
        # self.text.pack()
        self.text.grid(column=1, row=0, columnspan=2)

        self.input_label = tk.Label(self.root, text="Type here:")
        # self.input_label.pack()
        self.input_label.grid(column=1, row=1)

        self.input_entry = tk.Entry(self.root, width=40)
        # self.input_entry.pack()
        self.input_entry.grid(column=2, row=1)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        # self.start_button.pack()
        self.start_button.grid(column=1, row=2)

        self.restart_label = tk.Label(self.root, text="(Press F5 to restart)")
        # self.restart_label.pack()
        self.restart_label.grid(column=2, row=2)

        self.cost_time_label = tk.Label(self.root, text="")
        # self.cost_time_label.pack()
        self.cost_time_label.grid(column=1, row=3, columnspan=2)

        self.result_label = tk.Label(self.root, text="")
        # self.result_label.pack()
        self.result_label.grid(column=1, row=4, columnspan=2)

        self.words = [
            "apple", "banana", "orange", "grape", "pineapple", "kiwi",
            "lemon", "mango", "avocados", "strawberries", "watermelon", "papaya",
            "abcedfghijkl",
        ]
        self.word_to_type = None
        self.start_time = None

        # Event
        self.input_entry.bind('<KeyRelease>', self.on_key_release)
        # Press F5 to restart
        self.root.bind('<F5>', self.start_test)

    def on_key_release(self, event):
        # 獲取 Entry 中的內容
        typed_word = self.input_entry.get().strip()
        if typed_word == self.word_to_type:
            elapsed_time = time.time() - self.start_time
            wpm = len(typed_word) / (elapsed_time / 60)
            self.cost_time_label.config(text=f"Cost time: {elapsed_time:.5f}s")
            self.result_label.config(text=f"Word per minute: {wpm:.2f}")
            # self.start_time = time.time()
        else:
            # self.result_label.config(text="Incorrect word. Try again.")
            pass

    def start_test(self, event=None):
        self.word_to_type = random.choice(self.words)
        self.text.delete('1.0', tk.END) # "end"表示它将读取直到文本框的结尾的输入
        self.text.insert(tk.END, f"Type the word: \n{self.word_to_type}")

        self.start_time = time.time()

        self.input_entry.delete(0, tk.END) # clear the entry
        self.input_entry.focus() # put the cursor to the entry

        self.cost_time_label.config(text=f"") # clear the cost time label
        self.result_label.config(text=f"") # clear the wpm label

        # self.root.bind('<Return>', self.check_word) # 綁定了 <Return> 事件

    def check_word(self, event):
        # unused
        typed_word = self.input_entry.get().strip()
        if typed_word == self.word_to_type:
            elapsed_time = time.time() - self.start_time
            wpm = len(typed_word) / (elapsed_time / 60)
            self.result_label.config(text=f"Word per minute: {wpm:.2f}")
        else:
            self.result_label.config(text="Incorrect word. Try again.")

        self.root.unbind('<Return>')

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
