ecommendedInspectTargets[0]!] ? `cli=${recommendedInspectClis[recommendedInspectTargets[0]!]}` : '',
      recommendedInspectRoles[recommendedInspectTargets[0]!] ? `role=${recommendedInspectRoles[recommendedInspectTargets[0]!]}` : '',
      typeof recommendedInspectAlive[recommendedInspectTargets[0]!] === 'boolean' ? `alive=${recommendedInspectAlive[recommendedInspectTargets[0]!]}` : '',
      typeof recommendedInspectTurnCounts[recommendedInspectTargets[0]!] === 'number' ? `turn_count=${recommendedInspectTurnCounts[recommendedInspectTargets[0]!]}` : '',
      typeof recommendedInspectTurnsWithoutProgress[recommendedInspectTargets[0]!] === 'number'
        ? `turns_without_progress=${recommendedInspectTurnsWithoutProgress[recommendedInspectTargets[0]!]}` : '',