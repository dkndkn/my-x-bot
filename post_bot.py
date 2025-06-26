import tweepy
import os
from datetime import datetime
import pytz

# --- 投稿する内容をここで自由に設定 ---
def create_tweet_text():
    # 日本時間を取得
    jst = pytz.timezone('Asia/Tokyo')
    now = datetime.now(jst)
    time_str = now.strftime("%Y年%m月%d日 %H:%M")

    # ここに投稿したい文章を書きます
    # 例：毎日違う挨拶をする
    greetings = [
        "こんにちは！",
        "今日も一日、穏やかに過ごせますように。",
        "いかがお過ごしですか？",
        "ひと息ついて、リラックスする時間も大切に。",
        "体調に気をつけて、無理しないでくださいね。",
        "最近、何か楽しいことはありましたか？",
        "良い一日をお過ごしくださいね。",
        "今日の空はどんな色ですか？",
        "小さな幸せが見つかる一日になりますように。",
        "週末の予定はもう立てましたか？",
        "コーヒーでも飲みながら、少し休憩しませんか？",
        "何気ない日常に、素敵な発見がありますように。"
    ]
    # 日付を元に、日替わりで挨拶を選ぶ
    today_greeting = greetings[now.day % len(greetings)] 
    
    return f"{time_str}です。\n{today_greeting} #bot"
# ------------------------------------

def post_tweet():
    # ステップ2で設定したGitHub Secretsからキーを読み込む
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
