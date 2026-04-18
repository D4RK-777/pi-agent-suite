await io.question(`${prompt}${suffix}\n> `);
  return answer.trim() || currentValue?.trim() || '';
}

async function promptAction(io: AutoresearchQuestionIO, launchReady: boolean): Promise<'launch' | 'refine'> {
  const answer = (await io.question(`\nNext step [launch/refine further] (default: ${launchReady ? 'launch' : 'refine further'})\n> `)).trim().toLowerCase();
  if (!answer) {
    return launchReady ? 'launch' : 'refine';
  }
  if (answer === 'launch') {
    return 'launch';
  }
  if (answer === 'refine further' || answer === 'refine' || answer === 'r') {
    return 'refine';
  }
  throw new Error('Please choose either "launch" or "refine further".');
}