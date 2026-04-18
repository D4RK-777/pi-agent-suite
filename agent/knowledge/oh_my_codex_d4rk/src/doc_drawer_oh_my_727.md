return answer === "" || answer === "y" || answer === "yes";
  } finally {
    rl.close();
  }
}

function parseSemverTriplet(version: string): [number, number, number] | null {
  const match = version.match(/(\d+)\.(\d+)\.(\d+)/);
  if (!match) return null;
  return [Number(match[1]), Number(match[2]), Number(match[3])];
}

function semverGte(
  version: [number, number, number],
  minimum: readonly [number, number, number],
): boolean {
  if (version[0] !== minimum[0]) return version[0] > minimum[0];
  if (version[1] !== minimum[1]) return version[1] > minimum[1];
  return version[2] >= minimum[2];
}