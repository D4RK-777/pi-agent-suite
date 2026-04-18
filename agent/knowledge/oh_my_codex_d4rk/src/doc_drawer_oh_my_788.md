interop markers missing: ${missing.join(", ")}`,
      };
    }
    return { ok: true };
  } catch {
    return { ok: false, message: `cannot read ${teamCliPath}` };
  }
}