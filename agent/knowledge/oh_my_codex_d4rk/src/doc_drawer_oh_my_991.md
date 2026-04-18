,
        cursor: result.cursor,
        event: result.event ?? null,
      }));
      return;
    }

    if (result.status === 'timeout') {
      console.log(`No new event for ${name} before timeout (${timeoutMs}ms).`);
      return;
    }

    const event = result.event!;
    const context = [
      `team=${name}`,
      `event=${event.type}`,
      `worker=${event.worker}`,
      event.state ? `state=${event.state}` : '',
      event.prev_state ? `prev=${event.prev_state}` : '',
      event.task_id ? `task=${event.task_id}` : '',
      `cursor=${result.cursor}`,
    ].filter(Boolean).join(' ');
    console.log(context);
    return;
  }