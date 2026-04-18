rt -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Operasyonel komutlar:

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Önemli kural: İptal etmiyorsanız, görevler hâlâ `in_progress` durumundayken kapatmayın.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

Takım çalışanları için Worker CLI seçimi: