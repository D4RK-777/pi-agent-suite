rns_without_progress=${recommendedInspectTurnsWithoutProgress[recommendedInspectTargets[0]!]}` : '',
      recommendedInspectReasons[recommendedInspectTargets[0]!] ? `reason=${recommendedInspectReasons[recommendedInspectTargets[0]!]}` : '',
      recommendedInspectStates[recommendedInspectTargets[0]!] ? `state=${recommendedInspectStates[recommendedInspectTargets[0]!]}` : '',
      recommendedInspectTasks[recommendedInspectTargets[0]!] ? `task=${recommendedInspectTasks[recommendedInspectTargets[0]!]}` : '',
      recommendedInspectSubjects[recommendedInspectTargets[0]!] ? `subject=${recommendedInspectSubjects[recommendedInspectTargets[0]!]}` : '',
      recommendedInspectCommand ? `command=${recommendedInspectCommand}` : '',
    ]
      .filter(Boolean)
      .join(' ')
      .trim()