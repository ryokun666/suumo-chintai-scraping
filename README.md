# Overview
このプログラムは、SUUMOの任意の賃貸情報を検索したURLから物件情報を自動的にスクレイピングし、その結果をGoogleスプレッドシートに書き込むためのものです。定期的にこのスクリプトを実行することで、物件の坪単価の変動や他の詳細情報をデータとして収集できます。

# Requirements
Python 3.x

BeautifulSoup

requests

numpy

gspread

oauth2client


# Setup
必要なライブラリをインストールします。

``` pip install beautifulsoup4 requests numpy gspread oauth2client ```

Google Developer ConsoleからService AccountのJSONキーをダウンロードし、プロジェクトのディレクトリに配置します。例では./googleSeacretKey.jsonとしていますので、適宜パスを変更してください。

Googleスプレッドシートを作成し、Service Accountのメールアドレスを共有設定に追加します。

スプレッドシートのキーをSPREADSHEET_KEYの部分に追加します。

# Usage
スクリプトを実行してスクレイピングを開始します。

``` python suumo_scraping.py ```

# Note
このスクリプトはあくまで参考として提供されています。実際に使用する際は、スクレイピング先のサイトの利用規約やロボット排除標準に従ってください。

上記のREADME.mdは基本的なガイドラインとして提供されていますので、プロジェクトの詳細やニーズに合わせて適宜カスタマイズしてください。





