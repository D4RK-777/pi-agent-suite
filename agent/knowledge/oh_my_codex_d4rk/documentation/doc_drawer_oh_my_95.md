pprovals-and-sandbox`에 매핑됩니다.
신뢰할 수 있는/외부 sandbox 환경에서만 사용하세요.

### MCP workingDirectory 정책 (선택적 강화)

기본적으로 MCP state/memory/trace 도구는 호출자가 제공한 `workingDirectory`를 수락합니다.
이를 제한하려면 허용된 루트 목록을 설정하세요:

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

설정 시 이 루트 외부의 `workingDirectory` 값은 거부됩니다.

## Codex-First 프롬프트 제어

기본적으로 OMX는 다음을 주입합니다:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

이것은 `CODEX_HOME`의 `AGENTS.md`와 프로젝트 `AGENTS.md`(있는 경우)를 병합한 뒤 런타임 오버레이를 추가합니다.
Codex 동작을 확장하지만, Codex 핵심 시스템 정책을 대체/우회하지 않습니다.

제어:

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # AGENTS.md 주입 비활성화
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## 팀 모드

병렬 워커가 유리한 대규모 작업에 팀 모드를 사용합니다.

라이프사이클: