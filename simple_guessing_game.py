import random

def number_guessing_game():
    print("🎮 数当てゲームへようこそ！")
    print("=" * 40)
    print("1から100の間の数字を当ててください！")
    print("最大10回まで挑戦できます。")
    print("=" * 40)
    
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\n残り試行回数: {remaining}")
        
        try:
            guess = int(input("予想を入力してください (1-100): "))
            
            if guess < 1 or guess > 100:
                print("❌ 1から100の間の数字を入力してください！")
                continue
            
            attempts += 1
            
            if guess == target_number:
                print(f"\n🎉 正解！おめでとうございます！")
                print(f"答えは {target_number} でした。")
                print(f"{attempts}回で当てました！")
                break
            elif guess < target_number:
                print("📈 もっと大きい数字です！")
            else:
                print("📉 もっと小さい数字です！")
                
        except ValueError:
            print("❌ 有効な数字を入力してください！")
    
    else:
        print(f"\n😞 ゲームオーバー！")
        print(f"答えは {target_number} でした。")
    
    # 新しいゲームを開始するか確認
    while True:
        play_again = input("\nもう一度プレイしますか？ (y/n): ").lower()
        if play_again in ['y', 'yes', 'はい']:
            print("\n" + "=" * 40)
            number_guessing_game()
            break
        elif play_again in ['n', 'no', 'いいえ']:
            print("ゲームを終了します。ありがとうございました！")
            break
        else:
            print("yまたはnで答えてください。")

if __name__ == "__main__":
    number_guessing_game()