# まず本ファイルをsecret.pyに変更して中身を編集する。
# 次にターゲットにコピーして実行するとconfig.jsonが生成され、
# Wi-Fi接続とGitHubリポジトリへのアクセスに必要な情報を設定できます。
import ugit

ugit.create_config(
    ssid="YourWifiName",
    password="YourWifiPassword",
    user="your-github-username",
    repository="your-repo-name",  # 純粋なリポジトリ名（例: "my-repo"）
    branch="main",
    token="your-github-token",  # optional: GitHub personal access token for private repos
)
