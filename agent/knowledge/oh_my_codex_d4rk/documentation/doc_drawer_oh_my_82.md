TRUCTIONS_FILE=/path/to/instructions.md omx
```

## チームモード

並列ワーカーが有利な大規模作業にはチームモードを使用します。

ライフサイクル：

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

運用コマンド：

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

重要なルール：中断する場合を除き、タスクが`in_progress`状態の間はシャットダウンしないでください。

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

チームワーカー用のWorker CLI選択：