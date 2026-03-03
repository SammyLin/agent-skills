---
name: doc-coauthoring
description: Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks. Do not use for: quick one-off text generation, editing existing .docx files (use docx skill), internal comms like status updates (use internal-comms), or code documentation comments.
---

# Doc Co-Authoring Workflow

A structured workflow for collaborative document creation with three stages: Context Gathering, Refinement & Structure, and Reader Testing.

## When to Offer This Workflow

**Trigger conditions:** User mentions writing docs, drafting proposals, creating specs, PRDs, design docs, decision docs, RFCs, or starting substantial writing tasks.

**Initial offer:** Explain the three stages and ask if they want the structured workflow or freeform.

## Stage 1: Context Gathering

**Goal:** Close the gap between what the user knows and what Claude knows.

1. Ask meta-context questions: doc type, audience, desired impact, template/format, constraints
2. Encourage info dumping (stream-of-consciousness, links to docs/channels)
3. If integrations available, mention they can pull context directly
4. Ask 5-10 clarifying questions based on gaps
5. **Exit when** questions show understanding of edge cases and trade-offs

## Stage 2: Refinement & Structure

**Goal:** Build the document section by section through brainstorming, curation, and refinement.

1. Agree on section structure (suggest 3-5 sections if unclear)
2. Create initial document with placeholders (artifact or markdown file)
3. **For each section:**
   - Ask 5-10 clarifying questions
   - Brainstorm 5-20 options
   - User curates (keep/remove/combine)
   - Gap check
   - Draft using `str_replace`
   - Iterate with surgical edits until satisfied
4. At 80%+ completion, re-read entire doc for flow, consistency, redundancy
5. Final review for coherence before moving to Stage 3

## Stage 3: Reader Testing

**Goal:** Test the document with a fresh Claude (no context) to catch blind spots.

**With sub-agents (Claude Code):** Predict 5-10 reader questions, test with fresh instance, run ambiguity/contradiction checks, fix gaps.

**Without sub-agents (claude.ai):** Guide user to open fresh Claude conversation, paste doc, ask predicted questions, iterate on gaps.

**Exit when** Reader Claude consistently answers correctly without surfacing new gaps.

## Final Review

1. Recommend user's own final read-through
2. Suggest double-checking facts, links, technical details
3. Tips: link conversation in appendix, use appendices for depth, update from reader feedback

## Detailed Reference

For detailed stage instructions, question templates, artifact management guidelines, and tips for handling deviations, see [references/workflow-details.md](references/workflow-details.md).
