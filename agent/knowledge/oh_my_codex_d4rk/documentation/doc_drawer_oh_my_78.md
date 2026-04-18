/release-notes-0.9.0.md) と [リリース本文](./docs/release-body-0.9.0.md) を参照してください。

## 最初のセッション

Codex内部で：

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

ターミナルから：

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```

## 推奨ワークフロー

1. `$deep-interview` — スコープや境界がまだ曖昧なときに明確化するために使います。
2. `$ralplan` — 明確になった内容を、承認可能なアーキテクチャ/実装計画に落とし込みます。
3. `$team` または `$ralph` — 承認済みプランを並列で進めるなら `$team`、1 人の担当者が完了と検証まで粘り強く進めるなら `$ralph` を使います。

## コアモデル

OMXは以下のレイヤーをインストールして接続します：