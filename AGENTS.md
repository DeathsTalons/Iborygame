# Agent instructions: Ibory (iborygame.com)

This repo is the **published** iborygame.com site: the landing pages, translations, and the game itself in `play/`. GitHub Pages serves it as-is.

## Working together: Claude + Gemini (+ Cody)

Two AI agents work on this repo: **Claude** (Anthropic, via Claude Code) and **Gemini** (Google, via Antigravity).
**Cody owns the project and has the final say.** You are teammates: talk to each other in `AI-DISCUSSION.md`.

### Before you start any work
1. `git pull --rebase` first. The other agent may have pushed since you last looked.
2. Read the newest entries at the bottom of `AI-DISCUSSION.md`.
3. Post a **CLAIM** entry saying what you're about to change, **naming the files or areas** (for example `play/index.html: settings menu`), then commit and push it.
   Don't start on something the other agent has claimed and not yet marked **DONE**. Ask in the discussion instead.
4. Discussion entries (CLAIM, REVIEW, DONE and the rest) **always go to `main`**, even while your code is on a `claude/<topic>` or `gemini/<topic>` branch. That way the other agent sees them on the next pull, and merging a feature branch never conflicts in the log. Doc-only commits to `AGENTS.md` and `AI-DISCUSSION.md` are fine on `main`.

### While you work
- Small, focused commits. Start every commit message with `[claude]` or `[gemini]`.
- Never `git push --force`, never rewrite history, never delete a branch you didn't create.
- **`main` is live.** Every push to `main` publishes straight to iborygame.com and to players through GitHub Pages. There is no staging step. Only push to `main` what Cody has asked for.
  For anything else (experiments, refactors, ideas), push a branch named `claude/<topic>` or `gemini/<topic>`
  and post a **REVIEW** entry asking the other agent and Cody to look at it.
- If your work collides with the other agent's (merge conflict, overlapping files), stop and post a **QUESTION**. Never overwrite their work.
- Disagree openly and politely in the discussion. Cody would rather read a real debate than have one of you silently undo the other.

- **Keep a clean working tree between sessions.** Cody's `Latest` folder pulls from GitHub every 30 minutes. Before you stop, commit your work (on your branch if it isn't for `main`) and switch back to `main`, so a background pull never meets uncommitted edits.

### When you finish
Post a **DONE** entry: what changed, the commit hashes or branch, how you tested it, and anything the other agent should review.

### The `last-working` branch
`last-working` is a branch that points at the newest version **Cody has confirmed works**. Cody's PC mirrors it into a "Last Working" folder automatically.
Never commit to it directly. Only move it when Cody confirms a version works, and log it in the discussion:
`git push origin <commit>:last-working` (add `--force-with-lease` only if Cody wants to roll it *back* to an older commit).

## The source lives in a second, private repo: `DeathsTalons/ibory-source`
This repo is the **published output**. The full source is in the **private** repo `DeathsTalons/ibory-source` (same rules: pull first, CLAIM, `[claude]`/`[gemini]` commits, discussion entries go to **this** repo's `AI-DISCUSSION.md`). Its `README.md` explains the layout. In short:

| Thing | In `ibory-source` | What that means |
|---|---|---|
| The game | `ibory-phone/` | This repo's `play/` is a copy of it. Make game changes there; a release copies it to `play/` here. |
| The Caves | `caves/` (`cave_data.js`, `cave_src.js`, `cave_ui.js`, `fighter.js`) | **Never edit `cave.js` by hand.** Run `python3 caves/build_cave.py`, which writes `ibory-phone/cave.js`. |
| The game server | `scores-worker/worker.js` (Cloudflare Worker) | Anyone can edit it, but only Claude can deploy it for now (`tools/deploy-worker.py` needs a key that is never committed). Deploy the server **before** a site release that needs it. |
| Tests | `t/` (browser) and `scores-worker/test-harness/` (server) | Run the ones that touch your change; Claude runs the wider suite before a release. |
| Changelog and developer log | `CHANGELOG.md`, `BUNDLE.md` | Add a changelog line with every player-facing change. `BUNDLE.md` explains why things are the way they are. |
| Translations, website pages, War College tools, store listing | `i18n/`, `website/`, `war-college-tools/`, `play-store/` | **Never copy `war-college-tools/` or the server code into this public repo.** |

**Editing `play/` here directly still works:** before every release Claude folds any `play/` changes since its last release back into `ibory-source`, so nothing gets overwritten. Making the change in `ibory-source/ibory-phone/` is better, though. Don't run `build.py` in this repo; it's for an old layout.

## Release checklist (a new game version going live)
A release is a push to `main` that changes `play/`. **Only when Cody has said to push.**
1. **Pull first** (`git pull --rebase`) and read the bottom of `AI-DISCUSSION.md`, so nobody's work is overwritten.
2. **One version number for everything.** Bump all of these together, to the same `0.2.x`:
   - `play/index.html`: `window.IBORY_V` and `var APP_VERSION`
   - `play/sw.js`: `CACHE` (`ibory-v0.2.x`)
   - the server's `WORKER_VERSION` (Claude), even when the server code didn't change
3. **Cache busting.** Changing `CACHE` in `play/sw.js` is what makes installed phones fetch the new files. `cave.js` and the translations are loaded with `?v=IBORY_V`, so they follow the version too.
   **New art:** any new file under `play/art/` must also be added to `play/art/FILES.json` **and** to the `ART` list in `play/sw.js`, or offline play breaks.
4. **Server first.** If the release needs server changes, deploy the server before pushing the site. If tables or columns were added, the server's `SCHEMA_VER` must change too.
5. **Translations** (`play/lang/*.js`). New or changed English text shows in English until it's translated, so a release never waits on translations. Translation updates go out in later batches.
6. **Test:**
   - phone widths 390px and 360px;
   - the Caves both in landscape and turned sideways on an upright phone;
   - the browser console clean;
   - Claude runs the test suite.
7. **Commit message:** `[claude] 0.2.x: what changed` (or `[gemini] …`), in both repos. Add a player-facing line to `CHANGELOG.md` in `ibory-source`, and push `ibory-source` too.
8. **After pushing, verify it's live.** GitHub Pages takes about a minute. Check that `https://iborygame.com/play/sw.js` shows the new `CACHE` name and that the game opens without console errors. Then post **DONE** with the version and commit.
9. **`last-working`** moves only when Cody confirms the new version works (see above).

### This repo is public
Everything here, including `AI-DISCUSSION.md`, is readable by anyone. Never commit API keys, passwords, `.env` files, emails, or customer details.
