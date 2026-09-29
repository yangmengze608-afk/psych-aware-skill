# psych-aware

> An always-on psychology mindset for AI agents. Load it once, and every response gets a little quieter, a little more human, and a little closer to what you actually need to do next.
>
> 一个给 AI agent 用的"常驻心理学视角"。加载之后，它不是多了一个工具，而是换了一双看人的眼睛——用户感觉不到术语，只觉得这个 AI 说话让人松一口气、建议踩得准。

English README below · 中文说明在最后。

---

## What it is

`psych-aware` is an [Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — a folder with a `SKILL.md` plus a knowledge base. Once loaded, the agent:

- **Picks up the human layer behind any question** — not just the literal ask, but the emotion, the motivation, the bias underneath.
- **Applies 100 psychology concepts silently** — CBT, ACT/DBT, behavioral economics, social psychology, learning science, motivation research, communication research, positive psychology.
- **Never names the concepts out loud.** The terminology stays internal. The user hears plain language and a concrete next step.

It is *not* a therapy chatbot, a diagnosis engine, or a textbook. It is a tone-of-voice and a reasoning layer.

## What it is NOT

- Not a replacement for a mental health professional.
- Not a prompt library where users manually pick a card.
- Not a list of psychology terms to recite.
- Not dark-pattern persuasion. All techniques exist to help the user see more clearly, not to manipulate them.

## Quick install

Copy this folder into your agent's skills directory:

```bash
# Claude Code / any agent that reads SKILL.md
cp -r psych-aware ~/.claude/skills/

# Or point your agent at this repo's root
```

Restart your session. The skill auto-loads when conversations touch human behavior, decisions, emotion, motivation, learning, relationships, or growth.

## How it works

```
psych-aware/
├── SKILL.md              # The core: behavior rules, tone, routing, guardrails
├── references/           # 100 concept cards the agent consults internally
│   ├── decision-biases.md       (10)  — loss aversion, anchoring, sunk cost…
│   ├── social.md                (10)  — conformity, attribution error, halo…
│   ├── cbt.md                   (10)  — thought records, defusion, exposure…
│   ├── act-dbt.md               (10)  — acceptance, TIPP, opposite action…
│   ├── motivation.md            (10)  — implementation intentions, BJ Fogg…
│   ├── learning.md              (10)  — active recall, spaced repetition…
│   ├── emotion-regulation.md     (10)  — physiological sigh, urge surfing…
│   ├── communication.md         (10)  — NVC, Gottman repair, boundaries…
│   ├── growth-positive.md       (10)  — three good things, flow, values…
│   └── personality-development.md(10) — attachment, locus of control…
└── examples/              # Few-shot dialogues showing the right tone
```

The agent reads `SKILL.md` on load, then opens only the reference file that matches the user's current state (lazy-loaded, so context stays small).

## The design rule everything hangs on

**Internal jargon, plain output.**

- The agent may think "this is catastrophizing plus availability bias."
- It may **never** say those words to the user.
- It translates the mechanism into one concrete, human action: *"Write down three things you already know, then just read one section for 25 minutes."*

If the user can name the psychology concept the agent just used, the agent failed.

## Guardrails (hard-coded in SKILL.md)

- No diagnosis, no medication advice, no "should you go off your meds."
- Suicidal / self-harm / harm-to-others signals → immediately route to emergency hotlines, drop the role-play.
- Never use these techniques to persuade or nudge the user into something they don't want.
- Normal human struggles (exam anxiety, procrastination, arguments) are framed as ordinary, not pathological.

## Contributing

The 100 cards are a starting set. PRs welcome:

- Add a missing concept to the right `references/*.md` file (follow the existing card format).
- Add a dialogue example to `examples/`.
- Fix tone, tighten wording, translate.

Please keep the **脱术语 / plain-output** rule: examples must read like a friend talking, not a textbook.

---

## 中文说明

这个仓库做一件事：**让 AI agent 在任何对话里都自然地带一点心理学视角，但不拽术语**。

- 你问代码报错，它照样直接给答案，只多一句"别急，这种错改完就过"。
- 你说"明天考试感觉要凉"，它不讲课，只让你写下已经会的三件事、看 25 分钟一节、起来喝口水。
- 你跟对象吵架，它先让你别发那条消息，再把"你总是不回我"换成"我有点慌，你看到时回我一个表情就好"。

`references/` 里的 100 个概念是它的内功心法，不对你暴露。目录分类、安装方式、护栏规则和英文 README 一致。

### 伦理声明
本项目仅用于教育与自我提升目的，**不构成心理诊断、治疗或医疗建议**。如果你正在经历持续的情绪困扰、自伤或自杀念头，请立即联系当地心理援助热线或专业医生。技术的目的是帮你看清自己，不是替代专业帮助。

## License

[MIT](./LICENSE)
