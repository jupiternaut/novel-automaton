# Yaonv Kanzhao / 妖女看招 — local LightRAG fork

This repository preserves the LightRAG implementation used on liekkas for chapter ingestion, graph extraction, evidence retrieval and a read-only MCP adapter. The initial publication was source-only. A subsequent user-authorized data snapshot is now included at [novel-data/yaonvkanzhao](novel-data/yaonvkanzhao/README.md); it is not a backup of running processes, credentials or the host environment.

## Provenance

- Upstream: https://github.com/HKUDS/LightRAG
- Original local base: `e5866e64ceb9e935f009fa7fe8e3eebc12225c51`. Publication retains this source baseline and its attribution, but intentionally publishes a new root snapshot rather than upstream history. A scan of 24,070 historical/staged blobs found credential-shaped hardcoded values in old upstream commits; those objects are not included in the published history. The original checkout and the local historical copy remain intact. Publication did not upgrade the working tree to the latest upstream.
- Source directory: `/home/grf/.gemini/antigravity/scratch/LightRAG` on liekkas (192.168.6.201).
- Publishing copy: `/home/grf/Documents/yaonvkanzhao-lightrag-publish-20260922`.
- Git workflow: `grf/skill`, commit `557b17653d75b5aca60c874b56f8c0731a86a930`, package `git-evolution-workflow` v1.2.0. All 15 installed package files matched the repository copy when checked.
- Existing upstream license and attribution are retained.

## Included changes

- Bounded extraction-ahead / merge queue changes in `lightrag/pipeline.py`, the design contract, and regression tests.
- `local/`: ingestion, recovery, progress monitoring, local embeddings/reranking, evidence retrieval, complete source-map pagination, and read-only stdio MCP.
- Chapter scope checks, page-aligned references, and separate character-based source pagination from the subsequent Antigravity fixes.
- Cursor MCP configuration for this specific host, a retry unit template, and a citations-first prompt.

## Data and deployment boundary

The user-authorized `novel-data/yaonvkanzhao` snapshot includes chapter sources, graph/vector/KV stores, extraction results and source maps. Runtime logs, checkpoints, model weights, environments, secrets and host credentials remain excluded. `local/processed-before-queue-fix.json` is intentionally omitted. The live data remains untouched; the included restore utility verifies and reconstructs the archived dataset into a new directory.

The `.cursor/mcp.json` and service template retain explicit liekkas paths. They contain no credentials but require review before reuse elsewhere. The separate MiroFish/Cursor gateway, OAuth session, model services and installed systemd configuration are external dependencies, not deployed by Git push. `local/README.md` contains historical service observations; do not treat them as a live health check.

See `local/CURSOR_MCP.md` for the adapter. MCP STDIO is distinct from the LightRAG REST URL. Secrets must be provided locally, never committed. Do not run `local/write_env.py` blindly against an existing configured service.

## Evidence quality limits

The source collection was 210 numbered chapters plus an introduction and author notices (212 files). Completed ingestion is not proof of source correctness. Inspection found abrupt truncation and unrelated material in chapters 209–210, and suspicious entities in the graph. The extent of contamination is not fully audited. Do not treat this graph as verified novel canon or resume the story from an unverified ending.

The underlying graph is undirected. Relationships are retrieval clues, not causal proof. Full source maps can exceed the references retained on graph nodes. Chapter filtering limits returned evidence; it does not establish what an individual character knew. Writing targets must stay explicitly identified as 妖女看招, not the unrelated 空城 project.

## Validation

See `local/PUBLICATION_VALIDATION.md` for the current publication checks. No runtime services were restarted and no novel ingestion was triggered by this publication.
