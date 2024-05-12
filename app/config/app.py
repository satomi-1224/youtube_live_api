from dotenv import load_dotenv
import os

load_dotenv()

# 環境変数を使用する
address=os.getenv('ADDRESS', '127.0.0.1')
port=os.getenv('PORT', '8000')