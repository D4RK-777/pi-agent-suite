cs/release-notes-0.9.0.md) 및 [릴리스 본문](./docs/release-body-0.9.0.md)을 참고하세요.

## 첫 번째 세션

Codex 내부에서:

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

터미널에서:

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```

## 권장 워크플로

1. `$deep-interview` — 범위나 경계가 아직 모호할 때 먼저 명확히 합니다.
2. `$ralplan` — 정리된 범위를 승인 가능한 아키텍처 및 구현 계획으로 바꿉니다.
3. `$team` 또는 `$ralph` — 승인된 계획을 병렬로 조율해 실행하려면 `$team`, 한 명의 책임자가 끝까지 밀고 검증하려면 `$ralph`를 사용합니다.

## 핵심 모델

OMX는 다음 레이어를 설치하고 연결합니다: