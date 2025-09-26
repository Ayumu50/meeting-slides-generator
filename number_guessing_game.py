import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("数当てゲーム")
        self.window.geometry("400x300")
        self.window.configure(bg="#f0f0f0")
        
        # ゲームの状態
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        
        self.setup_ui()
        
    def setup_ui(self):
        # タイトル
        title_label = tk.Label(
            self.window, 
            text="数当てゲーム", 
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=20)
        
        # 説明
        instruction_label = tk.Label(
            self.window,
            text="1から100の間の数字を当ててください！",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666"
        )
        instruction_label.pack(pady=10)
        
        # 試行回数表示
        self.attempts_label = tk.Label(
            self.window,
            text=f"残り試行回数: {self.max_attempts - self.attempts}",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333"
        )
        self.attempts_label.pack(pady=5) 
       
        # 入力フィールド
        input_frame = tk.Frame(self.window, bg="#f0f0f0")
        input_frame.pack(pady=20)
        
        tk.Label(
            input_frame, 
            text="予想:", 
            font=("Arial", 12),
            bg="#f0f0f0"
        ).pack(side=tk.LEFT, padx=5)
        
        self.guess_entry = tk.Entry(
            input_frame, 
            font=("Arial", 12),
            width=10,
            justify="center"
        )
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.bind("<Return>", lambda event: self.make_guess())
        
        # 推測ボタン
        guess_button = tk.Button(
            input_frame,
            text="推測",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=self.make_guess,
            padx=20
        )
        guess_button.pack(side=tk.LEFT, padx=5)
        
        # 結果表示
        self.result_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        self.result_label.pack(pady=20)
        
        # 新しいゲームボタン
        new_game_button = tk.Button(
            self.window,
            text="新しいゲーム",
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            command=self.new_game,
            padx=20
        )
        new_game_button.pack(pady=10)
        
        # フォーカスを入力フィールドに設定
        self.guess_entry.focus()
    
    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
            
            if guess < 1 or guess > 100:
                messagebox.showerror("エラー", "1から100の間の数字を入力してください！")
                return
            
            self.attempts += 1
            
            if guess == self.target_number:
                self.result_label.config(
                    text=f"🎉 正解！ {self.attempts}回で当てました！",
                    fg="#4CAF50"
                )
                self.guess_entry.config(state="disabled")
                messagebox.showinfo("おめでとう！", f"正解です！\n答えは {self.target_number} でした。\n{self.attempts}回で当てました！")
                
            elif self.attempts >= self.max_attempts:
                self.result_label.config(
                    text=f"😞 ゲームオーバー！答えは {self.target_number} でした",
                    fg="#f44336"
                )
                self.guess_entry.config(state="disabled")
                messagebox.showinfo("ゲームオーバー", f"残念！答えは {self.target_number} でした。")
                
            elif guess < self.target_number:
                self.result_label.config(
                    text="📈 もっと大きい数字です！",
                    fg="#FF9800"
                )
                
            else:
                self.result_label.config(
                    text="📉 もっと小さい数字です！",
                    fg="#FF9800"
                )
            
            # 試行回数を更新
            self.attempts_label.config(text=f"残り試行回数: {self.max_attempts - self.attempts}")
            
            # 入力フィールドをクリア
            self.guess_entry.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("エラー", "有効な数字を入力してください！")
    
    def new_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text=f"残り試行回数: {self.max_attempts}")
        self.result_label.config(text="")
        self.guess_entry.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()