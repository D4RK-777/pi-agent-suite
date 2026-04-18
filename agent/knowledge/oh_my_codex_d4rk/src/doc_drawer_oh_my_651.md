import { createHash } from 'node:crypto';
import { chmodSync, createWriteStream, existsSync, readdirSync } from 'node:fs';
import { copyFile, mkdir, mkdtemp, readFile, readdir, rm, stat } from 'node:fs/promises';
import { homedir, tmpdir } from 'node:os';
import { dirname, extname, join, resolve } from 'node:path';
import { pipeline } from 'node:stream/promises';
import { Readable } from 'node:stream';
import { spawnPlatformCommandSync } from '../utils/platform-command.js';
import { getPackageRoot } from '../utils/package.js';

export type NativeProduct = 'omx-explore-harness' | 'omx-sparkshell';
export type NativeLibc = 'musl' | 'glibc';