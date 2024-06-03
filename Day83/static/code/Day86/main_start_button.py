import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text = tk.Text(self.root, height=10, width=50, wrap='word')
        self.text.pack()

        self.input_label = tk.Label(self.root, text="Type here:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        self.start_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.words = ["apple", "banana", "orange", "grape", "pineapple"]
        self.word_to_type = None
        self.start_time = None

    def start_test(self):
        self.word_to_type = random.choice(self.words)
        self.text.delete('1.0', tk.END) # "end"表示它将读取直到文本框的结尾的输入
        self.text.insert(tk.END, f"Type the word: {self.word_to_type}")

        self.start_time = time.time()

        self.input_entry.delete(0, tk.END) # clear the entry
        self.input_entry.focus() # put the cursor to the entry

        self.root.bind('<Return>', self.check_word) # 綁定了 <Return> 事件

    def check_word(self, event):
        typed_word = self.input_entry.get().strip()
        if typed_word == self.word_to_type:
            elapsed_time = time.time() - self.start_time
            wpm = len(typed_word) / (elapsed_time / 60)
            self.result_label.config(text=f"Word per minute: {wpm:.2f}")
        else:
            self.result_label.config(text="Incorrect word. Try again.")

        self.root.unbind('<Return>')

def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()


if __name__ == "__main__":
    main()