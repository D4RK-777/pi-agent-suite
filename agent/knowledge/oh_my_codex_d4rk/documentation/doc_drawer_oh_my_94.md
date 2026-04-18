hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (플러그인 확장 워크플로우)
omx hud ...        # --watch|--json|--preset
omx help
```

## Hooks 확장 (추가 표면)

OMX는 이제 플러그인 스캐폴딩 및 검증을 위한 `omx hooks`를 포함합니다.

- `omx tmux-hook`은 계속 지원되며 변경되지 않았습니다.
- `omx hooks`는 추가적이며 tmux-hook 워크플로우를 대체하지 않습니다.
- 플러그인 파일은 `.omx/hooks/*.mjs`에 위치합니다.
- 플러그인은 기본적으로 비활성화되어 있으며; `OMX_HOOK_PLUGINS=1`로 활성화합니다.

전체 확장 워크플로우 및 이벤트 모델은 `docs/hooks-extension.md`를 참조하세요.

## 시작 플래그

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # setup 전용
```

`--madmax`는 Codex `--dangerously-bypass-approvals-and-sandbox`에 매핑됩니다.
신뢰할 수 있는/외부 sandbox 환경에서만 사용하세요.

### MCP workingDirectory 정책 (선택적 강화)