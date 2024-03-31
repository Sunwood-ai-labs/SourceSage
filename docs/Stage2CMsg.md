下記はissuesの情報です

```json

[
    {
        "number": 5,
        "title": "マークダウンにもかっこいいタイムラインの図が欲しい",
        "body": null
    },
    {
        "number": 4,
        "title": "Git関係のモジュールのリファクタリング。",
        "body": "重複しているモジュールがある気がするのでその修正！"
    },
    {
        "number": 2,
        "title": "ハイパーパラメータを環境変数(.env)から設定できるようにしたい",
        "body": null
    }
]

```

また、下記はgitはStageの情報です

issueを解決していればそれも含めてコミットメッセージを書いて

見やすくコミットメッセージにして

```

# Staged Files Diff

## docs/Stage2CMsg.md

### 追加された内容:

```markdown
下記はissuesの情報です

また、下記はgitはStageの情報です

issueを解決していればそれも含めてコミットメッセージを書いて

見やすくコミットメッセージにして
コミットメッセージは日本語にして

```

## docs/css/style.css

### 追加された内容:

```css
.cp_timeline04 {
    position: relative;
    margin: 3em auto;
    padding-bottom: 2em;
 }
 .cp_timeline04:before {
    position: absolute;
    top: 0px;
    left: 45px;
    width: 3px;
    height: 100%;
    content: '';
    background: #6588A6;
 }
 .cp_timeline04 .timeline_item {
    margin: 0px 0px 0px 80px;
 }
 .cp_timeline04 .timeline_item .time_date .time {
    font-family: serif;
    font-size: 6em;
    font-weight: bold;
    position: relative;
    margin: 0;
    letter-spacing: 3px;
    color: rgba(156,162,166,0.5);
 }
 .cp_timeline04 .timeline_item .time_date .time:before {
    position: absolute;
    top: 50%;
    left: -42px;
    width: 10px;
    height: 10px;
    content: '';
    -webkit-transform: rotate(45deg);
            transform: rotate(45deg);
    border: 3px solid #6588A6;
    background: #fff;
 }
 .cp_timeline04 .timeline_item .time_date .flag {
    font-size: 1.5em;
    font-weight: bold;
    margin: 0;
    margin-top: -60px;
    color: #6588A6;
 }
 .cp_timeline04 .timeline_item .desc {
    font-size: 1em;
    line-height: 20px;
    margin-top: 10px;
    padding-left: 20px;
    border-left: 5px solid #D0D7D9;
 }
 @media only screen and (max-width: 767px) {
    .cp_timeline04:before {
        left: 15px;
    }
    .cp_timeline04 .timeline_item .time_date .time:before {
        left: -32px;
    }
    .cp_timeline04 .timeline_item {
        margin: 0px 0px 0px 40px;
    }
    .cp_timeline04 .timeline_item .desc {
        padding-left: 0px;
        border-top: 1px solid #6588A6;
        border-left: none;
    }
 }
```

## docs/timeline_sample.md

### 追加された内容:

```markdown
<style>
.cp_timeline04 {
   position: relative;
   margin: 3em auto;
   padding-bottom: 2em;
}
.cp_timeline04:before {
   position: absolute;
   top: 0px;
   left: 45px;
   width: 3px;
   height: 100%;
   content: '';
   background: #6588A6;
}
.cp_timeline04 .timeline_item {
   margin: 0px 0px 0px 80px;
}
.cp_timeline04 .timeline_item .time_date .time {
   font-family: serif;
   font-size: 6em;
   font-weight: bold;
   position: relative;
   margin: 0;
   letter-spacing: 3px;
   color: rgba(156,162,166,0.5);
}
.cp_timeline04 .timeline_item .time_date .time:before {
   position: absolute;
   top: 50%;
   left: -42px;
   width: 10px;
   height: 10px;
   content: '';
   -webkit-transform: rotate(45deg);
           transform: rotate(45deg);
   border: 3px solid #6588A6;
   background: #fff;
}
.cp_timeline04 .timeline_item .time_date .flag {
   font-size: 1.5em;
   font-weight: bold;
   margin: 0;
   margin-top: -60px;
   color: #6588A6;
}
.cp_timeline04 .timeline_item .desc {
   font-size: 1em;
   line-height: 20px;
   margin-top: 10px;
   padding-left: 20px;
   border-left: 5px solid #D0D7D9;
}
@media only screen and (max-width: 767px) {
   .cp_timeline04:before {
   	left: 15px;
   }
   .cp_timeline04 .timeline_item .time_date .time:before {
   	left: -32px;
   }
   .cp_timeline04 .timeline_item {
   	margin: 0px 0px 0px 40px;
   }
   .cp_timeline04 .timeline_item .desc {
   	padding-left: 0px;
   	border-top: 1px solid #6588A6;
   	border-left: none;
   }
}
</style>

<div class="cp_timeline04">
 <div class="timeline_item">
   <div class="time_date">
     <p class="time">開発前</p>
     <p class="flag">課題の確認とAIによる自動修正</p>
   </div>
   <div class="desc">
     <p>
       - <code>get_issues.py</code>を使用してGitHubのオープンなissueを取得し、JSONファイルに保存する<br>
       - issueの内容と現在のソースコードの情報をClaude AIに入力し、自動でissueの修正を行う<br>
         - <code>SourceSage.py</code>を使用して現在のプロジェクトのソースコードとファイル構成を1つのマークダウンファイルに統合する<br>
         - <code>get_issues.py</code>で取得したissueデータと<code>SourceSage.py</code>で生成したマークダウンをClaude AIに入力する<br>
         - AIがissueの内容を理解し、現在のソースコードを分析して自動的にissueの修正を提案する<br>
         - 提案された修正内容を確認し、必要に応じて手動で調整を行う
     </p>
   </div>
 </div>

 <div class="timeline_item">
   <div class="time_date">
     <p class="time">開発中</p>
     <p class="flag">ステージされた変更の確認とコミットメッセージの自動生成</p>
   </div>
   <div class="desc">
     <p>
       - <code>StagedDiffGenerator</code>クラスを使用してステージされた差分を取得し、マークダウンファイルに出力する<br>
       - ステージされた変更とissueの情報をAIに入力し、適切なコミットメッセージを生成する<br>
         - <code>get_issues.py</code>で取得したissueデータと<code>StagedDiffGenerator</code>で生成したマークダウンをClaude AIに入力する<br>
         - AIが既存のissueを考慮してコミットメッセージを自動生成する<br>
     </p>
   </div>
 </div>

 <div class="timeline_item">
   <div class="time_date">
     <p class="time">リリース後</p>
     <p class="flag">プロジェクトの統合とドキュメント化</p>
   </div>
   <div class="desc">
     <p>
       - <code>SourceSage.py</code>を使用してプロジェクト全体のソースコードとファイル構成をAIが理解しやすい形式で統合する<br>
         - プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめる<br>
         - 不要なファイルやディレクトリを除外するための設定が可能<br>
         - 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供<br>
       - Gitの変更履歴を自動生成し、ドキュメント化する<br>
         - ブランチごとに変更履歴をマークダウンファイルに出力する<br>
         - すべてのブランチの変更履歴を1つのファイルに統合する<br>
     </p>
   </div>
 </div>
</div>
```



```