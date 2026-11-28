# Agent instructions: Ibory (iborygame.com)

This repo is the **published** iborygame.com site: the landing pages, translations, and the game itself in `play/`. GitHub Pages serves it as-is.

## Working together: Claude + Gemini (+ Cody)

Two AI agents work on this repo: **Claude** (Anthropic, via Claude Code) and **Gemini** (Google, via Antigravity).
**Cody owns the project and has the final say.** You are teammates: talk to each other in `AI-DISCUSSION.md`.

### Before you start any work
1. `git pull --rebase` first. The other agent may have pushed since you last looked.
2. Read the newest entries at the bottom of `AI-DISCUSSION.md`.
3. Post a **CLAIM** entry saying what you're about to change, then commit and push it.
   Don't start on something the other agent has claimed and not yet marked **DONE**. Ask in the discussion instead.

### While you work
- Small, focused commits. Start every commit message with `[claude]` or `[gemini]`.
- Never `git push --force`, never rewrite history, never delete a branch you didn't create.
- **`main` is live.** Every push to `main` publishes straight to iborygame.com and to players through GitHub Pages. There is no staging step. Only push to `main` what Cody has asked for.
  For anything else (experiments, refactors, ideas), push a branch named `claude/<topic>` or `gemini/<topic>`
  and post a **REVIEW** entry asking the other agent and Cody to look at it.
- If your work collides with the other agent's (merge conflict, overlapping files), stop and post a **QUESTION**. Never overwrite their work.
- Disagree openly and politely in the discussion. Cody would rather read a real debate than have one of you silently undo the other.

### When you finish
Post a **DONE** entry: what changed, the commit hashes or branch, how you tested it, and anything the other agent should review.

### The `last-working` branch
`last-working` is a branch that points at the newest version **Cody has confirmed works**. Cody's PC mirrors it into a "Last Working" folder automatically.
Never commit to it directly. Only move it when Cody confirms a version works, and log it in the discussion:
`git push origin <commit>:last-working` (add `--force-with-lease` only if Cody wants to roll it *back* to an older commit).

### This repo is public
Everything here, including `AI-DISCUSSION.md`, is readable by anyone. Never commit API keys, passwords, `.env` files, emails, or customer details.
