import tweepy
import os
import pytz
import random
import time
from datetime import datetime

# --- 時間帯別の挨拶リスト ---
morning_greetings = [
    "おはようございます！",
    "朝の空気が気持ちいいですね。",
    "新しい一日の始まりです。素敵な日になりますように！",
    "朝のコーヒーはもう飲みましたか？",
    "今日も一日、元気にいきましょう！"
]

evening_greetings = [
    "こんばんは。",
    "お仕事や学校、お疲れ様です！",
    "今日一日、どんな日でしたか？",
    "ゆっくり休んでくださいね。",
    "素敵な夜をお過ごしください。"
]
# -----------------------------

def create_tweet_text():
    # 日本時間を取得
    jst = pytz.timezone('Asia/Tokyo')
    now = datetime.now(jst)
    current_hour = now.hour
    time_str = now.strftime("%Y年%m月%d日 %H:%M")

    # 朝（7時～11時）か、それ以外（夕方）かで挨拶リストを切り替える
    if 7 <= current_hour < 12:
        greeting_list = morning_greetings
    else:
        greeting_list = evening_greetings

    # リストからランダムに挨拶を選ぶ
    greeting = random.choice(greeting_list)
    
    return f"【{time_str}】\n{greeting} #bot"

def post_tweet():
    # 0分～119分（約2時間）のランダムな待ち時間を設定
    delay_seconds = random.randint(0, 119) * 60
    print(f"Wait for {delay_seconds // 60} minutes before posting...")
    time.sleep(delay_seconds)
    print("Wait finished. Posting tweet now...")

    # GitHub Secretsからキーを読み込む
    consumer_key = os.environ.get('X_API_KEY')
    consumer_secret = os.environ.get('X_API_KEY_SECRET')
    access_token = os.environ.get('X_ACCESS_TOKEN')
    access_token_secret = os.environ.get('X_ACCESS_TOKEN_SECRET')

    # Xの認証
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # 投稿するテキストを生成
    tweet_text = create_tweet_text()

    # 投稿を実行
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Tweet posted successfully! ID: {response.data['id']}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    post_tweet()
