# Profile source map and maintenance

Last reviewed: 2026-11-05. This file supports the public [profile README](../README.md). It is a map of repository-backed descriptions, not an independent certification of each project's performance.

## Featured project sources

| Profile entry | Repository evidence | Claim boundary |
| --- | --- | --- |
| VietLex | [README](https://github.com/TanNguyen234/VietLex-Tech-Spec/blob/main/README.md) and linked evaluation reports | Technical evaluation is described; independent legal correctness and full production readiness are not established. |
| AI CV Review | [README](https://github.com/TanNguyen234/CV-Review-System/blob/main/README.md) and backend directory | The repository describes a vanilla-JavaScript browser UI, not a React UI. Avoid unverified deployment/performance claims. |
| FinEvent | [README](https://github.com/TanNguyen234/finevent-nlp-finance/blob/main/README.md), `src/`, `app/`, `tests/`, and `frontend/` | Repository components are identifiable; do not convert their existence into an unverified accuracy or uptime claim. |
| VAIPE-MedGuard | [README](https://github.com/TanNguyen234/vaipe-medguard/blob/main/README.md), `src/`, `notebooks/`, and `tests/` | Medication image research is not equivalent to clinical validation or advice. |
| YouTubeAgents | [README](https://github.com/TanNguyen234/YoutubeAgents/blob/main/README.md), `app/`, `scripts/`, and `tests/` | The source documents pending full provider E2E verification and human publishing gates. Avoid autonomous revenue or production guarantees. |
| NEU Surface Defect Detection | [README](https://github.com/TanNguyen234/NEU-Surface-Defect-Detection/blob/main/README.md), `src/`, `analysis/`, and `runs/` | Workflow and training artifacts are visible; do not imply independent real-world deployment benchmarks. |

## Editing rules

1. Confirm each featured repository exists and review its current default-branch README and implementation before changing the profile description.
2. Distinguish implemented functionality from proposed work, model evaluation, live integration, and production deployment.
3. Keep the profile in ordinary GitHub Flavored Markdown. Prefer headings, lists, tables, and standard links over nested HTML and remote dynamic widgets.
4. Use canonical links that open the correct repository. Preserve spelling of repository names, including `portforlio`.
5. Run `python scripts/validate_profile.py` locally before pushing a README edit. This is a structural check, **not** a guarantee of semantic correctness or GitHub rendering.
6. Review the GitHub profile page visually after pushing; check mobile wrapping and every key project link.
7. Keep profile changes separate from validation/tooling changes in Git history.

## Why no GitHub Actions workflow?

The profile does not need a continuous job to render. Its checker uses only the Python standard library and can be run locally, avoiding scheduled jobs and unnecessary CI quota consumption.
