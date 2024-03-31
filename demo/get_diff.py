import git

# 現在のリポジトリのパスを指定
repo_path = './'

try:
    # リポジトリオブジェクトの初期化
    repo = git.Repo(repo_path)
    print(repo)

    # インデックス（ステージングエリア）にある変更を取得
    diff = repo.index.diff('HEAD')
    print(diff)
    # 差分を表示
    for diff_item in diff:
        print(f'差分があるファイル: {diff_item.a_path}')
        print(diff_item.diff.decode('utf-8'))
        
except Exception as e:
    print(f'エラーが発生しました: {e}')