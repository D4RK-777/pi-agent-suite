del_instructions_file="//; s/"$//\')',
          '      printf \'instructions-path:%s\\n\' "$file"',
          '      printf \'instructions-start\\n\'',
          '      cat "$file"',
          '      printf \'instructions-end\\n\'',
          '      ;;',
          '  esac',
          'done',
        ].join('\n'),
      );
      await chmod(fakeCodexPath, 0o755);

      const result = runOmx(wd, ['exec', '--model', 'gpt-5', 'say hi'], {
        HOME: home,
        NODE_OPTIONS: '',
        PATH: `${fakeBin}:/usr/bin:/bin`,
        OMX_AUTO_UPDATE: '0',
        OMX_NOTIFY_FALLBACK: '0',
        OMX_HOOK_DERIVED_SIGNALS: '0',
      });